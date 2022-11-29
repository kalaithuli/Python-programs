'''
a = ord("A")
for i in range(1,10,2):
    for j in range(1,i+1):
        print(chr(a),end="")
        a+=1
    print()

a = int(input())
b = int(input())
flag = True
for i in range(2,max(a,b)):
    if a%i == 0 and b%i == 0:
        flag = False
if flag == True:
    print("Co prime")
else:
    print("Nco")
places ="""karnataka bangalore lalbagh
tamilnadu kanyakumari vivekananda_rock
kerala Thiruvananthapuram padmanabha_temple
kerala idukki munnar
karnataka mysore brindavan_gardens
karnataka mysore mysore_palace
karnataka hassan shravanabelagola
tamilnadu chennai egmore_museum
tamilnadu kanyakumari kaamaakshmi_temple
karnataka bangalore cubbon_park
karnataka hampi maharnavami_dibba"""
l = places.split("\n")
result = {} #outer dict
for line in l:
    state,city,place = line.split()
    if state not in result:
        result[state] = {} #inner dict
    if city not in result[state]:
        result[state][city] = [] #list - value of inner dict
    result[state][city].append(place)
print(result)
'''

'''
AAAAA
BBBB
CCC
DD
E

a = ord("A")
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(chr(a),end ="")
    a = a + 1
    print()
'''
