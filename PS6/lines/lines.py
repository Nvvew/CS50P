import argparse
import sys
import os

parser = argparse.ArgumentParser(description='Name of the file.')
parser.add_argument('name', help='file name')
args=parser.parse_args()

def main():
    name = args.name
    file = name.replace('.py', '')
    path = f'../../PS0/{file}/{name}'

    if not (name.endswith('.py') and os.path.isfile(path)):
        sys.exit('Not a python file.')
    
    print(lines(path))

def lines(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
        
        count = 0
        for line in lines:
            if line.strip() and not line.strip().startswith("#"):
                count += 1
        
        return count
    
    except FileNotFoundError():
        sys.exit('File does not exist.')

if __name__ == "__main__":
    main()