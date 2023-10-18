from calculadora import *

#main = principal

#implementação da calculadora simples

#Apresentação
while True:

 print('\t      Calculadora Simples     ')

 print('1. Soma')
 print('2. Subtração')
 print('3. Multiplicação')
 print('4. Divisão')
 print('5. Saída')

 #ler a opção de escolha do usuario

 op = int(input('\n Opção: '))

 if op == 1:
    print('\n Soma')
    v1 = int(input('Informe o valor 1: '))
    v2 = int(input('Informe o valor 2: '))

    # processamento

    total = soma(v1, v2)

    print('{} + {} = {}'.format(v1, v2, total))

 elif op == 2:
    print('\nSubtração')
    v1 = int(input('Informe o valor 1: '))
    v2 = int(input('Informe o valor 2: '))

    # processamento

    total = sub(v1, v2)
    print('{} - {} = {}'.format(v1, v2, total))

 elif op == 3:
    print('\n Multiplicação')
    v1 = int(input('Informe o valor 1: '))
    v2 = int(input('Informe o valor 2: '))

    # processamento

    total = mult(v1, v2)
    print('{} * {} = {}'.format(v1, v2, total))

 elif op == 4:
    print('Divisão')
    v1 = int(input('Informe o valor 1: '))
    v2 = int(input('Informe o valor 2: '))

    # processamento

    total = div(v1, v2)
    print('{} / {} = {}'.format(v1, v2, total))

 elif op == 5:
    print('\nAté logo')
    break

 else:
     print('{}? Não há essa opção \n Faça novamente'.format(op))
     break
 #tratamento de exceção





