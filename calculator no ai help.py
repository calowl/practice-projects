# variable and ask for input

x =int(input("enter first number: "))

operation= input("choose equation type: ")

y = int(input("enter second number: "))

# equations

def equations():

    addition = x + y 
    subtraction = x - y 
    division = x / y 
    multiplication = x * y 

#if else staments

if operation == "+":
    result = x + y 
elif operation == "-":
    result = x - y
elif operation == "/":
    if y == 0:
        print("cannot divide by 0")
    else:
        print(x / y)
elif operation == "*":
    result = x*y
else :
    print("invalid operation")

#prints result 

print(f"the answer is: {result}")