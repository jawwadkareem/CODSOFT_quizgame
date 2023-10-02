# admin password is '12345'
def Quiz_Game():
    score = 0
    number = 1
    count = 0
    for i in quiz:
        count += 1
        if count != 5 and count != 10:
            print("\nQuestion", number, ':', i[0])
            number += 1
            print('a.', i[1], "\nb.", i[2], "\nc.", i[3])
            a, b, c = 1, 2, 3
            user = input("Select from the options a,b and c: ")
            print("\n")
            user = user.lower()
            if user == 'a' or user == 'b' or user == 'c':
                if i[eval(user)] == i[4]:
                    print("Your answer is correct")
                    score += 10
                    print('Your score:', score)
                else:
                    print('\nYou have selected the wrong option')
                    print("The correct answer is:", i[4])
                    print('Your score:', score)
            else:
                user = input("Please enter either a,b or c, otherwise your marks will be deducted: ")
                print("\n")
                user = user.lower()
                if user == 'a' or user == 'b' or user == 'c':
                    if i[eval(user)] == i[4]:
                        print("Your answer is correct")
                        score += 10
                        print("Your score:", score)
                    else:
                        print("\nYou have selected the wrong option")
                        print("The correct answer is:", i[4])
                        print("Your score:", score)
                else:
                    score -= 10
                    print("10 marks have been deducted")
                    print("Your score:", score)
        else:
            print("\nBonus Question")
            # Printing the Question and providing options
            print("\nQuestion", number, ':', i[0])
            number += 1
            print('a.', i[1], "\nb.", i[2], "\nc.", i[3])
            a, b, c = 1, 2, 3
            # Taking input from user
            user = input("Select from the options a,b and c: ")
            user = user.lower()
            if user == 'a' or user == 'b' or user == 'c':
                if i[eval(user)] == i[4]:
                    print("Your answer is correct")
                    score += 50
                    print('Your score:', score)
                else:
                    print('\nYou have selected the wrong option')
                    print("The correct answer is:", i[4])
                    print('Your score:', score)
            else:
                user = input("Please enter either a,b or c, otherwise your marks will be deducted: ")
                print("\n")
                user = user.lower()
                # Checking whether the input is correct or not
                if user == 'a' or user == 'b' or user == 'c':
                    if i[eval(user)] == i[4]:
                        print("Your answer is correct")
                        score += 50
                        print("Your score:", score)
                    else:
                        print("\nYou have selected the wrong option")
                        print("The correct answer is:", i[4])
                        print("Your score:", score)
                # Deducting marks
                else:
                    score -= 10
                    print("10 marks have been deducted")
                    print("Your score:", score)
    print("\nYou have finished the game")
    print("Your final score:", score)
    with open('score.txt', 'a') as i:
        savescore = i.write(str(score) + ',')
    with open("score.txt") as j:
        x = eval(j.read())
        print("Best Score:", max(x))


print("                             Welcome To Quiz Game")
while True:
    print('\nHow do you want to proceed?\n1. As an Administrator\n2. As a Player')
    player = input("Enter your choice to continue: ")
    if player == '2':
        print("You have selected to continue as a Player")
        print("\nNote the rules before starting: ")
        print("Each question carries 10 marks")
        print("Questions 5 and 10 are bonus questions. Both of them carry 50 marks apiece")
        while True:
            print(
                '\nWhich domain do you want to take the Quiz of?\n1. Cricket\n2. Pakistan Studies\n3. General Knowledge\n')
            domain = input("Enter your selection to start the quiz game: ")
            if domain == '1':
                print("\nYou have selected the domain of Cricket")
                with open("cric.txt") as f:
                    quiz = eval(f.read())
                    Quiz_Game()
                exit = input("If you want to play the game again, press \'Y\' otherwise press \'N\'")
                if exit == 'Y' or exit == 'y':
                    continue
                else:
                    break
            elif domain == '2':
                print("\nYou have selected the domain of Pakistan Studies")
                with open("pst.txt") as f:
                    quiz = eval(f.read())
                    # Calling the function
                    Quiz_Game()
                exit = input("If you want to play the game again, press \'Y\' otherwise press \'N\'")
                if exit == 'Y' or exit == 'y':
                    continue
                else:
                    break
            elif domain == '3':
                print("\nYou have selected the domain of General Knowledge")
                with open("gk.txt") as f:
                    quiz = eval(f.read())
                    Quiz_Game()
                exit = input("If you want to play the game again, press \'Y\' otherwise press \'N\'")
                if exit == 'Y' or exit == 'y':
                    continue
                else:
                    break
            else:
                print("\nYou have selected a wrong option. Please select from the given options.\n")
    elif player == '1':
        # admin password is '12345'
        password = input('Enter your password: ')
        f = open('password.txt')
        k = f.read()
        if password == k:
            while True:
                print('What do you want to do?\n')
                print(
                    '1. Read questions\n2. Add questions\n3. Remove questions\n4. Replace questions\n5. Change Password\n')
                choice = input('Enter your choice: ')
                if choice == '1':
                    while True:
                        print('Which domain do you want to read the questions of?')
                        print('1. Cricket\n2. Pakistan studies\n3. General Knowledge\n')



                        def dom():
                            def quiz_read():
                                number = 0
                                for i in cric:
                                    number += 1
                                    count = 0
                                    for j in i:
                                        count += 1
                                        if count == 5:
                                            print('The answer is ', '\"', j, '\"\n')
                                        elif count == 1:
                                            print('Question No.', number, ':', j)
                                        elif count == 2:
                                            print('a)', j)
                                        elif count == 3:
                                            print('b)', j)
                                        elif count == 4:
                                            print('c)', j)

                            domain = input('Press either 1, 2 or 3 to select: ')
                            print("\n")
                            if domain == '1':
                                f = open('cric.txt')
                                cric = eval(f.read())
                                quiz_read()
                                f.close()
                            elif domain == '2':
                                f = open('PST.txt')
                                cric = eval(f.read())
                                quiz_read()
                                f.close()
                            elif domain == '3':
                                f = open('GK.txt')
                                cric = eval(f.read())
                                quiz_read()
                                f.close()
                            else:
                                print('Please select from given options\n'), dom()


                        dom()
                        exit = input(
                            "If you want to read another set of questions, press \'Y\', otherwise press \'N\': ")
                        if exit == 'Y' or exit == 'y':
                            continue
                        elif exit == 'N' or exit == 'n':
                            break
                elif choice == '2':
                    while True:
                        print('In which domain do you want to add questions?')
                        print('1. Cricket\n2. Pakistan studies\n3. General Knowledge\n')


                        def dom():
                            def quiz_append():
                                while True:
                                    k = []
                                    a = input('Enter the question: ')
                                    b = input('Enter the first option: ')
                                    c = input('Enter the second option: ')
                                    d = input('Enter the third option: ')
                                    e = input('Enter the answer: ')
                                    # Appending the questions to a list
                                    k.append(a)
                                    k.append(b)
                                    k.append(c)
                                    k.append(d)
                                    k.append(e)
                                    cric.append(k)
                                    # Asking the Administrator whether they want to add more questions or not, and taking their response
                                    another = input(
                                        'If you want to add another question, press \'Y\', otherwise press \'N\': ')
                                    # Checking Administrator's response
                                    if another == 'Y' or another == 'y':
                                        continue
                                    elif another == 'N' or another == 'n':
                                        break

                            # Taking Administrator's input
                            domain = input('Press either 1, 2 or 3 to select: ')
                            print("\n")
                            # Checking the Administrator's input
                            if domain == '1':
                                # Opening a file and appending questions
                                f = open('cric.txt', 'a+')
                                f.seek(0)
                                cric = eval(f.read())
                                # Calling a function
                                quiz_append()
                                f = open('cric.txt', 'w')
                                f.write(str(cric))
                                f.close()
                            elif domain == '2':
                                # Opening a file and appending questions
                                f = open('PST.txt', 'a+')
                                f.seek(0)
                                cric = eval(f.read())
                                # Calling a function
                                quiz_append()
                                f = open('PST.txt', 'w')
                                f.write(str(cric))
                                f.close()
                            elif domain == '3':
                                # Opening a file and appending questions
                                f = open('GK.txt', 'a+')
                                f.seek(0)
                                cric = eval(f.read())
                                # Calling a function
                                quiz_append()
                                f = open('GK.txt', 'w')
                                f.write(str(cric))
                                f.close()
                            else:
                                # Prompting Administrator to give a correct input and recalling the function
                                print('Please give a correct input\n'), dom()


                        # Calling a function to check domain and appending questions
                        dom()
                        # Asking the Administrator whether they want to append questions to another domain, and taking their input
                        add = input(
                            'If you want to add more questions in another domain, press \'Y\', otherwise press \'N\': ')
                        # Checking Administrator's input
                        if add == 'Y' or add == 'y':
                            continue
                        elif add == 'N' or add == 'n':
                            break
                elif choice == '3':
                    while True:
                        # Asking the Administrator which domain they want to remove questions from
                        print('From which domain do you want to remove questions?')
                        print('1. Cricket\n2. Pakistan studies\n3. General Knowledge\n')


                        # Defining a function which prompts the Administrator to inform from which domain they want to remove questions
                        def dom():
                            # Taking Administrator's input
                            domain = input('Press either 1, 2 or 3 to select: ')
                            print("\n")
                            # Checking Administrator's input
                            if domain == '1':
                                while True:
                                    # Opening a file to remove questions from
                                    f = open('cric.txt', 'a+')
                                    f.seek(0)
                                    cric = eval(f.read())
                                    # Asking the user which question number they want to remove
                                    a = int(input('Which question do you want to remove: '))
                                    # Removing the question
                                    cric.pop(a - 1)
                                    f = open('cric.txt', 'w')
                                    f.write(str(cric))
                                    f.close()
                                    # Displaying the updated file
                                    print('\nThis is the updated record:\n')
                                    f = open('cric.txt')
                                    quizz = eval(f.read())
                                    number = 0
                                    # Displaying all the questions
                                    for i in quizz:
                                        number += 1
                                        count = 0
                                        for j in i:
                                            # Displaying the Question, it's options and the correct answer
                                            count += 1
                                            if count == 5:
                                                print('The answer is ', '\"', j, '\"\n')
                                            elif count == 1:
                                                print('Question No.', number, ':', j)
                                            elif count == 2:
                                                print('a)', j)
                                            elif count == 3:
                                                print('b)', j)
                                            elif count == 4:
                                                print('c)', j)
                                    f.close()
                                    # Asking the Administrator whether they want to remove more questions, and taking their input
                                    exit = input(
                                        '\nIf you want to remove more questions from this domain, press \'Y\', otherwise press \'N\':')
                                    # Checking Administrator's input
                                    if exit == 'Y' or exit == 'y':
                                        continue
                                    else:
                                        break
                            elif domain == '2':
                                while True:
                                    f = open('PST.txt', 'a+')
                                    f.seek(0)
                                    cric = eval(f.read())
                                    a = int(input('Which question do you want to remove: '))
                                    cric.pop(a - 1)
                                    f = open('PST.txt', 'w')
                                    f.write(str(cric))
                                    f.close()
                                    print('\nThis is the updated record:\n')
                                    f = open('PST.txt')
                                    quizz = eval(f.read())
                                    number = 0
                                    for i in quizz:
                                        number += 1
                                        count = 0
                                        for j in i:
                                            count += 1
                                            if count == 5:
                                                print('The answer is ', '\"', j, '\"\n')
                                            elif count == 1:
                                                print('Question No.', number, ':', j)
                                            elif count == 2:
                                                print('a)', j)
                                            elif count == 3:
                                                print('b)', j)
                                            elif count == 4:
                                                print('c)', j)
                                    f.close()
                                    exit = input(
                                        '\nIf you want to remove more questions from this domain, press \'Y\', otherwise press \'N\':')
                                    if exit == 'Y' or exit == 'y':
                                        continue
                                    else:
                                        break
                            elif domain == '3':
                                while True:
                                    f = open('GK.txt', 'a+')
                                    f.seek(0)
                                    cric = eval(f.read())
                                    a = int(input('Which question do you want to remove: '))
                                    cric.pop(a - 1)
                                    f = open('GK.txt', 'w')
                                    f.write(str(cric))
                                    f.close()
                                    print('\nThis is the updated record:\n')
                                    f = open('GK.txt')
                                    quizz = eval(f.read())
                                    number = 0
                                    for i in quizz:
                                        number += 1
                                        count = 0
                                        for j in i:
                                            count += 1
                                            if count == 5:
                                                print('Answer is ', '\"', j, '\"\n')
                                            elif count == 1:
                                                print('Question No.', number, ':', j)
                                            elif count == 2:
                                                print('a)', j)
                                            elif count == 3:
                                                print('b)', j)
                                            elif count == 4:
                                                print('c)', j)
                                    f.close()
                                    exit = input(
                                        '\nIf you want to remove more questions from this domain, press \'Y\', otherwise press \'N\':')
                                    if exit == 'Y' or exit == 'y':
                                        continue
                                    else:
                                        break
                            else:
                                print('Please give a correct input\n'), dom()


                        dom()
                        close = input(
                            'If you want to remove questions from another domain, press \'Y\', otherwise press \'N\':')
                        if close == 'Y' or close == 'y':
                            continue
                        else:
                            break
                elif choice == '4':
                    while True:
                        # Asking the Administrator which domain they want to replace questions of
                        print('From which domain do you want to replace questions?')
                        print('1. Cricket\n2. Pakistan studies\n3. General Knowledge\n')


                        def dom():
                            def quiz_replace():
                                a = int(input('Which question do you want to replace: '))
                                k = []
                                b = input('Enter your question: ')
                                c = input('Enter the first option: ')
                                d = input('Enter the second option: ')
                                e = input('Enter the third option: ')
                                f = input('Enter the Answer: ')
                                k.append(b)
                                k.append(c)
                                k.append(d)
                                k.append(e)
                                k.append(f)
                                cric[a - 1] = k

                            def quiz_read():
                                number = 0
                                for i in cric:
                                    number += 1
                                    count = 0
                                    for j in i:
                                        count += 1
                                        if count == 5:
                                            print('The answer is ', '\"', j, '\"\n')
                                        elif count == 1:
                                            print('Question No.', number, ':', j)
                                        elif count == 2:
                                            print('a)', j)
                                        elif count == 3:
                                            print('b)', j)
                                        elif count == 4:
                                            print('c)', j)

                            domain = input('Press either 1, 2 or 3 to select: ')
                            print("\n")
                            if domain == '1':
                                while True:
                                    f = open('cric.txt', 'a+')
                                    f.seek(0)
                                    cric = eval(f.read())
                                    quiz_replace()
                                    f = open('cric.txt', 'w')
                                    f.write(str(cric))
                                    f.close()
                                    print('\nThis is the updated record:\n')
                                    f = open('cric.txt')
                                    quizz = eval(f.read())
                                    quiz_read()
                                    f.close()
                                    exit = input(
                                        'If you want to replace another question from this domain, press \'Y\', otherwise press \'N\':')
                                    if exit == 'Y' or exit == 'y':
                                        continue
                                    else:
                                        break
                            elif domain == '2':
                                while True:
                                    f = open('PST.txt', 'a+')
                                    f.seek(0)
                                    cric = eval(f.read())
                                    quiz_replace()
                                    f = open('PST.txt', 'w')
                                    f.write(str(cric))
                                    f.close()
                                    print('\nThis is the updated record:\n')
                                    f = open('PST.txt')
                                    quizz = eval(f.read())
                                    quiz_read()
                                    f.close()
                                    exit = input(
                                        'If you want to replace another question from this domain, press \'Y\', otherwise press \'N\':')
                                    if exit == 'Y' or exit == 'y':
                                        continue
                                    else:
                                        break
                            elif domain == '3':
                                while True:
                                    f = open('GK.txt', 'a+')
                                    f.seek(0)
                                    cric = eval(f.read())
                                    quiz_replace()
                                    f = open('GK.txt', 'w')
                                    f.write(str(cric))
                                    f.close()
                                    print('\nThis is the updated record:\n')
                                    f = open('GK.txt')
                                    quizz = eval(f.read())
                                    quiz_read()
                                    f.close()
                                    exit = input(
                                        'If you want to replace another question from this domain, press \'Y\', otherwise press \'N\':')
                                    if exit == 'Y' or exit == 'y':
                                        continue
                                    else:
                                        break
                            else:
                                print('Please give a correct input\n'), dom()
                        dom()
                        close = input(
                            'If you want to replace questions from another domain, press \'Y\', otherwise press \'N\':')
                        if close == 'Y' or close == 'y':
                            continue
                        else:
                            break
                elif choice == '5':
                    password = input('Enter the new password: ')
                    f = open('password.txt', 'w')
                    f.write(password)
                    f.close()
                end = input(
                    'If you want to go back to the Administrator menu, press \'Y\', otherwise press \'N\': ')
                if end == 'Y' or end == 'y':
                    continue
                else:
                    break
        else:
            print('You have entered wrong password\n')

    else:
        print("Please select from the given options")
    menu = input('If you want to go back to the main menu, press \'Y\', otherwise press \'N\' ')
    if menu == 'Y' or menu == 'y':
        continue
    elif menu == 'N' or menu == 'n':
        break
    else:
        print("\nPlease enter a valid choice; Either \'Y\' or \'N\'\n")
