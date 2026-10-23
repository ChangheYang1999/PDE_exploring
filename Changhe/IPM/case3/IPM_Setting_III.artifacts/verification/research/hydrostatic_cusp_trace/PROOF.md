# Positive monotone traces with vanishing hydrostatic cusp coefficient

Written 2026-10-21T09:39:25.657386+00:00 before code checks. Status: analytic identities and counterexamples to a possible sign obstruction. This result does not construct a hydrostatic or original IPM profile.

## Statement and notation

Fix 0<p<1, let r=(x^2+y^2)^(1/2), c=1/p, D=c-1, and put C=1/(p+2). On R^2 minus the origin define

    f(x,y)=C y r^(p-3) [3x^2+(p+2)y^2],
    Psi(x,y)=-C xy r^(p-1),
    V_1=C x r^(p-3) (x^2+p y^2),
    V_2=-C y r^(p-3) (p x^2+y^2).

These functions are homogeneous of degrees p,p+1,p,p respectively, with the density even in x and odd in y and the stream odd in both variables. The velocity is the hydrostatic inverse of f, namely, at points where the displayed integrals are defined,

    V_1[f](x,y)=-int_y^infinity f_x(x,t) dt,
    V_2[f](x,y)=int_0^y t f_xx(x,t) dt+y int_y^infinity f_xx(x,t) dt    (y>=0).

The inverse is not the original elliptic IPM inverse: here -Psi_yy=f_x. Extend the fields by parity across y=0 and continuously with value0 at the origin. f is smooth away from0 but is not C^1 at0, so it is not an admissible primary profile.

The angular trace Theta(theta)=f(cos theta,sin theta) is smooth on the circle. It is strictly positive on the upper semicircle, strictly increasing on (0,pi/2), and has Theta(pi/2)=1. Also f_y>0 on the punctured plane, and f_x<0 when x,y>0. Its finite cusp coefficient C_p, as defined below, is exactly0. Small smooth angular perturbations supported away from the symmetry axes preserve these strict inequalities and the full jets at both axes, while producing either sign of C_p.

Its next formal density term f_2=(V[f].grad f)/D is smooth away from0 and has no vertical-axis cusp. Explicitly,

    f_2= -C^2 y r^(2p-6)/D
           *[3x^4+2p(p+2)x^2 y^2+p(p+2)y^4].

This is only the algebraic next term of an expansion; it is not asserted that an exact solution has this expansion or that the remaining inverse integrals and hierarchy converge.

There is also a smooth manufactured density with this trace. For L>0 replace r^2 by R^2=L^2+x^2+y^2 and set

    g_L=C_L y R^(p-3) [3(L^2+x^2)+(p+2)y^2],
    Psi_L=-C_L xy R^(p-1),
    V_1,L=C_L x R^(p-3) (L^2+x^2+p y^2),
    V_2,L=-C_L y R^(p-3) (L^2+p x^2+y^2),       C_L>0.

It is globally smooth with g_L,y>0 and the same hydrostatic inverse law. If C_L L^(p-1)=1/3, then g_L,y(0)=1 and V_2,L,y(0)=-1/3. Taking c=4/3 and p=3/4 makes both the hydrostatic origin normalization and leading transport exponent exact. Nevertheless its transport residual on the vertical axis equals -3 y^3/(8 L^2)+O(y^5) near0, so it is not a hydrostatic solution. This explicitly separates trace compatibility from nonlinear existence.

## Proof of the homogeneous identities and inequalities

Differentiate the formulas on the punctured plane. The stream gives V=(-Psi_y,Psi_x), so div V=0. Direct differentiation of f gives

    f_x=C(p-1)xy r^(p-5)(3x^2+p y^2)=-Psi_yy,
    f_y=C r^(p-5)[3x^4+6p x^2 y^2+p(p+2)y^4].

Every coefficient in the second bracket is positive and 0<p<1. Hence f_y>0 away from0 and f_x<0 in the open first quadrant. For fixed x and y large, f_x=O(|x| y^(p-2)), f_xx=O(y^(p-2)), and V_1 tends to0. Integrating V_1,y=f_x from y to infinity proves its canonical tail formula. For x nonzero, V_1,x is continuous down to y=0, differentiation under the tail integral is justified by the same integrable tail, and V_2(x,0)=0. Thus V_2,y=-V_1,x=int_y^infinity f_xx(x,t)dt. Integrating from0 to y and splitting at y gives the stated V_2 formula. At x=0, f_xx(0,t)=Q t^(p-2), where

    Q=p(p-1)/(p+2).

Here int_0^y t f_xx is integrable since p>0, and the tail from y>0 is integrable since p<1. Its value is Q y^p/[p(1-p)]=-C y^p, agreeing with V_2(0,y). At the origin the inverse integrals involving int_0^infinity f_xx need not exist; only the continuous field extension is claimed there. The explicit fields are O(r^p), and so extend continuously but not with a bounded first derivative. In particular f(0,y)=sgn(y)|y|^p excludes C^1 regularity at0.

The trace is

    Theta(theta)=sin(theta)[3cos^2(theta)+(p+2)sin^2(theta)]/(p+2).

The numerator factor in square brackets is positive. Differentiation gives

    Theta'(theta)=3cos(theta)[cos^2(theta)+p sin^2(theta)]/(p+2).

This proves strict increase in the first quadrant, Theta(pi/2)=1 and Theta'(0)=3/(p+2). Smooth trigonometric factors establish the parity and regularity assertions. Equivalently it is a positive multiple of sin(theta)+epsilon_p sin(3theta), with epsilon_p=(1-p)/(3(p+3)); no claim about a profile follows from this finite angular representation.

## The finite cusp coefficient

For any smooth homogeneous trace with these parities, write f(x,y)=|x|^p F(y/|x|), x nonzero, and set

    q(s)=p(p-1)F(s)-2(p-1)sF'(s)+s^2 F''(s),
    Q=p Theta(pi/2)+Theta''(pi/2),
    C_p=int_0^infinity s[q(s)-Q s^(p-2)] ds.

Smoothness at the horizontal ray and oddness give q(s)=O(s) near0. Smoothness and evenness about the vertical ray give F(s)=K s^p+(Q/2)s^(p-2)+O(s^(p-4)) and q(s)=Q s^(p-2)+O(s^(p-4)) as s tends to infinity. The corresponding derivative remainders follow from the same smooth angular expansion. The integral for C_p therefore converges at both ends, since p>0 and p<1.

For x>0 and S=y/x, substituting t=xs in the inverse yields

    V_2=x^p [int_0^S s q(s) ds+S int_S^infinity q(s) ds].

Subtracting the pure Q contribution gives exactly

    V_2-Q y^p/[p(1-p)]
       =x^p [C_p-int_S^infinity (s-S)(q(s)-Q s^(p-2)) ds].

The remaining integral is O(S^(p-2)), so

    V_2=Q y^p/[p(1-p)]+C_p |x|^p+O(x^2 y^(p-2))

near the vertical axis at fixed y>0. For our explicit velocity,

    V_2=-C y^p (1+(x/y)^2)^((p-3)/2)(1+p(x/y)^2)
        =-C y^p+O(x^2 y^(p-2)).

The leading coefficient is Q/[p(1-p)]=-C. Divide the difference by |x|^p and let x tend to0: because2>p, the quotient tends to0. Thus C_p=0 exactly. This proof uses the full tail inverse, not a finite upper endpoint or an imposed strain.

## Perturbations of either sign with fixed axis jets

Choose a nonnegative, nonzero smooth function chi supported in (1,2), for example exp(-1/((s-1)(2-s))) there and0 elsewhere. Define F_epsilon=F+epsilon chi for s>=0, and extend the corresponding angular trace by the same even-x, odd-y parities. Since the perturbation vanishes near both ends in the s chart, the new trace has exactly the same jets at both symmetry axes, including K and Q. It is smooth on the entire circle.

On the compact support, the strict positive quantities F,F', Theta' and the strictly negative quantity pF-sF' have nonzero margins. Their perturbations are bounded by a constant times |epsilon| in the relevant C^1 norm. Taking |epsilon| sufficiently small therefore preserves positivity of the trace, f_y>0, first-quadrant angular increase and f_x<0. Outside this compact angular set the functions are unchanged.

Because Q is unchanged and the perturbation is compactly supported, its contribution to C_p is

    epsilon int_0^infinity s[p(p-1)chi-2(p-1)s chi'+s^2 chi''] ds
      =epsilon (p+1)(p+2) int_0^infinity s chi(s) ds.

The equality follows from two ordinary integrations by parts. All boundary terms vanish: int s^2 chi'=-2 int s chi and int s^3 chi''=6 int s chi. Thus the coefficient has the sign of epsilon and is nonzero for epsilon nonzero. C_p=0, C_p>0 and C_p<0 all occur with the stated strict sign conditions. These conditions alone supply no sign exclusion through this coefficient.

## Formal next term and the manufactured smooth core

Euler's identity gives (c X.grad-1)f=0 for c=1/p. Multiplying the explicit V and grad f, collecting powers and factoring r^2 gives

    V.grad f= -C^2 y r^(2p-6)
                 [3x^4+2p(p+2)x^2 y^2+p(p+2)y^4].

Dividing by D gives the displayed f_2, because c(2p-1)-1=-D. This density coefficient has the same parities and is smooth near either axis away from0. It is negative on the upper half-plane, which alone is harmless as a lower-degree asymptotic term. In fact V.grad f is strictly negative there, so f itself is not an exact homogeneous solution.

For the smooth core, direct differentiation gives -Psi_L,yy=g_L,x and V_L=(-Psi_L,y,Psi_L,x), with the displayed formulas. Let A=L^2+x^2. Then

    g_L,x=C_L(p-1)xy R^(p-5)[3L^2+3x^2+p y^2],
    g_L,y=C_L R^(p-5)[3A^2+6p A y^2+p(p+2)y^4]>0.

The same tail decay and boundary value V_2,L(x,0)=0 prove the canonical hydrostatic integral formulas. The fields are globally smooth because L>0; differentiating a power of L^2+r^2 also gives all three growth/Hessian bounds of the hydrostatic class with exponent p. Its leading density is C_L(p+2) times the normalized trace above and still has C_p=0 by linearity.

Assume C_L L^(p-1)=1/3. Then on x=0,

    g_L(0,y)=y+E y^3+O(y^5),       E=5(p-1)/(6L^2),
    V_2,L(0,y)=-y/3+v_3 y^3+O(y^5),   v_3=-(p-1)/(6L^2).

With c=4/3, the linear part of c y+V_2,L is y. Consequently the residual coefficient is 2E+v_3=3(p-1)/(2L^2). At p=3/4 this is -3/(8L^2), nonzero. Hence even the normalized smooth manufactured core, correct leading exponent, positivity and vanishing cusp coefficient do not supply an exact hydrostatic solution.

## Dependencies and scope

The only prior dependency is the definition of the hydrostatic limit inverse and its formal next-order transport equation, already audited in results193 and194. The identities needed here have been proved again above, including the full-tail finite-part relation. There is no literature or external model assertion used as a premise. Independent exact differentiation, direct numerical infinite-tail integration and axis checks follow in verification/. An actual Opus5.5 lead review is requested through the lane notes and will be recorded separately; it is not assumed complete.

The result rules out a proposed trace-level sign obstruction, including under the extra monotonicity inequalities stated here. It rules out neither hydrostatic existence nor nonexistence, and it does not address all possible far-field constraints. Neither decisive endpoint for original SettingIII is reached.
