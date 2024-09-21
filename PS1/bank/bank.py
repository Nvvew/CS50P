def main():
    g = input("Greeting: ")
    print(f'${value(g)}')

def value(g):
    g2 = g.replace(" ", "").lower()
    if g2[0] != "h":
        return 100
    else:
        try:
            g3 = g2[:5]
        except IndexError:
            return 20
        else:
            if g3 == "hello":
                return 0
            else:
                return 20

if __name__ == "__main__":
    main()