# Infinite moment compatibility for a strong axis-weighted graph domain

Date 2026-10-22T02:51:08.584876+00:00. Proof written before the new finite algebra and canonical-application checks. Status OPEN until complete actual Claude Opus5.5 review, independent checks and later own adjudication. This characterizes a test-class restriction of a graph domain; it is not a full inverse theorem.

## Exact hypotheses and result

Let rho satisfy the local background hypotheses of axis_weighted_nonlocal_mapping:

 rho is even-x/odd-y, rho(0,y)=0 near0,
 rho=x^2y+R, |D^j R|<=C r^(5-j), 0<=j<=3.                   (1)

For the sufficiency assertion assume additionally rho and its canonical velocity U[rho] belong locally to C^(4,1/2) on the plane. The exactly joined canonical modal background satisfies this finite regularity by modal_graph_scaling/PROOF.md. Let L_rho be the full PLUS-strain linearization

 L_rho h=(ell X+U[rho]).grad h-h+U[h].grad rho
                                          +(Sigma(h)/3)D rho,
 -Delta psi[h]=partial_x h, U[h]=(-psi_y,psi_x),
 Sigma(h)=psi_xy(0).

The constant ell is arbitrary. Define T as the real vector space of smooth compact densities supported in1<r<2, at positive distance from both axes, even in x and odd in y. Every h in T has a smooth global x^2y factor and J(h)=0. Put T0={h in T:Sigma(h)=0}. Each h in T belongs to every logarithmic Y_(a,s) with finite real a and finite s>=0, where

 ||h||_Y=||exp((1/2-a)z)h(exp(z),y)||_(H^s(R^2)), z=log x.

Write its density sine coefficients F_l(r)=(1/pi)integral h(r,theta)sin(l theta)dtheta. For every even n>=2 define the exact linear functional

 Gamma_n(h)=(1/2)integral_0^infinity r^(-n)F_(n+1)(r)dr.    (2)

Fix any real a>=5/2 and set s=153/50. For h in T0, the following conditions are equivalent:

 (i) (L_rho h)|_(x>0) belongs to Y_(a,s).
 (ii) U_2[h](0,y)=0 for every sufficiently small positive y.
 (iii) Gamma_n(h)=0 for every even n>=2.
 (iv) psi[h] and U[h] are smooth, compactly supported,
      and vanish on neighborhoods of both coordinate axes. (3)

In fact (i) implies(ii) with any s>=0, and(iv) implies(i) for every0<=s<7/2 and every finite a. The stated s lies strictly in this interval.

The common subspace D0 of T0 in(3) is infinite-dimensional and has infinite algebraic codimension in T0. Consequently no finite collection of extra linear constraints on T0 can force all its members to have L_rho h in Y_(a,153/50). This means no finite moment or gauge cancellation suffices to restore mapping of the whole resulting finite-codimension test subspace. It does not imply that every smaller infinite-codimension domain is unusable.

## Necessary axis equation

For small y>0 set b(y)=rho_xx(0,y)/2 and u(y)=U_2[h](0,y). The background assumptions give

 b(y)=y+O(y^3), b'(y)=1+O(y^2), b(y)>0

after restricting to a sufficiently small positive interval. The derivative formula uses rho in C3 and the explicit differentiated remainder in(1). Since h vanishes on r<1 and Sigma(h)=0,

 g:=L_rho h=U[h].grad rho on r<1.

The trace condition and parity give g(0,y)=g_x(0,y)=0, as in the parent proof. The velocity is divergence free, so U_1,x(0,y)=-u'(y). Differentiating g twice in x, using rho_x=rho_y=rho_xy=U_1=U_2,x=0 on the vertical axis, yields exactly

 g_xx(0,y)/2=-2b(y)u'(y)+b'(y)u(y).                        (4)

All these derivatives exist: h is smooth compact and U[h] smooth, while rho is C3. Formula(4) is the coefficient of x^2 in the local image.

If(i) holds and this coefficient is nonzero at any y in the interval, continuity gives a fixed nearby positive y interval and a thin rectangle where, after multiplying by a sign, Taylor's integral formula gives |g(x,y)|>=c x^2. Its weighted square integral dominates integral_0^epsilon x^(4-2a)dx, which diverges for a>=5/2. Therefore the coefficient in(4) vanishes identically. Since b>0,

 (u/sqrt(b))'=0.

Hence u=C sqrt(b) on the interval. But oddness and smoothness of U_2 give u(y)=O(y), while b(y)/y tends to1. Thus u/sqrt(b) tends to0 as y decreases to0, so C=0. This proves(ii). Only the weighted L2 component was needed, so the same necessity holds for every s>=0. No fractional Sobolev embedding is used in this direction.

## Harmonic moments and continuation through the axis gaps

Inside r<1 the canonical stream is harmonic and odd in both coordinates. Its convergent harmonic Taylor series is

 psi[h](r,theta)=sum_(j>=1) Gamma_(2j)(h) r^(2j)sin(2j theta).

The coefficients are precisely(2), by the complete radial Green formula and compact-support integration by parts proved in the parent. All modes are retained. Termwise differentiation is valid on smaller discs. Restricting psi_x to x=0,y>0 gives

 u(y)=sum_(j>=1) (2j)(-1)^(j-1) Gamma_(2j)(h)y^(2j-1).      (5)

Every displayed multiplier is nonzero. Thus(ii) forces all Taylor coefficients, and hence all Gamma_(2j), to vanish. Conversely(iii) makes psi identically zero in r<1 and in particular gives(ii). This proves the equivalence of(ii) and(iii).

To prove(iii) implies(iv), take delta>0 with supp h disjoint from the two strips |x|<delta and |y|<delta. Let Omega be the connected component of R^2\supp h containing0. It contains both strips, their intersection, and the exterior r>2: the exterior is connected and intersects the vertical strip, so all these sets lie in the same component. The stream is harmonic on Omega because partial_x h=0 there. It is zero on the inner disc. Harmonic analyticity forces it to vanish throughout Omega. For completeness, propagation follows by chains of overlapping discs inside this connected open set: a harmonic Taylor series vanishing on an open subdisc has all coefficients zero at an interior point, so the function is zero on the next disc. Equivalently the set of points with a zero neighborhood is open and relatively closed, since all derivatives vanish at a limit point and harmonic Taylor convergence gives a zero neighborhood there.

Therefore psi and all its derivatives vanish on both strips and outside r=2. The stream is globally smooth for compact smooth h; this follows directly from the logarithmic potential with source partial_x h, splitting off a local smooth compact source and using distributional convolution or integration by parts to differentiate it, with the distant kernel smooth. Its support is contained in the compact set {|x|>=delta,|y|>=delta,r<=2}. This proves(iv). Condition(iv) plainly gives(ii). The use of the source-free component is essential: all inner moments alone would not force compact support for an arbitrary annular source whose support blocked every path from the inner disc to the exterior. Here the axis gaps provide those paths.

## Sufficiency in the indicated fractional Sobolev norm

Under(iv), h, all its derivatives and U[h] have compact support away from both axes. Since Sigma=0, every term of L_rho h is supported in a fixed compact set of that kind. The background C^(4,1/2) regularity gives g=L_rho h in C_c^(3,1/2). The logarithmic transformation and its smooth positive multiplier preserve this regularity on that support. It remains to justify H^(153/50) membership.

If f in C_c^(3,1/2)(R^2), then its derivatives through order3 are square integrable. For each derivative v of order3 and 0<t<1/2, its Gagliardo integral is finite:

 integral integral |v(X+Z)-v(X)|^2 / |Z|^(2+2t) dX dZ < infinity.

For |Z|<1, the numerator is at most C|Z|, and the X set where it can be nonzero has uniformly bounded measure because v has compact support. Polar integration in Z gives integral_0^1 r^(-2t)dr, finite when t<1/2. For |Z|>=1, use translation invariance and the bound integral|v(X+Z)-v(X)|^2 dX<=4||v||_2^2, followed by integral_1^infinity r^(-1-2t)dr<infinity.

The connection with the Fourier norm can be proved directly by Plancherel and Tonelli: the same double integral equals integral |v_hat(xi)|^2 times integral |exp(i xi.Z)-1|^2 |Z|^(-2-2t)dZ dxi. Rotational invariance and scaling make the inner integral c_t|xi|^(2t), where0<c_t<infinity for0<t<1 (near0 use |exp(i xi.Z)-1|<=|xi.Z|, and at infinity use2). Summing over third derivatives controls |xi|^(6+2t) because the sum of all degree-six derivative monomials is comparable to |xi|^6. Together with L2 this proves f in H^(3+t). Integer lower orders and monotonicity of Fourier weights give every0<=s<7/2. Here t=3/50<1/2, so s=3+3/50=153/50. No critical-endpoint embedding is claimed. This proves(iv) implies(i).

## Infinite codimension and nonempty compatible class

For any N>=1, take the sine frequencies3,5,...,2N+3 and a single reflection-invariant nonnegative smooth angular bump phi, positive on an open arc and supported away from both axes. Their(N+1)-dimensional Gram matrix M with weight phi/pi is positive definite by the trigonometric-polynomial argument in the parent. Choose fixed nonnegative nonzero chi smooth supported in(1,2). The moment map on h=chi phi sum_j c_j sin((2j+3)theta), j=0,...,N, is

 (Gamma2,Gamma4,...,Gamma_(2N+2))^T = D M c,
 D_nn=(1/2)integral r^(-n)chi(r)dr>0

with rows n=2,4,...,2N+2. D and M are invertible finite real matrices. Thus the first coordinate can be prescribed as0 and the remaining N coordinates arbitrarily. Since Sigma=2Gamma2, this proves that Gamma4,...,Gamma_(2N+2) map T0 onto R^N for every N. The simultaneous kernel D0 therefore has algebraic codimension at least N for every N. If a subspace cut out by finitely many extra linear constraints were contained in D0, its finite codimension would bound the codimension of D0, a contradiction. This statement is elementary algebra and does not assume continuity of those extra constraints or a normed completion.

Nevertheless D0 is infinite-dimensional. Choose any nonzero f in T and set h=-Delta f. Then h belongs to T, and psi=partial_x f is the canonical stream: -Delta partial_x f=partial_x h, its parity is odd/odd and its velocity is compact and therefore sublinear. Canonical uniqueness excludes an extra harmonic contribution. Consequently all inner Gamma_n and Sigma vanish, and(iv) holds. Also h is nonzero: if Delta f=0, integration by parts gives integral|grad f|^2=0 and compact support forces f=0. Infinitely many disjoint small reflected bump families inside the annulus give linearly independent such h. The same integration-by-parts argument shows injectivity of -Delta on their finite linear span. Hence a compatible infinite-dimensional domain exists, but the present theorem supplies no bounded inverse on it and no density or closedness assertion in Y.

## Verification and scope

Rehash the accepted axis_weighted_nonlocal_mapping verdict and all its181pins for the canonical application. Independently reconstruct(4), (5), the ODE integrating factor, the exact fractional exponent, the finite moment-map indexing and the compact-Laplacian construction with rational polynomial and independent symbolic paths. These checks carry finite identities only. Harmonic continuation, Gram positivity, the uniform lower bound and the Gagliardo argument are analytical parts of this proof, not inferred from finite samples.

This makes the domain cost of the strong-axis frozen model explicit: even on compact zero-strain test functions, membership of the full image requires infinitely many interior harmonic cancellations. The admissible compatible class is still infinite-dimensional. No full inverse, nonlinear preservation, range characterization, stationary solution, distance to X3, exclusion neighborhood or decisive PDE endpoint is proved. No conclusion about arbitrary noncompact domains or other spaces follows.
