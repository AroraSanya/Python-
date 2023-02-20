class Chocolate:

    def __init__(self, chocolate_type = None):
        self.chocolate_type = chocolate_type
    
    def check_flavour(self):
        chocolate_obj = self.chocolate_type()
        return "this choco is available in {} price's".format(chocolate_obj.price())

    def create_obj(self):
        return self.chocolate_type()

class Dairy_Milk:
    def price(self):
        return 4

class Munch:
    def price(self):
        return 2

class Barone:
    def price(self):
        return 3

if __name__ == "__main__":
    choco = Chocolate(Barone)
    munch =Chocolate(Munch)
    print(choco.check_flavour())
    print(munch.check_flavour())
    # print(tee.create_obj().colors())