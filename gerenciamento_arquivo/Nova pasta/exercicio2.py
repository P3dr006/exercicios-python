import shutil
from pathlib import Path
def pastas_imagem():
 inicio = Path('imagem')
 inicio.mkdir(exist_ok=True)


 if not Path("imagem/imagem1.png").exists() or not Path("imagem/imagem2.png").exists():
     
  Path('imagem1.png').touch(exist_ok=True)
  Path('imagem2.png').touch(exist_ok=True)
  shutil.move('imagem1.png' ,'imagem') 
  shutil.move('imagem2.png' ,'imagem') 
  shutil.copytree('imagem', 'imagem_backup')
  
 else:
    print('esses arquivos ja estao na pasta')

def backup_relatorio():
 relatorio_antigo =Path('relatorio_antigo')
 relatorio_antigo.mkdir(exist_ok=True)
 shutil.move('relatorio.txt' , relatorio_antigo / 'relatorio_backup.txt')

def Automatizando_extração():
    
 extrair = Path('extraido')
 extrair.mkdir(exist_ok=True)
 
 shutil.move('arquivos_secretos.zip',extrair )
 
 shutil.unpack_archive(f'{extrair}/arquivos_secretos.zip',extrair)

 

