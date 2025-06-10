from utilitarios import Calculos

print("digite x para sair")
while True:
    try:
        entrada=input("digite um valor:").lower()
    except:
        print("digite um numero!")
        
    if entrada == "x":
        break
    
    valor = int(entrada)
    
    Calculos.parouimpar(valor)
    Calculos.dobro(valor)
    Calculos.triplo(valor)