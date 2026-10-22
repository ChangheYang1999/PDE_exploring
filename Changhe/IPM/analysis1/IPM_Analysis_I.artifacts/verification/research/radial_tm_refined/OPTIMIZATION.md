# Positive linear remainder weights

This is a rearrangement of the proof's bound, before implementation.
It does not change the enclosure criterion.

Fix width b, order K=20, lambda values l_+,l_-, and put
c_b=b^(K+1)/(2(K+1)!). Write

 g_(d,k)=sum_(v=0)^min(d,k) choose(d,v)2^(d-v)k!/(k-v)! b^(k-v).

Every coefficient is nonnegative. Collecting like input magnitudes in
(8)-(9) gives exactly

 J <= (j_A |A|_box+j_B |B|_box)/E_lo^2
            + E_hi^2 sum_k j_(F,k) C_k,
 j_A=c_b |l_-|^(K+1),
 j_B=c_b |l_+|^(K+1) exp(l_+ b),
 j_(F,k)=c_b exp(2b) [b^(k+1)(|l_+|^(K+1)exp(l_+b)+|l_-|^(K+1))
                   +sum_(d=0)^K (|l_+|^(K-d)+|l_-|^(K-d))g_(d,k)].

Here l_+>=0 and l_-<0, including l_+=0 with 0^0=1. Directed
construction of these fixed positive weights can be cached by the exact
pair (b,n); substituting each cell's exact input magnitudes produces the
same sufficient derivative bound, up to harmless extra interval width.
The first engine computes g by the displayed binomial formula. The
second computes each monomial's derivative polynomial by repeated
p -> p'+2p and evaluates it at b. The two engines build and store their
own caches. Cache keys include the exact rational b and mode n, and the
engine precision is fixed for the entire run. Producer calls temporarily
change Arb precision to128; every first-engine operation restores512.
Changing a cache precision after construction is forbidden.

The ordinary coefficient interval calculations use independent integer
hulls: the first computes a midpoint and a radius from collected weights;
the second propagates lower and upper input endpoints according to the
sign of each independently recurrent formal weight. Their only common
utilities are data loading, finite exact dyadic decoding, output format
and endpoint comparison. Neither imports the other's weights or results.
