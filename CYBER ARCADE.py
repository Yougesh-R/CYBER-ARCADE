import random
import os

def clear():
    os.system('cls')

def play_again_or_not():
    h=0
    while h==0:
        try:
            v=int(input('                                                                     Enter 0 to play again or 1 to end: '))
            clear()
            if v==0:
                h+=1
                v=0
            elif v==1:
                h+=1
                v=1
            else:
                print('                                                                     ----------------------------')
                print('                                                                     Entry invalid enter only 0 or 1')
                print('                                                                     ----------------------------')
        except ValueError:
            print('                                                                     ----------------------------')
            print('                                                                     Enter only numerical values')
            print('                                                                     ----------------------------')
    return v

def handcricket():
    
    def computer_second_batting():
        print('                                                                     ----------------------------')
        print('                                                                     You are batting now')
        print('                                                                     ----------------------------')
        j=input('                                                                     Press ENTER to continue...')
        clear()
        ys=0
        g=0
        while g==0:
            try:
                n1=int(input('                                                                     Enter your number in range of 0 to 10: '))
                clear()
                if n1<0 or n1>10:
                    print('                                                                     ----------------------------')
                    print('                                                                     The value is out of range enter again')
                    print('                                                                     ----------------------------')
                else:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your number: ',n1)
                    n2=random.randrange(11)
                    print('                                                                     My number: ',n2)
                    if n1==0 and n2==1:
                        print('                                                                     You are Out')
                        print('                                                                     Your final score: ',ys)
                        print('                                                                     ----------------------------')
                        g+=1
                    elif n1==0 and n2>1:
                        ys+=n2
                        print('                                                                     Your current score: ',ys)
                        print('                                                                     ----------------------------')
                    elif n2==0:
                        print('                                                                     Free Hit +10')
                        ys+=n1+10
                        print('                                                                     Your current score: ',ys)
                        print('                                                                     ----------------------------')
                    elif n1!=n2:
                        ys+=n1
                        print('                                                                     Your current score: ',ys)
                        print('                                                                     ----------------------------')
                    elif n1==n2:
                        print('                                                                     You are Out')
                        print('                                                                     Your final score: ',ys)
                        print('                                                                     ----------------------------')
                        g+=1
            except ValueError:
                print('                                                                     ----------------------------')
                print('                                                                     Enter only numerical value')
                print('                                                                     ----------------------------')
        print('                                                                     Target: ',ys+1)
        print('                                                                     ----------------------------')
        j=input('                                                                     Press ENTER to continue...')
        clear()
        print('                                                                     ----------------------------')
        print('                                                                     Now it\'s my turn for batting')
        print('                                                                     ----------------------------')
        j=input('                                                                     Press ENTER to continue...')
        clear()
        cs=0
        t=ys+1
        g=0
        while g==0:
            try:
                print('                                                                     ----------------------------')
                n1=int(input('                                                                     Enter your number in range of 0 to 10: '))
                clear()
                if n1<0 or n1>10:
                    print('                                                                     ----------------------------')
                    print('                                                                     The value is out of range enter again')
                    print('                                                                     ----------------------------')
                else:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your number: ',n1)
                    n2=random.randrange(11)
                    print('                                                                     My number: ',n2)
                    if n2==0 and n1==1:
                        print('                                                                     I am Out')
                        print('                                                                     My final score: ',cs)
                        print('                                                                     Target: ',t)
                        print('                                                                     ----------------------------')
                        print('                                                                           YOU WON THE GAME')
                        print('                                                                     ----------------------------')
                        g+=1
                    elif n2==0 and n1>1:
                        cs+=n1
                        print('                                                                     My current score: ',cs)
                        print('                                                                     Target: ',t)
                        print('                                                                     ----------------------------')
                        if cs>=t:
                            print('                                                                     ----------------------------')
                            print('                                                                            I WON THE GAME')
                            print('                                                                     ----------------------------')
                            g+=1
                    elif n1==0:
                        print('                                                                     Free Hit +10')
                        cs+=n2+10
                        print('                                                                     My current score: ',cs)
                        print('                                                                     Target: ',t)
                        print('                                                                     ----------------------------')
                        if cs>=t:
                            print('                                                                     ----------------------------')
                            print('                                                                            I WON THE GAME')
                            print('                                                                     ----------------------------')
                            g+=1
                    elif n2!=n1:
                        cs+=n2
                        print('                                                                     My current score: ',cs)
                        print('                                                                     Target: ',t)
                        print('                                                                     ----------------------------')
                        if cs>=t:
                            print('                                                                     ----------------------------')
                            print('                                                                            I WON THE GAME')
                            print('                                                                     ----------------------------')
                            g+=1
                    elif n2==n1:
                        print('                                                                     I am Out')
                        print('                                                                     My final score: ',cs)
                        print('                                                                     Target: ',t)
                        print('                                                                     ----------------------------')
                        print('                                                                           YOU WON THE GAME')
                        print('                                                                     ----------------------------')
                        g+=1
            except ValueError:
                print('                                                                     ----------------------------')
                print('                                                                     Enter only numerical value')
                print('                                                                     ----------------------------')
        j=input('                                                                     Press ENTER to continue...')
        clear()

    def computer_first_batting():
        print('                                                                     ----------------------------')
        print('                                                                     I am batting now')
        print('                                                                     ----------------------------')
        j=input('                                                                     Press ENTER to continue...')
        clear()
        cs=0
        g=0
        while g==0:
            try:
                n1=int(input('                                                                     Enter your number in range of 0 to 10: '))
                clear()
                if n1<0 or n1>10:
                    print('                                                                     ----------------------------')
                    print('                                                                     The value is out of range enter again')
                    print('                                                                     ----------------------------')
                else:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your number: ',n1)
                    n2=random.randrange(11)
                    print('                                                                     My number: ',n2)
                    if n2==0 and n1==1:
                        print('                                                                     I am Out')
                        print('                                                                     My final score: ',cs)
                        print('                                                                     ----------------------------')
                        g+=1
                    elif n2==0 and n1>1:
                        cs+=n1
                        print('                                                                     My current score: ',cs)
                        print('                                                                     ----------------------------')
                    elif n1==0:
                        print('                                                                     Free Hit +10')
                        cs+=n2+10
                        print('                                                                     My current score: ',cs)
                        print('                                                                     ----------------------------')
                    elif n2!=n1:
                        cs+=n2
                        print('                                                                     My current score: ',cs)
                        print('                                                                     ----------------------------')
                    elif n2==n1:
                        print('                                                                     I am Out')
                        print('                                                                     My final score: ',cs)
                        print('                                                                     ----------------------------')
                        g+=1
            except ValueError:
                print('                                                                     ----------------------------')
                print('                                                                     Enter only numerical values')
                print('                                                                     ----------------------------')
        print('                                                                     ----------------------------')
        print('                                                                     Target: ',cs+1)
        print('                                                                     ----------------------------')
        j=input('                                                                     Press ENTER to continue...')
        clear()
        print('                                                                     ----------------------------')
        print('                                                                     Now it\'s your turn for batting')
        print('                                                                     ----------------------------')
        j=input('                                                                     Press ENTER to continue...')
        clear()
        ys=0
        t=cs+1
        g=0
        while g==0:
            try:
                print('                                                                     ----------------------------')
                n1=int(input('                                                                     Enter your number in range of 0 to 10: '))
                clear()
                if n1<0 or n1>10:
                    print('                                                                     ----------------------------')
                    print('                                                                     The value is out of range enter again')
                    print('                                                                     ----------------------------')
                else:
                    print('                                                                     ----------------------------')
                    print('                                                                     Your number: ',n1)
                    n2=random.randrange(11)
                    print('                                                                     My number: ',n2)
                    if n1==0 and n2==1:
                        print('                                                                     You are Out')
                        print('                                                                     Your final score: ',ys)
                        print('                                                                     Target: ',t)
                        print('                                                                     ----------------------------')
                        print('                                                                            I WON THE GAME')
                        print('                                                                     ----------------------------')
                        g+=1
                    elif n1==0 and n2>1:
                        ys+=n2
                        print('                                                                     Your current score: ',ys)
                        print('                                                                     Target: ',t)
                        print('                                                                     ----------------------------')
                        if ys>=t:
                            print('                                                                     ----------------------------')
                            print('                                                                           YOU WON THE GAME')
                            print('                                                                     ----------------------------')
                            g+=1
                    elif n2==0:
                        print('                                                                     Free Hit +10')
                        ys+=n1+10
                        print('                                                                     Your current score: ',ys)
                        print('                                                                     Target: ',t)
                        print('                                                                     ----------------------------')
                        if ys>=t:
                            print('                                                                     ----------------------------')
                            print('                                                                           YOU WON THE GAME')
                            print('                                                                     ----------------------------')
                            g+=1
                    elif n1!=n2:
                        ys+=n1
                        print('                                                                     Your current score: ',ys)
                        print('                                                                     Target: ',t)
                        print('                                                                     ----------------------------')
                        if ys>=t:
                            print('                                                                     ----------------------------')
                            print('                                                                           YOU WON THE GAME')
                            print('                                                                     ----------------------------')
                            g+=1
                    elif n1==n2:
                        print('                                                                     You are Out')
                        print('                                                                     Your final score: ',ys)
                        print('                                                                     Target: ',t)
                        print('                                                                     ----------------------------')
                        print('                                                                            I WON THE GAME')
                        print('                                                                     ----------------------------')
                        g+=1
            except ValueError:
                print('                                                                     ----------------------------')
                print('                                                                     Enter only numerical values')
                print('                                                                     ----------------------------')
        j=input('                                                                     Press ENTER to continue...')
        clear()
    
    print('''
                                        ██╗░░██╗░█████╗░███╗░░██╗██████╗░  ░█████╗░██████╗░██╗░█████╗░██╗░░██╗███████╗████████╗
                                        ██║░░██║██╔══██╗████╗░██║██╔══██╗  ██╔══██╗██╔══██╗██║██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝
                                        ███████║███████║██╔██╗██║██║░░██║  ██║░░╚═╝██████╔╝██║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░
                                        ██╔══██║██╔══██║██║╚████║██║░░██║  ██║░░██╗██╔══██╗██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░
                                        ██║░░██║██║░░██║██║░╚███║██████╔╝  ╚█████╔╝██║░░██║██║╚█████╔╝██║░╚██╗███████╗░░░██║░░░
                                        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░''')
    print('''
            ----------------------------------------------------------------------------------------------------------------------------------------
            | RULES:                                                                                                                               |
            |                                                                                                                                      |
            |  1. IF YOU ARE BATTING AND YOU ENTER 0 AND THE COMPUTER CHOOSES 1 THEN YOU ARE OUT AND THE SAME APPLIES WHEN THE COMPUTER IS BATTING.|
            |                                                                                                                                      |
            |  2. IF YOU ARE BATTING AND YOU ENTER 0 AND THE COMPUTER CHOOSES ANY NUMBER GREATER THAN 1 THEN THE NUMBER CHOOSEN BY THE COMPUTER    |
            |     WILL BE ADDED TO YOUR SCORE AND THE SAME APPLIES WHEN THE COMPUTER IS BATTING.                                                   |
            |                                                                                                                                      |
            |  3. IF YOU ARE BATTING AND YOU ENTER ANY NUMBER AND THE COMPUTER CHOOSES 0 THEN ITS A FREE HIT AND 10 WILL BE ADDED TO YOUR SCORE    |
            |     AND THE SAME APPLIES WHEN THE COMPUTER IS BATTING.                                                                               |
            |                                                                                                                                      |
            |  4. IF YOU ARE BATTING AND YOU ENTER ANY NUMBER AND THE COMPUTER CHOOSES A NUMBER WHICH IS NOT EQUAL TO YOUR NUMBER THEN THE NUMBER  |
            |     YOU ENTERED WILL BE ADDED TO YOUR SCORE AND THE SAME APPLIES WHEN THE COMPUTER IS BATTING.                                       |
            |                                                                                                                                      |
            |  5. IF YOU ARE BATTING AND YOU ENTER ANY NUMBER AND THE COMPUTER CHOOSES A NUMBER WHICH IS EQUAL TO YOUR NUMBER THEN YOU WILL BE OUT |
            |     AND THE SAME APPLIES WHEN THE COMPUTER IS BATTING.                                                                               |
            ----------------------------------------------------------------------------------------------------------------------------------------''')
    print('''
        

            ''')
    j=input('                                                                     Press ENTER to continue...')
    clear()
    print('                                                                     ----------------------------')
    print('                                                                             GAME STARTS')
    print('                                                                     ----------------------------')
    d=0
    while d==0:
        p1=input('                                                                     Enter o for odd or e for even: ')
        clear()
        if p1!='o' and p1!='e':
            print('                                                                     ----------------------------')
            print('                                                                     Entered value must be only o or e')
            print('                                                                     ----------------------------')
        elif p1=='o':
            print('                                                                     ----------------------------')
            print('                                                                     You are odd so I am even')
            print('                                                                     ----------------------------')
            p2='e'
            d+=1
        elif p1=='e':
            print('                                                                     ----------------------------')
            print('                                                                     You are even so I am odd')
            print('                                                                     ----------------------------')
            p2='o'
            d+=1
    e=0
    while e==0:
        try:
            t1=int(input('                                                                     Enter a number form 0 to 10 for toss: '))
            clear()
            if t1<0 or t1>10:
                print('                                                                     ----------------------------')
                print('                                                                     The value must be only in range of 0 to 10')
                print('                                                                     ----------------------------')
            else:
                print('                                                                     ----------------------------')
                print('                                                                     Your number: ',t1)
                t2=random.randrange(11)
                print('                                                                     My number is: ',t2)
                print('                                                                     ----------------------------')
                e+=1
        except ValueError:
            print('                                                                     ----------------------------')
            print('                                                                     Enter only numerical values')
            print('                                                                     ----------------------------')
    ts=t1+t2
    print('                                                                     Toss score: ',ts)
    if ts%2==0:
        if p1=='e':
            print('                                                                     You won the toss')
            print('                                                                     ----------------------------')
            f=0
            while f==0:
                try:
                    c1=int(input('                                                                     Enter 1 for batting or 2 for bowling: '))
                    clear()
                    if c1<1 or c1>2:
                        print('                                                                     ----------------------------')
                        print('                                                                     The value must only be 1 or 2')
                        print('                                                                     ----------------------------')
                    elif c1==1:
                        f+=1
                        print('                                                                     ----------------------------')
                        print('                                                                     You chose batting so I am bowling')
                        print('                                                                     ----------------------------')
                        j=input('                                                                     Press ENTER to continue...')
                        clear()
                        computer_second_batting()
                    elif c1==2:
                        f+=1
                        print('                                                                     ----------------------------')
                        print('                                                                     You chose bowling so I am batting')
                        print('                                                                     ----------------------------')
                        j=input('                                                                     Press ENTER to continue...')
                        clear()
                        computer_first_batting()  
                except ValueError:
                    print('                                                                     ----------------------------')
                    print('                                                                     Enter only numerical values')
                    print('                                                                     ----------------------------')
        elif p2=='e':
            print('                                                                     I won the toss')
            print('                                                                     ----------------------------')
            c2=random.randrange(1,3)
            if c2==1:
                print('                                                                     I choose batting so you are bowling')
                print('                                                                     ----------------------------')
                j=input('                                                                     Press ENTER to continue...')
                clear()
                computer_first_batting()
            elif c2==2:
                print('                                                                     I choose bowling so you are batting')
                print('                                                                     ----------------------------')
                j=input('                                                                     Press ENTER to continue...')
                clear()
                computer_second_batting() 
    elif ts%2!=0:
        if p1=='o':
            print('                                                                     You won the toss')
            print('                                                                     ----------------------------')
            f=0
            while f==0:
                try:
                    c1=int(input('                                                                     Enter 1 for batting or 2 for bowling: '))
                    clear()
                    if c1<1 or c1>2:
                        print('                                                                     ----------------------------')
                        print('                                                                     The value must only be 1 or 2')
                        print('                                                                     ----------------------------')
                    elif c1==1:
                        f+=1
                        print('                                                                     ----------------------------')
                        print('                                                                     You chose batting so I am bowling')
                        print('                                                                     ----------------------------')
                        j=input('                                                                     Press ENTER to continue...')
                        clear()
                        computer_second_batting()
                    elif c1==2:
                        f+=1
                        print('                                                                     ----------------------------')
                        print('                                                                     You chose bowling so I am batting')
                        print('                                                                     ----------------------------')
                        j=input('                                                                     Press ENTER to continue...')
                        clear()
                        computer_first_batting()   
                except ValueError:
                    print('                                                                     ----------------------------')
                    print('                                                                     Enter only numerical values')
                    print('                                                                     ----------------------------')
        elif p2=='o':
            print('                                                                     I won the toss')
            c2=random.randrange(1,3)
            if c2==1:
                print('                                                                     I choose batting so you are bowling')
                print('                                                                     ----------------------------')
                j=input('                                                                     Press ENTER to continue...')
                clear()
                computer_first_batting()
            elif c2==2:
                print('                                                                     I choose bowling so you are batting')
                print('                                                                     ----------------------------')
                j=input('                                                                     Press ENTER to continue...')
                clear()
                computer_second_batting()

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

def WORDLE():
    print('''
                                                        ░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░██╗░░░░░███████╗
                                                        ░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔════╝
                                                        ░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║██║░░░░░█████╗░░
                                                        ░░████╔═████║░██║░░██║██╔══██╗██║░░██║██║░░░░░██╔══╝░░
                                                        ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝███████╗███████╗
                                                        ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝
          ''')
    print('''
                        ---------------------------------------------------------------------------------------------------------------
                        | RULES:                                                                                                      | 
                        |   1. You can choose how many letter word you want to play.                                                  | 
                        |   2. After you choose, the computer chooses a word.                                                         | 
                        |   3. You will be asked to guess the word.                                                                   | 
                        |   4. The correctly placed letters, misplaced letters and letters not present will be showen from your guess.|
                        |   5. You win if you guess the word within 7 attempts else you loose.                                        |
                        ---------------------------------------------------------------------------------------------------------------''')
    print('''
        

            ''')
    h=input('                                                                     Press ENTER to continue...')
    clear()
    words3=['THE', 'AND', 'FOR', 'YOU', 'CAN', 'GET', 'HAS', 'ITS', 'LET', 'NOT', 'ONE', 'PUT', 'SAY', 'SEE', 'THE', 'ALL', 'ANY', 'ARE', 'BUT', 'CAN', 'DID', 'GET', 'HAS', 'HER', 'HIM', 'HIS', 'HOW', 'MAN', 'MAY', 'NEW', 'NOW', 'OLD', 'OUR', 'OUT', 'OWN', 'SAY', 'SEE', 'SHE', 'THE', 'TWO', 'USE', 'WHO', 'WHY', 'YES', 'YOU', 'BIG', 'CAT', 'DOG']
    words4=['BLUE', 'CHAT', 'DEAR', 'EASY', 'FISH', 'GOLD', 'HALO', 'JUMP', 'KIND', 'LOVE', 'MAKE', 'NOTE', 'OPEN', 'PART', 'QUAD', 'RACE', 'SOFT', 'TRUE', 'UNIT', 'VAST', 'WISH', 'XRAY', 'YARD', 'ZOOM', 'ATOM', 'BOLD', 'CLUB', 'DEEP', 'ECHO', 'FOUR', 'GLOW', 'HERO', 'ICON', 'JOLT', 'KISS', 'LIME', 'MIST', 'NOON', 'PINK', 'QUIT', 'ROSE', 'SNOW', 'TIDE', 'UPON', 'VIEW', 'WOLF', 'YOGA', 'ZEAL']
    words5=['APPLE', 'BRAVE', 'CHASE', 'DREAM', 'ELBOW', 'FAITH', 'GRACE', 'HUMOR', 'IMAGE', 'JOKER', 'LUNCH', 'MAGIC', 'NIGHT', 'OASIS', 'PLUTO', 'QUICK', 'RAVEN', 'SUNNY', 'THUMP', 'UMBRA', 'VIVID', 'WATCH', 'XENON', 'YIELD', 'ZEBRA', 'ABOVE', 'BLISS', 'CHAMP', 'DANCE', 'EXTRA', 'FROST', 'GLOWY', 'HELLO', 'IVORY', 'JAZZY', 'KNEAD', 'LEMUR', 'MUSIC', 'NOBLE', 'OPERA', 'PRIZE', 'QUEST', 'RAINY', 'SLEEP', 'TIGER', 'UMBRA', 'VISTA', 'WORTH', 'XENIA', 'YOGIC', 'ZONAL']
    words6=['BANANA', 'CIRCLE', 'DINNER', 'EASILY', 'FOLLOW', 'GUITAR', 'HUNGRY', 'INSECT', 'JACKET', 'KINDLY', 'LANTER', 'MELLOW', 'NATION', 'OUTLET', 'PEACHY', 'QUOTER', 'RADISH', 'SIMPLE', 'THRIVE', 'UNIQUE', 'VISION', 'WILLOW', 'YELLOW', 'ZEBRAS', 'ABOUND', 'BRIDGE', 'CLOUDY', 'DAISY', 'EXQUIS', 'FUTURE', 'GIGGLE', 'HEROIC', 'ISLAND', 'JIGSAW', 'KABOOM', 'LIZARD', 'MIRROR', 'NUANCE', 'ORANGE', 'PLUMPS', 'QUESTS', 'RANGER', 'STARRY', 'TRIFLE', 'UMBRAE', 'VOLUME', 'WONDER', 'XENONS', 'YOGURT', 'ZOMBIE']
    words7=['BUBBLES', 'COTTAGE', 'DAZZLED', 'EXPLORE', 'FRIENDS', 'GARDENY', 'HUNGRY', 'ISLANDS', 'JACKETY', 'KINDRED', 'LAUGHED', 'MELLOWY', 'NAPPING', 'OCEANIC', 'PLAYFUL', 'QUIETER', 'ROSEBUD', 'SUNBEAM', 'TRENDY', 'UMBRELL', 'VALUING', 'WALKING', 'YELLOWY', 'ZOOMING', 'APPLES', 'BRIDGE', 'CHERRY', 'DAFFOD', 'EXOTIC', 'FLYING', 'GRAPES', 'HEARTY', 'ISLAND', 'JIGSAW', 'KITTEN', 'LOVING', 'MUSING', 'NATURE', 'ORANGE', 'PUPPY', 'QUIRKY', 'RAVISH', 'SUNSET', 'UNWIND', 'VIBRANT', 'WINTER']

    while True:
        try:
            print('                                                                     ----------------------------')
            print('                                                                     Number of letters:')
            print('                                                                     ----------------------------')
            print('                                                                      3 Letters')
            print('                                                                      4 Letters')
            print('                                                                      5 Letters')
            print('                                                                      6 Letters')
            print('                                                                      7 Letters')
            print('                                                                     ----------------------------')
            l=int(input('                                                                     Enter your choice: '))

            if l<3 or l>7:
                clear()
                print('                                                                     ----------------------------')
                print('                                                                     Entry out of range, enter again')
            elif l==3:
                word=random.choice(words3)
                break
            elif l==4:
                word=random.choice(words4)
                break
            elif l==5:
                word=random.choice(words5)
                break
            elif l==6:
                word=random.choice(words6)
                break
            elif l==7:
                word=random.choice(words7)
                break
        except ValueError:
            clear()
            print('                                                                     ----------------------------')
            print('                                                                     Enter only numerical values.')
    clear()
    l1=len(word)
    print('                                                                     ----------------------------')
    print(f'                                                                     The word is {l1} letters')
    a=1
    g=[]
    while a!=8:
        print('                                                                     ----------------------------')
        guess=input(f'                                                                     Guess {a}: Enter your guess: ').upper()
        t=guess.split()
        l=''
        for i in t:
            l+=i
        guess=l
        clear()
        l2=len(guess)
        
        if l1!=l2 or guess.isdigit():
            c=1
            print('                                                                     ----------------------------')
            for b in g:
                print('                                                                     Guess ',c,': |',' | '.join(b),'|')
                c+=1
            print('                                                                     ----------------------------')
            
            print('                                                                     Correctly Placed Letters: ',','.join(cpl))
            print('                                                                     Misplaced Letters: ',','.join(mpl))
            print('                                                                     Letters Not Present: ',','.join(lnp))
            print('                                                                     ----------------------------')
            print('                                                                     Enter a ',l1,' letter word')
            
        elif guess in g:
            c=1
            print('                                                                     ----------------------------')
            for b in g:
                print('                                                                     Guess ',c,': |',' | '.join(b),'|')
                c+=1
            print('                                                                     ----------------------------')
            cpl=[]
            l=len(guess)
            for i in word:
                j=word.index(i)
                if i==guess[j]:
                    cpl.append(i)

            mpl=set(guess) & set(word) - set(cpl)
            lnp=set(guess) - set(word)
            print('                                                                     Correctly Placed Letters: ',','.join(cpl))
            print('                                                                     Misplaced Letters: ',','.join(mpl))
            print('                                                                     Letters Not Present: ',','.join(lnp))
            print('                                                                     ----------------------------')
            print('                                                                    ',guess,' already guessed')
            print('                                                                     Guess again')
            
        elif guess==word:
            g.append(guess)
            c=1
            print('                                                                     ----------------------------')
            for b in g:
                print('                                                                     Guess ',c,': |',' | '.join(b),'|')
                c+=1
            print('                                                                     ----------------------------')
            cpl=[]
            l=len(guess)
            for i in word:
                j=word.index(i)
                if i==guess[j]:
                    cpl.append(i)

            mpl=set(guess) & set(word) - set(cpl)
            lnp=set(guess) - set(word)
            print('                                                                     Correctly Placed Letters: ',','.join(cpl))
            print('                                                                     Misplaced Letters: ',','.join(mpl))
            print('                                                                     Letters Not Present: ',','.join(lnp))
            print('                                                                     ----------------------------')
            print('                                                                     You guessed it right')
            print('                                                                     The word is ',guess)
            print('                                                                     ----------------------------')
            break
        
        else:
            g.append(guess)
            c=1
            print('                                                                     ----------------------------')
            for b in g:
                print('                                                                     Guess ',c,': |',' | '.join(b),'|')
                c+=1
            print('                                                                     ----------------------------')
            cpl=[]
            l=len(guess)
            for i in word:
                j=word.index(i)
                if i==guess[j]:
                    cpl.append(i)

            mpl=set(guess) & set(word) - set(cpl)
            lnp=set(guess) - set(word)
            print('                                                                     Correctly Placed Letters: ',','.join(cpl))
            print('                                                                     Misplaced Letters: ',','.join(mpl))
            print('                                                                     Letters Not Present: ',','.join(lnp))
            a+=1
            if a==8:
                print('                                                                     ----------------------------')
                print('                                                                     Attempts over')
                print('                                                                     The word was ',word)
                print('                                                                     ----------------------------')
                break
    h=input('                                                                     Press ENTER to continue...')
    clear()


a=0
while a==0:
    clear()
    clear()
    print('''
                                        ░█████╗░██╗░░░██╗██████╗░███████╗██████╗░  ░█████╗░██████╗░░█████╗░░█████╗░██████╗░███████╗
                                        ██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
                                        ██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝  ███████║██████╔╝██║░░╚═╝███████║██║░░██║█████╗░░
                                        ██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗  ██╔══██║██╔══██╗██║░░██╗██╔══██║██║░░██║██╔══╝░░
                                        ╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║  ██║░░██║██║░░██║╚█████╔╝██║░░██║██████╔╝███████╗
                                        ░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝
        
                                                                    ----------------------------
                                                                        GAMES WITH COMPUTER 
                                                                    ----------------------------
                                                                                MAIN MENU
                                                                    1. HAND CRICKET
                                                                    2. ROCK PAPER SCISSORS
                                                                    3. PIG
                                                                    4. NUMBER GUESSING
                                                                    5. HANGMAN
                                                                    6. WORDLE
                                                                    7. EXIT GAMES MENU
                                                                    ----------------------------''')
    b=0
    while b==0:
        try:
            c=int(input('                                                                         ENTER YOU CHOICE: '))
            clear()
            if c==1:
                b+=1
                c=0
                while c==0:
                    handcricket()
                    c=play_again_or_not()
                    
            elif c==2:
                b+=1
                c=0
                while c==0:
                    RPS()
                    c=play_again_or_not()
                        
            elif c==3:
                b+=1
                c=0
                while c==0:
                    PIG()
                    c=play_again_or_not()
            
            elif c==4:
                b+=1
                c=0  
                while c==0:
                    NG()            
                    c=play_again_or_not()
            
            elif c==5:
                b+=1
                c=0
                while c==0:
                    HANGMAN()
                    c=play_again_or_not()
            
            elif c==6:
                b+=1
                c=0
                while c==0:
                    WORDLE()        
                    C=play_again_or_not()
                    
            elif c==7:
                print('''
                                            ░██████╗░░█████╗░███╗░░░███╗███████╗░██████╗  ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
                                            ██╔════╝░██╔══██╗████╗░████║██╔════╝██╔════╝  ████╗░████║██╔════╝████╗░██║██║░░░██║
                                            ██║░░██╗░███████║██╔████╔██║█████╗░░╚█████╗░  ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
                                            ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗  ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
                                            ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██████╔╝  ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
                                            ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░  ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░

                                            ░█████╗░██╗░░░░░░█████╗░░██████╗███████╗██████╗░
                                            ██╔══██╗██║░░░░░██╔══██╗██╔════╝██╔════╝██╔══██╗
                                            ██║░░╚═╝██║░░░░░██║░░██║╚█████╗░█████╗░░██║░░██║
                                            ██║░░██╗██║░░░░░██║░░██║░╚═══██╗██╔══╝░░██║░░██║
                                            ╚█████╔╝███████╗╚█████╔╝██████╔╝███████╗██████╔╝
                                            ░╚════╝░╚══════╝░╚════╝░╚═════╝░╚══════╝╚═════╝░''')
                h=input()
                clear()
                b+=1
                a+=1
                print()

        except ValueError:
            print('                                                                     ----------------------------')
            print('                                                                     CHOOSE ONLY FROM THE RANGE OF GAMES')
            print('                                                                     ----------------------------')