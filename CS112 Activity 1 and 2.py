print("CS112: Activity 1")
print("Complete Name: Artjohn Clark E. Dinorog")
print("Course: Bachelor of Science in Computer Science")
print("Section: CS1E")
print("Age: 21 years old")
print("Birthday: July 23, 2002")
print("Address: 224 Blk. 15 Sto. Niño Lapasan Cagayan de Oro City")

# Create a simple python program that asks the user to enter student name, id#, course and section ,
# and 4 quarter grades.
# Get the average of 4 quarter grades using math expression.

print("CS112: Activity 2")

Name = (input("Name: "))
Id = (input("ID number: "))
Section = (input("Section: "))
quarter1 = eval(input("1st Quarter Grade: "))
quarter2 = eval(input("2nd Quarter Grade: "))
quarter3 = eval(input("3rd Quarter Grade: "))
quarter4 = eval(input("4th Quarter Grade: "))
average = (quarter1 + quarter2 + quarter3 + quarter4) / 4
print("Name: ", Name)
print("ID number: ", Id)
print("Section: ", Section)
print("1st Quarter Grade: ", quarter1)
print("2nd Quarter Grade: ", quarter2)
print("3rd Quarter Grade: ", quarter3)
print("4th Quarter Grade: ", quarter4)
print("Average Grade: ", average)