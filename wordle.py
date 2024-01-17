import os
import random

def clear():
    os.system('cls')

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

