Phython
# let wee see methods of list
#append()
emp=['priya','vibisha','tamil','ayyapan','prakash']
# now need to add new emplyee prakash and ram
#emp.append()#its aacept one argument only 
new_emp=['prakash','ram']
emp.append(new_emp)
print(emp)
# now need to terminate all emplyess
#emp.clear()
print(emp)
#list.copy()
exela=emp.copy()
print(exela)
# how many prakash are there in your company
numberof_persons=emp.count('prakash')
print(numberof_persons)# it will considered another list
# we need to increase your emplyee count how we will do that
new_emplyees=['nandhini','akash','robo','srimathi']
new_memebers=emp.extend(new_emplyees)
print(new_memebers)# none  its woun't stored any value
print(emp)
# i need to find prakash rank or place where he was there ?
seatno=emp.index('prakash')
print(seatno)
# i want to sit place 4 for robo instead of prakash
emp.insert(4,'robo')
print(emp.index('robo'))
print(emp.index('prakash'))
print(emp)
# list like array starts from 0 ,2..
# i want to remove seat no 7
print(emp.pop(7))# its returns value 
# i needed to fire vibisha
emp.remove('vibisha')
print(emp)
# i want to prapere reverse
emp.reverse()
print(emp)
# now we want discuss about important fucntion 
"""Note: A list also has the sort() method which performs the same way as sorted(). The only difference is that the sort() method doesn't return any value and changes the original list."""
# i want to prapere list asc order by name 
#list.sort(reverse=True|False, key=myFunc)
def orderbynamelen(emp):
    return len(emp)
# i means enga namma nameoda len vachi asc print pannumnu soldrom
emp.sort(key=orderbynamelen)
print(emp)
emp.sort(key=orderbynamelen,reverse=True)
print(emp)
# we can use dic
tcs=[
    {'name':'prakash','age':22,'skills':'fullstack','exp':1},
     {'name':'prakash','age':30,'skills':'fullstack','exp':1},
      {'name':'prakash','age':28,'skills':'fullstack','exp':1},
       {'name':'prakash','age':27,'skills':'fullstack','exp':1},
    ]
print(tcs)    
tcs.sort(key=lambda argumentofdic:argumentofdic.get('age'),reverse=True)  
print(tcs)



# now let wee see tuples 
emplyees=('prakash','akash','ram','uday','ganesh','prakash')
print(type(emplyees))
# we cant modified anything so we only reterive the values so its has onlky two functions 
print(emplyees.count('prakash'))
print(emplyees.index('prakash'))

# let wee seee sets
ipl={'csk','mi','rcb','kkr'}
# its unorderedd and not allowed duplicate 
# how u will add new team frozenset([1,2,3,4,5])   frozen sets its like tuppesls etha edit panna mudiyathu + duplicates allow pannathu 
# how u will add new team
ipl.add('cheyyarsuperkings')
print(ipl)
#ipl.clear()
#kpl=ipl.copy()
kpl={'csk','mi','rcb','kkr','pk','ol','pkkkkllk','jdjjshdud','huhdehdeuhdeudhd','hhduehduedh'}
# kpl la india teams eppadi find pannuva
print(ipl.intersection(kpl))
# how u will update
#ipl.intersection_update(kpl) ethu update panni vittrum
# eppadi rendum team onnu seppa without dupliated
print(ipl.union(kpl))
# eppadi join pannjuva  without  duplicates\
print(ipl.update(kpl)) # updatedmeans its no returns
print(ipl)
#To add more than one item in the set, Python provides the update() method. It accepts iterable as an argument.
# union and update both are same union returen the value update its not returned its updated value
z = ipl.difference(kpl)# ipl ellathu ethu 2 nadla erukku so ethu etha call pandroma atha vachi than differ pakkum
print(z)

#ipl.difference_update(kpl)

print(ipl)
#Despite the fact that discard() and remove() method both perform the same task, There is one main difference between discard() and remove().

#If the key to be deleted from the set using discard() doesn't exist in the set, the Python will not give the error. The program maintains its control flow.
# rendu teamkum common na ethum ellana treu apdi common ethana onnu eruntha koda flase return pannu
z = ipl.isdisjoint(kpl)
print(z)
print(ipl.pop())# no argument list la arugument tharuvom athu order ethu un un oreder so ethu remove pannumna solla mudiyathu

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issuperset(y) #or we can write x>y(meanssuperset) orx<y(means y is supoer setta) or x==y both are samma  
print(z)
# ethu intersection ku oppsite common na erukaratha delete pannidum 
x = {"apple", "banana", "cherry","koyya"}
y = {"cherry", "banana", "apple"}

z = x.symmetric_difference(y) # first ethu call pannutho athulatha refelect agum ethu return than update pannathu athukku oru fuction erukku 

print(z)
x.symmetric_difference_update(y)

print(x)

# as end most of functions diffrence selathu return pannum selathu return pannathu athan main diffrent 
# how u will create dic
dic={}
print(type(dic))
n={1:'prakash',2:'pallavi'}
print(n)
#dict() --constctor
d=dict((['prakash',22],['pallavi',28])) # accept only one argument
e=dict({'name':'priya','status':'married'})
print(e)
# how u will access 
#1.key 
print(n[1])
print(n.get(1))
print('name : %s'%e['name'])
# how add or update 
# 1.key 
n[1]='robo'
print(n)
n[5]='coll' # if key its not present it will create  or added 
print(n)
del n[1]
print(n)
#del n
# print(n)
#pop(key)
n.pop(2)
print(n)
# how u will iterating its important 
# values itesm keys items(),values(),keys()
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
for x in Employee.values():
    print(x)

for x in Employee.keys():
    print(x)
for x in Employee.items():
    print(x)

for x,y in Employee.items():
    print(x,y)
#functions
#Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE",[100,201,301]:"Department ID"} # only tupples alloed  
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE",(100,201,301):"Department ID"} # only tupples alloed    
for x,y in Employee.items():      
    print(x,y)    
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)
x = car.copy()

print(x)
x = ('pallavi', 'nazriya', 'madahna')
y = 'pk'

thisdict = dict.fromkeys(x, y)

print(thisdict)
# get (key) u know thsat pop (key) ,popiteam()no arguments its re,ove last inserted keyvalues pair update() new car.update({"color": "White"}) The setdefault() method returns the value of the item with the specified key.

#If the key does not exist, insert the key, with the specified value, see example below
car = {
  "brand": "Ford",
 
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(car)



# function 
#Pass by Reference vs. Pass by Value
#All parameters in the Python programming language are provided by reference. It indicates that if we alter the value of an argument inside of a function, the calling function will likewise reflect the change. For example,

# calculate square of elemets
def square(ard):
    for i in ard:
        s=[]
        s.append(i**2)
    return s
     
     
numbers=[2,6,7,8,9,100]  
square(numbers)
print(square)# its prints function refrence or memeory addres
sq=square(numbers)
print(sq)
# see that diffrence 
# calculate square of elemets
def square(ard):
    s=[]
    for i in ard:
        
        s.append(i*2)
    return s
     
     
numbers=[2,6,7,8,9,100]  
square(numbers)
print(square)# its prints function refrence or memeory addres
sq=square(numbers)
print(sq)
#def function( n1, n2 = 20 ):  default ardguments
#function( n2 = 50, n1 = 30)    keyword arguments def function( n1, n2 ):    
#3) Required Arguments number supplies arg == number of parameters
#4) Variable-Length Arguments
#*args -These are Non-Keyword Arguments  -- list 
#**kwargs -These are Keyword Arguments. -- dictionary pass key value 
def function( *args_list ):    
    ans = []    
    for l in args_list:    
        ans.append( l.upper() )    
    return ans    
# Passing args arguments    
object = function('Python', 'Functions', 'tutorial')    
print( object )  

def function( **kargs_list ):    
    ans = []    
    for key, value in kargs_list.items():    
        ans.append([key, value])    
    return ans    
# Paasing kwargs arguments    
object = function(First = "Python", Second = "Functions", Third = "Tutorial")    
print(object)    
# inline function
# Python code to show how to access variables of a nested functions    
# defining a nested function    
def word():    
    string = 'Python functions tutorial'    
    x = 5     
    def number():    
        print( string )   
        print( x )  
             
    number()    
word()    
#lambda [argument1 [,argument2... .argumentn]] : expression    
# its accept n number of expression but return single value
# function name = lamda x,y,z=x+y+z
hello=lambda x,y:x+y
print(hello('prakash','nazriya'))
# local and global variable inisde and outside function
 1.)how we can swap two numbers 
 number1=int(input('please enter a number 1:'))
 number2=int(input('please enter a number 2:'))
 print('before swapping those numbers1 is{} and number2 is {} '.format(number1,number2))
 number2,number1=number1,number2
 print('after swapping those numbers1 is{} and number2 is {} '.format(number1,number2))
 2.)how to find prime number or not 
 logic :: a number should greater than 1 and number divide by 1 and itself it only callded prime number 
   
numb=lambda x=int(input("please enter a number:")): True if x>0 else False
 def prime():
    number=int(input('hello user please enter your number :'))
    counter=0
    if number>1:
      for i in range(1,number,1):
         if number%2==0:
             counter+=1
      if counter==2 or counter>=2:
         print("your entred number {} is prime number ".format(number))    
      else:
         print("sorry your number its not a prime dude")        
   
 prime ()
 how to find factouirals of given number 
 logic 0 or 1 factorials is 1 i mean 5 na 5*4*3*2*1 =120
 num=int(input('please enter your number :'))
 def fact():
     if num==0 or num==1:
         return 1
     elif num >0:
         n=1
         for i in range(1,num+1,1):
             n*=i
     return n        

 f=fact()
 print(f)
method recurion reverse 5 * 4 * 3 * 2 * 1 * 0
 num=int(input('please enter your number ::'))
 def fact(num):
     if num==0:
         return 1
     return num * fact(num-1)
 o=fact(num)
 print(o)
 ternary operator 
 def fact(num):
  return 1 if (num==0 or num==1) else num * fact(num-1)
 fibinaci series means add two preceeding number before number 
  0 1 1 2 3 5 8 13 ... n=how many elements u wants 
elemts=int(input('how many elements do u want print :'))
 def fibi(elemts):
     n1,n2=0,1
     print(n1)
     print(n2)
     for i in range(2,elemts,1):
         sum=n1+n2
         # 0 1 0+1(sum)
         print(sum)
         n1=n2
         n2=sum
 fibi(10)        
    




    

