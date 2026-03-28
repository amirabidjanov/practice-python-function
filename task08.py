def farenheit(a):
    return a * (9/5) + 32
    
def celsius(a):
    return a - 32 + 5 / 9


def tekshirish():
    a = float(input('farenheit kiriting:')) 
    b = float(input('celsius kiriting:'))
    

    print(f'fahrenheit: {farenheit(a)}----celcius: {celsius(b)}')


tekshirish()