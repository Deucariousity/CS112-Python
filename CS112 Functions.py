def diff_num(num1, num2, num3):
    result = num1 + num2 + num3
    return result


def same_num(num1, num2, num3):
    result = num1 * num2 * num3
    return result


def same_two_num1(num1, num2, num3):
    result = num1 * num2 + num3
    return result


def same_two_num2(num1, num2, num3):
    result = num1 * num3 + num2
    return result


def same_two_num3(num1, num2, num3):
    result = num2 * num3 + num1
    return result


def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input in ['yes', 'no']:
            return user_input

        else:
            print("Invalid input. Please enter 'yes' or 'no'")


print("CS112: Introduction to Programming 1"
      "\nArtjohn Clark E. Dinorog | CS 1E"
      "\nLABORATORY ACTIVITY: FUNCTIONS")

print("\nGuide Rules:"
      "\n[1] If all numbers is the same it will be multiplied."
      "\n[2] If all numbers are different it will be added."
      "\n[3] If two numbers are the same and the other one is different,"
      "\nthe two same numbers will be multiplied and the other one is added.")

while True:
    print("\nEnter a \"NUMBER\"")
    num1 = eval(input("Enter first number: "))
    num2 = eval(input("Enter second number: "))
    num3 = eval(input("Enter third number: "))
    num = num1, num2, num3
    if num1 != num2 != num3:
        print("Result is", diff_num(num1, num2, num3))

    elif num1 == num2 == num3:
        print("Result is", same_num(num1, num2, num3))

    elif num1 == num2 != num3:
        print("Result is", same_two_num1(num1, num2, num3))

    elif num1 == num2 != num3:
        print("Result is", same_two_num2(num1, num2, num3))

    elif num2 == num3 != num1:
        print("Result is", same_two_num3(num1, num2, num3))

    another = get_user_input("\nTry Again? (yes, no): ")
    if another != 'yes':
        break
