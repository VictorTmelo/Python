import tkinter as tk
import random

from Grafos import Grafo


class Application:
    options = [
        "Busca em Largura",
        "Busca em Profundidade",
        "Busca de Custo Uniforme",
        "Busca Gulosa por Melhor Escolha",
        "Busca A Estrela"
    ]

    def __init__(self):

        '''This class configures and populates the toplevel window.
                           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        self.elementos = []
        self.obstaculosIndex = []
        self.cliques = 0
        self.origem = 0
        self.destino = 0
        self.grafo = None

        self.root = tk.Tk(className="Algortimos de Busca")
        self.root.geometry("650x250")
        self.root.geometry("1124x561+375+259")
        self.root.minsize(120, 1)
        self.root.maxsize(4484, 1061)
        self.root.resizable(1, 1)
        self.root.title("Algoritmos de Busca")
        self.root.configure(background="#d9d9d9")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(self.root)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=0.986, relwidth=0.186)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(padx="20")
        self.Frame1.configure(pady="20")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.335, rely=0.018, height=21, width=56)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Linhas:''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.335, rely=0.127, height=21, width=60)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Colunas:''')

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.335, rely=0.072, height=20, relwidth=0.402)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(justify='center')
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.335, rely=0.181, height=20, relwidth=0.402)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(justify='center')
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")

        self.check = tk.IntVar()
        self.Checkbutton1 = tk.Checkbutton(self.Frame1, variable=self.check)
        self.Checkbutton1.place(relx=0.335, rely=0.253, relheight=0.045
                                , relwidth=0.292)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Pesos''')

        self.clicked = tk.StringVar()
        self.clicked.set(self.options[0])
        self.drop = tk.OptionMenu(self.Frame1, self.clicked, *self.options)
        self.drop.place(relx=0.080, rely=0.344, relheight=0.060, relwidth=0.900)
        self.drop.configure(background="#d9d9d9")

        self.RunButton = tk.Button(self.Frame1)
        self.RunButton.place(relx=0.335, rely=0.48, height=35, width=70)
        self.RunButton.configure(activebackground="#ececec")
        self.RunButton.configure(activeforeground="#000000")
        self.RunButton.configure(background="#32CD32")
        self.RunButton.configure(compound='center')
        self.RunButton.configure(disabledforeground="#a3a3a3")
        self.RunButton.configure(foreground="#000000")
        self.RunButton.configure(highlightbackground="#d9d9d9")
        self.RunButton.configure(highlightcolor="black")
        self.RunButton.configure(pady="0")
        self.RunButton.configure(text='''Gerar Grafo''')
        self.RunButton.configure()
        self.RunButton["command"] = self.iniciar

        self.ResetButton = tk.Button(self.Frame1)
        self.ResetButton.place(relx=0.335, rely=0.58, height=35, width=70)
        self.ResetButton.configure(activebackground="#ececec")
        self.ResetButton.configure(activeforeground="#000000")
        self.ResetButton.configure(background="#1E90FF")
        self.ResetButton.configure(compound='center')
        self.ResetButton.configure(disabledforeground="#a3a3a3")
        self.ResetButton.configure(foreground="#000000")
        self.ResetButton.configure(highlightbackground="#d9d9d9")
        self.ResetButton.configure(highlightcolor="black")
        self.ResetButton.configure(pady="0")
        self.ResetButton.configure(text='''Limpar''')
        self.ResetButton.configure()
        self.ResetButton["command"] = self.reset

        self.RestartButton = tk.Button(self.Frame1)
        self.RestartButton.place(relx=0.335, rely=0.68, height=35, width=70)
        self.RestartButton.configure(activebackground="#ececec")
        self.RestartButton.configure(activeforeground="#000000")
        self.RestartButton.configure(background="#DC143C")
        self.RestartButton.configure(compound='center')
        self.RestartButton.configure(disabledforeground="#a3a3a3")
        self.RestartButton.configure(foreground="#000000")
        self.RestartButton.configure(highlightbackground="#d9d9d9")
        self.RestartButton.configure(highlightcolor="black")
        self.RestartButton.configure(pady="0")
        self.RestartButton.configure(text='''Reiniciar''')
        self.RestartButton.configure()
        self.RestartButton["command"] = self.reiniciar

        self.LabelTamanho = tk.Label(self.Frame1)
        self.LabelTamanho.place(relx=0.00001, rely=0.82)
        self.LabelTamanho.configure(activebackground="#f9f9f9")
        self.LabelTamanho.configure(activeforeground="black")
        self.LabelTamanho.configure(background="#d9d9d9")
        self.LabelTamanho.configure(disabledforeground="#a3a3a3")
        self.LabelTamanho.configure(foreground="#000000")
        self.LabelTamanho.configure(highlightbackground="#d9d9d9")
        self.LabelTamanho.configure(highlightcolor="black")
        self.LabelTamanho.configure(text='''Tamanho do Caminho:''')
        self.LabelTamanho.place_forget()

        self.LabelPeso = tk.Label(self.Frame1)
        self.LabelPeso.place(relx=0.00001, rely=0.90)
        self.LabelPeso.configure(activebackground="#f9f9f9")
        self.LabelPeso.configure(activeforeground="black")
        self.LabelPeso.configure(background="#d9d9d9")
        self.LabelPeso.configure(disabledforeground="#a3a3a3")
        self.LabelPeso.configure(foreground="#000000")
        self.LabelPeso.configure(highlightbackground="#d9d9d9")
        self.LabelPeso.configure(highlightcolor="black")
        self.LabelPeso.configure(text='''Peso do Caminho:''')
        self.LabelPeso.place_forget()

        self.LabelSize = tk.Label(self.Frame1)
        self.LabelSize.place(relx=0.860, rely=0.82)
        self.LabelSize.configure(activebackground="#f9f9f9")
        self.LabelSize.configure(activeforeground="black")
        self.LabelSize.configure(background="#d9d9d9")
        self.LabelSize.configure(disabledforeground="#a3a3a3")
        self.LabelSize.configure(foreground="#000000")
        self.LabelSize.configure(highlightbackground="#d9d9d9")
        self.LabelSize.configure(highlightcolor="black")
        self.LabelSize.configure(text='''''')
        self.LabelSize.place_forget()

        self.LabelWeight = tk.Label(self.Frame1)
        self.LabelWeight.place(relx=0.730, rely=0.90)
        self.LabelWeight.configure(activebackground="#f9f9f9")
        self.LabelWeight.configure(activeforeground="black")
        self.LabelWeight.configure(background="#d9d9d9")
        self.LabelWeight.configure(disabledforeground="#a3a3a3")
        self.LabelWeight.configure(foreground="#000000")
        self.LabelWeight.configure(highlightbackground="#d9d9d9")
        self.LabelWeight.configure(highlightcolor="black")
        self.LabelWeight.configure(text='''''')
        self.LabelWeight.place_forget()

        self.Frame2 = None

        self.setFrame2()

        self.root.mainloop()

    def iniciar(self):
        for i in self.Frame2.grid_slaves():
            i.destroy()

        self.setFrame2()

        self.elementos = []
        self.obstaculosIndex = []

        self.linhas = int(self.Entry1.get())
        self.colunas = int(self.Entry2.get())

        peso = int(self.check.get())

        for i in range(0, self.linhas):
            colunasAux = []
            tk.Grid.rowconfigure(self.Frame2, i, weight=1)
            for j in range(0, self.colunas):
                randomNumber = random.randint(0, 5)
                tk.Grid.columnconfigure(self.Frame2, j, weight=1)
                if randomNumber == 3:
                    aux = tk.Button(self.Frame2)
                    aux.configure(bg="black")
                    aux['state'] = 'disabled'
                    self.obstaculosIndex.append([i, j])
                else:
                    aux = tk.Button(self.Frame2, command=lambda x=i, y=j: self.clicado(x, y))

                aux.grid(row=i, column=j, sticky="news")
                colunasAux.append(aux)

            self.elementos.append(colunasAux)

        self.reset()

        # Criar grafo

        self.grafo = Grafo(self.linhas, self.colunas, peso, self.elementos)

    def clicado(self, x, y):
        self.cliques += 1

        if len(self.elementos) > 0:
            if self.cliques == 1:
                self.origem = y + (x * self.colunas)
                self.elementos[x][y].configure(bg="yellow")
                self.elementos[x][y]['state'] = 'disabled'
            if self.cliques == 2:
                self.destino = y + (x * self.colunas)
                self.elementos[x][y].configure(bg="red")
                self.elementos[x][y]['state'] = 'disabled'

                for i in self.elementos:
                    for j in i:
                        j['state'] = 'disabled'

                metodo = self.clicked.get()

                resultado = None

                if metodo == self.options[0]:
                    resultado = self.grafo.bl(self.origem, self.destino)
                elif metodo == self.options[1]:
                    resultado = self.grafo.bp(self.origem, self.destino)
                elif metodo == self.options[2]:
                    resultado = self.grafo.bcu(self.origem, self.destino)
                elif metodo == self.options[3]:
                    resultado = self.grafo.bgme(self.origem, self.destino, [x, y])
                elif metodo == self.options[4]:
                    resultado = self.grafo.aStar(self.origem, self.destino, [x, y])

                if resultado is not None:
                    if type(resultado) is not tuple:
                        self.LabelSize.configure(text=f'''{resultado}''')
                        self.LabelTamanho.place(relx=0.00001, rely=0.82)
                        self.LabelSize.place(relx=0.860, rely=0.82)
                    else:
                        self.LabelSize.configure(text=f'''{resultado[0]}''')
                        self.LabelTamanho.place(relx=0.00001, rely=0.82)
                        self.LabelSize.place(relx=0.860, rely=0.82)

                        self.LabelWeight.configure(text=f'''{resultado[1]}''')
                        self.LabelPeso.place(relx=0.00001, rely=0.90)
                        self.LabelWeight.place(relx=0.730, rely=0.90)


    def reset(self):
        self.LabelTamanho.place_forget()
        self.LabelPeso.place_forget()
        self.LabelSize.place_forget()
        self.LabelWeight.place_forget()

        self.cliques = 0

        for i in range(0, self.linhas):
            for j in range(0, self.colunas):
                if [i, j] not in self.obstaculosIndex:
                    self.elementos[i][j]['state'] = 'normal'
                    self.elementos[i][j].configure(bg='SystemButtonFace')

    def reiniciar(self):
        self.root.destroy()
        self.__init__()

    def setFrame2(self):
        self.Frame2 = tk.Frame(self.root)
        self.Frame2.place(relx=0.187, rely=0.0, relheight=0.991, relwidth=0.814)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")