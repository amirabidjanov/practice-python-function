balance = 0

def deposite(a:int):
    global balance
    if a > 0:
        balance += a
    else:
        print("manfiy son kiritmang!")

def withdraw(a:int):
    global balance
    if a <= balance:
        balance -= a
    else:
        print("manlag' yetarli emas!")

def check_balance():
    print(balance)

def menyu():
    print('<----------->')
    print('1: balance')
    print('2: deposit')
    print('3: withdraw')
    print('4: stop')
    print('<----------->')

def tekshiruv():
    while True:
        menyu()
        a = int(input("menyu bo'yicha: "))
        
        if a == 1:
            check_balance()
        elif a == 2:
            summa = int(input("qancha pul qo'shasiz: "))
            deposite(summa)
        elif a == 3:
            summa = int(input("qancha pul yechasiz: "))
            withdraw(summa)
        elif a == 4:
            print("salomat bo\'ling!")
            break

        
tekshiruv()

