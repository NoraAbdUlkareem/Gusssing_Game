secret_word='Noran'
guess_limit=5
guess_count=0

while guess_count<guess_limit:
    guess=input("Enter Guess : ")
    if secret_word == guess:
        print("You Won!")
        break 
    guess_count +=1

if guess_count==guess_limit:
    print("You Lost")