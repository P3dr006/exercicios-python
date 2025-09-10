from final import *

def inicio():
    continuar = ""
    
    while continuar == "" or continuar.lower() == 's':
        
    tentativa = {
        'usuario': input('Usuário: '),
        'senha': input('Senha: '),
    }
    
    if tentativa['usuario'] == usuario['usuario'] and tentativa['senha'] == usuario['senha']:
        
        print('Acesso permitido!')
        break
    else:
        
        print('Acesso negado! Nome de usuário ou senha incorretos.')
        continuar = input('Deseja tentar novamente? (s/n): ').lower()
        
        if continuar not in ['s', 'n']:
            
            print("Opção inválida, saindo do sistema...")
            exit()
            
        if continuar == 'n':
            
            print('Saindo do sistema...')
            exit()