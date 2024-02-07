number = 10
i = 2 # Number of guesses

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))
while guess != 'q' and i >= 0:
    print()
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess > number:
        print(f'Sorry! {guess} was too high.', end=' ')
    else:
        print(f'Sorry! {guess} was too low.', end=' ')

    if i > 0:
        print(f'You have {i} guess(es) left.')
        guess = input('Try again or type "q" to quit: ')
    else:
        print(f'The number was {number}')
    
    i -= 1
