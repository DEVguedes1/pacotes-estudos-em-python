from utilitarios import analises

while True:
    texto=input("digite oq quiser aqui:")
    try:
        num=float(input("digite um numero aqui:"))
    except:
        print("formato invalido")
        
    analises.contar_letras(texto)
    analises.e_primo(num)
    
    opcao=input("digite x para sair ->").lower()
    if opcao=="x":
        break