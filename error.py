try:
    num1 = input("Input a number: ")
    num2 = input("Input another number: ")
    addition = int(num1) + int(num2)
    print(addition)
except ValueError:
    print("Inputs can only be numbers")