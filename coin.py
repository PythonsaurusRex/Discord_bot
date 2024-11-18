import random

def flip_coin():
    
    coin = random.randint(0,1)
    
    if coin == 0:
        return 'heads'
    
    else:
        return 'tails'