import shutil
from pathlib import Path

# 1. Sistema de relatórios organizado
def backup_relatorio_principal():
    # Criar pastas principais
    pasta_relatorios = Path('gerenciamento_arquivo/relatorios/pasta_relatorios')
    pasta_backup = Path('gerenciamento_arquivo/relatorios/backup_relatorios')

    pasta_relatorios.mkdir(parents=True, exist_ok=True)
    pasta_backup.mkdir(parents=True, exist_ok=True)

    print(f"Pasta principal criada: {pasta_relatorios}")
    print(f"Pasta de backup criada: {pasta_backup}")

    # Mover arquivos para a pasta principal
    pasta_atual = Path('gerenciamento_arquivo/relatorios')
    arquivos_movidos = 0

    for item in pasta_atual.iterdir():
        if item.is_file() and item.name != 'relatorio.py' and not item.name.startswith('backup_'):
            destino_principal = pasta_relatorios / item.name
            shutil.move(item, destino_principal)
            print(f"Movido para pasta principal: {item.name}")
            arquivos_movidos += 1

    # Fazer backup dos arquivos da pasta principal
    if arquivos_movidos > 0:
        print(f"\nFazendo backup dos arquivos da pasta principal...")
        for arquivo in pasta_relatorios.iterdir():
            if arquivo.is_file():
                destino_backup = pasta_backup / arquivo.name
                shutil.copy2(arquivo, destino_backup)
                print(f"Backup criado: {arquivo.name}")

        print("\nSistema de relatórios configurado com sucesso")
        print(f"Pasta principal: {pasta_relatorios}")
        print(f"Pasta de backup: {pasta_backup}")
    else:
        print("Nenhum arquivo encontrado para organizar")
        print("Adicione alguns arquivos .txt na pasta relatorios e execute novamente")


# 2. Backup simples: só move relatorio.txt para relatorio_antigo
def backup_relatorio_simples():
    relatorio_origem = Path('gerenciamento_arquivo/relatorios/relatorio.txt')
    relatorio_antigo = Path('gerenciamento_arquivo/relatorios/relatorio_antigo')
    relatorio_antigo.mkdir(exist_ok=True)

    if relatorio_origem.exists():
        shutil.move(relatorio_origem, relatorio_antigo / 'relatorio_backup.txt')
        print("Relatório movido para backup simples")
    else:
        print("Nenhum relatorio.txt encontrado para backup simples.")


# Executar o que você quiser
backup_relatorio_principal()
backup_relatorio_simples()
