print('\n')
print('Bem vindo a Lanchonete do Walisson Matheus RU: 3989950')

def cardapio():
    print('|*****************************************************|')
    print('|                     Cardápio                        |')
    print('|**********|****************************|*************|')
    print('|  Código  |          Descrição         |  Valor(R$)  |')
    print('|   100    |    Cachorro-Quente         |    9,00     |')
    print('|   101    |    Cachorro-Quente Duplo   |    11,00    |')
    print('|   102    |    X-Egg                   |    12,00    |')
    print('|   103    |    X-Salada                |    13,00    |')
    print('|   104    |    X-Bacon                 |    14,00    |')
    print('|   105    |    X-Tudo                  |    17,00    |')
    print('|   200    |    Refrigerante            |    5,00     |')
    print('|   201    |    Chá Gelado              |    4,00     |')
    print('*******************************************************')

desc1 = 'Cachorro-Quente'
desc2 = 'Cachorro-Quente Duplo'
desc3 = 'X-Egg'
desc4 = 'X-Salada'
desc5 = 'X-Bacon'
desc6 = 'X-Tudo'
desc7 = 'Refrigerante'
desc8 = 'Chá Gelado'

vlr1 = 9.00
vlr2 = 11.00
vlr3 = 12.00
vlr4 = 13.00
vlr5 = 14.00
vlr6 = 17.00
vlr7 = 5.00
vlr8 = 4.00

total = 0
pedido = 1
def pedidos():
    global pedido
    global total
    while pedido != 0:
        try:
            ped = int(input('Insira o código do produto desejado: '))
            if ped == 100:
                print(f'Produto Selecionado: {desc1} \nValor: {vlr1:.2f} Reais')
                total+=vlr1
            elif ped == 101:
                print(f'Produto Selecionado: {desc2} \nValor: {vlr2:.2f} Reais')
                total+=vlr2
            elif ped == 102:
                print(f'Produto Selecionado: {desc3} \nValor: {vlr3:.2f} Reais')
                total+=vlr3
            elif ped == 103:
                print(f'Produto Selecionado: {desc4} \nValor: {vlr4:.2f} Reais')
                total+=vlr4
            elif ped == 104:
                print(f'Produto Selecionado: {desc5} \nValor: {vlr5:.2f} Reais')
                total+=vlr5
            elif ped == 105:
                print(f'Produto Selecionado: {desc6} \nValor: {vlr6:.2f} Reais')
                total+=vlr6
            elif ped == 200:
                print(f'Produto Selecionado: {desc7} \nValor: {vlr7:.2f} Reais')
                total+=vlr7
            elif ped == 201:
                print(f'Produto Selecionado: {desc8} \nValor: {vlr8:.2f} Reais')
                total+=vlr8
            else:
                print('Código Inválido!')
                continue
        except ValueError:
            print('Insira um código númerico!')
            continue
        while True:
            try:
                print('Deseja pedir novamente?\n1 - Sim\n0 - Não')  
                cont_ou_sair = int(input('>> '))
            except ValueError:
                print('Insira um código númerico!')
                continue  
            if cont_ou_sair == 1:
                pedidos()  
            elif cont_ou_sair == 0:
                print(f'O valor total a ser pago é: {total:.2f} Reais\n')
                break
            else:
                print('Código invalido!\nTente novamente.')
mostrCard = cardapio()
fazerPed = pedidos()