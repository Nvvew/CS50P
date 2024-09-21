import re
import sys

def main():
    print(count(input("Text: ")))

def count(text: str) -> int:
    # Use regular expression to match "um" as a whole word, case-insensitively
    return len(re.findall(r'\bum\b', text, re.IGNORECASE))

if __name__ == "__main__":
    main()