# Compactness of the full coupling from the jet input

## Exact statement

Keep the spaces B, R, G, E, Z and Y of topics44 and46. Let a=17/4, eta=5/4, ell>1 and k=1/ell. Write the background as

 rho(x,y)=x^2 y b(t,theta), t=log r.

Assume b is even under x reflection and y reflection, has three continuous angular derivatives and one t derivative with two continuous angular derivatives on compact annuli. For a function f define

 N(f)=sum_(j=0)^3 sup_theta |partial_theta^j f|
                      +sum_(j=0)^2 sup_theta |partial_theta^j partial_t f|.

Assume finite constants Cminus,Cplus such that

 N(b-1)(t)<=Cminus exp(2t), t<=0,
 N(b)(t)<=Cplus exp((k-3)t), t>=0.                         (1)

The finite modal trial has these properties. No numerical values of Cminus,Cplus are claimed. Let chi0 be a smooth radial cutoff equal to1 near0 and compactly supported. Define

 C h=[U[h]+chi0(c[h]/3)X].grad rho

using the canonical full-plane velocity. Then

 beta -> C(E beta)

is a Hilbert-Schmidt map from B to Y=E G direct-sum R. More precisely, if Gamma is the compact axis map of proof 46, the remainder map

 beta -> C(E beta)-E Gamma_(E beta)

is Hilbert-Schmidt from B to R. This establishes the entire jet-input part of (E0), including the corners and the far field. The remainder-input map R->Y and its Garding estimate are not asserted here.

## Exact velocity formula

Use the moments from proof 46, now renamed to avoid collision with b:

 P(t)=integral_r^infinity s beta(log s)ds,
 Q(t)=r^(-4)integral_0^r s^5 beta(log s)ds,
 S(t)=r^(-6)integral_0^r s^7 beta(log s)ds,
 B0(t)=r^2 beta(t), z=cos(theta)^2.

The two stream-function modes are

 psi2=r^2(P-Q)/8, psi4=-r^2 S/8.

Converting U_r=-partial_theta psi/r and U_theta=partial_r psi to Cartesian components gives

 U1[E beta]/x=P1(t,z), U2[E beta]/y=P2(t,z),

 P1=-P/4-3Q/4+5S/2 +(Q-10S+B0)z +(8S-B0)z^2,
 P2= P/4- Q/4+ S/2 +(Q- 6S)z    +(8S-B0)z^2.             (2)

The formulas extend across both axes. They use beta but no derivative of beta. On the vertical axis, P2=V=T/y and P1=-V-V', as required by incompressibility. The identities can first be computed for smooth beta, then extended to B using the bounds and canonical trace construction of proof 46.

Put c=c[E beta]. Those bounds imply, with constants depending only on the B realization,

 ||P1(t,.)+c||_(C2_theta)+||P2(t,.)-c||_(C2_theta)
                             <=Kminus exp(2t)||beta||_B, t<=0,
 ||P1(t,.)||_(C2_theta)+||P2(t,.)||_(C2_theta)
                             <=Kplus exp(-11t/8)||beta||_B, t>=0. (3)

For the first inequality use P-4c=-integral_0^r s beta ds, Q=O(r^2), S=O(r^2) and B0=O(r^2). For the second use the bounds on P,Q,S from (16) in proof 46 and |B0|<=Bplus exp(-11t/8)||beta||_B. Since (2) is a fixed-degree polynomial in z, the same bounds hold for two angular derivatives. Thus no derivative of beta is hidden in (3).

## Subtraction of the axis coefficient

The gradient of the background is

 rho_x=xy [2b+z b_t-cos(theta)sin(theta)b_theta],
 rho_y=x^2[b+(1-z)b_t+cos(theta)sin(theta)b_theta].

Consequently C(E beta)=x^2y F_beta, where

 F_beta=P1[2b+z b_t-cos(theta)sin(theta)b_theta]
       +P2[b+(1-z)b_t+cos(theta)sin(theta)b_theta]
       +(c chi0/3)(3b+b_t).                              (4)

The vertical-axis value is precisely Gamma_(E beta)(t) from proof 46. Parity gives partial_theta F_beta(t,pi/2)=0. Taylor's integral formula and |sin u|>=2|u|/pi for |u|<=pi/2 imply

 |F_beta(t,theta)-F_beta(t,pi/2)|
       <=(pi^2/8) cos(theta)^2 ||partial_theta^2 F_beta(t,.)||_infinity. (5)

Reflection extends (5) to all angles. The same estimate holds in B* norm, because (4) is linear in beta and all its point evaluations are bounded functionals on B.

Near0 use P1=-c+(P1+c), P2=c+(P2-c), chi0=1. The contribution of the constant strain to (4) is exactly

 c[(4/3-2z)b_t+2 cos(theta)sin(theta)b_theta].              (6)

This is O(exp(2t)) with two angular derivatives by (1). Every other term in (4) has a coefficient P1+c or P2-c and is O(exp(2t)) by (3). At infinity chi0=0, so (1), (3), (4) give O(exp((k-35/8)t)) with two angular derivatives. On compact t intervals all these functional norms are bounded. Hence there exists a measurable function D(t), bounded on compact intervals, such that

 ||F_.(t,theta)-Gamma_(E .)(t)||_(B*)<=cos(theta)^2 D(t),
 D(t)=O(exp(2t)) as t->-infinity,
 D(t)=O(exp((k-35/8)t)) as t->+infinity.                   (7)

The derivative count in (1) is explicit: two derivatives of the term b_theta in (4) require three angular derivatives of b. No global high-Sobolev estimate is being inferred.

## The Hilbert-Schmidt bound

Let (e_n) be an orthonormal basis of B. Tonelli, Parseval for the B* evaluation functional and (7) imply

 sum_n ||C(E e_n)-E Gamma_(E e_n)||_R^2
   <= I_a integral_R exp(8t+mu(t))D(t)^2 dt,

 I_a=integral_0^(2pi)|cos(theta)|^(8-2a)sin(theta)^2 dtheta
    =2 B(1/4,3/2)<infinity.                              (8)

Here mu=-17t/2 on t<0 and mu=-5t/4 on t>=0. The integral in (8) is finite: its left integrand is O(exp(7t/2)) and its right integrand is O(exp(2(k-1)t)). This proves the asserted Hilbert-Schmidt remainder map. The jet part is Hilbert-Schmidt by proof 46, so the whole map B->Y is Hilbert-Schmidt.

All products in (4) are ordinary locally integrable functions for beta in B, since beta is locally H1 and the moments are continuous. Formula (8) supplies their actual Y-valued extension. Thus this is a proof of the jet-input mapping itself, not a conclusion conditional on the remaining part of (E0).

## Scope and evidence

The operator from remainder inputs still needs a global Taylor-subtracted weighted singular-integral bound. This theorem neither proves that bound nor the Garding inequality. It also does not provide an inverse norm, actual coefficient margins or a nonlinear estimate.

The accompanying exact symbolic check verifies (2), the divergence identity, the axis value, the gradient formulas, the cancellation (6) and the radial integrability exponents. It is an algebraic audit of the proof, not a numerical existence argument.

Dependencies: topics44 and46. Verdict: CONFIRMED under the stated background and scalar-domain hypotheses, which hold qualitatively for the selected modal trial whenever hypothesis (A) defining its B realization holds.
