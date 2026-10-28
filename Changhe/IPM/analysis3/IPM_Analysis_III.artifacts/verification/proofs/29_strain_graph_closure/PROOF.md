# Central strain is not closable in the radial fixed-operator graph

Status: proved for the exact hypotheses below. This is a domain obstruction
for the proposed radial Hilbert route, not a refutation of its fixed-operator
Fredholm theorem.

## Statement and notation

Write P for functions even in x and odd in y. For a smooth compact function
h in P supported away from0 define its central strain by the ordinary integral

 c[h]=(1/pi) integral_R2 h(X) sin(3 theta)/r cubed dX.

This agrees with partial_y U2[h](0) in the IPM convention
U[h]=(S12 h,-S11 h), Sij having multiplier xi_i xi_j/|xi| squared. Since h
vanishes near0, there is no local derivative term in this formula. Its
cubic origin coefficient J[h] is zero.

Let w be a positive radial weight, bounded above and below on compact
annuli, and comparable to r^eta near0, with eta>=-4. Assume V is locally
C1, has the IPM parity, and for some real matrix B and delta>0 satisfies

 V(X)=BX+O(r^(1+delta)) as r->0.

Let rho have the usual even-x, odd-y parity and satisfy |grad rho(X)|<=Cr
squared near0. Assume also

 integral_{r>=r0} w(X)|grad rho(X)| squared r^-6 dX < infinity

for a sufficiently small fixed r0>0. Define on smooth compact parity inputs
supported away from0

 Lfix h=V.grad h-h+U[h].grad rho.

Equip this core with the norm ||h||_{L2(w)}+||Lfix h||_{L2(w)}. Then there
exists a sequence h_n in this core such that

 J[h_n]=0, c[h_n]=1, ||h_n||_{L2(w)}+||Lfix h_n||_{L2(w)} ->0.

In particular c is not a closable scalar functional with respect to this
graph norm. Its kernel is dense in that core graph topology. If the core
is dense in a closed realization of Lfix, the kernel is dense there also.
The same sequence disproves closability of c as a scalar operator whose
base norm is only L2(w).

For the piecewise affine weight of proof 28, eta=1/4 and the far exponent
is -5/4. A sublinear IPM profile with grad rho=O(r^(k-1)) satisfies the
far integrability assumption for every k<29/8, hence for the current
0<k<1 profile. Thus the obstruction applies to that proposed weight.

## A normalized annular packet and its exact scaling

Choose a nonnegative, nonzero smooth radial cutoff chi supported in(1,2).
Set H0(X)=x squared y chi(r). Angular integration gives

 c[H0]=(1/4) integral_1^2 r chi(r) dr >0.

Normalize H=H0/c[H0]. Then H is smooth, compact, in P, and c[H]=1. For
0<epsilon<r0/4 set

 h_epsilon(X)=epsilon H(X/epsilon).

Its support lies in epsilon<r<2epsilon, so J[h_epsilon]=0 exactly. Changing
variables in the strain integral gives c[h_epsilon]=1 exactly: the factors
are epsilon from h, epsilon^-3 from the kernel, and epsilon squared from
area.

The multiplier U is homogeneous of degree0, so

 U[h_epsilon](X)=epsilon U[H](X/epsilon).

The field U[H] is smooth near0 and vanishes at0 by parity. It is bounded
globally. At infinity it is O(|X|^-3): H has zero integral by oddness in y,
and subtracting the zeroth-order kernel from the convolution leaves a
first kernel derivative, O(|X|^-3), against a compact first moment. Therefore

 |U[h_epsilon](X)| <= C r                 (r<=epsilon),
 |U[h_epsilon](X)| <= C epsilon^4 r^-3    (r>=epsilon).

Constants can be enlarged to cover the intermediate annulus. This estimate
uses the actual nonlocal velocity, not an independently prescribed field.

## The case eta>-4

On the packet's annulus,

 ||h_epsilon||_{L2(w)}+||(BX.grad-1)h_epsilon||_{L2(w)}
     <= C epsilon^(2+eta/2).

Indeed the amplitudes of both functions are O(epsilon), and weighted area
is O(epsilon^(eta+2)). The nonlinear part of V contributes at most
C epsilon^(2+delta+eta/2), since grad h_epsilon has bounded amplitude.
These quantities tend to zero for eta>-4.

For the nonlocal coupling on r<=epsilon, the amplitude bound is Cr cubed.
Its squared norm is at most C epsilon^(eta+8), finite for eta>=-4. On
epsilon<r<r0 the amplitude is at most C epsilon^4/r, so its squared norm
is at most

 C epsilon^8 integral_epsilon^r0 r^(eta-1) dr.

For eta>0 this is O(epsilon^8), for eta=0 it is
O(epsilon^8 |log epsilon|), and for -4<=eta<0 it is
O(epsilon^(eta+8)). All tend to zero. On r>=r0 the assumed far integral
bounds the squared norm by C epsilon^8. This proves the required graph
convergence for any epsilon_n->0 when eta>-4.

The far integrability computation for the proposed weight is explicit:
the radial integrand is O(r^(-5/4+2(k-1)-6+1))=O(r^(2k-33/4)), which is
integrable at infinity if 2k-33/4<-1, equivalently k<29/8.

## The endpoint eta=-4

Take epsilon_j=epsilon_* 4^-j with 2epsilon_*<r0. The packet supports are
disjoint. Define the finite smooth sum

 h_n=(1/n) sum_{j=1}^n h_{epsilon_j}.

Then c[h_n]=1 and J[h_n]=0. At eta=-4 the individual L2(w) norms of both
h_epsilon and (BX.grad-1)h_epsilon are uniformly bounded. Disjointness
gives a norm at most C/sqrt(n) for their averages. The transport error is
at most (C/n) sum_j epsilon_j^delta, which tends to zero. The coupling
norm of one packet is at most C epsilon_j squared by the bounds above;
its averaged norm is at most (C/n) sum_j epsilon_j squared, also tending
to zero. This proves the endpoint assertion.

## Closedness consequences

A scalar operator is closable only if every sequence converging to zero
in its base space whose scalar images converge has scalar limit zero.
Here the base space can be the fixed-operator graph completion and the
scalar images are constantly1. Thus c is not closable. For any fixed core
input f, the inputs f-c[f]h_n have zero strain and converge to f in graph
norm. Hence the zero-strain core is graph dense.

For contrast, the elementary Cauchy-Schwarz estimate for this integral
near0 requires

 integral_0^{r0} r^-6 w(r)^-1 r dr < infinity,

which for w comparable to r^eta holds exactly when eta<-4. This is the
sharp threshold for boundedness on L2(w) of the local strain integral on
this parity core. Necessity for eta>=-4 has just been proved, including
the borderline. At infinity, a pure weight exponent nu gives the analogous
condition nu>-4. These statements concern the integral on inputs vanishing
near0; for more general regular inputs the local derivative correction in
the strain formula must also be included. A cubic jet belongs to L2(w)
near0 if eta>-8, so -8<eta<-4 is a possible stronger origin window. It
lies outside the |mu'|<2 class used by proof 28.

## The full normalized operator and tail compensation

Let G=X.grad rho be nonzero. On the same core the full normalized expression
is

 Lh=Lfix h+(c[h]/3)G.

If G belongs to L2(w), this operator is not closable from L2(w) to L2(w),
because h_n->0 and Lh_n->G/3!=0. If G does not belong to L2(w), let the
target be the algebraic direct sum Y=L2(w) direct-sum span{G}, with norm
||f+aG||_Y=||f||_{L2(w)}+|a|. The same sequence proves that L is not closable
from L2(w) to Y. This direct-sum statement needs no distributional
interpretation of arbitrary elements of L2(w); on the current radial
weight they are also locally integrable, so the usual interpretation is
available.

When a nonzero homogeneous tail r^k Theta is present in rho, G has leading
term k r^k Theta and is not in the proposed radial L2 space. Requiring
Lh to lie in L2(w) then forces c[h]=0 on the compact core. Closing that
restriction in the Lfix graph loses the scalar condition, since its kernel
is graph dense. The closure is the fixed operator, not an enforcement of
the classical central-strain normalization.

A sole extra tail coordinate does not repair that graph topology. More
precisely, let d=lambda c[h0] be the imposed compensation relation with a
fixed nonzero lambda, for example

 lambda=-k/(3ell+k c[KP])

when its denominator is nonzero. In D(Lfix) direct-sum R, the constrained
pairs (h_n,lambda) converge to (0,lambda), which violates d=lambda c[0]=0.
Thus this constrained subspace is not closed in the product of the
fixed-operator graph topology and the scalar topology. This statement
requires h0 in the physical scalar domain on the initial core only and
does not assume c has a continuous extension.

Adding c itself to an abstract graph norm produces a completion containing
an independent strain-defect coordinate: the sequence above converges in
that augmented norm to a nonzero defect with zero density. It is not a
closed operator domain embedded injectively into the original density
space. A valid formulation can use stronger origin control, or deliberately
introduce such an independent coordinate with additional equations. It
must specify that choice rather than infer physical closedness from the
fixed-operator Fredholm theorem.

## Dependencies and scope

The IPM multiplier convention and strain formula are independently derived
in proof 01. The present proof uses only the explicit annular packet,
scaling, parity, elementary kernel decay, and the stated coefficient
hypotheses. It does not invalidate the explicit jet-plus-remainder space
in proof 20, whose stronger origin norm does control strain. It does not
assert that no suitable closed full-operator realization exists.
