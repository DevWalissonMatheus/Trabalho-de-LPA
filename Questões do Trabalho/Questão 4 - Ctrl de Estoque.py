print('\n')
print('Bem vindo ao Controle de Estoque da Bicicletaria do Walisson Matheus RU: 3989950')
def cadastrarPeca():
    cadastro = {'Nome':[], 'Fabricante':[], 'Valor':[]}
    for i in range(3):
        nome = input('Insira o Nome da Peça: ')
        fabricante = input('Insira o Fabricante da Peça: ')
        valor = float(input('Insira o Valor da Peça: '))
        cadastro['Nome'].append(nome)
        cadastro['Fabricante'].append(fabricante)
        cadastro['Valor'].append(valor)