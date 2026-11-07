## lista de bytes
dados = bytes([67,32,16,73,23])

## escrevendo os dados em um arquivo binário (wb = write binary)
with open("dados.bin", "wb") as arquivo:
    arquivo.write(dados)

## lendo os dados do arquivo binário (rb = read binary)
with open("dados.bin", "rb") as arquivo:
    dados_lidos = arquivo.read()

    ## dois formatos de exibição dos dados lidos
    
    print(dados_lidos) ## exibe os dados como bytes

    ## exibe os dados como uma lista sendo inteiros ou strings dependendo do formato de exibição escolhido (pega os bytes e transforma em uma lista de inteiros)
    print(list(dados_lidos))