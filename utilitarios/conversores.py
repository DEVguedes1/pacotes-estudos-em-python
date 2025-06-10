# temperaturas
def cels_for_faren(x):
    f=((9/5) * x)+32
    return print(f,"ºF graus")

def faren_for_cels(x):
    c=((x-32)*5)/9
    return print(c,"ºC graus")

# pesos
def g_for_kg(valor) -> float:
    gramaParaKilos = valor / 1000
    return print(gramaParaKilos)

def g_for_hg(valor) -> float:
    gramaParaHecto = valor / 100
    return print(gramaParaHecto)

def g_for_dag(valor) -> float:
    gramaParaDeca = valor / 10
    return print(gramaParaDeca)

def g_for_dg(valor) -> float:
    gramaParaDeci = valor * 10
    return print(gramaParaDeci)

def g_for_cg(valor) -> float:
    gramaParaCenti = valor * 100
    return print(gramaParaCenti)

def g_for_mg(valor) -> float:
    gramaParaMili = valor * 1000
    return print(gramaParaMili)

# distancia

def m_for_km(valor) -> float:
    metroParaKilos = valor / 1000
    return print(metroParaKilos)

def m_for_hm(valor) -> float:
    metroParaHecto = valor / 100
    return print(metroParaHecto)

def m_for_dam(valor) -> float:
    metroParaDeca = valor / 10
    return print(metroParaDeca)

def m_for_dm(valor) -> float:
    metroParaDeci = valor * 10
    return print(metroParaDeci)

def m_for_cm(valor) -> float:
    metroParaCenti = valor * 100
    return print(metroParaCenti)

def m_for_mm(valor) -> float:
    metroParaMili = valor * 1000
    return print(metroParaMili)