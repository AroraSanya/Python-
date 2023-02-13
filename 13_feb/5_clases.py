class phone:
    color="black"
    cost=70000
    def play_game(self):
        print("phone color is",self.color)
        print("phone cost is",self.cost)

class  students:
    age=21
    gender='female'       
    def dance(self):
        print("sanya's age",self.age)
        print("sanya's gender",self.gender)

class user:
    f_name="sanya"
    l_name="arora"
    def details(self):
         print("first name",self.f_name)
         print("last name",self.l_name)

class country:
    country1="INDIA"
    country2="CANADA"     
    def show(self):
        print("my fav country is ",self.country1)
        print("my dream country is ",self.country2)  


 
class rectangle:
    length=10
    breadth=20 
    def area(self):
         print("area of reactangle is ",self.length*self.breadth)  

        




        

       
ph=phone()
ph.play_game()
stu=students()
stu.dance()
userobj=user()
userobj.details()  
cont_obj=country()  
cont_obj.show()
rect_obj=rectangle()
rect_obj.area()

