from random import randint
number = randint(1,10)
while True:
    guess = int(input('Ваше число: '))
    if guess < number:
        print(f'Ваше число меньше.')
    elif guess > number:
        print(f'Ваше число больше.')
    elif guess == number:
        print(f'Вы победили!')
        break
    else:
        print(f'неправльный формат.')
        exit()
