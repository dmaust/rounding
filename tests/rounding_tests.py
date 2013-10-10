__author__ = 'dmaust'

from nose.tools import *
import rounding
import random

def setup():
    pass

def teardown():
    pass

def test_standard():
    standard = rounding.StandardRound()
    assert standard.round(123.45)==123, "Rounds down normally"

def test_stochastic():
    stochastic = rounding.StochasticRound(random_generator=random.Random(123))
    total = sum(stochastic.round(123.45) for i in range(100))
    assert (12340 <= total <= 12360), "Rounds down some of the time:%d" % (total,)
    # error + total = expected
    eq_(total-stochastic.cumulative_error, 12345)


