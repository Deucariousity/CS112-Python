print("CS112 - Intro to Prog 1"
      "\nActivity 3: MinSec Converter & SalesTax Activity"
      "\nBy: Artjohn Clark E. Dinorog"
      "\nSection: CS 1E")

while True:

    print("\nMinutes and Seconds Converter")
    print("Enter an integer for Seconds")
    integer_seconds = eval(input("Input: "))
    minutes = integer_seconds // 60
    seconds = integer_seconds % 60
    print("OUTPUT:", integer_seconds, "seconds is", minutes, "minutes and", seconds, "seconds.")

    another = input("Do you want to convert again?(yes/no): ")
    if another != 'yes':
        break

while True:

    print("\nWelcome!, Dear Customer")
    print("Our Product Sales is 6% discount!")

    name = input("Please Enter your name: ")
    print("Hello!", name)

    purchase_amount = float(input("Enter Purchase Amount: "))
    tax = 0.06
    sale_tax = purchase_amount * tax
    discounted_price = purchase_amount - sale_tax

    print("Your Sales Tax is", round(sale_tax, 2))
    print("Then your Discounted Price is", discounted_price)
    print("Thank you!")

    another = input("\nProceed to next customer?(yes/no): ")
    if another != 'yes':
        break
