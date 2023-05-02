num1 = int(input("Enter The Number : "))
str = str(input("Enter [+,-,*,/] : "))
num2 = int(input("Enter The Number : "))

if str == "+":
    output = num1 + num2
elif str == "-":
    output = num1 - num2
elif str == "*":
    output = num1 * num2
elif str == "/":
    output = num1 / num2

print(f"Answer is :{output}")
