def calculate_tax(salary):
    if salary > 5_000_000:
        return salary
    else:
        return salary * 0.13
    

def calculate_net_salary(salary):
    return salary - calculate_tax(salary)


def main():
    amout = float(input("oylik:"))


    tex = calculate_tax(amout)
    print(f"soliq: {tex:,.2f}so'm")

    net_salary = calculate_net_salary(amout)
    print(f"daromad: {net_salary:,.2f}so'm")
    

main()