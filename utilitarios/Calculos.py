def dobro(a) -> int:
    dobro_resultado = a * 2
    return print(dobro_resultado)

def triplo(a) -> int:
    triplo_resultado = a * 3
    return print(triplo_resultado)

def parouimpar(a) -> int:
    par = False
    resultado = a % 2
    if resultado == 0:
        print(f"{a} é par")
    else:
        print(f"{a} é impar")