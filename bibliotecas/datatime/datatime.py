from datetime import datetime

##primeiro teste, criação de assinatura. 
agora = (datetime.now())

nome = input('insira sua assinatura:')

print(agora.strftime(f'Assinatura gerada por [{nome}] em %d de %B de %Y às %H:%M'))