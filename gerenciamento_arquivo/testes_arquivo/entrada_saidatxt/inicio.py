from pathlib import Path

inicial = Path('gerenciamento_arquivo/testes_arquivo/entrada_saidatxt/exercicios')
inicial.mkdir(parents=True, exist_ok=True)

relatorios = Path('gerenciamento_arquivo/testes_arquivo/entrada_saidatxt/relatorio')
relatorios.mkdir(parents=True,exist_ok=True)

Path(inicial/'entrada.txt').touch(exist_ok=True)
Path(inicial/'saida.txt').touch(exist_ok=True)

print (f'tem {len(list(inicial.rglob('*.txt')))}')

for arq in Path(inicial).glob('*.txt'):
    print("-", arq.stem)
