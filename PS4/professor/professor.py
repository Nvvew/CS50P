import random

def main():
    l = get_level()
    score = 10
    for i in range(10):
        str, ans = gi(l)
        c = 0
        while True:
            try:
                if int(input(str)) == ans:
                    break
                else:
                    print("EEE")
                    c += 1
            except ValueError:
                print("EEE")
                c += 1
            if c == 3:
                print(str + f'{ans}')
                score -= 1
                break
    
    print(f"Your score is {score}")
def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if 1 <= l <= 3:
                return l
        except ValueError:
            pass

def gi(l):
    x = int(random.uniform(0.1, 1.0)*10**(l))
    y = int(random.uniform(0.1, 1.0)*10**(l))
    return f'{x} + {y} = ', x + y

if __name__ == "__main__":
    main()