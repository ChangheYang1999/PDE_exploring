# Simple axis endpoints: limits, signs and analytic realizations

## Statement, hypotheses and scope

Fix beta>0 and write L=3beta+2, M=2beta+1 and N=7beta+2. Let b,T,eta,v,D be real smooth functions on a neighborhood of y_* satisfying

    b T_y+(L-2b_y)T=0,
    b eta_y+(M-b_y)eta=T,
    eta=-b_yy-2v,
    b D_y+(N-4b_y)D=8v_y T-12v T_y.                 (1)

Assume b(y_*)=T(y_*)=0, b_y(y_*)!=0 and T!=0 on a punctured side. Put y=y_*-epsilon s, s>0, epsilon in {-1,1}. These are four local axis relations. No global inverse, center data, complete axis hierarchy or B2 profile is asserted.

Then T has finite integer vanishing order n>=1 and T=C s^n tau(s), C!=0, with tau smooth and tau(0)=1. Consequently I2=D/T^2 has a limit in the extended real line. If D has first nonzero Taylor coefficient d_j at order j, then I2~(d_j/C^2)s^(j-2n). If D is flat, I2 tends to zero. Oscillatory failure of a limit is impossible at a simple zero under these hypotheses.

At an attractive endpoint b_y(y_*)=-c<0, n=2+L/c>=3. For every side and every nonzero A, all finite values and both infinite signs of A I2 occur among smooth local solutions of (1) already at beta=2,c=1 with A/T>0. Finite values can occur with v identically zero and even with the leading homogeneous coefficient of eta having the same sign as C. The examples are not asserted to extend to global profiles.

If an attractive smooth solution has b=epsilon B(s), B=cs+ks^2+O(s^3), and k!=0, its ratio K=D/T necessarily satisfies

    K= -12kn/(4beta+3c) s^(-1)(1+o(1)).            (2)

This is a necessary conclusion for an already smooth solution. It is not an existence assertion for arbitrary prescribed B.

## Finite vanishing order and the complete limit classification

Write xi=y-y_* and b=xi a(xi), with a smooth and a(0)=b1!=0. Direct division gives

    T_y/T = 2b_y/b-L/b = alpha/xi+q(xi),
    alpha=2-L/b1,

where q is smooth through zero: each apparent difference quotient has smooth numerator vanishing at zero and a nonzero denominator a. Integrating on either punctured side gives T=C_0 |xi|^alpha exp(Q(xi)), where Q is smooth. The nonzero exponential tends to a positive constant. Since T tends to zero, alpha>0. Such a function cannot be flat: a flat smooth function is O(|xi|^m) for every integer m, contradicting the displayed asymptotic for m>alpha. Thus T has a first nonzero Taylor coefficient, at an integer n>=1. Comparison of its Taylor asymptotic with the explicit formula gives alpha=n. Normalizing the positive smooth factor yields T=C s^n tau(s), tau(0)=1. If b1=-c, n=2+L/c>2.

A smooth D is either flat or has a first nonzero Taylor coefficient. In the latter case D=d_j s^j(1+o(1)), d_j!=0, so division by C^2s^(2n)tau^2 proves the classification. If D is flat, Taylor's theorem gives D=o(s^(2n)), and the limit is zero. This covers every smooth D; it does not assume analyticity or derive a limit merely from a formal series. Multiplication by A!=0 preserves existence of the extended limit.

## Exactly linear endpoints, including resonances

Suppose B=cs exactly with c>0. Put

    n=2+L/c, m=1+M/c, lambdaK=2+4beta/c,
    delta=n+lambdaK=4+N/c,
    h=c+beta+1, F=8c+10beta+8,
    R1=2c+2beta-1, R2=c+beta-2.

The first three equations in (1), written in s, have solutions

    T=C s^n,
    eta=H s^m-(C/h)s^n,
    v=-eta/2.                                    (3)

Indeed B T_s=(L+2B_s)T and B eta_s=(M+B_s)eta-T. Since n-m=h/c>0, the two powers are distinct.

For K=D/T, the fourth equation reduces exactly to

    -cs K_s+(4beta+2c)K=Q,
    Q=-epsilon(FH/c)s^(m-1)+epsilon(2nC/h)s^(n-1). (4)

To obtain the second coefficient, use F-4h=2cn. The operator on s^r is c(lambdaK-r)s^r. When R1,R2 are nonzero, c(lambdaK-m+1)=R1 and c(lambdaK-n+1)=R2 give

    D=E s^delta-epsilon FCH/(cR1)s^(n+m-1)
                      +epsilon 2nC^2/(hR2)s^(2n-1),
    I2=(E/C^2)s^((beta-2)/c)
       -epsilon FH/(cR1C)s^(-2-(beta+1)/c)
       +epsilon 2n/(hR2)s^(-1).                 (5)

Here E is arbitrary before smoothness is imposed. At R1=0, the H term in K is epsilon FH/c^2 s^(m-1)log s. At R2=0, the C term in K is -epsilon 2nC/(ch)s^(n-1)log s. This follows from the operator on s^r log s at r=lambdaK, which is -c s^r.

Smoothness requires integer n; if H!=0 it also requires integer m. If delta is not an integer, E must vanish. Nonzero powers times log s are not smooth through zero. The R1 resonance therefore forces H=0. The R2 resonance has nonzero C coefficient and permits no smooth exactly linear realization with T nonzero. These two resonances cannot coincide: at R2=0, R1=3. Away from resonance, the nonzero s^-1 term in (5) cannot be canceled by the other distinct powers. Thus a smooth exactly linear attractive endpoint never has finite I2, although nonlinear B can, as proved below.

## Polynomial examples giving both infinite signs at beta=2

For beta=2,c=1 and arbitrary real C!=0,H,E, set

    b=epsilon s,
    T=C s^10,
    eta=H s^6-(C/4)s^10,
    v=-eta/2,
    D=E s^20-epsilon(36/5)CH s^15+epsilon 5C^2s^19.   (6)

Interpret s=epsilon(y_*-y) as signed on a full neighborhood. These polynomials are smooth through the endpoint; no zero extension is used. Formula (3) proves the first three equations, while the fourth is

    -s D_s+20D=epsilon[-36CHs^15+5C^2s^19],

which follows by direct differentiation. The ratio is

    I2=E/C^2-epsilon(36H/(5C))s^-5+epsilon5s^-1.

Choose C with A/C>0. The sign of the leading term of A I2 can be either sign by choosing nonzero H of either sign. All hypotheses remain unchanged. The equations therefore do not give a universal sign from beta,c or orientation alone. A separately imposed global relation might restrict H; these local examples assert no such freedom for a prescribed global center.

For comparison, the beta=c=1/5 polynomials from (5) are

    b=epsilon s/5, T=Cs^15,
    eta=Hs^8-(5C/7)s^15, v=-eta/2,
    D=Es^21+epsilon290CHs^22-epsilon(375/28)C^2s^29.

They give I2=(E/C^2)s^-9+epsilon(290H/C)s^-8-epsilon(375/28)s^-1. Even C=H=A=1 leaves either infinite sign available by choosing E. This supplementary example is a local beta>0 statement and is not presented as a beta>=2 profile counterexample.

## Curvature can change the leading law

For any smooth attractive solution, B=cs+ks^2+O(s^3), T=Cs^n tau(s) as above, and eta(0)=0, since the second equation of (1) at the endpoint is (M+c)eta(0)=T(0)=0. Thus eta/B is bounded and T/B tends to zero. The exact ratio equation, obtained from (1), is

    -B K_s+(4beta+2B_s)K=Q,
    Q=4B_sss-6B_ss(L+2B_s)/B
      -epsilon[(10beta+8+8B_s)eta+4T]/B.          (7)

Taylor's theorem gives sQ -> -12k(L+2c)/c=-12kn. Set t=integral_s^s0 du/B, so t tends to infinity and d/dt=-B d/ds. For Z=sK, (7) becomes

    Z_t+(4beta+2B_s+B/s)Z=sQ.

The coefficient tends to4beta+3c>0. A scalar equation Z_t+a(t)Z=f(t) with a->a_*>0 and f->f_* has Z->f_*/a_*: subtract that constant, apply the integrating factor, bound the recent forcing by its tail supremum, and let the exponentially decaying contribution from each fixed earlier interval vanish. This proves (2). Nonzero curvature can therefore dominate the exactly linear powers. No existence for arbitrarily prescribed curvature has been used.

## Analytic examples attaining every finite ratio at beta=2

Fix beta=2,c=1, epsilon in {-1,1}, real C!=0,H and ell. Seek analytic functions x,z,h,g of signed s near zero with x(0)=z(0)=0,h(0)=H,g(0)=C satisfying

    s x_s=z-x,
    s z_s=-epsilon s^7h,
    (1+x)s h_s=(z-6x)h-s^4g,
    (1+x)s g_s=(2z-10x)g.                       (8)

Define B=s(1+x), b=epsilon B, T=s^10g, eta=s^6h, v=0 and D=ell T^2. The first equation gives B_s=1+z and the second gives B_ss=-epsilon eta, which is the curl relation. The last two equations are exactly the eta and thermal relations. Finally, with v=0, substitution D=ell T^2 into the fourth relation gives

    ell T^2[N-2L]=(beta-2)ell T^2=0.

Thus the four relations hold at beta=2. For small positive s, B>0 and T has the sign of C. Hence A/C>0 supplies A/T>0 and I2=ell exactly.

It remains to prove existence of actual analytic functions, rather than a formal expansion. Put X=(x,z,h-H,g-C). The right side of (8), after dividing only by1+x in the last two equations, is analytic near(0,0), and has the form

    sX_s=A0X+R(s,X),
    A0=[[-1,1,0,0],[0,0,0,0],[-6H,H,0,0],[-10C,2C,0,0]].

Taylor's theorem for this analytic function gives R(s,0)=O(s^4) and ||D_X R(s,X)||<=C_0(|s|+|X|) on a sufficiently small complex neighborhood. The eigenvalues of A0 are -1,0,0,0. Jordan normal form implies ||r^(-A0)||<=C_1(1+|log r|^q) for0<r<=1 and some finite q: the eigenvalue-1 contribution carries the bounded factor r; zero-eigenvalue blocks give only powers of log r.

Use the Banach space of vector functions analytic in the disk |s|<delta, continuous on its closure, vanishing at0, with norm ||X||_*=sup |X(s)|/|s|. Define

    F(X)(s)=integral_0^1 r^(-A0) R(rs,X(rs)) dr/r. (9)

On the ball ||X||_*<=K, the stated derivative bound and R(rs,0)=O(r^4|s|^4) show that ||F(0)||_*=O(delta^3) and that the Lipschitz constant of F is at most C_2(1+K)delta. Integrals of r^a|log r|^q are finite for a>-1. For a fixed positive K, choose delta small enough to preserve the ball and make the Lipschitz constant less than1. Uniform convergence of the analytic integrals proves F maps this Banach space into itself. The contraction theorem gives a unique fixed point in the ball. The data are real, so conjugation preserves F and uniqueness makes the fixed point real on the real interval.

For any analytic G=O(s), differentiation under the integral gives

    (s d/ds-A0) integral_0^1 r^(-A0)G(rs)dr/r=G(s).

Indeed the integrand after differentiation is d/dr[r^(-A0)G(rs)], whose boundary value at0 is zero by G(rs)=O(r|s|) and the logarithmic bound. Applying this identity to G(s)=R(s,X(s)) proves (8) for the fixed point. Thus the functions used above are actual real analytic solutions on a signed neighborhood. Taking H/C>0 is permitted independently of ell. Choosing ell to be any desired finite ratio, or ell=value/A for A I2, proves finite attainability.

## Dependencies and limits

The proof uses only smooth Taylor theory, elementary first-order integrating factors, the finite-dimensional Jordan estimate, and the contraction theorem with the explicit estimates above. The four equations are independently derived from the coefficient hierarchy in P286/P289. The lead's A166 discussion supplied the claims to audit, not assumptions to trust. Exact symbolic checks are supplementary controls of displayed identities and matrix algebra; they do not replace the endpoint, smoothness or analytic-existence arguments. No global profile, admissible inverse, far-field condition or decisive B2 endpoint is obtained.
