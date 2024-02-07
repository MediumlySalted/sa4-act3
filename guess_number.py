number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

i = 2
while guess != 'q' and i >= 0:
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif i > 0:
        print(f'Sorry! {guess} was not the number I was thinking of. You have {i} guess(es) left.')
        guess = input('Try again or type "q" to quit: ')
    else:
        print(f'Sorry. {guess} was not the number I was thinking of. The number was {number}')
    
    i -= 1
