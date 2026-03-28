def yosh(a: int,b: int):
    age = b - a
    return age


def tekshiruv():
    a = int(input('yilingizni kiriting:'))   
    b = int(input('hozirgi yilini kiriting:')) 
    
    age = yosh(a, b)

    if age < 18:
        print('siz balog\'atga yetmagansiz')     
    elif age >= 18:
        print('siz balog\'at yoshdasiz')

tekshiruv()

