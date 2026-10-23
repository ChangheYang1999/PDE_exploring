# Global capped nonprofiles and a fixed weighted residual gap

Date: 2026-10-20. Status: independent analytic reconstruction CONFIRMED; supporting exact checks follow the proof. These examples satisfy the elliptic law and several necessary conditions, but fail exact transport. They do not decide primary existence.

## Statements and notation

Let S=(DU+DU^T)/2, sigma=sup ||S||_op, and M=sup_({X!=0})[-X.U/|X|^2]. A canonical pair obeys -Delta psi=rho_x, U=(-psi_y,psi_x), the required parities and U=o(r). We prove two constructions.

For ell=2, D=1, A=3, put c_*=1/73746, C=16/c_*=1179936. For every B>=9 define L=CB, delta=B/(L+1)^2 and t=1-delta. The density

    rho_B=4t*y*(1+r^2)^(-1/4)+B*y*exp(-x^2/L^2-y^2)          (1)

is smooth and canonical with a=rho_y(0)=B+4t, c=psi_xy(0)=-1 and sigma=M=1. It has exponent p=1/2 and angular far coefficient 4t sin(theta). It also has 0<rho/(ay)<=1, |grad rho|<=a, an outward rescaled field and forward-decreasing rho/(ay). Yet exact transport fails. If h=rho-ay, R=(2X+U).grad rho-rho and ||g||_m^2=int g^2 r^(-2m)dX, then

    ||R||_3/||h||_3 >= B/(B+4)*sqrt(32/(15625*pi)) > 1/100.   (2)

Thus increasing a in this family cannot make that fixed scale-invariant residual ratio vanish.

For every ell>1, D=ell-1, a=4D and beta=D/(2ell), a second family is

    rho=a*y*f_beta(r),  f_beta(r)=(1-exp(-1/r^2))^beta,
    f_beta(0)=1.                                          (3)

It has c=-D, sigma=M=D, |grad rho|<=a, positive q=rho/(ay)<=1 and exponent p=1/ell. The nonzero defect h is flat at the origin. Exact transport fails. This separates flat Taylor compatibility from the full transport equation used in the flat exclusion.

Dependencies: the canonical radial inverse below, elementary Fourier and heat integrals, and elementary calculus. The exclusion of the radial exact subclass is proved directly below and does not depend on a cap theorem. Source claims audited: lead referee/scap2/PROOF.md Sections6-8 and referee/scap3/PROOF.md Section4. The arguments and checker here are independently implemented.

## Radial inverse and a quantitative base cap

For rho=a*y*f(r), set H(r)=int_0^1 u^3 f(ur)du and psi=-a*xy*H(r). Then rH'+4H=f and rH''+5H'=f', proving -Delta psi=rho_x. Differentiation gives

    U_1=a*x*(H+y^2 H'/r),  U_2=-a*y*(H+x^2 H'/r),
    X.U/r^2=a*H*cos(2theta).

If K=2f+rf' and Q=rf'-6f+24H, the strain entries are

    S_11=a*(K-Q*cos(4theta))/8,
    S_12=-a*Q*sin(4theta)/8, S_22=-S_11.

Therefore max_theta||S||_op=|a|(|K|+|Q|)/8. These identities extend to r=0 by smoothness. For f=(1+r^2)^(-1/4), a=4, convexity of P(z)=(1+z)^(-1/4), with its tangent at r^2 and its chord from0 to r^2, gives

    H>=f/4-rf'/24,   H<=1/12+f/6.

One can verify the constants by substituting u^2=v in the defining integral: H=(1/2)int_0^1 vP(r^2 v)dv. Thus Q>=0 and K>0, and

    max_theta||S_b||=12H-2f+rf'
       <=1+rf'=1-r^2/[2(1+r^2)^(5/4)].                    (4)

For r<=64 the deficit in (4) is at least c_* r^2, since 4097^(1/4)<9. For r>=64, H<=r^(-1/2)int_0^1 u^(5/2)du=(2/7)r^(-1/2), so the exact expression in (4) is at most12H<=3/7. Combining both regions gives

    ||S_b(X)||<=1-c_*min(r^2,1).                           (5)

## Gaussian inverse and global perturbation estimates

With Fourier convention fhat=int exp(-iX.xi)f(X)dX, the Gaussian summand has

    rhohat_g=-i*B*pi*L*xi_y*exp(-(L^2 xi_x^2+xi_y^2)/4)/2,
    Uhat=(xi_x xi_y,-xi_x^2)*rhohat_g/|xi|^2.

The Fourier norm of the two-component strain vector (S_11,S_12) is exactly B*pi*L*|xi_x xi_y|exp(-(L^2 xi_x^2+xi_y^2)/4)/4. Inversion with factor(2pi)^(-2), and the one-dimensional moments int|z|exp(-L^2z^2/4)dz=4/L^2, int|z|^3 exp(-L^2z^2/4)dz=16/L^4, prove

    ||S_g||_infinity<=B/(pi L),
    ||S_g(X)-S_g(0)||<=2B*(1+L^-2)*r^2/(pi L)<=4B*r^2/L.    (6)

The difference bound uses the evenness under X->-X, so the inverse has cos(X.xi), and |1-cos z|<=z^2/2. It is a bound on the vector norm, not on the entries separately.

Writing alpha=L^-2, a separately explicit heat inverse is

    psi_g=-2B*alpha*xy*int_0^infinity
      exp[-alpha*x^2/(1+4alpha*s)-y^2/(1+4s)]
      /[(1+4alpha*s)^(3/2)(1+4s)^(3/2)] ds.                (7)

Integrating the heat equation proves the Poisson law, with no boundary term at s=infinity. At the origin use

    int_0^infinity [(1+4alpha*s)(1+4beta*s)]^(-3/2)ds
      =1/[2(sqrt(alpha)+sqrt(beta))^2].                    (8)

For unequal parameters, differentiating (2s+u+v)/sqrt((s+u)(s+v)) and evaluating the endpoints proves the equivalent integral with shifted factors. For equal parameters direct integration gives the same limit. Formula(8) with beta=1 gives c_g=-B/(L+1)^2=-delta. Parity gives S_g(0)=delta*diag(1,-1). Combining its size with the first part of (6) bounds the difference globally by2B/L. Hence

    ||S_g(X)-delta*diag(1,-1)||<=4B*min(r^2,1)/L.           (9)

The base strain is multiplied by t. Since t+delta=1, t>1/2 and4B/L=c_*/4, (5),(9) give

    ||tS_b+S_g||<=1-(t*c_*-c_*/4)min(r^2,1)
                  <=1-(c_*/4)min(r^2,1).                (10)

Equality occurs at zero, where the strain is diag(1,-1). Thus sigma=1. Since U(0)=0, integration of X.S(sX).X along a radial segment gives X.U>=-r^2, so M<=1. Approach zero along the vertical axis to obtain M>=1.

The inverse (7) is canonical. For each derivative order q, its differentiated integrand is bounded by C_q(1+s)^(-2-q/2)exp[-c_L r^2/(1+s)]. This follows by absorbing each differentiated polynomial factor into a weaker Gaussian; the widths are comparable to(1+s)^(-1) with constants depending on L. Substitution u=r^2/(1+s) gives D^q psi_g=O(r^(-2-q)), hence D^j U_g=O(r^(-3-j)). The radial base has D^j rho,D^j U=O(r^(1/2-j)). Thus all required growth and derivative statements follow. Uniqueness of the sublinear inverse follows from the differentiated mean-value estimate for the entire harmonic difference: its gradient is bounded by C R^-1 sup_(B_R)|U|=o(1), and parity removes the resulting constant vector. The Gaussian is Schwartz, not compactly supported.

## Additional conditions and the fixed weighted gap

Both terms in q=[4t(1+r^2)^(-1/4)+B exp(-x^2/L^2-y^2)]/a are positive and at most their center values. They decrease in each positive coordinate. The cap and coordinate parities imply1<=W_1/x,W_2/y<=3 by integrating S_11 or S_22 along the appropriate coordinate line. Hence W is outward, backward orbits tend to zero and W.grad q<=0.

For the base, the derivative of X->Xf(r) has eigenvalues f and f+rf', both between0 and1. For the Gaussian, put Z=(x/L,y); the derivative of Z->Zexp(-|Z|^2) has eigenvalues exp(-|Z|^2) and(1-2|Z|^2)exp(-|Z|^2), whose absolute values are at most1. The input linear map diag(1/L,1) contracts. Taking the row for the vertical component and adding the two contributions gives |grad rho|<=4t+B=a.

On E_+={|x|<=1,1<=y<=6/5}, let v=1+r^2. Then2<=v<7/2, y^2>=1 and2^(-1/4)<6/7, so

    d_y[4t*y*v^(-1/4)]<4*(6/7)*(1-1/7)=144/49<3.

For z in[1,3/2], (2z-1)exp(-z) is increasing. Therefore the Gaussian y derivative is at most -B exp(-1-1/L^2)<-B/3. To certify the latter, use e<11/4 and exp(1/L^2)<=16/15 for L>=4, whose product is44/15<3. Thus rho_y<0 on E_+. Also x*rho_x<=0 and W_1 has the sign of x, while W_2>0. Consequently W.grad rho<0 and R< -rho on E_+.

On that same rectangle rho>B/5: y>=1, y^2<=3/2, x^2/L^2<=1/16, and exp(3/2+1/16)<5, as follows by squaring and using (11/4)^3(16/15)^2<25. Reflect E_+ in y to give area4/5 with |R|>B/5 and r^2<5/2. Hence

    ||R||_3^2>= (B^2/25)*(8/125)*(4/5)=32B^2/15625.         (11)

The inequalities 1-exp(-s)<=min(s,1) and1-(1+s)^(-1/4)<=min(s/4,1), with L>=1 and t<1, give |h|<=(B+4)|y|min(r^2,1). Polar integration yields

    ||h||_3^2<=pi(B+4)^2*int_0^infinity min(r^4,1)r^-3 dr
                 =pi(B+4)^2.                             (12)

Equations(11),(12) prove (2). The strict1/100 bound follows already from B/(B+4)>=9/13 and pi<22/7. Elementary certificates suffice: e<65/24+1/100<11/4 by bounding the exponential series tail, and int_0^1 x^4(1-x)^4/(1+x^2)dx=22/7-pi>0. The origin center defect is exactly zero, so here the corrected residual F of result62 equals R. Both norms have the same dilation law and their ratio is scale invariant.

## The flat capped family

First consider f_1=1-exp(-1/r^2). Set z=r^-2, g=exp(-z), H_g=int_0^1 u^3 exp(-z/u^2)du and H_(f1)=1/4-H_g. Direct differentiation gives

    K=2[1-(1+z)exp(-z)]>=0,
    K-Q=2-8g+24H_g<=2,
    K+Q=2+4(1-z)g-24H_g<=2.                              (13)

The first upper bound uses H_g<=g/4. For z>=1 the second is immediate; for0<z<=1,

    H_g/g>=int_0^1 u^3[1-z(u^-2-1)]du=(1-z)/4
             >=(1-z)/6.

Since K>=0, max(K+Q,K-Q)=|K|+|Q|<=2. Thus the radial strain is bounded by a/4 and attains that value at zero.

For0<beta<1, the binomial identity

    (1-z)^beta=sum_(j>=1) c_j(1-z^j),
    c_j=(-1)^(j+1)binom(beta,j)>0, sum c_j=1               (14)

expresses f_beta as a convex combination of spatial dilates f_1(r/sqrt(j)). The sum of coefficients follows from the positive power series for1-(1-z)^beta and monotone convergence as z increases to1. The radial inverse commutes with the sum by positivity. Derivatives converge on compact sets; for sets containing zero, factors j^q r^-k exp(-j/r^2) are bounded by a constant times r^-k exp(-1/(2r^2)), after summation, so the remainders are flat as well. Linearity of strain and convexity of its norm prove sigma<=a/4=D; equality and M=D follow at zero as above.

For f_1 the radial map derivative has eigenvalues f_1 and1-(1+2z)exp(-z). The latter has absolute value at most1 since(1+2z)exp(-z)<=2exp(-1/2)<2. The same convex combination gives |grad rho|<=a. The function f_beta is positive, at most1 and decreasing. At infinity f_beta=r^(-2beta)(1+O(r^-2)) with differentiated expansions. The radial inverse has the corresponding bounds, so p=1-2beta=1/ell and Theta_0=a sin(theta). It is canonical by the sublinear uniqueness argument. Near zero its nonconstant defect and its stream correction are flat.

Finally an exact smooth radial density of this form is impossible in the primary class. Inserting the radial inverse into the transport equation, the coefficient of cos^2(theta) must vanish. It is a*r*(2Hf'-H'f). Where f>0 this gives H/f^2 constant; its value at zero is1/4. Thus H=f^2/4. Combining with rH'+4H=f gives rf'=2(1-f), whose solutions are f=1+C/r^2. Smoothness at zero makes C=0. Uniqueness of this regular ordinary differential equation away from zero extends f=1 throughout its positive interval, which cannot end at a finite radius because f remains1. Hence f=1 everywhere, contradicting sublinear growth. This proves failure of transport for(3), even though transport holds to every Taylor order at zero. The Gaussian failure was already explicit on E_+.

No bound above on the origin slope follows from the elliptic law, center relation, global cap, gradient bound and monotonicity of q alone. The full transport equation remains indispensable.
