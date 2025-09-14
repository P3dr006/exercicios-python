from pathlib import Path

inicial = Path('exercicios')
inicial.mkdir(exist_ok=True)

relatorios = Path('relatorios')
relatorios.mkdir(exist_ok=True)

Path(inicial/'entrada.txt').touch(exist_ok=True)
Path(inicial/'saida.txt').touch(exist_ok=True)

print (f'tem {len(list(inicial.rglob('*.txt')))}')

for arq in Path(inicial).glob('*.txt'):
    print("-", arq.stem)
