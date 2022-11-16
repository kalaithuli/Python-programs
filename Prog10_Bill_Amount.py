# Write a program to calculate the bill amount for an item given its quantity sold, value, discount, tax
qnty = int(input("Enter the quantity of the items "))
val = float(input("Enter the price "))
disc = float(input("Enter the discout "))
tax = float(input("Enter the tax percentage "))
bill = (val * qnty) - (disc / 100 * (val * qnty)) + (tax / 100 * (val * qnty))
print("Bill amount " , bill)
