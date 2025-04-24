"""
name = input("Your name:")
money = input("Your cash:")
hungry = input("are you hungry? (Y/N):")

if hungry == "Y":
    if int(money) >= 30:
        print("go to eat")
    else:
        print("U R hungry but no money")
elif hungry == "N":
    if int(money) >= 30:
        print("no want buy")
    else:
        print("no hungry no money")
else:
    print("I don't know")
------------------------------------------------------
x = 0

while x < 5:
    print(x)
    x += 1

------------------------------------------------------
# cont = 0  # 計數用
# break #停止用
# continue #跳過用

for i in range(1, 5):
    for j in "abcdef":
        print(i, j)
        # cont += 1
# print(cont)
-------------------------------------------------------
x = [1, 2, 3, 4]
sqaure_x = [item**2 for item in x]
print(sqaure_x)
--------------------------------------------------------
def myAddition(a, b):
    print(a+b)
    return a+b

myAddition(10, 5)
-------------------------------------------------------
def myAddition(a, b):
    for i in range(a):
        for j in range(b):
            if i == 3 and j == 4:
                return
            print(i, j)

myAddition(10, 15)
-------------------------------------------------------
def square(num):
    return num ** 2


myList = [-10, 3, 9, 8, 10]

for item in map(square, myList):
    print(item)
-------------------------------------------------------
result = (lambda x: x**2)(5) #lambda本身就是一個不用名子的func簡寫且自帶return
print(result)
-------------------------------------------------------
"""
