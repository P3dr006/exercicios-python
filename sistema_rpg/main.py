from sistema import *

potencial = potencial()

while True:

    print(f'\npotencial: {potencial} - rank: {rank_potencial(potencial)} - compra de status: {compra_status}')

    iniciar_fichar = input(f'''
    [1] Criar Atributos
    [2] Informações sistema
    ''')

    if iniciar_fichar == '1':
        atributos()
    elif iniciar_fichar == "2":
        informacoes_ficha()   
    else:
        print('nao temos essa opção')    

