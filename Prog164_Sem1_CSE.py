import matplotlib.pyplot as plt
import math
"""
# initializing the data
x = [10,20,30,40,50]
y = [20, 30, 40, 50]

# plotting the data
plt.plot(x, y)

# Adding the title
plt.title("Simple Plot")

# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()

import matplotlib.pyplot as plt
import math

# initializing the data
x = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
y = [4.646*10**-14,2.647*10**-13,1.735*10**-12,1.282*10**-11,1.157*10**-10,1.301*10**-9,2.015*10**-8,5.145*10**-7,3.571*10**-5]

# plotting the data
plt.plot(x, y)

# Adding the title
plt.title("Simple Plot")

# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()
"""
"""
l=[]
x=[]
c = 1
i = 0.1
while i != 10.1 :
  a = ((2 * (9.1 * 10**-31) * (10-c) * (1.6* 10**-19))**0.5)/(1.05* 10**-34)
  t = math.exp(-2 * 10**-9 * a)
  l.append(t)
  x.append(i)
  c+=1
  i = i + 0.1
plt.plot(x,l)
"""
l = []
x = []
c = 1
i = 0.1
while c!=500:
    a = ((2 * (9.1 * 10 ** -31) * (10 - c) * (1.6 * 10 ** -19)) ** 0.5) / (1.05 * 10 ** -34)
    t = 2.718281828459045235360 ** (-2 * 10 ** -9 * a)
    l.append(t)
    x.append(i)
    c += 1
    i = i + 0.1
print(x)
print(l)
plt.plot(x,l)
plt.show()