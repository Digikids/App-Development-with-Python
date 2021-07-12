try:
    num1 = input("Input a number: ")
    num2 = input("Input another number: ")
    addition = int(num1) + int(num2)
    print(addition)
except ValueError:
    print("Inputs can only be numbers")

def calculation(num1, num2):
    p = num1 * num2
    d = num1 / num2
    print(f"Their product is {p} and their division is {d}")

calculation(100, 5)

def ShowStudent(StudentName, StudentAge):
    print(f"Their name is {StudentName} and they are {StudentAge} years old")

ShowStudent("Catherine", 90)

i = 50
my_list = []
while i <= 200:
    my_list.append(i)
    i += 1

# for i in range(0,100):
#     if i % 4 == 0:
#         print(i)

for i in range(1, len(my_list), 2):
    print(my_list[i])




