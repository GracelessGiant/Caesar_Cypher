"""
Creator: GracelessGiant
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
    :param letter:
    :return: the position of the desired letter or 100 if it is a space or special character
    """
    counter = 0
    capital = False

    if letter.isupper():        # checks to see if the letter is a capital
        capital = True
        letter = letter.lower()

    for char in alphabet:
        if char == letter:
            if capital:         # checks to see if the letter needs to be reverted to lowercase
                return counter+50
            return counter
        counter += 1

    return 100


def word_or_phrase(answer):
    """
    Takes the possible answer and determines if it is a word or phrase
    :param answer: possible answer
    :return: 0 if it a word or 1 if it is a phrase
    """
    if len(answer.split(" ")) == 1:
        return 0
    else:
        return 1


def parse_phrase(phrase):
    """
    Parses the phrase to determine how many words are in the dictionary from the phrase
    :param phrase: possible phrase
    :return: the likely phrase
    """
    pass


def ai(answers):
    """
    Takes the potential answers and attempts to determine which answer is the most likely
    :param answers: list of possible answers
    :return: most likely answer
    """
    likely_answers = []

    for ans in answers:
        sol = word_or_phrase(ans)
        if sol == 0:
            if ans in dictionary:
                likely_answers.append(ans)
        else:
            parse_phrase(ans)


def pretty_print(text, function):
    """
    Nicely prints out the potential answers
    :param text: the word or phrase that was encrypted or decrypted
    :param function: id for which function was used
    """
    counter = 0

    if function == 1:
        print("\nEncrypted Text: "+text)
    else:
        print("Potential Original Words: ")
        for word in text:
            if counter == 5:
                print("\n")
                counter = 0
            else:
                print(word+"  ", end="")
                counter += 1


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
            if position > 50:
                swing = ((position-50) + shift) % 26
                encrypted_text = encrypted_text+(alphabet[swing].upper())
            else:
                swing = (position + shift) % 26
                encrypted_text = encrypted_text+alphabet[swing]
    return encrypted_text


def decypher():
    """
    Takes encrypted text and finds all possible answers
    :return: list of all possible answers
    """
    original_text = ""
    answers = []

    encrypted_text = input("Enter the encrypted text: ")

    for shift in range(26):
        for letter in encrypted_text:
            position = find_letter(letter)
            if position == 100:
                original_text = original_text+letter
            else:
                if position > 50:
                    swing = ((position - 50) + shift) % 26
                    original_text = original_text + (alphabet[swing].upper())
                else:
                    swing = (position + shift) % 26
                    original_text = original_text + alphabet[swing]
        answers.append(original_text)
        original_text = ""
    return answers


def main():
    create_set()
    function = int(input("Enter the associated number with the desired function:\n1. Apply desired Caesar cypher to "
                         "original word/phrase\n2. Decypher text to find original word/phase\nFunction: "))
    if function == 1:
        encryption = create_cypher()
        pretty_print(encryption, 1)
    elif function == 2:
        decryption = decypher()
        pretty_print(decryption, 2)
    else:
        print("That's not a correct input. Enter again.")
        os.system("clear")
        main()


if __name__ == '__main__':
    main()
