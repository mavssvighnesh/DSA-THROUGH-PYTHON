from abc import abstractmethod, ABCMeta 
import math 

class Polygon(metaclass = ABCMeta): 
 def __init__(self, side_lengths = [1,1,1], num_sides = 3): 
    self._side_lengths = side_lengths 
    self._num_sizes = 3 
    
 
 @abstractmethod 
 def area(self): 
    pass 
 
 
 @abstractmethod 
 def perimeter(self): 
    pass 
 
 
 def __repr__(self): 
    return (str(self._side_lengths)) 
 
 
 
class Triangle(Polygon): 
 def __init__(self, side_lengths): 
    super().__init__(side_lengths, 3) 
    self._perimeter = self.perimeter() 
    self._area = self.area() 

 
 
 def perimeter(self): 
    return(sum(self._side_lengths)) 
 
 
 def area(self): 
    #Area of Triangle 
    s = self._perimeter/2 
    product = s 
    for i in self._side_lengths: 
        product*=(s-i) 
    return product**0.5 
 
 
class Quadrilateral(Polygon): 
 def __init__(self, side_lengths): 
    super().__init__(side_lengths, 4) 
    self._perimeter = self.perimeter() 
    self._area = self.area() 

 
 
 def perimeter(self): 
     return(sum(self._side_lengths)) 
 
 
 def area(self): 
     # Area of an irregular Quadrilateral 
    semiperimeter = sum(self._side_lengths) / 2 
    return math.sqrt((semiperimeter - self._side_lengths[0]) * 
    (semiperimeter - self._side_lengths[1]) * 
    (semiperimeter - self._side_lengths[2]) * 
    (semiperimeter - self._side_lengths[3])) 
class Pentagon(Polygon): 
 def __init__(self, side_lengths): 
    super().__init__(side_lengths, 5) 
    self._perimeter = self.perimeter() 
    self._area = self.area() 
 
 def perimeter(self): 
    return((self._side_lengths) * 5) 
 
 def area(self): 
 # Area of a regular Pentagon 
  a = self._side_lengths 
  return (math.sqrt(5 * (5 + 2 * (math.sqrt(5)))) * a * a) / 4 
 


#object of Triangle 
t1 = Triangle([1,2,2]) 
print("perimeter of triangle: ",t1.perimeter()   ,"Area of triangle: ",t1.area()) 
#object of Quadrilateral 
q1 = Quadrilateral([1,1,1,1]) 
print("perimeter of Quadrilateral: ",q1.perimeter()   ,"Area of Quadrilateral: ",q1.area()) 
#object of Pentagon 
p1 = Pentagon(1) 
print("perimeter of  Pentagon : ",p1.perimeter()   ,"Area of Pentagon: ",p1.area()) 