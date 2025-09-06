#CONDITIONS, BRANCHING,LOOPS & FUNCTION CREATION
--------------------------------------------------------------
#CONDITIONS AND BRANCHING
--------------------------------------------------------------

#COMPARISON OPERATORS
a=6
print(a==7) #False 

#EXCLAMATION MARK- eqautes to "not"
b=9
print(a==b)
print(a!=b)

--------------------------------------------------------------
#BRANCHING- runs different staments for different inputs
--------------------------------------------------------------

#IF STATEMENTS- checks if criteria are met and exceutes code block 
age= 19
if(age>18):
    print(f"{age} years old is too old to enter") #indentation is very important for Python 
    print("Proceed to other option")


#ELSE STATEMENT- runs only if first conditon is false 
password= "Cadburyman"
if (password== "Cadburyman"):
    print("Correct user detected")
else:
    print("Incorrect password")

print("Move on")

--------------------------------------------------------------
#LOGIC OPERATORS
#NOT
print(not(True)) #False

#OR 
albumyr=1998
albumname="Adore"

if (albumyr>=1990) or (albumyr<2000):
    print(f"{albumname} is a 90s bop")

else:
    print("Not a 90s bop unfortunately")
    print("Unknown date period")

#AND
if (albumyr>=1990) and (albumyr<2010):
    print(f"The album: {albumname} is a classic")
else:
    print("This is not a classic")

----------------------------------------------------------------------------
#LOOPS- repeat instructions as many times as specified in function
----------------------------------------------------------------------------

#FOR LOOPS- repeats code for item in a sequence e.g a list or range
    
for number in range(1,11): #Range- outputs the numbers in sequence from 0 to n-1 
     print(number)

squares=["white","blue","white","white","white"]

for i in range(0,5): # 
    squares[1]="white"

print(squares)

squares2=["white","black","indigo","purple"]
print(squares2)

for i in range(0,5):
    squares2[0]="white"
print(squares2)

for i,square in enumerate(squares2): #Enumerate- used to obtain index and element in a list
    print(f"{i}:{square}")           #format strings 


#WHILE LOOPS- only iterate when a condition is true
circles=["black","black","black","indigo","black","orange","black"]
newcircles=[]
i=0

while(circles[i]=="black"):         #Adds all black squares to new list 
    newcircles.append(circles[i])
    i=i+1
print(newcircles)
print(len(newcircles)) #5 

-----------------------------------------------------------------------------
#FUNCTIONS - repeatble blocks of code 
#Built in functions
#Len- get length of a argument

l=[1,2,3,4,5,6]
print(len(l))

#Sum- total of all elements
print(sum(l))

#Sorted- general function and creates new instance of 
l2=[3,4,6,8,2,6]
newl=sorted(l2)
print(newl)

#Min- gives min value in sequence  
lowestl2=min(l2)
print(lowestl2)

#Max- gives min value in sequence  
highestl2=max(l2)
print(highestl2)

#Concatenate- adds togther two sequences 
l3=l+l2
print(l3)

#Sort- is a method and modifies the object
l2.sort()
print(l2)

----------------------------------------------------------------------------
#MAKING FUNCTIONS
----------------------------------------------------------------------------
#Creating your own blocks of re-runable code

def add1(a):   #def- keyword to declare own function 
    """
    add 1 to a
    """
    b=a+1      #actual code block to run 
    return b   # return statemnt for output 

print(add1(6)) 

def mult(a,b):
    c=a*b
    return c

x=mult(3,"Michael Jackson")
print(x)       #returns :Michael Jackson" 3 times 

----------------------------------------------
#Functions  without a return statement 
def MJ():
    print("Michael Jackson")
MJ()          #returns orint statement

----------------------------------------------------------
#Functions with an empty body
def NoWork():
    pass
print(NoWork()) 

NoWork() #prints value of None when using pass function

-----------------------------------------
#Functions with multiple lines of code
def add1(a):
    b=a+1
    print(a,"plus 1 equals", b)
    return b
add1(5)

-----------------------------------------------------------------
#Functions with loops
def summ(a,b):
    ssum= 0
    for i in range(a,b+1): #goes over range to add each iteratively 
        ssum+=i
    print(f"The summation of values from {a} to {b} is:{ssum}")

summ(1,3)                 #adds together values from 2 to 6 inclusive
summ(2,6)                 #adds together values from 2 to 6 inclusive 

def print_family(x):
    for i,s in enumerate(x):
        
        print("The value of", s , " in the index is:", i+1)

family_tree=["JB","Mama","Daddy","Game","Atang","Ezekiel"]

print_family(family_tree)

---------------------------------------------------------------------
#Variadic parameters-multiple parameters defined in function input

def printnames(*names): #multiple parameters possible 
    for name in names:
        print("This is the list of names:",name)

Names=("MJ","Whitney","Zahara","VeeMampizi","Doctor Mokento")
printnames(Names)


def avg(*numbers):
    c=sum(numbers)/len(numbers)
    print("The average of you numbers is:", c)

avg(1,2,3,4,5,6,7,8)

-----------------------------------------------------------------
#SCOPE
-----------------------------------------------------------------
def ACDC(y):
    print(Rating)
    return(Rating+y)
Rating =9 #rating variable in local scope 

z=ACDC(1)
print(z)

def pinkFloyd():
    global ClaimedSales #claimedsales in global scope 
    ClaimedSales= "45 million"
    return ClaimedSales

#Counting words in a string:
def word_count(string):
    words=[]
    words=string.split() #separates the string into list and populates the words list
    Dict={}
    for key in words:
        Dict[key] = words.count(key) #counts each word in words list and populates dictionary with them 

    print("The frequency of words is:",Dict)

word_count("Malatsi otlhe ha ke bata go ja dijo ke ja dijo tsa Setswana tse di tlhakantsweng le tsa Sekgoa. Mme jaaka ke bonang ka teng, dijo tsone tsa Setswana di monate")
word_count("The itsy bitsy spider was crawling up the wall. Down came the rain and washed the spider out. Out came the sun and dried up all the rain and the itsy bitsy spider came crawling out again")
        

-------------------------------------------------------------------------------------------------------------------------------------     
#EXCEPTION HANDLING- were data is entered incorrectly but you want program to id and continue running regardless with error message
-------------------------------------------------------------------------------------------------------------------------------------

#Try/ Except Statements
try:
 words_combined=  "Hello world." + " It's me"
 print(words_combined)
 
except TypeError:
    print("This object is of an incompatible type with the function used")

else:
    print("Successful concatenation!")

try:
   x=100/1

except ZeroDivisionError:
    print("Dividing by zero in undefined.")

else:
    print("Expression complete.")

---------------------------------------------------------------------------------
#Functions and exception handling- def,try, (code block), except, else, finally 

def name_index(list):
        try:
            for i, tags in enumerate(list):
                print("The name of %s is employeed  number %d." %(tags,i))

        except TypeError:
            print("Please enter a list of empolyee names.")
        else:
            print("This is the number and name of each employee.")
        finally:
            print("Thank you.")
    
    
employees=["Alex","Lelentle","Bishop","Omogolo","Tinashe","Gosego"]
employees2=100/4
name_index(employees)






