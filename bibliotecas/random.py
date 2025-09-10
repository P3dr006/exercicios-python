from random import randint

aleatorio = randint(1,10)
num2 = 0
num1 = ()
while aleatorio!=num1:
 num1 = int(input('insira um numero')) 
 num2 +=1    
 if aleatorio > num1:
    print('muito baixo')
    
 elif aleatorio == num1:
    print('acerto')
    
 elif aleatorio < num1:
    print('muito alto') 
    
 print(num2)          