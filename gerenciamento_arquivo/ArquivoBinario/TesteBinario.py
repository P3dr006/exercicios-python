def copia_binario():
    # Abre o arquivo dados.bin em modo binário para escrita (write-binary)
    # e grava os bytes definidos na lista.
    with open("dados.bin", "wb") as arquivo:
        arquivo.write(bytes([67, 32, 16, 73, 23]))

    # Abre o mesmo arquivo em modo binário de leitura (read-binary)
    # e lê todo o conteúdo em uma variável chamada dados.
    with open("dados.bin", "rb") as arquivo:
        dados = arquivo.read()

    # Cria um novo arquivo copia.bin e grava nele os mesmos bytes lidos.
    with open("copia.bin", "wb") as arquivo:
        arquivo.write(dados)

    # Abre o arquivo copia.bin para leitura e imprime os bytes como lista
    # de valores numéricos, para facilitar a visualização do conteúdo.
    with open("copia.bin", "rb") as arquivo:
        print(list(arquivo.read()))

def modifica_binario():
    # Abre o arquivo dados.bin em modo binário de leitura (read-binary)
    # e lê todo o conteúdo, imprimindo os bytes como lista de valores numéricos
    # para visualizar o conteúdo original.
    with open("dados.bin", "rb") as arquivo:
        print(list(arquivo.read()))
        
    # Abre novamente o arquivo dados.bin em modo binário de leitura
    # e lê o conteúdo em um bytearray para permitir modificações.
    with open("dados.bin", "rb") as arquivo:
        dados = bytearray(arquivo.read())

    # Modifica os primeiros dois bytes do bytearray com novos valores.
    dados[0] = 234
    dados[1] = 123

    # Cria um novo arquivo modificado.bin em modo binário para escrita
    # e grava nele os bytes modificados.
    with open("modificado.bin", "wb") as arquivo:
        arquivo.write(dados)

    # Abre o arquivo modificado.bin para leitura e imprime os bytes como lista
    # de valores numéricos, para visualizar o conteúdo modificado.
    with open("modificado.bin", "rb") as arquivo:
        print(list(arquivo.read()))

modifica_binario()