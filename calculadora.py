n = 1
while n != 0:
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
        
    if n == 1:
        print(" ")
        print('Você escolheu SOMA')
        print(" ")
        num1 = int(input('Escolha um número: '))
        num2 = int(input('Escolha outro número: '))
        print(f'{num1} + {num2} = {num1+num2}') 
    elif n == 2:
        print(" ")
        print('Você escolheu SUBTRAÇÃO')
        print(" ")
        num1 = int(input('Escolha um número: '))
        num2 = int(input('Escolha outro número: '))
        print(f'{num1} - {num2} = {num1-num2}')
    elif n == 3:
        print(" ")
        print('Você escolheu MULTIPLICAÇÃO')
        print(" ")
        num1 = int(input('Escolha um número: '))
        num2 = int(input('Escolha outro número: '))
        print(f'{num1} x {num2} = {num1*num2}')
    elif n == 4:
        print(" ")
        print('Você escolheu DIVISÃO')
        print(" ")
        num1 = int(input('Escolha um número: '))
        num2 = int(input('Escolha outro número: '))
        print(f'{num1} / {num2} = {num1/num2}')
    elif n == 5:
        print(" ")
        print('Você escolheu POTENCIAÇÃO POR 2')
        print(" ")
        num1 = int(input('Escolha um número: '))
        print(f'{num1}² = {num1**2}')
    elif n < 0 or n > 5:
        print('Opção inválida, tente novamente!')
    if n == 0:
        print(" ")
        print('Até a próxima!')
        print(" ")
        break