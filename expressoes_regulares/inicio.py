import re

def encontrar_produtos():
 produtos = 'arroz 15.99, feijão 10.99, carne 25.99, ovos 3.99'
 padrao = r'\w+\ \d+.\d+'
 busca = re.findall(padrao,produtos)
 print('os produtos sao:')
 for item in busca:
    print(item)

def placa_veiculo():
    placas = 'o sistema de busca deve esconder a placa de todos os veiculos: AFS-5124, FDS-1234, GFS-5124, HFS-5124'
    padrao = r'\w{3}-\d{4}'
    esconder = re.sub (padrao, 'placa', placas)
    print(esconder)

def encontrar_usuarios():
    texto = "Obrigado @joaopereira e @maria_silva pela ajuda! Também cito @123julio e @_admin"
    padrao = r'@\w+'
    usuarios = re.findall(padrao,texto)
    for usuario in usuarios:
        print(usuario)
        