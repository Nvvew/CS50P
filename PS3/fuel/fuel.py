def main():
    while True:
        frac = input("Fraction: ")
        try:
            print(convert(frac))
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

def convert(frac):
    x, y = frac.split('/')[0:2]
    if not x.isdigit() and y.isdigit():
        raise ValueError
    f = int(x)/int(y)
    if f < 0 or f > 1:
        raise ValueError
    elif f <= 0.01:
        return("E")
    elif f >= 0.99:
        return("F")
    else:
        return(f'{int(f*100)}%')

if __name__ == "__main__":
    main()