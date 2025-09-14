from pathlib import Path

pasta_inicial =  Path('exercicios/exercicios-python-1/gerenciamento_arquivo')

nova_pasta = pasta_inicial/'dados'

nova_pasta.mkdir(parents=True,exist_ok=True)

print(f'pasta criada em :{nova_pasta}')