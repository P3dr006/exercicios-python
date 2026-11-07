

alunos = ["pedro 7 8\n","tHiago 2 4\n","yurI 1 10\n","MigUel 4 9\n"]

novo_aluno = input("Digite o nome do aluno, seguido das notas (ex: 'João 5 7'): ")
alunos.append(novo_aluno + "\n")

with open("alunos.txt", "w") as arquivo:
    for linha in alunos:
        arquivo.writelines(linha)

ListaTeste = [Aluno.split() for Aluno in alunos]
Numero = 1
valor = {}
entrada_das_linhas = []

for aluno in ListaTeste:
   media = int(aluno[1]) + int(aluno[2]) /2
   valor[aluno[0].lower()] = f"({int(aluno[1])}, {int(aluno[2])})"
    
   if media >= 7:
    valor[aluno[0].lower()] += "aprovado"
    mensagem = f"""Aluno: {aluno[0]} Aprovado
    Notas: {aluno[1]} e {aluno[2]}
    Média: {media}\n"""
    # print(mensagem) 
    entrada_das_linhas.append(mensagem)
    
    Aprovado =+1

   else:
    valor[aluno[0].lower()] += "Reprovado"
    mensagem = f"""Aluno: {aluno[0]} Reprovado
    Notas: {aluno[1]} e {aluno[2]}
    Média: {media}\n"""
    # print(mensagem) 
    entrada_das_linhas.append(mensagem)
    Reprovados = +1
    

   with open("relatorio.txt", "w") as arquivo:
    for linha in entrada_das_linhas:
        arquivo.write(linha)
    arquivo.write(f"Total de Aprovados: {Aprovado}\n")

   with open("relatorio.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)
   
   