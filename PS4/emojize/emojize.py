def main():
    str = input("Input: ")
    print(emo(str))

emoji_dict = {
    ":thumbs_up:": "👍",
    ":thumbsup:": "👍",
    ":smile:": "😄",
    ":grinning:": "😀",
    ":heart:": "❤️",
    ":laughing:": "😆",
    ":cry:": "😢",
    ":clap:": "👏",
    ":sunglasses:": "😎",
    ":1st_place_medal:": "🥇"
}

def emo(str):
    for code in emoji_dict.keys():
        str = str.replace(code, emoji_dict[code])
    return str

if __name__ == "__main__":
    main()