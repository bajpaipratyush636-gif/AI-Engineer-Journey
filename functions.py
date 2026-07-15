# def greet():
#     print("Hello, World!")

# greet()
# def welcome():
#     print("welcome to the ai journey")
# welcome()
# def greet(name):
#     print("Hello, ", name)
# greet("John")
# greet("Aadi")
# def college(name):
#     print("welcome to LPU, ", name)
# college("Aadi")
# college("John")

# def add(a, b):
#     return a + b
# result = add(5, 3)
# print(result)

# def sqaure(n):
#     return n*n
# result = sqaure(5)
# print(result)

# def student(name, age):
#     print("name: ", name)
#     print("age ", age)
# student("Pratyush", 19)

# def marks(math , english):
#     return math + english
# result = marks(90, 80)
# print(result)

# def add(a,b):
#     return a + b
# def subtract(a,b):
#     return a - b
# def multiply(a,b):
#     return a * b
# def divide(a,b):
#     return a / b
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("Enter operation (+, -, *, /): ")

# if op == "+":
#     print("Result: ", add(a, b))
# elif op == "-":
#     print("Result: ", subtract(a, b))
# elif op == "*":
#     print("Result: ", multiply(a, b))
# elif op == "/":
#     print("Result: ", divide(a, b))
# else:
#     print("Invalid operation")

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
num = int(input("Enter a number: "))
if isEven(num):
    print(num, "is even")
else:
    print(num, "is not even")