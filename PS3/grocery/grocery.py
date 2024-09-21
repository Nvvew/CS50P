def main():
    d = {}
    while True:
        k = input().lower()
        if k:
            if k in d:
                d[k] += 1
            else:
                d[k] = 1
        else:
            for k in sorted(d.keys()):
                print(f'{d[k]} {k.upper()}')
            break
                
if __name__ == "__main__":
    main()