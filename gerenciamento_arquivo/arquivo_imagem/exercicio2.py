from pickle import TRUE
import shutil
from pathlib import Path



def pastas_imagem():
    pasta_inicial = Path("gerenciamento_arquivo/arquivo_imagem")
    nova_pasta = pasta_inicial / "imagem"

    # cria pasta (incluindo pais se necessário)
    nova_pasta.mkdir(parents=True, exist_ok=True)

    # extensões de imagens que queremos mover
    extensoes_imagem = [".png", ".jpg", ".jpeg"]

    # percorre todos os arquivos dentro da pasta inicial e subpastas
    for arquivo in pasta_inicial.rglob("*"):
        if arquivo.is_file() and arquivo.suffix.lower() in extensoes_imagem:
            destino = nova_pasta / arquivo.name
            try:
                shutil.move(str(arquivo), destino)
                print(f"Movido: {arquivo.name} → {destino}")
            except Exception as e:
                print(f"Erro ao mover {arquivo.name}: {e}")

    # cria backup (se já existir, remove antes)
    backup_pasta = pasta_inicial / "imagem_backup"
    if backup_pasta.exists():
        shutil.rmtree(backup_pasta)
    shutil.copytree(nova_pasta, backup_pasta)
    print(f"Backup criado em: {backup_pasta}")


def backup_relatorio():
 relatorio_antigo =Path('relatorio_antigo')
 relatorio_antigo.mkdir(exist_ok=True)
 shutil.move('relatorio.txt' , relatorio_antigo / 'relatorio_backup.txt')

def Automatizando_extração():
    
 extrair = Path('extraido')
 extrair.mkdir(exist_ok=True)
 
 shutil.move('arquivos_secretos.zip',extrair )
 
 shutil.unpack_archive(f'{extrair}/arquivos_secretos.zip',extrair)

pastas_imagem()
 

