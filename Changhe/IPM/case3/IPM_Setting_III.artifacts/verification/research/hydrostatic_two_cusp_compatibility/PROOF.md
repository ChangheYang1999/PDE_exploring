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
