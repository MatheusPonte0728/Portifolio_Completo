# int(Inteiro) - números inteiros
# float(Flutuante) - números quebrados
# bool(Booleano) - valores lógicos
# str(string) - caracteres


n1 = int(input('Digite um número '))
n2 = int(input('igite mais um número '))
s = n1 + n2
print ('A soma de de {} + {} é: {}'.format(n1, n2, s))

x = input('Digite algo: ')
print('É numerico?', x.isalnum())
print('É alfabético?', x.isalpha())
print('É decimal?', x.isdecimal())
print('Esta minusculo?', x.islower())
print('Esta maiusculo?', x.isupper())
print('É somente espaços?', x.isspace())
