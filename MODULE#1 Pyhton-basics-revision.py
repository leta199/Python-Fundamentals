
#LEARNING PYTHON BASICS 
-----------------------------------------
#Basic python syntax, functions and tools
-----------------------------------------

print(type(2.0) ) #float 
float(12.31) #12.31
int(12.103) #12

bool(1) #True 
bool(0) #False
-----------------------------------------
#Arithmetic (division with typing)
-----------------------------------------

12.3/3 #Division: returns float 
12.3//3  #Floor division: removes decimal and creates integer object 
27.9/3
27.9//3

type(27.3/4) #returns float  
type(27.3//3) #returns integer 

--------------------------------------
#Indexing and Striding 
--------------------------------------

Hello="Just saying hi."
print(Hello) #prints "Just saying hi."

Hello[0] #J
Hello[::2] # Reyrns ever second character 

#Striding index
Hello[0:6:2] #Characters 0 to 5 ever 2nd object 
Hello[0:5] #Prints characters 0 to to 4 

len(Hello) #length function- length of string

--------------------------------------
#Concatenate - combines multiple strings together
--------------------------------------

Con_String=Hello + "This is actually really fun!!"
print(Con_String) #Prints "Just saying hi. This is actually really fun!!"

con= Hello + "This is so fun!"
print(con) #Prints  "Just saing hi. This is really fun!"
