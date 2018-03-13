import random  # for choosing random words
import json  # db
import sys  # for exiting script
score = 0
mistakes = 0
gamecount = 0
userid = 0


def game():
    global gamecount
    global mistakes
    global score
    print "Hangman"
    ctg = raw_input("Choose your category\nA) Animals\nB) Cars\n>")
    dif = raw_input("Choose your difficulty\nA) Easy- 1point\nB) Medium- 3 points\nC) Hard- 5points\n>")
    with open("database/words.json", "r") as f:
        data = json.load(f)
        if ctg == "A" and dif == "A":
            name = list(data["Animals_EASY"][random.randint(0, len(data["Animals_EASY"]) - 1)])  # word to guess
        elif ctg == "A" and dif == "C":
            name = list(data["Animals_HARD"][random.randint(0, len(data["Animals_HARD"]) - 1)])  # word to guess
        elif ctg == "A" and dif == "B":
            name = list(data["Animals_MEDIUM"][random.randint(0, len(data["Animals_MEDIUM"]) - 1)])  # word to guess

        elif ctg == "B" and dif == "A":
            name = list(data["Cars_EASY"][random.randint(0, len(data["Cars_EASY"]) - 1)])  # word to guess
        elif ctg == "B" and dif == "C":
            name = list(data["Cars_HARD"][random.randint(0, len(data["Cars_HARD"]) - 1)])  # word to guess
        elif ctg == "B" and dif == "B":
            name = list(data["Cars_MEDIUM"][random.randint(0, len(data["Cars_MEDIUM"]) - 1)])  # word to guess

        new_name = []
        new_secret = []
        for letter in name:
            if letter.isspace():
                new_name.append("-")
                new_secret.append("-")
            else:
                new_name.append(letter)
                new_secret.append("_ ")

    print ' '.join(new_secret)

    while True:
        if new_secret == new_name:
            print "You won"
            if dif == "A":
                score += 1
            elif dif == "B":
                score += 3
            elif dif == "C":
                score += 5
            print "Current points: {}".format(score)
            print ""
            game()
        if mistakes == 7:
            print "You lost"
            with open("database/stats.json", "r") as f:
                data = json.load(f)
            for i in data:
                if data[i] != userid:
                    dictt = {userid: {"Highscore": 0}}
                    break
            data.update(dictt)
            with open("database/stats.json", "w") as f:
                json.dump(data, f, indent=2)
            with open("database/stats.json", "r") as f:
                data = json.load(f)
                highscore = data[userid]["Highscore"]

            if score > highscore:
                data[userid]["Highscore"] = score

            with open("database/stats.json", "w") as f:
                json.dump(data, f, indent=2)

            play_again = raw_input("Play again ?\nY/N\n>")
            if play_again == "Y" or play_again == "y":
                mistakes = 0
                game()
            elif play_again == "N" or play_again == "n":
                with open("database/user.json", "r") as f:
                    data = json.load(f)
                user_logout = data[userid]["Name"]
                print "See you next time {}.".format(user_logout)
                sys.exit()
            else:
                print "Exited"
                sys.exit()
        char_input = raw_input("Type a letter:")
        if char_input in new_name:
            for i in range(len(name)):
                if char_input == new_name[i]:
                    new_secret[i] = char_input
        else:
            mistakes += 1
        if mistakes == 1:
            print """
            ________
            |
            |
            |
            |
            |____
            """
        elif mistakes == 2:
            print """
            ________
            |      O
            |
            |
            |
            |____
            """
        elif mistakes == 3:
            print """
            ________
            |      O
            |      |
            |      |
            |
            |____
            """
        elif mistakes == 4:
            print """
            ________
            |      O
            |     \|
            |      |
            |
            |____
            """
        elif mistakes == 5:
            print """
            ________
            |      O
            |     \|/
            |      |
            |
            |____
            """
        elif mistakes == 6:
            print """
            ________
            |      O
            |     \|/
            |      |
            |     /
            |____
            """
        elif mistakes == 7:
            print """
            ________
            |      O
            |     \|/
            |      |
            |     / \\
            |____
            """
        print ""
        print ' '.join(new_secret)


#========================================
#=Game
#========================================

def start():
    username_input = raw_input("Enter your username\n>")
    password_input = raw_input("Enter your password\n>")
    numvar = 0
    with open("database/user.json") as f:
        data = json.load(f)
        for i in data:
            if username_input == data[i]["Username"] and password_input == data[i]["Password"]:
                global userid
                userid = i
                game()
        print "You do not have an account. Do you want to sign up ?"
        for i in data:
            numvar += 1
        sign_up = raw_input("Y/N")
        if sign_up == "Y" or sign_up == "y":
            username = raw_input("Enter username: ")
            password = raw_input("Enter password: ")
            confirm_password = raw_input("Confirm password: ")
            # loop derisa confirm password == password
            while confirm_password != password:
                print "Wrong password"
                password = raw_input("Enter password: ")
                confirm_password = raw_input("Confirm password: ")
            name = raw_input("Enter name: ")
            surname = raw_input("Enter surname: ")
            email = raw_input("Enter Email: ")
            numvar += 1
            a_dict = {numvar: {"Username": username, "Password": password, "Name": name, "Surname": surname, "Email": email}}
            data.update(a_dict)
            with open("database/user.json", "w") as f:
                json.dump(data, f, indent=2)
        elif sign_up == "N" or sign_up == "n":
            print "Goodbye."
        else:
            print "The given input is not understandable. Please write Y for yes and N for no."


start()
