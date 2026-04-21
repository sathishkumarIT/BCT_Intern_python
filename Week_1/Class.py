class Circle:
    def __init__(self ,radius):
        self.a = radius
    def area(self):
        return 3.14 * self.a * self.a   
    
circle_are = Circle(5)
print(circle_are.area())