import random

def is_int(element: str) -> bool: #function to determine if an input can be converted to an integer
    try:
        int(element)
        return True
    except ValueError:
        return False

while True: #system while loop, can continue creating and solving problems if wanted
    while True: #difficulty selection loop
        print("\n1: coefficient 'a' always equals 1, coefficients 'b' & 'c' don't exceed 50, no need for the quadratic formula")
        print("2: coefficient 'a' doesn't exceed 10, coefficients 'b' & 'c' don't exceed 100, no need for the quadratic formula")
        print("3: coefficients don't exceed 100, the quadratic formula should be used")
        print("4: coefficients are always between 100 and 1000, the quadratic formula should be used")
        difficulty = input("Select a difficulty: ")
        if not is_int(difficulty): #if they didn't enter a number
            print("\nInvalid selection\n")
        else:
            difficulty = int(difficulty)
            if difficulty < 1 or difficulty > 4: #if they didn't enter one of the difficulty options
                print("\nInvalid selection\n")
            else:
                break

    while True: #amount of problem selection loop
        num_problems = input("How many problems would you like (choose less than 50): ")
        if not is_int(num_problems):
            print("\nInvalid selection\n")
        else:
            num_problems = int(num_problems)
            if num_problems > 50:
                print("\nInvalid selection\n")
            else:
                break
    a_max = 1
    b_max = 50
    c_max = 50
    quad = False
    if difficulty == 2:
        a_max = 10
        b_max = 100
        c_max = 100
    elif difficulty == 3:
        a_max = 100
        b_max = 100
        c_max = 100
        quad = True
    elif difficulty == 4:
        a_max = 1000
        b_max = 1000
        c_max = 1000
        quad = True

    a_min = -a_max
    b_min = -b_max
    c_min = -c_max
    if difficulty == 1:
        a_min = 1


    print("\nINSTRUCTIONS: \nEnter your answer with up to 3 digits after the decimal")
    print("If there are two roots enter your answer separated by a space")

    for problem_num in range(1, num_problems+1): #problem solving loop
        print("\nProblem Number " + str(problem_num) + "\n")
        while True: #equation gen loop
            while True: #coefficient gen loop
                a = random.randint(a_min, a_max)
                b = random.randint(b_min, b_max)
                c = random.randint(c_min, c_max)
                if not (a == 0 or b == 0 or c == 0):
                    if not (difficulty == 4 and (a < 100 and a > -100 or b < 100 and b > 100 or c < 100 and c > 100)):
                        break
            determinant = b**2-4*a*c
            if determinant >= 0:
                sigfig = 3 #max(len(str(a)), len(str(b)), len(str(c)))
                answer = [round((-b + determinant**0.5)/(2*a), sigfig), round((-b - determinant**0.5)/(2*a), sigfig)]
                if not quad:
                    i1, d1 = divmod(answer[0], 1)
                    i2, d2 = divmod(answer[1], 1)
                    if d1 == 0 and d2 == 0:
                        break
                else:
                    break

        eq = str(a) + "x^2 + " + str(b) + "x + " + str(c)
        if b < 0 and c < 0:
            eq = str(a) + "x^2 - " + str(abs(b)) + "x - " + str(abs(c))
        elif b < 0:
            eq = str(a) + "x^2 - " + str(abs(b)) + "x + " + str(c)
        elif c < 0:
            eq = str(a) + "x^2 + " + str(b) + "x - " + str(abs(c))
        print(eq)
        while True: #loop for continued guessing (if you get it wrong you can try again)
            while True: #loop for checking valid guesses
                guess = input("Enter your answer: ").split()
                if len(guess) == 0:
                    print("You didn't enter an answer")
                elif len(guess) > 2:
                    print("You entered too many numbers")
                elif not is_int(guess[0]) or not is_int(guess[1]):
                    print("Invalid guess (not a number)")
                else:
                    break

            if len(guess) == 1: #if there is only one guess, append it to the list so there is 2 indexes
                guess.append(guess[0])

            for x in range(0, len(guess)): #convert all indices to floats
                guess[x] = float(guess[x])

            if (guess[0] == answer[0] and guess[1] == answer[1]) or (guess[0] == answer[1] and guess[1] == answer[0]):
                print("\nCongratulations! You got it right!")
                break
            elif guess[0] == answer[0] or guess[0]==answer[1] or guess[1] == answer[1] or guess[1] == answer[0]:
                print("\nNice try, you got the one root correct but the other root wrong")
            else:
                print("\nNice try but you got it wrong")

            if not input("Enter 1 to guess again; Enter anything else to see the answer: ") == "1":
                break

        if determinant > 0:
            print("There are two roots:")
            print("x1 = " + str(answer[0]))
            print("x2 = " + str(answer[1]))
        elif determinant == 0:
            print("There is one root:")
            print("x = " + str(answer[0]))

    if not input("\nEnter 1 to go again (anything else to quit): ") == "1":
        break
