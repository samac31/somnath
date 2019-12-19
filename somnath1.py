# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 09:52:40 2019

@author: Administrator
"""

a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
print("before swaping")
print("a=",a)
print("b=",b)
print("aftre swaping")
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)


a=input("enter 1st string\n")
b=input("enter 2nd string\n")
c=a+b
print(c)

a1='abc'
a1="abc"

b1=a1

a1='abc11'
a1="abc12"
b1=a1


a1=ab

2*ab

25+11/19

10*(5-2)

11% 5



a1='abcdef'
c1='m'
b1=a1.replace(a1[3],c1)
print(b1)




a1='abcdef'
b1='m'
a1[3]=b1
print(a1)




"apple's are healthy"*3


for i in range(1,20):
    
   
    if i%2!=0:
        pass
    else:
        print(i)
        
        
        
        
        
        
n=int(input("enter n\n"))        
a1=[]
for i in range(0,n):
    a1.append(int(input("enter elements\n")))
    
    
s1=sum(a1)
print("sum:",s1)
print("average:",s1/n)



for i in range(0,3):
    for j in range(0,3):
        print("*",end="")
        
    print("")



print("c:\myfiles\myfolder")


print("c:\myfiles\\newfolder")

print("""This is Demo text
      along with sample
      output""")

n=int(input("enter year\n")) 

if n%4==0:
    print(n,"is leap year")
else:
    print(n,"is not a leap year")
    
    
    
    

n=[]
n=input("enter STRING\n")
t1=t2=t3=t4=0

x=len(n)
print("Lentgh of string",x)


for m in range(x):
    if n[m]=='a':
        t1=t1+1
 
    elif n[m]=='s':
        t2=t2+1

    elif n[m]=='e':
        t3=t3+1

    elif n[m]=='m':
        t4=t4+1
        
        
print("a=",t1)
print("s=",t2)
print("e=",t3)
print("m=",t4)




print("""mon\ttue\twed\tthur\tfri\tsat\tsun""")
for d in range(31):




a=input("Enter your name\n")
print(a)
print(type(a))    
print(len(a))


print(f"\nHello,{a}")
print("hello,{}".format(a))



x=2

def f1():
    x=5
    print(x)
f1()
print(x)




name='abc'
if 'a' in name:
    print("a is present")
else:
    print("not present")
    
    
    
n1=[1,2,3]
n2=[1,2,3]
if n1==n2:
    print("n1=n2")
else:
    print("not equal")
    
    
    
    
n1=[1,2,3]
n2=[1,2,3]
if n1 is n2:
    print("n1=n2")
else:
    print("not equal")






l1=[1,2,3,4]
print(l1)

for i in l1:
    print(i)
    


l1.append('a')
print(l1)


l1.insert(1,'b')
print(l1)

l2=[243,54,7853]

l1.extend(l2)
print(l1)

l1.pop()
print(l1)

l1.pop(3)
print(l1)



l1.remove(243)
print(l1)




l4=[543,768,678,123,1,2,3,3,3,3,3,4]
print(l4)
#del(l4)
print(l4)


del l4[0]
print(l4)


l4.sort()
print(l4)



l4.sort(reverse=True)
print(l4)


l4.count(3)

l5=['dog','tiger','egarhda','sdf']
l5.sort()
print(l5)

print(min(l5))
print(max(l5))



t1=(1,2,423,573,2,12,435,'c')

del t1()
t1.sort()
print(t1)

t2=(423,531,745)
t3=(t2,t1)
print(t3)


t2.extend(t1)
t2.__len__()

s={32,4632,2347,75623,5428,2,4,149,67,32,2}
print(s)

s.add(543)

s1={43,542,89723,79,21,724,967,51}

s.union(s1)


d={'somnath':53453,'samac':3242}
print(d)

d.get('samac')
print(d['somnath'])
d2=dict(d)
print(d2)
d2.keys()
d2.values()


d2.clear()
print(d2)



a=[1,2,3]
b=[i*2 for i in a]
print(b)


c={i:i**2 for i in a}
print(c)


t={i:i*3 for i in t2}
print(t)


s6={i:i*3 for i in s}
print(s6)