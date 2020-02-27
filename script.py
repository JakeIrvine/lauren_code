myList = [1, 2, 3, 4]
myOtherList = ["sdfls", 56, "sdfs", -1]

for item in myList:
    print(item, end='')
print("")
x=int(input("number 1:"))
y=int(input("number 2:"))
z=input("divide or multiply?")
if z=="divide":
    print(x/y)
else:
    print(x*y)
