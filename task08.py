def farenheit(a: float):
    return a * (9/5) + 32
    
def celsius(b: float):
    return b - 32 + 5 / 9


def tekshirish():
    a = float(input('farenheit kiriting:')) 
    b = float(input('celsius kiriting:'))
    

    print(f'fahrenheit: {farenheit(a)}----celcius: {celsius(b)}')


tekshirish()