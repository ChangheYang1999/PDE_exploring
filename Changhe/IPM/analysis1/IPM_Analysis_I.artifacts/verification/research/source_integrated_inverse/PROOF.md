# Integrated cutoff norms and the dilated auxiliary inverse

## Statement and imported exact trial data

Let rho,V be the exact normalized modal_v2 density and canonical rescaled
velocity, P its certified positive source, D=DV(P)=diag(A,mu), and
g=rho_y(P). Topics84,85,89,95 give on B_(3delta)(P), delta=33/2000,

 V(P)=0, grad rho(P)=(0,g),
 10<=A<=51/5, 99/100<=mu<=101/100, 29<=g<=30,
 ||D^2 V||F<M_V=743/2500, ||D^2 rho||F<M_rho=5059/10000,
 ||D^3 U||F<6376, ||D^4 U||F<87933,
 ||D^3 rho||F<505, ||D^4 rho||F<24381, ||D^5 rho||F<3758450.

The norms are pointwise suprema on the whole disc. These are imported
certificates, not new evaluations or a second canonical integration.
The trial density is C6 and V is at least C4 on the disc, including all
seven original spline joins, as proved in topic89 and used in topic95.
Higher derivatives of V here equal those of U since V=c_l X+U.
Use exactly the compact C4 cutoff theta of topic95 and define

 w=theta[V-D(X-P)], q=theta[grad rho-(0,g)],
 A_s u=(D(X-P)+w).grad u-u-gM u+q.U[u],
 Mhat=xi_1^2/|xi|^2, Uhat=(xi_1 xi_2,-xi_1^2)/|xi|^2.

For every fixed s in[61/20,31/10] this auxiliary operator, on its
maximal Hs distributional transport domain, has the inverse asserted
by topics78,92,95. We obtain a sharper bound for this same operator
using exact radial integrals of theta and isotropic dilation (topic96).
The physical rank-one strain is absent. This does not give an inverse
for the full IPM linearization or any nonlinear conclusion.

Use the unitary Fourier transform in dimension2 and Hs defined by
J^s=(1-Delta)^(s/2). For0<ell<=1 put

 N_(1/ell)(u)^2=integral(ell^(-2)+|xi|^2)^s|uhat|^2,
 w_ell(Y)=w(P+ell Y)/ell, q_ell(Y)=q(P+ell Y).

The finite calculation below supplies upper bounds R^*(s,ell).
Define the exact rational lower bounds

 kappa(s)=1301/200-(101/100)s,
 a^*(s)=kappa(s)-delta[(12s+9/2)M_V+3M_rho]>0,
 d^*(s)=(101s-1)/100>0.

Then

 ||A_s^(-1)||_(N_(1/ell)->N_(1/ell))
   <=[1+R^*(s,ell)/d^*(s)]^s/a^*(s)=:B_N(s,ell),
 ||A_s^(-1)||_(Hs->Hs)<=ell^(-s)B_N(s,ell)=:B_H(s,ell).   (1)

Each certified scale yields a valid bound. The best of the computed
scales is not asserted to be the global optimal scale. The previous
coarse bound in topic95 remains valid independently.

## 1. Exact cutoff polynomials and regularity

Let a=273/64, v=|Y|^2, tau=(v-4)/a. Write theta(P+delta Y)=Q(v).
Define T(t)=7t^5-14t^6+10t^7-(5/2)t^8. The exact piecewise formula is

 Q(v)=1,                         0<=v<=4,
 Q(v)=1-T(4tau)/3,                0<=tau<=1/4,
 Q(v)=7/6-(4/3)tau,               1/4<=tau<=3/4,
 Q(v)=T(4(1-tau))/3,              3/4<=tau<=1,
 Q(v)=0,                         v>=4+a=529/64.

Indeed T'=S with S(t)=35t^4-84t^5+70t^6-20t^7 and T(1)=1/2.
Differentiating recovers the b and chi of topic95 exactly. The value
and derivatives through order4 agree at every piece boundary because
S has vanishing first three derivatives at0,1. The fourth derivative
of chi is proportional to S''', also zero at the outer joins. Thus
Q(|Y|^2) is C4 on R^2 and compactly supported in radius23/8. It is
constant near zero. There is no distributional boundary term in its
first four weak derivatives. It satisfies the unchanged gradient bound
delta||grad theta||infinity<=1472/819<2. Therefore the earlier a^*,d^*
remain valid for the same operator and every dilation.

## 2. Radial derivative tensor identities

Primes below mean derivatives in v. At Y=(r,0), v=r^2, direct Cartesian
differentiation gives the nonzero ordered tensor components:

 order1: x=2rQ';
 order2: xx=2Q'+4vQ'', yy=2Q';
 order3: xxx=r(12Q''+8vQ'''), xyy=4rQ'';
 order4: xxxx=12Q''+48vQ'''+16v^2Q'''',
         xxyy=4Q''+8vQ''', yyyy=12Q''.

Mixed derivative labels include all their permutations. Odd numbers
of y derivatives vanish at y=0. The Frobenius norm of an ordered
Cartesian derivative tensor is invariant under an orthogonal change of
coordinates. Since Q(|Y|^2) is radial, its squared norm is the following
polynomial K_j(v) on each piece:

 K_0=Q^2,
 K_1=4v(Q')^2,
 K_2=(2Q'+4vQ'')^2+(2Q')^2,
 K_3=v[(12Q''+8vQ''')^2+3(4Q'')^2],
 K_4=(12Q''+48vQ'''+16v^2Q'''')^2
       +6(4Q''+8vQ''')^2+(12Q'')^2.                      (2)

These sums of squares are pointwise nonnegative. Let0<=j<=4,0<=d<=2.
The rational number

 C_(j,d)=integral_0^(529/64) v^d K_j(v)dv                 (3)

is computed exactly by piecewise polynomial integration. Polar
coordinates, r dr=dv/2 and angular measure2pi, prove

 integral_R2 |X-P|^(2d)||D_X^j theta(X)||F^2 dX
       =pi delta^(2+2d-2j) C_(j,d).                     (4)

For j=0 the tensor is the scalar cutoff. Formula(4) includes the inner
disc v<=4, not just the transition rings.

A separate reconstruction expands each exact polynomial
Q(v)=sum_n c_n v^n into sum_n c_n(x^2+y^2)^n. At y=0, the derivative
partial_x^u partial_y^b with u+b=j vanishes for odd b. For even b the
term with index n>=b/2 contributes

 c_n binom(n,b/2) b! (2n-b)!/(2n-j)! r^(2n-j),            (5)

provided2n>=j; otherwise it contributes zero. Squaring these derivative
polynomials and summing binom(j,b) copies reconstructs K_j, without
using the list(2). Its powers of r are even after multiplication, so
it is a polynomial in v. Equality of every rational coefficient of
this reconstructed K_j with(2) is checked before integration. A second
integration converts v^d K_j to Bernstein coefficients on each exact
piece[a,b]; its integral is(b-a) times the mean of those coefficients.
This verifies(3) by a different exact basis and integration algorithm.
The Bernstein coefficients need not themselves be nonnegative.

## 3. Weighted product estimates without cutoff suprema

Set v0(X)=V(X)-D(X-P) and q0(X)=grad rho(X)-(0,g). Taylor's integral
formula at P and the imported derivative ceilings imply

 ||D^k v0(X)||F<=beta^v_k |X-P|^(d^v_k),
 (beta^v_k,d^v_k)=(M_V/2,2),(M_V,1),(M_V,0),(6376,0),(87933,0),

 ||D^k q0(X)||F<=beta^q_k |X-P|^(d^q_k),
 (beta^q_k,d^q_k)=(M_rho,1),(M_rho,0),(505,0),(24381,0),(3758450,0),

for k=0,...,4. Bounds are applied only in B_(3delta)(P), which contains
the support of theta. At k=0 these are vector norms. At other orders
they include every output component and every ordered input index.

The ordered tensor product rule, invariance under permutations of
indices, pointwise Frobenius Cauchy-Schwarz and L2 Minkowski give

 ||D^j(theta f0)||_(L2,F)
 <=sum_(k=0)^j binom(j,k) beta^f_k
     [pi delta^(2+2d^f_k-2(j-k)) C_(j-k,d^f_k)]^(1/2)
 =:L^f_j,                    0<=j<=4, f=v or q.          (6)

Every factor under the square root is nonnegative and exactly defined.
The support is strictly inside the disc where the coefficient bounds
hold. The product extends by zero as C4, so its weak derivatives in(6)
are precisely the ordinary piecewise derivatives. This avoids the much
larger bound obtained by multiplying a derivative supremum by the area.
It does not assume independence of the coefficients or drop cross terms:
Minkowski replaces the entire product derivative by a sum of L2 norms.

## 4. Scaled H3,H4 and fractional norms

For m=3,4, expansion of the integer Fourier weight and Parseval give

 ||w_ell||Hm <=ell^(-2)
       [sum_(j=0)^m binom(m,j)ell^(2j)(L^v_j)^2]^(1/2)=:W_m(ell),
 ||q_ell||Hm <=ell^(-1)
       [sum_(j=0)^m binom(m,j)ell^(2j)(L^q_j)^2]^(1/2)=:Q_m(ell). (7)

Here the exponent ell^(-2) for w includes both the spatial L2 scale
ell^(-1) and its extra coefficient amplitude ell^(-1). For q only
spatial scaling occurs. The same norm is summed over all components.
Fourier Holder interpolation, applied before substituting upper bounds,
yields for3<=s<=4

 ||w_ell||Hs<=W_3^(4-s)W_4^(s-3)=:W_s^*,
 ||q_ell||Hs<=Q_3^(4-s)Q_4^(s-3)=:Q_s^*.                  (8)

The constructed positive upper bounds satisfy W4>=W3 and Q4>=Q3,
since binom(4,j)>=binom(3,j) and the extra fourth term is nonnegative.
Thus both interpolants in(8) increase with s. This fact will be used
for a uniform interval bound; evaluating three orders alone would not
justify a bound for every real s between them.

## 5. Wiener constants and a fully specified R bound

For the unitary Fourier transform define
W_r(f)=(2pi)^(-1) integral<xi>^r |fhat|, as in topics78,92.
Cauchy-Schwarz and integral_R2<xi>^(-4)=pi imply

 W_2(f)<=alpha_2||f||H4,
 W_1(f)<=alpha_2||f||H3,
 alpha_r=1/[2sqrt(pi(r-1))].

Summing two component norms costs at most sqrt2 times the vector norm.
With beta_r=1/[2sqrt(pi(r-1)(r-2))], a valid explicit bound is

 R^*(s,ell)=sqrt2 s(s-1)2^(s-4)
       [alpha_2 W_4(ell)+beta_(s-1) W_s^*(ell)]
   +sqrt2 s2^(s-2)
       [alpha_2 Q_3(ell)+alpha_(s-1) Q_s^*(ell)].          (9)

It bounds exactly the R_s(w_ell,q_ell) in the auxiliary theorem.
There is no estimate of the physical scalar strain in(9). The E_s,d_s
are unchanged under this dilation by topic96. Substituting(9) and the
rational margin bounds in the theorem proves(1).

For a whole-order-interval bound at a fixed scale let s_-=61/20,
s_+=31/10. In(9) replace the positive increasing prefactors
s(s-1)2^(s-4),s2^(s-2) by their s_+ values, beta_(s-1) and alpha_(s-1)
by their s_- values, and W_s^*,Q_s^* by their s_+ values. This yields
R_bar(ell)>=R^*(s,ell) for every s in the interval. Since a^* decreases
and d^* increases with s, a common bound is

 B_N,bar(ell)=[1+R_bar(ell)/d^*(s_-)]^(s_+)/a^*(s_+),
 B_H,bar(ell)=ell^(-s_+) B_N,bar(ell).                    (10)

The base is at least1. Formula(10) proves a uniform statement directly,
without relying on sampled orders or interpolation of computed constants.

## Computational evidence and limitations

Before execution, the exact cutoff formulas, full proof and all imported
ceilings are fixed above. The checker will compare two exact polynomial
reconstructions and integrations for all15 radial moments, then use Arb
and mpmath.iv independently for square roots, fractional interpolation,
Wiener constants and inverse bounds. A separate output audit must check
all current dependencies, coefficient finiteness, directed ceilings and
strict publication inequalities. Any failure remains OPEN until repaired
and rerun. No numerical value is promised by this proof alone.

The result concerns the same compact C4 auxiliary operator as topic95.
It may improve an upper bound without changing the operator or the trial.
It does not compare with the lead's different smooth cutoff, certify a
residual norm, show the physical rank-one denominator nonzero, assemble
the global inverse or establish any decisive IPM endpoint.
