# The next vorticity relation at a curved simple endpoint

Status: complete standalone informal proof, with a symbolic calculation and a separately implemented exact rational-series check. The initial proof and OPEN coefficient evaluation are preserved in verification/PROOF_preparation.md. This theorem concerns only the explicit local family below, not all simple endpoints or global B2 profiles.

## Exact problem

Set beta=2 and use signed s=y_*-y. For nonzero C,k and any real H, let

    B=s+k s^2+a s^13, a=-Ck/260,
    T=C s^10 tau, eta=s^6 rho(H-CJ),
    tau=exp int_0^s[(8+2B')/B-10/u]du,
    rho=exp int_0^s[(5+B')/B-6/u]du,
    J'=s^3 tau/((B/s)rho), J(0)=0,
    v=-(B''+eta)/2.

These are the P303 analytic fields. Let I be any meromorphic primitive of

    f=[-4B'''+6B''(8+2B')/B+6eta(8+2B')/B-4eta']/(BT),

and D=T^2 I. The residue of f is zero for the specified a; hence D is analytic. Changing the primitive by a constant changes D by a multiple of T^2, of order twenty.

A smooth B2 profile has the additional vorticity coefficient gamma=Omega_xxx(0,y) satisfying

    B gamma'-(13+3B')gamma=-D+2v'eta-6v eta'.     (1)

All primes in this packet mean d/ds. This follows independently by substituting Psi=h0 x+v x^3/3+p5 x^5/120 and Theta=T x^2/2+D x^4/24 into the original vorticity equation, with gamma=-p5-2v_yy. The x^3 coefficient, multiplied by six, is b gamma_y+(13-3b_y)gamma-D-2v_y eta+6v eta_y; d_y=-d_s gives (1).

## Necessary and sufficient local residue test

Let Z=s^16 zeta(s), where zeta=exp int_0^s[(13+3B')/B-16/u]du is an analytic unit with zeta(0)=1. Equation (1) is equivalent away from zero to

    (gamma/Z)'=g,
    g=(-D+2v'eta-6v eta')/(BZ).                 (2)

The right side is meromorphic, with pole order at most twelve, because eta has order six, v has order zero, eta' has order five, and D has order at least nine. Therefore gamma is analytic through zero exactly when the residue of g vanishes. If it vanishes, g has a convergent meromorphic primitive with pole order at most eleven, and its product with Z is analytic of order at least five. Conversely a nonzero residue forces a nonzero s^16 log|s| term in gamma, which fails to be C^16; adding a homogeneous multiple of Z cannot cancel it. The free constant in I does not affect the residue, since its contribution to g has order three.

For the decisive coefficient only finitely many Taylor coefficients are needed. Replacing B by B0=s(1+ks) changes T/T0, rho/rho0 and zeta/zeta0 by 1+O(s^12), where

    T0=C s^10/(1+ks)^6,
    eta0=s^6(1+ks)^-4(H-CJ0),
    J0'=s^3/(1+ks)^3,
    Z0=s^16/(1+ks)^10.

In particular eta-eta0=O(s^18). The correction to D through degree sixteen is zero, since the change of its primitive first occurs at logarithmic/constant order; the tuned sum has zero logarithmic coefficient. The correction to 2v'eta-6v eta' at degree sixteen is 1092 a H s^16, from v-v0=-78a s^11+O(s^18). The relative denominator change has order twelve, which cannot change a residue whose most singular term is s^-12. Thus the residue equals the quadratic calculation plus 1092aH.

## Evaluation of the residue

The exact answer is

    Res_0 g = -9 C k(231 H+k^7)/385.               (3)

Here is a finite coefficient derivation. For B0=s(1+ks), write

    J0=sum_{j>=0} (-1)^j binom(j+2,2) k^j s^(j+4)/(j+4).

This is the convergent primitive of s^3/(1+ks)^3 for |ks|<1. Decompose I0 into the curvature part, the homogeneous eta part, and the forced eta part. Only the first two can contribute to the residue of -D0/(B0 Z0). They are

    Icurv = (12k/C) sum_{j=0}^5 F_j k^j s^(j-11)/(j-11),
    (F_0,...,F_5)=(10,44,76,64,26,4),
    IH=-(36H/(5C))s^-5-(4kH/C)s^-4.

The forced eta part of I0 has pole order at most one plus a logarithm, while
T0^2/(B0 Z0)=C^2 s^3/(1+ks)^3, so that part has no residue after multiplication. This statement is only a finite coefficient computation: the untuned quadratic family itself need not have analytic D0.

Using [s^j] for a Taylor coefficient and Res for a Laurent residue, the curvature contribution follows from the finite sum

    Res[-C^2 s^3 Icurv/(1+ks)^3]
      = -12 C k^8 sum_{j=0}^5
          F_j (-1)^(7-j) binom(9-j,2)/(j-11)
      = -16 C k^8/385.

The IH contribution is -(88/5)CHk. Thus the complete D contribution is

    -(88/5)CHk-(16/385)Ck^8.                     (4)

For the other two terms, v0=-k-eta0/2 gives

    2v0'eta0-6v0 eta0'=6k eta0'+2eta0 eta0'.

Put L=H-CJ0. Then eta0=s^6(1+ks)^-4 L. Direct differentiation and division by B0 Z0 give the residues

    Res[6k eta0'/(B0 Z0)]
       = -6kC [s^11] (6+2ks)(1+ks)^4 J0
       = Ck^8/55,                              (5)

    Res[2eta0 eta0'/(B0 Z0)]
       = [s^5] 2(6+2ks)L^2
           -2C Res[L/(s^2(1+ks)^2)]
       = (82/5)CHk.                            (6)

For (5), the rational term containing J0' has no residue by polynomial degree, and the displayed coefficient uses only j<=7 in J0. For (6), the J0^2 term begins in degree eight, so only the H-C cross term contributes to [s^5]; J0 starts in degree four, so only H contributes to the remaining residue. These finite sums prove (4)-(6) by rational arithmetic, without an infinite summation interchange.

Their sum is -(6/5)CHk-(9/385)Ck^8. The degree-thirteen correction established above adds 1092aH=-(21/5)CHk. This proves (3).

## Consequences and exact scope

Since Ck is nonzero, an analytic gamma solving (1) exists if and only if

    H=-k^7/231.                                (7)

When (7) holds, all such analytic solutions differ by a constant multiple of Z. They vanish to order at least five. When it does not hold, every punctured solution has the nonzero logarithmic term described above and cannot be smooth through the endpoint. The free homogeneous constant in D cannot change this conclusion.

If the positive-temperature and vorticity signs are imposed through A/C>0 and H/A>0, then H/C>0. Under (7), this is equivalent to Ck<0. In the normalization A>0, it forces C,H>0 and k<0. On the side s>0, corresponding to approach from below, P303 gives

    A I_2 ~ -(120 k A/(11C))s^-11 -> +infinity.

On the other side the odd negative power reverses this infinite sign. Without fixing A>0, the sign of the first infinite limit is -sgn(k), and (7) together with the profile signs makes this sgn(C)=sgn(A). No general sign statement for all simple endpoints follows.

This is an additional necessary-jet test of one explicit family B=s+ks^2-(Ck/260)s^13. Allowing other lower coefficients of B could alter the residue. No simultaneous global construction of two axis endpoints, canonical full-plane inverse, material-center normalization or full transverse Taylor hierarchy has been supplied. The analytic four-equation constructions remain valid with their original scope; only their possible extension through the next vorticity equation has been classified here. The main B2 problem is OPEN.

## Dependencies and evidence

P303 supplies the already verified analytic construction and exact residue cancellation for D. The current proof derives the additional equation, analytic criterion and exact residue. verification/symbolic_residue.json records the symbolic finite sum. verification/fraction_checks.json records 594/594 checks from a separate Fraction implementation, including 48 signed rational parameter triples, two independent choices of the homogeneous constant in D, direct thermal and vorticity equations, the exact fourth-equation coefficients, and the predicted fifth-equation defect. This finite arithmetic corroborates the general symbolic derivation; it is not being used as a proof by sampling. The actual Opus 5.5 review attempt 528 returned no audit text (refusal); no endorsement is inferred. Further model review is recorded separately if obtained. No teammate code is reused; no Lean or Lake build is performed.
