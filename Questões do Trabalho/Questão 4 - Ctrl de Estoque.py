print('\n')
print('Bem vindo ao Controle de Estoque da Bicicletaria do Walisson Matheus RU: 3989950')

def m_Inicial():
    while True:
        try:
            print('Escolha a opção desejada: \n1 - Cadastrar Peças\n'
            '2 - Consultar Peças\n3 - Remover Peças\n4 - Sair')
            op_menu = int(input('>> '))
            if op_menu <= 4 and op_menu >= 1:
                break
            else:
                print('Opção Inválida!')
                m_Inicial()
        except ValueError:
            print('Valor Inválido!')
    return op_menu

def cadastrarPeca(Código):
    while True:
        try:
            print('Você escolheu a opção de Cadastrar de Peças')
            print('Código da Peça ', Código)
            nome = input('Insira o Nome da Peça: ')
            fabric = input('Insira o Fabricante da Peça: ')
            valor = float(input('Insira o Valor da Peça: '))
            pecas_cads = {'Nome' : nome, 'Fabricante' : fabric, 'Valor' : valor}
            break
        except ValueError:
            print('Dado Inválido!')
    return pecas_cads

cont_codigo = 1
list_cads = []
op_desejada = m_Inicial()
while op_desejada != 0:
    if op_desejada == 1:
        cadPecas = cadastrarPeca(cont_codigo)
        cont_codigo += 1
        list_cads.append(cadPecas)
    elif op_desejada == 2:
        print('2')
    elif op_desejada == 3:
        print('3')
    elif op_desejada == 4:
        print('Programa Encerrado!')
        break