def son(a: int):
    num = a % 2 == 0
    return num


def tekshiruv():
    a = int(input('son kiriting:'))

    num = son(a)
    
    if num == 0:
        print('toq son')
    else:
        print('juft son')

tekshiruv()