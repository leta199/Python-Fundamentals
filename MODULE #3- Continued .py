----------------------------------------------------------------------------------------------------------------------------------
#TYPES/ CLASSES IN PYTHON- have data attributes and methods
----------------------------------------------------------------------------------------------------------------------------------
#DATA ATTIRBUTES- defines what variables each object requires

class Rectangle(object): 
    def __init__ (self, height,width,colour): #__init__ constructor-  with type attirbutes always begin with (self) 
        self.height=height
        self.width=width
        self.colour=colour # instance  attributes of your type for each objects
        
redRectangle=Rectangle(1,2,"red")  #a rectangle with height= 1, width= 2 and colour= "red"  

#Peering into an instance/ object 
print(redRectangle.height) #returns instance height attributes 
print(redRectangle.width)  #returns instance height attributes 
print(redRectangle.colour) #returns instance height attributes

#Changing an object - requires methods to change existing object
redRectangle.height="2"
print(redRectangle.height) #new redrecatngle  height= 2

----------------------------------------------------------------------------------------------------------
#METHODS- defines actions that can be done on each object of a type form of functions 
class Rectangle(object):
    def __init__ (self, height,width,colour): 
        self.height=height
        self.width=width
        self.colour=colour
    def add_height(self,h):
        self.height=self.height + h #adds parameter h to the height of an already existing object
    def add_width(self,w):
        self.width=self.width + w #adds parameter w to width of object 
  

rr=Rectangle(1,2,"red")

--------------------------------------------------------------------------
#DIR Function- prints all attributes and methods available to an object
--------------------------------------------------------------------------
print(dir(rr)) 

--------------------------------------------------------------------------
#Calling methods
#Dot notation- object_to_be_altered.method_applied(parameters)
rr.add_height(2)
print(rr.height)

#Assign to variables- assign the object with mehod to variable and use variable to (change_h) create new object with it
change_h=rr.add_height
rr2=change_h(1)
print(rr.height)





