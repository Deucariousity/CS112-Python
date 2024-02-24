# Import Module
import time
# Storage of user credentials
user_accounts = {}


# Database Area -------------------------------------------------------------------------------------------------------
# Functions for user registration (Sign Up)
def register_user(username, password):
    if username in user_accounts:
        print("Sorry!"
              "\n<Username already existed"
              "\nPlease create a different one>"
              "\nThank you!")
        return None
    else:
        user_accounts[username] = password
        print("Successfully Signed in"
              "\n<You can now proceed to Log in your account>")
        return username


# Function for user login (Sign In)
def login_user(username, password):
    if username in user_accounts and user_accounts[username] == password:
        print(f"Welcome Ma'am/Sir!, {username}!")
        return username
    else:
        print("ERROR 404: Account Not Found!"
              "\n<Invalid username or password>"
              "\nPlease try again.")
        return None


# Making the text message align at the center by calling the function
def align_center_message(introduction, width=80):
    lines = introduction.split('\n')

    for line in lines:
        line = line.strip()  # Remove leading and trailing spaces from the introduction
        introduction_length = len(line)

        if introduction_length >= width:
            print(line)

        else:
            padding = (width - introduction_length) // 2
            centered_message = " " * padding + line
            print(centered_message)


# function for user before to enter the program
def get_user_input(prompt):
    while True:
        user_input = input(prompt)

        if user_input.lower() in ['yes', 'no']:
            return user_input.lower()

        else:
            print("\nError 404")
            print("Invalid input."
                  "\n<Please enter 'yes' or 'no'>\n")


# function for age
def get_user_age(prompt):
    while True:
        try:
            user_input1 = int(input(prompt))

            if 1 <= user_input1 <= 1000:
                return user_input1

            else:
                print("\nInvalid input."
                      "\n<Please enter your exact age>\n")

        except ValueError:
            print("\nERROR 404")
            print("<Please enter valid numeric age>\n")


# function for height
def get_user_height(prompt):
    while True:
        try:
            user_input2 = float(input(prompt))

            if 0.3048 <= user_input2 <= 10:
                return user_input2

            else:
                print("\nInvalid input."
                      "\n<Please enter your exact height>\n")

        except ValueError:
            print("\nERROR 404")
            print("<Please enter valid numeric height>\n")


# function for weight
def get_user_weight(prompt):
    while True:
        try:
            user_input3 = float(input(prompt))

            if 1 <= user_input3 <= 1000:
                return user_input3

            else:
                print("\nInvalid input."
                      "\n<Please enter your exact weight>\n")

        except ValueError:
            print("\nERROR 404")
            print("<Please enter valid numeric weight>\n")


# function for gender
def get_user_gender(prompt):
    while True:
        user_input4 = input(prompt)

        if user_input4.upper() in ['M', 'F', 'N']:
            return user_input4.upper()

        else:
            print("\nERROR 404")
            print("Invalid input."
                  "\n<Please enter 'M' for male, 'F' for female, 'N' for non-binary>\n")


# function for program
def get_user_program(prompt):
    while True:
        try:
            user_input6 = input(prompt)

            if user_input6 in ['1', '2', '3']:
                return user_input6

            else:
                print("\nInvalid input."
                      "\n<Please enter program [1] [2] [3]>\n")

        except ValueError:
            print("\nERROR 404")
            print("<Please enter valid input>\n")


# function for user feedback ratings
def get_user_options(prompt):
    while True:
        try:
            user_input9 = input(prompt)

            if user_input9 in ['1', '2', '3', '4', '5']:
                return user_input9

            else:
                print("\nInvalid input."
                      "\n<Please enter [1-5]>\n")

        except ValueError:
            print("\nERROR 404")
            print("<Please enter valid input>\n")


def motivational_for_young_warrior():
    quote = ("You are still young and growing!"
             "\nThere are still many open doors for improvement and opportunities.\n"
             "\nHere are some exercise/workout recommendations for you:")
    print(quote)


def motivational_for_old_goat():
    quote = ("Age doesn't matter! Age is just a number"
             "\nKeep grinding that fats and trust the process!\n"
             "\nHere are some exercise/workout recommendations for you:")
    print(quote)


def exercise_for_superhuman():
    exercise1 = ("1. Stretching - Start with gentle stretching exercises to improve flexibility"
                 "\nand prevent muscle stiffness. Include stretches for the major muscle groups,"
                 "\nsuch as legs, arms, neck, and back.\n"
                 "\n2. Body Weight Exercise"
                 "\n- squats"
                 "\n- push ups"
                 "\n- planks"
                 "\n- wall sits\n"
                 "\n3. Jog/walk - it is an excellent low-impact exercise that can be done at your"
                 "\nown pace. It's suitable for people of all ages and fitness levels. You can"
                 "\nstart with a gentle stroll and gradually increase your duration and speed.\n"
                 "\n4. Yoga - it can help with flexibility, balance, and relaxation. There are"
                 "\nbeginner-friendly yoga routines that focus on simple poses and breathing exercises.")
    print(exercise1)


def never_give_up_exercise():
    exercise2 = ("1. Stretching - Start with gentle stretching exercises to improve flexibility"
                 "\nand prevent muscle stiffness. Include stretches for the major muscle groups,"
                 "\nsuch as legs, arms, neck, and back.\n"
                 "\n2. Jog/walk - it is an excellent low-impact exercise that can be done at your"
                 "\nown pace. It's suitable for people of all ages and fitness levels. You can start"
                 "\nwith a gentle stroll and gradually increase your duration and speed.\n"
                 "\n3. Seated Yoga - Seated yoga routines can be done in a chair or on the floor"
                 "\nwith support. These routines emphasize gentle stretches and relaxation.\n"
                 "\n4. Water Aerobics - Water aerobics in a pool provides buoyancy and support"
                 "\nfor your body, reducing the impact on your joints. This is an excellent way"
                 "\nto improve cardiovascular fitness and muscle strength.\n"
                 "\n5. Low-Intensity Resistance Training - Use light weights or resistance bands"
                 "\nto perform low-intensity strength training exercises. Focus on high repetitions"
                 "\nwith low resistance to avoid straining muscles and joints.\n"
                 "\n6. Breathing Exercises - Focus on deep breathing exercises to increase lung"
                 "\ncapacity and reduce stress.\n"
                 "\n7. Recumbent Bike - Using a recumbent stationary bike can provide a comfortable"
                 "\nworkout experience with back support and minimal impact on the joints.")
    print(exercise2)


# Functions for Calorie Tracker
def kg_to_lbs(weight_kg):
    conversion_factor = 2.20462
    weight_pounds = weight_kg * conversion_factor
    return weight_pounds


# Class for Calorie Tracker
class CalorieTracker:
    def __init__(self):
        self.exercises = []
        self.meals = []

    def log_exercise(self, exercise, duration, calories_burned):
        self.exercises.append({'exercise': exercise, 'duration': duration, 'calories_burned': calories_burned})
        print(f"Exercise logged: {exercise} - {duration} minutes, Calories burned: {calories_burned}")

    def log_meal(self, meal, calories_consumed):
        self.meals.append({'meal': meal, 'calories_consumed': calories_consumed})
        print(f"Meal logged: {meal}, Calories consumed: {calories_consumed}")

    def calculate_total_calories(self):
        total_calories_burned = sum(exercise['calories_burned'] for exercise in self.exercises)
        total_calories_consumed = sum(meal['calories_consumed'] for meal in self.meals)
        return total_calories_consumed, total_calories_burned
# End of Database Area ------------------------------------------------------------------------------------------------


# Starting point
# Page Title/Heading
print("L I F E 100 // to infinity and beyond 🚀")

# Subheading: Slogan
print('\"A Journey to a Long Life Experience\"')

# for organize stuff and space 'print()' or '\n'
print()

print("Updated Version: New Features!"
      "\n> Secured Personal Account (with username & password)"
      "\n> New Programs!"
      "\n> Calorie Deficit & Calorie Surplus "
      "\n> Record of Calorie"
      "\n> Record of Exercise"
      "\n> Record of Food intake")
print()

# Greetings
print("|------------------------------------------------------------------------------|"
      "\n| Welcome to our Dearest and Fellow Human Being, that soon to be a Super Human |"
      "\n|------------------------------------------------------------------------------|")
print()

# Introduction text
print("Introduction:")

intro = "\nIn a world that's constantly evolving, with advances in science, technology, " \
        "\nand healthcare, we have an unprecedented opportunity to extend and " \
        "\nenhance the quality of our lives. The aspiration of living " \
        "\nto one hundred years old is no longer a mere dream " \
        "\nbut a realistic goal within reach. It's a journey that's not just " \
        "\nabout adding years to our life but adding life to our years. " \
        "\nOur collective quest to promote longevity is not only a celebration " \
        "\nof aging but a testament to the potential of the human spirit. " \
        "\nJoin us on this inspiring journey as we explore the keys to unlocking a " \
        "\ncentury of vibrant living and discover the secrets to achieving that " \
        "\nthat cherished milestone of a hundred years."
align_center_message(intro)

# Disclaimer text
disclaimer = '\n"Disclaimer: For Educational Purposes Only"\n'
align_center_message(disclaimer)

print("L I F E 100 // to infinity and beyond 🚀"
      "\n\"A Journey to a Long Life Experience\"")

print("\nLogin your account."
      "\n>If you don't have any account yet, please Sign up. "
      "\nThank you!")

# User's input
# the starting point of loop
# calling 'while' to create loop
logged_in_user = None
while True:

    print("\n[1] SIGN UP"
          "\n[2] SIGN IN"
          "\n[3] Exit")

    choice = get_user_program("Select: ")

    if choice == '1':
        new_username = input("Enter a username: ")
        new_password = input("Enter a password: ")
        register_user(new_username, new_password)
        continue
    elif choice == '2':
        log_username = input("Enter your username: ")
        log_password = input("Enter your password: ")
        logged_in_user = login_user(log_username, log_password)
        if logged_in_user is None:
            continue
    elif choice == '3':
        print("Goodbye, Have a great day!")
        break

    print("\n// L I F E 100 🚀 | CONTENTS"
          "\n> Overall Health Check"
          "\n - Personal physical information"
          "\n - Body mass index"
          "\n> Calorie Deficit & Calorie Surplus"
          "\n> Burn that Fats: Calorie Tracker"
          "\n> Superhuman Knowledge"
          "\n - Exercise/workout"
          "\n - Health Tips"
          "\n - Food Diets")
    user_choice = get_user_input("\n> Are you ready to experience this kind of journey?"
                                 "\n[yes] Continue"
                                 "\n[no] Exit"
                                 "\nInput: ")

    # if-elif statement
    if user_choice == 'yes':
        print("\nLET's BEGIN!")
        print('\n> [It does not matter how slowly you go as long as you do not stop]\n')

    elif user_choice == 'no':
        print('\n> [You are never too old to set another goal or to dream a new dream]')
        print("\nBYE!, SEE YOU NEXT TIME!\n")
        break

# Collecting data to users information
    # calling second loop
    while True:
        print("// L I F E 100 🚀 | OVERALL HEALTH CHECK")
        print("// Personal Information")
        name = input("Enter your Name: ")
        user_age = get_user_age("Enter your age: ")
        user_height = get_user_height("Enter your height (in meters): ")
        user_weight = get_user_weight("Enter your weight (in kilograms): ")
        user_gender = get_user_gender("Enter your Gender [M]male | [F]female | [N]non-binary: ")

        if user_gender == 'M':
            print(f"\nHello Sir!, {name}")
            print("Welcome to L I F E 100 // to infinity and beyond 🚀\n")

        elif user_gender == 'F':
            print(f"\nHello Ma'am!, {name}")
            print("Welcome to L I F E 100 // to infinity and beyond 🚀\n")

        elif user_gender == 'N':
            print(f"\nHello Ma'am/Sir!, {name}")
            print("Welcome to L I F E 100 // to infinity and beyond 🚀\n")

        # putting some delay effects at text using time module
        first_prog = ("// L I F E 100\n"
                      "> [First, let's check your BMI]\n")
        for character in first_prog:
            print(character, end='', flush=True)
            time.sleep(0.1)

        # bmi scale list
        bmi_scale = "BODY MASS INDEX SCALE" \
                    "\n-------------------------------------------------" \
                    "\nUnderweight: BMI less than 18.5 " \
                    "\nNormal Weight: BMI between 18.5 and 24.9 " \
                    "\nOverweight: BMI between 25 and 29.9 " \
                    "\nObesity (Class I): BMI between 30 and 34.9 " \
                    "\nObesity (Class II): BMI between 35 and 39.9 " \
                    "\nObesity (Class III): BMI between 40 or higher " \
                    "\n-------------------------------------------------"
        align_center_message(bmi_scale)

        # bmi calculator
        bmi = user_weight / (user_height ** 2)
        if user_gender == 'M':
            print(f"Hello Sir!"
                  f"\n> {name}, {user_age} years of age"
                  f"\nYour height is"
                  f"\n> {user_height} meters"
                  f"\nYour weight is"
                  f"\n> {user_weight} kilograms"
                  f"\nBMI: {format(bmi, '.1f')}")

        elif user_gender == 'F':
            print(f"Hello Ma'am!"
                  f"\n> {name}, {user_age} years of age"
                  f"\nYour height is"
                  f"\n> {user_height} meters"
                  f"\nYour weight is"
                  f"\n> {user_weight} kilograms"
                  f"\nBMI: {format(bmi, '.1f')}")

        elif user_gender == 'N':
            print(f"Hello Ma'am/Sir!"
                  f"\n> {name}, {user_age} years of age"
                  f"\nYour height is"
                  f"\n> {user_height} meters"
                  f"\nYour weight is"
                  f"\n> {user_weight} kilograms"
                  f"\nBMI: {format(bmi, '.1f')}")

        # bmi scale identification
        bmi_scale_result = user_weight / (user_height ** 2)
        if bmi_scale_result < 18.5:
            print('> it means you are "UNDERWEIGHT"')

        elif 18.5 < bmi_scale_result < 25:
            print('> it means you are in a "NORMAL WEIGHT"')

        elif 25 <= bmi_scale_result < 30:
            print('> it means you are "OVERWEIGHT"')

        elif 30 <= bmi_scale_result < 35:
            print('> it means you are "OBESITY (CLASS I)"')

        elif 35 <= bmi_scale_result < 40:
            print('> it means you are "OBESITY (CLASS II)"')

        elif bmi_scale_result >= 40:
            print('> it means you are "OBESITY (CLASS III)"')

        print()

        # third loop for calling another program
        # user's choice to whether continue or end the program
        while True:
            user_choice = get_user_input("Proceed to the program?"
                                         "\n[yes] Continue"
                                         "\n[no] Exit"
                                         "\nInput: ")

            if user_choice == 'yes':
                print("\n> [\"The only person you are destined to become is the person you decide to be.\""
                      "\n- Ralph Waldo Emerson]")

            elif user_choice == 'no':
                print("\n> [You are never too old to set another goal or to dream a new dream]"
                      "\nBYE!, SEE YOU NEXT TIME!")
                break

            while True:
                # move to calorie deficit option
                print("\n// L I F E 100 🚀 | CALORIE DEFICIT & CALORIE SURPLUS")
                user_calorie = get_user_input("\nProceed to Calorie Deficit/Calorie Surplus?"
                                              "\n[yes] Continue"
                                              "\n[no] Next"
                                              "\nInput: ")
                if user_calorie == 'yes':
                    print(f"\n> Your current weight is {format(user_weight, '.1f')}kg")
                    if bmi_scale_result < 18.5:
                        print("Recommendation: Calorie Surplus")
                    elif 18.5 < bmi_scale_result < 25:
                        print("> Your BMI is NORMAL"
                              "\nYou are near to become a SuperHuman")
                    elif 25 <= bmi_scale_result < 30:
                        print("Recommendation: Calorie Deficit")
                else:
                    break

                calorie_choice = get_user_program("\n[1] Calorie Deficit"
                                                  "\n[2] Calorie Surplus"
                                                  "\n[3] Exit"
                                                  "\nInput: ")
                # Calorie Deficit
                if calorie_choice == '1':
                    print("// Calorie Deficit")
                    weight_lbs = kg_to_lbs(user_weight)
                    print(f"Current Weight:{user_weight}kg = {format(weight_lbs, '.1f')}lbs ")
                    maintenance_calorie = weight_lbs * 12
                    calorie_deficit = maintenance_calorie - 500
                    maintenance_calorie_active = weight_lbs * 14
                    calorie_deficit_active = maintenance_calorie_active - 500
                    print("If NOT ACTIVE:"
                          f"\n{format(weight_lbs, '.1f')} x 12 = ", format(maintenance_calorie, '.1f'),
                          "g (Maintenance Calorie)"
                          f"\n{format(maintenance_calorie, '.1f')} - 500 = ", format(calorie_deficit, '.1f'),
                          "g (Calorie Deficit)")
                    print("If ACTIVE:"
                          f"\n{format(weight_lbs, '.1f')} x 14 = ", format(maintenance_calorie_active, '.1f'),
                          "g (Maintenance Calorie)"
                          f"\n{format(maintenance_calorie_active, '.1f')} - 500 = ", format(calorie_deficit_active,
                                                                                            '.1f'),
                          "g (Calorie Deficit)")
                # Calorie Surplus
                elif calorie_choice == '2':
                    print("// Calorie Surplus")
                    weight_lbs = kg_to_lbs(user_weight)
                    print(f"Current Weight:{user_weight}kg = {format(weight_lbs, '.1f')}lbs ")
                    maintenance_calorie = weight_lbs * 12
                    calorie_deficit = maintenance_calorie + 500
                    maintenance_calorie_active = weight_lbs * 14
                    calorie_deficit_active = maintenance_calorie_active + 500
                    print("If NOT ACTIVE:"
                          f"\n{format(weight_lbs, '.1f')} x 12 = ", format(maintenance_calorie, '.1f'),
                          "g (Maintenance Calorie)"
                          f"\n{format(maintenance_calorie, '.1f')} + 500 = ", format(calorie_deficit, '.1f'),
                          "g (Calorie Surplus)")
                    print("If ACTIVE:"
                          f"\n{format(weight_lbs, '.1f')} x 14 = ", format(maintenance_calorie_active, '.1f'),
                          "g (Maintenance Calorie)"
                          f"\n{format(maintenance_calorie_active, '.1f')} + 500 = ", format(calorie_deficit_active,
                                                                                            '.1f'),
                          "g (Calorie Surplus)")
                elif calorie_choice == '3':
                    continue

            tracker = CalorieTracker()

            while True:
                print("\n// L I F E 100 🚀 | BURN THAT FATS: CALORIE TRACKER")
                exercise_tracker = get_user_input("Proceed to Calorie Tracker"
                                                  "\n[yes] Continue"
                                                  "\n[no] Next"
                                                  "\nInput: ")
                if exercise_tracker == 'yes':
                    print("\n// Calorie Tracker")
                    print("[1] Log Exercise"
                          "\n[2] Log Meal"
                          "\n[3] View Total Calories"
                          "\n[4] Exit")

                    choice = input("Select: ")

                    if choice == '1':
                        exercise = input("Enter exercise: ")
                        duration = float(input("Enter duration (minutes): "))
                        calories_burned = float(input("Enter calories burned: "))
                        tracker.log_exercise(exercise, duration, calories_burned)
                    elif choice == '2':
                        meal = input("Enter meal: ")
                        calories_consumed = float(input("Enter calories consumed: "))
                        tracker.log_meal(meal, calories_consumed)
                    elif choice == '3':
                        total_calories_consumed, total_calories_burned = tracker.calculate_total_calories()
                        print(f"\nTotal Calories Consumed: {total_calories_consumed} kcal")
                        print(f"Total Calories Burned: {total_calories_burned} kcal")
                        print(f"Net Calories: {total_calories_consumed - total_calories_burned} kcal")
                    elif choice == '4':
                        print("Goodbye! Exiting the calorie tracker.")
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
                    continue
                else:
                    break

            # loop for program choices
            while True:
                print("\n// L I F E 100: SuperHuman Knowledge"
                      "\n[1] Exercise/Workout"
                      "\n[2] Health Tips"
                      "\n[3] Food Diets")

                # Program 1: Exercise/Workout
                user_prog = get_user_program("\nSelect a program [1-3]: ")
                if user_prog == '1':

                    print("\n// L I F E 100:"
                          "\nYou selected program: [1] Exercise/Workout 101\n")

                    # for ages 18 below
                    if user_age < 18 and bmi_scale_result < 18.5:
                        print(f"Personal Information"
                              f"\nName: {name}"
                              f"\nAge: {user_age} years old"
                              f"\nBMI: {format(bmi, '.1f')}"
                              f"\nHealth Status: Underweight")
                        motivational_for_young_warrior()
                        exercise_for_superhuman()
                        print()
                        print("(For more health improvement go to [2] Health Tips | [3] Food Diets)")

                    elif user_age < 18 and 18.5 < bmi_scale_result < 25:
                        print(f"Personal Information"
                              f"\nName: {name}"
                              f"\nAge: {user_age} years old"
                              f"\nBMI: {format(bmi, '.1f')}"
                              f"\nHealth Status: Normal Weight")
                        motivational_for_young_warrior()
                        exercise_for_superhuman()
                        print()
                        print("(For more health improvement go to [2] Health Tips | [3] Food Diets)")

                    elif user_age < 18 and 25 <= bmi_scale_result < 30:
                        print(f"Personal Information"
                              f"\nName: {name}"
                              f"\nAge: {user_age} years old"
                              f"\nBMI: {format(bmi, '.1f')}"
                              f"\nHealth Status: Overweight")
                        motivational_for_young_warrior()
                        exercise_for_superhuman()
                        print()
                        print("(For more health improvement go to [2] Health Tips | [3] Food Diets)")

                    elif user_age < 18 and 30 <= bmi_scale_result < 35:
                        print(f"Personal Information"
                              f"\nName: {name}"
                              f"\nAge: {user_age} years old"
                              f"\nBMI: {format(bmi, '.1f')}"
                              f"\nHealth Status: Obesity (Class I)")
                        motivational_for_young_warrior()
                        never_give_up_exercise()
                        print()
                        print("(For more health improvement go to [2] Health Tips | [3] Food Diets)")

                    elif user_age < 18 and 35 <= bmi_scale_result < 40:
                        print(f"Personal Information"
                              f"\nName: {name}"
                              f"\nAge: {user_age} years old"
                              f"\nBMI: {format(bmi, '.1f')}"
                              f"\nHealth Status: Obesity (Class II)")
                        motivational_for_young_warrior()
                        never_give_up_exercise()
                        print()
                        print("(For more health improvement go to [2] Health Tips | [3] Food Diets)")

                    elif user_age < 18 and bmi_scale_result >= 40:
                        print(f"Personal Information"
                              f"\nName: {name}"
                              f"\nAge: {user_age} years old"
                              f"\nBMI: {format(bmi, '.1f')}"
                              f"\nHealth Status: Obesity (Class III)")
                        motivational_for_young_warrior()
                        never_give_up_exercise()
                        print()
                        print("(For more health improvement go to [2] Health Tips | [3] Food Diets)")

                    # for ages 18 above
                    elif user_age > 18 and bmi_scale_result < 18.5:
                        print(f"Personal Information"
                              f"\nName: {name}"
                              f"\nAge: {user_age} years old"
                              f"\nBMI: {format(bmi, '.1f')}"
                              f"\nHealth Status: Underweight")
                        motivational_for_old_goat()
                        exercise_for_superhuman()
                        print()
                        print("(For more health improvement go to [2] Health Tips | [3] Food Diets)")

                    elif user_age > 18 and 18.5 < bmi_scale_result < 25:
                        print(f"Personal Information"
                              f"\nName: {name}"
                              f"\nAge: {user_age} years old"
                              f"\nBMI: {format(bmi, '.1f')}"
                              f"\nHealth Status: Normal Weight")
                        motivational_for_old_goat()
                        exercise_for_superhuman()
                        print()
                        print("(For more health improvement go to [2] Health Tips | [3] Food Diets)")

                    elif user_age > 18 and 25 <= bmi_scale_result < 30:
                        print(f"Personal Information"
                              f"\nName: {name}"
                              f"\nAge: {user_age} years old"
                              f"\nBMI: {format(bmi, '.1f')}"
                              f"\nHealth Status: Overweight")
                        motivational_for_old_goat()
                        exercise_for_superhuman()
                        print()
                        print("(For more health improvement go to [2] Health Tips | [3] Food Diets)")

                    elif user_age > 18 and 30 <= bmi_scale_result < 35:
                        print(f"Personal Information"
                              f"\nName: {name}"
                              f"\nAge: {user_age} years old"
                              f"\nBMI: {format(bmi, '.1f')}"
                              f"\nHealth Status: Obesity (Class I)")
                        motivational_for_old_goat()
                        never_give_up_exercise()
                        print()
                        print("(For more health improvement go to [2] Health Tips | [3] Food Diets)")

                    elif user_age > 18 and 35 <= bmi_scale_result < 40:
                        print(f"Personal Information"
                              f"\nName: {name}"
                              f"\nAge: {user_age} years old"
                              f"\nBMI: {format(bmi, '.1f')}"
                              f"\nHealth Status: Obesity (Class II)")
                        motivational_for_old_goat()
                        never_give_up_exercise()
                        print()
                        print("(For more health improvement go to [2] Health Tips | [3] Food Diets)")

                    elif user_age > 18 and bmi_scale_result >= 40:
                        print(f"Personal Information"
                              f"\nName: {name}"
                              f"\nAge: {user_age} years old"
                              f"\nBMI: {format(bmi, '.1f')}"
                              f"\nHealth Status: Obesity (Class III)")
                        motivational_for_old_goat()
                        never_give_up_exercise()
                        print()
                        print("(For more health improvement go to [2] Health Tips | [3] Food Diets)")

                    print()

                # Program 2: Health Tips
                elif user_prog == '2':
                    print("// L I F E 100:"
                          "\nYou selected program: [2] Health Tips 101]")
                    health_tips = "\nEmbrace the gift of life with open arms and a commitment to your well-being." \
                                  "\nA long and vibrant life is not solely a matter of genetics; it's shaped by" \
                                  "\nthe choices you make every day\n "
                    align_center_message(health_tips)

                    print()

                    print("Here are some health tips to help you lead a long and healthy life:")
                    print("1. Maintain a Balanced Diet"
                          "\n- Eat a variety of fruits, vegetables, whole grains, lean protein, and healthy fats."
                          "\n- Limit processed foods, sugar, and excessive salt intake."
                          "\n- Stay hydrated by drinking plenty of water.\n ")
                    print("2. Portion Control"
                          "\n- Be mindful of portion sizes to avoid overeating, which can lead to weight gain and"
                          "\nassociated health issues.\n")
                    print("3. Regular Physical Activity"
                          "\n- Incorporate regular exercise into your routine, including cardiovascular,"
                          "\nstrength training, and flexibility exercises."
                          "\n- Aim for at least 150 minutes of moderate-intensity aerobic activity per week.\n")
                    print("4. Stress Management"
                          "\n- Practice stress-reduction techniques such as meditation, deep breathing,"
                          "\nor yoga to lower stress levels and improve mental well-being.\n")
                    print("5. Adequate Sleep"
                          "\n- Get at least 7-9 hours of quality sleep per night to allow your body to"
                          "\nrest and recover.\n")
                    print("6. Stay Socially Active"
                          "\n- Maintain social connections with friends and family to reduce feelings of"
                          "\nisolation and loneliness.\n")
                    print("7. Regular Check-Ups"
                          "\n- Visit your healthcare provider for regular check-ups and screenings to catch"
                          "\npotential health issues early.\n")
                    print("8. Mental Stimulation"
                          "\n- Keep your mind active with activities such as puzzles, reading, or learning"
                          "\nnew skills to maintain cognitive health.\n")
                    print("9. Avoid Smoking and Excessive Alcohol"
                          "\n- Quit smoking or avoid it altogether."
                          "\n- Limit alcohol consumption to moderate levels, if at all.\n")
                    print("10. Sun Protection"
                          "\n- Protect your skin from the sun to prevent skin damage and skin cancer.\n")
                    print("11. Stay Hydrated"
                          "\n- Drink an adequate amount of water to support overall health and well-being.\n")
                    print("12. Have a Purpose"
                          "\n- Engage in activities that give you a sense of purpose and fulfillment.")

                    print()

                # Program 3: Food Diets
                elif user_prog == '3':
                    print("// L I F E 100:"
                          "\nYou selected program: [3] Food Diets 101")
                    food_diet = "\nA balanced and nutritious diet is a crucial factor in promoting a longer" \
                                "\nand healthier life. While there's no single superfood that guarantees a" \
                                "\nlonger life, certain dietary patterns and food choices have been associated" \
                                "\nwith longevity and overall well-being"
                    align_center_message(food_diet)

                    print()

                    print("Here are some dietary guidelines to consider:")
                    print("1. Mediterranean Diet"
                          "\nThe Mediterranean diet is often cited for its association with longevity."
                          "\nThis diet is rich in antioxidants, fiber, and heart-healthy fats."
                          "\nIt emphasizes:"
                          "\n- Fruits and vegetables"
                          "\n- Whole grains"
                          "\n- Lean protein, including fish and legumes"
                          "\n- Healthy fats, such as olive oil and nuts"
                          "\n- Reduced red meat consumption"
                          "\n- Moderate wine consumption (if appropriate and in moderation)\n")
                    print("2. Plant-Based Diet"
                          "\nPlant-based diets, such as vegetarian or vegan diets, are linked to longevity."
                          "\nThese diets tend to be lower in saturated fats and cholesterol."
                          "\nThey are high in:"
                          "\n- Fruits and vegetables"
                          "\n- Whole grains"
                          "\n- Legumes"
                          "\n- Nuts and seeds\n")
                    print("3. High-Fiber Foods"
                          "\n- Foods high in fiber, such as whole grains, oats, fruits, and vegetables,"
                          "\ncan help maintain digestive health and reduce the risk of chronic diseases.\n")
                    print("4. Fatty Fish"
                          "\n- Fatty fish like salmon, mackerel, and sardines are rich in omega-3 fatty acids,"
                          "\nwhich support heart health and reduce inflammation.\n")
                    print("5. Antioxidant-Rich Foods"
                          "\n- Foods rich in antioxidants, including berries, leafy greens, and nuts,"
                          "\ncan help protect against cellular damage and lower the risk of chronic diseases.\n")
                    print("6. Probiotic Foods"
                          "\n- Fermented foods like yogurt, kefir, and sauerkraut can promote gut health"
                          "\nand may have positive effects on the immune system.\n")
                    print("7. Low Sugar Intake"
                          "\n- Reducing sugar intake and avoiding sugary beverages can help prevent obesity and"
                          "\nchronic diseases.\n")
                    print("8. Limit Processed Foods"
                          "\n- Minimize the consumption of highly processed and packaged foods, which often"
                          "\ncontain unhealthy additives and excessive salt.\n")

                else:
                    print("Invalid input.")
                    break

                # recalling the program by using loop
                new_program = get_user_input("> Select another program?"
                                             "\n[yes | no]"
                                             "\nInput: ")
                if new_program == 'no':
                    break

            # last loop: user's feedback program
            while True:
                user_feedback = get_user_input("\n> Are you happy with the result?"
                                               "\n[yes | no ]"
                                               "\nInput: ")

                if user_feedback == 'yes':
                    print('\n"Success is not the key to happiness. Happiness is the key to success.'
                          '\nIf you love what you are doing, you will be successful."')
                    print("\n> [Thank you for trusting L I F E 100]")
                    print("Hoping to see you again!")

                elif user_feedback == 'no':
                    print('\n"Failure is only the opportunity to begin again, only this time more wisely"')
                    print("\nFor more information"
                          "\nYou can reach out to our email: Life100@gmail.com"
                          "\nThanks have a great day ahead\n")

                # user's rate to the program
                print("---------------------------------------------")
                print("[5] Outstanding"
                      "\n[4] Very helpful"
                      "\n[3] Helpful"
                      "\n[2] Poor"
                      "\n[1] Very poor")

                user_rate = get_user_options("> Send us your ratings [1-5]: ")

                if user_rate in ['1', '2', '3', '4', '5']:
                    print("\nThank you so much!"
                          "\nHave a great day ahead!")

                    break
                break
            break
        break

    # repeat all program by another user
    print("---------------------------------------------")
    new_user = get_user_input("Do you want to try again with another user?"
                              "\n[yes | no]"
                              "\nInput:")

    if new_user == 'yes':
        print("---------------------------------------------")
    else:
        break
