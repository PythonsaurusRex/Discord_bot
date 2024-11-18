import random

def gen_pass(longitud):
    
    caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    psw_generada = ""

    for i in range(longitud):
        psw_generada += random.choice(caracteres)
    return psw_generada



