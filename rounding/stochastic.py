'''
Created on Sep 21, 2013

@author: dmaust
'''

import random
import math

class StochasticRound(object):
    '''
    Rounding class for performing stochastic rounding operations.
    
    Stochastic rounding provides a mechanism to eliminate accumulated 
    roundoff error in the presence of a distribution where for 
    individual samples, the roundoff error is skewed. This is typically
    caused by small values.
    
    One drawback to stochastic rounding is the output is non-deterministic,
    but this can be avoided by providing a custom deterministic generator, 
    or invoking random.Random() with a fixed seed.
    '''


    def __init__(self, precision=0, random_generator=random.Random()):
        '''
        Initialize the rounding object.
        
        @param precision: Number of decimal places to round to.
        @param random_generator: Generator for obtaining roundoffs
        '''
        self.random_generator = random_generator
        self.precision = precision
        
    def round(self, x):
        """Round the given value.
        
        @param x: to round
        @type x: numeric  
        """
        scale = 10.0**self.precision
        scaled_x = x * scale
        fraction = scaled_x - int(scaled_x)
        rounddown = fraction < self.random_generator.random()
        if rounddown:
            return math.floor(scaled_x) / scale
        else:
            return math.ceil(scaled_x) / scale
         

def sround(x, precision=0):
    """
    Round a single number using default non-deterministic generator.
    
    @param x: to round.
    @param precision: decimal places to round.  
    """
    sr = StochasticRound(precision=0)
    return sr.round(x)
    
if __name__=='__main__':
    num = 5.3
    count = 1000
    expected =  num * count
    
    print "Expected: ", expected
    print "Simple round: ", sum(round(num) for i in xrange(count))
    print "Stochastic Round: ", sum(sround((num)) for i in xrange(count)) 