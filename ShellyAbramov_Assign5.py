#Name: Shelly Abramov
#Assignment 5
#Date: 11/27/24
#Description: I am working with objcets, classes, encapsulation, inheritance, and polymorphism

#1. Car Class
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    #Getter methods
    def get_year_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make
    
    def get_speed(self):
        return self.__speed
    
    #Methods for accelerating and braking
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    
    #Setter methods
    def set_year_model(self, year_model):
        self.__year_model = year_model
        
    def set_make(self, make):
        self.__make = make
        
    def set_speed(self, speed):
        self.__speed = speed
    def __str__(self):
        return f'Year Model: {self.get_year_model()}, Make: {self.get_make()}, Speed:{self.get_speed()}'


#################################################################
#2. Employee Class
class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
    #Getter methods
    def get_name(self):
        return self.__name
        
    def get_id_number(self):
        return self.__id_number
        
    def get_department(self):
        return self.__department
        
    def get_job_title(self):
        return self.__job_title
        
    #Setter methods
    def set_name(self, name):
        self.__name = name
            
    def set_id_number(self, id_number):
        self.__id_number = id_number
            
    def set_department(self, department):
        self.__department = department
            
    def set_job_title(self, job_title):
        self.__job_title = job_title

    def __str__(self):
        return f'Name: {self.get_name()}, ID Number: {self.get_id_number()}, Department: {self.get_department()}, Job Title: {self.get_job_title()}'
################################################################
#3. Employee and ProductionWorker Classes
class EmployeeNew:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number
    
    #getter methods
    def get_name(self):
        return self.__name
        
    def get_id_number(self):
        return self.__id_number
    
    #setter methods
    def set_name(self, name):
        self.__name = name
            
    def set_id_number(self, id_number):
        self.__id_number = id_number
    

class ProductionWorker(EmployeeNew):
    def __init__(self, name, id_number, shift, hourly_pay_rate):
        EmployeeNew.__init__(self, name, id_number)
        self.__shift = shift
        self.__hourly_pay_rate = hourly_pay_rate

        if shift == 2:
            self.__hourly_pay_rate = hourly_pay_rate * 1.5
        else:
            self.__hourly_pay_rate = hourly_pay_rate
            
        
    def get_shift(self):
        return self.__shift
    
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def set_shift(self,shift):
        self.__shift = shift
        
    def set_hourly_pay_rate(self, hourly_pay_rate):
        
        self.__hourly_pay_rate = hourly_pay_rate
##        if shift == 2:
##            self.__hourly_pay_rate = hourly_pay_rate*1.5
##        else:
##            self.__hourly_pay_rate = hourly_pay_rate

    def __str__(self):
        return f'Employee name: {self.get_name()}, ID Number: {self.get_id_number()}, Shift: {self.get_shift()}, Hourly Pay Rate: {self.get_hourly_pay_rate()}'
        
    
def main():
    #1 Car Class
    car1 = Car(2022, 'Toyota')
    
    for i in range(5): 
        car1.accelerate()
        print(f'The speed after accelerating: {car1.get_speed()}')
    for i in range(5):
        car1.brake()
        print(f'The speed after braking is: {car1.get_speed()}')
    print(car1)
    print()
############################################################################################
    #2 Employee Class
    #These are instances of the data
    employee1 = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    print(employee1)
    employee2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')
    print(employee2)
    employee3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')
    print(employee3)
    print()
#############################################################################################
    #3 Employee and ProductionWorker Class
    name = input("Enter employee name: ")
    id_number = input("Enter employee ID number: ")
    shift = int(input("Please enter shift type (1 for day, 2 for night): "))
    hourly_pay_rate = float(input("Please enter hourly pay rate: "))

    worker1 = ProductionWorker(name, id_number, shift, hourly_pay_rate)

    print(worker1)
            
main()
      
        
    
        
        
    
