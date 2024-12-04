import re


def main():
    with open("puzzle_input.txt") as data_file:
        input = data_file.read()
        matches = re.findall(r"mul\(([0-9]+),([0-9]+)\)", input)
        total = 0
        for match in matches:
            total += int(match[0]) * int(match[1])

        print(f"Total: {total}")


if __name__ == '__main__':
    main()
