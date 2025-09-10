from pathlib import Path

pasta_inicial =  Path('exrcicios')

nova_pasta = pasta_inicial/'arquivos'

nova_pasta.mkdir(exist_ok=True)

print(f'pasta criada em :{nova_pasta}')