# Density convergence on positive area determines exterior convergence

Status: PROVED after the theory part's independent reviews at2026-10-31T07:31Z and07:33Z and verifier closure V178. An all-order geometric bound for the computed rational sequence remains open.

## Exact statement

Let delta=a/b be reduced in(0,1), q_0=2b/gcd(a,2), and let f_1 be a nonzero finite real odd-sine polynomial with largest frequency L. Use the canonical stationary polynomial-log recursion with zero resonant stream constants. Put

    D_n(t,theta)=exp((1-n delta)t) F_n(t,theta),
    T_n(t,theta)=exp((2-n delta)t) G_n(t,theta),
    M_n=sum_(q,m)|[t^q sin(m theta)]F_n|,
    N_n=sum_(q,m)|[t^q sin(m theta)]G_n|.

The following are equivalent:

1. M_n is bounded geometrically in n.
2. N_n is bounded geometrically in n.
3. The individual density terms D_n are bounded at each point of some Lebesgue-measurable set of positive area in the(t,theta) plane.
4. The density series converges pointwise at each point of some such set.
5. The density series converges uniformly on some full closed annulus of positive radial width.
6. The density, stream and common-potential series define an exact exterior stationary solution with absolute convergence of all fixed weighted derivatives at sufficiently large radii.

If these equivalent conditions fail, the set where the density terms are bounded has measure zero and is meagre. Consequently the density series, as well as the stream, radial-velocity and potential series specified in topic94, has unbounded individual terms almost everywhere and on a dense residual set. The conclusion concerns each of these fields; a finite intersection gives a common set of full measure which is also residual.

These statements also hold for area in the physical punctured plane. The map(t,theta) to(exp(t)cos(theta),exp(t)sin(theta)) has positive Jacobian exp(2t) and is a local homeomorphism. Use a countable cover by bounded rectangles and angular charts to transfer null sets and meagreness.

## Recovering density coefficients from bounded terms

The canonical degree bounds are deg_t F_n<=n/q_0 and angular frequency at most(L+1)n. Suppose condition3 holds on E. By a countable cover, restrict to a rectangle Q=[T_0,T_1] times one angular period where E has positive measure. Set B=max(|T_0|,|T_1|) and h=T_1-T_0>0.

The measurable sets E_j={x in E intersect Q: |D_n(x)|<=j for every n} increase to E intersect Q. Choose j for which E_j has area A>0. Put eta=A/(2h). Fubini gives a measurable set S of t values whose angular slices have length at least eta and whose measure is at least mu=A/(4pi)>0: the other slices contribute at most eta h=A/2, and every slice has length at most2pi.

On every such slice, after removing a null set of t values if necessary,

    |F_n(t,theta)|<=j exp(B) exp(n delta T_1).

The two coefficient-recovery lemmas proved in topic94 say:

- If a trigonometric polynomial of frequency at most M has modulus at most V on angular measure eta, its Fourier coefficient sum is at most V(16pi e/eta)^(2M).
- If a polynomial of degree d has modulus at most V on a measurable subset of[-B,B] of measure at least mu, its coefficient sum is at most V[8e(1+B)/mu]^d.

For completeness, both are Lagrange interpolation estimates. A measurable set of length mu supplies d+1 nodes separated by at least |j-k|mu/(4d). The product denominator for node j is at least(mu/(4d))^d j!(d-j)!. Polynomial numerators have coefficient sum at most(1+B)^d; sum_j1/[j!(d-j)!]=2^d/d!, and d!>=(d/e)^d. For angles restrict to a half-period retaining at least half the measure, use chord distance at least2 angular distance/pi, and numerator coefficient sum at most2^d for d=2M. These give precisely the stated constants, including degree0 by direct inspection.

First apply the trigonometric estimate to each slice. Every sine amplitude of F_n is bounded on S by

    j exp(B) exp(n delta T_1)(16pi e/eta)^(2(L+1)n).

Next apply the polynomial estimate in t to each amplitude, then sum over at most(L+1)n frequencies. Both interpolation brackets exceed one. Thus

    M_n <= j exp(B)(L+1)n A_*^n,
    A_*=exp(delta T_1)(16pi e/eta)^(2(L+1))
                  [8e(1+B)/mu]^(1/q_0).

For any A'>A_*, the factor n(A_*/A')^n is bounded, proving condition1. The estimate uses neither the stationary equation nor the Poisson inverse, only the degree bounds and radial factor.

## Completing the equivalences and the divergence alternative

Topic98 gives1=>2, using the next stationary equation and a fixed angular coefficient weight. Topic93 gives2=>1 and, with topics41 and95,2=>6. Absolute exterior convergence gives5, uniform convergence gives4 on the interior of that annulus, and pointwise convergence gives bounded terms, so4=>3. Together with the coefficient recovery just proved, all six conditions are equivalent.

Let Z be the set where all D_n are bounded. Since every term is continuous,

    Z=union_(j>=1) intersection_(n>=1){|D_n|<=j}

is a countable union of closed sets. If condition1 fails, the implication3=>1 shows that Z has measure zero. Each closed constituent therefore has empty interior, so Z is meagre. Its complement is a dense residual set and has full measure. At every point of this complement the terms are unbounded, precluding series convergence. Because conditions1 and2 are equivalent, topic94 gives the corresponding statements for stream, radial velocity and common potential. Finite intersections preserve full measure and the residual property.

The conclusion cannot be upgraded to every point. All density terms vanish identically at theta=0 and theta=pi by sine parity, regardless of coefficient growth. Such symmetry lines have area zero and empty interior, as the statement allows.

## Dependencies and remaining open steps

Topic17 supplies the degree bounds. Topic94 supplies the separated-node construction and interpolation estimates, reproduced above at the level needed here. Topic98 supplies the independently confirmed density-to-stream implication. Topic93 and topics41,95 supply stream-to-density control and common-potential convergence with the precise weighted derivative norms. Every implication is conditional on the same generated canonical sequence; no claim applies to arbitrary unrelated density/stream input polynomials. Establishing an all-order geometric bound, or its failure, for any computed rational sequence remains open.
