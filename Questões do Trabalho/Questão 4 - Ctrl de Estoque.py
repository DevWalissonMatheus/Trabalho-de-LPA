print('\n')
print('Bem vindo ao Controle de Estoque da Bicicletaria do Walisson Matheus RU: 3989950')

def cadastrarPeca(codigo):
    print('-' * 30)
    print('Você escolheu a opção Cadastrar Peça.')
    print('Código da peça {}'.format(codigo))
    nome = input('Insira o Nome da peça: ')
    facric = input('Insira o Fabricante da peça: ')
    while True:
        try:
            valor = int(input('Insira o Valor da peça: '))
            dicPeca = {'Codigo' : codigo,
                        'Nome' : nome,
                        'Fabricante' : facric,
                        'Valor' : valor}
            l_pecas.append(dicPeca.copy())
            break
        except ValueError:
            print('Insira Um Valor Inteiro!')

def consultarPeca():
    while True:
        try:
            print('-' * 30)
            print('Você escolheu a opção Consultar Peça')
            op_consulte = int(input('Selecione a opção desejada:\n'
            '1 - Consultar Todas as Peças\n2 - Consultar Peças por Código\n'
            '3 - Consultar Peças por Fabricante\n4 - Retornar\n>> '))
            if op_consulte == 1:
                for peca in l_pecas:
                    for key, value in peca.items():
                        print('{} : {}'.format(key,value))
            elif op_consulte == 2:
                try:
                    entr_cod = int(input('Insira o Código: '))
                    for peca in l_pecas:
                        if(peca['Codigo'] == entr_cod):
                            for key, value in peca.items():
                                print('{} : {}'.format(key,value))
                except ValueError:
                    print('Insira Um Valor Inteiro!')
            elif op_consulte == 3:
                    entr_fabr = input('Insira o Fabricante: ')
                    for peca in l_pecas:
                        if(peca['Fabricante'] == entr_fabr):
                            for key, value in peca.items():
                                print('{} : {}'.format(key,value))
            elif op_consulte == 4:
                return
            else:
                print('Opção Inválida!')
                continue
        except ValueError:
            print('Insira Um Valor Inteiro!')

def removerPeca():
    while True:
        try:
            print('-' * 30)
            print('Você selecionou a opção Remover Peça')
            entr_codi = int(input('Insira o código da peça que deseja remover: '))
            for peca in l_pecas:
                if(peca['Codigo'] == entr_codi):
                    l_pecas.remove(peca)
        except ValueError:
            print('Insira Um Valor Inteiro!')

cod = 0
l_pecas = []
while True:
    try:
        print('-' * 30)
        opMenu = int(input('Selecione a opção desejada:\n'
        '1 - Cadastrar Peça\n2 - Consultar Peça\n'
        '3 - Remover Peça\n4 - Sair\n>> '))
        if opMenu == 1:
            cod = cod + 1
            cadastrarPeca(cod)
        elif opMenu == 2:
            consultarPeca()
        elif opMenu == 3:
            removerPeca()
        elif opMenu == 4:
            print('Programa Finalizado!')
            break
        else:
            print('Opção Inválido!')
            continue
    except ValueError:
        print('Insira Um Valor Inteiro!')