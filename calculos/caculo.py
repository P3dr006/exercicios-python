i = 1
somar = 1
valor = 0
valor_final = 0

while i <=99:
    print(valor)
    valor_final += valor
    valor += somar
    
    i+=1

print (valor_final +100)
print (f'''valor somando do rank 100 até 99 = {valor_final}
esse valor + 100 do top 1 é = {valor_final+100}''')
    
