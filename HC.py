import random
import os

def clear():
    os.system('cls')

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

