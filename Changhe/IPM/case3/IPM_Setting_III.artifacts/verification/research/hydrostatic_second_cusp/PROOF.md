# A second cusp for the explicit two-mode trace when 1<c<2

Written 2026-10-21T09:46:18.784267+00:00 before verification code. This is a conditional obstruction to a termwise smooth homogeneous expansion for the particular trace of result197. It is neither hydrostatic nonexistence nor nonexistence in original SettingIII.

## Exact statement and hypotheses

Let 1/2<p<1, c=1/p, D=c-1, C=1/(p+2), d=2p-1, beta=p(p+2), and A=C^2/D. Thus 0<d<1 and 0<beta<3. Let f be the degree-p density in result197:

    f=C y r^(p-3)[3x^2+(p+2)y^2],

with its canonical hydrostatic inverse V. Its forced degree-d density coefficient is

    h=(V[f].grad f)/D
      =-A y r^(2p-6)[3x^4+2p(p+2)x^2y^2+p(p+2)y^4].

For a degree-d trace H, let C_d(H) be the full-tail finite-part coefficient of result197, now with exponent d. For h, this coefficient is strictly negative. If J_d=int_0^infinity (1+s^2)^((d-3)/2) ds, then

    C_d(h)=-A J_d [beta(1-d^2)/d
                    +(3-beta)(d+1)(d+2)/(3-d)] < 0.             (1)

Consequently, a formal expansion g=f+h+k+... satisfying the hydrostatic equation term by term, using the canonical hydrostatic inverse separately on f and h and requiring coefficients C^1 in x near every positive vertical-axis point, cannot have a degree-(3p-2) term k. It would be forced to have a nonzero |x|^d cusp. This conclusion assumes the stated termwise expansion and inverse: angular layers, nonhomogeneous matching terms and other traces are outside it. In particular no assertion is made for p<=1/2, where the axis inverse of h is not covered by the convergent homogeneous calculation.

## A finite-part identity

For a homogeneous degree-d trace with H(x,y)=|x|^d F(y/|x|), define

    q=d(d-1)F-2(d-1)sF'+s^2F'',
    F(s)=K s^d+(Q/2)s^(d-2)+O(s^(d-4)) as s tends to infinity.

The derivative expansions follow from smooth angular parity. Smooth oddness at the horizontal ray gives F(s)=O(s) near0. The finite coefficient is C_d=int_0^infinity s(q-Qs^(d-2))ds. Two integrations by parts on [0,S], with the zero-end boundary terms vanishing, give

    int_0^S s q ds
      =S^3F'(S)-(2d+1)S^2F(S)+(d+1)(d+2)int_0^S sF(s)ds.

Substituting the two leading terms at S and subtracting Q S^d/d shows

    C_d=(d+1)(d+2) FP int_0^infinity sF(s)ds,                  (2)

where FP denotes the limit after subtracting K S^(d+2)/(d+2)+(Q/(2d))S^d. The boundary remainders tend to0 because d<1. This is a finite-part identity, not an assertion that int sF itself converges.

## Two positive coefficients

Put B_0(s)=s(1+s^2)^((d-1)/2) and B_2(s)=s(1+s^2)^((d-5)/2). Their homogeneous densities are respectively y r^(d-1) and x^4 y r^(d-5), smooth away from0. For B_0, K=1 and Q=d-1. Write I_0(S)=int_0^S (1+s^2)^((d-1)/2)ds and J_d(S)=int_0^S (1+s^2)^((d-3)/2)ds. Differentiation gives

    d_s[s(1+s^2)^((d-1)/2)]
      =d(1+s^2)^((d-1)/2)+(1-d)(1+s^2)^((d-3)/2).

Hence I_0(S)=[S(1+S^2)^((d-1)/2)-(1-d)J_d(S)]/d, and its finite part after subtracting S^d/d tends to -(1-d)J_d/d. Also

    d_s[s(1+s^2)^((d+1)/2)]
      =(1+s^2)^((d-1)/2)+(d+2)s^2(1+s^2)^((d-1)/2).

It follows that the finite part of int_0^S sB_0(s)ds is (1-d)J_d/[d(d+2)]. The subtraction coefficients are exactly those in (2): the S^d coefficient equals (d-1)/(2d). Therefore

    C_d(B_0)=(1-d^2)J_d/d >0.                               (3)

For B_2, K=Q=0 and the integral I_2=int_0^infinity s^2(1+s^2)^((d-5)/2)ds converges absolutely. Since

    d_s[s(1+s^2)^((d-3)/2)]
       =(1+s^2)^((d-3)/2)+(d-3)s^2(1+s^2)^((d-5)/2)

and this primitive tends to0 at both ends, I_2=J_d/(3-d). Equations(2) and this identity give

    C_d(B_2)=(d+1)(d+2)J_d/(3-d)>0.                          (4)

The integrals J_d and I_2 are positive and finite for0<d<1. No analytic continuation or special-function sign convention is used.

## Apply the identities to h

On x=1,

    h(1,s)=-A s(1+s^2)^(p-3)
                       [3+2beta s^2+beta s^4]
           =-A[beta B_0(s)+(3-beta)B_2(s)],

because (d-1)/2=p-1 and (d-5)/2=p-3. Linearity of the full-tail coefficient, (3) and(4) prove(1). Every bracket coefficient is positive. One may equivalently simplify(1) to

    C_d(h)=-3p^2(4p^2+5p-1)J_d
              /[(p+2)^2(2p-1)(2-p)],

which is negative on1/2<p<1. The positive-sum form(1) suffices for the proof.

The inverse of h is well-defined on the punctured plane: its vertical curvature is Q_h y^(d-2), with Q_h=A beta(1-d), so int_0^y t h_xx converges because d>0, and the exterior tail converges because d<1. Applying the exact finite-part formula proved in result197 at fixed y>0 gives

    V_2[h](x,y)=Q_h y^d/[d(1-d)]+C_d(h)|x|^d+O(x^2 y^(d-2)). (5)

For completeness the cusp follows directly by setting S=y/|x| in the two integrals: the difference from the first two terms is

    -|x|^d int_S^infinity (s-S)(q_h(s)-Q_h s^(d-2))ds,

whose magnitude is O(x^2 y^(d-2)). The inverse V_1[h] is smooth near a fixed positive vertical-axis point. Indeed its integration interval starts at that positive y, on which h is smooth, and every x derivative of the homogeneous angular expression has an integrable tail when differentiated near the axis. Thus V_1[h]=O(x) there. For this particular finite angular h the same assertion follows by differentiating its explicit rational radial-power formula term by term. No regularity at the origin is asserted.

## Why the third density coefficient has a cusp

The terms of homogeneous degree3p-2 in (cX+V[g]).grad g=g give

    -2D k+V[f].grad h+V[h].grad f=0.                         (6)

The factor is c(3p-2)-1=-2D and is nonzero. V[f], f and h are smooth near any point (0,y) with y>0. Consequently V[f].grad h is smooth there. Also V_1[h]f_x is smooth there and O(x^2). Since f_y(0,y)=p y^(p-1), f_y(x,y)=p y^(p-1)+O(x^2), (5) yields

    k(x,y)=a smooth function of x
             +[p C_d(h)/(2D)] |x|^d y^(p-1)+O(x^2)

at fixed y>0, with harmless higher terms O(|x|^(d+2)) absorbed into O(x^2). The smooth and O(x^2) terms have zero even one-sided cusp quotient after subtraction of the value at0: dividing by |x|^d makes their nonconstant even part tend to0. The coefficient of |x|^d is nonzero by(1), and 0<d<1. For an even C^1 function, (k(x,y)-k(0,y))/|x|^d would tend to0 because its derivative at0 is0 and k(x,y)-k(0,y)=o(|x|). Here the quotient tends to p C_d(h)y^(p-1)/(2D), not0. Hence k cannot be C^1. This argument only needs the O(x^2) remainder, not differentiated asymptotics for that remainder.

## Dependencies and scope

Result197 supplies f, its canonical hydrostatic inverse and its forced h; those identities were proved independently and checked83ways. This proof rederives all finite-part identities used at the next degree. Code will verify the polynomial identities and compare(1) against direct finite-part quadrature and inverse cusp quotients. Actual Opus5.5 review is pending until recorded.

This excludes only the stated regular termwise expansion beginning with this specific two-mode trace when1<c<2. It does not exclude another leading trace or an exact smooth solution with angular layers or different matched asymptotics. The original admissible class assumes no such expansion. No decisive endpoint follows.
