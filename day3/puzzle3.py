import re


def summarize_string(instruction_string: str) -> int:
    matches = re.findall(r"mul\(([0-9]+),([0-9]+)\)", instruction_string)
    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])

    return total

def get_next_instruction_snippet(instruction_string: str, start_pos: int) -> (str, int):
    disabled_at = [match.end() for match in re.finditer(r"don't\(\)", instruction_string) if match.end() > start_pos]
    enabled_at = [match.end() for match in re.finditer(r"do\(\)", instruction_string)  if match.end() > start_pos]

    disable_at = disabled_at[0] if len(disabled_at) > 0 else len(instruction_string)

    relevant_start_positions = [pos for pos in enabled_at if pos > disable_at]
    if len(relevant_start_positions) > 0:
        next_pos = relevant_start_positions[0]
    else:
        next_pos = -1

    return instruction_string[start_pos:disable_at], next_pos

def main():
    instruction_string = ""
    with open("puzzle_input.txt") as data_file:
        instruction_string = data_file.read()

    start_pos = 0
    total = 0
    while start_pos >= 0:
        instruction_snippet, start_pos = get_next_instruction_snippet(instruction_string, start_pos)
        total += summarize_string(instruction_snippet)

    print(f"Total: {summarize_string(instruction_string)}")
    print(f"Total with enabled instructions: {total}")


if __name__ == '__main__':
    main()
