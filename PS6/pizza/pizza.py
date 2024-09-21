import sys
import os
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        sys.exit('No')

    if not (file.endswith('.csv') and os.path.isfile(file)):
        sys.exit('Not a CSV file.')
    
    try:
        with open(file, newline='') as file:
            reader = csv.reader(file)
            table = [row for row in reader]
        
        print(tabulate(table, tablefmt='grid'))
    
    except Exception as e:
        sys.exit(f"An error occurred: {e}")


if __name__ == "__main__":
    main()