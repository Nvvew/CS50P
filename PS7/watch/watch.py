import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'<iframe[^>]+src="https?://(?:www\.)?(?:youtube(?:-nocookie)?\.com/embed/|youtube\.com/watch\?v=)([a-zA-Z0-9_-]+)"'
    match = re.search(pattern, s)

    if match:
        video_id = match.group(1)
        return f'http://youtu.be/{video_id}'
    else:
        return None

if __name__ == "__main__":
    main()