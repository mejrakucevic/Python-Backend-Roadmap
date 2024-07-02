from polygon import Polygon
class Square(Polygon):
    def area(self):
       return self.getWidth() * self.getHeight()
   