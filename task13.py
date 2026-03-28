def text():
    text = input("soz kiriting:")
    if text == text[::-1]:
        print("to'g'ri")
    else:
        print("noto'g'ri")

text()