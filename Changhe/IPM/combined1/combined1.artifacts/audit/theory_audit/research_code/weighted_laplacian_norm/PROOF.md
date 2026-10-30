# A continuous weighted-Laplacian lower bound for the dyadic norm

## Statement

Let Y be the exact dyadic space of T4-058, with0<a<2 and q=2+s,0<s<1. For every h in Y,

    Y(h)>=5^((a-2)/2) ||(1+r^2)^((2-a)/2) Delta h||_2.    (1)

This inequality is independent of the low regularization radius. It provides a necessary residual bound for the scheme: if the actual-inverse theorem in ../farfield_resolvent_floor/PROOF.md applies and the closure inequalities hold, then

    5^((a-2)/2) ||(1+r^2)^((2-a)/2) Delta F||_2
      < sqrt(8pi)(1+c-ca)^2/(1+a).                        (2)

The new ingredient is only(1) and the exact evaluation below. Inequality(2) remains conditional on independent acceptance of that inverse theorem.

## Proof of the continuous lower bound

The audited plateau estimate is

    Y(h)^2>=||Delta h||_(L2(r<2))^2
       +sum_(j>=1)2^(2(2-a)j)||Delta h||_(L2(2^j<r<2^(j+1)))^2.

On r<2,1+r^2<=5. On shell j>=1,

    1+r^2<=1+2^(2j+2)<=5*2^(2j).

Since2-a>0, each shell coefficient and the core coefficient are at least5^(a-2)(1+r^2)^(2-a). Integrating proves(1).

## Complete finite formula

Use the finite canonical residual representation from ../weighted_full_residual/PROOF.md:

    F=r sum_(ell,n) z^(ell delta/2) P_(ell,n)(t) sin(n theta),
    t=r^2/(1+r^2), z=1-t, delta=1-1/c.

Set d_ell=ell delta/2 and

    K_(ell,n)=T_(d_ell,1)^2 P_(ell,n)-n^2 P_(ell,n),
    T_(d,k)P=(k-2dt)P+2t(1-t)P'.

Then Delta F=r^-1 sum z^d K(t)sin(n theta). Check exact divisibility K=t L for every component before proceeding. It follows either from the smooth canonical construction and grouped angular orders, or directly by exact polynomial division. A failed check stops the computation.

Angular orthogonality and dr/r=-dz/[2z(1-z)] now give

    ||(1+r^2)^((2-a)/2) Delta F||_2^2
      =(pi/2) sum_n sum_(ell,k) integral_0^1
           z^(d_ell+d_k+a-3)(1-z)L_(ell,n)(1-z)L_(k,n)(1-z) dz.        (3)

Group every square polynomial exactly, including all off-diagonal multiplicities. If the resulting polynomial at exponent e=d_ell+d_k-3 is H_e(z)=sum_j h_(e,j)z^j, then(3) is

    (pi/2) sum_(e,j) h_(e,j)/(a+e+j+1).                  (4)

Check that every denominator with a nonzero term is positive. For rigorous separated integrability, also check each nonzero diagonal component before summing, using its exact vanishing order at z=0. This prevents treating cancellation between divergent moments as ordinary integration. Formula(4) is evaluated by exact rational sums or outward ball arithmetic at a stated precision; all signed cancellations are retained. Positivity of the final interval is required before its square root.

## Uniform parameter comparisons

The unscaled norm in(1) is nonincreasing in a, because its pointwise squared weight is(1+r^2)^(2-a). Its prefactor5^((a-2)/2) is increasing in a. The residual ceiling on the right of(2) is strictly decreasing while beta_infinity=1+c-ca>0. Thus on a cell[l,h], a sufficient certificate contradicting(2) is

    5^((l-2)/2) ||(1+r^2)^((2-h)/2) Delta F||_2
       >= sqrt(8pi)(1+c-cl)^2/(1+l).

All endpoint values must be certified, and the cells must cover the entire stated parameter interval. A finite list of values without such a cover gives only pointwise tests.

## Status

This proof and its candidate computations are original and OPEN pending independent review. A high inverse or existence is not established. Failure of the lower bound to contradict(2) does not prove feasibility. The exact canonical input, code, precision, final norm intervals and actual times are retained in verification.
