def qoshish(a,b):
    return a + b


def ayiruv(a,b):
    return a - b


def kopaytiruv(a,b):
    return a * b


def boluv(a,b):
    if b != 0:
        return a/b 
    else:
        None
def main():
    a = float(input('son kiriting:'))
    b = float(input('son kiriting:'))
    op = input('amal:')

    if op == "+":
        print(qoshish(a,b))
    elif op == "-":
        print(ayiruv(a,b))
    elif op == "*":
        print(kopaytiruv(a,b))
    elif op == "/":
        result = boluv(a,b)
        if result == None:
            print('0ga bo\'lish mumkin emas.')
        else:
            print(result)
    else:
        print('bunday amal yo\'q')
main()