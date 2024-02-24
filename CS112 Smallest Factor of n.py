# Smallest Factor of n

# Function for getting an integer
def get_user_integer(prompt):
    while True:
        try:
            user_integer = int(input(prompt))
            if user_integer >= 2:
                return user_integer

            else:
                print("[Invalid input. Enter a number greater than 2]\n")

        except ValueError:
            print("[Error 404. Please input an integer]\n")


# Function for yes or no
def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input in ['yes', 'no']:
            return user_input

        else:
            print("[Invalid input. Please enter 'yes' or 'no']\n")


# Loop
while True:
    print("SMALLEST FACTOR OF N")
    print()

    # user input
    n = get_user_integer("Enter an integer >=2 (greater than or equal to two): ")
    if n > 2:
        for i in range(2, int(n**0.5) + 1):  # formula for getting the smallest factor
            if n % i == 0:
                print(f"The smallest factor other than 1 for {n} is {i}.")
                
    else:
        print("[Invalid input. Enter a number greater than 2]\n")

    # recalling loop
    print()
    another = get_user_input("Try Again? (yes or no): ")
    if another != 'yes':
        break
