# Hydrostatic far-field trace diagnostics and their limits

Written UTC 2026-10-21T10:49:47.781975+00:00 before the evaluator. Result208 is an independent coefficient calculation and a conditional asymptotic audit. It is not a proof of a hydrostatic or original profile.

## Setting and exact trace

Fix c>1, P>1, p=1-1/P in(0,1), L>0. The finite trial density is

    g(r,theta)=r sin(theta) w sum_k (1-w)^k beta_k(1-2w) cos(2k theta),
    r=L sqrt(1-w)/(2w)^P,  0<w<=1.

Every beta_k is a finite polynomial in its stored local coordinate. Let b_k=beta_k(1), b'_k=partial_t beta_k(1), and let

    B(z)=sum_k b_k T_k(2z-1)=sum_j a_j z^j,
    F(s)=(1+s^2)^(p/2) Theta(atan s).

Here T_k is the Chebyshev polynomial, z=cos^2(theta), and all coefficients are interpreted as exact stored binary numbers. Put pref=L^(1/P)/2. Since w=(L/r)^(1/P)/2+O(r^(-2/P)),

    Theta(theta)=pref sin(theta) B(cos^2(theta)),
    F(s)=pref sum_j a_j s(1+s^2)^((p-1)/2-j),
    K=Theta(pi/2)=pref a_0,
    Q=f_xx(0,1)=pref[(p-1)a_0+2a_1].                    (1)

The trace formula is an exact limit. The exponent is the stored p; it need not equal1/c exactly when P is rounded. The independent evaluator must preserve this distinction. The linear leading residual then contains (cp-1)r^pTheta. At c=3, for example, a binary P near1.5 can give a nonzero rounding-level coefficient.

The next radial coefficient also follows directly. Set zeta=(L/r)^(1/P). The implicit map gives w=zeta/2-zeta^2/(8P)+O(zeta^3). Consequently

    A2(theta)=L^(2/P)sin(theta) sum_k[-b_k/(8P)-k b_k/4-b'_k/2]cos(2k theta),
    g=r^p Theta+r^(2p-1)A2+O(r^(3p-2)).                (2)

This expansion and its angular derivatives hold for each fixed finite coefficient vector. Its constants need not be uniform under refinement.

## Convergent finite-part formula without derivative differencing

For f=r^pTheta define q(s)=f_xx(1,s)=p(p-1)F-2(p-1)sF'+s^2F''. Smooth even vertical and odd horizontal parity imply F(s)=Ks^p+(Q/2)s^(p-2)+O(s^(p-4)) at infinity and F=O(s) at0. Hence

    Cp(f)=int_0^infinity s[q(s)-Q s^(p-2)]ds
         =(p+1)(p+2) FP int_0^infinity sF(s)ds,       (3)

where FP subtracts K S^(p+2)/(p+2)+Q S^p/(2p) from the integral up toS. To prove(3), two integrations by parts give

    int_0^S s q = S^3 F'-(2p+1)S^2F+(p+1)(p+2)int_0^S sF.

Insert the two large-S terms. The S^(p+2) terms cancel and the S^p term is Q S^p/p; all remainders tend to0. The zero-end terms vanish by F=O(s). The integrand in the first form is O(s^(p-1))+O(s^2) at0 and O(s^(p-3)) at infinity, so it is genuinely integrable.

Write I_j=FP int_0^infinity s^2(1+s^2)^((p-1)/2-j)ds and

    J_p=int_0^infinity (1+s^2)^((p-3)/2)ds>0.

Ordinary integration by parts, with their explicit leading terms subtracted when needed, gives

    I_0=(1-p)J_p/[p(p+2)],  I_1=-J_p/p,
    I_2=J_p/(3-p),
    I_(j+1)=I_j(2j-p-2)/(2j+1-p), j>=2.              (4)

For completeness, differentiate s(1+s^2)^((p-1)/2) to relate FP int(1+s^2)^((p-1)/2) to J_p, then differentiate s(1+s^2)^((p+1)/2) to obtain I_0. For I_1 use s^2=(1+s^2)-1 in its integrand and subtract the preceding finite integral. Differentiating s(1+s^2)^((p-3)/2) gives I_2=J_p/(3-p), its endpoint values being0. For j>=2 substitute u=s^2/(1+s^2); the integral is B(3/2,j-(p+2)/2)/2, and integration by parts in the beta integral gives the recurrence. All beta arguments here are positive; no analytic continuation defines these finite parts. The same substitution gives J_p=sqrt(pi)Gamma(1-p/2)/(2Gamma((3-p)/2)). Therefore the finite polynomial formula is

    Cp=(p+1)(p+2) pref sum_j a_j I_j.                 (5)

The polynomial coefficients and the two exceptional weights must be evaluated with sufficient precision because cancellations grow with degree. Increasing precision tests observed numerical stability, not a rigorous enclosure.

## Independent integral checks

For a_j x^(2j)y r^t, t=p-1-2j and m=2j, direct Cartesian differentiation atx=1 gives

    q_j(s)=s[m(m-1)r^t+t(2m+1)r^(t-2)+t(t-2)r^(t-4)], r=sqrt(1+s^2).

This gives an independent derivative expression for the first form of(3). To integrate without subtracting nearly equal powers at huge s, take a finite S>1 and expand

    F(s)=s^p sum_n d_n s^(-2n),
    d_n=pref sum_(j<=n) a_j binomial((p-1)/2-j,n-j).

Then d_0=K,2d_1=Q. The full tail after the two subtractions is

    sum_(n>=2) d_n S^(p+2-2n)/(2n-p-2)

for the finite-part moment, and the same series with multiplier2n(2n-1) for the q-form. These converge absolutely forS>1 because the binomial series is analytic in s^(-2) on|s^(-2)|<1. Compare lengths and precisions. On[0,S] evaluate F and the displayed Cartesian q directly by multiprecision quadrature; subtract the elementary leading integrals. No numerical derivative or producer inverse is reused. Manufactured traces include the result197 trace, whose Cp=0 exactly, and individual modes and their combinations with known nonzero Cp.

## What a nonzero Cp does and does not imply

Assume now the ideal relation cp=1 and a termwise canonical homogeneous expansion, so that its first nonlinear correction is governed by

    E(theta)=V[f].grad f on the unit circle - D A2(theta), D=c-1.

At fixedy>0 the exact canonical inverse identity gives

    V2[f](x,y)=V2[f](0,y)+Cp|x|^p+O(x^2 y^(p-2)).

V1[f] is smooth near the positive vertical axis, f_x=O(x), and f_y=pK y^(p-1)+O(x^2). Thus the homogeneous nonlinear transport has cusp coefficient pKCp, while the density coefficient that would cancel it has coefficient pKCp/D. A fixed smooth A2 cannot cancel a nonzero cusp exactly. In a small fixed angular window the continuous leading residual coefficient is therefore not identically0. This is a qualitative obstruction to exact termwise cancellation for that fixed trace and smooth A2. It does not identify where a finite-radius residual maximum lies.

If the leading normalization denominator is used, it equals2K+O(delta^2) near the positive axis, delta=cos(theta). Therefore the signed leading coefficient of R_h/N_f has cusp coefficient pCp/2, not pCp/D. The latter belongs to the required correction divided byK. For an actual finite field, the inverse/expansion remainders and the term(cp-1) must be separately assessed before fitting this law. On-axis core corrections and nonuniform angular layers are not covered by a bare formal expansion.

A uniform bound proportional only to|Cp| over growing smooth trial spaces does not follow. For0<p<1 the even analytic functions

    h_e(x)=(x^2+e^2)^(p/2)-e^p

satisfy h_e(0)=0 and sup_x ||x|^p-h_e(x)|<=e^p, by concavity of t^(p/2). They approximate the cusp arbitrarily well in the uniform norm while their second derivative at0=p e^(p-2) diverges. On a compact interval they can also be approximated uniformly by even polynomials, preserving value0 by subtracting the polynomial's constant term. Multiply by a smooth angular cutoff within the axis window if needed. Smooth angular trial functions thus approximate the required cusp arbitrarily closely without an a priori uniform derivative bound. For the finite Q basis, endpoint values and first derivatives of sufficiently high-degree beta_k can be prescribed independently by elementary Hermite interpolation, so smooth trigonometric approximations are not ruled out by the radial representation alone.

Consequently stable nonzero Cp under refinement is evidence of failure of exact smooth coefficient compatibility; it is not by itself proof of a nonvanishing sampled residual floor, a numerical nonconvergence theorem, or a hydrostatic NO result. A quantitative bound requires a fixed finite space or common higher-derivative bounds and control of the asymptotic remainder. The limits of radial distance and increasing resolution need not commute.

## Scope and verification record

This proof uses the canonical hydrostatic inverse, not the full Laplace inverse of original SettingIII. The independent evaluator records frozen coefficient hashes, actual exponents, Cp/K, K and Q, precision changes and trace limits. It will compare producer diagnostics when published but does not import their code. Any selected-window residual audit uses the independently manufactured185/187 inverse. The original prompt's endpoint remains OPEN.
