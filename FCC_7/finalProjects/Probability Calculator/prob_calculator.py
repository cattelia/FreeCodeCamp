import copy
import random

class Hat:

    def __init__(self, **colors):
        '''
        Initializes a new instance of HAT object with the given ball color and number of balls.
        Storing only a list of colors equivalent to the number provided.

        Args:
            **kwargs: Dictionary of color and number.
        '''

        self.contents = []
        self.refillHat = []
        
        for ball, value in colors.items():
            self.contents.extend([ball] * value)
            self.refillHat.extend([ball] * value)

    def draw(self, pull):
        '''
        Draws the given number of balls from the hat and stores it in a list of strings.
        Removing it from the main list.
        If the main list is exhausted, refill it.

        Args:
            pull: the number of balls to pull randomly from the hat

        Return:
            ['red', 'blue'] : List of (strings) balls pulled from the hat.
            
        '''

        ballsPulled = []
        if pull > len(self.contents):
            self.contents = copy.copy(self.refillHat)

        for i in range(pull):
            #print(i, self.contents)
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            ballsPulled.append(ball)
        
        return ballsPulled
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''
    experiment( hat = hat,
                expected_balls = {"red":2,"green":1},
                num_balls_drawn = 5,
                num_experiments = 2000 )

    Args:
        hat: a hat class object containing balls that should be copied inside the function 
        expected_balls: a dictionary object indicating the exact group of balls to attempt to draw from the hat.
        num_balls_drawn: the number of balls to draw out of the hate in each experiment
        num_experiments: the number of experiments to perform

    Return:
        the probability of the experiment
    '''

    # Check to see if we are trying to pull more balls than we have in the hat
    # If so , return 1.0
    initialCount = 0
    for number in hat.contents:
        initialCount += 1
    if num_balls_drawn > initialCount:
        return 1.0    
    

    success = 0
    # Run the experience N times
    for i in range(num_experiments):

        successCheck = 0

        # Look at each hat draw
        collected = hat.draw(num_balls_drawn)
    
        # Compare 'collected' to what we are looking for in 'expected_balls'
        # Every success will be calculated M times
        for color, number in expected_balls.items():
            check = collected.count(color)

            # Check how many we found versus how many we are looking for
            if check == number:
                # If successfully found, add to tracker that is comparing against how many colors we inputted.
                successCheck += 1

                # If we have found all of the colors, we add +1 to how many times it was found
                if successCheck == len(expected_balls):
                    success += 1
    
    #print("Total Matches", success)

    # Calculate the probability of the permutation of colors to numbers show up in the experiments
    probability = success / num_experiments
    return probability

''' Resources '''
# Passing multiple values in class initialization
#   https://stackoverflow.com/questions/32005839/how-to-pass-multiple-parameters-to-class-during-initialization
# **kwargs
#   https://realpython.com/python-kwargs-and-args/

