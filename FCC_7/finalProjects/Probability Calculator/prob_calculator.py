import copy
import random
# Consider using the modules imported above.


class Hat:
    
    def __init__(self, **colors):
        contents = []
        for item, value in colors.items():
            for i in range(value):
                contents.append(item) #>>> ['red', 'red', 'red', 'orange']   
        print(contents)

    def draw(self, pull):
        # Use random here and return those balls as a list of strings
        pass





def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass



''' Resources '''
# Passing multiple values in class initialization
#   https://stackoverflow.com/questions/32005839/how-to-pass-multiple-parameters-to-class-during-initialization
# **kwargs
#   https://realpython.com/python-kwargs-and-args/

