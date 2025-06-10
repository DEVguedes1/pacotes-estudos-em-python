from utilitarios.conversores import *

while True:
    try:
        print("\n")
        print("=================MENU==================")
        print("1- conversão temperaturas")
        print("2- conversão de pesos")
        print("3- conversão de distância")
        print("4- SAIR")
        entrada=float(input("digite uma das opções acima:"))
    
    except:
        print("opção inválida")
        
    if entrada == 1:
        while True:
            try:
                print("\nTEMPERATURAS")
                print("1- conversão celsius para fahrenheit")
                print("2- conversão fahrenheit para celsius")
                print("3- SAIR")
                opcao=float(input("digite uma das opções acima:"))
                print("\n")
            
            except:
                print("opção inválida")
                
            match opcao:
                case 1:
                    temperatura=float(input("digite a temperatura que você quer converter:"))
                    cels_for_faren(temperatura)
                case 2:
                    temperatura=float(input("digite a temperatura que você quer converter:"))
                    faren_for_cels(temperatura)
                case 3:
                    break
                case _:
                    print("opção inválida")
    elif entrada == 2:
                while True:
                    try:
                        print("\nPESOS")
                        print("1- grama para kilogramas")
                        print("2- grama para hectogramas")
                        print("3- grama para decagramas")
                        print("4- grama para decigramas")
                        print("5- grama para centigramas")
                        print("6- grama para miligramas")
                        print("7- SAIR")
                        opcao=float(input("digite uma das opções acima:"))
                        print("\n")
                    except:
                        print("opção inválida")
                        
                    match opcao:
                        case 1:
                            peso=float(input("digite o peso em kilos que você vai converter:"))
                            g_for_kg(peso)
                        case 2:
                            peso=float(input("digite o peso em kilos que você vai converter:"))
                            g_for_hg(peso)
                        case 3:
                            peso=float(input("digite o peso em kilos que você vai converter:"))
                            g_for_dag(peso)
                        case 4:
                            peso=float(input("digite o peso em kilos que você vai converter:"))
                            g_for_dg(peso)
                        case 5:
                            peso=float(input("digite o peso em kilos que você vai converter:"))
                            g_for_cg(peso)
                        case 6:
                            peso=float(input("digite o peso em kilos que você vai converter:"))
                            g_for_mg(peso)
                        case 7:
                            break
                        case _:
                            print("invalido")
    elif entrada == 3:
                while True:
                    try:
                        print("\nDISTANCIAS")
                        print("1- metro para kilometro")
                        print("2- metro para hectometro")
                        print("3- metro para decametro")
                        print("4- metro para decimetro")
                        print("5- metro para centimetro")
                        print("6- metro para milimetro")
                        print("7- SAIR")
                        opcao=float(input("digite uma das opções acima:"))
                        print("\n")
                    except:
                        print("opção inválida")
                        
                    match opcao:
                        case 1:
                            distancia=float(input("digite o distancia em metros que você vai converter:"))
                            m_for_km(distancia)
                        case 2:
                            distancia=float(input("digite o distancia em metros que você vai converter:"))
                            m_for_hm(distancia)
                        case 3:
                            distancia=float(input("digite o distancia em metros que você vai converter:"))
                            m_for_dam(distancia)
                        case 4:
                            distancia=float(input("digite o distancia em metros que você vai converter:"))
                            m_for_dm(distancia)
                        case 5:
                            distancia=float(input("digite o distancia em metros que você vai converter:"))
                            m_for_cm(distancia)
                        case 6:
                            distancia=float(input("digite o distancia em metros que você vai converter:"))
                            m_for_mm(distancia)
                        case 7:
                            break
                        case _:
                            print("invalido")
    elif entrada==4:
        print("\nsaindo...")
        break
    else:
        print("\nopcao invalida")
    
   
