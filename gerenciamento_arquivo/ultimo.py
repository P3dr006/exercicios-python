from pathlib import Path
import shutil
from datetime import datetime

def arquivo_data():
 producao = datetime.now()
 producao = (producao.strftime('%d/%m/%Y'))

 with open('arquivo.txt', 'w', encoding= 'utf-8')  as arquivo:
     arquivo.write(f'eae bom dia \ndata de criação:{producao}')

def contador_letras():
    with open('mensagem.txt', 'r+', encoding= 'utf-8') as mensagem:
        mensagem.write(f'bom dia aqui tem quantas letras?')
        mensagem.seek(0)
        leitura = mensagem.read()
        apenas_letras = [c for c in leitura if c.isalpha()]
        print (len(apenas_letras))     

def filtragem_pala_chave(arquivo, palavra):
    caminho = Path(f'{arquivo}.log')
    with caminho.open(encoding= 'utf-8') as log:
        for numero_linha, linha in enumerate(log, start = 1):
            if palavra in linha:
                print(f'linha [{numero_linha}] : {linha.strip()}')

cmd = input('''
[1] ver DEBUG
[2] ver INFO
[3] ver ERROR
[4] ver WARNING                  
      
                   ''')
   
match cmd.lower():
        case "1":
            palavra = "DEBUG"
        case "2":
            palavra = 'INFO'
        case "3":
            palavra = 'ERROR'
        case '4':
            palavra = "WARNING"
        case _:
          print('nao temos essa opcao')
                 
arquivo = input('insira nome do arquivo:')          
filtragem_pala_chave(arquivo,palavra)        