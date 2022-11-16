def binarysearch(arr,item):
    beg = 0
    last = len(arr) - 1
    while(beg<=last):
        mid = (beg+last)//2
        if(item ==arr[mid]):
            print("Element found at " ,mid)
            break
        elif(item > arr[mid]):
            beg = mid + 1
        else:
            last = mid - 1
    else :
        print("Element not found ")

def removeduplicate(a):
    empnonew = []
    for i in a:
        if i not in empnonew:
            empnonew.append(i)
    print(empnonew)

def bubblesort(a):
    n = len(a) - 1
    for i in range(n, 0, -1):
        for j in range(n, n - i, -1):
            if (a[j] > a[j - 1]):
                a[j], a[j - 1] = a[j - 1], a[j]
    print(a, n)

empno = eval(input("Enter the employees numbers "))
name = eval(input("Enter the employees names "))
salary = eval(input("Enter the employees salary "))
ans ='y'
while ans == 'y':
    print("1)Binary search")
    print("2)Remove duplicate")
    print("3)Bubble sort")
    ch = int(input("Enter your choice "))
    if ch == 1:
        item = eval(input("Enter the employee number to be found "))
        binarysearch(empno,item)
    elif ch == 2:
        removeduplicate(empno)
    elif ch == 3:
        bubblesort(salary)
    else:
        print("Wrong choice ")
    ans = input("Do you want to continue? y or n? ")



