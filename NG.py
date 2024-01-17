import os
import random

def clear():
    os.system('cls')

def NG():
    print('''
                    ███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░  ░██████╗░██╗░░░██╗███████╗░██████╗░██████╗██╗███╗░░██╗░██████╗░
                    ████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗  ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██║████╗░██║██╔════╝░
                    ██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝  ██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░██║██╔██╗██║██║░░██╗░
                    ██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗  ██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██║██║╚████║██║░░╚██╗
                    ██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║  ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝██║██║░╚███║╚██████╔╝
                    ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝  ░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░''')
    print('''
                                        ------------------------------------------------------------------------------
                                        |RULES:                                                                      |
                                        |    1. The computer chooses a number in the range of 1-50.                  |
                                        |    2. You have to guess the number.                                        |
                                        |    3. You will have a total of 7 attempts.                                 |
                                        |    4. If u use up all the attempts, then u lose and the number is revealed.|
                                        ------------------------------------------------------------------------------''')
    print('''
        

            ''')
    h=input('                                                                     Press ENTER to continue...')
    clear()
    n=random.randint(1,50)
    a=7
    i=0
    while i==0:
        if a==0:
            i=1
            clear()
            print('                                                                     ----------------------------')
            print('                                                                     Maximum',a,'attempts are over')
            print('                                                                     The number was ',n)
            print('                                                                     ----------------------------')
        else:
            try:
                print('                                                                     You have',a,'attempts left')
                print('                                                                     ----------------------------')
                j=0
                while j==0:
                    g=int(input('                                                                     Enter your guess: '))
                    if g<0 or g>50:
                        print('                                                                     ----------------------------')
                        print('                                                                     Enter the value in the range 1-50 only')
                        print('                                                                     ----------------------------')
                    else:
                        j=1
                        clear()
                        if g==n:
                            print('                                                                     ----------------------------')
                            print('                                                                     You guessed it right')
                            print('                                                                     The number is',n)
                            print('                                                                     ----------------------------')
                            print()
                            i=1
                        elif g<n:
                            print('                                                                     ----------------------------')
                            print('                                                                     Guess a highter number')
                            a-=1
                        elif g>n:
                            print('                                                                     ----------------------------')
                            print('                                                                     Guess a lower number')
                            a-=1
            except ValueError:
                print('                                                                     ----------------------------')
                print('                                                                     Enter only numerical values')
                print('                                                                     ----------------------------')
    h=input('                                                                     Press ENTER to continue...')
    clear()

