n = '1'
while n != '0':
    print('''
          CALCULADORA

          1 - SOMA
          2 - SUBTRAÇÃO
          3 - MULTIPLICAÇÃO
          4 - DIVISÃO
          5 - POTENCIAÇÃO POR 2
          0 - SAIR
          ''')  
    n = int(input("Escolha uma opção: "))

    if n == 0:
        print('Até a próxima!')
        break
    if n < 0 or n > 5 or n == " ":
        print('Opção inválida, tente nvamente!')
        
    if n == 1:
        num1 = int(input('Escolha um número: '))
        num2 = int(input('Escolha um número: '))
        print(f'{num1} + {num2} = {num1+num2}') 
    elif n == 2:
        num1 = int(input('Escolha um número: '))
        num2 = int(input('Escolha um número: '))
        print(f'{num1} - {num2} = {num1-num2}')
    elif n == 3:
        num1 = int(input('Escolha um número: '))
        num2 = int(input('Escolha um número: '))
        print(f'{num1} x {num2} = {num1*num2}')
    elif n == 4:
        num1 = int(input('Escolha um número: '))
        num2 = int(input('Escolha um número: '))
        print(f'{num1} / {num2} = {num1/num2}')
    elif n == 5:
        num1 = int(input('Escolha um número: '))
        print(f'{num1}² {num2} = {num1**2}')