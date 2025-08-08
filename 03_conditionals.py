day_of_week = input ("today is").lower() # convert case to lower

print (day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
    print ("i will learn LIVE DevOps")
else:
    print("i will practice DevOps")

# input sum of two numbers
num1 = int(input("enter first number:"))
num2 = int (input ("enter second number:"))
choice = input ("Enter the oprations: (options +,-,*,/,%)")
if choice == "+":
    sum_of_number = num1 + num2
    print("addition of two number",sum_of_number)
elif choice == "-":
    sub_of_number = num1 - num2
    print("subtractions of two number",sub_of_number)
elif choice == "*":
    prod_of_number = num1 * num2
    print("multiplications of two number",prod_of_number)
elif choice == "/":
    div_of_number = num1 / num2
    print("divisions of two number",div_of_number)
elif choice == "%":
    remainder_of_number = num1 % num2
    print("remainder of two number",remainder_of_number)
else:
   print ("invalid choice")
