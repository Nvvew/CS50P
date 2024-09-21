def convert(str):
    str2 = str.replace(":)", chr(0x1F60A))
    str3 = str2.replace(":(", chr(0x1F602))
    return str3

def main():
    str = input("Input your string:\n")
    print(convert(str))

main()