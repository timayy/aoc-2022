

from typing import Tuple


def read_input(file_name: str) -> str:
    with open(file_name, "r") as input:
        content = input.read()
    
    return content


# Not handling the iterator index explicitly.
def part_one(content: str) -> int:

    elves_calories = [0]
    current_elf_calories = 0

    for line in content.splitlines():
        if line == "":
            elves_calories.append(current_elf_calories)
            current_elf_calories = 0
            continue

        current_elf_calories += int(line)

    elves_calories.sort(reverse=True)

    return elves_calories[0]


# Handling the iterator index explicitly.
def part_two(content: str) -> Tuple[int, int, int]:

    current_elf = 0
    elves_calories = [0]

    for line in content.splitlines():
        if line == "":
            elves_calories.append(0)
            current_elf += 1
            continue

        elves_calories[current_elf] += int(line)

    elves_calories.sort(reverse=True)

    return elves_calories[0], elves_calories[1], elves_calories[2]


def part_one_cg(content: str) -> int:
    return max(
        [sum(int(line) for line in part.splitlines()) for part in content.split('\n\n')]
    )



def main():
    content = read_input("./day-1/input.txt")

    print(part_one_cg(content))

    print(part_one(content))

    print(sum(part_two(content)))

if __name__ == "__main__":
    main()