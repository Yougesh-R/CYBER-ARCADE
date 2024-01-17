import os
import random

def clear():
    os.system('cls')

def HANGMAN():
    def choose_word():
        words=['CAT', 'DOG', 'FISH', 'BIRD', 'TREE', 'HOUSE', 'MOON', 'SUN', 'RAIN', 'STAR', 'BOOK', 'PEN', 'RED', 'BLUE', 'GREEN', 'FOOD', 'BALL', 'GAME', 'JUMP', 'RUN', 'BABY', 'BIRD', 'SING', 'CAKE', 'DOOR', 'LAMP', 'HAT', 'CAR', 'BED', 'HILL', 'FARM', 'KEY', 'LOCK', 'TIME', 'SAND', 'CLOUD', 'SHOE', 'SHIP', 'HILL', 'FLAG', 'LEAF', 'LAKE', 'HILL', 'ROAD', 'BELL', 'SONG', 'BABY', 'DOLL', 'TOY', 'APPLE', 'ORANGE', 'BANANA', 'MOUSE', 'HAPPY', 'SAD', 'SMILE', 'LAUGH', 'CRY', 'FRIEND', 'PLAY', 'FLOWER', 'SLEEP', 'WAKE', 'HUG', 'KITE', 'OCEAN', 'RIVER', 'BRIDGE', 'SLIDE', 'SWING', 'COLOR', 'PAINT', 'DRAW', 'CHAIR', 'TABLE', 'BEDROOM', 'KITCHEN', 'WINDOW', 'MIRROR', 'MIRROR', 'WATCH', 'TIME', 'CLOCK', 'LETTER', 'MAIL', 'SEND', 'RECEIVE']

        return random.choice(words)

    def display_word(secret_word, guessed_letters):
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def hangman():
        print('''
                                                    ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
                                                    ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
                                                    ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
                                                    ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
                                                    ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
                                                    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
                
                            -----------------------------------------------------------------------------------------------------------                                     
                            | RULES:                                                                                                  |   
                            |     1. A random word will be selected by the computer for you to guess it.                              |   
                            |     2. You can guess a single letter every time.                                                        |
                            |     3. If the guessed letter is not in the word your attempts gets reduced.                             |
                            |     4. If your guess is right it is added to the word and you will have no deduction from the attempts. |
                            |     5. If the number of attempts is over and you did not guess the word then you lose the game.         |   
                            |     6. If you guess the entire word in the number of attempts then you win the game.                    |   
                            |     7. Improper inputs are not counted as a wrong guess.                                                |   
                            -----------------------------------------------------------------------------------------------------------''')
        print('''
        

            ''')
        h=input('                                                                     Press ENTER to continue...')
        clear()
        secret_word = choose_word()
        guessed_letters = []
        attempts = 11

        while attempts > 0:
            print('                                                                     ----------------------------')
            current_display = display_word(secret_word, guessed_letters)
            print(f"                                                                     Current Word: {current_display}")
            print(f"                                                                     Attempts left: {attempts}")
            print(f'                                                                     Letters guessed: {guessed_letters}')
            
            print('                                                                     ----------------------------')
            guess = input("                                                                     Guess a letter: ").upper()
            if len(guess) != 1 or not guess.isalpha():
                clear()
                print('                                                                     ----------------------------')
                print("                                                                     Invalid input. Please enter a single letter.")
                continue

            if guess in guessed_letters:
                clear()
                print('                                                                     ----------------------------')
                print("                                                                     You already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            if guess not in secret_word:
                attempts -= 1
                clear()
                print('                                                                     ----------------------------')
                print("                                                                     Incorrect guess!")
                print('                                                                     ----------------------------')
            else:
                clear()
                print('                                                                     ----------------------------')
                print("                                                                     Correct guess!")
                print('                                                                     ----------------------------')
                

            if all(letter in guessed_letters for letter in secret_word):
                print(f"                                                                     Congratulations! You guessed the word: {secret_word}")
                print('                                                                     ----------------------------')
                break

        if attempts == 0:
            print(f"                                                                     Sorry, you ran out of attempts. The word was: {secret_word}")
            print('                                                                     ----------------------------')
        h=input('                                                                     Press ENTER to continue...')
        clear()


    hangman()

