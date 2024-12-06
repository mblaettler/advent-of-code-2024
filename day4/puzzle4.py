def search_diagonals(letter_grid: [[str]], r_idx: int, c_idx: int) -> int:
    found = 0
    if r_idx + 3 < len(letter_grid) and c_idx + 3 < len(letter_grid[r_idx]):
        if letter_grid[r_idx + 1][c_idx + 1] == "M" and \
           letter_grid[r_idx + 2][c_idx + 2] == "A" and \
           letter_grid[r_idx + 3][c_idx + 3] == "S":
            print(f"Found diagonal at {r_idx}, {c_idx}")
            found += 1
    if r_idx - 3 >= 0 and c_idx -3 >= 0:
        if letter_grid[r_idx - 1][c_idx - 1] == "M" and \
           letter_grid[r_idx - 2][c_idx - 2] == "A" and \
           letter_grid[r_idx - 3][c_idx - 3] == "S":
            print(f"Found diagonal at {r_idx}, {c_idx}")
            found += 1
    if r_idx + 3 < len(letter_grid) and c_idx - 3 >= 0:
        if letter_grid[r_idx + 1][c_idx - 1] == "M" and \
           letter_grid[r_idx + 2][c_idx - 2] == "A" and \
           letter_grid[r_idx + 3][c_idx - 3] == "S":
            print(f"Found diagonal at {r_idx}, {c_idx}")
            found += 1
    if r_idx - 3 >= 0 and c_idx + 3 < len(letter_grid[r_idx]):
        if letter_grid[r_idx - 1][c_idx + 1] == "M" and \
           letter_grid[r_idx - 2][c_idx + 2] == "A" and \
           letter_grid[r_idx - 3][c_idx + 3] == "S":
            print(f"Found diagonal at {r_idx}, {c_idx}")
            found += 1
    return found


def search_horizontal(letter_grid: [[str]], r_idx: int, c_idx: int) -> int:
    found = 0
    if c_idx + 3 < len(letter_grid[r_idx]):
        if letter_grid[r_idx][c_idx + 1] == "M" and \
           letter_grid[r_idx][c_idx + 2] == "A" and \
           letter_grid[r_idx][c_idx + 3] == "S":
            print(f"Found horizontal at {r_idx}, {c_idx}")
            found += 1
    if c_idx - 3 >= 0:
        if letter_grid[r_idx][c_idx - 1] == "M" and \
           letter_grid[r_idx][c_idx - 2] == "A" and \
           letter_grid[r_idx][c_idx - 3] == "S":
            print(f"Found horizontal at {r_idx}, {c_idx}")
            found += 1
    return found

def search_vertical(letter_grid: [[str]], r_idx: int, c_idx: int) -> int:
    found = 0
    if r_idx + 3 < len(letter_grid):
        if letter_grid[r_idx + 1][c_idx] == "M" and \
           letter_grid[r_idx + 2][c_idx] == "A" and \
           letter_grid[r_idx + 3][c_idx] == "S":
            print(f"Found vertical at {r_idx}, {c_idx}")
            found += 1
    if r_idx - 3 >= 0:
        if letter_grid[r_idx - 1][c_idx] == "M" and \
           letter_grid[r_idx - 2][c_idx] == "A" and \
           letter_grid[r_idx - 3][c_idx] == "S":
            print(f"Found vertical at {r_idx}, {c_idx}")
            found += 1
    return found


def search_x_mas(letter_grid: [[str]], r_idx: int, c_idx: int) -> int:
    if r_idx + 1 < len(letter_grid) and r_idx - 1 >= 0 and \
        c_idx + 1 < len(letter_grid[r_idx]) and c_idx - 1 >= 0:
        up_down_str = [letter_grid[r_idx - 1][c_idx - 1], letter_grid[r_idx + 1][c_idx + 1]]
        down_up_str = [letter_grid[r_idx + 1][c_idx - 1], letter_grid[r_idx - 1][c_idx + 1]]
        up_down_str.sort()
        down_up_str.sort()
        if up_down_str == ["M", "S"] and down_up_str == ["M", "S"]:
            print(f"Found X-MAS at {r_idx}, {c_idx}")
            return 1
    return 0


def main():
    with open("puzzle_input.txt") as f:
        letter_grid = []

        for line in f:
            letter_grid.append(list(line.strip()))

    found_xmas = 0
    found_x_mas = 0
    for r_idx in range(len(letter_grid)):
        for c_idx in range(len(letter_grid[r_idx])):
            if letter_grid[r_idx][c_idx] == "X":
                found_xmas += search_diagonals(letter_grid, r_idx, c_idx)
                found_xmas += search_horizontal(letter_grid, r_idx, c_idx)
                found_xmas += search_vertical(letter_grid, r_idx, c_idx)
            elif letter_grid[r_idx][c_idx] == "A":
                found_x_mas += search_x_mas(letter_grid, r_idx, c_idx)

    print(f"Found {found_xmas} XMAS")
    print(f"Found {found_x_mas} X-MAS")


if __name__ == "__main__":
    main()
