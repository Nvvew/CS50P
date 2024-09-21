import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(p):
    pattern = r'^((0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'
    return bool(re.match(pattern, p))

if __name__ == "__main__":
    main()