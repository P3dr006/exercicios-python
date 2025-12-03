def imovel_plano_linear():
    credito = float(input("Digite o valor do credito"))
    duracao = int(input("Digite a duracao do emprestimo em meses"))
    taxa_juros = float(input("Digite a taxa de juros ao mes (em porcentagem)")) / 100
    parcela_capital = credito / duracao
    print(f"\n{'Mes':<5}{'Parcela Capital':<20}{'Parcela Juros':<20}{'Parcela Total':<20}{'Saldo Devedor':<20}")
    saldo_devedor = credito
    for mes in range(1, duracao + 1):
        parcela_juros = saldo_devedor * taxa_juros
        parcela_total = parcela_capital + parcela_juros
        saldo_devedor -= parcela_capital
        print(f"{mes:<5}{parcela_capital:<20.2f}{parcela_juros:<20.2f}{parcela_total:<20.2f}{saldo_devedor:<20.2f}")
imovel_plano_linear()        