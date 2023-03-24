secret_word='Noran'

while True:
    guess=input("Enter Guess : ")
    if secret_word == guess:
        print("You Won!")
        break