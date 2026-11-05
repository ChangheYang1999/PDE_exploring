# Independent reconstruction of the nonlinear Q estimate

Status: analytic review PASS, with a fresh continuum scalar certificate.
This verifies the fixed-q transport core without relying on a missing old
audit-program archive. It does not supply the background-energy constants.

## Fresh scalar input

For q=21/10 put H(t)=tq-t^-q-q(t-t^-1). Then
\[
\boxed{0\le H(t)\le\frac{53}{50}(t-1)^q\quad(t\ge1).}
\]
Its derivative factors exactly as
q t^(-q-1)(t^(q-1)-1)(t^(q+1)-1), so H is increasing. On t-1<=1/100,
H(1)=H'(1)=H''(1)=0 and H'''<=26.922<27, giving normalized bound
(9/2)(t-1)^.9<=9/20. On t>=64, H<=tq and
(t/(t-1))q<=(64/63)^3<53/50. The intervening compact interval is covered
by3210 exact rational closed intervals in the companion script. On each,
H(right)/(left-1)q is a containing upper by monotonicity.256-bit Arb
proves every such upper below53/50; the largest is below1.057102.
The result is `nonlinear_core_scalar_result.json`.

## Core Hilbert--Schmidt bound

For divergence-free a=U[k], and G=Jq z with arbitrary Schwartz z, the
symmetrized commutator minus its Bessel principal term has Fourier kernel
\((i/2)\eta\cdot\widehat a(\zeta)H(J\xi/J\eta)\), zeta=xi-eta.
The scalar inequality and |Jxi-Jeta|<=|zeta| give the majorant
\[
\frac{53}{100}|\eta\cdot\widehat a(\zeta)|
|\zeta|^q\min(J\xi,J\eta)^{-q}.
\]
Split min(Jxi,Jeta)^(-2q)<=Jxi^(-2q)+Jeta^(-2q). Divergence freeness
gives eta·ahat=xi·ahat, so the two integrals are identical. Their angular
integral is pi|ahat|², and their radial integral is
\(\int_0^\infty r³(1+r²)^{-q}dr=[2(q-1)(q-2)]^{-1}\).
With the campaign Fourier normalization this proves
\[
|Core(a;G)|\le\frac{53}{100}S_1\|D^qa\|2\|G\|2²,
\quad S_1=[2\sqrt{\pi(q-1)(q-2)}]^{-1}.
\]
No parity of the test z was used, so the bound applies to x_jg as required
by the coordinate proof. The coefficient k remains S1.

## Principal/Wiener constants

Optimized Fourier Cauchy-Schwarz with lambda+|xi|^(2q) gives the scalar
moment interpolation constant
\[
B_p=(4q\sin(\pi s))^{-1/2}
(1-s)^{-(1-s)/2}s^{-s/2},\quad s=(p+1)/q,
\]
for p0,1. The vector velocity multiplier has angular squared integralpi,
so its p0 constant is Ca=B0/sqrt2. For every unit vector e=(cos phi,sin phi),
the strain projection multiplier has angular squared integral
\[
\int_0^{2\pi}\cos²\theta\cos²(\theta-\phi)
\sin²(\theta-\phi)d\theta=\pi/8.
\]
Compared with the scalar2pi integral this gives Cs=B1/4. Thus the principal
and core constants used in `QNORM_NONLINEAR_BOUND.md` are correct.

## Review of the remaining coordinate proof

The exact xJq commutator identity, the X=Y+Z split, and the direct
divergence-free transport cancellations have the displayed signs. The
operator commutator upper Cc follows from the stated mean-value inequality,
Young convolution, and ||grad z||A<=S1||Jqz||. Its use is only in the
lower-order cross term, without asserting the sharper energy constant as
an operator norm.

The two product estimates use the elementary positive-frequency inequality
J(eta+zeta)^s<=2^(s-1)(Jeta^s+|zeta|^s), s>=1. Their interpolation powers
reduce to1-1/q as stated. Since Q(g)>=M, the negative powers of Q in those
ratios are bounded in the correct direction. This verifies each term of
the final LQ formula, including the2(qv+P+T) coefficient.

For W_a=sqrt(1+a²r²),0<a<=2, replace2x by ax in the exact identity. Then
aX<=Q_a and aZ<=2Z; the same displayed a2 loss is an upper bound. The
coefficient inequalities ||Jqk||<=Q_a(k),||Dqk||<=Q_a(k) are exact, so no
new norm-conversion constant or strain-hyperplane restriction enters.

The resulting inequality retains its explicit outside-ball scope. It is
compatible with, and sufficient for, the forced-evolution bridge. No
global Q dissipativity is inferred from this review.
