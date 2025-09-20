
from openpyxl import Workbook 

from pathlib import Path

arquivo = Workbook() 

base = Path(__file__).parent

caminho = base /'planilha.xlsx'

def cadastro():

 planilha_atual = arquivo.active

 planilha_atual.title = 'Cadastro'

 planilha_atual['A1'] = 'nome'

 planilha_atual['B1'] = 'cidade'

 planilha_atual.append(['pedro','fortaleza'])

 planilha_atual.append(['kaue','sao paulo'])

def visitas():

    planilha_visita = arquivo.create_sheet('visitas')

    planilha_visita.append(['data', 'visitantes'])

    planilha_visita.append(['01/01/2025', '142'])

    planilha_visita.append(['02/01/2025', '123'])

    planilha_visita['B2'] = '190'


visitas()

arquivo.save(caminho)