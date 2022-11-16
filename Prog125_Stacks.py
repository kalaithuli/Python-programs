top = None
stack = eval(input("Enter a stack "))
# Function to push elements into the stack
def push(stk):
    item = input("Enter the Element")
    stk.append(item)
    top = len(stk) - 1

# Function to pop elements from the stack
def pop(stk):
    if stk == []:
        print("Underflow! Stack is empty")
        return
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk) - 1
        print("Popped Item = ", item)

# Function to display elements in the stack
def display(stk):
    if stk == []:
        return "Underflow"
    else:
        top = len(stk) - 1
        print(stk[top], "<-top")
        for i in range(top - 1, -1, -1):
            print(stk[i])

# Main program - Menu
while True:
    print("Stack Operations")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    ch = int(input("Enter your Choice"))
    if ch == 1:
        push(stack)
    elif ch == 2:
        pop(stack)
    elif ch == 3:
        display(stack)
    elif ch == 4:
        break
    else:
        print("Invalid Choice")

