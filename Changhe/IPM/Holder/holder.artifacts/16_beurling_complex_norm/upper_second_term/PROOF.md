# The second term of the explicit complex upper bound

Use the normalized complex operator S, the homogeneous Holder seminorm,
and the elementary upper bound F_a in ../optimized_upper/PROOF.md. Then

    lim_(a -> 0) (F_a-1/a)
        = 1+log(2)/2+log(1+1/pi).                           (1)

Consequently this expression is an upper bound for
limsup_(a -> 0)(M_a-1/a). Together with the glued witness,

    1-log(2)/2 <= liminf_(a -> 0)(M_a-1/a)
       <= limsup_(a -> 0)(M_a-1/a)
       <= 1+log(2)/2+log(1+1/pi).

The existence of a second-term limit for M_a is not proved.

To prove (1), logarithmically differentiate the exact formula for Q2.
It gives Q2(0)=1 and Q2'(0)=log(2)/2. Since 2b2=2^a/Q2,
2b2=1+a log(2)/2+O(a^2). Also Q3(0)=1, b3(0)=1/2, and the smaller
sphere bound near zero is 2^a/pi, since 1/pi<1/2. Hence
s_a -> 1+1/pi. Expanding

    F_a = (2b2) exp(a log(s_a)) / [a(1-a)]

gives (1). Continuity of s_a is sufficient for the constant term.

The decimal 1.6223, used in lead draft16, is not the value of (1).
Even without decimal logarithms, pi<22/7, log(2)>6931/10000, and
log(29/22)>2[7/51+(7/51)^3/3] imply that (1)>1.6223.
An outward numerical enclosure is to be saved under verification.
This numerical correction does not invalidate the exact symbolic upper
bound F_a or the two endpoint coefficients already proved.
