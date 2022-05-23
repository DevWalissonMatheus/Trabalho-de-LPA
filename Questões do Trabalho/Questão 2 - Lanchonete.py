print('\n')
print('Bem vindo a Lanchonete do Walisson Matheus RU: 3989950') # Identificador Pessoal

def cardapio(): # Função do Cardápio
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
# Váriavéis com a Descrição dos Produtos
desc1 = 'Cachorro-Quente'
desc2 = 'Cachorro-Quente Duplo'
desc3 = 'X-Egg'
desc4 = 'X-Salada'
desc5 = 'X-Bacon'
desc6 = 'X-Tudo'
desc7 = 'Refrigerante'
desc8 = 'Chá Gelado'
# Variavéis com o valor de cada produto
vlr1 = 9.00
vlr2 = 11.00
vlr3 = 12.00
vlr4 = 13.00
vlr5 = 14.00
vlr6 = 17.00
vlr7 = 5.00
vlr8 = 4.00

total = 0 # Variavél contadora do total que o cliente irá pagar
pedido = 1 # Varial do  que fiz do pedido para habilitar o (while)
def pedidos(): # Função dos pedidos
    global pedido
    global total
    while pedido != 0: # Usei while para algum possivel erro 
        # try/except para um possivel valor não inteiro
        try:
            ped = int(input('Insira o código do produto desejado: '))
            # Sequencia de if e elif para fazer a separação de cada pedido e a soma do total
            if ped == 100:
                print(f'Produto Selecionado: {desc1} \nValor: {vlr1:.2f} Reais')
                total+=vlr1 # Parametro total mais o valor do produto
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
            # else para um possivel código inválido
            else:
                print('Código Inválido!')
                continue
        except ValueError: # except ValueError para um valor não inteiro ou se for digitado uma letra
            print('Insira um valor inteiro!')
            continue # Se der erro continua no Loop
        while True:
            try:
                print('Deseja pedir novamente?\n1 - Sim\n0 - Não') 
                cont_ou_sair = int(input('>> '))
                if cont_ou_sair == 1: # Se inserir 1 continua pedindo
                    pedidos()  
                elif cont_ou_sair == 0: # Se digitar 0 mostra o valor total a ser pago e encerra o programa
                    print(f'O valor total a ser pago é: {total:.2f} Reais\n')
                    break # break para encerrar o programa
                else: # else para um possivel código errado
                    print('Código invalido!\nTente novamente.')
                    continue # continua o loop em caso de código errado
            except ValueError:
                print('Insira um valor inteiro!')
                continue  
mostrCard = cardapio() # Váriavel para executar a função cardápio
fazerPed = pedidos() # Váriavel para executar a função pedidos
print('\n')