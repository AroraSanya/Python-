# single inheritance

class Brand:
    def __init__(self,name):
        self.name=name
    def display(self):
        return self.name
class Product(Brand):
    def __init__(self,name,product_name):
        Brand.__init__(self,name)
        self.product_name=product_name
    def __str__(self):
        return self.product_name
      
p1=Product("GUCCI","T_SHIRT")     
print(p1)  
print(p1.display())


# # multiple inheritance

# class calculator1:
#     def __init__(self,a):
#         self.a=a
#         # self.b=b
#     def __mul__(self,other):
#         return calculator1(self.a*other.a)
# c1=calculator1(3)        
# c2=calculator1(2)
# print(c1*c2)

class Calculator1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def mul(self):
        return self.a*self.b

class Calculator2:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b   

class Calculator3(Calculator1,Calculator2):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sub(self):
        return self.a-self.b     
c3=Calculator3(4,5)
print(c3.mul())
print(c3.add()) 
print(c3.sub()) 
              
         

#multilevel inheritence
class GrandParent:
    def head(self):
        return "head of the family"
class Parent(GrandParent):
    def show(self):
        return " secondary head of the family"
class Child(Parent):
    def display(self):
        return" i am cute child" 
c1=Child()
print(c1.head())
print(c1.show())
print(c1.display())

#multilevel

class GrandDog:
    def head(self):
        return "head of the Dog family"
class ParentDog(GrandDog):
    def show(self):
        return " secondary head of the Dog family"
class ChildDog(ParentDog):
    def display(self):
        return" i am cute puppy" 
c1=ChildDog()
print(c1.head())
print(c1.show())
print(c1.display())

#multiple

class Dad():
	def singing(self):
		print("Dad sings well")
		

class Mom():
	def coding(self):
		print("Mom codes well")

class Child(Dad, Mom):
	def play(self):
		print("Kid loves to play")

child = Child()
child.singing()
child.coding()
child.play()	