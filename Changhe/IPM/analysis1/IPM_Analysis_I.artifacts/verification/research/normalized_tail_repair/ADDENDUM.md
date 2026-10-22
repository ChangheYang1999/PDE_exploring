# Mandatory addendum: interval dependence, scope and complete remainder

This addendum accompanies the unchanged proof-first PROOF.md.

## A1. Exact coefficient collection before interval evaluation

For the recurrence in (11), let c_d=(-1)^d(floor(d/2)+1). Its generating
function is 1/[(1-z)(1+z)^2]; equivalently c_0=1, c_1=-1 and
c_d=-c_(d-1)+c_(d-2)+c_(d-3), with negative subscripts zero. For M=520,

 q_m=8 sum_(j=m+1)^(M+1) c_(j-m-1) h_j,  1<=m<=M,
 q_0=4 sum_(j=1)^(M+1) c_(j-1) h_j.

Substitution proves these formulas from the triangular recurrence. They
are exact linear forms, so collecting their integer coefficients before
interval evaluation avoids repeated occurrences of a shared uncertain
coefficient. The first experimental implementation directly iterated
intervals and had severe wrapping. The statement in the first Opus review
that the recurrence roots themselves imply polynomial *interval* growth
is false: independent interval radius propagation discards the correlated
sign cancellation. The collected exact forms have at most linear integer
coefficients and give rigorous narrow enclosures by directed sums.

The second implementation retains the distinct three Laurent synthetic
divisions of PROOF.md, taking its input from the independent direct-product
certificate. Both triangular algorithms enclose the unique exact quotient
whether their diagnostic remainder intervals happen to contain zero or
not. Algebraic divisibility, including the discarded low coefficient,
is proved in (9). Neither overlap nor zero containment proves equality
of functions. Independent interval overlap is only a consistency test;
each output separately certifies the published bounds. Neither output
must be a subset of the other after distinct dependency patterns.

Topic42 means research/outer_leading_cancellation, whose CONFIRMED verdict
pins both complete 522-sine certificates and their sources. The modal
exterior factor is R_b^3 sum_m,j A_mj exp((k-j(1-k)-2l)tau) cos(2mtheta)
when converted to density, with the common cos^2theta sin theta factor.
The exterior pair (j,l)=(1,0) is therefore exactly the Aout column1
projection. The exact normalization changes column0 only and adds a
joined fast-decaying correction, as defined in modal_repair/PROOF.md;
it leaves column1 unchanged. Hence (9) uses P1 without z, and the
conversion from the coefficient of exp(beta tau) to r^beta is precisely
R_b^(-beta), including in the definition H=k Epsilon/(1-k).

## A2. Numeric assumptions and exact transition moments

The source audit verifies directly, by integer comparison of the exact
NPZ dyadic k, that 0<k<1/3. It also verifies beta=2k-1, beta2=3k-2<-1,
and all finitely many original exterior powers. Thus the square
integrability conclusion uses the stronger bound actually available.
The degree16 polynomial for b is stored as exact integer JSON and its
integrals B and J_b, zeros of derivatives0 through7, symmetry and
maximum are independently checked with rational arithmetic. The optional
log2 case in the original general integration formula never occurs:
-beta lies strictly between1/3 and1. No numerical evaluation of J_chi
is required here; its convergent integral defines it exactly, and (14)
supplies its certified upper bound. T>=1 is retained only to let every
remainder use powers of 1+log r without a separate small-radius convention.

## A3. Precisely the topology claimed

The numerical estimate is for the explicitly displayed weighted factor
supremum norm, with exactly the dyadic L of the original modal archive
and W=(1+(r/L)^2)^((k-3)/2). It is not a bound in an unweighted Sobolev
norm, a source-graph norm, or an unspecified stronger topology. Therefore
it does not supply the hypotheses of a nonlinear closing theorem or
containment in an uncertainty class around X3.

For completeness, a qualitative derivative extension is available.
On the correction support r>=T, every fixed Cartesian derivative D^a
of order |a|<=7 obeys

 sup r^|a| |D^a[h_T/(x^2 y W)]| <= C_a T^(k-1),

where C_a is finite and depends only on k,L,Q,b,chi and the order, not T.
Indeed outside2T differentiate r^(k-1)(1+L^2/r^2)^alpha Q(cos2theta),
and on [T,2T] put X=T Y: all factors become smooth functions of Y on
1<=|Y|<=2 and L/T in[0,1], with the common prefactor T^(k-1).
The quotient is the explicit factor and extends across the axes.
For the compensator use the same scaling and its C7 joins. This is a
qualitative estimate in these particular weighted derivative seminorms;
only C_0 is evaluated numerically below, and no unrelated norm is claimed.

## A4. Full exterior velocity and residual remainder

Let a_i be the eleven original density exponents: the ten listed pairs
in PROOF.md plus3-bo. They are k, beta, and then at most beta2. The last
row carries a polynomial in log(r/R_b) of finite degree6; differentiation
does not increase this degree. In a mode sin(2ntheta), the stream
particular solution of -Delta psi=partial_x rho with density power a_i
has power a_i+1 and denominator (2n)^2-(a_i+1)^2. If a resonance occurs,
solving the constant-coefficient radial equation adds only a finite
power of log r. Thus every particular velocity has power a_i, times a
finite logarithmic polynomial. The leading k and beta rows are
nonresonant: their stream exponents k+1 and2k lie strictly between0 and2.
The canonical homogeneous stream terms at infinity are r^(-2n),
n>=1, and their velocities are r^(-2n-1), at most r^-3.

Accordingly U0=r^k V0(theta)+O(r^beta(1+log r)^q), while the original
finite expansion supplies every smaller power explicitly. The derivative
of rho0 starts with r^(k-1) and its next power is r^(beta-1). The sole
original residual term of power beta is Epsilon. Every other particular
product has exponent a_i+a_j-1<=beta2, except that leading pair, and
every homogeneous product has exponent a_i-2n-2<=k-4<beta2.
The original linear terms at power k cancel, at beta contribute to
Epsilon, and at all other powers are at most beta2. These assertions
also hold for their finite logarithmic factors.

For the new tail r^beta H, the forcing has even modes2n with1<=n<=522.
The stream exponent is beta+1=2k and its denominators are
(2n)^2-4k^2>0. The canonical outer integral is convergent because its
integrand is r^(beta-2n), whose exponent is less than-1.
The inner integral has an upper-limit particular contribution and a
finite integration constant. It yields precisely the r^(2k) particular
stream plus r^(-2n) homogeneous streams outside2T. Compact annular
terms only change the latter constants. Thus U[h_T]=r^beta V_H(theta)
plus finitely many r^(-2n-1) angular velocities. No growing homogeneous
term is introduced. The cross terms in (17) have respectively exponents
k+beta-1=beta2, beta+k-1=beta2, and2beta-1=4k-3<beta2, with all smaller
original powers and homogeneous terms decaying faster. Finite log degrees
may be collected in a single q; all constants may depend on T. This
proves (18) and the finite unweighted L2 residual, without a norm ceiling.

## A5. Local regularity and gauge

Here only the kinematic requirements of the task's P2 class are claimed:
rho in C^(2,alpha)_loc for some alpha in(0,1), a continuous centre factor
rho=x^2 y a with a(0)=1, the parities, canonical velocity and stated
sublinear density/first-derivative growth. P2 itself additionally requires
the stationary equation, which has not been proved. A C2 centre factor
is neither required by PROMPT nor asserted for the original modal trial.
The original density centre regularity is unchanged; its global spline
joins have the already verified C6 regularity.
The correction density and factor are C7, vanish identically on r<=T,
and have only the two new radial joins. Its stream is harmonic and
analytic inside T, and its velocity changes analytically there.
Consequently the residual is continuous on compact sets, which proves
local L2 directly. P_infty is not asserted. The canonical gauge is the
finite-mode Green inverse with no growing harmonic streams; equivalently
parities and sublinear velocity growth remove constant and affine
harmonic velocity freedoms, by the mollified harmonic Liouville argument
of topic104. Exact zero strain, not an approximately small value, then
preserves 3c0-psi_xy(0)=1.

The unweighted residual norm is not quantified. The construction proves
it is finite for each T; this alone does not claim monotonic growth with
T. The first review's request to say it grows is stronger than the proof
as written and is not used. No stationarity or decisive endpoint follows.
