"""
Creator: GracelessGiant
Peep my twitter [@GracelessGiant]
Description: Caesar_Cypher offers two functions.
    1. Enter a word/phrase and amount to create cyphered word/phrase
    2. Enter a cyphered work/phase to get potential solutions
"""

import os

dictionary = set()
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


def create_set():
    """
    Creates the set of all the unique words found in the dictionary
    """
    with open("dictionary.csv") as file:
        for line in file:
            word = line.strip().split(",")[0]
            dictionary.add(word)


def find_letter(letter):
    """
    Finds the position of the current letter in the alphabetical list
    :return: the position of the desired letter or 100 if it is a space or special character
    """
    counter = 0
    for char in alphabet:
        if char == letter:
            return counter
        counter += 1

    return 100


def create_cypher():
    """
    Takes the original text and creates the encrypted text
    :return: the encrypted text
    """
    encrypted_text = ""
    original_text = input("Enter the original text: ")
    shift = int(input("Enter the shift: "))
    shift = shift % 26

    original_text = original_text.strip()

    for letter in original_text:
        position = find_letter(letter)
        if position == 100:
            encrypted_text = encrypted_text+letter
        else:
            encrypted_text = encrypted_text+alphabet[position+shift]
    return encrypted_text


def decypher():
    """

    :return:
    """
    pass


def main():
    create_set()
    function = int(input("Enter the associated number with the desired function:\n1. Apply desired Caesar cypher to "
                         "original word/phrase\n2. Decpyher text to find original word/phase\nFunction: "))
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
