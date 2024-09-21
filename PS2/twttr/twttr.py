def main():
    a = input("Input: ").strip()
    print(f"Output: {shorten(a)}")

def shorten(a):
    l = ['a', 'e', 'o', 'i', 'u']
    b = [x for x in a if not x.lower() in l]
    return ''.join(b)

if __name__ == "__main__":
    main()