# Replay notes

All stored integer masses, signs, 30,369 flow edges and exact marginals were
checked by the independent auditor. It calls no optimizer. The transport
cost reproduces the producer interval. The residual uses the minimum of
two valid algebraically equivalent angular integral enclosures.

A first 320-bit pass failed to prove domination of one stored extraction
quantum. This was a tighter-enclosure comparison failure, not evidence of
an invalid extraction: different evaluation order and Arb radius rounding
can make one endpoint weaker when precision increases. At row83/cell30
the recomputed original count was595595744 at320bits but595595745 at160bits,
matching the stored count. The final pass uses160bits throughout and
strictly proves every stored extraction bound; no tolerance was added.

The independently recomputed old residual differs from the producer by
about4.7e-11 because the intersection of two valid enclosures slightly
reduces its variation bound. The new local-plus-small upper component is
less than1.3864490587. It is not a full operator bound.
