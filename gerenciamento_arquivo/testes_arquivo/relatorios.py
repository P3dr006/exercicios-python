from pathlib import Path

pasta_inicial =  Path('gerenciamento_arquivo/testes_arquivo')

nova_pasta = pasta_inicial/'dados'

nova_pasta.mkdir(parents=True,exist_ok=True)

arquivo = nova_pasta/'arquivo.txt'
arquivo.touch(exist_ok=True)
if not arquivo.exists():
    print('arquivo nao existe')
    print(f'pasta criada em :{nova_pasta}')

elif arquivo.exists():
    print('arquivo ja existe')

#caso queira rodar como se fosse arquivo principal
#from pathlib import Path

#pasta_inicial =  Path('teste_arquivo/')

#nova_pasta = pasta_inicial/'dados'

#nova_pasta.mkdir(parents=True,exist_ok=True)

#arquivo = nova_pasta/'arquivo.txt'
#arquivo.touch(exist_ok=True)
#if not arquivo.exists():
#    print('arquivo nao existe')
#    print(f'pasta criada em :{nova_pasta}')

#elif arquivo.exists():
#    print('arquivo ja existe')


