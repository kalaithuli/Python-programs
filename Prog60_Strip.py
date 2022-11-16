a = input("Enter a string ").strip()
b = a[len(a)-1] + a[1:len(a)-1] + a[0]
print(b)

