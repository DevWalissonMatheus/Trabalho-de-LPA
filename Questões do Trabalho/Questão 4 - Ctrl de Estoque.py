print('\n')
print('Bem vindo ao Controle de Estoque da Bicicletaria do Walisson Matheus RU: 3989950')
codigo = 1
ct_pecas = []
def cadastrarPeca():
    codigo + 1
    print('Você escolheu a opção Cadastar Peças.')
    print('Codigo da peça: ',format(codigo))
    for i in range(1):
        nome = input('Insira o Nome da Peça: ')
        fabric = input('Insira o Fabricante da Peça: ')
        vlr = float(input('Insira o Valor da Peça: '))
        dic_pecas = {'Nome' : nome,
                    'Fabricante' : fabric,
                    'Valor' : vlr}
        ct_pecas.append(dic_pecas.copy())

def consultarPeca():
    while True:
        try:
            print('Você escolheu a opção Consultar Peças.')
            print('Escolha a opção desejada:\n1 - Consultar Todas as Peças\n'
            '2 - Consultar Peças por Código\n3 - Consultar Peças por Fabricante\n'
            '4 - Retomar')
            men_op = int(input('>>'))
            if men_op == 1:
                print(ct_pecas)
                break
        except ValueError:
            print('Insira um dos códigos acima!')
            continue
