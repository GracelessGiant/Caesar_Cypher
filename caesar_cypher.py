"""
Creator: GracelessGiant
Peep my twitter [@GracelessGiant]
Description: Caesar_Cypher offers two functions.
    1. Enter a word/phase and amount to create cyphered word/phase
    2. Enter a cyphered work/phase to get potential solutions
"""
dictionary = set()


def create_set():
    with open("dictionary.csv") as file:
        for line in file:
            word = line.strip().split(",")[0]
            dictionary.add(word)


def main():
    create_set()


if __name__ == '__main__':
    main()
