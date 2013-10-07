'''
Created on Oct 6, 2013

@author: dmaust
'''

import math

class StandardRounding(object):
    '''
    Rounding class for traditional rounding of round nearest.
    '''

    def __init__(self, precision=0):
        '''
        Initialize the rounding object.
        
        @param precision: Number of decimal places to round to.
        '''
        self.precision = precision
        
    def round(self, x):
        """Round the given value.
        
        @param x: to round
        @type x: numeric  
        """
        scale = 10.0**self.precision
        scaled_x = x * scale
        fraction = scaled_x - math.floor(scaled_x)
        rounddown = fraction < .5
        if rounddown:
            return math.floor(scaled_x) / scale
        else:
            return math.ceil(scaled_x) / scale
         
    
    
if __name__ == '__main__':
    num = 5.3
    count = 1000
    expected =  num * count
    
    sr = StandardRounding(precision=0)
    
    print "Expected: ", expected
    print "Simple round: ", sum(round(num) for i in xrange(count))
    print "Stochastic Round: ", sum(sr.round(num) for i in xrange(count)) 