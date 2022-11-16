def insertionsort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while (j >= 0 and key < l[j]):
            l[j + 1] = l[j]
            j -= 1
            l[j + 1] = key
    print ("Sorted array is:")
    for i in range(len(l)):
        print (l[i])

def bubblesort(l):
    for j in range(len(l)):
        swapped = False
        i = 0
        while i < len(l) - 1:
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True
            i = i + 1
        if swapped == False:
            break
    print(l)

print("1) Sort numbers ")
print("2) Sort names ")
ch = int(input("Enter your choice: "))
if (ch == 1):
    list = eval(input("Enter a list of numbers "))
    insertionsort(list)
else :
    list = eval(input("Enter a list of names "))
    bubblesort(list)

