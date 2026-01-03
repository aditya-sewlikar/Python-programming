# #1 Functions
#     #Function is a block of code that performs a specific task.
# def greet(): # Defining a function named 'greet'.
#     print("Hello!") # This line prints a greeting message.
# greet()  # Calling the function to execute its code.

# #2 Calling a Function
# def say_hello():
#     print("Hello, World!")
# say_hello()  # This will output: Hello, World!
# #Example #Addition Function
# def addition():
#     print(2001+2002)
# addition()  # This will output: 4003

# #3 Arguments: values you pass into a fun so it can use them inside
# def greet(name):  # 'name' is a variable
#     print("Hello, ",name)
# greet("Alice")  # Passing 'Alice' as an value of variable 'name'   

# #4 Return Values
# def add(a,b):
#     return a + b  # Returns the sum of a and b
# print(add(5, 3))  # This will output: 8
# def sub(a,b):
#     return a - b
# print(sub(10, 4))  # This will output: 6
# def mul(a,b):
#     return a * b
# print(mul(6, 7))  # This will output: 42
# def div(a,b):
#     return a / b
# print(div(20, 4))  # This will output: 5.0

# #5 Scope 
# x=10  # Global variable
# def show():
#     y=5  # Local variable
#     print("y=",y)
# print("x=",x)  # Accessing global variable
# show()  # Calling the function to access local variable

# #6 Lambda Functions
# Square = lambda x: x * x  # Lambda function to calculate square
# print(Square(6))  # This will output: 36

# Square2 = lambda x: x * x  # Lambda function to calculate product
# print(square(2.5))  # This will output: 6.25
# add = lambda x, y: x + y  # Lambda function to add two numbers
# print(add(10, 15))  # This will output: 25

# #7 recrusion
# def factorial(n):
#     if n == 0 or n == 1:  # Base case
#         return 1
#     else:
#         return n * factorial(n - 1)  # Recursive case
# print(factorial(5))  # This will output: 120

# #8 Docstrings
# name="Ram"
# print(name.upper())
# print(name.lower())

# #9 Lists
# fruits=["apple","banana","cherry"]
# fruits.append("orange")  # Adding an item to the list
# fruits.remove("banana")  # Removing an item from the list
# print(fruits)  # This will output: ['apple', 'cherry', 'orange

# #10 Tuples
# point(3,4)
# print(point[0])  # Accessing the first element
# print(point[1])  # Accessing the second element

# #15 Set Methods
# a={1,2,3}
# b={3,4,5}
# print(a.union(b))  # Union of sets a and b
# print(a.intersection(b))

#slicing method
# a= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(a[2:5])
# print(a[::-1]) #reverseing the set
# print(a[2::-1]) #staring from index 2 prints [3,2,1]
# print(a[12:1:-3]) #negative slicing

# #16 Dictionary Methods
# student = {"name":"Ram","age":23}
# print(student.get("age"))

# #17 List Comprehension
# #In columns
# squares =[x*x for x in range(5)]
# print(squares)
# #In rows
# x=4
# squares = x * x
# for square in range(1, 5):
#     print(square * square)
# print("Last square:", squares)

# #18 Dictionary Comprehension
# square_dict={x:x*x for x in range(1,5)}
# print(square)

# #19 Set Comprehension
# square_set={x*x for x in range(5)}
# print(square_set)
                                                                    #QUESTION !!!!
# square_set={x*x for x in range(0,9)}
# print(sorted (square_set))