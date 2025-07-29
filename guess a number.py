# list of numbers
numbers=[20,32,65,44,33,22,57]
#the infinite loop asking user to guess a number.
while True:
    question = input("guess a number or type q to quit.")
    if question == "q":
        print("You quit. Game over")
        break
    try:
        guess = int(question)
        if guess in numbers:
            print("correct, you got it")
        else:
            print("wrong, you didnt get it")
    except ValueError:
        print("please type a number or q to quit.")
