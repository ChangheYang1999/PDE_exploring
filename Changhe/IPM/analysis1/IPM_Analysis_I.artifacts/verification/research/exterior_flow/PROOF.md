# Exterior velocity, axis quotients and outward drift

2026-10-20. Independent argument written before computation. Application requires every check below to pass. This concerns the exact normalized modal trial already used by the residual certificates, not an exact IPM solution.

## Statement and input

Write t=log r, t_b=2289893859708677/281474976710656, tau=t-t_b>=0, k=1615536043799051/9007199254740992 and c_l=1/k. The exact exterior trial is

rho(r,theta)=exp(3t_b) sum_(j=0)^260 sum_beta exp(beta tau)c_(j,beta)(tau) sin((2j+1)theta).

There are eleven exact rational exponents. Ten coefficient polynomials are constant, with beta=k-j(1-k)-2l for the ten pairs in the audited JSON. The last exponent is3-b_o, b_o>120, and its polynomial degree is at most6. Coefficients are rational affine functions of the single exact normalization parameter z, contained in a previously independently certified interval. Put c_(261,beta)=0. We require the pinned exact coefficient table and the independently audited canonical lower Green moment at t_b in each of261 modes. Their verification is a dependency, not supplied anew by importing the data.

For omega=1-k>0 and any T>=0, the finite constructions below give constants P_T and Q_T such that, for every tau>=T and every theta in(0,pi/2),

|U_r/r|<=P_T exp(-omega(tau-T)),
|U_1/x|<=Q_T exp(-omega(tau-T)),
|U_2/y|<=Q_T exp(-omega(tau-T)).

Continuous extension supplies the axis values of the quotients. Thus U=O(r^k) and the component quotients tend uniformly to0, including the axes. If P_T<c_l, then X dot(c_l X+U)>=(c_l-P_T)|X|^2 for r>=exp(t_b+T). If Q_T<c_l, both drift component quotients V_1/x,V_2/y are positive in that exterior quadrant. This verifies only an exterior part of the global-flow hypotheses.

## Two reconstructions of the velocity

Let m=2n, n=1,...,261, and let rho_j(r) be the radial coefficient of sin((2j+1)theta) in rho. The canonical normalized density moments are

i_n(t)=r^(-m-4) integral_0^r s^m rho_(n-1)(s) ds,
j_n(t)=r^(m-4) integral_r^infinity s^(-m) rho_n(s) ds,
H_j(t)=rho_j(r)/r^3, r=exp(t).

Their normalizing power is r^4 relative to the usual moments r^(-m) integral_0^r s^m rho_(n-1) ds and r^m integral_r^infinity s^(-m) rho_n ds. The previously established canonical identities are

i_n'=-(m+4)i_n+H_(n-1),
j_n'=(m-4)j_n-H_n,
H_j(t)=exp(-3tau) sum_beta exp(beta tau)c_(j,beta)(tau).

These follow by differentiating the lower and upper radial integrals. At t_b, i_n=i_(n,0) is the certified lower moment. The upper moment is uniquely fixed by the convergent integral to infinity. Convergence holds because beta+1-m<0 for every mode and every exponent. More precisely the canonical upper integral imposes exp(-(m-4)tau)j_n(t_b+tau) -> 0 as tau -> infinity. This condition eliminates its homogeneous constant for every m, including m=2 (whose homogeneous solution decays) and m=4 (whose homogeneous solution is constant). Decay of j_n alone would not give uniqueness when m=2.

For a polynomial P and nonzero lambda, the polynomial inverse I_lambda P is the unique polynomial Q satisfying Q'+lambda Q=P. Uniqueness follows from the highest coefficient; descending recurrence gives Q_d=P_d/lambda and Q_l=(P_l-(l+1)Q_(l+1))/lambda. Equivalently

Q_l=sum_(j=l)^d (-1)^(j-l) j! P_j/(l! lambda^(j-l+1)).

All denominators beta+1+m and beta+1-m are checked nonzero in exact arithmetic. Set

Q_i=I_(beta+1+m)c_(n-1,beta),
Q_j=-I_(beta+1-m)c_(n,beta),
C_i=i_(n,0)-sum_beta Q_i(0).

Solving the moment equations gives

i_n=exp(-(m+4)tau)C_i+sum_beta exp((beta-3)tau)Q_i(tau),
j_n=sum_beta exp((beta-3)tau)Q_j(tau).

The polar velocity coefficients in U_r/r=sum_n p_n cos(m theta), U_theta/r=sum_n s_n sin(m theta) are

p_n=(m/2)exp(2t)(i_n-j_n),
s_n=exp(2t)[m(i_n+j_n)-H_(n-1)-H_n]/2.

Therefore each has the same transient exp(2t_b)(m C_i/2)exp(-(m+2)tau), and their beta polynomials, before multiplication by exp(2t_b), are respectively

p_beta=m(Q_i-Q_j)/2,
s_beta=[m(Q_i+Q_j)-c_(n-1,beta)-c_(n,beta)]/2.

The independent Green-forcing reconstruction starts with

F_beta=[(beta+1-m)c_(n-1,beta)+(beta+1+m)c_(n,beta)+c'_(n-1,beta)+c'_(n,beta)]/2,
q_plus=I_(beta+1+m)F_beta,
q_minus=-I_(beta+1-m)F_beta.

It gives p_beta=-(q_plus+q_minus)/2 and s_beta=(q_minus-q_plus)/2, with transient -H_n/2 from the audited homogeneous Green coefficient. The exact polynomial identities

q_plus=(c_(n-1,beta)+c_(n,beta))/2-m Q_i,
q_minus=-(c_(n-1,beta)+c_(n,beta))/2+m Q_j,
H_n=-m C_i

prove the agreement of the two exact constructions. In the code the first two identities are checked for exact affine polynomial coefficients. The homogeneous boundary identity is justified by the canonical moment definitions and the audited upstream formulas; its new numerical check is only overlap of two valid enclosures, not an equality proof or fresh boundary certification. The two methods share the already audited boundary input and normalization enclosure; the new check does not claim fresh independent boundary integration. Evaluating each coefficient separately discards correlations in the common parameter z. This enlarges the set of possible coefficients and can only enlarge these upper bounds.

## Uniform angular estimate

The finite geometric-sum identity gives |sin(m theta)|<=m|sin theta| for integer m. For even m, reflection about pi/2 gives also |sin(m theta)|<=m|cos theta|. Consequently

|tan(theta)sin(m theta)|<=m,
|cot(theta)sin(m theta)|<=m.

Since U_1/x=U_r/r-tan(theta)U_theta/r and U_2/y=U_r/r+cot(theta)U_theta/r, the sums sum_n|p_n| and sum_n(|p_n|+m|s_n|) give P and Q. These inequalities hold uniformly up to the axes by continuity of the finite trigonometric quotients. No angular grid or deletion of high modes is used.

## Two different bounds over the infinite radial interval

Every velocity constituent is exp(-a tau)P(tau), with a=1-beta or a=m+2. All have a>=omega. The sole zero value of a-omega occurs for beta=k, and its polynomial is constant.

Method A, Arb: bound coefficients in the original tau basis. For d=a-omega>0,

sup_(tau>=T) tau^l exp(-d tau)=x_l^l exp(-d x_l), x_l=max(T,l/d).

This follows by differentiating the nonnegative monomial. For d=0 only l=0 occurs and the supremum is1. Multiplication by exp(-omega T), then summation of absolute coefficient bounds, gives an upper bound for exp(omega(tau-T)) times the constituent. This method uses exact critical points and Arb exponential enclosures.

Method B, mpmath.iv: reconstruct the polynomials from the density moment equations by the descending recurrence, then shift P(T+sigma)=sum_j D_j sigma^j. For d=a-omega>0, the exponential series gives

sigma^j exp(-d sigma)<=j!/d^j, sigma>=0.

Hence exp(-aT) sum_j |D_j| j!/d^j is an upper bound for the same weighted constituent. For d=0 the constant case is exact. This method uses a shifted basis and the positive exponential-series bound, not the critical-point formula. It may give a larger upper bound. Agreement of upper bounds is neither required nor asserted. Each bound must independently be below any published rational upper bound; the final bound is the larger of their upper endpoints.

Summing all261 modes and all11 exponent families, including the homogeneous transients, yields the stated P_T and Q_T. Exact scalar comparisons also certify a public radius and any displayed drift margin. Finiteness and positivity checks are mandatory, and no floating approximation is used in a comparison.

## Explicit corollaries to be checked in the output audit

The planned rational comparisons use the full bounds from both methods, without assuming one contains the other. At T=1/16, if P_T<1.744311, exp(t_b+T)<3634 and c_l-P_T>3.83, then

X dot V(X)>3.83 |X|^2 for |X|>=3634.

At T=1/8, if P_T<0.104, Q_T<0.313 and exp(t_b+T)<4000, then, for r>=4000,

|U_r/r|<0.104(4000/r)^(1-k),
|U_1/x|, |U_2/y|<0.313(4000/r)^(1-k),
X dot V>5.47 r^2,
V_1/x>5.26 and V_2/y>5.26.

For the last line the output audit also directly checks c_l-P_T>5.47 and c_l-Q_T>5.26. The replacement of exp(t_b+T) by4000 increases the decay factor because1-k>0. The product estimates extend continuously to the closed quadrant. These explicit corollaries are conditional on the saved output audit returning PASS; no decimal is used as a floating comparison.

## Execution and interval implementation

The mpmath.iv endpoint conversion uses the private _mpi_ representation of mpmath1.3.0. The code pins that version, rejects the negative bit-count encodings for infinities and NaNs, and checks exact signed-mantissa and power-of-two decoding on rational interval contracts. Arb uses python-flint0.9.0 at512 bits; mpmath.iv uses180 decimal digits. These are implementation dependencies, not an interchangeability claim between their endpoints.

The saved-number audit checks source hashes, summary contracts and the13 exact public comparisons. It does not execute the coefficient recurrences. The final verdict therefore also binds an actual completed core run and its log to the exact source, proof, output and dependency hashes. The main residual worker was paused during this computation so the one-heavy-process restriction was respected.

## Scope

This proof establishes no interior no-zero theorem, axis sign below the certified radius, uniqueness at the two equilibria, finite transit time, orbit cost, smooth weight, coupled inverse, nonlinear closure or decisive endpoint. It leaves the center forcing-space obstruction unchanged. It does supply the stronger uniform component-quotient tail needed by the conic-weight analysis, and the O(r^k) hypothesis of the pure-transport far-field lower bound.
