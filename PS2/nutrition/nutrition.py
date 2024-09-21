d = {"apple": 130, 
     "avocado": 50,
     "banana": 110,
     "cantaloupe": 50,
     "grapefruit": 60,
     "grapes": 90}

def main():
    f = input("Item: ").strip().lower()
    if  f in d:
        print(f'Calories: {d[f]}')

if __name__ == "__main__":
    main()