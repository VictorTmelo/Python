from Matematica.FatorialRecursivo import fatorial_recursivo, fatorial_iterativo

if __name__ == '__main__':

    num = int(input("Digite o numero: "))

    print(f"o fatorial de {num} é igual a {fatorial_recursivo(num)}" , "- metodo recursivo")
    print(f"o fatorial de {num} é igual a {fatorial_iterativo(num)} " + "- metodo iterativo")