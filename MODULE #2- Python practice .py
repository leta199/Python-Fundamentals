#COMPUND DATA TYPES
---------------------------------------------------------
#TUPLES- compound data types with brackets (immutbale)
---------------------------------------------------------
tuple=(1,3,2,5,4,6,7)
print("Tuple is:", tuple) #Prints "Tuples is" follwed by tuple objet elements
print(type(tuple))

#INDEXING- similar to strings from 0-infinity or -1 to infinity 
print(tuple[-1])# =7
print(tuple[0]) #=1

#CONCATENATE- adds more onto tuples 
tuple2=("Avery", "Bradley", "Samantha")
print(tuple2) 

tuple_conc=tuple+tuple2
print(tuple_conc) #Prints the elements of tuple1 and tuple2 addedtogether 

#SORTED-sorts tuples
tuple_sort=sorted(tuple)
print(tuple_sort)

#NESTING- having tuples and lists inisde yout tuple
nestedtuple=(8,9,10,("warhammer","attack"),11,12)
print(nestedtuple)

print(nestedtuple[3][1]) #prints out only attack from tuple index 3

---------------------------------------------------------
#LISTS- ordered sequence in sqaure brackets (mutable) 
---------------------------------------------------------
list=["Atang", "Brett", "Cummingham"]
print(list[0:3]) #Prints elements 1 to 2
print(list[-1]) #Prints last elements in list 

#CONCATENATE
list2=["Santiago","Micca","Ephraim"]
print(list2)
list_conc=list+list2
print(list_conc) 

-----------------------------------------------------------------------------
#LIST METHODS- Mutable objects have operations called methods to change them
#EXTEND- adds elements, list grows by no of elements >1

list_conc.extend(["Tabitha","James","Letlhabula"])
print(list_conc) #Prints list_con elements plus elements called in method 
print(list_conc[-1]) #Letlhabula 

#APPEND- adds elements, list grows by 1
list.append(["Jesus", "Zeus"])
print(list)
print(list[-1]) #Prints "Jesus", "Zeus"


#CHANGING LISTS- changing out elements in a list
#Adding elements 

list[2]="Game"
print(list) #Changes last element to Game 

#Deleting elements
del(list[0]) 
print(list) #Removes first item in list 

#SPLIT- splits a string into a list
print("Bakwena,Baruti,Mongwato,Ross".split())

#ALIASING- multiple names for the same list 
A=['rock','jazz','amapiano','reggaeton']
B=A 
print(B, "Is equal to", A) #A and B are the same list 

A[1]="pop"
print(A)
print(B) #Both lists are changed by change to one 

#CLONE
A2=[1,2,3,4,5,6]
B=A2[:] #B is clone of A 
print(A2)
print(B)
B.extend([7,8,9]) #B is changed but A does not change 
print(B)

---------------------------------------------------------
#DICTIONARIES- type of collection using keys-value pairs 
---------------------------------------------------------
dictionary1={"Name1":"Atang","Name2":"Geoffrey","Name3":"Ayanda"}
print(dictionary1)

dictionary1["Name4"]="Mmoloki"
print(dictionary1) #Adds new key-value pair to dictionary 

---------------------------------------------------------
#DICTIONARY METHODS

#DELETE- deletes the key of dictionary 
del(dictionary1["Name1"])
print(dictionary1) 
print("Name4" in dictionary1)

#KEYES
print(dictionary1.keys()) #Prints all the keys of a dictionary

---------------------------------------------------------
#SETS-  type of unordered collection with curly brackets 
---------------------------------------------------------
set1={"opera","musical","theatre","classical", "operetta", "operetta"}
print(set1)

#List into set- makes sure there are no duplicates
listtoset=["Michael","Sohyang","Whitney"]
list_to_set=set(listtoset)
print(list_to_set)

---------------------------------------------------------
#SET METHODS
#ADD- adds elements to exixstong list 
set1.add("pop")
print(set1) 

#REMOVE- removes elements to existing list 
set1.remove("pop")
print(set1)

#IN- check if element in set 
print("pop" in set1)

#DIFFERENCE- checks to see the difference in elements between sets
set2={"opera","operetta","live","choir","acoustic"}
print(set1.difference(set2))

---------------------------------------------------------
#MATHEMATICAL OPERATIONS 
#AND- used to unify elements present in mulitple sets, like intersection 
set_unify=set1 & set2
print(set_unify)

#UNION- combines elements in either 1 or both sets
print(set1.union(set2))

#SUBSETS
#Is subset- tells you if 1 set is subset of another 
print(set1.issubset(set2))

set3={"operetta","musical"}
print(set3.issubset(set1))

#SUPERSETS- tells you if 1 set is superset of another
print(set1.issuperset(set3))

