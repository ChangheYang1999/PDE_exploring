# Automatic first compatibility for a single high harmonic

Status: PROVED automatic first-compatibility theorem, independently reviewed by the theory part at 17:14Z and admitted in V479. No all-order response or convergence conclusion follows from this support result alone.

## Statement

Let h>=2 and Q>2h be coprime integers, with Q odd. Put delta=2h/Q and M=Q+2h-2, which is odd. For any real amplitude epsilon, take

    f_1(theta)=epsilon sin(M theta).

The first pure stream compatibility condition, at order Q and density frequency2h-3, holds identically. If epsilon is nonzero, this gives nontrivial leading data with no frequency-one component. This statement alone does not ensure compatibility of the later resonances or convergence of the series.

More generally, the same conclusion holds for any finite leading profile supported on odd multiples of an odd M satisfying M-(Q-1)>2h-3.

## Proof

There are no positive even stream resonances before order Q. Let Lambda be the signed support of f_1 and E_j={-j,-j+2,...,j}. Every Cartesian derivative or Poisson forcing shifts a signed angular frequency by one. The nonlinear recurrence, with the Poisson inverse supplying one net support enlargement per input, therefore gives

    supp f_n subset n Lambda+E_(n-1), 1<=n<=Q,
    supp g_n subset n Lambda+E_n, 1<=n<Q.

Here n Lambda is the n-fold sumset. This is proved by induction: at order n=i+j, the stream factor contributes i Lambda+E_i and the density factor contributes j Lambda+E_(j-1); their products are contained in n Lambda+E_(n-1). Angular differentiation does not enlarge support, and the Poisson forcing enlarges it by one.

Every element of Lambda is M times an odd integer. Since Q is odd, every element of Q Lambda is M times an odd integer and has absolute value at least M. Every element of E_(Q-1) has modulus at most Q-1. Thus every possible density frequency at order Q has modulus at least M-(Q-1)>2h-3. The first obstruction coefficient is zero.

For M=Q+2h-2 the lower bound is exactly2h-1, strictly larger than the obstruction frequency. The proof applies over complex amplitudes as well, since it is an identity of supports.

## Response experiments and limits

The separately proved compact-response formula applies with B=M+1. Positive and negative carriers are disjoint whenever q=2hk-2>=BQ, so

    K=ceil((BQ+2)/(2h))

is a sufficient threshold for comparing the full and compact formulas. A finite probe and a nonzero limiting response do not prove nonvanishing at every integer. The first new case selected for an independent probe is h2,Q7,M9, hence delta4/7 and K18. The already studied h2,Q9,M11 case is topic227.

Dependencies: the recurrence and Poisson support calculation in01, the resonance classification144, and the signed-support argument197/201. No genericity or convergence claim is made here.
