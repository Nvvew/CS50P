media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
def main():
    f = input("File name: ").lower()
    for e, type in media_types.items():
        if f.endswith(e):
            print(type)
            return
    
    print("application/octet-stream")

if __name__ == "__main__":
    main()