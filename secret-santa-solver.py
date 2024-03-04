import argparse
import random


PEOPLE = ["Alice", "Bob", "Charlie", "Dana", "Eve", "Frank", "George", "Hannah"]
COUPLES = [("Alice", "Bob"), ("Charlie", "Dana"), ("Eve", "Frank"), ("George", "Hannah")]


def is_couple(person1: str, person2: str, couples: list[tuple[str, str]]) -> bool:
    return (person1, person2) in couples or (person2, person1) in couples


def main(people: list[str], couples: list[tuple[str, str]]):
    if len(people) == 0 or len(people) == 1:
        raise Exception("The list of people must have at least two people")
    elif (len(people) == 2 or len(people) == 3) and len(couples) == 1:
        raise Exception("The list doesn't contain enough people to create the secret santa list")

    random.shuffle(people)

    has_gift = []
    secret_santa = []

    # ensure last people can give to first
    if is_couple(people[0], people[-1], couples):
        people[0], people[1] = people[1], people[0]

    for index, person in enumerate(people):
        # using index of names allows us to handle list with the same name in it
        next_index = (index + 1) % len(people)
        receiver = None

        while not receiver:
            if next_index == index:
                raise Exception("An error occured while building your secret santa list")
            elif is_couple(person, people[next_index], couples) or next_index in has_gift:
                next_index = (next_index + 1) % len(people)
            else:
                receiver = people[next_index]

        has_gift.append(next_index)
        secret_santa.append((person, receiver))

    return secret_santa


if __name__ == "__main__":
    people = PEOPLE
    couples = COUPLES

    parser = argparse.ArgumentParser(description="Generate a Secret Santa list.")
    parser.add_argument('--people', type=str, help='A comma-separated list of people.')
    parser.add_argument('--couples', type=str, help='A semicolon-separated list of couples, each defined by two names separated by a comma.')

    args = parser.parse_args()

    # NOTE: you can mix custom with default args. In our case we will accept it.
    if args.people:
        people = args.people.split(',')

    if args.couples:
        couples_input = args.couples.split(';')
        couples = [tuple(couple.split(',')) for couple in couples_input]
    else:
        couples = []

    assignments = main(people, couples)

    for giver, receiver in assignments:
        print(f"{giver} gives to {receiver}")
