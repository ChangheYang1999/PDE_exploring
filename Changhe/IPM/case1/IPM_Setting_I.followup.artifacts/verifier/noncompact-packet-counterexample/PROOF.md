# A noncompact packet with a smooth nonzero first trace

Date: 2026-10-21. Status: CONFIRMED by independent derivation, exact checks and completed Claude Opus 5.5 review. This is a counterexample to deleting compact support from the scalar trace rigidity statement in ../complex-packet-rigidity/PROOF.md. It is not a counterexample to that correctly qualified theorem or a coupled IPM profile.

## Exact statement

Set A=2, g=1, q=2, b=1/2, eta=1 and c_F=(2pi)^(-2). For t>0 define

    u(t)=t^(-1/2) exp(-(log t)^2) sin(2pi log t),
    Phi(t)=u(t),    Phi(-t)=-u(t),    Phi(0)=0.

Then Phi is a nonzero real Schwartz function, flat at zero, with Phi(-t)=-conjugate(Phi(t)) and integral_R Phi=0. It is not supported in a compact annulus. The grouped packet integral

    V(s,y)=2i c_F integral_0^infinity sin(yr)r^(-2)
            integral_R Phi(t) exp(i s t r^2)(1+t^2 r^2)^(-1/2)dt dr

converges and has a classical first y derivative at y=0. Its trace G(s)=partial_y V(s,0) is C^infinity on R, and

    G'(0)=-4c_F sqrt(pi) exp(1/16-pi^2) != 0.             (1)

Every weighted moment occurring in the compact-annular first-trace rigidity proof nevertheless vanishes:

    M_n=integral_0^infinity u(t)t^(-1/2-n)dt=0,
    n=0,1,2,... .                                       (2)

No two-dimensional smoothness of V is claimed. Smoothness of one scalar trace does not supply it. No coupled velocity law, admissible global profile or task endpoint is asserted.

## Gaussian identity and exact moments

For real lambda and omega, absolute integrability and differentiation under the integral give

    integral_R exp(-z^2+lambda z) sin(omega z)dz
      =sqrt(pi) exp((lambda^2-omega^2)/4) sin(lambda omega/2). (3)

For completeness, first complete the real square and shift z by lambda/2. The sine of the shifted phase decomposes into an odd sine integral and a cosine integral. The odd integral is zero. Put F(omega)=integral exp(-z^2)cos(omega z)dz. Integration by parts, with vanishing Gaussian boundary terms, gives F'(omega)=-(omega/2)F(omega). Since F(0)=sqrt(pi), F= sqrt(pi)exp(-omega^2/4). The value at zero follows by squaring the Gaussian integral and using polar coordinates; all integrands in that step are nonnegative. This proves (3) without a complex contour shift.

Under z=log t, the moment in (2) becomes integral exp(-z^2-nz)sin(2pi z)dz. Formula (3) makes it sqrt(pi)exp(n^2/4-pi^2)sin(-n pi)=0. All these integrals are absolutely convergent. More generally integral |u(t)|t^p dt is finite for every real p, since its logarithmic integrand is bounded by exp(-z^2+(p+1/2)z).

For J=integral_0^infinity u(t)t^(-1)dt, (3) with lambda=-1/2 gives

    J=-sqrt(pi)exp(1/16-pi^2).                            (4)

The datum is nonzero, for example at t=exp(1/4). Derivatives of u are finite sums of powers of t, polynomials in log t and sin/cos factors times exp(-(log t)^2). The Gaussian in log t dominates every power at both ends. Thus all derivatives vanish faster than every power at zero and infinity. Odd extension gives a real Schwartz function flat at zero. Absolute integrability and oddness give integral Phi=0.

## Convergent trace formula

Pair the t and -t integrals. The inner integral is2i integral_0^infinity u(t)sin(s t r^2)(1+t^2r^2)^(-1/2)dt. At small r its absolute value is at most C|s|r^2 integral |u|t. At large r it is at most C r^(-1) integral |u|t^(-1). Both moments are finite. These bounds, with sin(yr) bounded by min(|y|r,1), justify V and dominated differentiation once in y, uniformly on compact s,y intervals. Therefore

    G(s)=-4c_F integral_0^infinity dr/r
                 integral_0^infinity u(t)sin(s t r^2)
                                      (1+t^2r^2)^(-1/2)dt.

For each fixed s the double integral is absolutely integrable: the small-r sine estimate and the large-r weight bound just given suffice. Substitute k=t r^2; then dr/r=dk/(2k) and t^2r^2=kt. Fubini gives

    G(s)=-2c_F integral_0^infinity sin(sk) h(k)dk,
    h(k)=k^(-1) integral_0^infinity u(t)(1+kt)^(-1/2)dt.  (5)

At small k, |h(k)|<=k^(-1) integral|u|, so the sine must be retained. Its contribution on0<k<1 is C^infinity: order j>=1 is dominated by k^(j-1) and order0 by C|s|. No divergent integral of h at zero is introduced.

## Vanishing moments make the high-frequency trace smooth

For every integer N>=1, Taylor's formula on the entire nonnegative real axis gives

    (1+z)^(-1/2)=sum_(n=0)^(N-1) a_n z^n+R_N(z),
    a_n=(-1)^n(1/2)_n/n!,
    |R_N(z)|<=((1/2)_N/N!) z^N,    z>=0.                 (6)

Indeed the Nth derivative has absolute value(1/2)_N(1+z)^(-1/2-N)<=(1/2)_N, so the integral remainder has the stated bound. This is global in z; no uniform lower bound on t is needed.

Factor (1+kt)^(-1/2)=k^(-1/2)t^(-1/2)(1+(kt)^(-1))^(-1/2). Insert (6) into (5). Each finite Taylor coefficient integrates to the zero moment M_n. The remainder is absolutely bounded using the already established weighted absolute moments. Hence for k>=1,

    |h(k)|<=C_N k^(-3/2-N)
                integral_0^infinity |u(t)|t^(-1/2-N)dt. (7)

For every derivative order j choose N>j-1/2. Then integral_1^infinity k^j |h(k)|dk<infinity. Differentiation under the sine transform at every order follows, uniformly on compact s intervals. Together with the low-frequency argument this proves G is smooth on R.

Compactness was essential in the earlier moment argument: t^(-1) now ranges over an unbounded interval, so approximation by polynomials on a compact interval no longer forces u=0. Equation (2) supplies a concrete nonzero signed density with all those moments zero.

## The trace is nonzero

Let f(k)=k h(k). It is integrable over0<k<infinity by (7) and the small-k bound. Thus from (5),

    G'(0)=-2c_F integral_0^infinity f(k)dk.               (8)

For finite K>0, Fubini is justified by absolute integrability and gives

    integral_0^K f(k)dk
      =2 integral_0^infinity u(t)t^(-1)[sqrt(1+Kt)-1]dt.

Since M_0=integral u(t)t^(-1/2)dt=0, subtract2sqrt(K)M_0. Rationalizing the difference gives exactly

    integral_0^K f(k)dk
      =2 integral_0^infinity u(t)t^(-1)
           [1/(sqrt(1+Kt)+sqrt(Kt))-1]dt.                (9)

The bracket has absolute value at most1 for Kt>=0 and tends to-1 for every t>0. The weight |u|/t is integrable. Dominated convergence therefore gives integral f=-2J. Combining(8) and(4) yields(1), which is nonzero. This also confirms that the construction has a nonzero smooth trace, not merely nonzero data invisible to that trace.

## Dependencies, verification and scope

The only dependency is the explicit packet convention in ../complex-packet-rigidity/PROOF.md; the trace and all estimates needed here are reproved. Exact symbolic moment/constant identities and independent quadrature illustrations will be placed in code/ and verification/. They test the formulas but are not proofs of smoothness. This result demonstrates the necessity of compact-annular support for that scalar rigidity theorem. It does not make any assertion about all frozen solutions, smoothness in two dimensions, the nonlinear equation, a profile's center or source regularity, or existence/nonexistence in the strong setting.
