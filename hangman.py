import random

def hangman(word):
    wrong = 0
    stages = ['',
              '______        ',
              '|      |       ',
              '|      |       ',
              '|      0       ',
              '|     /|\      ',
              '|     / \      '
              ]
    rletters = list(word)
    board = ['__']*len(word)
    win = False
    print('Welcome to death')

    while wrong<len(stages)-1:
        print('\n')
        char = input('enter a letter: ')
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong+=1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '__' not in board:
            print('you win! The word was: ')
            print(' '.join(board))
            win = True
            break
    if not win:
        #print('\n'.join(stages[0:wrong]))
        print('you lose, the word was: {}.'.format(word))

Words=['cat',
       'cow',
       'monster',
       'god',
       'dog',
       'shelter',
       'author',
       'gamer',
       'designer',
       'application',
       'music',
       'dance']
print(Words)
#not work
'''
try:
    with open('words.txt','r') as f:
        Words=[]
        for item in f:
            Words.append(item)
        print(Words)
except FileNotFoundError: 0

while (input('do you want to add word to dictionary? y/n ')=='y'):
    with open('words.txt','w') as f:
        Words.append(input('input word: '))
        for item in Words:
            f.write('{}'.format(item))
    print(Words)
'''


hangman(random.choice(Words))


