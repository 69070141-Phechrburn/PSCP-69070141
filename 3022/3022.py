"""temp"""
def main():
    """temp"""
    units = float(input())
    kra = input()
    krra = input()
    to_celcius = 0
    if kra == "C":
        to_celcius = units
    elif kra == "K":
        to_celcius = units - 273.15
    elif kra == "F":
        to_celcius = (units - 32) / 1.8
    elif kra == "R":
        to_celcius = (units / 1.8) - 273.15
    if krra == "C":
        print(f"{to_celcius:.2f}")
    elif krra == "K":
        print(f"{to_celcius + 273.15:.2f}")
    elif krra == "F":
        print(f"{to_celcius * 1.8 + 32:.2f}")
    elif krra == "R":
        print(f"{(to_celcius + 273.15) * 1.8:.2f}")

main()
