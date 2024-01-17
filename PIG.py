import os
import random

def clear():
    os.system('cls')

def PIG():
    print('''         
                                                                    ██████╗░██╗░██████╗░
                                                                    ██╔══██╗██║██╔════╝░
                                                                    ██████╔╝██║██║░░██╗░
                                                                    ██╔═══╝░██║██║░░╚██╗
                                                                    ██║░░░░░██║╚██████╔╝
                                                                    ╚═╝░░░░░╚═╝░╚═════╝░''')
    print('''
                            --------------------------------------------------------------------------------------------------------------- 
                            | RULES:                                                                                                      |  
                            |     1. In this game, a user and a computer opponent roll a 6-sided die each round.                          |
                            |     2. If the value of the die is a 1, the player that rolled the 1 loses all of their points.              |
                            |     3. Otherwise, the player gets the value of the die added to their points.                               |   
                            |     4. The first player to reach 30 points wins!                                                            |       
                            ---------------------------------------------------------------------------------------------------------------''')
    print('''
        

            ''')
    h=input('                                                                     Press ENTER to continue...')
    clear()
    a=0
    while a==0:
        ys=0
        cs=0
        b=0
        e=0
        while b==0:
            print('                                                                     ----------------------------')
            h=input('                                                                     Press ENTER to roll the dice...')
            clear()
            while e==0:
                y=random.randint(1,6)
                if y==1:
                    print('                                                                     ----------------------------')
                    print('''                                                                     You rolled a 1
                                                                     Your score reset to 0''')
                    d=0
                    ys=0
                    e=1
                else:
                    ys+=y
                    print('                                                                     ----------------------------')
                    print(f'''                                                                     You rolled a {y} 
                                                                     Your Score: {ys}''')
                    if ys>=30:
                        print('                                                                     ----------------------------')
                        print('                                                                                You win')
                        print('                                                                     ----------------------------')
                        print()
                        d=1
                        e=1
                        b=1
                        a=1
                    else:
                        d=0
                        e=1
                        
                        
            
            while d==0:         
                c=random.randint(1,6)
                if c==1:
                    print('''
                        ''')
                    print('''                                                                     I rolled a 1
                                                                     My score reset to 0
    ''')
                    e=0
                    cs=0
                    d=1
                else:
                    print('''
                        ''')
                    cs+=c
                    print(f'''                                                                     I rolled a {c}
                                                                     My score: {cs}
    ''')
                    if cs>=30:
                        print('                                                                     ----------------------------')
                        print('                                                                                I win')
                        print('                                                                     ----------------------------')
                        print()
                        d=1
                        e=1
                        b=1
                        a=1
                    else:
                        e=0
                        d=1
    h=input('                                                                     Press ENTER to continue...')
    clear()

