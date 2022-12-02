
from dataclasses import dataclass
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')


@dataclass
class Shape:
    points: int
    wins_against: 'Shape'
    loses_against: 'Shape'

ROCK = Shape(1, None, None)
PAPER = Shape(2, ROCK, None)
SCISSORS = Shape(3, PAPER, ROCK)

ROCK.wins_against = SCISSORS
ROCK.loses_against = PAPER
PAPER.loses_against = SCISSORS


shape_lookup = {
    "A": ROCK, 
    "B": PAPER, 
    "C": SCISSORS, 
}


def part_two(content: str) -> int:
    score = 0

    for line in content.splitlines():
        opponent, you = line.split()
        opponent_shape = shape_lookup[opponent] 

        if you == "X":
            your_shape = opponent_shape.wins_against
        elif you == "Z":
            your_shape = opponent_shape.loses_against
        else:
            your_shape = opponent_shape

        outcome = round_outcome(opponent_shape, your_shape)
        score += outcome + your_shape.points

    return score
 

def round_outcome(opponent: Shape, you: Shape) -> int:
    if you == opponent.loses_against:
        return 6

    if you == opponent.wins_against:
        return 0

    # Draw.
    return 3

def read_input(path: str) -> str:
    with open(path, "r") as input_file:
        content = input_file.read()

    return content


def main():
    content = read_input(INPUT_FILE)

    print(part_two(content))

if __name__ == "__main__":
    main()
