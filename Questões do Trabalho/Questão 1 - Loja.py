print('\n')
print('Bem Vindo a Loja do Walisson Matheus RU: 3989950')
# Identificador pessoal

v_uni = 1 # Usei para habilitar o "while v_uni"
qtd_prod = 1 # Usei para habilitar o "while qtd_prod"

while v_uni != 0: # Loop para o caso de apresentar erro
    # Try/Except usado para evitar um erro se o usuário digitar um valor não numérico
    try:
        v_unit = float(input('Insira o valor unitário do produto: '))
        if v_unit > 0: # Se digitar um valor maior que Zero continua    
            break # Função usada para encerrar o Loop
        else: # Se Inserir um valor igual ou menor que Zero repete a pergunta
            print('Insira um valor maior!') # Mensagem que informa o erro
            continue # Função usada para continuar o Loop
    except ValueError: 
        print('Insira um valor numérico!')
        continue # Se inserir um valor não numérico informa erro e repete a pergunta

while qtd_prod != 0: # Loop para o caso de apresentar erro
    # Try/Except usado para evitar um erro se o usuário inserir letras
    try:
        qtd_p = int(input('Insira a quantidade: '))
        v_sem_desc = v_unit * qtd_p # Função para fazer o cálculo do valor sem desconto

        if qtd_p <= 0: # Se digitar um valor menor ou igual a Zero repete a pergunta
            print('Insira uma quantidade maior!')
            continue # Função para refazer a pergunta

# Sequência de elif para fazer a diferenciação dos descontos
        elif qtd_p <= 9:
            print(f'Valor sem desconto: {v_sem_desc:.2f} Reais')
            print('Para essa quantidade não oferecemos desconto')
        # Parâmetro para quantidade menor que ou igual a 9
        elif qtd_p >= 10 and qtd_p <= 99:
            # and para verificar se está entre o intervalo de 10 até 99
            print(f'Valor sem desconto: {v_sem_desc:.2f} Reais')
            desc_5 = (5 * v_sem_desc) / 100 # Cálculo do desconto
            v_com_desc = v_sem_desc - desc_5 # Cálculo para inserir o desconto
            print(f'Valor com desconto: {v_com_desc:.2f} Reais (Desconto de 5%)')
        elif qtd_p >= 100 and qtd_p <= 999:
            print(f'Valor sem desconto: {v_sem_desc:.2f} Reais')
            desc_10 = (10 * v_sem_desc) / 100 
            v_com_desc = v_sem_desc - desc_10 
            print(f'Valor com desconto: {v_com_desc:.2f} Reais (Desconto de 10%)')
        elif qtd_p >= 1000:
            print(f'Valor sem desconto: {v_sem_desc:.2f} Reais')
            desc_15 = (15 * v_sem_desc) / 100 
            v_com_desc = v_sem_desc - desc_15
            print(f'Valor com desconto: {v_com_desc:.2f} Reais (Desconto de 15%)')
        break # break para encerar o programa
    except ValueError: # except para evitar erro
        print('Insira uma quantidade numérica!')
        continue # Se houver erro repete a pergunta
print('\n')