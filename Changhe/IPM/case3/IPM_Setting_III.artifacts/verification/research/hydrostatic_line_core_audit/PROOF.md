# Vertical line constants and conditional hydrostatic far-field constraints

Written 2026-10-21 before the accompanying verification program. This is an independent audit of proposed Section3.77. The hypotheses concern the hydrostatic limiting equation, not the original full-plane IPM profile equation. The theorem below is conditional on an actual solution of that equation. A trial density with small residual does not satisfy its premise.

## Statement and notation

Let c>1, p=1/c, D=c-1. Suppose g is C2 on R2, even in x, odd in y, g_y(0)=1, and, for constants C and 0<gamma<1,

    |g| <= C(1+r)^gamma,
    |grad g| <= C(1+r)^(gamma-1),
    |g_xx| <= C(1+r)^(gamma-2),  r=sqrt(x^2+y^2).

For y>=0 define the canonical hydrostatic inverse

    V1(x,y)=-int_y^inf g_x(x,t) dt,
    V2(x,y)=int_0^y t g_xx(x,t) dt + y int_y^inf g_xx(x,t) dt.

Use the parities for y<0. Assume the equation

    (cx+V1)g_x+(cy+V2)g_y=g.

Put G(y)=g(0,y), v(y)=cy+V2(0,y), b(x,y)=cy+V2(x,y), a(x,y)=cx+V1(x,y), and Delta(x,y)=V2(x,y)-V2(0,y).

The following conclusions hold.

1. There are y0>=1 and C0 independent of x such that, for y>=y0, the improper integral I(x,y)=int_y^inf G Delta/(b v) dt converges and |I(x,y)|<=C0 x^2 y^(gamma-2). In particular, Delta cannot have a nonzero finite limit on any fixed vertical line. More generally, Delta=A y^alpha(1+o(1)), A nonzero, is impossible if alpha>gamma-1-p. If the weighted moments relative to powers Qx t^(p-2) exist absolutely on a line and on the axis, both Qx and the moments must agree.
2. Let f=r^p Theta be smooth off the origin, with the stated parities and Theta(pi/2)=K, where K is the positive axis coefficient established below. Let chi be smooth and radial, zero for r<=1/2 and one for r>=1. Write R=g-chi f. If, for all |x|>=2, v_R(x)=lim_y[V2[R](x,y)-V2[R](0,y)] exists and v_R=o(|x|^p) as |x| tends to infinity, then C_p(Theta)=0. The precise finite-part definition of C_p is given below.
3. If c>2 and |R_xx|<=C'(1+r)^(-2-epsilon), epsilon>0, then C_p=0, the common axis moment m0=0, and

    G=K y^p + A2 y^(2p-1) + o(y^(p-1)),
    A2=KQ/((1-p)D),  Q=pK+Theta''(pi/2).

If R=chi f_d+R2, where d=2p-1<0, f_d is smooth off zero, homogeneous of degree d with the same parities, and |(R2)_xx|<=C'(1+r)^(e-2), e<d, then the convergent ordinary moment C_d^-(f_d)=int_0^inf s q_d(s) ds also vanishes.
4. If c=2 and g=chi(f+f0)+R2, where f0 has degree0 and the same smoothness and parities, and |(R2)_xx|<=C'(1+r)^(e-2), e<0, define B=(f0)_xx(0,1) and C0(f0)=lim_S[int_0^S s q0(s)ds-B log S]. Then C_p=0, B=0,

    V2(0,y)=4Q sqrt(y)+C0(f0)+o(1),
    G(y)=K sqrt(y)+2KQ+(K C0(f0)/4)y^(-1/2)+o(y^(-1/2)).

Only item1 is unconditional within the hydrostatic solution class above. Items2-4 impose extra tail hypotheses. No claim of existence or nonexistence in that class, or in original IPM, follows.

## Axis facts and uniform line estimates

Evenness and the curvature bound give, by integration in x,

    |g_x(x,y)| <= C|x|(1+y)^(gamma-2),
    |g(x,y)-G(y)| <= (C/2)x^2(1+y)^(gamma-2).

These hold for every x, with common constants: at each intermediate abscissa r>=y and gamma-2<0. The inverse therefore converges absolutely on each line, and

    |V1(x,y)| <= C|x|(1+y)^(gamma-1)/(1-gamma),
    |V2(x,y)| <= C int_0^y t(1+t)^(gamma-2)dt
                  + Cy int_y^inf(1+t)^(gamma-2)dt
               <= C1(1+y)^gamma.

The second bound is uniform in x. Consequently b>=cy/2 for y>=y0 with a common y0, and |a|<=C2|x| there.

For completeness, the positive axis facts used here follow directly from the equation. On the axis vG'=G. The inverse gives v(0)=0, v'=c+int_y^inf g_xx(0,t)dt, v''=-g_xx(0,y), and v=cy+O(y^gamma). Dividing vG'=G by y at zero yields v'(0)=1. Initially v,G,G'>0. If v had a first positive zero, then G'=G/v on the preceding interval makes G positive and increasing, contradicting the continuous identity vG'=G at that zero. Thus v>0 on the whole positive axis and integration of the linear equation gives G,G'>0. Moreover 1/v-p/y=O(y^(gamma-2)) is integrable at infinity. Hence

    G=K y^p(1+O(y^(gamma-1))),  0<K<inf,
    log(G/(K y^p))=-int_y^inf(1/v-p/t)dt.

The original growth bound also forces p<=gamma. This is the axis proof in result186, repeated here to specify every dependency.

## Weighted line identity and moment rigidity

For y>=y0 subtract the axis equation, without differentiating g_xx:

    g_y-G' = (g-G)/b - a g_x/b - G Delta/(b v).                 (1)

The first two terms on the right have absolute value at most C3 x^2 y^(gamma-3). Integrating (1) over [y,Y], then taking Y to infinity, is legitimate because g(x,Y)-G(Y) tends to zero and these two terms are absolutely integrable. It proves convergence of the last integral and gives the signed identity

    I(x,y)=(g-G)(x,y)+int_y^inf[(g-G)/b-a g_x/b]dt.

This is convergence of an improper integral, with no unproved assertion of absolute convergence for its last term. The stated bound follows from int_y^inf t^(gamma-3)dt=y^(gamma-2)/(2-gamma).

For fixed x the positive weight G/(bv)=(K/c^2)t^(p-2)(1+O(t^(gamma-1))). If Delta=A t^alpha(1+o(1)), A nonzero, the integrand eventually has one sign. If p-1+alpha>=0 its integral diverges. Otherwise its tail magnitude is asymptotic to K|A|y^(p-1+alpha)/(c^2(1-p-alpha)). This contradicts the bound whenever alpha>gamma-1-p. The inequality is strict; the argument asserts nothing at equality. A nonzero finite limit has alpha0 and is excluded since gamma-1-p<0. Divergence to either sign of infinity is excluded as well by comparison to a nonzero constant on a final interval, though no general oscillatory pointwise bound on Delta is being claimed.

If e_x(t)=g_xx(x,t)-Qx t^(p-2) and int_0^inf t|e_x|dt<inf, direct integration, not a formal asymptotic interchange, gives

    V2(x,y)=Qx y^p/(p(1-p))+m(x)-int_y^inf(t-y)e_x(t)dt,
    m(x)=int_0^inf t e_x(t)dt.

The last integral tends to zero by the absolute moment hypothesis. Subtracting the corresponding axis identity, a difference in Q gives the excluded power alpha=p; after its removal a difference in m gives an excluded nonzero limit. Thus Qx=Q and m(x)=m0 wherever both weighted moment hypotheses hold. No spatial regularity of m is needed.

## Homogeneous line inversion with fixed constants

For u homogeneous of degree q, even in x and odd in y, set F_q(s)=u(1,s). On x>0, u(x,y)=x^q F_q(y/x). Two x derivatives give

    u_xx(x,t)=x^(q-2)q_u(t/x),
    q_u=q(q-1)F_q-2(q-1)s F_q'+s^2 F_q''.

Evenness extends the expression to |x|. Smoothness at the horizontal axis gives q_u=O(s) as s tends to zero. Smoothness and evenness at the vertical axis give, with Q_u=u_xx(0,1),

    F_q(s)=K_u s^q+(Q_u/2)s^(q-2)+O(s^(q-4)),
    q_u(s)=Q_u s^(q-2)+O(s^(q-4)).

The second expansion is justified by the smooth Taylor expansion including its differentiated remainders, not by differentiation of an arbitrary big-O formula. For q=p in(0,1) define

    C_p=int_0^inf s[q_f(s)-Q s^(p-2)]ds.

At zero s^(p-1) is integrable. At infinity the subtracted integrand is O(s^(p-3)), also integrable. Explicit integration then yields

    V2[f](x,y)=Q y^p/(p(1-p))+C_p|x|^p+O(x^2 y^(p-2))

as y tends to infinity for each fixed nonzero x. No use of this homogeneous singular density on x=0 is made. The smooth cutoff instead gives exactly, for y>=1,

    V2[chi f](0,y)=Q y^p/(p(1-p))+kappa,
    kappa=int_0^1 t(chi f)_xx(0,t)dt-Q/p.

For |x|>=2 the cutoff and all its derivatives are identically one along a neighborhood of the whole vertical line. Thus V2[chi f](x,y)=V2[f](x,y). Linearity and the remainder hypothesis in item2 imply

    Delta(x,y) -> C_p|x|^p-kappa+v_R(x).

Item1 makes this limit zero. Divide by |x|^p and let |x| tend to infinity, in that order. This proves C_p=0. These two limiting operations use the expressly stated hypothesis; they do not assume a uniform homogeneous expansion down to the axis.

## Decaying remainders and c>2

If |R_xx|<=C(1+r)^(-2-epsilon), then

    w(x)=int_0^inf t R_xx(x,t)dt,
    |w(x)|<=C_epsilon(1+|x|)^(-epsilon).

Indeed r>=(|x|+t)/sqrt2 and the elementary integral of t(A+t)^(-2-epsilon) is A^(-epsilon)/(epsilon(1+epsilon)). Also V2[R](x,y)=w(x)-int_y^inf(t-y)R_xx dt. Its tail tends to zero, so v_R=w-w(0). Item2 gives C_p=0. The vanishing line limit then says w(x)=kappa+w(0) for |x|>=2. Taking |x| to infinity gives kappa+w(0)=0, and in fact w(x)=0 on every such line.

The homogeneous comparison and the remainder bound ensure the weighted moment hypothesis on every line: near zero t^(p-1) is integrable; at infinity the leading homogeneous discrepancy is O_x(t^(p-4)), while tR_xx is integrable. In particular

    V2(0,y)=a_Q y^p+E(y),  a_Q=Q/(p(1-p)),
    E(y)=-int_y^inf(t-y)R_xx(0,t)dt=O(y^(-epsilon)).

Thus m0=0. Expanding the exact axis integral gives

    1/v-p/t=-a_Q t^(p-2)/c^2+O(t^(2p-3))+O(t^(-2-epsilon)),
    log(G/(Ky^p))=a_Q y^(p-1)/(c^2(1-p))
                    +O(y^(2p-2))+O(y^(-1-epsilon)).

When p<1/2, both remainders are o(y^-1). Exponentiating and multiplying by Ky^p proves item3 and its coefficient. The square of the first correction also has order y^(3p-2)=o(y^(p-1)); this is where c>2 matters. Neither this truncation nor its error is asserted for p>=1/2.

For the additional term f_d, d=2p-1<0, smoothness gives q_d=O(s) near zero and q_d=Q_d s^(d-2)+O(s^(d-4)) at infinity. Consequently s q_d is integrable. For |x|>=2,

    w(x)=C_d^-|x|^d+O(|x|^e),  e<d.

The remainder estimate follows by integrating t(|x|+t)^(e-2). The previous paragraph applies because d-2<-2, and gives w(x)=0 outside the cutoff. Dividing by |x|^d proves C_d^-=0. The ordinary homogeneous inverse on the singular vertical axis was never assumed to converge for d<0.

## Degree zero and the logarithmic case c=2

Here F0(s)=F_inf+(B/2)s^-2+O(s^-4), and q0=2sF0'+s^2F0''=B s^-2+O(s^-4). Hence the finite part C0 exists and

    int_0^S s q0 ds=B log S+C0+O(S^-2),
    S int_S^inf q0 ds=B+O(S^-2).

Both terms are required: the upper integral supplies the additional B. For |x|>=2,

    V2[f0](x,y)=B log y-B log|x|+C0+B+o(1).

On the axis the cutoff gives V2[chi f0](0,y)=kappa0+B log y+B, where kappa0=int_0^1 t(chi f0)_xx(0,t)dt. With w2(x)=int_0^inf t(R2)_xx dt=O((1+|x|)^e), subtraction therefore gives

    Delta -> C_p|x|^(1/2)-B log|x|+C0-kappa-kappa0+w2(x)-w2(0).

This limit is zero by item1. Successively divide by |x|^(1/2), then by log|x| after removing C_p, and finally take the unscaled limit. It follows that C_p=0, B=0, and C0=kappa+kappa0+w2(0). In particular C0 need not be zero. The axis velocity is 4Q sqrt(y)+C0+O(y^e).

Set u=2Q y^-1/2+C0/(2y)+O(y^(e-1)). Since v=2y(1+u), expansion of the exact integral gives

    log(G/(K sqrt(y)))=2Q y^-1/2+(-2Q^2+C0/4)y^-1+o(y^-1).

The quadratic term of the exponential contributes +2Q^2/y and cancels the displayed -2Q^2/y. This proves item4. Omitting that cancellation or the upper-tail B before setting B=0 gives an incorrect constant.

## Independent controls and optional Taylor identity

The equation premise cannot be omitted. The smooth density g=y exp(-r^2) satisfies all weighted bounds and g_y(0)=1. Its inverse is V1=x exp(-r^2), V2=sqrt(pi)(x^2-1/2)exp(-x^2)erf(y). At c=2 it even has v'(0)=1. Its limiting V2 depends on x, however, and it does not solve the transport equation. It is a counterexample to any inference from the inverse, symmetry, growth and origin relation alone.

Likewise B=0 does not imply C0=0 for a degree-zero trace. For

    f0=y/r+(1/2)yx^2/r^3,
    F0'=3/(2(1+s^2)^(5/2)),

B=0 and integration of s(s^2F0')' gives C0=-1/2. This is a smooth angular trace with the required parities, not a hydrostatic solution.

If the leading homogeneous inverse is smooth at the vertical axis (in particular under the previously proved C_p=0 criterion for a smooth trace), put T=f_xxxx(0,1). Taylor expansion of V[f].grad f/D gives the optional identity

    (f_d)_xx(0,1)=1/D[-(p+2)Q^2/(p(1-p))
                         +pKT/((p-2)(3-p))].

Indeed V1=-Q x y^(p-1)/(1-p)+O(x^3), V2=Q y^p/(p(1-p))+T x^2 y^(p-2)/(2(p-2)(3-p))+O(x^4). Multiply by f_x=Qx y^(p-2)+O(x^3) and f_y=pK y^(p-1)+(p-2)Qx^2 y^(p-3)/2+O(x^4) and take twice the x^2 coefficient. This identity needs the smooth inverse premise and does not force B nonzero.

## Scope, dependencies and evidence order

Read this proof, then verification/CHECKS.json and VERDICT.md when completed. The independent source copies in sources/ and their hashes in verification/INPUTS.json identify the exact proposed text and the external referee analysis. Result186 supplies the previously checked axis theorem; the needed argument is repeated above. Results193/194 and209 establish the homogeneous inverse conventions and smooth-cusp scope, also rederived above for the particular uses here. The verification program supplies symbolic identities, exact counterexamples and selected numerical quadrature checks; the mathematical proof is the argument in this file. No program output upgrades a formal expansion to a theorem about all solutions. Proposed Section3.77 states sufficient hypotheses; no assertion that these hypotheses are minimal or automatic is made. Actual lead-model collaboration is with Opus5.5 through the lane notes. The external referee analysis reports an unsuccessful Opus invocation, which is not counted as another model review.
