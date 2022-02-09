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
# dataset={1,2,3}
# print(dataset)
# dataset.add(4)
# print(dataset)
# dataset.remove(1)
# print(dataset)
# dataset.update({4,5,6},[7,9,10])
# print(dataset)
# dataset.discard(2)
# print(dataset)
# dataset.discard(11)
# print(dataset)
# dataset.remove(3)
# print(dataset)

# class one :
#     def add (self,a,b):
#         c=a+b
#         print(c)
#         return c
#     def sub(self,a,b):
#         c=a-b
#         return c
# if __name__ =="__main__":
#     obj = one()
#     print(obj)
#     A=obj.add(1,2)
#     B=obj.sub(1,2)
#     print(A,B)
#
# class Test:
#     def __str__(self):
#         return"phyton"
#     def __int__(self):
#         return 10
#     def add(self,a,b):
#         c=a+b
#         return c
# obj=Test()
# A=obj.add(2,3)
# print(A)
# print(int(obj))

# class new:
#     c=0
#     def __init__(self):
#         self.b=int(input("enter the value of b"))
#         self.h=int(input("enter the value of h"))
#     def  areaoftriangle(self):
#         c=1%2*self.b*self.h
#         print("Result",c)
#         return c
#     def areaofsquare(self):
#         s=self.b*self.b
#         print("Result",s)
#         return s
#     def add(self,a,b):
#         d=a+b
#         print("Result",d)
#         return d
#     def square(self,a,b):
#         sq=1%2*a*b
#         print("Result",sq)
#         return sq
# obj=new()
# tt=obj.areaoftriangle()
# ss=obj.areaofsquare()
# dd=obj.add(3,5)
# sa=obj.square(4,4)
# print(tt)
# print(ss)
# print(dd)
# print(sa)

# import Test1.func as t
# result=t.add(10,20)
# print(result)
# import Test1.func as s
# result=s.sub(23,10)
# print(result)
# import class1
# result=class1.add()
# print(result)
# import Test1.func as f
# from Test1.func import add
# result=add(10,10)
# print(result)
# from Test1.func import sub
# result=sub(10,5)
# print(result)
# class marks():
#     def __init__(self,Tamil,English,Maths,Science,Social):
#         self.a=Tamil
#         self.b=English
#         self.c=Maths
#         self.d=Science
#         self.e=Social
#
#     def avg(self):
#         avg=(self.a+self.b+self.c+self.d+self.e)//5
#         print("Average",avg)
#         grade=""
#         if avg >= 90:
#             grade="A"
#         elif(avg >= 80):
#             grade="B"
#         else:
#             grade="fail"
#         return grade
#
# Tamil=int(input("enter the mark of Tamil"))
# English=int(input("enter the mark of English"))
# Maths=int(input("enter the mark of maths"))
# Science=int(input("enter the mark of science"))
# social=int(input("enter the valur of social"))
# grade=marks(Tamil,English,Maths,Science,social)
# Marksavg=grade.avg()
# # print(Marksavg)
# ###########inheritenc|single########
# class parent():
#     def add(self,a,b):
#         return a+b
# class child(parent):
#     def sub(self,a,b):
#         return a-b
# obj=child()
# x=obj.add(1,2)
# y=obj.sub(3,2)
# print(x,y)
# ############inheritence|multiple child#######
# class parent1():
#     def add(self,a,b):
#         return a+b
# class child1(parent1):
#     def mul(self,a,b):
#         return a*b
# class child2(parent1):
#     def div(self,a,b):
#         return a//b
# obj1=child1()
# obj2=child2()
# aa=obj1.add(3,4)
# bb=obj1.mul(5,4)
# cc=obj2.div(25,5)
# print(aa,bb,cc)
# ###############inheritence|multiple parent#########
# class parent3():
#     def add(self,a,b):
#         return a+b
# class parent4():
#     def sub(self,a,b):
#         return a-b
# class child3(parent3,parent4):
#     def mul(self,a,b):
#         return a*b
# obj3=child3()
# dd=obj3.add(5,5)
# ee=obj3.mul(15,5)
# ff=obj3.sub(10,5)
# print(dd,ee,ff)
#
# ################inheritence|multilevel#######
# class university():
#     def add(self,a,b):
#         return a+b
# class college(university):
#     def mul(self,a,b):
#         return a*b
# class department(college):
#     def div(self,a,b):
#         return a//b
# class classroom(department):
#     def sub(self,a,b):
#         return a-b
# obj4=classroom()
# multi=obj4.add(5,4)
# print(multi)
####################inheritence|call parent form child############
# class test():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         c=self.a+self.b
#         print(c)
# class test1(test):
#     def __init__(self,a,b,c,d):
#         self.c=c
#         self.d=d
#         super().__init__(a,b)
#     def mul(self):
#       self.c*self.d
# obj5=test1(10,20,49,56)
# ab=obj5.add()
# bb=obj5.mul()
# print(ab)
# print(bb)
################################################Ploymorphism#####
#
# class network():
#     def basic(self):
#         print("CCNA")
#     def advanced(self):
#         print("CCNP")
# class program():
#     def basic(self):
#         print("java")
#     def advanced(self):
#         print("phyton")
# net = network()
# pro = program()
# for i in (net,pro):
#     i.basic()
#     i.advanced()
#################################Overloading#############
# def add(a,b):
#     return a+b
# a=add(2,3)
# def add(a,b,c):
#     return a+b+c
# b=add(2,3,4)
# print(a)
# print(b)
#####################overloading args#########
# def add(datatype,*args):
#     sum=0
#     if (datatype =='int'):
#         for i in args:
#             sum=i+sum
#         return sum
#     if (datatype=='str'):
#         return "phyton"
# b=add('int',10,20,10,50)
# c=add('str')
# print(b)
# print(c)
##################overriding########
# class anand():
#     def vaishu(self):
#         return 'dharshan'
# class anand1(anand):
#     def vaishu(self):
#         return 'surya'
# father=anand()
# fatherr=anand1()
# a=father.vaishu()
# b=fatherr.vaishu()
# print(a)
# print(b)
###############################exception handling######try,except,finally and raise
# def add(a,b):
#     try :
#         c=a+b ###if we define any value other than a and b it will go to exception blog example:d
#         print(c)
#     except Exception as e:
#         print(e)
# add(1,2)
############################file handling######
# class handling():
#     def red(self):
#         A=open("C:\\Users\\HP\\Desktop\\phy.txt",'r')
#         rd=A.read()
#         A.close()
#         return rd
#     def wri(self):
#         W=open("C:\\Users\\HP\\Desktop\\phy.txt",'w')
#         W.write("surya/n dharshan/n anand/n")
#         W.close()
#     def apn(self):
#         d=open("C:\\Users\\HP\\Desktop\\phy.txt",'a')
#         d.write("vaishnavi")
#         d.close()
# obj=handling()
# # obj.wri()
# obj.apn()
# nn=obj.red()
# print(nn)
##################################################
# class newfile():
#     def redd(self):
#         r=open("C:\\Users\\HP\\Desktop\\phy.txt",'r')
#         rrd=r.read()
#         r.close()
#         return rrd
#     def rw(self):
#         w=open("C:\\Users\\HP\\Desktop\\phy.txt",'w')
#         w.write("Surya Dharshan")
#         w.close()
# obj=newfile()
# nw=obj.redd()
# print(nw)
# rww=obj.rw()



# r=open("C:\\Users\\HP\\Desktop\\phy.txt",'r')
# rrd=r.read()
# r.close()
#
#
# rrd=rrd.split("\n") ##### splite used to convert it to array
#
# rrd=rrd[::-1] ####reverse predefined fucniton in phyton
# print(rrd)
# w=open("C:\\Users\\HP\\Desktop\\phy.txt",'w')
# for i in rrd:
#     w.write(i+"\n")
# w.close()

# mylist=[['s.no','name','age','citloy'],[1,'Anand',    34,'   chennai'],[2,'Vaishu',27,'chennai'],[3,'Surya',2,'chennai']]
# for a in mylist:
#
#     for b in a:
#         print(b,end='\t')
#     print()

# mylist1 = []
# a = int(input("enter the number of elements:"))
# for m in range(0,a):
#     element = [input(),input(),int(input())]
#     mylist1.append(element)
# print('name'+'\t'+'city'+'\t'+'age',end='\n')
# for b in mylist1:
#     for j in b:
#         print(j,end=' ')
#     print()

##############args and kwargs########
# def num (*args):
#     sum = 0
#     for n in args:
#         sum+=n
#     return sum
# tt=num(12,34,67)
# print(tt)
# def ite (**data):
#     for key,value in data.items():
#         print("{},{}".format(key,value))
# result = ite(firstname='anand',age =34,lastname = 'c',pincode=627811)
# print(result)
####################API##restAPI####import json###Json.loads####json.dumps+

#####lamda##Assert###List comprehension###dist comprehension###map ### filter ### Chr(Ascii)
# x=lambda a,b:a+b
# print(x)
# print(x(10,20))
#
# def ad (n):
#     return lambda a:n*a
# a=ad(3)
# n=a(10)
# print(n)
#
# def avg (n):
#     assert len(n)!=0,"empty list"
#     return sum(n)/len(n)
# x=avg([1,2,5,8,10])
# print(x)
#
# x=[i for i in range(100) if i%10==0]
# print(x)
#
# x={i:chr(i) for i in range(91) if (i > 64)}
# print(x.keys())
# print(x.values())
#
# def name (n):
#     return n*n
# x=map(name,[1,2,3,4,5])
# print(list(x))
#
# def vowels (n):
#     a = ['a','e','i','o','u']
#     if n in a:
#         return True
#     else:
#         return False
# x=filter(vowels,['a','b','c','d','e','f','g','h','i','j'])
# print(list(x))

#############################Tkinter###########################
# import tkinter as tk
# from tkinter import *
# import pymysql
#
# root = tk.Tk()
# root.geometry('500x500')
# root.title("Registration form")
#
# Fullname=StringVar()
# Email=StringVar()
# var = IntVar()
# c=StringVar()
# var1= IntVar()
#
# def database():
#    name1=Fullname.get()
#    email=Email.get()
#    gender=var.get()
#    country=c.get()
#    prog=var1.get()
#    conn = pymysql.connect('Registration form.db')
#    with conn:
#       cur=conn.cursor()
#    cur.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
#    cur.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
#    conn.commit()
#
# label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
# label_0.place(x=90,y=53)
# label_1 = Label(root, text="Fullname",width=20,font=("bold",10))
# label_1.place(x=80,y=130)
# entry_1 = Entry(root,textvariable=Fullname)
# entry_1.place(x=240,y=130)
# label_2=Label(root, text="Email",width=20,font=("bold",10))
# label_2.place(x=68,y=180)
# entry_2 = Entry(root,textvariable=Email)
# entry_2.place(x=240,y=180)
# label_3=Label(root, text="gender",width=20,font=("bold",10))
# label_3.place(x=70,y=230)
# Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
# Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
# label_4=Label(root,text="country",width=20,font=("bold",10))
# label_4.place(x=70,y=280)
# list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
# droplist=OptionMenu(root,c, *list1)
# droplist.config(width=15)
# c.set('select your country')
# droplist.place(x=240,y=280)
# label_5 = Label(root, text="Programming",width=20,font=("bold", 10))
# label_5.place(x=85,y=330)
# var2= IntVar()
# Checkbutton(root, text="java", variable=var1).place(x=235,y=330)
# Checkbutton(root, text="python", variable=var2).place(x=290,y=330)
# Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)
# root.mainloop()
# import os
# cwd = os.getcwd()
# lst = os.listdir()
# print(cwd)
# print(lst)
# print(os.name)


import datetime

dateti=datetime.datetime.now()
datety=datetime.date.today()
print(dateti)
print(datety)
print(dir(datetime))

from datetime import date
today = date.today()
print(today)

from datetime import *
a=time()
b=time(11,30,40)
c=time(hour=11,minute=15,second=13,microsecond=15)
print(a)
print(b)
print(c)

from datetime import time
a=time(11,30,15)
print(a.hour)
























