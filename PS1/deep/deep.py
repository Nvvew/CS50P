def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    check(ans)


def check(a):
    aw = a.lower()
    if aw == "42" or aw == "forty-two" or aw == "forty two":
        print("Yes")
    else:
        print("No")


main()