class Person: 
 def __init__(self, name, age): 
    self.name = name 
    self.age = age 
 def displayData(self): 
    print('In parent class displayData method') 
    print(self.name) 
    print(self.age) 
    

class Employee(Person): 
 def __init__(self, name, age, id): 
 # calling constructor of super class 
    super().__init__(name, age) 
    self.empId = id 
 def displayData(self): 
    print('In child class displayData method') 
    print(self.name) 
    print(self.age) 
    print(self.empId)


#Person class object 
person = Person('MANDALEEKA AVSS VIGHNESH', 20) 
person.displayData() 
#Employee class object 
emp = Employee('MANALEEKA AVSS VIGHNESH',20,"21026A0511") 
emp.displayData() 