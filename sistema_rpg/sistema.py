import random

atributos_list = {'FORCA':0, 'DES':0, 'CONS':0, 'SAB':0, 'INTE':0}

def info_basicos():
    nome = input('insira seu nome personagem:')
    idade = input('insira sua idade:')
    altura = input('insira sua altura:')
    genero = input('insira seu genero:')
    peso = int(input('insira seu peso'))

    print (f'''
    estetica ficha base

    BASICO
    Nome:{nome}
    Idade:{idade}
    Altura:{altura}
    Gênero:{genero}
    Peso:{peso}KG
    ''')

def roll_status():
    while True:
        roll1 = [random.randint(1, 6) for _ in range(5)]
        total1 = sum(roll1)
        print(f'Primeiro dado: {total1}')

        roll2 = [random.randint(1, 6) for _ in range(5)]
        total2 = sum(roll2)
        print(f'Segundo dado: {total2}')

        roll_max = roll1 if total1 >= total2 else roll2
        valor = sum(roll_max)

        if valor < 13:
            print('Valor mínimo de 13 não atingido, rerolando...\n')
        else:
            print(f'Valor final dos dados: {valor}')
            return valor

def potencial():
    return random.randint(1,100)    

def rank_potencial(p):
    if p <= 10: return 'F'
    elif p <= 20: return 'E'
    elif p <= 40: return 'D'
    elif p <= 55: return 'C'
    elif p <= 70: return 'B'
    elif p <= 85: return 'A'
    elif p <= 100: return 'S'
    elif p <= 115: return 'SS'
    elif p <= 130: return 'SSS'
    else: return 'SSS+'

def atributos():
    print (f'pontos de compra:{compra_status}')

    forca = des = cons = sab = inte = 0
    continuar =""
    valor = compra_status

    tabela_ranks = {
        "F": {"custo": 0, "bonus": -2},
        "E": {"custo": 1, "bonus": 0},
        "D": {"custo": 2, "bonus": 1},
        "C": {"custo": 3, "bonus": 2},
        "B": {"custo": 4, "bonus": 3},
        "A": {"custo": 6, "bonus": 4},
        "S": {"custo": 8, "bonus": 6},
        "SS": {"custo": 12, "bonus": 8},
        "SR": {"custo": 15, "bonus": 13},
        "SSR": {"custo": 18, "bonus": 16},
        "UR": {"custo": 25, "bonus": 20}
}
    ordem = list(tabela_ranks.keys())
    ordem.insert(0, 0)

    while continuar != '5':


        continuar = input(f'''
            Pontos disponiveis:{valor}

            [1] Ver tabela de preços
            [2] Comprar Atributos
            [3] Mostrar Status
            [4] Resetar
            [5] Encerrar
        ''')

atributos_list = {'FORCA':0, 'DES':0, 'CONS':0, 'SAB':0, 'INTE':0}

def menu_atributos(pontos_iniciais, ficha):

    tabela_ranks = {
        "F": {"custo": 0, "bonus": -2},
        "E": {"custo": 1, "bonus": 0},
        "D": {"custo": 2, "bonus": 1},
        "C": {"custo": 3, "bonus": 2},
        "B": {"custo": 4, "bonus": 3},
        "A": {"custo": 6, "bonus": 4},
        "S": {"custo": 8, "bonus": 6},
        "SS": {"custo": 12, "bonus": 8},
        "SR": {"custo": 15, "bonus": 13},
        "SSR": {"custo": 18, "bonus": 16},
        "UR": {"custo": 25, "bonus": 20}
    }
    
    ordem = list(tabela_ranks.keys())
    ordem.insert(0, 0) 

    valor_atual = pontos_iniciais
    continuar = ""

    while continuar != '5':
   
        continuar = input(f'''
            Pontos disponíveis: {valor_atual}

            [1] Ver tabela de preços
            [2] Comprar Atributos
            [3] Mostrar Status
            [4] Resetar
            [5] Encerrar
            
            Escolha: ''')

        if continuar == '1':
            print("\n--- TABELA ---")
            for k, v in tabela_ranks.items():
                print(f"{k} | Custo: {v['custo']} | Bônus: {v['bonus']}")

        elif continuar == "2":
        
            atributo = input("""
            Qual atributo deseja melhorar?
            FORCA, DES, CONS, SAB, INTE
            """).upper().strip()

            if atributo not in ficha:
                print("Atributo inválido!")
                continue

            novo_rank = input("Escolha o rank desejado: ").upper().strip()
            
            if novo_rank not in tabela_ranks:
                print("Rank não existe na tabela!")
                continue

            valor_que_tenho_agora = ficha[atributo]
            
            indice_atual = ordem.index(valor_que_tenho_agora)
            indice_novo = ordem.index(novo_rank)

            if indice_novo <= indice_atual:
                print("Você já tem esse nível ou um melhor!")
                continue

            custo_compra = tabela_ranks[novo_rank]['custo']

            if valor_atual < custo_compra:
                print(f'Pontos insuficientes! Custa {custo_compra}, você tem {valor_atual}.')
                continue

            valor_atual -= custo_compra
            ficha[atributo] = novo_rank 
            
            print(f"Sucesso! {atributo} definido para {novo_rank}")

        elif continuar == '3':
            print("\n--- STATUS ATUAIS ---")
            for k, v in ficha.items():
                rank_str = "Sem Rank" if v == 0 else v
     
                bonus = tabela_ranks[v]['bonus'] if v != 0 else 0
                print(f"{k}: {rank_str} (Bônus: {bonus})")

        elif continuar == '4':
            for k in ficha:
                ficha[k] = 0
            valor_atual = pontos_iniciais
            print("Ficha resetada!")

    return valor_atual


menu_atributos(50, atributos_list)

print("\nFicha Final Salva:", atributos_list)
def vida(r):
    vida_rolagem = {
        "F":  (1, 4),
        "E":  (2, 4),
        "D":  (3, 4),
        "C":  (4, 4),
        "B":  (5, 4),
        "A":  (7, 4),
        "S":  (10, 4),
        "SS": (13, 4),
        "SSS": (16, 4),
        "SR": (20, 4),
        "SSR": (25, 4),
        "UR": (30, 4)
    }
    dados, faces = vida_rolagem[r]

    rolagem = [random.randint(1,faces) for _ in (dados)]

    total = sum(rolagem)

    print(f'rolagem de vida{r}:{rolagem}')
    print(f'VIDA TOTAL:{total}')

    return total

def informacoes_ficha():
   info = ''
   while info != '3': 
    info = input('''
[1] informações para criação de ficha
[2] informações para tabela de potencial
[3] Voltar
''')
    if info == '1':
        return print('''
----INFORMAÇOES PARA CRIAÇÃO DE FICHA----


CRIAÇÃO DE FICHA
Rolê 2x 5d6 para compra(Mínimo 13)

Ranks

F-0
E-1
D-2
C-3
B-4
A-6
S-8

Dado de Potencial:1d100 

Gastando: 4 Pontos transforma desvantagem em vantagem 

Gastando: 2 Pontos permite re-rolar.

Escolha entre uma arte marcial ou um traço extra''')
    elif info == '2':
        return print('''
----TABELA DE POTENCIAL----
Jogue 1d100(Um jogador que tire C- pode gastar 2 pontos de atributos para rerolar)(Um personagem que tire E- pode escolher ter dois traço extras)

10-F
20-E
40-D
55-C
70-B
85-A
100-S
115-SS
130-SSS


- O jogador pode abandonar um traço ou arte marcial inicial para adicionar 1d20(Mínimo 10) como bônus.

- O jogador pode receber uma limitação para adicionar 1d20(Mínimo 10) no seu potencial.

- O jogador pode bloquear seu traço especial durante tempo indeterminado para receber +1d10(Mínimo 5).''')
    elif info == '3':
        return print('Voltando')
    else: 
        return print('opção invalida')

compra_status = roll_status()