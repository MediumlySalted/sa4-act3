number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while guess != 'q':
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f'Sorry! {guess} was not the number I was thinking of')
        guess = input('Try again or type "q" to quit: ')
