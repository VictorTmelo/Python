#!/usr/bin/env python
credits = """
mp3p by Remco Gerlich, this code is public domain

This is yet another mpg123 frontend. Do not fear, there won't be yet another
sourceforge page for this one, this is just the thingy I use for myself, and
Useless Python wants to host that sort of code ;).

It's a wxPython GUI that runs mpg123 in a thread. It does what I want a
mp3 player to do, that is:
- I have a directory ~/mp3/ with mp3s.
- I have a directory ~/playlist/ with symlinks to the things in ~/mp3/ that
  the player should choose from.
- By default the player plays randomly.
- It's possible to put some songs in the queue, so that the player plays those
  first before it goes back to random play.
- The QueueDir button makes it possible to place a whole directory in the queue
  at once (a CD, for instance).
- 'Next' goes to the next song - rigorously. It actually runs 'killall mpg123'.
  (evil grin)

It depends on those directories, the mp3 is played with the 'mpg123 -q'
command, and stopped with 'killall mpg123'. That's the things that need porting
if you want to run it on some place without mpg123 or killall.

Things that are not so good:
- The function 'expand_list' below is pretty convoluted, that was the first
  time I got to play with list comprehensions
- There is no scroll bar in the queue list because I couldn't get the text
  control to resize smoothly horizontally. So I just made it far too big. The
  scroll-bar is a few meters to the right.
- 'killall mpg123' is really horrible overkill for a Next button :)
- After closing the window, the current song will go on. I couldn't get
  methods like OnClose to work.

I like the threading stuff with the semaphore.
"""

import sys, os, threading, random
from wxPython.wx import *

playlistdir = os.environ['HOME'] + '/playlist/'  # Dir for random mp3s to play


def expand_list(l):
    # l is a list of files and directories. expand_list expands the
    # directories into their contents and keeps only the .mp3 files.
    dirs = [os.path.abspath(d) for d in l
            if os.path.isdir(d)]
    mp3s = [os.path.abspath(f) for f in l
            if os.path.isfile(f)
            if f.endswith('.mp3')]
    for d in dirs:
        listdir = [os.path.abspath(d + '/' + x) for x in os.listdir(d)]
        dirs += filter(os.path.isdir, listdir)
        mp3s += [x for x in listdir
                 if x.endswith('.mp3')
                 if os.path.isfile(x)]
    return mp3s


class MP3PFrame(wxFrame):
    """MP3PFrame inherits wxFrame
    This is where all the GUI stuff is defined, and where the state of the
    rest of the player is kept, like the currently running mpg123 thread
    and the song queue. This is almost the whole program, in short."""

    # First the initialization

    def __init__(self):
        wxFrame.__init__(self, NULL, -1, "All yuor mp3 are... never mind", size=wxSize(400, 100))

        # Status bar
        self.CreateStatusBar()
        self.SetStatusText("Nothing playing yet")

        # If there were command line args, add them to the queue
        if len(sys.argv) > 1:
            self.queue = expand_list(sys.argv[1:])
        else:
            self.queue = []

        # We need a semaphore because different threads change the queue
        self.queue_semaphore = threading.Semaphore()

        self.mainbox = wxBoxSizer(wxVERTICAL)
        self.buttonbox = wxBoxSizer(wxHORIZONTAL)
        self.mainbox.Add(self.buttonbox, 0)

        self.queuelist = wxTextCtrl(self, 5, style=wxTE_MULTILINE | wxTE_READONLY,
                                    size=wxSize(1000, 100))
        self.queuebox = wxBoxSizer(wxHORIZONTAL)
        self.queuebox.Add(self.queuelist, 0, wxALL | wxEXPAND | wxGROW)
        self.mainbox.Add(self.queuebox, 1)

        self.buttonbox.Add(wxButton(self, 10, "Next"), 1, wxEXPAND | wxALL)
        EVT_BUTTON(self, 10, self.NextButton)

        # 'Queue' button
        self.buttonbox.Add(wxButton(self, 20, "Queue"), 1, wxEXPAND | wxALL)
        EVT_BUTTON(self, 20, self.QueueButton)

        # 'DirQueue' button
        self.buttonbox.Add(wxButton(self, 30, "DirQueue"), 1, wxEXPAND | wxALL)
        EVT_BUTTON(self, 30, self.DirQueueButton)

        self.SetAutoLayout(true)
        self.SetSizer(self.mainbox)

        # Start playing!
        self.mp3thread = threading.Thread(target=self.mp3play)
        self.mp3thread.start()

    def NextButton(self, event):
        # Crudest possible way, pretty horrible, but works well
        os.system("killall mpg123")

    def QueueButton(self, event):
        self.queueDialog = wxFileDialog(self, "Choose a file",
                                        style=wxOPEN | wxMULTIPLE, defaultDir=playlistdir)
        self.queueDialog.ShowModal()
        self.add_to_queue(self.queueDialog.GetPaths())
        self.queueDialog.Destroy()

    def DirQueueButton(self, event):
        self.queueDialog = wxDirDialog(self, "Choose a file",
                                       style=wxOPEN | wxMULTIPLE, defaultPath=playlistdir)
        self.queueDialog.ShowModal()
        self.add_to_queue([self.queueDialog.GetPath()])
        self.queueDialog.Destroy()

    # End of GUI stuff, this is the playing stuff

    def pop_queue(self):
        # Return the first song from the queue, or a random mp3 if it is empty
        self.queue_semaphore.acquire()
        if not self.queue:
            mp3s = expand_list([playlistdir])
            m = mp3s[random.randrange(0, len(mp3s))]
        else:
            m = self.queue.pop(0)
            # Construct a new string for the queue dialog
            s = ""
            for i in range(len(self.queue)):
                s += "%2d. %s\n" % (i + 1, os.path.basename(self.queue[i]))
                self.queuelist.SetValue(s)
        self.queue_semaphore.release()
        self.SetStatusText(os.path.basename(m))
        return m

    def add_to_queue(self, l):
        l = expand_list(l)
        l.sort()
        self.queue_semaphore.acquire()
        self.queue.extend(l)
        s = ""
        for i in range(len(self.queue)):
            s += "%d. %s\n" % (i + 1, os.path.basename(self.queue[i]))
        self.queuelist.SetValue(s)
        self.queue_semaphore.release()

    def mp3play(self):
        """mp3play()
        This function runs in its own thread. It gets an mp3 from pop_queue()
        and plays it, repeat until the main window is gone."""

        while self.IsShown():
            mp3file = self.pop_queue()
            # Quote ' characters so the shell isn't confused
            os.system("mpg123 -q '%s'" % mp3file.replace("'", "\\'"))


class MP3PApp(wxApp):
    # Almost empty, standard, MP3PFrame does everything
    def OnInit(self):
        self.frame = MP3PFrame()
        self.frame.Show(true)
        self.SetTopWindow(self.frame)
        return true


def main():
    app = MP3PApp()
    app.MainLoop()


if __name__ == '__main__':
    main()





