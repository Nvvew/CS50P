import random as rd

def main():
    l = get_level()
    n = rd.randint(1, l)
    guess(n)

def get_level():
    while True:
        x = input("Level: ")
        try:
            if int(x) > 0:
                return int(x)
            else:
                pass
        except ValueError:
            pass

def guess(l):
    while True:
        try:
            x = int(input("Guess: "))
            if x < l:
                print("Too small!")
            elif x > l:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass

if __name__ == "__main__":
    main()