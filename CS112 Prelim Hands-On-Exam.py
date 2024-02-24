print("CS112 - Prelim: Number System Conversion"
      "\nBy: Artjohn Clark E. Dinorog & Ryan Hermoso"
      "\nBSCS - 1E")

# Creating a loop program
while True:

    print("\nNumber System Conversion")
    # Ask user to input a value
    number = eval(input("Enter a number: "))

    print()

    # Given options to user
    print("OPTIONS:")
    print("[1] Decimal Number to Binary Number")
    print("[2] Decimal Number to Octal Number")
    print("[3] Decimal Number to Hexadecimal Number")

    print()

    # User's option
    option = eval(input(f"How do you want to convert {number}? Enter from [1-3]: "))

    # Display result of a given option
    if option == 1:
        print(f"Decimal {number} Converted to Binary Number is", format(number, 'b'))
    elif option == 2:
        print(f"Decimal {number} Converted to Octal Number is", format(number, 'o'))
    elif option == 3:
        print(f"Decimal {number} Converted to Hexadecimal Number is ", format(number, 'x'))
    else:
        print('"Invalid input. Please try again."')

    print()

    # option to end or not the loop program
    another = input("Do you want to try again?(yes/no): ")
    if another != 'yes':
        break
