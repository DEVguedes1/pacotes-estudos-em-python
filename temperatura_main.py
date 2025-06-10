from utilitarios import conversores

while True:
    try:
        print("1- conversão celsius para fahrenheit")
        print("2- conversão fahrenheit para celsius")
        print("3- SAIR")
        entrada=float(input("digite uma das opções acima:"))
    
    except:
        print("opção inválida")
        
    match entrada:
        case 1:
            temperatura=float(input("digite a temperatura que você quer converter:"))
            conversores.cels_for_faren(temperatura)
        case 2:
            temperatura=float(input("digite a temperatura que você quer converter:"))
            conversores.faren_for_cels(temperatura)
        case 3:
            break
        case _:
            print("opção inválida")