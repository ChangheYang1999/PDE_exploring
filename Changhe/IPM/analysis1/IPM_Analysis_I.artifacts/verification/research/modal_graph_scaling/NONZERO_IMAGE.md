# The actual scaling image is nonzero

2026-10-21. This supplement uses the differentiated center expansion proved and audited in research/center_obstruction/PROOF.md for the same exact modal trial. It does not infer nonzero image merely from a nonzero residual.

Let M=260, R=exp(t_-), d=D[M-1,0] and c=3/k-1. The center proof gives

    epsilon=r^5 E_5(theta)+O(r^7(1+|log r|)),
    (E_5)_(2M+3)=c(M-2)d/(8R^2),

with the corresponding first Cartesian derivative remainder bound. The latter hypothesis justifies applying E=r partial_r to the remainder: the resulting error is still O(r^7(1+|log r|)). Therefore the already proved spatial identity gives

    LK=epsilon-E epsilon=-4r^5 E_5(theta)
                            +O(r^7(1+|log r|)).

Its leading sine coefficient at frequency523 is

    (LK)_5,523=-c(M-2)d/(2R^2).                            (3)

There is also a direct reconstruction. The quintic density part has top sine frequency nu=2M+1, with coefficient d/(8R^2). K=rho-E rho multiplies this quintic part by-4. The linear center transport V_lin dot grad-1 maps r^5 sin(nu theta) to a term at frequency nu+2 with coefficient c(nu-5)/2. The remaining degree-five terms use only cubic polynomial velocities and the cubic polynomial density, so they have no frequencies above5. Thus the top coefficient of LK is (-4)d/(8R^2) times c(nu-5)/2, exactly(3). The rank-one contribution is zero since Sigma(K)=0.

The actual d is positive and nonzero by exact dyadic decoding; c>0, and R>0. Hence(3) is strictly negative. A nonzero Fourier coefficient means the continuous angular leading function is nonzero on a closed angular interval. On a smaller such interval and all sufficiently small positive radii the leading term dominates the uniform O(r^7(1+|log r|)) remainder. Thus LK is nonzero on a set of positive planar measure. As membership in X has already been proved, this establishes

    0 < ||epsilon-E epsilon||_X < infinity.

No explicit lower bound on this entire norm is obtained, because no numerical constant or domination radius for the remainder is supplied here. Consequently(2) supplies an actual, positive necessary quotient for this trial but not an evaluated numerical inverse bound.

Recompute(3) in Arb from exp(-2t_-) and in mpmath.iv from1/exp(t_-)^2, using independent decoding of k,t_-,d. Both must prove the same strict public bracket

    -2.4e-11 < (LK)_5,523 < -2.0e-11.

This is a coefficient bracket, not a residual or image norm enclosure. The inherited center theorem already proves the differentiability and the uniform remainder estimate needed for positivity; agreement of finite numbers alone would not establish that argument.
