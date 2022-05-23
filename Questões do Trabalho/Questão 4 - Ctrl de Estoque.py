print('\n')
print('Bem vindo ao Controle de Estoque da Bicicletaria do Walisson Matheus RU: 3989950')
# Identificador pessoal
def cadastrarPeca(codigo): # Função de cadastramento de peça
    print('-' * 30) # print de alguns hifens para separar as informações
    print('Você escolheu a opção Cadastrar Peça.')
    print('Código da peça {}'.format(codigo)) # Informa o código da peça
    nome = input('Insira o Nome da peça: ')
    facric = input('Insira o Fabricante da peça: ')
    while True:
        # while e try/except para verificar possiveis erros
        try:
            valor = float(input('Insira o Valor da peça: '))
            dicPeca = {'Codigo' : codigo,
                        'Nome' : nome,
                        'Fabricante' : facric,
                        'Valor' : valor}
            # Dicionario com as informações coletadas
            l_pecas.append(dicPeca.copy()) # Parametro para copiar as informações
                                           # para lista
            break
        except ValueError:
            print('Insira Um Valor Inteiro!')

def consultarPeca(): # Função para consultar as peças
    while True:
        # try/except para verificar erros
        try:
            print('-' * 30)
            print('Você escolheu a opção Consultar Peça')
            op_consulte = int(input('Selecione a opção desejada:\n'
            '1 - Consultar Todas as Peças\n2 - Consultar Peças por Código\n'
            '3 - Consultar Peças por Fabricante\n4 - Retornar\n>> '))
            if op_consulte == 1: # Se for escolhida a opção 1
                for peca in l_pecas: # Verifica as peças na lista de peças
                    for key, value in peca.items(): # Para cada chave e dado correspondente
                        print('{} : {}'.format(key,value)) # Impre os respectivos resultados
            elif op_consulte == 2: # Se for escolhida a opção 2
                try:
                    entr_cod = int(input('Insira o Código: ')) # Pergunta o código da peça
                    for peca in l_pecas:
                        if(peca['Codigo'] == entr_cod): # Faz a pesquisa do código na liasta
                            for key, value in peca.items():
                                print('{} : {}'.format(key,value)) # E imprime o resultado
                except ValueError:
                    print('Insira Um Valor Inteiro!')
                # try/except para verificar erros na digitação do código
            elif op_consulte == 3: # Se for escolhida a opção 3
                    entr_fabr = input('Insira o Fabricante: ') # Pergunta a fabricante
                    for peca in l_pecas:
                        if(peca['Fabricante'] == entr_fabr): # Faz a pesquisa da fabricante na lista
                            for key, value in peca.items():
                                print('{} : {}'.format(key,value)) # E imprime o resultado
            elif op_consulte == 4: # Se for escolhida a opção 4
                return # Retorna pra seleção das opço~es
            else: # else se for digitado um código não existente
                print('Opção Inválida!')
                continue
        except ValueError:
            print('Insira Um Valor Inteiro!')
        # try/except para verificar erros
def removerPeca(): # Função para remover peças
    while True:
        try:
            print('-' * 30)
            print('Você selecionou a opção Remover Peça')
            entr_codi = int(input('Insira o código da peça que deseja remover: '))
            # Pergunta o código da peça que deseja remover
            for peca in l_pecas: # Para cada peça na lista
                if(peca['Codigo'] == entr_codi): # Pesquisa o código na lista
                    l_pecas.remove(peca) # E faz a remoção
        except ValueError:
            print('Insira Um Valor Inteiro!')
        break # Enserra a função

cod = 0 # Variavel contadora do código da peça
l_pecas = [] # Lista de peças
while True:
    try:
        print('-' * 30)
        opMenu = int(input('Selecione a opção desejada:\n'
        '1 - Cadastrar Peça\n2 - Consultar Peça\n'
        '3 - Remover Peça\n4 - Sair\n>> '))
        # Sequencia de if e elif para fazer a verificação das opções
        if opMenu == 1: # Se escolher 1 chama a função de cadastramento
            cod = cod + 1 # Função para atribuir o código novo a cada cadastro
            cadastrarPeca(cod)
        elif opMenu == 2: # Se escolher 2 chama a fução de consulta de peça
            consultarPeca()
        elif opMenu == 3: # Se escolher 3 chama a função de remoção de peça
            removerPeca()
        elif opMenu == 4: # Se escolher 4 encerra o programa
            print('Programa Finalizado!')
            break
        else: # else para o caso de digitar uma opção não existente
            print('Opção Inválido!')
            continue
    except ValueError: 
        print('Insira Um Valor Inteiro!')