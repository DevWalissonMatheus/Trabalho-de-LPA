print('\n')
print('Bem vindo a Companhia de Logistica Walisson Matheus S.A. RU: 3989950')
# Identificador pessoal
dimenOB = 0 # Variável contadora das dimensões do objeto
pesoOB = 0 # Variável contadora do peso do objeto
rotaOb = 0 # Variável contadora da rota do objeto
def dimensoesObejto(): # Função das dimensões do objeto
    altura = 1 
    comprimento = 1
    largura = 1
    # Usei esses parâmetro para habilitar os while
    while altura != 0: # Loop para ficar repetindo até que seja digitado 
                       #um dado valido
        try: 
            print('-' * 45) # print de alguns hifens para separar as informações
            altura = float(input('Insira a altura do Objeto (em cm): '))
            break
        except:
            print('ERRO! Insira um valor numérico.')
        # try/except para verificar se foi digitado um dado inválido
    while comprimento != 0:
        try:
            comprimento = float(input('Insira o comprimento do Objeto (em cm): '))
            break
        except:
            print('ERRO! Insira um valor numérico.')
        # try/except para verificar se foi digitado um dado inválido
    while largura != 0:
        try:
            largura = float(input('Insira a largura do Objeto (em cm): '))
            volume = altura * comprimento * largura
            # Variavel para fazer o calculo da dimensão do objeto
            print('O volume do objeto é: ', volume)
            print('-' * 38)
            global dimenOB # Variável para tornar esse parâmetro global
            # Sequencia de if e elif para fazer a verificação dos dados
            # E retornar os dados para a dimensão global
            if volume <= 1000:
                valor1 = 10 # Variável com o valor até essa dimensão
                dimenOB = dimenOB + valor1 # Variável para fazer a 
                                           #atribuição dos dados
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
            # elif para informar que essa dimensão não é aceita e 
            # tentar novamente
            elif volume > 100000:
                print('Não aceitamos objetos com as dimensões tão grandes.')
                print('Insira as informações novamente.')
                dimensoesObejto()
                break
        except:
            print('ERRO! Insira um valor numérico.')
        # try/except para verificar se foi digitado um dado inválido
def pesoObjeto(): # Função do peso do objeto
    while True:
        # try/except para verificar possíveis erros  
        try:
            peso = float(input('Insira o peso do objeto (em kg): '))
            print('-' * 40)
            global pesoOB
            # Sequência de if e elif para fazer a verificação dos dados
            # E atribuir o resultado à variável global
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
            print('ERRO! Insira um valor numérico.')
def rotaObjeto(): # Função das rotas do objeto
    while True:
        print('Selecione a rota:\nRS - De Rio de Janeiro até São Paulo\n'
        'SR - De São Paulo até Rio de Janeiro\nBS - De Brasília até São Paulo\n'
        'SB - De São Paulo até Brasília\nBR - De Brasília até Rio de Janeiro\n'
        'RB - Rio de Janeiro até Brasília')
        rota = input('>> ').lower() # lower para verificar se o dado foi digitado
                                    # em letra minúscula, caso seja digitada em 
                                    # maiúsculo transforma as letras em minúscula
        print('-' * 35)
        global rotaOb
        # Sequencia de if e elife para verificar as rotas
        if rota == 'rs':
            rs = 1 # Variavel contadora
            rotaOb = rotaOb + rs # Variável para adicionar os dados a 
                                 # parâmetro global
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
        else: # else para um possível código errado
            print('Essa rota não existe.\nInsira a rota novamente!')
dimensoesObejto()
pesoObjeto()
rotaObjeto()
vlrDPR = dimenOB * pesoOB * rotaOb # Variável para fazer o cálculo do valor 
                                   # a ser pago
print(f'O valor a ser pago é: {vlrDPR:.2f} Reais'
     f'(Dimensões: {dimenOB} * Peso: {pesoOB} * Rota: {rotaOb})')
print('\n')