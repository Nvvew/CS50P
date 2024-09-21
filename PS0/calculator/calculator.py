def main():
    dollars = dollars_to_float(input("How much was the meal?\n"))
    percent = percent_to_float(input("What percentage would you like to tip?\n"))
    tip = dollars*percent
    print(f'Leave ${tip}.')

def dollars_to_float(d):
    d2 = d.replace("$", "")
    return float(d2)

def percent_to_float(p):
    p2 = p.replace("%", "")
    p3 = float(p2)
    return p3/100

main()