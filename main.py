num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose operation (1/2/3/4): ")

if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid choice")


#python Basics 50

#Q1
print("Hello, World!")

# Q2
print("John")
print(25)

# Q3
print("Bangalore")

# Q4
a, b = 5, 10
print(a + b)

# Q5
age = 25
print(f"My age is {age}")

# Q6
x = 10.5
print(type(x))

# Q7
flag = True
print(type(flag))

# Q8
a = b = 10
print(a)
print(b)

# Q9
age = 25
print(f"I am {age} years old")

# Q10
print(10, 20, 30)

# Q11
print(10)
print(10.5)
print("Python")
print(True)

# Q12
age = 25
print("Age is " + str(age))

# Q13
s = "100"
print(int(s))

# Q14
print(10 + 5.5)

# Q15
print(5 / 2)

# Q16
print(round(3.14159, 2))

# Q17
status = True
print(f"Active status: {status}")

# Q18
print(int("100"))

# Q19
print(float(10))

# Q20
print(int(10.7))

# Q21
name = input()
print(f"Hello {name}")

# Q22
age = input()
print(age)

# Q23
age = int(input())
print(age + 5)

# Q24
a = int(input())
b = int(input())
print(a + b)

# Q25
a = int(input())
b = int(input())
print(a * b)

# Q26
x = float(input())
print(int(x))

# Q27
n = int(input())
print(n * n)

# Q28
birth_year = int(input())
print(2025 - birth_year)

# Q29
s = input()
print(len(s))

# Q30
print("Integer")

# Q31
print("Name: John, Age: 25")

# Q32
price = 500
print(f"Total: {price}")

# Q33
print(f"{3.14159:.2f}")

# Q34
print(f"Sum is {10 + 5}")

# Q35
name, age = "John", 25
print(f"{name} is {age} years old")

# Q36
print("Item: Pen")
print("Price: 10")

# Q37
print(f"I have {2} apples")

# Q38
print("Name: John Age: 25")

# Q39
print("Temperature: 30°C")

# Q40
print("Logged in: True")

# Q41
first = input()
last = input()
print(first, last)

# Q42
a = int(input())
b = int(input())
print(f"Sum: {a+b}")
print(f"Diff: {a-b}")

# Q43
print(float("12.5"))

# Q44
cm = int(input())
print(cm / 100)

# Q45
x = int(input())
print(x)
print(float(x))

# Q46
print("Item: Book")
print("Price: 200")

# Q47
x = int(input())
print(type(x))
print(type(float(x)))

# Q48
x = int(input())
print(x)
print(float(x))

# Q49
name = input()
age = input()
print(f"Hello {name}, you are {age} years old")

# Q50
print("Name: John")
print("Age: 25")
print("Status: Active")



