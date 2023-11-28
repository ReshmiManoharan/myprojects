import random  

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
           guess=random.randint(low,high)
        else:
            guess=low
        print("===============================")
        print("Guess a number between 1 to 10")
        print("===============================")

        feedback=input(f'Is {guess} too high(h), too low(l), or correct(c).. Enter your option as in the bracket: ')
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print("===============================")
    print(f'Yay!! Your number {guess} is right!!')



computer_guess(10)
    