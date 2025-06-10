def contar_letras(text) -> str:
    cont=0
    for letras in text:
        cont+=1
    return print(f"ele tem {cont} letras")

def e_primo(numero):
  if numero <= 1:
    return print(f"{numero} não é primo")
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return print(f"{numero} não é primo")
  return print(f"{numero} é primo")  