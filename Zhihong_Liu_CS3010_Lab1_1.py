class Car():
    brand=" "
    make=" "
    horsepower=0
    CC=0

    
    def __init__(self,brand,make,horsepower=0,CC=0):
        self.brand=brand
        self.make=make
        self.horsepower=horsepower
        self.CC=CC

    def get_brand(self):
        return self.brand

    def get_make(self):
        return self.make

    def get_horsepower(self):
        return self.horsepower

    def get_CC(self):
        return self.CC

    def set_brand(self,brand):
        self.brand=brand

    def set_make(self,make):
        self.make=make

    def set_horsepower(self,horsepower):
        self.horsepower=horsepower

    def set_CC(self,CC):
        self.CC=CC

    def get_details(self):
        return self.brand+"-"+self.make+"\n"+str(self.horsepower)+"HP("+str(self.CC)+"cc"+")"





'''

def main():
    car1=Car("Porsche", "Cayenne", 350, 1000)
    print(car1.get_brand())
    print(car1.get_make())
    print(car1.get_horsepower())
    print(car1.get_CC())

    car1.set_brand("Benz")
    car1.set_make("manufacturer")
    car1.set_horsepower(400)
    car1.set_CC(1500)

    print(car1.get_brand())
    print(car1.get_make())
    print(car1.get_horsepower())
    print(car1.get_CC())

    print(car1.get_details())




main()'''
