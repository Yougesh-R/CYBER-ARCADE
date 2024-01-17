import os
import random

def clear():
    os.system('cls')

def RPS():
    print('''
                                            ██████╗░░█████╗░░█████╗░██╗░░██╗  ██████╗░░█████╗░██████╗░███████╗██████╗░
                                            ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                                            ██████╔╝██║░░██║██║░░╚═╝█████═╝░  ██████╔╝███████║██████╔╝█████╗░░██████╔╝
                                            ██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
                                            ██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
                                            ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

                                                    ░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
                                                    ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
                                                    ╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
                                                    ░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
                                                    ██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
                                                    ╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░''')
    print('''
                                                --------------------------------------------------------------
                                                | RULES:                                                     |
                                                |     1. ROCK BEATS SCISSORS.                                | 
                                                |     2. SCISSORS BEAT PAPER.                                | 
                                                |     3. PAPER BEATS ROCK.                                   | 
                                                |     4. PICK '1' FOR ROCK, '2' FOR PAPER, '3' FOR SCISSORS. |
                                                |     5. THIS IS A BEST OF 7 GAME.                           | 
                                                |     6. YOU HAVE TO WIN 4 GAMES TO WIN THE SERIES.          | 
                                                |     7. DRAWS ARE NOT COUNTED.                              | 
                                                -------------------------------------------------------------- ''')
    print('''
        

            ''')
    j=input('                                                                     Press ENTER to continue...')
    clear()
    print('                                                                     ----------------------------')
    print('                                                                             GAME STARTS')
    print('                                                                     ----------------------------')
    c=0
    y=0
    i=0
    l=['rock','paper','scissors']
    while i==0:
        try:
            print('                                                                     [1=Rock, 2=Paper, 3=Scissors]')
            d=int(input('                                                                     Enter your choice: '))
            clear()
            print()
            if d>3 or d<1:
                print('                                                                     ----------------------------')
                print('                                                                     The entered number must be 1,2,3 enter again')
                print('                                                                     ----------------------------')
            else:
                z=random.randrange(1,4)
                if d==1 and z==1:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your choice: Rock')
                    print('                                                                     My choice: Rock')
                    print('                                                                     Draw')
                    print('                                                                     No.of games you won: ',y)
                    print('                                                                     No.of games I won: ',c)
                    print('                                                                     ----------------------------')
                elif d==1 and z==2:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your choice: Rock')
                    print('                                                                     My choice: Paper')
                    print('                                                                     Paper beats Rock I win')
                    c+=1
                    print('                                                                     No.of games you won: ',y)
                    print('                                                                     No.of games I won: ',c)
                    print('                                                                     ----------------------------')
                    if c==4:
                        print('                                                                     I won the game because I won 4 out of 7 games')
                        print('                                                                     ----------------------------')
                        print('                                                                              GAME OVER')
                        print('                                                                     ----------------------------')
                        i+=1
                elif d==1 and z==3:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your choice: Rock')
                    print('                                                                     My choice: Scissors')
                    print('                                                                     Rock beats Scissors You win')
                    y+=1
                    print('                                                                     No.of games you won: ',y)
                    print('                                                                     No.of games I won: ',c)
                    print('                                                                     ----------------------------')
                    if y==4:
                        print('                                                                     You won the game because you won 4 out of 7 games')
                        print('                                                                     ----------------------------')
                        print('                                                                              GAME OVER')
                        print('                                                                     ----------------------------')
                        i+=1
                elif d==2 and z==1:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your choice: Paper')
                    print('                                                                     My choice: Rock')
                    print('                                                                     Paper beats Rock You win')
                    y+=1
                    print('                                                                     No.of games you won: ',y)
                    print('                                                                     No.of games I won: ',c)
                    print('                                                                     ----------------------------')
                    if y==4:
                        print('                                                                     You won the game because you won 4 out of 7 games')
                        print('                                                                     ----------------------------')
                        print('                                                                              GAME OVER')
                        print('                                                                     ----------------------------')
                        i+=1
                elif d==2 and d==2:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your choice: Paper')
                    print('                                                                     My choice: Paper')
                    print('                                                                     Draw')
                    print('                                                                     No.of games you won: ',y)
                    print('                                                                     No.of games I won: ',c)
                    print('                                                                     ----------------------------')
                elif d==2 and z==3:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your choice: Paper')
                    print('                                                                     My choice: Scissors')
                    print('                                                                     Scissors beats paper I win')
                    c+=1
                    print('                                                                     No.of games you won: ',y)
                    print('                                                                     No.of games I won: ',c)
                    print('                                                                     ----------------------------')
                    if c==4:
                        print('                                                                     I won the game because I won 4 out of 7 games')
                        print('                                                                     ----------------------------')
                        print('                                                                              GAME OVER')
                        print('                                                                     ----------------------------')
                        i+=1
                elif d==3 and z==1:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your choice: Scissors')
                    print('                                                                     My choice: Rock')
                    print('                                                                     Rock beats Scissors I win')
                    c+=1
                    print('                                                                     No.of games you won: ',y)
                    print('                                                                     No.of games I won: ',c)
                    print('                                                                     ----------------------------')
                    if c==4:
                        print('                                                                     I won the game because I won 4 out of 7 games')
                        print('                                                                     ----------------------------')
                        print('                                                                              GAME OVER')
                        print('                                                                     ----------------------------')
                        i+=1
                elif d==3 and z==2:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your choice: Scissors')
                    print('                                                                     My choice: Paper')
                    print('                                                                     Scissors beats Paper You win')
                    y+=1
                    print('                                                                     No.of games you won: ',y)
                    print('                                                                     No.of games I won: ',c)
                    print('                                                                     ----------------------------')
                    if y==4:
                        print('                                                                     You won the game because you won 4 out of 7 games')
                        print('                                                                     ----------------------------')
                        print('                                                                              GAME OVER')
                        print('                                                                     ----------------------------')
                        i+=1
                elif d==3 and z==3:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your choice: Scissors')
                    print('                                                                     My choice: Scissors')
                    print('                                                                     Draw')
                    print('                                                                     No.of games you won: ',y)
                    print('                                                                     No.of games I won: ',c)
                    print('                                                                     ----------------------------')
            
        except ValueError:
            print('                                                                     ----------------------------')
            print('                                                                     Enter only numerical values')
            print('                                                                     ----------------------------')
    j=input('                                                                     Press ENTER to continue...')
    clear()

