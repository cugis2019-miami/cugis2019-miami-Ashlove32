# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

5/8 #division
print("Hello World")
print("I am learning to code on python today")
print(53)
(5*2)
(5/2)
(5-2)
(5^2)
(8/9*3)
"the division of 5/2 is 2.5"
print("5/2")
print("the division of 5/2 is" , 2.5)
#create fuction to sum any two numbers
def plus(a,b):
    plus = a + b
    print(plus)
plus(2,3)

#create function to sum any two numbers
def subtract(a,b):
    subtract= a-b
    print(subtract)
    
Subtract(80,60)

def triangle(b,h):
    triangle= b * h * (1/2)
    print(triangle)
hey
"hey"
helllloooo




def areasquare(a):
    areasquare= a**2
    print(areasquare)
    
areasquare(4)











print("box",=5)








box = 5+5
print(box)


#choclate types
d = "dark"
m = "milk"
w = "white"

print(d,m,w)


"d"= dark
print("hi Mrs.Amita how are you doing today?")



m = " Mrs. Amita"
print("how are you doin today",m,"?")


a = "74"
print("I have",a,"choclate bars !!!")

kim = "5"
print("I have",kim,"phones")
import math

dir(math)

math.pow(2,1/4)





chocolatebox = {"milk":5,"dark":3,"white":8}
print("the number of white chocolate in chocolate box is",chocolatebox["milk"])

male = "male"




#dict
classroom1 = {"Steve is 32 year old male"}
classroom2 = {"Lia is a 28 year old female"}
classroom3 = {"Vin is a 45 year old male"}
classroom4 = {"Katie is a 38 year old female"}

import pandas
dir(pandas)

pandas.Series("hi")


classroominfo = pandas.Series(classroom4)
print(classroominfo)
classroom4 = {"milk":5,"white":3,"dark":8}




#convert dict
classroomdata = [classroom4]
print(classroomdata)


classroomdf = pandas.DataFrame(classroomdata)
print(classroomdf)

age = {"Steve":32,"Lia":28,"Vin":45,"Kate":38}
Gender = {"Steve":M,"Lia":F,"Vin":M,"Kate":F}


#dict
studentinfo = [['Steve',32,'male'],['Lia',28,'female']]
df = pandas.DataFrame(studentinfo)
print(df)

df1 = pandas.DataFrame([studentinfo])
print(df1)

df12 = pandas.DataFrame([studentinfo], index=["age"])
print(df12)

df2 = pandas.DataFrame(studentinfo, colums=["name","age","gender"])
print(df2)



