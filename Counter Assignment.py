numOne = int(input("Please enter a number."))
numTwo = 1


def add():
    global numOne
    user = input("\nWould you like to add?")

    if user == "yes":
        numOne = numOne + numTwo
        print(numOne)

        add()

    else:

        def sub():
            global numOne
            user = input("Would you like to subtract")

            if user == "yes":
                numOne = numOne - numTwo
                print(numOne)
                sub()
            else:
                add()

        sub()


add()
