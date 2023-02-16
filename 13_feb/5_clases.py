class Phone:
    def __init__(self,color="black",price=7000):
        self.color=color
        self.price=price
    def display(self):
        print("phone color is",self.color)
        print("phone price is",self.price)
        
    
class  Students:
    def __init__(self,age=21 ,gender='female'):
        self.age=age
        self.gender=gender
    def intro(self):   
        print("sanya's age",self.age)
        print("sanya's gender",self.gender)


class User:
    def __init__(self,f_name="sanya",l_name="arora"):
        self.f_name=f_name
        self.l_name=l_name
    def details(self):    
         print("first name",self.f_name)
         print("last name",self.l_name)


class Country:    
    def __init__(self,country1="INDIA",country2="CANADA" ):
        self.country1=country1
        self.country2=country2
    def show(self): 
        print("my fav country is ",self.country1)
        print("my dream country is ",self.country2)  


class Rectangle:
    def __init__(self, length=10,breadth=20 ):
        self.length=length
        self.breadth=breadth
    def area(self):
         print("area of reactangle is ",self.length*self.breadth)  

        

ph=Phone()
ph.display()
stu=Students()
stu.intro()
user_obj=User()
user_obj.details()
obj=Country()
obj.show()               
rect_obj=Rectangle()
rect_obj.area()

