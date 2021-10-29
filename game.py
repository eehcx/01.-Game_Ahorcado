import random
import os


def run():

    IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    DB = [
        "C",
        "Python",
        "Javascript",
        "Java",
        "PHP"
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6

    while True:
        os.system("clear")
        for character in spaces:
            print(character, end="")
        print(IMAGES[attemps])
        elected = input("Escribe la letra que creas correcta: ".upper())

        found = False
        for idx, character in enumerate(word):
            if character == elected:
                spaces[idx] = elected
                found = True
        if not found:
            attemps -= 1

        # GANASTE
        if "_" not in spaces:
            os.system("clear")
            print("You are winner")
            break
            input()
        # PERDISTE
        if attemps == 0:
            os.system("clear")
            print("You lost")
            break
            input()


if __name__ == '__main__':
    run()
