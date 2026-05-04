def hello():
    print("Hello, World!");

hello();

def add(a, b):
    c = a + b;
    print("The sum of a and b is:", c);

add(10, 20);

def multiply(a, b):
    c = a * b;
    print("The product of a and b is:", c);

multiply(30, 50);

def divide(a, b):
    if b != 0:
        c = a / b;
        print("The division of a by b is:", c);
    else:
        print("Error: Division by zero is not allowed.");

divide(100, 4);

def modulus(a, b):
    c = a % b;
    print("The modulus of a by b is:", c);

modulus(10, 3);

def subtract(a,b):
    c=a-b;
    print("the difference of a and b is :",c);

subtract(50,20);


def power(a,b):
    c=a**b;
    return c;

print("the value of a raised to the power b is :",power(2,3));