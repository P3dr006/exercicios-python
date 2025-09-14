from pathlib import Path
import shutil
from datetime import datetime

organizador = Path('organizador')
organizador.mkdir(exist_ok=True)

shutil.move('organizador.zip', organizador)

shutil.unpack_archive(f'organizador/organizador.zip', organizador)

txt = 'txt'
png = 'png'
pdf = 'pdf'
xlsx = 'xlsx'
docx = 'docx'
jpg = 'jpg'
def registros(pasta, arq):
    log = Path('log')
    log.mkdir(exist_ok=True)
    
    agora = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    registro_log = Path(log / 'registro.log',)
    
    with registro_log.open('a', encoding= 'utf-8' ) as f:
        f.write(f'{agora} - Movimento {pasta} - {arq}\n')
        
        
def indentificador_arq(tipe):
    arquivos = list(organizador.rglob(f"*.{tipe}"))
    print(f"\nTem {len(arquivos)} arquivos {tipe}")
    for arq in arquivos:
        print  ("-", arq.stem)

def organizar_arq(tipe):
    
    pasta = Path(f'pasta.{tipe}')
    pasta.mkdir(exist_ok=True)       
    for arq in Path(organizador).rglob((f'*.{tipe}')):
        shutil.move(str(arq), pasta / arq.name)
        registros(pasta, arq.name)
        
arquivos = list(organizador.rglob("*"))
                                  
print(f"\nforam {len(arquivos)} arquivos que foram movidos")

indentificador_arq(txt)
indentificador_arq(png)
indentificador_arq(pdf)
indentificador_arq(xlsx)
indentificador_arq(docx)
indentificador_arq(jpg)

organizar_arq(txt)   
organizar_arq(png)   
organizar_arq(pdf)   
organizar_arq(xlsx)   
organizar_arq(docx) 
organizar_arq(jpg) 