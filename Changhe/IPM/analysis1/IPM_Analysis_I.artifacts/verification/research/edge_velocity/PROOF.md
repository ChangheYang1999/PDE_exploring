# Taylor subtraction for the face velocity, and its low-frequency limitation

Date: 2026-10-20. Status: analytic face estimate and low-frequency obstruction CONFIRMED after independent derivation and actual Claude Opus5.5 review; independent Arb/iv constants audit passed17:07:02Z. Final notation clarifications recorded below. This audits the pinned lead note in `evidence/lead_weighted_velocity.md`. It proves a face estimate; it does not close the full IPM coupling, the corner, or a global inverse.

## Exact statement

For a real number b let H_b=L^2(R^2,|y|^(-2b) dx dy), and let D_0=C_c^infinity(R^2 minus {y=0}). Fix an integer N>=0 and N-1/2<b<N+1/2. Use the full-plane velocity U=(-psi_y,psi_x), -Delta psi=partial_x h, defined on D_0 by its Fourier multipliers

U_1: xi eta/(xi^2+eta^2),  U_2: -xi^2/(xi^2+eta^2).

For h in D_0 set u_(i,j)(x)=partial_y^j U_i[h](x,0)/j! and

T_N U_i[h]=U_i[h]-sum_(j=0)^(N-1) y^j u_(i,j)(x).

Then

||T_N U_i[h]||_(H_b)<=C_(N,b)||h||_(H_b),
||u_(i,j)||_(dot H^(b-j-1/2)(R))<=c_(j,b)||h||_(H_b),  j<N,

where the homogeneous norm means the Fourier seminorm, or its Hilbert completion, without asserting a particular polynomial representative. In unitary Fourier normalization,

c_(j,b)=2^(-b-1) sqrt(Gamma(2b+1))/j!,
C_(N,b)=2^|b|+sqrt(S_A)+sqrt(S_K)+sum_(j<N)[sqrt(S_(B,j))+sqrt(S_(C,j))],
S_A=2^(2b-2N-1) Gamma(2N+2)/[(2N+1-2b)(N!)^2],
S_K=2^(-2b-1)/(2b+1),
S_(B,j)=2^(-2b-1) Gamma(2j+2)/[(2b-2j-1)(j!)^2],
S_(C,j)=3*2^(2|b|-1) Gamma(2j+2)/(j!)^2.

The constants agree with the lead's formula when b>=0. The absolute value in the convolution constant is needed in this proof for the allowed N=0,b<0 cases. The polynomial sum is empty there; its absolute-value notation is harmless and equals the lead formula whenever that sum is present. No claim that the lead's smaller total constant is false is made.

If chi is smooth, even, 0<=chi<=1, chi=1 on [-1,1] and supported in [-2,2], set

(E_j u)^hat(xi,y)=y^j chi(y|xi|) u^hat(xi),
T_N^chi U_i[h]=U_i[h]-sum_(j<N) E_j u_(i,j).

Then

||T_N^chi U_i[h]||_(H_b)<=C'_(N,b)||h||_(H_b),
C'_(N,b)=C_(N,b)+sum_(j<N)c_(j,b) sqrt(2/(2b-2j-1)).

These estimates commute with ordinary x derivatives. For every nonnegative integer m, a finite constant C_(N,b,m) also bounds the m-th y partial_y derivative of either remainder by the sum of the corresponding input norms through order m. This assertion concerns b derivatives, not m ordinary transverse derivatives.

The window is sharp for arbitrary test functions when using this global Taylor subtraction. In contrast, neither the homogeneous trace bounds nor the remainder bound alone control the canonical edge forcing locally in x when b>2. The explicit dilation argument below proves this latter failure, even with IPM parity and density factor x^2 y.

## Partial Fourier kernels and Taylor coefficients

For a=|xi|>0, the one-dimensional fundamental solution of a^2-partial_y^2 is exp(-a|y|)/(2a): its derivative has jump -1 and its equation is the delta distribution. Thus

U_2^hat(xi,y)=-(a/2) integral exp(-a|y-y'|) h^hat(xi,y') dy',
U_1^hat(xi,y)=(i xi/2) integral sgn(y-y') exp(-a|y-y'|) h^hat(xi,y') dy'.

The frequency xi=0 has measure zero in Plancherel and causes no loss in this estimate. Each h in D_0 vanishes on a strip around y=0. Differentiating the displayed smooth kernel there gives

u_(2,j)^hat= -a^(j+1)/(2j!) integral (sgn y')^j exp(-a|y'|) h^hat(xi,y') dy',
u_(1,j)^hat= -i xi a^j/(2j!) integral (sgn y')^(j+1) exp(-a|y'|) h^hat(xi,y') dy'.

The signs follow from exp(-a|y-y'|)=exp(-a|y'|)exp(a y sgn y') for |y|<|y'|, while the odd kernel has the extra sign -sgn y'. Cauchy-Schwarz with the weighted input gives

integral_R exp(-2a|y'|)|y'|^(2b)dy'=2 Gamma(2b+1)/(2a)^(2b+1).

This is finite since b>-1/2. Multiplying by a^(j+1)/(2j!) proves the pointwise frequency trace bound and, after multiplying by a^(b-j-1/2) and applying Plancherel, the asserted homogeneous norm estimate.

## Uniform one-dimensional remainder estimate

Dilation reduces the problem to a=1. Indeed, for delta_l f(y)=f(ly),

||delta_l f||_(L^2(|y|^(-2b)))=l^(b-1/2)||f||,
K_a*f=delta_a[K_1*(delta_(1/a)f)],

and Taylor subtraction commutes with these dilations. The unimodular factors in the velocity formulas do not change norms. Write K(t)=exp(-|t|)/2 or sgn(t)exp(-|t|)/2. With K_j(y') the j-th y derivative of K(y-y') at y=0, the conjugated remainder kernel is

k_b(y,y')=|y|^(-b)[K(y-y')-sum_(j<N)y^j K_j(y')/j!]|y'|^b.

The absolute value of K_j(y') is exp(-|y'|)/2 for y'!=0. Partition the (y,y') plane into A: |y|<=|y'|/2, B: |y|>=2|y'|, and C: |y'|/2<|y|<2|y'|. The triangle inequality for operator norms lets us estimate the pieces separately.

On A, Taylor's formula on the single analytic side of K gives

|K(y-y')-sum_(j<N)y^j K_j(y')/j!|
 <= |y|^N exp(-|y'|/2)/(2N!).

This also holds for N=0 by the direct exponential bound. The square Hilbert-Schmidt integral is bounded by

1/[4(N!)^2] integral_R |y'|^(2b)exp(-|y'|)
  [integral_(|y|<=|y'|/2)|y|^(2N-2b)dy]dy'.

The inner integral is 2(|y'|/2)^(2N+1-2b)/(2N+1-2b); the two signs of y' and the gamma integral produce exactly S_A.

On B the convolution kernel is bounded by exp(-|y|/2)/2. Its weighted square integral is

(1/4) integral_R |y|^(-2b)exp(-|y|)
 [2(|y|/2)^(2b+1)/(2b+1)]dy=S_K.

For the j-th polynomial term the square integral is

1/[4(j!)^2] integral_R |y'|^(2b)exp(-2|y'|)
 [2(2|y'|)^(2j+1-2b)/(2b-2j-1)]dy'=S_(B,j).

All denominators are positive in the stated window.

On C the weight ratio is at most 2^|b|. The convolution part has norm at most 2^|b|, since its absolute kernel is bounded by 2^|b||K(y-y')| and ||K||_1=1. For example, this convolution bound follows by integrating translated L^2 norms against |K| and using the triangle inequality. The j-th polynomial kernel is bounded by

2^|b| |y|^j exp(-|y|/2)/(2j!).

For fixed y, the y'-section of C has length 3|y|. Its square integral is consequently at most

3*2^(2|b|)/(4(j!)^2) integral_R |y|^(2j+1)exp(-|y|)dy=S_(C,j).

Adding these bounds proves C_(N,b). The test domain D_0 is dense: truncate to bounded sets separated from y=0, then use ordinary smooth approximation where the weight is bounded above and below. Thus the remainders extend to H_b, while the traces extend to the stated homogeneous Hilbert completions. This density argument does not choose absolute polynomial representatives for the traces.

For completeness, the lead's regional bound 2^b when b<0 is genuinely false as a bound for the region-C convolution operator. Choose smooth functions nearly constant on a long interval centered at Y, first with length tending to infinity and then Y much larger than that length. In this regime the weight ratio tends uniformly to1, the region-C indicator tends to1, and convolution by the even kernel has norm tending to1 on those functions. Since 2^b<1, the proposed regional bound cannot hold. The total constant may still be sufficient by a different proof.

## Frequency-adapted extension and b derivatives

For a=|xi| and j<N,

integral_(|y|>1/a)|y|^(2j-2b)dy=2 a^(2b-2j-1)/(2b-2j-1).

Since 1-chi(ay) vanishes on |y|<=1/a and is bounded by1, Plancherel and the trace estimate give

||(1-chi(y|D_x|))y^j u_(i,j)||_(H_b)
 <=sqrt(2/(2b-2j-1)) c_(j,b)||h||_(H_b).

Adding this to T_N proves the estimate for T_N^chi. The extension itself is an edge component and need not be in H_b at y=0.

Ordinary x derivatives multiply by i xi and commute with these operations. Put Y=y partial_y. Distributional integration by parts yields

Y(K*f)=(t K'(t))*f+K*((Y+1)f).

For the odd kernel K' includes a delta mass, but t delta(t)=0. The kernels (t partial_t)^l K, l>=0, are piecewise analytic polynomial multiples of exp(-|t|), with exponential decay, finite one-sided jets of every order and no delta mass. Taylor subtraction commutes with Y. Repeated use of the displayed identity expresses Y^m T_N(K*f) as a finite sum of Taylor-subtracted convolutions with these kernels applied to (Y+1)^j f, j<=m.

The A/B/C proof applies to each new kernel with finite constants: the A remainder is bounded by |y|^N times a polynomial in |y'| times exp(-|y'|/2); the B Taylor coefficients and C kernels have the analogous polynomial-exponential bounds. Near zero the same powers 2N-2b and 2j-2b determine integrability, while all extra polynomial factors are integrable at infinity against the exponential. This proves the finite C_(N,b,m). For the adapted extension, derivatives of chi(ay) are supported where 1<=a|y|<=2 and yield the same finite weighted integrals. This gives the corresponding estimate for T_N^chi.

At b=N+1/2 choose a test input with nonzero N-th output Taylor coefficient. The remainder is a nonzero multiple of y^N to leading order, and its squared weighted integral diverges as integral_0^1 dy/y. At b=N-1/2 with N>=1 choose a nonzero highest subtracted coefficient u_(i,N-1). The polynomial dominates the decaying convolution as |y| tends to infinity, again giving logarithmic divergence. The same tests give failure beyond these endpoints. For N=0, the lower endpoint and lower exterior follow by adjoint duality with the upper endpoint and upper exterior: the even convolution kernel is self-adjoint and the odd one skew-adjoint in unweighted L^2, so conjugated weighted operators at b and -b have the same norm. One may localize xi near any nonzero frequency to transfer these one-dimensional failures to the plane; smooth approximation then gives test functions in D_0.

## A canonical low-frequency obstruction, even with IPM symmetry

Choose a nonnegative smooth bump chi supported in four disjoint reflected small patches away from both axes, with chi even in x and y and each patch satisfying 3x^2>y^2. Put F=x^2 y chi. It belongs to D_0, is even in x and odd in y, vanishes near the origin, and has the required x^2 y factor. Its canonical strain c_F is strictly positive. Indeed, differentiating the fundamental solution -log|X|/(2pi) three times gives the exact formula

c_F=psi_xy[F](0)=(1/pi) integral_R2 y(3x^2-y^2)F(x,y)/(x^2+y^2)^3 dx dy>0.

There is no singularity because F vanishes near zero, and the displayed integrand is positive wherever chi>0. In a disk around zero, psi[F] is harmonic and has odd-x, odd-y symmetry. Its Taylor expansion therefore starts with c_F xy; all remaining terms have degree at least4. Hence

U[F](x,y)=(-c_F x,c_F y)+O(|(x,y)|^3),

with the corresponding differentiated remainder bounds on smaller disks.

For R>=1 set F_R(X)=R^(b-1)F(X/R). Change of variables proves ||F_R||_(H_b)=||F||_(H_b). Homogeneity of the velocity multiplier gives

U[F_R](X)=R^(b-1)U[F](X/R).

On every fixed compact x interval,

u_(1,0)[F_R](x)=-c_F R^(b-2)x+O(R^(b-4)),
u_(2,1)[F_R](x)=c_F R^(b-2)+O(R^(b-4)),

uniformly with any fixed finite number of x derivatives. These formulas concern the actual canonical velocity of the smooth compactly supported F_R, without a choice of homogeneous representative.

Let rho be any smooth fixed background on an axis interval where

H(x)=rho_y(x,0)-x rho_xy(x,0)

is not identically zero. Then its edge forcing equals

u_(1,0)[F_R]rho_xy+u_(2,1)[F_R]rho_y
 =c_F R^(b-2)H(x)+O(R^(b-4)).

After multiplying by a fixed compact cutoff on which H is nonzero, its L^2 norm diverges for b>2, and so does every stronger nonnegative Sobolev norm. Thus a bounded map from H_b alone into such a local canonical edge forcing space is impossible. The homogeneous trace estimates are consistent with this: their unpenalized low frequencies contain this growing strain. An added far-field norm, a bounded normalization functional in a stronger space, or another separately proved condition may remove this sequence. None is part of W1 or W1'.

Finally, for 2.5<b<3.5 the two edge traces have homogeneous orders b-1/2 and b-3/2 respectively. The combined forcing cannot be credited with a gain greater than2 from these inequalities: its minimum listed order is b-3/2, between1 and2. Multiplication by a variable background also needs low-frequency control and an appropriate multiplier theorem. The lead note acknowledges the far-field gap; this argument shows why it is substantive.

## Scope and dependencies

This proof uses the fundamental solution identity, Fourier Plancherel, elementary Taylor estimates, gamma integrals, weighted Cauchy-Schwarz, and exact dilation. It confirms a modified-velocity face estimate on the dense test domain and its remainder completion, not a canonical full-plane inverse on every weighted input. No corner product-weight estimate, global edge system, solution trace extension, compactness, index, nonlinear estimate, or decisive endpoint follows. The exact lead snapshots and the independent constants audit are kept alongside this proof.

## Arithmetic verification

At N=3,b=13/5, the two constants satisfy C<78.798713938733 and C_prime<82.260031194549. At N=3,b=17/5, C<151.060134903140 and C_prime<156.124040371967. The corrected N=0,b=-1/4 constant is below2.863906001713. Every displayed decimal is strictly above an exact rational interval endpoint in `evidence/constants_audit.json`. The primary computation uses Arb256 on the simplified formulas; a separate mpmath.iv160 calculation assembles the double integrals in their integration order and the Cauchy-Schwarz gamma integral. Every primary interval contains its independent counterpart. This checks arithmetic, not the infinite-dimensional estimate by numerical sampling.

Actual Claude Opus5.5 reconstructed the constants, b-derivative argument, extension, endpoints and symmetric strain obstruction, accepting the stated face scope at17:07:53Z. Its request to distinguish the empty N=0 polynomial sum was incorporated. The regional lower-bound counterexample above concerns only the even kernel; no claim about the odd restricted kernel follows from its whole-line Fourier multiplier norm.
