'''
Created on Oct 6, 2013

@author: dmaust
'''
import math

class RounderBase(object):
    '''
    Abstract base class for rounding
    '''


    def __init__(self, precision=0):
        '''
        Constructor
        '''
        self.precision = precision
        self.cumulative_error = 0
        
    def _get_fraction(self, x):
        
        scale = 10.0**self.precision
        scaled_x = x * scale
        fraction = scaled_x - math.floor(scaled_x)
        return fraction, scaled_x, scale
    
    def _record_roundoff_error(self, x, result):
        self.cumulative_error += result - x
        
    @property
    def roundoff_error(self):
        return self.cumulative_error