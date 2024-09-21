import sys
from PIL import Image
from PIL import ImageOps

def main():
    if not len(sys.argv) == 3:
        sys.exit("No")

    input = sys.argv[1]
    output = sys.argv[2]
    fmt = ('.jpg', '.jpeg', '.png')

    if not (input.endswith(fmt) and output.endswith(fmt)):
        sys.exit("No")
    
    try:
        with Image.open(input) as img, Image.open('shirt.png') as shirt:
            img2 = ImageOps.fit(img, (600,600))
            img2.paste(shirt, (0, 0), shirt)
            img2.save(output)
            
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

if __name__ == "__main__":
    main()