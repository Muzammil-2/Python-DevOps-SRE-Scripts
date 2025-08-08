# Multiple if elif else statments

# score = int(input("Please Enter yours marks:"))
# if score > 90:
#     print("grade A+")
# elif score > 80 :
#     print("grade A")
# elif score > 70 :
#     print("grade B")
# else:
#     print ("grade c")


number = int(input("Please Enter number:"))

if number > 0:
    if number % 2 == 0:
        print("This is Even number")
    else:
        print("This is Odd number")
else:
    if number == 0:
        print("number is possitive")
    else:
        print("number is negative")