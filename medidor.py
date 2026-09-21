Imovel = str (input("Tipo do imovel: ").lower())
Consumo = float (input("Consumo em m3: "))

##processamento    
if Imovel.strip() == "comercial":
  print ("Tarifa comercial aplicada, consulte o plano corporativo.")

elif Imovel.strip()== "apartamento" and Consumo <10: 
    
    print ("excelente controle de água!")

elif  Imovel.strip == "apartamento" or "casa" and Consumo <26:
    print ("Consumo moderado – dentro do padrão residencial.")   

else: 
 print  ("Consumo excessivo – adote medidas de economia e verifique vazamentos")