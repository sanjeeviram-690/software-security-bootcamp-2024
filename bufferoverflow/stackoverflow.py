import sys

def valid_serial(psz):
    length = len(psz)
    total = 0

    if length < 10:
        return 0

    for char in psz:
        if char < '0' or char > 'z':
            return 0
        total += ord(char)

    if total % 853 == 83:
        return 1

    return 0

def validate_serial():
    serial = input()

    if valid_serial(serial):
        return 1
    else:
        return 0

def do_valid_stuff():
    print("The serial number is valid!")
    sys.exit(0)

def do_invalid_stuff():
    print("Invalid serial number!\nExiting")
    sys.exit(1)

def main():
    if validate_serial():
        do_valid_stuff()
    else:
        do_invalid_stuff()

if __name__ == "__main__":
    main()

