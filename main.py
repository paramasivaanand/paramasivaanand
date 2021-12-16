# print("Anand again")
# a=10
# b=15
# c=a+b
# print("the value of c is",c)
# print(a>b)
# print(a//b)
# print(a%b)
# print(a>b and a<b)
# print (c+100)
# print(c*100)
# print(c*100)

# a=int(input("enter the value a="))
# b=int(input("enter the value b="))
# c=a+b
# print("the result is",c)
# print("a" in "anand")
# a=int(input("Enter the value of A"))
# b=int(input("Enter the value of B"))
# if(a>b):
#     print("A is greater than B")
# elif(a<b):
#     print(" A is less than B")
# else:
#     print("A is not greater than B")
# a=int(input("enter tha value of a"))
# b=int(input("enter the value of b"))
# c=int(input("enter tha value of c"))
# if(a>=b) and (a>=c):
#     largest = a
# elif(b>=a) and (b>=c):
#     largest = b
# else:
#     largest = c
# print("c is greater",largest)
# year=int(input("Enter the year"))
# if(year%4)==0:
#     if(year%100)==0:
#         if(year%400)==0:
#             print("The year is leap year".format(year))
#         else:
#             print("The year is not leap year".format(year))
#     else:
#         print("The year is leap year".format(year))
# else:
#     print("The year is not leap year".format(year))
# a=2
# while (a<10):
#     a=a+1
#     print(a)
# for a in range(10,20):
#     print(a)
#
# for a in range(100,2,-2):
#     print(a)
# for a in range(500,2,-100):
#     print(a)
# import os
# os.mkdir("test")

# import class1
# from class1 import  *
# from class1 import  add
# a=class1.add()
# print(a)
# number = int(input("Enter the number"))
# revnumber = 0
# while (number > 0):
#     remainder=number%10
#     revnumber=(revnumber * 10) + remainder
#     number=number//10
# print ("The reverse number is {0} {1}".format(revnumber,123))
# for i in range(15):
#     for j in range(i+1):
#         print (j+1,end="")
#     print("")
# a=[1,2,3]
# b=[1,2,3]
# a.append(4)
# b.append(77//10)
# a.extend(b)
# a.pop(2)
# a[2]=1000
# a[:3]
# print(a)
# def add(n):
#     return n+n
# x=map(add,[100,120,300,400,234])
# print(list(x))

# ####
# with parameter,with return
# without parameter,with return
# with parameter,without return
# without parameter,without return

# def test(a,b):
#     c=a+b
#     return c
# xx=test(10,20)
# print(xx)
#
#
#
# def test1():
#     c=10+20
#     return c
# result=test1()
# print(result)
#
#
#
# def test2(a,b):
#     c=a+b
#     print(c)
# test2(30,40)
#
#
# def test3():
#     c=10+20
#     print(c)
# test3()

# x=int(input("enter the value"))
# def fun1():
#     a=(x+2)*(x-3)
#     print(a)
# fun1()

# x=int(input("enter the value for x"))
# y=int(input("enter the value for y"))
# def fun2():
#     a=(x+23)
#     b=(y+42)
#     print (a,b)
# fun2()
#
# def vowels (n):
#     b=['a','e','i','o','u']
#     if (n in b):
#         return True
#     else:
#         return False
# x=vowels('a')
# print(x)
# data=(1,2,3,24)
# print(data)
# print(data[2])
# print(data[1:])
# print(1 in data)
# print(1 not in data)
# data1=(1,2,3,4,[1,4,5,6],"anand")
# data1[4][2]=100
# print(data1)
# fruit=('apple')
# n=10
# for i in range(int(n)):
#     fruit=(fruit,)
# print(fruit)
dataset={1,2,3}
print(dataset)
dataset.add(4)
print(dataset)
dataset.remove(1)
print(dataset)
dataset.update({4,5,6},[7,9,10])
print(dataset)
dataset.discard(2)
print(dataset)
dataset.discard(11)
print(dataset)
dataset.remove(3)
print(dataset)
