# questao 1
'''
a = int (input('Digite um número inteiro. '))
print (a)
'''

# questao 2
'''
num1 = int (input('Digite o primeiro número. '))
num2 = int (input('Digite o segundo número. '))
num3 = int (input('Digite o ultimo número. '))

print (f'A soma de num1 + num2 + num3 é {num1 + num2 + num3}')
'''

# questao 3
'''
num1 = int (input('Digite um número. \n'))

print (f'{num1 - 1 } é o antecessor do seu numero e {num1 + 1} é o sucessor dele.')
'''

# questao 4
'''
celsius = float (input('Qual a temperatura em Celsius? \n'))

F = celsius * (9 / 5) + 32

print (f'A temperatura Celsius convertida em Fahrenheit é {F}')
'''

# questao 5
'''
kmh = float (input('Qual a velocidade em km/h? \n'))

ms = kmh / 3.6

print (f'A velocidade em km/h convertida em m/s é {ms:.2f}')
'''

# questao 6
'''
nota1 = float (input('Qual a primeira nota? \n'))
nota2 = float (input('Qual a segunda nota? \n'))
nota3 = float (input('Qual a terceira nota? \n'))
nota4 = float (input('Qual a última nota? \n'))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média das quatro notas é {media}') 
'''

# questao 7
'''
real = float (input('Qual o valor em Real a ser convertido? \n'))
dolar = float (input ('Qual a cotação atual do Dolar? \n'))

DOLAR = real * dolar
print (f'O valor convertido em Dolar é ${DOLAR}')
'''

# questao 8
'''
raio = 8
PI = 3.141592

area = PI * (raio ** 2)

print(f'A área do círculo é igual a {area:.2f}')
'''

# questao 9
'''
TOTAL = 780000
ganhador1 = 780000 * 0.46
ganhador2 = 780000 * 0.32
ganhador3 = 780000 - ganhador1 - ganhador2

print(f'O primeiro ganhador recebeu R${ganhador1}, o segundo ganhador recebeu R${ganhador2} e o terceiro ganhador recebeu R${ganhador3}')
'''

# questao 10
'''
num = float (input('Digite um número. \n'))

if num > 0:
    quad = num ** 2 
    print (f'Seu número ao quadrado é {quad}')

    raiz = num ** 1/2
    print (f'A raiz quadrada do seu número é {raiz}')

else:
    print ('NÃO É POSITIVO')
'''

# questao 11
'''
num = int(input('Digite um número. \n'))

if num > 0:
    print ('Esse número é positivo', end='')
    if num % 2 == 0:
        print (' e par.')
    if num % 2 != 0:
        print (' e ímpar.')

elif num < 0:
    print ('Esse número é negativo', end='')
    if num % 2 == 0:
        print (' e par.')
    if num % 2 != 0:
        print (' e impar.')

else:
    print('Esse número é par e neutro') 
'''

# questao 12
'''
n1 = float (input('Qual a nota 1? \n'))
n2 = float (input('Qual a nota 2? \n'))

if 0.0 < n1 < 10.0 and 0.0 < n2 < 10.0:
    media = (n1 + n2) / 2
    print (f'A média das duas notas é {media}')

else:
    print ('AS NOTAS NAO SAO VALIDAS.') 
'''

# questao 13
'''
sexo = input('Qual seu sexo: feminino ou masculino? \n')
h = float(input('Qual sua altura? \n'))

if sexo == 'feminino':
    peso = (62.1 * h) - 44.7
    print (f'Seu peso ideal é {peso:.2f}kg')

elif sexo == 'masculino':
    peso = (72.7 * h) - 58
    print (f'Seu peso ideal é {peso:.2f}kg')

else:
    print ('ERRO')
'''

# questao14
'''
trabalho = float (input('Qual a nota do seu trabalho? '))
avaliacao = float (input('Qual a nota da sua avaliação? '))
exame = float (input('Informe a nota do seu exame. '))

media = (trabalho * 2 + avaliacao * 3 + exame * 5) / 10

if  media < 3:
    print('REPROVADO')
elif media < 5:
    print ('RECUPERACAO')
else:
    print ('APROVADO')
'''

# questao15 
'''
print ('Responda sim ou nao para as seguintes perguntas: ')

q1 = input('Telefonou para a vítima? ')
q2 = input('Esteve no local do crime? ')
q3 = input('Mora perto da vítima? ')
q4 = input('Devia para a vítima? ')
q5 = input('Já trabalhou com a vítima? ')

resultado = 0

if q1 == 'sim':
    resultado += 1
if q2 == 'sim':
    resultado += 1
if q3 == 'sim':
    resultado += 1
if q4 == 'sim':
    resultado += 1
if q5 == 'sim':
    resultado += 1
else:
    resultado += 0

if resultado == 2:
    print('SUSPEITA!')
elif resultado == 3 or resultado == 4:
    print ('CÚMPLICE!')
elif resultado == 5:
    print ('ASSASSINO!')
else:
    print ('INOCENTE!')
'''

# questao 16
'''
idade = int(input('Ola, informe sua idade: '))
tempo = int(input('Qual seu tempo de serviÇo? '))

if idade >= 65 or tempo >= 30 or idade >= 60 and tempo >= 25:
    print ('VOCÊ PODE SE APOSENTAR.')

else:
    print('VOCÊ AINDA NÃO PODE SE APOSENTAR.') 
'''

# questao 17
'''
distancia = int (input('Qual a distancia em KM? '))
litros = int (input('Quantos litros de gasolina foram consumidos para percorrer essa distância? '))

consumo = distancia / litros

if consumo < 8:
    print ('VENDA O CARRO!')

elif 8 <= consumo <= 12:
    print ('ECONÔMICO!')

else:
    print ('SUPER ECONÔMICO!')
'''

# questao 18
'''
for i in range (1, 100 + 1):
    print (i)
'''
'''
i = 0
while i < 100:
    i += 1
    print (i)
'''

# questao 19
'''
soma = 0

for i in range (10):
    num = int (input('Digite um numero. '))
    soma += num

print (f' A soma dos 10 numeros é {soma}')
'''

# questao 20
'''
x = 1
soma = 0

while x <= 10:
    n = int(input('Digite um valor. '))
    soma = soma + n
    x = x + 1
print (f'Média é: {soma/ 10}') 
'''

# questao 21
'''
x = 1
soma = 0

while x <= 10:
    n = int (input('Digite um valor. '))
    if n > 0:
        soma = soma + n
        x = x + 1
print (f'Média é: {soma/10}')
'''

# questao 22
'''
n = int (input('Digite um número inteiro. '))

if n < 0:
    n = n * (-1)

for i in range (n * 2):
    if i % 2 != 0:
        print (i)
'''

# questao 23
'''
n = int (input('Informe um numero inteiro positivo. '))
if n < 0:
        print ('Número inválido.')

for i in range (0, n + 1):
        print (i)
'''

# questao 24
'''
n = int (input('Digite um numero inteiro positivo. '))
if n < 0:
    print ('Entrada inválida.')

for i in range (n, -1, -1):
    print (i)
'''

# questao 25  
'''
n1 = int (input('Digite um numero. '))
n2 = int (input('Digite outro número. '))
soma = 0
mult = 1

if n1 >= n2:
    for i in range (n2, n1 + 1):
        if i % 2 == 0:
            soma += i

            
        if i % 2 != 0:
            mult *= i 
elif n2 >= n1:  

    for i in range ( n1, n2 + 1):
        if i % 2 == 0:
            soma += i
            
        if i % 2 != 0:
            mult *= i
          

print (f'A soma dos numeros pares do intervalo de {n1} a {n2} é {soma}')
print (f'A multilplicação dos numeros ímpares do intervalo de {n1} a {n2} é {mult}')
'''

# questao 26
'''
num = int (input('Você quer saber a tabuada de qual número? '))

for i in range (1, 10 + 1,):
    print (f'{num} * {i} = {num * i}')
'''

# questao 27 
'''
numN = int (input('Digite um numero inteiro positivo. '))
cont = 1

for i in range (1, numN + 1):  
    for z in range (1, i + 1):
        print (cont, end= ' ')
        cont += 1
    print ()
'''


