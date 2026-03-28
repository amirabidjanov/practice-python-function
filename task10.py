def password():
    result = input("password kiriting:")
    return result


def len_password():

    result = password()


    if len(result) >= 8:
        print('kuchli password!')
    else:
        print('kuchsiz password!')
    

len_password()