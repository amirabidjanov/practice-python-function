def phone_num(num):
    return len(num) == 9


def tekshiruv():
    while True:
        a = input('tel nomer kiriting (9 ta raqam): ')
        
        if phone_num(a):
            print('qabul qilindi')
            break
        else:
            print('xato')

tekshiruv()