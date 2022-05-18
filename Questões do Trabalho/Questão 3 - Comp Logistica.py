print('\n')
print('Bem vindo a Companhia de Logistica Walisson Matheus S.A. RU: 3989950')
dimenOB = 0
pesoOB = 0
rotaOb = 0
def dimensoesObejto():
    altura = 1
    comprimento = 1
    largura = 1
    while altura != 0:
        try:
            altura = float(input('Insira a altura do Objeto (em cm): '))
            break
        except:
            print('ERRO! Insira um valor númerico.')
    while comprimento != 0:
        try:
            comprimento = float(input('Insira o comprimento do Objeto (em cm): '))
            break
        except:
            print('ERRO! Insira um valor númerico.')
    while largura != 0:
        try:
            largura = float(input('Insira a largura do Objeto (em cm): '))
            volume = altura * comprimento * largura
            print('O volume do objeto é: ', volume)
            global dimenOB
            if volume <= 1000:
                valor1 = 10
                dimenOB = dimenOB + valor1
                break
            elif volume >= 1001 and volume <= 10000:
                valor2 = 20
                dimenOB = dimenOB + valor2
                break
            elif volume >= 10001 and volume <= 30000:
                valor3 = 30
                dimenOB = dimenOB + valor3
                break
            elif volume >= 30001 and volume <= 100000:
                valor4 = 50
                dimenOB = dimenOB + valor4
                break
            elif volume > 100000:
                print('Não aceitamos objetos com as dimensões tão grandes.')
                print('Insira as informações novamente.')
                dimensoesObejto()
                break
        except:
            print('ERRO! Insira um valor númerico.')
def pesoObjeto():
    while True:    
        try:
            peso = float(input('Insira o peso do objeto (em kg): '))
            global pesoOB
            if peso <= 0.1:
                mult1 = 1
                pesoOB = pesoOB + mult1
                break
            elif peso >= 0.11 and peso <= 1:
                mult2 = 1.5
                pesoOB = pesoOB + mult2
                break
            elif peso >= 1.10 and peso <= 10:
                mult3 = 2
                pesoOB = pesoOB + mult3
                break
            elif peso >= 10.1 and peso <= 30:
                mult4 = 3
                pesoOB = pesoOB + mult4
                break
            elif peso > 30:
                print('Não aceitamos objetos tão pesados!')
                print('Insira o peso novamente.')
                pesoObjeto()
                break
        except ValueError:
            print('ERRO! Insira um valor númerico.')
def rotaObjeto():
    while True:
        print('Selecione a rota:\nRS - De Rio de Janeiro até São Paulo\n'
        'SR - De São Paulo até Rio de Janeiro\nBS - De Brasília até São Paulo\n'
        'SB - De São Paulo até Brasília\nBR - De Brasília até Rio de Janeiro\n'
        'RB - Rio de Janeiro até Brasília')
        rota = input('>> ').lower()
        global rotaOb
        if rota == 'rs':
            rs = 1
            rotaOb = rotaOb + rs
            break
        elif rota == 'sr':
            sr = 1
            rotaOb = rotaOb + sr
            break
        elif rota == 'bs':
            bs = 1.2
            rotaOb = rotaOb + bs
            break
        elif rota == 'sb':
            sb = 1.2
            rotaOb = rotaOb + sb
            break
        elif rota == 'br':
            br = 1.5
            rotaOb = rotaOb + br
            break
        elif rota == 'rb':
            rb = 1.5
            rotaOb = rotaOb + rb
            break
        else:
            print('Essa rota não existe.\nInsira a rota novamente!')
dimensoesObejto()
pesoObjeto()
rotaObjeto()
vlrDPR = dimenOB * pesoOB * rotaOb
print(f'O valor a ser pago é: {vlrDPR:.2f} Reais (Dimensões: {dimenOB} * Peso: {pesoOB} * Rota: {rotaOb})')
print('\n')