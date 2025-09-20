import shutil
from pathlib import Path

def Automatizando_extração():
    
    # Caminho correto para o arquivo ZIP
    origem_zip = Path('gerenciamento_arquivo/extrair_arquivo/arquivos_secretos.zip')
    
    # Pasta onde vamos extrair
    pasta_destino = Path('gerenciamento_arquivo/extrair_arquivo/arquivos_extraidos')
    
    # Criar pasta de destino se não existir
    pasta_destino.mkdir(parents=True, exist_ok=True)
    
    # Verificar se o arquivo ZIP existe
    if origem_zip.exists():
        print(f'Extraindo {origem_zip} para {pasta_destino}')
        shutil.unpack_archive(origem_zip, pasta_destino)
        print('Extração concluída com sucesso!')
    else:
        print(f'Erro: Arquivo {origem_zip} não encontrado!')

Automatizando_extração() 

#caso queira rodar arquivo com o comando e o arquivo na pasta principal

#def Automatizando_extração():
    
 #extrair = Path('extrair_arquivo')

 #extrair.mkdir(exist_ok=True)
 
 #shutil.move('arquivos_secretos.zip',extrair )
 
 #shutil.unpack_archive(f'{extrair}/arquivos_secretos.zip',extrair)