def BMI_m():
    m = float(input("bo'yingiz:"))
    if not 1 <= m <= 3:
        print("bo'y 1 dan 3 oralig'ida kiriting")
        return None
    return m


def BMI_kg():
    kg = float(input("vazningin:"))
    if not 1 <= kg <= 200:
        print("vazn 1dan 200 oralig'ida kiriting")
        return None
    return kg


def hisob():
    m = BMI_m()
    kg = BMI_kg()

    if m is None or kg is None:
        return

    result = kg / (m ** 2)
    
    if result <= 18.5:
        print("ozg'in")
    elif 18.5 <= result <= 24.9:
        print("normal")
    elif 24.9 <= result <= 29.9:
        print("ortiqcha vazn")
    elif 30 <= result:
        print("semiz")


hisob()

