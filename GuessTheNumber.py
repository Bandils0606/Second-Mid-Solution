n = 56  #This is the number which shouldn't be shown in the output of this program.

print('Welcome to the Guessing Game.\nYou have to guess a number between 1-100.')
print('You have total 10 chances.\n')

remaining = 10
count = 1

for i in range (remaining, 0, -1):
    num = int(input('Enter your number:'))
    if num == n:
        print('Congratulations you hit the jackpot just in ',count,'try(s).')
        print('Thankyou.')
        break

    else:
        if num < n:
            print('The number you entered is too low.')
        elif num > n:
            print('The number you entered is too high.')
        
        remaining -= 1
        print('Oops!. The number you has entered isn\'t the jackpot number. Try again.')
        print('Total chances remaining:',remaining); print('\n')
        if remaining ==0:
            print('Game over.')
    count += 1
