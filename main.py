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
class handling():
    def red(self):
        A=open("C:\\Users\\HP\\Desktop\\phy.txt",'r')
        rd=A.read()
        A.close()
        return rd
    def wri(self):
        W=open("C:\\Users\\HP\\Desktop\\phy.txt",'w')
        W.write("surya/n dharshan/n anand/n")
        W.close()
    def apn(self):
        d=open("C:\\Users\\HP\\Desktop\\phy.txt",'a')
        d.write("vaishnavi")
        d.close()
obj=handling()
# obj.wri()
obj.apn()
nn=obj.red()
print(nn)


























