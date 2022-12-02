
from enum import Enum
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


shape_lookup = {
    "A": Shape.ROCK, 
    "X": Shape.ROCK, 
    "B": Shape.PAPER, 
    "Y": Shape.PAPER, 
    "C": Shape.SCISSORS, 
    "Z": Shape.SCISSORS, 
    }


def part_one(content: str) -> int:
    score = 0

    for line in content.splitlines():
        opponent = shape_lookup.get(line[0])
        you = shape_lookup.get(line[2])

        outcome = round_outcome(opponent, you)
        score += outcome + you.value

    return score
    

def round_outcome(opponent: Shape, you: Shape) -> int:
    # Draw
    if opponent == you:
        return 3

    if opponent is Shape.ROCK and you is Shape.SCISSORS:
        return 0

    if opponent is Shape.PAPER and you is Shape.ROCK:
        return 0

    if opponent is Shape.SCISSORS and you is Shape.PAPER:
        return 0

    return 6

def read_input(path: str) -> str:
    with open(path, "r") as input_file:
        content = input_file.read()

    return content


def main():
    content = read_input(INPUT_FILE)

    print(part_one(content))

if __name__ == "__main__":
    main()
