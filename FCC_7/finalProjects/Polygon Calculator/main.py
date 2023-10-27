class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)
    
    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
        self.height = height
        return self.height

    def get_area(self):
        area = (self.width * self.height)
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        #Print an ascii representation of the shapes created by, "*"
        #If the area is > 50, print "Too big for picture."

        if self.get_area() > 50:
            return "Too big for picture."
        else:
            for w in range(self.width):
                # -1 in range due to indexing starting at 0
                for h in range(self.height - 1):
                    print("*", end = "")
                print("*")
        
        return ""

    def get_amount_inside(self, shape):
        # Calculate how many times (square or rectangle) shape can fit into the passed shape.
        # If rect:4x8 could fit in 2 squares:4x4
        pass


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect.get_diagonal())
print(rect)
print(rect.get_picture())
rect.set_width(3)
print(rect.get_picture())


class Square:
    
    def __init__(self, width):
        self.width = width
        self.height = width
    
    def __str__(self):
        print("Square(side={})".format(self.width))

    def set_side(self):
        pass

'''
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
'''