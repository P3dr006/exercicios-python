from datetime import datetime,timedelta

def dias_ate_ano_nova():
    
  final_ano = datetime(2025,12,31)

  falta = (final_ano - datetime.now())

  print (f'falta {falta.days} dias ate o ano novo')
  
def  data_evento():
    
    agora = datetime.now()
    
    data_evento = input('insira a data do seu evento (Formato: 2025/08/19)')
    
    data = datetime.strptime (data_evento, "%Y/%m/%d")
    
    falta = data - agora + timedelta(days=1)
    
    print (data)
    
    if data.day == agora.day and data.month == agora.month and data.year == agora.year:
        
        print ('o evento sera hoje')
        
    elif data.day <= agora.day and data.month <= agora.month and data.year <= agora.year:
        
        print ('ja aconteceu esse evento')
        
    elif data.day >= agora.day and data.month >= agora.month and data.year >= agora.year:
        
        print(f'falta {falta.days}dia para o evento')        
    
    
def data_validacao2():
    
    agora = datetime.now().date()
    
    data_produto = input('insira a data do seu evento (Formato: 2025/08/19)')
    
    data = datetime.strptime(data_produto, "%Y/%m/%d").date()
    
    aleatorio = agora
    
    
    if data > agora :
        
        vencimento =  data - agora +timedelta(days=1)
        print(f'produto ainda tem {vencimento.days} ate o dia de vencimento')    
        
    elif data < agora:
        
        vencimento = (data - agora) * -1
        print(f'o produto venceu faz {vencimento.days} dias')   
        
    else:
        
        print('hoje e a data de vencimento')    

data_validacao2()      
  
    
    