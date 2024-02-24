print("CS112: Computer Programming 1"
      "\nACTIVITY: Reverse Text")
print("Created by: Artjohn Clark E. Dinorog")


def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input in ['yes', 'no']:
            return user_input

        else:
            print("[Invalid input. Please enter 'yes' or 'no']")


def get_user_reverse_text():
    while True:
        user_input = input("\nEnter a text: ")

        if user_input.isdigit():
            print("Error Reported! Enter text only.")
        else:
            reversed_text = user_input[::-1]
            print("Reversed Text:", reversed_text)

        another = get_user_input("\nTry again? (yes/no): ")
        if another != 'yes':
            break


get_user_reverse_text()

