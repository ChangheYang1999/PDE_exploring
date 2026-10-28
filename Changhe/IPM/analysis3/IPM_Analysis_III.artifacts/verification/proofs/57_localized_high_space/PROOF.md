# A high space with natural origin jets and localized source regularity

## Exact setting and statement

Use the fixed low spaces and actual transport V of proof 54. Explicitly,
with r=|X|, t=log r, p=x^2 y,

    R=L2_P(w dX), w=|x|^(-17/2) max(1,r)^(29/4),
    G=L2(exp(-t/2)dt on t<0; exp(27t/4)dt on t>0),
    X0=E B direct-sum R, Y=E G direct-sum R,
    Z=E B direct-sum D(V.grad-1 on R), E beta=p beta(t).

The parity P is even in x and odd in y. The scalar space B, with its fixed
norm, is as in topics38 and44: beta=H z, z(+infinity)=0,

    ||beta||_B^2=|J|^2+||z'||^2_L2(omega)
               +||z-J||^2_L2(omega,t<0)+||z||^2_L2(omega,t>0),
    omega=e^(-t/2) on t<0, omega=e^(2(k+3/8)t) on t>0.

Here J=z(-infinity), H is the fixed positive integrating factor of the
axis transport, H=1+O(r^2) at0 and H comparable to r^(k-3) at infinity,
with the corresponding first derivative bounds. The hypothesis that the
actual axis rate is positive remains in force; no new positivity claim
is made in this result. The transport properties are those proved in
proof 52: V is globally Lipschitz C1, V_i/X_i are bounded, and
|V.grad theta|<=C|cos theta sin theta|.

Fix

    1/4<delta<2, gamma<-3/8, s>2,

and a compact reflection-invariant set K contained in {x!=0}. It can
contain closed neighborhoods of both source points. Fix a smooth cutoff
q(t) with q=0 for t<=0 and q=1 for t>=1. Set

    chi=1-q,
    a_(delta,gamma)(t)=exp(delta t+(gamma-3-delta)t q(t)).

Let H_(delta,gamma) consist of functions

    h=p[j chi(t)+a_(delta,gamma)(t)u(t,theta)],
    j real, u in H7(R x S1), u even under both Cartesian reflections,

with norm squared |j|^2+||u||_H7^2. Let H^s_K be the closed subspace of
H^s(R2) with parity P and distributional support in K. Finally define

    H_high = H_(delta,gamma) + H^s_K,

with the infimum Hilbert sum norm

    ||h||_high = inf_(h=h1+h2)
                  (||h1||^2_H(delta,gamma)+||h2||^2_Hs)^(1/2).    (1)

Then H_high is a Hilbert space continuously and injectively embedded in
Z. Its J is continuous and equals the classical cubic coefficient.
There are finite constants C_B,C_V, depending on the fixed data above,
such that, for every d in X0 and h in H_high,

    ||W[d].grad h||_Y <= C_B ||d||_X0 ||h||_high,                 (2)
    ||D W[h]||_infinity+|c[h]| <= C_V ||h||_high,                (3)
    W[g]=U[g]+c[g]X/3.

The product and velocity are the canonical ones, with no added harmonic
field. No derivative of the low input d is required. In particular one
may choose delta=3/2 and s=31/10. This permits the already verified frozen
source H^(31/10) regularity without requiring H7 there. It does not prove
that the actual variable-coefficient inverse preserves H_high, and it
does not handle a moving leading far tail by itself.

## Why the old exponent should be relaxed

Take h=p r^2 chi_0(r), with chi_0 smooth radial, equal1 near0 and compactly
supported. This is a smooth natural quintic perturbation. In proof 54's
space its J must be zero, so its only possible cofactor representation
has u=1 on an entire left half-cylinder. Therefore u is not L2 and h is
not in that space. This is an exact exclusion, not a numerical effect.

For the present space, u=r^(2-delta) near0, which and all its cylinder
derivatives are square integrable since delta<2. Away from0 the cutoff
is smooth and compact. Thus h belongs to H_(delta,gamma). More generally
this space admits smooth p-factored perturbations whose cofactor is a
constant plus O(r^2), with differentiated bounds. The strict lower bound
delta>1/4 used below is the integrability condition for the pointwise
power envelope; no assertion about the endpoint delta=1/4 is needed.

## Embedding and origin integrals

H7 on the two-dimensional cylinder embeds into bounded C5. For example,
Cauchy-Schwarz in Fourier variables bounds each derivative of order m<=5
by the H7 norm because

    sum_n integral_R (1+xi^2+n^2)^(m-7) dxi < infinity.

Consequently the cofactor b of h in H_(delta,gamma) satisfies, with all
the t and angular derivatives through the orders used here,

    b=j+O(r^delta) near0, b=O(r^(gamma-3)) at infinity.

All constants are bounded linearly by ||h||_H(delta,gamma). On annuli
r~R0, the scaled Cartesian C5 norm of h is bounded by C R0^3 near0 and
C R0^gamma at infinity; the inner correction h-jp has the sharper scale
R0^(3+delta). The representation is unique, since chi/a grows as
exp(-delta t) at the left end and is not L2.

Set A(t)=b(t,pi/2). Evenness gives b_theta(t,pi/2)=0. Thus
b-A and b_t-A' have an extra cos^2(theta), and their theta derivatives
have an extra cos(theta), with sizes O(r^delta) near0 and
O(r^(gamma-3)) at infinity. It follows that h-E A belongs to R: the
angular square integral is 2 B(1/4,3/2), and its squared radial logarithmic
powers are

    exp((2delta-1/2)t) near minus infinity,
    exp((2gamma+3/4)t) near plus infinity.                     (4)

Both are integrable. The same calculation gives A in B, since
A/H-J and (A/H)' have order r^delta near0, and A/H has order r^(gamma-k)
at infinity. For T(h-E A), the angular derivative is multiplied by
V.grad theta=O(cos theta sin theta); the extra lost cos is restored.
All other coefficients are bounded. Thus the same integrals prove the
continuous embedding H_(delta,gamma)->Z. They also prove J=j and the
classical expansion h=p[j+O(r^delta)].

Every h2 in H^s_K belongs to D_R. The weight and V are bounded on the
compact support and the weight is bounded away from zero there. Since
s>2, h2 and its first derivatives are L2. Its transport image is L2 with
the same support, and it has zero jet near the entire vertical axis.
Therefore H^s_K->Z continuously, with J=0.

The sum map from the Hilbert product H_(delta,gamma) direct-sum H^s_K
to Z is continuous, so its kernel is closed. Quotienting by that kernel
proves that (1) defines a Hilbert space on its image, with continuous
injective embedding into Z. The classical cubic coefficient is invariant
under decomposition because the compact component vanishes near0.
This also proves its continuity on the quotient.

## Bilinear bound for the factored component

For d in X0 put T_d(y)=U2[d](0,y), c_d=c[d]. The independently proved
trace estimates of proof 46 give

    |T_d(r)/r-c_d|+|T_d'(r)-c_d| <= C r^2 ||d||_X0, r<=1,
    |T_d(r)/r|+|T_d'(r)| <= C r^(-11/8)||d||_X0, r>=1.          (5)

The axis row of the product, obtained from incompressibility and the
cofactor expansion, is exactly

    Gamma=(A+A')T_d/r-2A T_d'+c_d(A+A'/3)
          =(A'-A)(T_d/r-c_d)-2A(T_d'-T_d/r)+(4/3)c_d A'.        (6)

At0 it is O(r^delta) because delta<2; at infinity it is
O(r^(gamma-3)), including the uncut normalization. Its G integrals are
exactly (4), proving the axis-row bound.

Here are the remainder estimates with their dependence on delta. They
also specify why the change from proof 54 is valid. First use the cutoff
normalization C_h d=[U[d]+chi_0(r)c_d X/3].grad h, chi_0=1 near0 and
compactly supported. For jet inputs d=E beta_d, the explicit two-mode
Green formulas of proof 47 show a linear strain plus an O(r^3) velocity
at0. After subtracting (6), the constant cofactor j cancels exactly; the
remaining density is O(r^(3+delta)) times cos^4(theta) sin(theta).
At infinity it is O(r^(gamma-11/8)) with this angular factor. Its square
logarithmic exponents are 2delta-1/2 and 2gamma-2. This proves its bounded
map into R. All bounds are linear in both input norms.

For the remainder input use the dyadic decomposition of proof 48. On
comparable input and output scales r~R0, the local axis-subtracted strip
estimate and the radial-versus-vertical lift estimate use only the
scaled C5 bound above. Their operator norm is at most

    C min(R0^2,R0^(gamma-1)) ||h||_H(delta,gamma).

The dyadic input bands have bounded overlap. This gives the bounded
near-diagonal map. For smaller separated sources the parity kernel and
axis subtraction give the same square integrals as in proof 54,

    integral_0^1 r^3 dr + integral_1^infinity r^(2gamma-3)dr.

For larger separated sources, expand the velocity as
c_Z(-x,y)+O(r^3|Z|^-5), where |c_Z|<=C|Z|^-3. The leading j p term
cancels on subtracting its exact axis row. The remaining kernel near0
is bounded by

    C cos^4(theta)|sin(theta)|
      [r^(3+delta)|Z|^-3+r^5|Z|^-5] ||h||_H(delta,gamma).       (7)

The square integrals of both source kernels against w(Z)^-1 over |Z|>4r
are bounded uniformly for 0<r<1: at0 the stronger |Z|^-5 kernel has
radial exponent 2a-9=-1/2>-1, and at infinity its decay is integrable;
the |Z|^-3 kernel is easier. The output radial integrals in dr are

    integral_0^1 [r^(2delta-3/2)+r^(5/2)] dr,                 (8)

which converge precisely under the strict envelope condition delta>1/4.
At infinity the same separated-source calculation gives
integral_1^infinity r^(2gamma-3)dr. Thus these pieces are Hilbert-Schmidt,
with bounded norm linear in ||h||_H(delta,gamma). The cutoff strain
remainder itself has the extra cos^2 cofactor and is bounded by (4).
This proves the remainder estimate for C_h.

Finally the omitted full-strain term is (c_d/3)(1-chi_0)X.grad h.
It vanishes near0. Its axis-subtracted cofactor has an extra cos^2, and
at infinity its square logarithmic exponent is 2gamma+3/4<0 in both
rows. Hence it belongs to Y with the required bilinear bound. Together
with (6), this proves (2) for h in H_(delta,gamma).

These estimates initially apply to smooth approximants. The canonical
velocity of d converges in local L2, the trace pairings converge by (5),
and high cofactors converge with the stated local derivative bounds.
Thus the limit is the canonical locally integrable product, and its Y
decomposition is exactly (6). This checks both domain and target.

## The compact source component and the velocity bound

On a fixed compact neighborhood of K, the low-input canonical velocity
has an L2 bound C_K||d||_X0. For the R input, restrict first to a bounded
input neighborhood and use the ordinary L2 multiplier bound with the
locally comparable weight; the separated part is a bounded smooth kernel
pairing against w^-1. For the E B input the explicit radial Green
formulas of proof 47 give a bounded local velocity from the bounded B
cofactor. The strain term is bounded by the already proved strain
functional. Since H^s(R2)->W^(1,infinity) for s>2,

    ||W[d].grad h2||_R <= C_K ||d||_X0 ||h2||_Hs.

The product is supported in K, so it has zero vertical-axis row and is
already in Y. This proves (2) on the second component.

For completeness, if a scalar g is bounded, globally C^alpha and L2,
0<alpha<=1, the same kernel split as in proof 54 gives

    ||U_i[g]||_infinity <= (1/2)||g||_infinity
                    +[g]_Calpha/alpha+||g||_2/(2 sqrt(pi)).  (9)

The small-ball integral is integral_0^1 r^(alpha-1)dr=1/alpha;
the outer kernel has L2 norm at most1/(2 sqrt(pi)). The point-mass term
has magnitude at most1/2. Each g=partial_j h1 is globally Lipschitz,
bounded and L2 by the annular bounds: its second derivatives are bounded
near0 since delta>0, and its far squared radial exponent is 2gamma-1<-1.
For h2 in H^s_K choose 0<alpha<min(1,s-2). Sobolev embedding gives the
bounds in (9) for partial_j h2. Derivatives commute with the canonical
operator by regularization and the convergent far kernel.

If M bounds the right side of (9) for both derivatives, then
||DU||_op<=2M, |c|<=M, and ||DW||_infinity+|c|<=(10/3)M.
This proves (3) on both summands. Taking the infimum over decompositions
in (1), with Cauchy-Schwarz for the two summand constants, proves (2)-(3)
on H_high. It also shows the bounds are independent of decomposition.

## Scope, numerical checks and dependencies

The exact exponents and the old-space counterexample are recorded in
evidence/check.json. There is no numerical inverse or smallness bound.
The choice s=31/10 satisfies the previously certified frozen window
s<2373/680; this comparison is exact. A cutoff supported in K can therefore
carry such source regularity, but transferring the full actual inverse
to this mixed space is still an open analytic step.

Dependencies are the low-space realization and strain continuity of
proof 44, the local strip estimate of proof 23, the trace and jet formulas
of topics46-47, the dyadic decomposition of proof 48, the actual transport
bounds of proof 52, and the exact frozen-source window of proof 10. The
origin and far integrals affected by the new high space are proved above.
