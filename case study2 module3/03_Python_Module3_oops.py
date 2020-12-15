# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:13:57 2018

@author: NAEEN REDDY
"""



#Creating a Class
class number():
    pass

#Creating Instance of Class
x=number()
print(x)

##Method

class Edureka():
    def Hello(self):
        print("Happy Learning")
    def bye(self):
        print("GooD Bye")

ob=Edureka()
ob.Hello()
ob.bye()

ob1=Edureka()
ob1.Hello()



##Scope of variables
a=50
class number():
    b=30
    print(b)

print(a)
print(b)
number()


a=30
def add(b):
    c=30
    print("c=",c)
    sum=b+c
    print("Addition is: ",sum)

print(a)
add(40)
print(c)


##Built in class attributes
class Edureka:
    empcount=0

print("Edureka.__dict__:",Edureka.__dict__)

print("Edureka.__doc__:",Edureka.__doc__)

print("Edureka.__name__",Edureka.__name__)

print("Edureka.__module__:",Edureka.__module__)

print("Edureka.__bases__:",Edureka.__bases__)


##user defined attributes

a=50

class Foo(object):
    def meth(self):
       pass
   

###public provate protected
class Edureka():
    def __init__(self):
        self.__pri="I am Private"
        self._pro="I am Protected"
        self.pub="I am Public"

ob=Edureka()

#Accessing Public Attribute
ob.pub

#Accessing Protected Attributes
ob._pro

#Accessing Private Attributes
ob.__pri



###Private method
class MyClass:
    def myPublicMethod(self):
        print('public method')
    def __myPrivateMethod(self):
        print('this is private!!')

obj = MyClass()
obj.myPublicMethod()

obj.__myPrivateMethod()

#obj.__myPrivateMethod()
obj._MyClass__myPrivateMethod()


### Class variables are instence variables
class Edureka:
    domain=("Data Science")
    def Setcourse(self,name):
        self.name=name

ob1=Edureka()
ob2=Edureka()
ob3=Edureka()

ob1.Setcourse("Python")
ob2.Setcourse("Machine Learning")
ob3.Setcourse("R")

print(ob1.domain)
ob1.domain = 'Sciprting'
print(ob1.domain)
print(ob2.domain)

print(ob1.name)
print(ob2.name)


##Constructor an destructor
class TestClass:
    def __init__(self):
        print("genrate emp id ")

    def __del__(self):
        print("destructor")

obj = TestClass()

if __name__ == "__main__":
    obj = TestClass()
    del obj
    
#self :

#self represents the instance of the class. By using the "self" keyword we can 
#access the attributes and methods of the class in python.

#__init__ :

#"__init__" is a reseved method in python classes. It is known as a constructor 
#in object oriented concepts. This method called when an object is created from the class 
#and it allow the class to initialize the attributes of a class.
    
##Multiple constructor
#You can make static methods or class methods with the  
#@classmethod decorator to return an instance of your class, or to              https://stavshamir.github.io/python/2018/05/26/overloading-constructors-in-python.html
#add other constructors.
class Date:
	def __init__(self, year, month, day): #year-month-day
		self.year = year
		self.month = month
		self.day = day
		# print("init")

	@classmethod
	def dmy(cls, day, month, year): #day-month-year
		# print("dmy")
		cls.year = year
		cls.month = month
		cls.day = day
		#order of return should be same as init
		return cls(cls.year, cls.month, cls.day)

	@classmethod
	def mdy(claas, month, day, year): #month-day-year
		# print("mdy")
		claas.year = year
		claas.month = month
		claas.day = day
		#order of return should be same as init
		return claas(claas.year, claas.month, claas.day)
    
    

a=Date(2016, 12, 11)
print(a.month) #2016

b=Date.dmy(9, 10, 2015)
print(b.year) #2015

a=Date.mdy(7, 8, 2014)
print(a.month) #2014


##Getter and Setter
class Edureka:
    def __init__(self,courseName):
        self.courseName=courseName

    def setCourse_Name(self,courseName):
        self.courseName=courseName

    def getCourse_Name(self):
        return(self.courseName)

ob=Edureka("Machine Learning")

print(ob.getCourse_Name())

ob.setCourse_Name("Python")
print(ob.getCourse_Name())



###sing inheritence
class base1:
    def fun(self):
        print("my property ")
        
class sub(base1):
        pass
 

ob=sub()
ob.fun()

           
      
class base2:
    def funtoo(self):
        print("my property2 ")

class sub(base2,base1):
        pass

ob=sub()
ob.fun()
ob.funtoo()


#####multi inheritence

#Additionally, we use super() function before __init__() method. 
#This is because we want to pull the content of 
#__init__() method from the parent class into the child class.

#Multiple Inheritance
class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")


class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")


class Third(Second, First):
    def __init__(self):
        super(Third, self).__init__()
        print("third")


Third();
Second();



#Multilevel Inheritance
class Animal:
    def eat(self):
      print('Eating...')
      
class Dog(Animal):
   def bark(self):
      print('Barking...')
      
class BabyDog(Dog):
    def weep(self):
        print('Weeping...')
d=BabyDog()
d.eat()
d.bark()
d.weep()




##Over writing method
class Parent: # define parent class
  def myMethod(self):
    print("Calling parent method")
    
class Child(Parent): # define child class
  def myMethod(self):
    print("Calling child method")
    
c = Child()   # instance of child
c.myMethod() # child calls overridden method

p = Parent()   # instance of parent
p.myMethod()


##Getter and Setter
class Edureka:
    def __init__(self,courseName):
        self.courseName=courseName

    def setCourse_Name(self,courseName):
        self.courseName=courseName

    def getCourse_Name(self):
        return(self.courseName)

ob=Edureka("Machine Learning")

print(ob.getCourse_Name())

ob.setCourse_Name("Python")
print(ob.getCourse_Name())



#Another Example:

class Rectangle():
  def __init__(self,length,breadth):
    self.length = length
    self.breadth = breadth
  def getArea(self):
    print(self.length*self.breadth," is area of rectangle")

class Square(Rectangle):
  def __init__(self,side):
    self.side = side

  def getArea(self):
    print(self.side*self.side," is area of square")

s = Square(4)
r = Rectangle(2,4)
s.getArea()
r.getArea()



###Poly
class Animal:
    def __init(self,name):
        self.name=name

    def talk(self):
        print("Talk")

class Cat(Animal):
    def talk(self):
        print("Meow")

class Dog(Animal):
    def talk(self):
        print("Woof")

c=Cat()
c.talk()

d=Dog()
d.talk()




class Bear(object):
    def sound(self):
        print ("Groarrr")
 
class Dog(object):
    def sound(self):
        print ("Woof woof!")
 
def makeSound(animalType):
    animalType.sound()
 
 
bearObj = Bear()
dogObj = Dog()
 
makeSound(bearObj)
makeSound(dogObj)






###Moules

import math 

print(dir(math))


from math import ceil,fabs

###sys
import sys

print(math.__doc__)
print(not sys)

print(sys.winver)

print(sys.flags)

print(sys.prefix)


print(sys.argv)

print(sys.exit())






##Math
import math

print(dir(math))
print(math.ceil(10.098))

print(math.copysign(10,-1))

print(math.fabs(-19.7))

print(math.exp(6.907755278982137))

print(math.expm1(2))

print(math.log(1000))


print(math.acos(0.5))

print(math.asin(0.5))

print(math.atan(5))

print(math.cos(3))

print(math.degrees(0.1))

print(math.radians(5.729577795))

print(math.pi)

print(math.e)


##JSON
















