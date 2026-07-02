
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
#Taking input for first time

first_number = float(input("Pls type the first Number \n"))
if first_number == type(str):
    print("Invalid Input")
Operation = input("""PLs type the operation you want to apply to the number
operation supported-:
+ for addition
- for subtraction
* for Multiplication
/ for Division
""")
second_number = float(input("Pls type the second Number \n"))
if second_number == type(str):
    print("Invalid Input")
#assigning functions based on input operation
if Operation == "+":
    A = add(n1=first_number, n2=second_number)
    print(A)
elif Operation == "-":
    A = subtract(n1=first_number, n2=second_number)
    print(A)
elif Operation == "*":
    A =multiply(n1=first_number, n2=second_number)
    print(A)
elif Operation == "/":
    A = divide(n1=first_number, n2=second_number)
    print(A)

else:
    print("invalid Input")
#asking user if they want continue the calculation on the number or start a new calculation
continue1 = input(f"if you want to continue more calculation with {A} press Y, or you want to start a new calculator,press N").upper()
#doing calculation with the number
while continue1 == "Y":
    second_number = float(input("Pls type the Number you want to do operation with a\n"))
    if second_number == type(str):
        print("Invalid Input")
    Operation = input("""PLs type the operation you want to apply to the numbers
    operation supported-:
    + for addition
    - for subtraction
    * for Multiplication
    / for Division
    """)

    if Operation == "+":
        A = add(n1=A, n2=second_number)
        print(A)
    elif Operation == "-":
        A = subtract(n1=A, n2=second_number)
        print(A)
    elif Operation == "*":
        A = multiply(n1=A, n2=second_number)
        print(A)
    elif Operation == "/":
        A = divide(n1=A, n2=second_number)
        print(A)

    else:
        print("invalid Input")

    continue1 = input(
        f"if you want to continue more calculation with {A} press Y, or you want to start a new calculator,press N").upper()
#Starting a new calculator
while continue1 == "N":
    print(art.logo)
    first_number = float(input("Pls type the first Number \n"))
    if first_number == type(str):
        print("Invalid Input")
    second_number = float(input("Pls type the second Number \n"))
    if second_number == type(str):
        print("Invalid Input")
    Operation = input("""PLs type the operation you want to apply to the numbers
    operation supported-:
    + for addition
    - for subtraction
    * for Multiplication
    / for Division
    """)

    if Operation == "+":
        A = add(n1=first_number, n2=second_number)
        print(A)
    elif Operation == "-":
        A = subtract(n1=first_number, n2=second_number)
        print(A)
    elif Operation == "*":
        A = multiply(n1=first_number, n2=second_number)
        print(A)
    elif Operation == "/":
        A = divide(n1=first_number, n2=second_number)
        print(A)

    else:
        print("invalid Input")

    continue1 = input(
        f"if you want to continue more calculation with {A} press Y, or you want to start a new calculator,press N").upper()
