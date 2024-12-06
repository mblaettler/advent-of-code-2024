from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col


class Guard:
    def __init__(self, position: Position, direction: Direction):
        self.position = position
        self.direction = direction

    def move(self, lab_map: [[str]]):
        if self.direction == Direction.UP:
            if self.position.row - 1 >= 0:
                if lab_map[self.position.row - 1][self.position.col] != "#":
                    self.position.row -= 1
                else:
                    self.direction = Direction.RIGHT
                return True
            else:
                return False
        elif self.direction == Direction.RIGHT:
            if self.position.col + 1 < len(lab_map[self.position.row]):
                if lab_map[self.position.row][self.position.col + 1] != "#":
                    self.position.col += 1
                else:
                    self.direction = Direction.DOWN
                return True
            else:
                return False
        elif self.direction == Direction.DOWN:
            if self.position.row + 1 < len(lab_map):
                if lab_map[self.position.row + 1][self.position.col] != "#":
                    self.position.row += 1
                else:
                    self.direction = Direction.LEFT
                return True
            else:
                return False
        elif self.direction == Direction.LEFT:
            if self.position.col - 1 >= 0:
                if lab_map[self.position.row][self.position.col - 1] != "#":
                    self.position.col -= 1
                else:
                    self.direction = Direction.UP
                return True
            else:
                return False

def main():
    with open("puzzle_input.txt") as f:
        lab_map = []

        for line in f:
            lab_map.append(list(line.strip()))

    guard = None
    for row_idx, row in enumerate(lab_map):
        for col_idx, cell in enumerate(row):
            if cell == "^":
                guard = Guard(Position(row_idx, col_idx), Direction.UP)

    lab_map[guard.position.row][guard.position.col] = "X"
    while guard.move(lab_map):
        lab_map[guard.position.row][guard.position.col] = "X"

    for row in lab_map:
        print("".join(row))

    count = 0
    for row in lab_map:
        for element in row:
            if element == 'X':
                count += 1

    print(f"Visited {count} cells")

if __name__ == "__main__":
    main()
