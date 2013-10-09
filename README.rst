rounding
========

Rounding methods

Stochastic rounding provides a mechanism to eliminate accumulated 
roundoff error in the presence of a distribution where for 
individual samples, the roundoff error is skewed. This is typically
caused by small values.

One drawback to stochastic rounding is the output is non-deterministic,
but this can be avoided by providing a custom deterministic generator, 
or invoking providing the random number generator with a fixed seed.

.. code:: python
  
  r = random.Random()
  r.seed(123)
  sr = StochasticRound(precision=0, random_generator=r)
