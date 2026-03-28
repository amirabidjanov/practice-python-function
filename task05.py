from random import randint 

def taxminiy_son():
    random_son = randint(1, 20)
    return random_son


def tekshirish():
    random_son = taxminiy_son()
    a = int(input("1 dan 20 gacha son kiriting: "))
    while 1 <= a <= 20 :
        if a == random_son:
            print('topdingiz')
            break
        elif a > random_son:
            print('kichikroq')
        elif a < random_son:
            print('kattaroq')
        else:
            print('son 1 dan 20 oralig\'ida')
        a = int(input("1 dan 20 gacha son kiriting: "))
    
tekshirish()