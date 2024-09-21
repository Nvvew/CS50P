import argparse
import sys
import random
from pyfiglet import Figlet


parser = argparse.ArgumentParser(description="Choose your font.")
parser.add_argument("-f", "--font", help="The font name(optional)")
args = parser.parse_args()

figlet = Figlet()
l = figlet.getFonts()

def main():
    if args.font:
        if not args.font in l:
            sys.exit("Invalid Font Name")
        else:
            figlet.setFont(font=args.font)
            str = input("Input: ")
            print(figlet.renderText(str))
    
    else:
        f = random.choice(l)
        figlet.setFont(font=f)
        str = input("Input: ")
        print(figlet.renderText(str))


if __name__ == "__main__":
    main()