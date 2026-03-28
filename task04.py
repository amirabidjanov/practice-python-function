def num(num):
    num = int(input('ball kiriting:'))
    
    
    if 0 <= num <= 59:
        print('D')
    elif 60 <= num <= 69:
        print('F')    
    elif 70 <= num <= 79:
        print('C')
    elif 80 <= num <= 89:
        print('B')
    elif 90 < num <= 100:
        print('A')
    else:
        print('0 va 100 oralig\'ida bo\'lsin!')
num(num)