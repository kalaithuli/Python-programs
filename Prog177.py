'''
#closure
def outer_function():
    message="Hi"

    def inner_function():
        print(message)
    return inner_function

a = outer_function()
a()
'''
'''
#callback
def hi():
    print("hi")
def bye():
    print("bye")
def display(x):
    x()
display(hi)
display(bye)
'''
'''
#closure
def outer_function():
    message="Hi"

    def inner_function():
        print(message)
    return inner_function

x = outer_function()
x()
'''
'''
#closure
def outer_function(msg):
    message=msg
    
    def inner_function():
        print(message)
    return inner_function

fncn1 = outer_function("First fncn")
print(fncn1)
fncn2 = outer_function("Second fncn")
print(fncn2)
fncn1()
fncn2()
'''
'''
#decorators
def decorator_function(original_function):
    def wrapper_function():
        print("wrapper function got excecuted before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print("display fncn just ran")
    
decorated_display = decorator_function(display)

decorated_display()
'''
'''
# decorators
def decorator_function(original_function):
    def wrapper_function():
        return original_function()

    return wrapper_function

@decorator_function
def display():
    print("I just ran")
    
#display = decorator_function(display)
display()
'''
'''
def decorator_function(original_function):
    def wrapper_function():         #*args , **kwargs
        return original_function()

    return wrapper_function

@decorator_function
def display():
    print("display function just ran")
#@decorator_function
def display_info(name,age):
    print("Display info ran with ({},{})".format(name,age))

display_info("Kola",32)
# display = decorator_function(display)
display()
'''
'''
# the days earning is $x
def decorator(x):
    def wrapper(*args):
        print("The day's earning is $" , end =" ")
        x(*args)
    return wrapper

@decorator
def earn(a):
    print(a)

b = int(input("enter"))
earn(b)
'''
'''
def decorator(x):
    def wrapper(*args):
        print("**************")
        x(*args)
        print("**************")
    return wrapper
@decorator
def greet(*args):
    print("hello")

b=int(input("enter time"))
if b>7 and b<10:
    #greet = decorator(greet)
    greet()
'''
'''
#print vaaniiiii
def decorator(x):
    def wrapper(*args):
        print("**********")
        x(*args)
        print("**********")
    return wrapper
@decorator
def name(a):
    print(a)

b=input("Enter")
name(b)
'''
'''
def ola(s,d):
    print("Booked ola from ",s,"to",d)
def uber(s,d):
    print("Booked uber from ",s,"to",d)
def maps(s,d,app):
    app(s,d)
s,d,service=input("Enter s,d and service").split()
if service=='ola':
    maps(s,d,ola)
if service=='uber':
    maps(s,d,uber)
'''
'''
def num(x):
    def inc():
        nonlocal x
        x = x + 5
        return x
    return inc
a=int(input("enter: "))
b=num(a)
c=int(input("Enter: "))
for i in range(c):
    d = b()
print(d)
'''
'''
def sum(x):
    s=0
    for i in range(x):
        s+=i
    print(s)
def double(x):
    print(x*2)
def triple(x):
    print(x*3)
def do(a,n):
    n(a)
a=int(input("Enter: "))
do(a,sum)
do(a,double)
do(a,triple)
'''
import pickle
fin = open("Accounts.dat",'ab+')
try:
    while True:
        data = pickle.load(fin)
        print(data)
except EOFError:
    fin.close()
