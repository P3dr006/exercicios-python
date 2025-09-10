
lista_alunos = {
    'Pedro':[3,10,7],
    'Diego':[5,14,9],
    'Paulo':[8,16,8],
}

def adicionar_aluno():
    nome = input('insira seu nome:').title()
    serie = int(input('insira sua serie:'))
    idade = int(input('insira sua idade'))
    nota = float(input('insira sua nota'))
    lista_alunos[nome] = serie,idade,nota

def listar_alunos():
    for nomes,(serie,idade,nota) in lista_alunos.items():
        print(f'Aluno:{nomes} | Serie:{serie} | Idade:{idade} | Nota:{nota}')

def buscar_alunos():
    aluno = input('insira o nome do Aluno:')
    
    if aluno in lista_alunos:
        print (f'Aluno:{aluno} | Serie:{lista_alunos[aluno]}')
    else:
        print('nao temos esse aluno no nosso sistema')    
    
def remover_alunos():
    listar_alunos()
    remover = input('insira o nome de usuario que ira retirar:').title()   
    del lista_alunos[remover]
    listar_alunos()
    

def media_notas():
    notas = 0
    media = 0
    for nomes,(serie,idade,nota) in lista_alunos.items():
      notas +=nota
      media = notas / len(lista_alunos) 
    print (f"{media:.2f}") 
     
while True:
    inicio = input('''
---------inicio---------
[1] Adicionar aluno

[2] Listar todos os alunos

[3] Buscar aluno pelo nome

[4] Remover aluno

[5] Mostrar média geral das notas

[6] Sair                   
                   
                   ''')
    if inicio == '1':
        adicionar_aluno()   
    elif inicio == '2':
        listar_alunos()
    elif inicio == '3':
        buscar_alunos()           
    elif inicio == '4':
        remover_alunos() 
    elif inicio == '5':
        media_notas()   
    elif inicio == '6':
        print('muito obg ate logo')
        break
    else:
        print('nao temos essa opcao')              
    
    
    