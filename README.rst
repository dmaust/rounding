rounding
========

Rounding methods

`StandardRound` rounds to the nearest, and in the event of a tie, rounds up.

`RoundToEven` rounds to the nearest, but in the event of a tie, rounds toward 
the nearest even number.

`StochasticRound` provides a mechanism to eliminate accumulated
roundoff error in the presence of a distribution where for 
individual samples, the roundoff error is skewed. This is typically
caused by small values. This may be a common problem when dealing with applying a
function to many small integer values as the number of discreet inputs is small.

One drawback to stochastic rounding is the output is non-deterministic,
but this can be avoided by providing a custom deterministic generator, 
or invoking providing the random number generator with a fixed seed.

.. code:: python
  
  r = random.Random()
  r.seed(123)
  sr = StochasticRound(precision=0, random_generator=r)

