# python program to find out Chinese Zodiac sign for a given year

# creating a loop
while True:

    # starting a program by collecting the user's information
    print("Discover your Chinese Zodiac sign")
    user_name = input("What is your name? ")
    user_age = input("How old are you? ")

    print("Let's start!")

    # providing choices whether to continue or not
    user_input = input("To unravel the truth...\nMay I know your birth of date?(yes/no): ")
    if user_input == 'no':
        print("Bye, see you next time!")
        break
    elif user_input == 'yes':
        print("proceed...")
    else:
        print("ERROR 404")
        break

    # user birthdate input
    month = input("Month: ")
    day = input("Day: ")
    birth_year = int(input("Year: "))

    # formula to calculate the Chinese Zodiac sign
    zodiac_signs = (birth_year - 1000) % 12 + 1

    # using a Multi-Way if-elif-else statement to construct program
    # displays result
    if zodiac_signs == 1:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the RAT"')

    elif zodiac_signs == 2:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the OX"')

    elif zodiac_signs == 3:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the TIGER"')

    elif zodiac_signs == 4:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the RABBIT"')

    elif zodiac_signs == 5:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the DRAGON"')

    elif zodiac_signs == 6:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the SNAKE"')

    elif zodiac_signs == 7:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the HORSE"')

    elif zodiac_signs == 8:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the SHEEP"')

    elif zodiac_signs == 9:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the MONKEY"')

    elif zodiac_signs == 10:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the ROOSTER"')

    elif zodiac_signs == 11:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the DOG"')

    elif zodiac_signs == 12:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the PIG"')

    # if user put invalid input
    else:
        print('ERROR 404')

    print()

    # option to try again, if no = end of loop
    another = input("Do you want to try again?(yes/no): ")
    if another != 'yes':
        break

# other way ---------------------------------------------------------------------------------------------------
# program that will find your Chinese Zodiac Sign for a given year
# program that also identify your age using birthdate input
import datetime

while True:
    print("Discover your Chinese Zodiac Sign")
    name = input("What is your name? ")
    print("Let's start!")
    user_input = input("To unravel the truth...\nMay I know your birth of date?(yes/no): ")
    if user_input != 'yes':
        print("Bye, see you next time!")
        break

    month = int(input("Enter the month of birth (1-12): "))
    day = int(input("Enter the day of birth (1-31): "))

    def find_chinese_zodiac(year):
        zodiac_signs = ["RAT", "OX", "TIGER", "RABBIT", "DRAGON", "SNAKE", "HORSE", "SHEEP",
                        "MONKEY", "ROOSTER", "DOG", "PIG"]
        start_year = 1000

        year_index = (year - start_year) % 12
        return zodiac_signs[year_index]

    try:
        year = int(input("Enter the year of birth (e.g., 1969): "))
        if year < 1000:
            print("ERROR 404")
        else:
            zodiac = find_chinese_zodiac(year)
            print(f"Your Chinese Zodiac Sign for the year {year} "
                  f'is "Year of the {zodiac}."')
    except ValueError:
        print("Please enter a valid year number")

    # Get the current date
    current_date = datetime.date.today()

    # Create a date object for the birthdate
    birthdate = datetime.date(year, month, day)

    # Calculate the age
    age = current_date.year - birthdate.year - (
            (current_date.month, current_date.day) < (birthdate.month, birthdate.day))

    # Display the age
    print(f"You are {age} years old.")

    print()

    another = input("Do you want to try again?(yes/no): ")
    if another != 'yes':
        break
