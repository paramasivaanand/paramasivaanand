# print("anand")
# year=int(input("Enter the year"))
# if(year%4)==0:
#     if(year%100)==0:
#         if(year%400)==0:
#             print("the year is leap year")
#         else:
#             print("The year is not leap year")
#     else:
#         print("The year is leap year")
# else:
#  print("The year is not leap year")
# a=int(input("enter the number"))
# if a%2==0:
#     print("even number")
# else:
#     print("odd number")
# a=int(input("Enter the valu"))
# if (a==1):
#     print("The value is ",a)
# elif(a==10):
#     print("The value is ",a)
# else:
#     print("The value is not equal")
# a=int(input("Enter the value of a"))
# b=int(input("enter the value of b"))
# c=int(input("Enter the value of c"))
# if(a>=b)and(a>=c):
#     print(" A is greatest")
# elif(b>=a)and(b>=c):
#     print("B is greatest")
# else:
#     print("c is greatest")
# year=int(input("Enter the year"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("The year is leap year")
#         else:
#             print("The year is not leap year")
#     else:
#         print("The year is leap year")
# else:
#     print("The year is not leap year")
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# while True:
#     choice = input("enter the option(1/2/3)")
#     if choice in ( '1','2','3'):
#         num1=float(input("enter the first number"))
#         num2=float(input("enter the second number"))
#     if choice == '1':
#         print(num1,"+",num2,"=",add(num1,num2))
#     elif choice == '2':
#         print(num1,"-",num2,"=",sub(num1,num2))
#     elif choice == '3':
#         print(num1,"*",num2,"=",mul(num1,num2))
#         next = input("do you ready for another calculation(y/n)")
#         if next == "n":
#             break
#     else:
#         print("invalid entry")
# a = 1
# while a < 10:
#     print(a)
# #     a=a+1
# import random
# n=10
# To_be_guess = int(n*random.random()) +1
# guess = 0
# while guess != To_be_guess:
#     guess = int(input("New number"))
#     if guess > 0 :
#         if guess > To_be_guess:
#             print("number large")
#         elif guess < To_be_guess:
#             print("Numbe small")
#     else:
#         print ("sorry")
#         break
#
# else:
#     print("congo")

# mylist = []
# heading = ['Name','city','Age']
# a = int(input("enter the element count:"))
# for b in range(0,a):
#     element =[input(),input(),int(input())]
#     mylist.append(element)
# for c in mylist:
#     print(heading,end='\n')
#     print( c,end='\n')
#     print()

# import tkinter as tk
# from tkinter import *
# anand = tk.Tk()
# anand.geometry('500x500')
# anand.title("anand")
# label_1=Label(anand,text="vaishuanand",width=100,font=100)
# label_1.place(x=100,y=150)
# anand.mainloop()
# import os
# cwd=os.getcwd()
# print(cwd)
import datetime
from datetime import *
class datfile():
    def timdat(self):
        op=open("C:\\Users\\ADMIN\\Desktop\\new file.txt",'w')
        op.write("anand")
        op.close()

    def timdat1(self):
        on=open("C:\\Users\\ADMIN\\Desktop\\new file.txt",'r')
        nn=on.read()
        on.close()
        return nn
obj=datfile()
nw=obj.timdat()
nw1=obj.timdat1()
print(nw)
print(nw1)

