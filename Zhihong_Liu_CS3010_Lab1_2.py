'''class Car():
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
from Zhihong_Liu_CS3010_Lab1_1 import Car 


class Garage():

     carList=list()


    
     def __init__(self):
         self.carList=[]

     def get_list(self):
         return self.carList
    

     def load_cars(self):
       file_path = r"F:\电子书\CS3010\Assignment backup\Assignment1\file.txt"

       try:  
         with open(file_path, 'r') as file:  # Open the file for reading  
             for line in file:  # Read each line in the file  
                # Strip any leading/trailing whitespace and split by commas  
                 attributes = line.strip().split(', ')
                
                 tempList=list() #Store the attribute information

                 for item in attributes:
                    key, value = item.split(': ')
                    tempList.append(value)

                
                 self.carList.append(Car(tempList[0],tempList[1],int(tempList[2]),int(tempList[3])))

                


       except FileNotFoundError:  
         print(f"The file {file_path} was not found.")  
       except Exception as e:  
         print(f"An error occurred: {e}")  

     def list_all(self):
          for car in self.carList:
              print(car.get_details())
              print()




def main():
    garage1=Garage()
    garage1.load_cars()
    garage1.list_all()

    print("Stat information printing : ")
    print()

    for car in garage1.get_list():
        if(car.get_CC()>800):
            print(car.get_details())
            print()




main()
