import pandas as pd


def calculate_distance(data: pd.DataFrame) -> None:
    for col in data:
        data[col] = data[col].sort_values(ignore_index=True)

    difference = abs(data[0] - data[1])
    print(f"Difference score: {difference.sum()}")


def calculate_similarity(data: pd.DataFrame) -> None:
    similarity = 0

    for value in data[0]:
        num_of_entities = data[1] == value
        similarity += num_of_entities.sum() * value

    print(f"Similarity score: {similarity}")


def main():
    data = pd.read_table("input_puzzle1.txt", sep="\s+", header=None)

    calculate_distance(data.copy(deep=True))
    calculate_similarity(data.copy(deep=True))



if __name__ == '__main__':
    main()
