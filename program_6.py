# write a program that uses built-in functions to find the largest and smallest among three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)
print("The largest number is:", largest)
print("The smallest number is:", smallest)