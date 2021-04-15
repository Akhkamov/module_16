from rectangle1 import Rectangle, Square, Circle

#creating 2 rectangles

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(6,10)

#print(rect_1.get_area())
#print(rect_2.get_area())

square_1 = Square(4)
square_2 = Square(11)

#print(square_1.get_area_square(), square_2.get_area_square())

#creating 2 circles

circle_1 = Circle(7)
circle_2 = Circle(11)

#print(circle_1.get_area_circle(), circle_2.get_area_circle())

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
        print(figure.get_area())