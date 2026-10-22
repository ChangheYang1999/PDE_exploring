# Infinitely flat axis endpoints with two different ratio behaviors

## Exact statement and scope

Fix beta>0, epsilon in {-1,1}, a point y_* and a nonzero real A. Put L=3beta+2, M=2beta+1, d=L/2 and c=3d/beta. For each of the two choices

    B0(s)=exp(-1/s),
    B1(s)=exp(-1/s)[2+sin(s^-2)],       0<s<s0,

there are real smooth local axis functions b,T,eta,v,D across y_* such that, with y=y_*-epsilon s,

    b(y)=epsilon B(s),    A/T(y)>0,
    b T_y+(L-2b_y)T=0,
    b eta_y+(M-b_y)eta=T,
    eta=-b_yy-2v,
    b D_y+(7beta+2-4b_y)D=8v_y T-12v T_y.       (1)

Every one of b,T,eta,v,D is flat at y_*. On the other side all five functions may be zero. Write K=D/T and I2=D/T^2 on the nonzero side. Then

    K(s)=-c B''(s)/B(s)+o(1).                  (2)

Primes in (2) denote s derivatives. In the B0 example,

    K(s)=-c(s^-4-2s^-3)+o(1),  A I2 -> -infinity.

In the B1 example let s_n^+=(pi/2+2pi n)^(-1/2) and s_n^-=(3pi/2+2pi n)^(-1/2), for all sufficiently large n. Then

    K(s_n^+)~(4d/beta)(s_n^+)^-6,
    K(s_n^-)~-(12d/beta)(s_n^-)^-6.

Thus A I2 has subsequences tending to positive and negative infinity. In particular the four local axis equations alone do not force a one-sided sign or a limit of A I2 at an infinitely flat endpoint.

These are local four-equation axis data. They assert neither the complete hierarchy of axis equations nor a global canonical inverse, center normalization, admissible far field or B2 profile. The negative conclusion concerns an attempted extension of the finite-order endpoint law under only these local hypotheses. It does not refute a theorem using additional global information.

## Smoothness estimates for B and its time coordinate

Write B=exp(-1/s)h(s), with h=1 or h=2+sin(s^-2). In both cases 1<=h<=3, and every fixed derivative of h and of 1/h is bounded by some power of 1/s on a sufficiently small interval. The latter follows inductively by differentiating h(1/h)=1, using h>=1. Hence every derivative of B is exp(-1/s) times a polynomially bounded function, and every derivative of 1/B is exp(1/s) times such a function. In particular B extends smoothly by zero through s=0, with every derivative zero.

Set

    t(s)=integral_s^s0 du/B(u).

Then t_s=-1/B, t>=0, and t tends to infinity. The bounds on h compare this integral to integral_s^s0 exp(1/u)du. Substitution z=1/u changes the latter to integral_(1/s0)^(1/s) exp(z)z^-2 dz. The ratio of this integral to exp(1/s)s^2 tends to1: both diverge, and the quotient of their derivatives with respect to z tends to1. Therefore there are constants c1,c2>0 such that

    c1 s^2 exp(1/s)<=t(s)<=c2 s^2 exp(1/s)

for all sufficiently small s. Every positive-order s derivative of t is bounded by exp(1/s) times a power of 1/s. It follows in particular that, for every mu>0 and every fixed C,N,

    s^-N exp(C/s) exp(-mu t(s)) ->0.            (3)

Indeed t(s)/(1/s+|log s|) tends to infinity. Repeated differentiation of exp(-mu t) gives a finite sum of products of derivatives of t times exp(-mu t), so each fixed derivative obeys a bound of the form in (3), with a possibly larger C,N. These bounds establish flatness, not merely pointwise decay.

## Exact thermal and vorticity coefficients

Choose a nonzero constant C with A/C>0 and an arbitrary real H. Define

    T=C B^2 exp(-Lt),
    J(t)=H+C integral_0^t B(s(u)) exp(-(L-M)u)du,
    eta=B exp(-Mt)J(t),
    v=-epsilon B''/2-eta/2.                   (4)

Here s(u) is the inverse of the strictly decreasing time coordinate. Since L-M=beta+1>0 and B is bounded, J is bounded for t>=0. Its spatial derivative is exactly J_s=-C exp(-(L-M)t). Thus every positive spatial derivative of J has a bound given by (3) with mu=L-M, while J itself is bounded. Formulas (3)-(4) prove flatness of T, eta and v. They also show directly, using b_y=-B' and b_yy=epsilon B'', that the first three equations in (1) hold. For example

    B T_s=(L+2B')T,
    B eta_s=(M+B')eta-T.

The constant C fixes the sign of T. The functions T and B have no zeros for 0<s<s0.

## Exact quartic ratio equation and the curvature approximation

The fourth equation divided by T, minus K times the first equation divided by T, gives

    -B K_s+(4beta+2B')K=Q,
    Q=4B'''-6B''(L+2B')/B
      -epsilon[(10beta+8+8B')eta+4T]/B.        (5)

This formula is independently derived in P286 for both orientations, and is verified again here from (1). It does not require finite order of B.

Let F=B''/B and P=-cF, where c=6L/(4beta)=3d/beta. Every spatial derivative of F is polynomially bounded: differentiating B''/B cancels the common exponential, leaving derivatives of h divided by powers of h and finite powers of 1/s. Put

    R=K-P,   a(s)=4beta+2B',
    H0(s)=Q+B P_s-aP.

Since 4beta P=-6L F, cancellation in H0 gives

    H0=4B'''+(-12+2c)B'F-cB F'
        -epsilon[(10beta+8+8B')eta+4T]/B.     (6)

Each of the first three terms tends to zero: it is exp(-1/s) times a polynomially bounded factor. The final term and all its derivatives are flat by (3)-(4), even after division by B. Thus H0(s)->0 and a(s)->4beta>0.

Solve (5) from any fixed interior point with an arbitrary finite value of K there. On every compact punctured interval ordinary linear ODE theory gives a unique solution, and its integrating-factor formula extends it to all 0<s<=s0. Since ds/dt=-B, the difference solves

    R_t+a(s(t))R=H0(s(t)).                   (7)

It follows that R->0. Explicitly, from a sufficiently late time a>=2beta. Variation of constants bounds the homogeneous term by its initial magnitude times exp(-2beta(t-t1)). If |H0|<=delta after t1, the inhomogeneous term is at most delta/(2beta). Taking the upper limit and then delta->0 proves the assertion. This establishes (2), including its absolute o(1) error.

To prove that D=TK joins smoothly, note first that F is polynomially bounded and R->0, so K is polynomially bounded. Every derivative of Q is polynomially bounded: its geometric terms have this property, and its thermal terms are flat as just shown. Rewrite (5) as

    K_s=[(4beta+2B')K-Q]/B.

An induction using Leibniz's rule and the bounds for derivatives of B and 1/B gives, for each fixed j, a bound |K^(j)|<=exp(C_j/s)s^-N_j for some finite constants C_j,N_j. The step multiplies finitely many already bounded derivatives by at most one extra exp(1/s) factor; no uniform estimate in j is needed. Combining this with (3) and the corresponding derivative bounds for T shows that every derivative of D=TK tends to zero. Hence D extends smoothly and flatly. On the other side set b,T,eta,v,D all equal to zero. Every join is smooth, (1) holds on both punctured sides, and it holds at the common endpoint by continuity. This proves existence of the asserted local data.

## The two asymptotic behaviors

For B0 direct differentiation yields

    B0''/B0=s^-4-2s^-3.

The factor c is strictly positive, so (2) gives K->-infinity. Since A/T is positive and tends to positive infinity, A I2=(A/T)K tends to negative infinity.

For B1, put q=s^-2. Direct differentiation, including the derivatives of its oscillatory factor, gives

    B1''/B1=s^-4-2s^-3
      +[-4s^-6 sin(q)+6s^-4 cos(q)-4s^-5 cos(q)]/[2+sin(q)].      (8)

At s_n^+, sin(q)=1, cos(q)=0, and the leading term in (8) is -(4/3)s^-6. At s_n^-, sin(q)=-1, cos(q)=0, and it is 4s^-6. The exact o(1) remainder in (2) is negligible relative to s^-6. Multiplication by -c gives the displayed constants 4d/beta and -12d/beta. Multiplication by A/T>0, tending to infinity on each sequence, proves the two opposite infinite subsequential limits of A I2.

## Dependencies and evidentiary limits

The proof uses elementary calculus, linear ODEs, the physical four-axis equations and the exact ratio identity. All endpoint smoothness and limit arguments are included above. The construction suggested in A161 D5(ii) is treated as a proposal, not an authority. The present argument independently checks the oscillatory derivatives, absolute error estimate, flat extension and both orientation signs. Exact symbolic controls and actual model review follow separately. There is no formalization or numerical B2 existence claim.

Written 2026-10-22T05:55:04.532646+00:00 before controls.
