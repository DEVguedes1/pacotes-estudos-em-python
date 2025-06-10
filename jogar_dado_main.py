from utilitarios.dado import *

while True:
    entrada=int(input("""escolha um dado->
1 - dado 6 lados
2 - dado 10 lados
3 - dado 20 lados
qual vc quer?"""))
    
    match entrada:
        case 1:
            dado_seis(6)
        case 2:
            dado_dez(10)
        case 3:
            dado_vinte(20)
        case _:
            print("invalido")

    opcao=input("digite x para sair:").lower()
    if opcao == "x":break