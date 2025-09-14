from pathlib import Path

pasta_inicial =  Path('gerenciamento_arquivo/')

nova_pasta = pasta_inicial/'dados'

nova_pasta.mkdir(parents=True,exist_ok=True)



arquivo = nova_pasta/'arquivo.txt'
arquivo.touch(exist_ok=True)
if not arquivo.exists():
    print('arquivo nao existe')
    print(f'pasta criada em :{nova_pasta}')

elif arquivo.exists():
    print('arquivo ja existe')


