rounding
========

Stochastic rounding provides a mechanism to eliminate accumulated 
roundoff error in the presence of a distribution where for 
individual samples, the roundoff error is skewed. This is typically
caused by small values.

One drawback to stochastic rounding is the output is non-deterministic,
but this can be avoided by providing a custom deterministic generator, 
or invoking random.Random() with a fixed seed.
