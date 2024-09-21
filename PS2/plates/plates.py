def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    for i, c in enumerate(s):
        if c.isdigit():
            if  int(c) == 0:
                return False
            else:
                if not s[i:].isdigit():
                    return False
            return True
    return True

if __name__ == "__main__":
    main()