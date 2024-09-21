def main():
    while True:
        str = input("Date: ")
        date = parse(str)
        if date:
            print(fmt(*date))
            break
        else:
            pass
    
def parse(str):
    months = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    
    y, m, d = 0, 0, 0

    try:
        m, d, y = map(int, str.split('/'))
    except ValueError:
        pass

    try:
        str = str.replace(',', '').strip()
        month, date, year = str.split(' ')
        m = months[month]
        d, y = map(int, [date, year])
    except (ValueError, KeyError):
        pass
    
    if is_valid_day(d) and is_valid_month(m):
        return y, m, d

def fmt(y, m, d):
    return f'{y:04d}-{m:02d}-{d:02d}'

def is_valid_day(x):
    return isinstance(x, int) and 1 <= x <= 31

def is_valid_month(y):
    return isinstance(y, int) and 1 <= y <= 12

if __name__ == "__main__":
    main()