import random
def contraseña_random():
    valores = "0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ[]{,}|@#~\€¬!·$%&/()=?¿¡!^*¨Ç_:;,.-"
    longitud = 8
    contraseña = ''
    for i in range(longitud):
        contraseña += valores[random.randint(0, len(valores)-1)]

    return contraseña

print(contraseña_random())


