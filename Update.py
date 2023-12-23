# Program to create a personal statement for university applications

user_details = []
user_details2 = {}

def interests0():
    print("what are your academic interests?")
    response = input("> ")
    return True, user_details.append(str(response))

def occupation1():
    print("what do you work as?")
    response = input("> ")

    return True, user_details.append(str(response))

def aspirations2():
    print("what would you like to do in future?")
    response = input("> ")
    return True, user_details.append(str(response))

def university3():
    print("what would you like to not do")
    response = input("> ")
    return True, user_details.append(str(response))

def bachelors_degree():
    bachelors = input("what degree did you study for bachelors?: ")
    bachelors_grade = input("what grade did you get?: ")

    return True ,user_details2.update({str(bachelors):int(bachelors_grade)})

def hobbies4():
    print("what are some of your some of your hobbies?: ")
    response = input("> ")

    return True, user_details.append(str(response))

def personaldescription5():
    print("could you give more detail more about yourself?")
    print("starting with your full name")
    response = input("> ")

    return True, user_details.append(str(response))

def reason_of_interest6():
    print("could you tell me why you're applying to this school?")
    response = input("> ")

    return True, user_details.append(str(response))

def introduction():
    options = ["yes","no"]
    print("Hii, I'm an app created to help you make your personal statement")
    print("would you like to continue?")

    print(options)
    response = input("> ")

    if response.casefold() == options[0]:
        return interests0(), occupation1(), aspirations2(), university3(), bachelors_degree(), hobbies4(), personaldescription5(), reason_of_interest6()
    else:
        return False

if __name__ == "__main__":
    introduction()
    print(f"My name is {user_details[5]}.\n"
          f"In order to achieve my interests in {user_details[2]} \n"
          f"While is school studying {user_details2.keys()} at {user_details[3]}, I worked hard and was able to acheive a {user_details['finance']}. \n"
          f"Aside school i took part in extra curriculum activities to further my hobbies like {user_details[4]}. \n"
          f"since leaving school I started my job as a {user_details[1]}. \n"
          f"The reason I am applying to your school is because {user_details[6]}. Thank you for your consideration"
          )




