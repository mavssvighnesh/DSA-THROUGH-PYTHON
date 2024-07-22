class OverloadDemo: 
 # sum method with default as None for parameters 
 def sum(self, a=None, b=None, c=None): 
    # When three params are passed 
   if a!=None and b!=None and c!=None: 
     s = a + b + c 
     print('Sum = ', s) 

 # When two params are passed 
   elif a!=None and b!=None: 
    s = a + b 
    print('Sum = ', s) 


od = OverloadDemo() 
od.sum(7, 8) 
od.sum(7, 8, 9) 