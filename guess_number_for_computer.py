import random


def main():
    guess(100)

def guess(x):
    low = 1
    high = int (x)
    feedback=' '

    

    while feedback !='c':
        if low!=high:
            guess=random.randint(low,high)
            
        elif low==high:
            guess =low #or it can be high also

        feedback = input(f"Is {guess} correct . If it is type 'C'(correct) or 'L'(low) or 'H'(high) : ".lower())


        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    
    print("Correct Answer")




if __name__=='__main__':
    main()