import copy
import random
from collections import Counter

class Hat():
    
    def __init__(self, **args):
        self.args = args
        self.contents = []
        for x,y in args.items():
            for n in range(y):
                self.contents.append(x)
                n = n + 1

    def draw(self, num):
        if num>=len(self.contents):
            return self.contents
        result = list()
        for x in range(num):
            a = random.choice(self.contents)
            result.append(a)
            self.contents.remove(a)
            x = x + 1
        return result



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    index = 0
    m = 0
    counts = dict()
    istrue = list()
    originalhat = copy.deepcopy(hat)
    for x in range(num_experiments):
        for ball in originalhat.draw(num_balls_drawn):
            counts[ball] = counts.get(ball, 0) + 1
        for ball in expected_balls:
            if counts.get(ball,0) >= expected_balls.get(ball,0):
                istrue.append(True)
            else:
                istrue.append(False)
        print(istrue)
        if len(istrue)==istrue.count(True):
            m = m + 1
        istrue.clear()
        counts.clear()
        x = x + 1
        originalhat = copy.deepcopy(hat)
    
    return m/num_experiments






hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
actual = probability
expected = 0.272
print(actual)
print(expected)
hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
actual = probability
expected = 1.0
print(actual)
print(expected)