# Inicio del programa Conjutos
# Autor: E.A.H.
# Fecha: 09/Abril/2019

def U(x,y):
    un = []
    for i in x:
        if i in y:
            continue
        else:
            un.append(i)
    return (un + y)

def I(x,y):
    inter = []
    for i in x:
        if i in y:
            inter.append(i)
        else:
            continue
    return (inter)

def C(x,y):
    com_uni = []
    for i in y:
        if i in x:
            continue
        else:
            com_uni.append(i)
    return (com_uni)

def D(x,y):
    rest = []
    for i in x:
        if i in y:
            continue
        else:
            rest.append(i)
    return (rest)

def DS(x,y):
    dif_1 = []
    dif_2 = []

    for i in x:
        if i in y:
            continue
        else:
            dif_1.append(i)
    for j in y:
        if j in x:
            continue
        else:
            dif_2.append(j)
    dif_sim = dif_1+dif_2

    return (dif_sim)

def ordenamiento(lista):
    intercambios = True
    numPasada = len(lista) -1
    while numPasada > 0 and intercambios:
        intercambios = False
        for i in range(numPasada):
            if lista[i] > lista[i+1]:
                intercambios = True
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i+1] = temp
        numPasada = numPasada-1
    return lista

def main():
    # Tabla de datos
    u=[1,2,5,6,8,9,10]
    a=[1,2,5,9]
    b=[5,8,9,10]
    c=[1,2,4,6,8]

    # EJERCICIO 3.2 DEL CAPÍTULO 3 DEL LIBRO "ESTADÍSTICA I, FUNDAMENTOS DE PROBABILIDAD Y ESTADÍSTICA", BY MTRA. SILVIA SÁNCHEZ DÍAZ

    print("a)", U(a,b) )                  # Union de A y B
    print("b)", I(a, b) )                 # Intersección de A y B
    print("c)", U(a, c) )
    print("d)", I(U(a,c),C(b,u)) )
    print("e)", I(a, c) )
    print("f)", C(a,u) )                  # Complemento de A
    print("g)", C(b, u) )
    print("h)", C(c, u) )
    print("i)", I(U(b,c),a) )
    print("j)", I(U(b,c), b ) )
    print("k)", U(U(C(b,u),C(c,u)), a) )
    print("l)", U(C(b,u),C(c,u)) )
    print("m)", I(C(b,u),C(c,u)) )
    print("n)", D(a,c) )                  # Diferencia de A y C
    print("o)", DS(a,c) )
    print("p)", ordenamiento( DS(a,c)) )  # Diferenca simetrica ordenada de A y C


main()