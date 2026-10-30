# The universal velocity obstruction persists in every fixed fractional ball

Status: new analytic result offered for independent review. This complete
argument is written before its finite identity checks. No stationary
solution is constructed or assumed.

## 1. Exact statement

Let -5<q<-3, a=-q, 0<s<2, w1,w2>0, and

 omega(X)=(1+4|X|^2)^(2/5), J=(1-Delta)^(1/2),
 X_(s,w)(h)^2=||omega D2 J^s h||2^2
                 +w1||D J^s h||2^2+w2||J^s h||2^2.

Dk denotes the complete ordered Cartesian derivative tensor. Define the
space as the completion of real compact smooth S1 functions in this
norm, with S1 meaning even in x and odd in y. Let

 H_q(h)=max(sup (1+|X|)^a |h(X)|,
             sup (1+|X|)^(a+1)|grad h(X)|).

Fix any rho>0, beta>0 and R0>0. Use the canonical velocity
U[h]=(psi_xy,-psi_xx), Delta psi=h, the canonical kernel K, the absolute
first moment M[h]=integral X h(X)dX, and c[h]=partial_y U2[h](0).
If E satisfies

 |U[h](X)+DK(X)M[h]|<=E H_q(h)|X|^q, |X|>=R0,                (1)

for every real smooth S1 h in this space with finite H_q and first
absolute moment, c[h]=0, X_(s,w)(h)<=rho and ||h||2<=beta, then

 E>=(a-1)/(2a(a-3)).                                       (2)

This remains true if one also requires H_q(h)=Hstar for any prescribed
Hstar>0. Thus the universal lower constant survives the full fixed
fractional ball, its normalization and any fixed positive weighted
budget. It applies in particular to s=1/5184, w1=32768, w2=1048576 and
rho=1351/1000000. It uses no stationary equation, reference estimates,
or background matrix hypotheses restricted to actual stationary
corrections.

## 2. A weighted Bessel estimate with a stated constant

Put alpha=2-s>0. The multiplier J^(-alpha) is convolution with the
nonnegative Bessel kernel

 G_alpha(Z)=1/Gamma(alpha/2) integral_0^infinity
 t^(alpha/2-1)e^(-t)(4pi t)^(-1)exp(-|Z|^2/(4t))dt.          (3)

Indeed the Fourier transform of the Gaussian factor is exp(-t|xi|^2),
and the Gamma integral gives (1+|xi|^2)^(-alpha/2). Tonelli shows its
mass is1. This derives (3) with the Fourier convention
fhat(xi)=integral f(X)exp(-i X.xi)dX.

The elementary inequality

 1+4|X|^2<=2(1+4|Y|^2)(1+4|X-Y|^2)

gives omega(X)<=2^(2/5)omega(Y)omega(X-Y). A two-dimensional Gaussian
of density (4pi t)^(-1)exp(-r^2/(4t)) has moment
integral r^(4/5)dmu=(4t)^(2/5)Gamma(7/5), by the substitution
u=r^2/(4t). Since (1+x)^(2/5)<=1+x^(2/5) for x>=0, (3) implies

 integral omega(Z)G_alpha(Z)dZ
 <=1+16^(2/5)Gamma(7/5)Gamma(alpha/2+2/5)/Gamma(alpha/2).

Define C_s to be2^(2/5) times this last right side. Weighted Young's
inequality, or Minkowski followed by the displayed weight inequality,
therefore gives

 ||omega J^(-alpha)g||2<=C_s||omega g||2.                   (4)

The unweighted norm is at most||g||2. The same statements hold for a
finite Cartesian tensor, using its Euclidean norm in Minkowski.
For smooth f with the indicated weighted derivatives, use
J^s f=J^(-alpha)(f-Delta f) and commute derivatives. Trace contraction
on the final two tensor indices has norm sqrt(2), so

 ||omega D2 J^s f||2<=C_s(||omega D2 f||2+sqrt(2)||omega D4 f||2),
 ||D J^s f||2<=||Df||2+sqrt(2)||D3f||2,
 ||J^s f||2<=||f||2+sqrt(2)||D2f||2.                        (5)

All operations first hold for compact smooth f and then by the stated
bounds and Fourier limits. These are upper bounds with explicit C_s;
no fractional derivative is replaced by a formal integer derivative.

## 3. Smallness of the normalized sequence

Use the smooth first-sine functions from T4-384:

 f_R=y(R^2+|X|^2)^(-(a+1)/2)/a,
 b=y eta(|X|^2),
 eta(t)=exp(1-1/(1-t)) for0<=t<1, and eta(t)=0 for t>=1,
 k_R=f_R-R^(-a-1)b/a, R>=1.                               (6)

Every derivative of f_1 is smooth and has
Dk f_1=O((1+r)^(-a-k)). Hence all constants

 A_k=||Dk f_1||2 (0<=k<=4),
 B_k=||omega Dk f_1||2 (k=2,4)

are finite. The exact scaling f_R(X)=R^(-a)f_1(X/R) gives

 ||Dk f_R||2=R^(1-a-k)A_k,
 ||omega Dk f_R||2<=R^(1-a-k+4/5)B_k.                      (7)

The second inequality uses omega(RY)<=R^(4/5)omega(Y), R>=1.
Combining (5), (7), and the triangle bound for the three components
of X gives

 X_(s,w)(f_R)<=D_(s,w,a) R^(1-a),                          (8)
 D_(s,w,a)=C_s(B_2+sqrt(2)B_4)
          +sqrt(w1)(A_1+sqrt(2)A_3)
          +sqrt(w2)(A_0+sqrt(2)A_2).

Here all omitted powers of R are at most1: in particular the two
weighted powers after dividing by R^(1-a) are R^(-6/5) and R^(-16/5).
The constants A_k and B_k are defined by the convergent integrals
above, so (8) is an exact finite bound, not an uncomputed existence
hypothesis. The compact b belongs to the space, and therefore

 X_(s,w)(k_R)<=D_(s,w,a)R^(1-a)+R^(-a-1)X_(s,w)(b)/a
                  tends to0.                             (9)

Likewise ||k_R||2<=A_0R^(1-a)+R^(-a-1)||b||2/a tends to0.

For completeness, these noncompact functions belong to the specified
completion. Choose radial smooth cutoffs chi_L equal to1 on r<=L
and0 on r>=2L, with D^j chi_L bounded by constants times L^(-j).
The functions f_R and k_R and their derivatives through order4 are
in weighted L2; for k=0 this follows from a>3>1+4/5. Leibniz's rule
and tail integrability give convergence of chi_L f_R and chi_L k_R
in those integer weighted norms. Equation (5) then gives convergence
in X_(s,w). The cutoffs preserve S1. In fact chi_L k_R has zero first
sine slope at the origin, hence exact c=0 by the identity below,
so membership can also be approximated within the normalized class.

## 4. Normalization, weighted budget and the limiting velocity

For a smooth first sine mode g=F(r)sin(theta), the regular Poisson
solution near the origin has coefficient F'(0)r^3sin(theta)/8.
Thus c[g]=-F'(0)/4. This is the local contact term; the full kernel's
sin(3theta) principal-value integral is zero on centered annuli.
In (6), f_R has slope R^(-a-1)/a and b has slope1, so c[k_R]=0.
All first absolute moments are finite because a>3.

The polar gradient of f_R has radial coefficient
(R^2-a r^2)(R^2+r^2)^(-(a+3)/2)/a and angular coefficient
(R^2+r^2)^(-(a+1)/2)/a. Using the squared sine/cosine combination and
(1+r)/sqrt(R^2+r^2)<=sqrt(1+R^-2) proves

 1<=H_q(k_R)<=(1+R^-2)^((a+1)/2)+R^(-a-1)5*2^(a+1)/a.

The lower bound is the limit of the weighted gradient on the positive
y-axis. Hence H_q(k_R) tends to1.

The canonical mode-one Green formula is

 psi=-sin(theta)/2[r^-1 integral_0^r u^2F(u)du
                                  +r integral_r^infinity F(u)du].

Subtraction of the complete moment and use of
F(r)=r^q/a+O_R(r^(q-2)) show that the nondipole leading potential is
r^(q+2)sin(theta)/(a(q+1)(q+3)). The remainder has two controlled
derivatives; differentiate the two integrals directly. Its Hessian
velocity divided by r^q tends to

 W(theta)=(cos(theta)[1+(q-1)sin(theta)^2],
           -sin(theta)[1+(q-1)cos(theta)^2])/(a(q+3)).

The compact first-sine subtraction in (6) contributes exactly its
dipole outside the unit disk and leaves this limit unchanged.
At theta=pi/4, |W|=(a-1)/(2a(a-3)). By (9), every sufficiently
large R lies in both prescribed balls. Apply (1) to k_R, let the
observation radius tend to infinity, and then let R tend to infinity.
This proves (2).

If H_q must equal a prescribed Hstar>0, replace k_R by
h_R=Hstar k_R/H_q(k_R). The multipliers tend to Hstar, so (9) and
the L2 smallness still hold. The normalized velocity ratio is
unchanged. This proves the last assertion as well.

## 5. Scope and verification

This extends T4-384's class to the full selected fractional ball.
It shows that adding those norm and normalization restrictions cannot
rescue a universal-constant version of the endpoint closure test.
A velocity estimate using the stationary equation or a specific
stationary tail profile is a different question and remains OPEN.
No quantitative finite-R membership number is claimed: (9) gives
the complete limiting argument with stated finite integral constants.
The finite checker verifies the algebraic exponents, heat-kernel
moment and trace contraction fixtures. The analytic argument above,
not those finite fixtures alone, proves the result. Source hashes
are preserved in data/manifest.json. Independent Opus review is
required before this proposal becomes AUDITED.
