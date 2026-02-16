
#if-else statements are used to make decisions in Python. They allow you to execute different blocks of code based on certain conditions. 
# The basic syntax of an if-else statement is as follows:   


marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
