from pathlib import Path

def parse_line(line):
    if "^" in line:
        split = line.split("^")
        return int(split[0]) ** int(split[1])

    return int(line)


def next_magic_number(number):
    str_number = str(number)
    length = len(str_number)

    if str_number == "9" * length:
        return int("1" + "0" * (length - 1) + "1")

    half = (length + 1) // 2
    left = str_number[:half]

    magic_number = create_palindrome(left, length)

    if magic_number <= number:
        new_left = int(left) + 1
        return create_palindrome(new_left, length)

    return magic_number


def create_palindrome(left, length):
    str_left = str(left)

    if length % 2 == 0:
        result = str_left + str_left[::-1]
    else:
        result = str_left + str_left[:-1][::-1]

    return int(result)


def main():
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()

    for line in data:
        print(next_magic_number(parse_line(line)))


if __name__ == "__main__":
    main()
