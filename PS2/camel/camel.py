def main():
    w = input("camelCase: ").strip()
    print(f'snake_case: {snake(w)}')

def snake(c):
    s = []
    for l in c:
        if l.isupper():
            s.append('_')
        s.append(l.lower())
    
    return ''.join(s)

if __name__ == "__main__":
    main()