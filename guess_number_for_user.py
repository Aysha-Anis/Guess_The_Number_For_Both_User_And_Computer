import random
def main():
    guess(100)

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess = int(input(f"Guess a number between 1 to {x} : "))
        if guess>random_number:
            print(f"Wrong number . Your number is too high")
        elif guess<random_number:
            print(f"Wrong number, Your number is too low")
    
    print(f"Congratulation , you have guessed the right number ,{random_number}")

if __name__=='__main__':
    main()