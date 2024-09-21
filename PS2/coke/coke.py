def main():
    a = 50
    while a > 0:
        a -= int(input(f'Amount Due: {a}\nInsert Coin: '))
        if a <= 0:
            print(f'Change owed: {-a}')

if __name__ == "__main__":
    main()