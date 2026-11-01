# Exact response minima at four ninths

Status: PROVED. The exact generic identity173, every finite and tail certificate, and both radius replays pass in V328-V329.

## Exact objects and proposed minima

Use the five real roots b1<...<b5 of the exact two-mode obstruction
polynomial in144 and146. Set delta=4/9 and f1=sin(theta)+b sin(3 theta).
The response sigma_k is the derivative of the density obstruction at
order9(k+1) with respect to the free stream harmonic at order9k.
It is defined for every integer k>=1.

The proposed unique minimizing indices for |sigma_k| are7,4,13,5
at roots1,2,3,5, respectively. At root4 the proposed infimum is
|sigma_infinity| and is not attained at any finite integer. These
are hypotheses to be verified, not assumptions in the proof.

## Exact finite and tail argument

Let sigma_k(b)=N(k,b)/D(k) for k>=10 be the exact rational response
derived from the finite carrier recurrence in the theory part's source.
Its derivation uses the same equations as149. The signed constant
and highest-degree coefficients in b can additionally be compared
with the independently derived pure-mode formulas in146.
The limiting polynomial must equal the independent formula144.
The finite responses below10 are computed by the full signed
Cartesian recurrence.

For each algebraic root, refine its isolating interval by exact
rational bisection. Let A(b) be the appropriate signed polynomial
representing the proposed absolute minimum, or the signed limiting
polynomial for root4. Determine the signs by interval evaluation.
Check every integer below a chosen tail start K directly: all
absolute response intervals must lie strictly above the target
interval, except at the proposed unique minimizing integer.

Normalize D so that D(K+t) has positive coefficients. With e equal
to the limiting response sign, expand exactly

    e N(K+t,b)-D(K+t) A(b).

If every coefficient in t is nonnegative throughout the isolating
root interval and the constant coefficient is strictly positive,
the displayed polynomial is positive for every real t>=0.
Division by D(K+t)>0 then gives |sigma_k(b)|>A(b) throughout the
tail. For a limiting target, its highest coefficient cancels
identically and is checked as an exact algebraic zero before
interval evaluation. The finite checks and tail inequality prove
the claimed unique minimum, or the unattained limiting infimum.
If a proposed tail start fails, a later start is valid only after
checking every intervening integer.

Choose an explicit rational s below the certified target and a
rational a>1+|b|. Apply the exact nonnegative majorant145 with
h=2,Q=9,B=4. A strict componentwise box inequality at z=2^-q
gives convergence with every appropriately weighted derivative
on each exterior

    r>=R>2^(9q/4) |epsilon|^(9/4).

The box test and input constants are retained exactly. Failure of
the adjacent box does not establish optimality of the radius.

## Dependencies and scope

The existing convergence theorem for all five profiles is already
proved in145,146,149,150. This topic audits sharper constants and
the location of response infima; failure here would not remove
those existing convergence results. The generic response, every
finite check and every coefficient inequality must be identified
in the retained evidence. No finite scan is used to certify a
global minimum by itself.

## Completed audit

The minimizing indices are7,4,13,infinity,5 in increasing root order; infinity denotes an unattained infimum. Uniform lower bounds are211/25000000000,87/200000000,47/200000000,99/250000,4114. With norm bounds133/125,1153/1000,127/100,1423/1000,2857/1000, the original145 boxes first pass at z-exponents211,201,206,187,160. With the independently certified initial coefficients and constants168/169, the exponents improve to100,94,107,96,83. The latter radius powers are225,423/2,963/4,216,747/4, with the amplitude factor stated above. These are sufficient strict exterior radii.

The generic rational function is independently identified in both variables by173. The low-index coefficients were recomputed exactly in Q[b], matching all four previously completed Q(k)[b] computations and completing all nine in36.96353 seconds. The stored comparison flag is false where no previous value existed; it does not indicate a disagreement.
