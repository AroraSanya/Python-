class NetSolutions:
    def loc(self):
        return "CHANDIGARGH"
    
    def Emp(self):
        return "1000+"
    
    def Rating(self):
        return "*****"


class Infosys:
    def loc(self):
        return "PUNE"
    
    def Emp( self):
        return "2lakh+"
    
    def  Rating(self):
        return "*****"


class Microsoft:
    def loc(self):
        return "HYDERABAD"
    
    def Emp( self):
        return "3lakh+"
    
    def  Rating(self):
        return "*****"


class Amazon:
    def loc(self):
        return "GURUGRAM"
    
    def Emp( self):
        return "3lakh+"
    
    def  Rating(self):
        return "*****"   

class Jio:
    def loc(self):
        return "MUMBAI"
    
    def Emp( self):
        return "2lakh+"
    
    def  Rating(self):
        return "*****"        


class Airtle:
    def loc(self):
        return "CHANDIGARGH"
    
    def Emp( self):
        return "3lakh+"
    
    def  Rating(self):
        return "*****"     
def Factory(Rating="NetSolutions"):
   
    cls_dict = {
        "NetSolutions":NetSolutions(),
        "Infosys":Infosys(),
        "Microsoft":Microsoft(),
        "Amazon":Amazon(),
        "Jio":Jio(),
        "Airtle":Airtle()
    }
    return cls_dict[Rating]

for x in ["NetSolutions","Infosys","Microsoft", "Amazon","Jio", "Airtle"]:
    print(Factory(x).Emp())
    print(Factory(x).loc())
    print(Factory(x).Rating())
    print("---------------------------------")
   