# Independent polar whole-plane weak test for scaled generators

## Statement and exact hypotheses

Use the exact rational candidate016 source already independently
verified in ../candidate016_point, with c>1, gamma=1/c and
delta=1-gamma. The potential class and canonical velocity are those
of ../scaled_field_audit/PROOF.md. Let h be a real S1-symmetric L2
correction solving (cX+U[rho+h]).grad(rho+h)-(rho+h)=0 weakly.
Assume the canonical velocity decomposition, div U[h]=0 and
||U[h]||2<=||h||2. Every weak product uses its locally integrable
representative. These are exactly the hypotheses of the audited
weak-distance theorem; no normalization or contact term is changed.

For the frozen rational polynomial P=t^K, K>=(n-1)/2, and any positive odd n, set
phi=r(1-t)^2 P(t)sin(n theta), t=r^2/(1+r^2). P is divisible by
t^((n-1)/2), which ensures smoothness at the origin. The probe decays
as r^-3 and its gradient as r^-4. Let

    I=int F phi, M=||(2c+1)phi+(cX+u).grad phi||2,
    C=||phi grad rho||2, Hbar>=||grad phi||infinity.

Then every admissible correction has

    ||h||2 >= 2|I|/(M+C+sqrt((M+C)^2+4Hbar|I|)).          (1)

The compact-cutoff subtraction and integration by parts give
|I|<=(M+C)||h||2+Hbar||h||2^2. Growth of the smooth background as
r^gamma, gamma<1, and the escaping-annulus L2 mass justify the cutoff
limit. Solving that quadratic proves (1). The all-c interpretation
requires the separate leading-tail pinning theorem.

## Independent polar field reconstruction

Put v=1-t and a_j=(j+1)delta/2, so p_j=2-a_j. The potential has form
sum S^p_j A_jn(t)cos(n theta), where n is even and S=1+r^2.
Each A is reconstructed from the raw generator by the independent
shifted-Legendre coefficient identity

    P_N(2z-1)=sum_k (-1)^(N+k) C(N,k) C(N+k,k) z^k.

For scale R and L=R^2(1-t)+t, its contribution is

    sum_k c_k R^(2q) t^(m+w+k) v^q / L^(w+q+k).

The audited Rat arithmetic is a shared primitive; its generator and
Cartesian differentiation routines are not used for this reconstruction.
Define E_p A=2tv A'+2ptA. This is Euler radial differentiation after
extracting S^p. For each even n let B=E_p^2 A-n^2 A and D=E_p B-2B.
Then rho=-partial_y Delta chi gives density numerators

    R_(n-1) += (D+nB)/(2t^2),
    R_(n+1) += -(D-nB)/(2t^2).

The stream function psi=partial_xy chi gives

    S_(n+2) += [E_p(E_p A-nA)-(n+2)(E_p A-nA)]/(4t^2),
    S_(n-2) += -[E_p(E_p A+nA)+(n-2)(E_p A+nA)]/(4t^2).

Fold negative sine frequencies with sign reversal and discard zero.
Sum each numerator before dividing by t^2; the required two origin
zeros are verified exactly. This proves

    rho=r sum v^a_j R_jn(t)sin(n theta),
    psi=r^2 sum v^a_j S_jn(t)sin(n theta).

Let T_d(A,a)=(d-2at)A+2tvA'. Then
u_r=-r sum n v^a_j S_jn cos(n theta),
u_theta=r sum v^a_j T_2(S_jn,a_j)sin(n theta),
rho_r=sum v^a_j T_1(R_jn,a_j)sin(n theta), and
rho_theta/r=sum n v^a_j R_jn cos(n theta).
The R=1 specialization is checked exactly against the earlier independent
polynomial polar fields. Point values of the scaled fields are compared
against the independently audited raw Cartesian point record.

## Complete angular assembly

Write Q=(1-4t)P+2tvP' and A0=(2c+1)P+cQ. The drift field divided by
r v^2 has sine n amplitude A0. Each background stream mode m contributes
v^a_j times

    (n T_2(S_jm)P-m S_jm Q)/2 at n+m,
    (-n T_2(S_jm)P-m S_jm Q)/2 at n-m,

again folding negative frequencies. Squaring this complete field uses
angular orthogonality and all ordered radial cross terms within each
frequency. Thus its squared norm is pi/2 times a sum of
int_0^1 t v^(1+(ell+ell')delta/2) A_ell A_ell' dt.

For C^2, for density frequencies m,l define

    A_ml=2[m=l]-[|m-l|=2n]+[m+l=2n],
    B_ml=2[m=l]-[|m-l|=2n]-[m+l=2n].

The exact integral of sin(n theta)^2|grad rho|^2 gives pi/8 times the
sum over every ordered pair of

    int_0^1 t v^(1+(j+k+2)delta/2) P^2
          (A_ml T_1(R_jm)T_1(R_kl)+B_ml m l R_jm R_kl)dt.

These coefficients follow by product-to-sum, including equal and
opposite interacting frequencies. The direct I is assembled from
c r rho_r-rho+u_r rho_r+u_theta rho_theta/r, projected onto sine n.
A second pairing is -int rho[(2c+1)phi+(cX+u).grad phi]. All angular
modes and branches are retained; agreement of the two pairings is required.

## Independent rational integration

After v=1-t every scalar moment has form int_0^1 v^b N(v)/D(v)dv,
where b>-1 and D is a product of positive powers of1+624v (the second stored denominator has exponent zero).
Divide N=QD+R exactly. For each coprime factor D_i=(1+a_i v)^m_i,
let E_i=D/D_i. Extended Euclidean polynomial division computes an exact
inverse B_i of E_i modulo D_i. Put R_i=(R B_i) mod D_i. Then

    R/D=sum_i R_i/D_i,

because both sides have the same residues modulo every D_i and both
combined numerators have degree less than deg D. The implementation
also replays the full exact polynomial identity. Expanding
R_i((z-1)/a_i) gives the coefficients of each (1+a_i v)^(-k).
This is independent of the peer's local reciprocal Taylor algorithm.

Polynomial moments are1/(b+j+1). Each pole moment is evaluated directly
as 2F1(k,b+1;b+2;-a)/(b+1), with outward Arb arithmetic. The installed
implementation's bc and abc integer-relation flags are valid because
c-b=1 and c-a-b=1-k are exact integers. This avoids the peer's recurrence
in k. Positive endpoint integrability and at least150relative accuracy
bits are required before accepting any nonzero moment. Exact zero
numerators are handled separately. Denominator factors have no zeros
on[0,1], so no principal-value convention is involved.

## Gradient and evidence

The radial and angular probe amplitudes are v^2 Q and n v^2 P.
Their maximum bounds the Euclidean gradient because sin^2+cos^2=1.
The independent rational subdivision and interval mean-value argument
already used in ../new_successor_weak verifies the frozen Hbar again.
Source hashes, exact probe JSON, pair counts, endpoint exponents,
whole-plane moment records, comparisons, strict rational floors and
real times are stored in verification/. No candidate is called exact,
and no inverse or nonlinear closure is claimed by this distance test.

## Factored localization for candidate016

For this audit n=23,K=2400, or n=19,K=1800. The exact raw coefficient hash is a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42. Only scales1 and25 occur. Their radial denominator is 1+624v>0. All field reconstruction formulas above are used unchanged.

Do not expand t^K. Write Q=t^K q_K, where q_K=(2K+1)-(2K+4)t. Remove t^K from every M amplitude and from each factor phi in C, and from I. The preceding angular formulas then apply with P=1 and Q=q_K. Each norm integral has the additional factor t^(2K), and each pairing has t^K. The factor t from the polar measure in the formulas above stays in the rational numerator. This is a finite exact factorization, with no truncation.

For a rational numerator A(t)=P(t)/D(t), the scalar integral becomes

    J=integral_0^1 v^b (1-v)^L N(v)/D(v) dv,
    N(v)=(1-v)P(1-v), b>-1, L=K or2K.

The exact CRT decomposition described above is unchanged. Replace each polynomial moment by B(b+j+1,L+1) and each pole moment by

    B(b+1,L+1) 2F1(k,b+1;b+L+2;-a).

The beta formula follows from its defining integral. The pole formula follows by termwise binomial expansion for small a, then analytic continuation along a>0; both sides are real analytic and the integrand has no pole on[0,1]. Each pole is evaluated directly by Arb, independently of the peer's recurrence in k. The exact integer-parameter flags are valid: c-b=L+1 and c-a-b=L+1-k are integers in the hypergeometric parameters. Polynomial beta terms use their positive recurrence starting from a gamma quotient. Every CRT numerator identity is replayed exactly, and each nonzero scalar integral must retain at least150 relative accuracy bits.

The gradient supremum is certified by a complete critical-point calculation. The radial amplitude is t^K(1-t)^2[(2K+1)-(2K+4)t] and the angular amplitude is n t^K(1-t)^2. The angular maximum is at t=K/(K+2). The two radial critical points in(0,1) are the roots of

    (2K+4)(K+3)t^2
      -[(K+2)(2K+1)+(K+1)(2K+4)]t+K(2K+1)=0.

Both endpoint amplitudes vanish. The maximum of the three absolute values bounds the Euclidean gradient because the angular factors have squared sum1. The peer's exact rational H is accepted only if it strictly exceeds all three enclosing values. Thus the same quadratic root can be compared without ambiguity from different rounded gradient caps.

An R=1 field calibration compares every coefficient with the earlier polynomial polar implementation. The actual R25 fields reproduce six separately accepted physical point values. The complete M,C,I and integration-by-parts I are compared with the independent raw Cartesian path. Small scalar fixtures compare factored and explicitly expanded localization; no foreign code is executed. A successful scalar primitive test alone does not certify the candidate.
