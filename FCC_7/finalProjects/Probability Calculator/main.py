import prob_calculator


hat = prob_calculator.Hat(red=3,blue=2)
actual = hat.contents
print(actual)
#expected = ["red","red","red","blue","blue"] PASSED


hat = prob_calculator.Hat(red=5,blue=2)
actual = hat.draw(2)
print(actual)
#expected = ['blue', 'red'] PASSED
actual = len(hat.contents)
print(actual)
#expected = 5 PASSED


hat = prob_calculator.Hat(blue=3,red=2,green=6)
probability = prob_calculator.experiment(hat = hat, expected_balls = {"blue":2,"green":1}, num_balls_drawn = 4, num_experiments = 1000)
actual = probability
print(actual)
#expected = 0.272
'''

hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = prob_calculator.experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
actual = probability
print(actual)
#expected = 1.0
'''