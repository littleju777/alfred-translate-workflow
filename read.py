import sys
import subprocess
import re

def is_english(string):
    # Check if the string contains only English characters
    if re.match("^[A-Za-z0-9\s\.\,\!\?\;\'\"]+$", string):
        return True
    return False

def download_pronunciation(text):
    url = f"http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={text}&tl=en"
    filename = "pronunciation.mp3"
    try:
        subprocess.run(['curl', '-o', filename, url], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error downloading pronunciation: {e}")
        sys.exit(1)

def play_audio(file_path):
    try:
        subprocess.run(['afplay', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error playing audio: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python pronounce.py 'your string here'")
        return

    text = sys.argv[1]
    if is_english(text):
        download_pronunciation(text)
        play_audio('pronunciation.mp3')
        os.remove(filename)
    else:
        print("The string is not in English.")

if __name__ == "__main__":
    main()