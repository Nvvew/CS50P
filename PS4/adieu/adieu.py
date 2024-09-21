def main():
    names = get_name()
    print(fmt(names))

def get_name():
    names = []
    try:
        while True:
            name = input("Name: ")
            if name:
                names.append(name)
            else:
                return names
    except EOFError:
        pass

def fmt(names):
    if len(names) == 0:
        return"Please enter names."
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    if len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[-1]}"
    if len(names) >= 3:
        return "Adieu, adieu, to " + ",".join(names[:-1]) + ", and " + names[-1]

if __name__ == "__main__":
    main()
