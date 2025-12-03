def consorcio_imovel():
    valor = float(100000)
    prazo = float(40)    
    taxa_administrativa = 0.13
    seguro = 0.0380
 

    valor = valor / prazo
    valor = valor * (1 + taxa_administrativa+ seguro)
   
    
    parcela_mensal = valor 

    

    print (f"{parcela_mensal:.2f}")
consorcio_imovel()
