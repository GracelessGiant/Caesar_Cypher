"""
Creator: GracelessGiant
Peep my twitter [@GracelessGiant]
Description: Caesar_Cypher offers two functions.
    1. Enter a word/phase and amount to create cyphered word/phase
    2. Enter a cyphered work/phase to get potential solutions
"""

import os

dictionary = set()
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


def create_set():
    with open("dictionary.csv") as file:
        for line in file:
            word = line.strip().split(",")[0]
            dictionary.add(word)


def create_cypher():
    pass


def decypher():
    pass


def main():
    create_set()
    function = int(input("Enter the associated number with the desired function:\n1. Apply desired Caesar cypher to "
                         "original word/phase\n2. Decpyher text to find original word/phase\nFunction: "))
    if function == 1:
        create_cypher()
    elif function == 2:
        decypher()
    else:
        print("That's not a correct input. Enter again.")
        os.system("clear")
        main()


if __name__ == '__main__':
    main()
