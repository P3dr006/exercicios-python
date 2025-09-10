from calculos.matematica import saudacao,metade,dobro
from perfil.usuario import criar_perfil
from perfil.validacao import validacao

nome = input('insira seu nome ')
idade = int(input('insira sua idade'))
idade2 = idade

validacao(idade,nome)

