def main():
    t = input("What time is it? ").strip()
    t2 = convert(t)
    
    if t2 >= 7 and t2 <= 8:
        print("breakfast time")
    elif t2 >= 12 and t2 <= 13:
        print("lunch time")
    elif t2 >= 18 and t2 <= 19:
        print("dinner time")
    else:
        print("Not meal time")

def convert(t):
    x, y = t.split(":")
    x, y = float(x), float(y)
    return x + y/60

if __name__ == "__main__":
    main()