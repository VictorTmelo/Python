nome = input("Qual teu nome ?")

"""
#print("Bem vindo " + (ou ,) nome)

"""

print("Bem vindo {}".format(nome).upper())

dia = input()

mes = input()

ano = input()

print(dia + '/' + mes + '/' + ano)

num1 = int(input())

num2 = int(input())

print("a Soma entre {} e {} = ".format(num1, num2) , (num1 + num2))

#tipo da variavel
print("Tipo da variavel: " , type(num1), end = " ")

#é numerico ?
print("nome É numerico: " , nome.isnumeric())

#ta em maiusculo ?
print(nome.isupper())

#ta em minusculo ?
print(nome.islower())
