class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        # Print representation of the class
        return "Rectangle(width={}, height={})".format(self.width, self.height)
    
    def set_width(self, width):
        # Reset width to new value
        self.width = width
        return self.width

    def set_height(self, height):
        # Reset height to new value
        self.height = height
        return self.height

    def get_area(self):
        # Return the area of the shape
        area = (self.width * self.height)
        return area

    def get_perimeter(self):
        # Return the perimeter of the shape
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        # Return the diagonal of the shape
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        #Print an ascii representation of the shapes created by, "*"
        #If the area is > 50, print "Too big for picture."

        if self.get_area() > 50:
            return "Too big for picture."
        else:
            for w in range(self.height):
                # -1 in range due to compensate for w's "*"
                for h in range(self.width - 1):
                    print("*", end = "")
                print("*")
        
        return ""

    def get_amount_inside(self, shape):
        # Calculate how many times (square or rectangle) shape can fit into the passed shape.
        # If rect:16x8 could fit in 8 squares:4x4
        russianDoll = self.get_area() // shape.get_area()
        return russianDoll


class Square(Rectangle):
    # Square to inherit all of Rectangle and then some: new __str__ and set_side() method.
    
    def __init__(self, width):
        # equivalent to `Rectangle.__init__(self, width, width)`
        super().__init__(width, width)
        #   -> self.width = width
        #   -> self.height = width

    def __str__(self):
        # Print representation of the class
        return "Square(side={})".format(self.width)

    def set_side(self, width):
        # Reset side to new value
        # equivalent to `Rectangle.__init__(self, width, width)`
        return super().__init__(width, width)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

''' Resources '''
# https://bobbyhadz.com/blog/python-call-class-method-from-another-class
# OOP Inheritance
#   https://www.pythonlikeyoumeanit.com/Module4_OOP/Inheritance.html 