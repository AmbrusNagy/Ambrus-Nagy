import random

print('0 = rock, 1 = paper, 2 = scissors')
p = int(input('Lets play!'))
c = random.randint(0,2)
 
if p == 0:
    print('You have chosen Rock!')
if p == 1:
    print('You have chosen paper!')
if p == 2:
     print('You have chosen scissors!') 
if c == 0:
    print('The computer has chosen Rock!')
if c == 1:
    print('The computer has chosen paper!')
if c == 2:
     print('The computer has chosen scissors!')

if p == c :
    print('Tie!')
if p == 0 and c ==1 or p == 1 and c == 2 or p == 2 and c == 0:
    print('You Lost!')
if p == 1 and c ==0 or p == 2 and c == 1 or p == 0 and c == 2:
    print('You Won!')
if p > 2:
    print('ERROR!!!')