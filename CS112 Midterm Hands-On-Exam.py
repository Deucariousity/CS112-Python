import random


def get_student_answer(prompt):
    while True:
        try:
            student_answer = float(input(prompt))
            return student_answer
        except ValueError:
            print("Error 404"
                  "\n<Please enter a number>")


def get_new_answer(prompt):
    while True:
        new_answer = input(prompt)
        if new_answer in ['yes', 'no']:
            return new_answer
        else:
            print("Invalid Input."
                  "\n<Please enter 'yes' or 'no'>")


while True:
    print("WELCOME GRADE SCHOOL STUDENT!"
          "\nMATH PRACTICE PROGRAM: CALCULATE BASIC OPERATIONS")
    print("\nAnswer the following questions:")

    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    addition = eval(f"{num1} + {num2}")
    print(f"Question 1: Addition"
          f"\n{num1} + {num2}?")
    first_question = get_student_answer("Answer: ")

    if first_question == addition:
        print("Your answer is CORRECT")
    else:
        print("Your answer is WRONG")

    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    subtraction = eval(f"{num1} - {num2}")
    print(f"\nQuestion 2: Subtraction"
          f"\n{num1} - {num2}?")
    second_question = get_student_answer("Answer: ")

    if second_question == subtraction:
        print("Your answer is CORRECT")
    else:
        print("Your answer is WRONG")

    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    multiplication = eval(f"{num1} * {num2}")
    print(f"\nQuestion 3: Multiplication"
          f"\n{num1} * {num2}?")
    third_question = get_student_answer("Answer: ")

    if third_question == multiplication:
        print("Your answer is CORRECT")
    else:
        print("Your answer is WRONG")

    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    division = round(num1 / num2, 2)
    print(f"\nQuestion 4: Division"
          f"\n{num1} / {num2}?")
    fourth_question = get_student_answer("Answer: ")

    if fourth_question == division:
        print("Your answer is CORRECT")
    else:
        print("Your answer is WRONG")

    another_student = get_new_answer("\nDo you want to answer again [yes | no]: ")
    if another_student != 'yes':
        break