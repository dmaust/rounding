'''
Created on Sep 21, 2013

@author: dmaust
'''

import random
import math

class StochasticRound(object):
    '''
    classdocs
    '''


    def __init__(self, random_generator=random.Random(), precision=0):
        '''
        Constructor
        '''
        self.random_generator = random_generator
        self.precision = precision
        
    def round(self, x):
        scale = 10**self.precision
        scaled_x = x * scale
        fraction = scaled_x - int(scaled_x)
        rounddown = fraction < self.random_generator.random()
        if rounddown:
            return math.floor(scaled_x) / scale
        else:
            return math.ceil(scaled_x) / scale
            
         
        
if __name__=='__main__':
    random_generator = random.Random()
    random_generator.seed(101) 
    sr = StochasticRound(random_generator=random_generator)
    num = 5.3
    count = 1000
    expected =  num * count
    
    print "Expected: ", expected
    print "Simple round: ", sum(round(num) for i in xrange(count))
    print "Stochastic Round: ", sum(sr.round((num)) for i in xrange(count)) 