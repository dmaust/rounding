'''
Created on Oct 6, 2013

@author: dmaust
'''

import math
from rounding.common import RounderBase

class StandardRound(RounderBase):
    '''
    Rounding class for traditional rounding of round nearest. 
    
    In the event of a tie, the number is rounded up.
    '''

    def __init__(self, precision=0):
        '''
        Initialize the rounding object.
        
        @param precision: Number of decimal places to round to.
        '''
        super(StandardRound, self).__init__(precision=precision)
        
        
    def round(self, x):
        """Round the given value.
        
        @param x: to round
        @type x: numeric  
        """
        fraction, scaled_x, scale = self._get_fraction(x)
        rounddown = fraction < .5
        if rounddown:
            result = math.floor(scaled_x) / scale
        else:
            result = math.ceil(scaled_x) / scale
        self._record_roundoff_error(x, result)
        return result
         
    
    
if __name__ == '__main__':
    num = 5.3
    count = 1000
    expected =  num * count
    
    sr = StandardRound(precision=0)
    
    print "Expected: ", expected
    print "Simple round: ", sum(round(num) for i in xrange(count))
    print "Standard Round: ", sum(sr.round(num) for i in xrange(count))
    print "Error: ", sr.roundoff_error 