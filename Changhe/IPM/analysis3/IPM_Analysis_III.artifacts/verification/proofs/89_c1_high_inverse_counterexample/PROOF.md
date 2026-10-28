# C1 convergence of transport fields does not give uniform high inverse bounds

## Exact theorem

Let T2=(R/2pi Z)^2 with normalized Lebesgue measure and the standard Fourier Sobolev spaces Hs. Fix any real s>1 and choose beta with 1<beta<s. For positive integers n define

 a_n(y)=n^(-beta) sin(ny),
 T_n=(1+a_n(y))partial_x-1,
 D_n={h in L2:T_n h in L2 in distributions}.

Then T_n:D_n->L2 is bijective and its inverse has L2 operator norm at most1. Its vector field converges in C1 to (1,0). Nevertheless there is one fixed smooth forcing f(x,y)=exp(ix) for which the unique solutions h_n=T_n^(-1)f satisfy

 ||h_n||_Hs >= c_s n^(s-beta)-C_s

for all sufficiently large n. In particular no uniform Hs inverse bound can be deduced from C1 proximity of these fields alone. Every h_n is smooth and belongs to its corresponding high graph domain. Taking real or imaginary parts gives a real-valued version after, if necessary, passing to an infinite subsequence.

This is a counterexample to a general implication about coefficient control. It does not refute a high inverse for the actual IPM family with additional high norm restrictions on the correction.

## Low inverse and fixed forcing

Fourier transform only in x. For each integer m and almost every y,

 (T_n h)_m(y)=(-1+i m(1+a_n(y)))h_m(y).

The multiplier has modulus at least1. Division defines an L2 solution for every L2 forcing, with norm at most the forcing norm; the distributional equation puts it in D_n. The same formula gives uniqueness. For the fixed forcing, with d=-1+i,

 h_n(x,y)=exp(ix)/(d+i a_n(y)).                         (1)

The denominator has real part -1 and never vanishes, so (1) is smooth.

## High norm lower bound

For n>=2, |a_n/d|<1/2. Expand the uniformly convergent series

 h_n=exp(ix)[d^(-1)-i d^(-2)a_n+R_n],
 R_n=d^(-1) sum_{j>=2}(-i a_n/d)^j.                    (2)

The j-th power of sin(ny) is a trigonometric polynomial supported on frequencies of absolute value at most jn; the sum of the absolute values of its Fourier coefficients is at most1. Therefore, after multiplication by exp(ix), its Hs norm is at most (2+j^2 n^2)^(s/2). The series in (2) and the geometric decay imply

 ||exp(ix)R_n||_Hs <= C_s n^(s-2beta).                 (3)

For example, divide the series by n^s n^(-2beta); the remaining sum is bounded by a constant times sum_{j>=2}(1+j)^s (1/2)^(j-2), uniformly in n. This also justifies convergence in Hs, including fractional s.

The first oscillatory term has exactly the two Fourier modes (1,n) and (1,-n), so

 ||exp(ix)(-i d^(-2)a_n)||_Hs
 = |d|^(-2) n^(-beta)(2+n^2)^(s/2)/sqrt(2).

The reverse triangle inequality, (3), and the fixed norm of exp(ix)/d give the claimed lower bound, since n^(-beta) tends to zero. Finally ||a_n||_C1 is at most n^(-beta)+n^(1-beta), which tends to zero because beta>1.

## Application boundary

The low inverses are uniformly controlled, the transport fields have no degenerating zero, and the high forcing is fixed. The failure is high differentiation of the coefficients, which C1 proximity does not control. Consequently the geometric radius in proof 88 does not by itself provide the uniform high inverse constants needed for nonlinear closure. A restricted IPM perturbation family can still succeed through additional high coefficient bounds and a proved tame estimate. This calculation establishes neither success nor failure for that family.
