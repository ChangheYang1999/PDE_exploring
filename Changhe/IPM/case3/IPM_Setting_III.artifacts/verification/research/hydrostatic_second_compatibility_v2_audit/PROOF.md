# Revised second hydrostatic compatibility theorem

Written 2026-10-21T10:54:10.503251+00:00 before the executable v2 audit. Result209 supersedes205's blanket text confirmation where the appendix opening permitted unnecessarily general W with only a bound on W'. The actual constructed streams, and the complete independent proof of the substantive conclusions, already obey the stronger assumptions. The following is a standalone proof with the local repair justified first and the complete205 proof reproduced below.

## Exact changed hypotheses and their proof

Fix1/2<p<1, c=1/p,D=c-1,d=2p-1. The objects are precisely the smooth streams W_e,W_0 and their positive additions, normalizations and convex combinations constructed below. The nonsmooth limiting chart W_* is used only for the explicit density/moment calculation and the limit argument. Near0, W_e is exactly linear, while W_0=C_0 s(1+s^2)^((p-1)/2) is odd analytic. Near infinity W_e is exactly s^p and W_0 has its convergent expansion in s^(-2). Thus these W have odd smooth extension at0 and every differentiated large-s expansion, in particular W^(j)=O(s^(p-j)) forj=1,2,3. The same statements hold for their linear combinations.

For x>0,s=y/x,Psi=-x^(p+1)W(s), the displayed density F solves pF-sF'=W''. Its canonical identification uses

    V1=x^p W',
    V2=x^p[sW'-(p+1)W],
    V2_y=x^(p-1)[sW''-pW'].

The derivative bounds imply V1->0 and V2_y->0 asy->infinity atfixedx>0. Further, V1_y=g_x and V2_yy=-g_xx. The bounds on W'',W''' give absolute integrability of the resulting tails; oddness gives V2(x,0)=0. Integrating these differential identities with those endpoints identifies exactly the canonical inverse. At the vertical axis this identity follows by the explicit smooth local formulas and their convergent axis integrals, as in the proof below.

The original W' bound alone is insufficient for this step. For a smooth cutoff tail W'=s^(p-1)sin(s^2), it holds, but

    sW''-pW'=2s^(p+1)cos(s^2)-s^(p-1)sin(s^2)

does not approach0. At s=sqrt(2pi n) it tends to positive infinity. This is a counterexample to that boundary implication, not a counterexample to the constructed theorem or a profile. The revised text correctly narrows to the constructed streams and states the needed derivatives.

Absence of a constant in the differentiated outer stream expansion yields V2=-w_1 y^p+O(x^2 y^(p-2)), so comparison with the established cusp identity forces Cp=0. Smoothness itself follows from the explicit axis expressions, not from that finite expansion alone. The strict positive horizontal-axis slope of the final density is supplied by the positive W_0 component. Its normalized vertical restriction is y^p, giving f_y(0,y)=p|y|^(p-1)>0. Strict interior signs are proved below and parities supply the other quadrants. All these properties survive the final convex interpolation.

Forc>=2 the degree d is nonpositive. If the next homogeneous density has nonzero axis curvature Q_d, its lower velocity integral on the positive axis contains Q_d int_0^y t^(d-1)dt, which diverges for everyd<=0. WhenQ_d=0 this particular implication does not apply. The revised scope states this condition and general need for core matching, not universal divergence. No statement about actual solutions is added.

The lead's p=.6 direct finite-cutoff numerical error is about1.905e-9 absolute and9.09e-10 relative; 'relative discrepancies below1e-9' is accurate. The exact formula is proved independently below. Numerical agreement remains supplemental, not an enclosure.

## Complete independent proof of all unchanged assertions

# Exact audit of the second hydrostatic compatibility section

Written 2026-10-21T10:39:06.264012+00:00 before the verification program. Result205 audits the frozen body and appendix of the lead's Section3.76 v1. The claim is a theorem about homogeneous traces and a conditional formal hierarchy, not a hydrostatic profile or an original SettingIII endpoint.

## Statement and notation

Fix 1/2<p<1, c=1/p, D=c-1, d=2p-1. Let f be smooth on the punctured plane, homogeneous of degree p, even in x, odd in y, and K=f(0,1)>0. Assume its canonical hydrostatic velocity V[f] is smooth on that punctured plane. The canonical inverse on y>=0 is

    V1[u](x,y)=-int_y^infinity u_x(x,t)dt,
    V2[u](x,y)=int_0^y t u_xx(x,t)dt+y int_y^infinity u_xx(x,t)dt.

Reflection fixes the inverse in the lower half plane. For a smooth homogeneous degree-q density u, 0<q<1, put B(s)=u(1,s), Q=u_xx(0,1), and

    b(s)=q(q-1)B-2(q-1)s B'+s^2 B'',
    Cq(u)=int_0^infinity s[b(s)-Q s^(q-2)]ds.

Then h=V[f].grad f/D is smooth of degree d with the same parities. Define k by

    2D k=V[f].grad h+V[h].grad f.

At every fixed y>0 the quotient (k(x,y)-k(0,y))/|x|^d tends to p K Cd(h)y^(p-1)/(2D). Thus k can be C1 near the positive vertical axis only if Cd(h)=0. The lead's two explicit and existence claims (a),(b) are proved below. All assertions refer to these definitions; their appearance as coefficients of an actual solution is only formal.

## General inverse regularity and the cusp quotient

Smooth even angular data give B(s)=K_u s^q+(Q/2)s^(q-2)+O(s^(q-4)) as s grows, with all derivative expansions; consequently b(s)=Q s^(q-2)+O(s^(q-4)). At zero smooth oddness gives B=O(s), b=O(s). The defining integral converges, since its subtracted integrand is O(s^(q-1)) at zero and O(s^(q-3)) at infinity. The two integrations by parts and the exact finite-part subtractions are proved below.

For x in a bounded interval and t large, write u(x,t)=t^q U(x/t), U(z)=u(z,1), smooth and even near zero. Then u_x=O(|x|t^(q-2)) and u_x^j=O(t^(q-j)) for j>=2. At a positive vertical-axis point, the integration interval defining V1 starts strictly above zero. The estimate for the original integrand and those for every x derivative are integrable because q<1. Mixed y derivatives reduce to derivatives of u at the lower endpoint. Differentiation under the integral therefore proves that V1[u] is smooth there and odd in x. This applies to h because V[f] is assumed smooth and h is its product with grad f; no smoothness of V2[h] is assumed or inferred.

For x not zero, put S=y/|x|. Homogeneity gives

    V2[u](x,y)=|x|^q [int_0^S s b(s)ds+S int_S^infinity b(s)ds].

At x=0 the corresponding two weighted integrals converge since q>0 at their lower endpoint and q<1 at infinity. Their value is Q y^q/[q(1-q)]. Subtract that value and Cq(u)|x|^q in the displayed identity. The exact remainder is

    -|x|^q int_S^infinity (s-S)[b(s)-Q s^(q-2)]ds.

Its magnitude is O(|x|^q S^(q-2))=O(x^2 y^(q-2)). This proves continuity on the vertical axis and the required cusp expansion. It also shows why q>0, which becomes p>1/2 for h, is necessary for this homogeneous inverse argument. Smoothness of V[f] forces Cp(f)=0 by the same quotient.

Parity makes V[f].grad h smooth and even in x near (0,y), so its difference from its axis value is O(x^2). The product V1[h]f_x is smooth and O(x^2). Also f_y=pK y^(p-1)+O(x^2). Applying the preceding V2 expansion with u=h and q=d yields

    k(x,y)-k(0,y)=pK Cd(h)y^(p-1)|x|^d/(2D)+O(x^2).

The product correction |x|^(d+2) is absorbed by O(x^2). An even C1 function has zero derivative at zero and difference o(|x|), so the stated nonzero quotient obstructs C1. This argument needs no derivative estimate on the O(x^2) remainder.

For the formal equation (cX+V[g]).grad g=g, the linear degree-e term is (ce-1)f_e. Degrees p and d=p+p-1 give the first forced coefficient h. The next cross degree is e=p+d-1=3p-2 and ce-1=-2D, which gives the definition of k. The conclusion is conditional on the termwise hierarchy and canonical inverse. It neither proves that an actual profile has this expansion nor excludes angular layers.

## Complete proof of the explicit trace formula and positive-trace construction

The following two proofs are reproduced in full from the verifier's independently written results198 and199, so this file contains the finite-part integrations, the jump accounting, the smoothing argument and the normalization and interpolation proof. Their statements agree with the preceding general argument. Their historical review-status notes are superseded by the evidence paragraph at the end.

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


# Smooth positive traces satisfying the first two hydrostatic cusp conditions

Written 2026-10-21T09:59:03.116703+00:00 before the verification program. This is a theorem about angular traces and the first two formal compatibility conditions. It does not construct a hydrostatic solution or an original IPM profile.

## Statement

Fix 1/2<p<1, let c=1/p, D=c-1 and d=2p-1. There exists a smooth homogeneous degree-p density f on the punctured plane, even in x and odd in y, with f(0,1)=1, strictly positive trace in the upper semicircle, strictly increasing trace on the first quadrant, f_y>0 away from0, and f_x<0 in the open first quadrant, such that

    C_p(f)=0,                 C_d((V[f].grad f)/D)=0.

Here V is the canonical hydrostatic vertical-tail inverse and C_q is the convergent finite-part cusp functional defined below. This is an existence theorem for traces only. In particular, the negative second coefficient of result198 is specific to its trace; neither the first nor the second cusp condition supplies a sign obstruction for every positive monotone trace. Higher compatibility conditions remain open. No smoothness at the origin and no nonlinear profile equation are claimed.

## Stream representation and the cusp functional

For x>0, set s=y/x and write

    Psi(x,y)=-x^(p+1) W(s),       f(x,y)=x^p F(s),
    H=W',                        J=sH-(p+1)W.

Then V_1=x^p H and V_2=x^p J. The hydrostatic identity -Psi_yy=f_x is exactly

    W''=pF-sF'.                                                    (1)

For the functions below W is odd at s=0, W(0)=0, W'=O(s^(p-1)) at infinity, and

    F(s)=-s^p int_0^s t^(-p-1) W''(t) dt.                        (2)

The integrand is integrable at0 because W''=O(s). Formula(2) solves(1) with F=O(s) at0. Integrating V_1,y=f_x from infinity, and V_2,y=-V_1,x from0, proves the canonical inverse exactly as in result197. Extend by parity. Smooth expansions of W and F at both ends make f and Psi smooth on the punctured plane, including the axes. Their degrees and 0<p<1 give sublinear velocity.

If W''<=0 and F>=0, (1) implies F'>=pF/s. With strict W''<0 and F>0 both F'>0 and pF-sF'<0 hold. Also the angular trace derivative has the sign of

    (1+s^2)F'-psF > 0.

Thus these inequalities imply all the stated first-quadrant signs. Reflections give f_y>0 on the whole punctured plane when the axis limits are positive.

For any smooth degree-q trace with 0<q<1, write its value at (1,s) as B(s), where

    B(s)=K s^q+(Q/2)s^(q-2)+O(s^(q-4)),
    b=q(q-1)B-2(q-1)sB'+s^2 B''.

The finite coefficient and its equivalent moment expression are

    C_q(B)=int_0^infinity s[b-Qs^(q-2)] ds
          =(q+1)(q+2) FP int_0^infinity sB(s)ds,                 (3)

where FP subtracts K S^(q+2)/(q+2)+(Q/(2q))S^q at the upper endpoint S. The complete two integrations by parts and all endpoint estimates are in result198 and are restated by the displayed subtraction. Smooth horizontal oddness gives b=O(s) at0, and the subtracted tail is O(s^(q-4)); both integrals converge in the stated sense.

In the stream representation a smooth expansion

    W(s)=u s^p+v s^(p-2)+O(s^(p-4))

has no constant term. Since J=sW'-(p+1)W=-u s^p+O(s^(p-2)), the vertical inverse has no |x|^p term near a positive vertical-axis point. The exact finite-part inverse formula of result197 therefore gives C_p(f)=0.

Euler's identity simplifies the nonlinear term to

    T(s)=(V[f].grad f)(1,s)=p H(s)F(s)-(p+1)W(s)F'(s).          (4)

This follows equally from H W''+J F' and(1). At any finite S, integration by parts gives

    int_0^S sT ds=(2p+1)int_0^S sHF ds
                     +(p+1)int_0^S WF ds-(p+1)S W(S)F(S).    (5)

The lower boundary term is zero. Formula(5) is useful for passing to a limit with a jump in F: it only integrates bounded undifferentiated functions.

## A positive second coefficient before smoothing

Use the continuous concave stream chart

    W_*(s)=s for 0<=s<=1,        W_*(s)=s^p for s>=1.

This intermediate chart is not smooth and is not itself a trace in the theorem. Its derivative drops from1 to p at1. Formula(2), understood through this single jump or by approximation, gives F_*=0 for s<1 and

    F_*(s)=K_* s^p+b_* s^(p-2) for s>1,
    K_*=(1-p)(p+2)/2,          b_*=-p(1-p)/2.                 (6)

In particular F_* jumps by1-p at1. Away from1, (4) vanishes below1 and equals

    T_*=-p K_* s^d+(p+2)b_* s^(d-2)                          (7)

above1. The jump in F contributes -(p+1)(1-p) to the moment int sT. This is not a nonlinear distribution product: W_* is continuous at1, and the same contribution follows by inserting the bounded functions W_*, H_*, F_* in(5). Subtracting the two tail terms of(7) gives the finite moment

    M_* = -(p+1)(1-p)+p K_* /(2p+1)-(p+2)b_* /(2p-1)
        = (1-p)^2(2p^2+2p+1)/(4p^2-1) > 0.                 (8)

All denominators are positive for1/2<p<1. The coefficient corresponding to h=T/D is (d+1)(d+2)M_*/D>0. The following smoothing argument turns this limiting sign into a sign for admissible smooth angular data.

## Smooth concave approximation with exactly zero first cusp

Choose a nonnegative C-infinity function eta supported in(-1,1), positive there, with integral1. For example normalize exp(-1/(1-z^2)) on that interval and set it to0 outside. Put eta_e(a)=eta(a/e)/e and

    W_e(s)=int_{-e}^e exp(pa) W_*(s exp(-a)) eta_e(a) da.     (9)

For e>0 this is smooth for s>0 by convolution in log s. Each integrand is concave in s, so W_e''<=0. For s<exp(-e), W_e is exactly A_e s with A_e>0. For s>exp(e), W_e is exactly s^p. Thus it is smooth at the horizontal ray, and has the required power expansion at the vertical ray. Formula(2) defines F_e. Equivalently, linearity and a change of variable give

    F_e(s)=int_{-e}^e exp((p-2)a) F_*(s exp(-a)) eta_e(a)da.  (10)

The jump of F_* is smoothed by this integral. Hence F_e is smooth, zero for s<exp(-e), positive afterwards, and for s>exp(e) is exactly

    F_e(s)=K_e s^p+b_* s^(p-2),
    K_e=K_* int_{-e}^e exp(-2a)eta_e(a) da >0.              (11)

Equations(9)-(11) also prove smoothness across the transition endpoints: eta is flat there. They give a globally smooth angular trace, possibly zero near the horizontal axis, with canonical inverse and C_p=0 exactly. Its second density coefficient is smooth on the punctured plane, so(3) applies to it.

Let M_e=FP int sT_e, with T_e given by(4). For a fixed S=2 and e<log2, the exterior terms are exactly(7) with K_* replaced by K_e. On[0,2], W_e tends uniformly to W_*, while H_e and F_e converge almost everywhere to H_* and F_* and are bounded uniformly for e sufficiently small. These claims follow directly from their positive averages of bounded functions on a fixed compact interval; all are zero or linear below a common positive transition radius. Dominated convergence in(5), and K_e to K_*, give M_e to M_*. Therefore M_e>0 for all sufficiently small e. No interchange with an unbounded subtracted tail is needed, because its two terms are exact outside2.

## Strict signs and simultaneous compatibility

Let W_0(s)=s(1+s^2)^((p-1)/2)/(p+2), with density F_0 from result197. That result proves all strict signs, K=1 and C_p=0. Result198 proves

    C_d((V[f_0].grad f_0)/D)<0.                              (12)

For fixed sufficiently small e, replace W_e by W_e+delta W_0, with delta>0 sufficiently small. By linearity of(2), the density is F_e+delta F_0. It has strict positivity, F'>0 and W''<0 throughout s>0; at both axes the positive F_0 contribution gives f_y>0. The angular derivative is positive by(1). Its axis coefficient is K_e+delta>0. Both summands have no constant term in the stream expansion at infinity, so C_p remains exactly0.

The second coefficient is continuous in delta at0. On a fixed compact interval this follows from(4) or(5). In the exterior both streams and densities have smooth expansions in powers s^(p-2j), with coefficients polynomial in delta in the product T and a uniform O(s^(d-4)) remainder after the first two terms are removed. Multiplication by s is integrable there because d<1. Formula(3) and dominated convergence therefore prove continuity of the finite part. Thus the second coefficient stays positive for sufficiently small delta. Divide the density and stream by K_e+delta. This makes f(0,1)=1, preserves all signs and C_p=0, and multiplies the second coefficient by a positive square. Call the resulting smooth trace f_+.

Finally define f_t=(1-t)f_0+t f_+ for0<=t<=1. The inverse is linear; C_p is linear and zero for every t. Positivity and the strict derivative signs survive convex combination, and the axis coefficient stays1. The function

    t -> C_d((V[f_t].grad f_t)/D)

is a real quadratic polynomial by bilinearity, with continuous finite coefficients by the preceding tail estimates. It is negative at0 by(12) and positive at1. The intermediate value theorem gives a t in(0,1) at which it is zero. This proves the statement.

## Dependencies and scope

The hydrostatic inverse and finite-part formula are proved in result197; result198 supplies the negative reference trace and the moment identity. The limiting positive chart, its smoothing and the interpolation are proved here. Each final angular trace is smooth, while its homogeneous extension is only continuous at the origin, since p<1 and its vertical coefficient is1. It is not an admissible primary density. Vanishing of two formal compatibility coefficients neither solves the hydrostatic equation nor rules out later compatibility conditions or angular layers. Both original SettingIII endpoints remain open. Independent algebra and full-tail/moment checks follow in verification/. Actual Opus5.5 review will be requested and recorded separately.

## Audit conclusion and evidence scope

The exact frozen Section3.76 v1 body and appendix are CONFIRMED. Its smoothness hypothesis on V[f] suffices for every use of the inverse near a positive vertical-axis point. The normalization divisor K_e+delta is the density axis coefficient, since the smoothed chart has coefficient K_e and the strict reference density has coefficient1. Scaling both stream and density by its reciprocal scales Cd(h) by its reciprocal square. The continuity argument in delta includes the two subtracted exterior coefficients and an integrable remainder. Convex interpolation gives a polynomial in t because the inverse and Cq are linear and the transport is bilinear.

All p-dependent statements require 1/2<p<1. Assertions about k defined by its displayed equation are proved; the expansion from which that equation is selected is formal. The proof does not imply the sufficient converse Cd(h)=0 gives a complete smooth expansion. Neither SettingIII endpoint follows.

Independent prior checks198 and199 are frozen alongside the exact source. The lead's actual Opus5.5 hand-check source and numerical log are frozen too. Its direct quadrature is only a cutoff computation with a leading asymptotic tail correction and binary input parameters, so its 1e-9 agreement is numerical corroboration, not a certified error bound. The verifier's earlier checks used a separate complete-tail implementation at45 and65 digits, without this cutoff approximation. A hostile external audit was pending when this proof was written; no result is attributed to it before its text arrives.


## Review provenance and scope of this revision

The hostile review supplied with v2 was produced by referee. It records a failed Opus5.5 credential attempt and is not itself an Opus review. The lead is the actual Opus5.5 collaborator; its written repairs and previous hand-check are independently tested here. The generic-stream and precision wording gaps missed by205 are repaired in this revision. No change is made to the coefficient equations, finite-part integrations, jump accounting or interpolation construction. The full original SettingIII and hydrostatic profile endpoints remain OPEN.
