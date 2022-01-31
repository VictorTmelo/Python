def fatorial_recursivo(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1 or x == 0:
        return 1
    else:
        return (x * fatorial_recursivo(x-1))


def fatorial_iterativo(x):

    fat = x
    i = x -1

    while i >= 1:

        fat *= i
        i -= 1

    return fat

