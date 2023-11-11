
def redondear(numero):
    entero=int(numero)
    decimal=numero-entero
    if decimal>0.50:
        return entero+1
    else:
        return entero


