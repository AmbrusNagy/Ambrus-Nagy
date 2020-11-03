import random

number_computer = random.randint(1, 20)

for i in range(5):
    number_player = int(input('Guess my number: '))
    if number_player == number_computer:
        print('Well done! You guessed right!')
        break
    else:
        if number_player < number_computer:
            print('too low!')
        if number_player > number_computer:
            print('too high!')
        if number_player > 20:
            print('You need a number under 20! ')
if number_player > number_computer or number_player < number_computer:
    print('You lost!', 'My number was', number_computer)