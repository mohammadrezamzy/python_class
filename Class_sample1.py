class Cpoint:
    
    def __init__(self, a, b):
        self.x = a
        self.y = b
        print('I am in initializing')
    
    
    def __str__(self):
       return f"({self.x},{self.y})"
        
    def test(self):
        print('this is test' , self)
    
         
        
point1 = Cpoint(10, 20)
point2 = Cpoint(20, 30)
point3 = Cpoint(5, 8 )

print(point1)
# print(point1.__str__())
print(point2)
print(point3)


point1.test()
point2.test()
point3.test()

# Cpoint.test(point3)
point1.z = 100
point1.z += 200
print (point1 , point1.z)

# print (point2 , point2.z)
# del point1
point1.test()
 
print(point3.__dict__)
print(dir(Cpoint))
print(dir(point3))