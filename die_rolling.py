import random

die1 =  random.randint(1,6)
die2 =  random.randint(1,6)

while True:
    die1 =  random.randint(1,6)
    die2 =  random.randint(1,6)
    choose = input('do you want to continue(y/n): ')
    if choose == 'n':
        print('thanks for playing')
        break
    else:
        print(f'you have rolled {die1} and {die2}')


