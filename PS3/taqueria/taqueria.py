price = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price = {k.lower(): v for k, v in price.items()}

def main():
    tp = 0
    while True:
        try:
            tp += price[input("Item: ").lower()]
            print(f'Total: ${tp}')
        except KeyError:
            pass

if __name__ == "__main__":
    main()