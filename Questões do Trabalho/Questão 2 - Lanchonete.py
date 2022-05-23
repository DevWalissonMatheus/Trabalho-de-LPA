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
# Variáveis com a Descrição dos Produtos
desc1 = 'Cachorro-Quente'
desc2 = 'Cachorro-Quente Duplo'
desc3 = 'X-Egg'
desc4 = 'X-Salada'
desc5 = 'X-Bacon'
desc6 = 'X-Tudo'
desc7 = 'Refrigerante'
desc8 = 'Chá Gelado'
# Variáveis com o valor de cada produto
vlr1 = 9.00
vlr2 = 11.00
vlr3 = 12.00
vlr4 = 13.00
vlr5 = 14.00
vlr6 = 17.00
vlr7 = 5.00
vlr8 = 4.00

total = 0 # Variável contadora do total que o cliente irá pagar
pedido = 1 # Variável do  que fiz do pedido para habilitar o (while)
def pedidos(): # Função dos pedidos
    global pedido
    global total
    while True: # Usei while para algum possível erro 
        # try/except para um possível valor não inteiro
        try:
            ped = int(input('Insira o código do produto desejado: '))
            # Sequência de if e elif para fazer a separação de cada pedido e a soma do total
            if ped == 100:
                print('-' * 30) # Adiciona alguns hifens
                print(f'Produto Selecionado: {desc1} \nValor: {vlr1:.2f} Reais')
                total+=vlr1 # Parâmetro total mais o valor do produto
                break
            elif ped == 101:
                print('-' * 30)
                print(f'Produto Selecionado: {desc2} \nValor: {vlr2:.2f} Reais')
                total+=vlr2
                break
            elif ped == 102:
                print('-' * 30)
                print(f'Produto Selecionado: {desc3} \nValor: {vlr3:.2f} Reais')
                total+=vlr3
                break
            elif ped == 103:
                print('-' * 30)
                print(f'Produto Selecionado: {desc4} \nValor: {vlr4:.2f} Reais')
                total+=vlr4
                break
            elif ped == 104:
                print('-' * 30)
                print(f'Produto Selecionado: {desc5} \nValor: {vlr5:.2f} Reais')
                total+=vlr5
                break
            elif ped == 105:
                print('-' * 30)
                print(f'Produto Selecionado: {desc6} \nValor: {vlr6:.2f} Reais')
                total+=vlr6
                break
            elif ped == 200:
                print('-' * 30)
                print(f'Produto Selecionado: {desc7} \nValor: {vlr7:.2f} Reais')
                total+=vlr7
                break
            elif ped == 201:
                print('-' * 30)
                print(f'Produto Selecionado: {desc8} \nValor: {vlr8:.2f} Reais')
                total+=vlr8
                break
            # else para um possível código inválido
            else:
                print('Código Inválido!')
                continue
        except ValueError: # except ValueError para um valor não inteiro ou se for digitado uma letra
            print('Insira um valor inteiro!')
            continue # Se der erro continua no Loop
mostrCard = cardapio() # Variável para executar a função cardápio
fazerPed = pedidos() # Variável para executar a função pedidos
while True: # loop para perguntar se quer continuar pedindo
            try: # try/except para verificar erros
                print('-' * 30)
                print('Deseja pedir novamente?\n1 - Sim\n0 - Não') 
                cont_ou_sair = int(input('>> '))
                if cont_ou_sair == 1: # Se inserir 1 continua pedindo
                    pedidos()  
                elif cont_ou_sair == 0: # Se digitar 0 mostra o valor total a ser pago e encerra o programa
                    print(f'O valor total a ser pago é: {total:.2f} Reais\n')
                    break
                else: # else para um possivel código errado
                    print('Código invalido!\nTente novamente.')
                    continue # continua o loop em caso de código errado
            except ValueError:
                print('Insira um valor inteiro!')
                continue
print('\n')