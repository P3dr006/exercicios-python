
produtos = {
    "frutas": {
        "uva": 3,
        "maca": 4,
        "abacaxi": 7
    },
    "eletronicos": {
        "celular": 300,
        "tv": 500,
        "geladeira": 800
    }
}

carrinho = {
    'frutas': [],
    'eletronicos': []
}

dinheiro_em_conta = 100.00

usuario = {
    'usuario': 'admin',
    'senha': 'admin123',
}

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


while True:
    
    print(f'\nSeja muito bem-vindo Sr.{usuario["usuario"]} ao supermercado\n')
    
    mercado = input('''
-----------menu-----------
[1] ver conta
[2] ver mercadorias
[3] sair
--------------------------
''')
    
    if mercado == '1':
        
        while True:
            
            print(f'\nSeu saldo é de R$ {dinheiro_em_conta:.2f}\n')
            sistema_banco = input('''
-----------conta bancaria-----------               
[1] adicionar dinheiro
[2] retirar dinheiro
[3] voltar ao menu anterior
-------------------------------------
''')
            if sistema_banco == '1':
                
                adicionar = float(input('\nQuanto deseja adicionar? R$ '))
                
                if adicionar <= 0:
                    
                    print('Valor inválido, tente novamente.')
                    
                else:
                    
                    dinheiro_em_conta += adicionar
                    print(f'Seu novo saldo é de R$ {dinheiro_em_conta:.2f}')
                    
            elif sistema_banco == '2':
                
                retirar = float(input('Quanto deseja retirar? R$ '))
                
                if retirar <= 0:
                    
                    print('Valor inválido, tente novamente.')
                    
                elif retirar > dinheiro_em_conta:
                    
                    print('Saldo insuficiente para essa operação.')
                    
                else:
                    
                    dinheiro_em_conta -= retirar
                    print(f'Seu novo saldo é de R$ {dinheiro_em_conta:.2f}')
                    
            elif sistema_banco == '3':
                
                break
            else:
                
                print('Opção inválida!')

    elif mercado == '2':
        
        while True:
            
            sistema_mercado = input('''
-----------mercadinho-----------  
[1] ver todos produtos
[2] ver frutas
[3] ver eletronicos
[4] finalizar pagamento
[5] remover item do carrinho
[6] voltar ao menu anterior
--------------------------------
''')
          
            if sistema_mercado == '1':
                lista_produtos = []
                contador = 1
                
                for categoria, itens in produtos.items():
                    
                    print(f"\n{categoria.capitalize()}:")
                    
                    for nome, preco in itens.items():
                        
                        preco = int(preco)
                        print(f"{contador}. {nome.capitalize()} - R$ {preco}")
                        lista_produtos.append((categoria, nome, preco))
                        contador += 1
                numero = int(input("\nDigite o número do produto que deseja adicionar ao carrinho (0 para cancelar): "))
                
                if numero == 0:
                    
                    print("Nenhum produto adicionado.")
                    
                elif 1 <= numero <= len(lista_produtos):
                    
                    categoria, nome, preco = lista_produtos[numero - 1]
                    carrinho[categoria].append((nome, preco))
                    print(f"{nome.capitalize()} adicionado ao carrinho!")
                    
                else:
                    
                    print("Número inválido!")

            
            elif sistema_mercado == '2':
                
                frutas = produtos['frutas']
                lista_produtos = list(frutas.items())
                print("Frutas disponíveis:")
                for i, (nome, preco) in enumerate(lista_produtos, start=1):
                    
                    print(f"{i}. {nome.capitalize()} - R$ {preco}")
                numero = int(input("Digite o número do produto que deseja adicionar ao carrinho (0 para cancelar): "))
                
                if numero == 0:
                    
                    print("Nenhum produto adicionado.")
                    
                elif 1 <= numero <= len(lista_produtos):
                    
                    chave, valor = lista_produtos[numero - 1]
                    carrinho['frutas'].append((chave, valor))
                    print(f"{chave.capitalize()} adicionado ao carrinho!")
                    
                else:
                    
                    print("Número inválido!")

            elif sistema_mercado == '3':
                
                eletronicos = produtos['eletronicos']
                lista_produtos = list(eletronicos.items())
                print("Eletrônicos disponíveis:")
                
                for i, (nome, preco) in enumerate(lista_produtos, start=1):
                    
                    print(f"{i}. {nome.capitalize()} - R$ {preco}")
                numero = int(input("Digite o número do produto que deseja adicionar ao carrinho (0 para cancelar): "))
                
                if numero == 0:
                    
                    print("Nenhum produto adicionado.")
                    
                elif 1 <= numero <= len(lista_produtos):
                    
                    chave, valor = lista_produtos[numero - 1]
                    carrinho['eletronicos'].append((chave, valor))
                    print(f"{chave.capitalize()} adicionado ao carrinho!")
                    
                else:
                    
                    print("Número inválido!")

            elif sistema_mercado == '4':
                
                print("\nCarrinho atual:")
                
                for categoria, itens in carrinho.items():
                    
                    print(f"{categoria.capitalize()}:")
                    
                    for i, (nome, preco) in enumerate(itens, start=1):
                        
                        print(f"{i}. {nome.capitalize()} - R$ {preco}")
                        
                total = sum(preco for itens in carrinho.values() for _, preco in itens)
                
                print(f"\nTotal a pagar: R$ {total}")
                
                if total == 0:
                    
                    print("Seu carrinho está vazio!")
                    
                elif total > dinheiro_em_conta:
                    
                    print("Saldo insuficiente para finalizar a compra!")
                    
                else:
                    
                    dinheiro_em_conta -= total
                    print(f"Compra realizada com sucesso! Novo saldo: R$ {dinheiro_em_conta:.2f}")
                    
                    for categoria in carrinho:
                        carrinho[categoria] = []

         
            elif sistema_mercado == '5':
                
                print("\nItens no carrinho:")
                
                for categoria, itens in carrinho.items():
                    
                    print(f"{categoria.capitalize()}:")
                    
                    for i, (nome, preco) in enumerate(itens, start=1):
                        
                        print(f"{i}. {nome.capitalize()} - R$ {preco}")
                        
                cat = input("De qual categoria deseja remover o item? (frutas/eletronicos): ").lower()
                
                if cat not in carrinho or len(carrinho[cat]) == 0:
                    
                    print("Categoria inválida ou carrinho vazio!")
                    
                else:
                    
                    for i, (nome, preco) in enumerate(carrinho[cat], start=1):
                        
                        print(f"{i}. {nome.capitalize()} - R$ {preco}")
                    numero = int(input("Digite o número do item que deseja remover (0 para cancelar): "))
                    
                    if numero == 0:
                        
                        print("Nenhum item removido")
                        
                    elif 1 <= numero <= len(carrinho[cat]):
                        
                        removido = carrinho[cat].pop(numero-1)
                        print(f"{removido[0].capitalize()} removido do carrinho!")
                        
                    else:
                        print("Número inválido!")

           
            elif sistema_mercado == '6':
                
                break
            
            else:
                
                print("Opção inválida! Tente novamente.")

    elif mercado == '3':
        
        print("Saindo do sistema...")
        break
    
    else:
        
        print("Opção inválida! Tente novamente.")
