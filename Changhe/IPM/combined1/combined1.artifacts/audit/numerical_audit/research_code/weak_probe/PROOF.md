# Weak residual probes and lower bounds on correction size

## Statement, hypotheses and scope

Fix the exact reference density rho and velocity U[rho] in the primary S1 chart, with c fixed. The velocity operator is U[h]=(-R1 R2 h,R1^2 h), with the Fourier convention of the campaign. Write V=cX+U[rho] and F=V.grad rho-rho. Suppose rho and U[rho] are smooth, U[rho]=O(r^gamma), grad rho=O(r^(gamma-1)) at infinity for some gamma<1, and div U[rho]=0. For the probes used below also assume F phi is integrable. This follows from F in L2 and phi in L2 for d2, whose full-plane L2 membership and norm were independently checked.

Suppose h belongs to H^(2+s)(R2), s>0, solves the same stationary equation at this c in distributions, and satisfies ||h||2<=m and ||grad h||infinity<=d. For every integer p>=2 set

phi_p(x,y)=y(1+x^2+y^2)^(-p), u=(1+r^2)^(-1), t=1-u,
N_p=||phi_p||2,
A_p=||phi_p[(3c+1)-2cp t]||2,
B_p=||u^p U[rho]||2,
C_p=||r u^p grad rho||2.

Then the following necessary inequality holds:

|<F,phi_p>| <= m [A_p+(1+2p)B_p+C_p+d N_p].                 (1)

Thus a positive value of |<F,phi_p>| minus the right side excludes the specified pair of bounds (m,d). In particular, for a correction ball X_(s,w)(h)<=R with X_(s,w)^2=||omega D2 J^s h||2^2+w1||D J^s h||2^2+w2||J^s h||2^2, w1>=2,w2>=1, one may take

m=R/sqrt(w2), d=R/sqrt(4 pi s(1+s)).                       (2)

A positive gap is an actual exclusion of this correction ball, independent of the validity or failure of any sufficient inverse theorem. It does not exclude arbitrary larger corrections, changes to c, or all exact stationary profiles.

This document proves (1), (2), and the exact finite-integral algorithm before its execution. Numerical exclusions are pending until valid interval results and independent reproduction are recorded.

## Weak inequality and removal of the cutoff

Expand the stationary equation:

0=F+V.grad h-h+U[h].grad rho+U[h].grad h.

For a real compactly supported smooth phi, integration by parts and div V=2c give

<F,phi>=<h,V.grad phi+(2c+1)phi>-<U[h],phi grad rho>-<U[h].grad h,phi>.

The vector Fourier multiplier of U has squared modulus xi1^2/|xi|^2<=1. Plancherel therefore implies ||U[h]||2<=||h||2. Cauchy-Schwarz yields

|<F,phi>|<=m(||V.grad phi+(2c+1)phi||2+||phi grad rho||2+d||phi||2).       (3)

This is Proposition W in T2-R3, rederived here. To use phi_p choose a smooth radial cutoff chi_R which is one for r<=R and zero for r>=2R, with |grad chi_R|<=C/R. Apply (3) to chi_R phi_p. The functions phi_p, V.grad phi_p, and phi_p grad rho all lie in L2 by the stated sublinear growth and p>=2. Dominated convergence handles these terms and the assumed integrability handles the left side. The extra cutoff term is phi_p V.grad chi_R. Since |V|<=C'(1+r), on its annular support this is at most a constant times |phi_p| for R>=1; its L2 norm tends to zero. Thus (3) holds for phi_p.

Direct differentiation gives grad phi_p=e_y u^p-2p y X u^(p+1), hence |grad phi_p|<=(1+2p)u^p, and |phi_p|<=r u^p. Also

cX.grad phi_p+(2c+1)phi_p=phi_p[(3c+1)-2cp t].

The triangle inequality bounds the first norm in (3) by A_p+(1+2p)B_p and the second by C_p, proving (1).

The norm X controls H^(2+s), because omega>=1 and |xi|^4+w1|xi|^2+w2 >=(1+|xi|^2)^2. Also ||h||2<=||J^s h||2<=X/sqrt(w2). The campaign's independently audited Fourier embedding gives ||grad h||infinity<=||h||H^(2+s)/sqrt(4 pi s(1+s)), proving (2). No parity improvement of this embedding is assumed.

## Exact radial integration

All norms are over the full plane. Angular orthogonality gives an angular factor pi for a nonzero sine or cosine mode and 2pi for cosine zero. There are no cross terms between different harmonics or vector components.

The reference fields have exact finite expansions

f=sum_(j,n) r^(-a)(1+r^2)^(b_j) P_(j,n)(t) trig(n theta),
b_j=(3+gamma-j(1-gamma))/2,

where a=3 for each velocity component and a=4 for each density gradient component. The existing independent differentiation code constructs the rational polynomials P. For the smooth fields here every P is divisible by t^2, checked exactly. Write P=t^2 Q. For a pair of branches i,j of the same angular harmonic, the radial factor in ||r^k u^p f||2^2 is

(1/2) integral_0^1 t^(k-a+4) u^(a-b_i-b_j+2p-k-2) Q_i(t) Q_j(t) dt.     (4)

We use (a,k)=(3,0) for B_p and (4,1) for C_p, so the power of t is exactly one in both cases. The exponent of u is greater than -1 for every included pair. After the exact shift t=1-u, the integrand is u^b times a polynomial. The integral is the finite sum sum_l q_l/(b+l+1), computed with outward Arb arithmetic. Off-diagonal branch pairs receive factor two. This proves the complete-plane values without quadrature or truncation.

The elementary probe terms are

N_p^2=pi/[2(2p-1)(2p-2)],
A_p^2=(pi/2) integral_0^1 t u^(2p-3)[(3c+1)-2cp t]^2 dt.               (5)

The already independently verified residual expansion is

F=r sum_(ell,n) u^(ell delta/2) P_(ell,n)(t) sin(n theta), delta=1-gamma.

Only n=1 contributes to the pairing, and

<F,phi_p>=(pi/2) sum_ell integral_0^1 t u^(ell delta/2+p-3) P_(ell,1)(t) dt.   (6)

Each polynomial is shifted exactly before interval integration. Endpoint exponents are checked to exceed -1. If that check fails the algorithm must stop, not report a finite norm. Formula (6) is signed; its absolute value is taken only after summing all branches.

## Verification evidence and dependencies

Dependencies are T2-R3 Proposition W, rederived above; the established Fourier embedding; the independent exact potential differentiation and residual reconstruction in ../radial_fourier and ../whole_plane_norms; finite polynomial integration; and outward Arb arithmetic. The coefficient and cached residual hashes are recorded in each result. Source code and numerical JSON live in code/ and verification/. There is no Lean build. Until independent numerical reproduction, all new outputs remain N4-ORIGIN.

## A rational rectangle in correction norms

The p=2 probe also permits a statement independent of all framework parameters. If the recorded intervals imply

|<F,phi_2>| > (27/10000)[A_2+5B_2+C_2+(3/100)N_2],                 (7)

then no correction can simultaneously satisfy ||h||2<=27/10000 and ||grad h||infinity<=3/100. This follows immediately from (1) with these two rational caps. The separate uniform-rectangle record checks (7) from the exact-integral output. It does not rely on any sufficient inverse theorem, background coercivity, or particular fractional exponent. The gradient cap remains essential; this is not an unconditional lower bound over every L2 correction.
