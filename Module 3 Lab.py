'''
Car Classes
Zachary Rosch

This program accepts a users inputs that discribe a vechicle and
    makes a new car object with those inputs. For this project it
    is assumed a car is the selected vehicle type.

'''



class Vehicle:

    def __init__(self,type):
        self.type = type

class Automobile(Vehicle):

    def __init__(self, type,year,make,model,doors,roof):
        super().__init__(type)
        try:
            self.year = year
            self.make = make
            self.model = model
            self.doors = doors
            self.roof = roof
        except:
            print("Something went wrong.")
    
    def __str__(self):
        return f"Car detials- \n Vehicle type:{self.type} \n Year:{self.year} \n Make:{self.make} \n Model:{self.model} \n Number of doors:{self.doors} \n Roof Type:{self.roof}"
    

Car = Automobile(
                 str(input("Input the type :")),
                 int(input("Input the year :")),
                 str(input("Input the make :")),
                 str(input("input the model :")),
                 int(input("Input the number of doors :")),
                 str(input("Input the roof type :"))
                 )

print(Car)
