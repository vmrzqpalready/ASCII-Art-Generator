import pyfiglet

def main():
    text = input("Enter a string to convert to ASCII art: ")
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

if __name__ == "__main__":
    main()
