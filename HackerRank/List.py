if __name__ == '__main__':
    N = int(input())

    list = []

    list.insert(0, 5)
    list.insert(1, 10)
    list.insert(0, 6)

    print(list)

    list.remove(6)
    list.append(9)
    list.append(1)

    list.sort()

    print(list)

    list.pop()

    list.reverse()

    print(list)