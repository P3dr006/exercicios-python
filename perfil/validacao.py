from perfil.usuario import criar_perfil
def validacao(idade,usuario):
    if idade >= 18:
        criar_perfil(usuario,idade)
        print (criar_perfil)
    else:
        print('voce e menor de idade')    