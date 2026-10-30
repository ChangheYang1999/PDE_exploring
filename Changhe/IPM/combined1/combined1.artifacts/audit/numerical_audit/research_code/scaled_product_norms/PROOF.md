# Exact Laurent products for full scaled residual norms

Status: proposed implementation of an exact algebraic reduction. No full
candidate norm is established by this document alone.

## Statement and hypotheses

Let c>1 be rational, delta=1-1/c, t=r^2/(1+r^2), v=1-t,
and w=v^(delta/2). Let chi be a finite exact generator sum from the
family specified in ../joint_scaled_factored_weak/PROOF.md. All scales
R are positive rational numbers with a=R^2-1 in {99,624,2499,9999},
or R=1. Let rho=-partial_y Delta chi, psi=partial_x partial_y chi,
u=(-partial_y psi,partial_x psi), and
F=(cX+u) dot grad rho-rho on R^2. The compact generator formulas are
smooth at the origin. Their exact Cartesian derivatives through order
six exist.

We give a finite exact algorithm for F and its derivatives through
order two, followed by whole-plane norm integrals when the explicitly
tested endpoint exponents are greater than -1. The algorithm claims no
smallness, inverse bound or existence result. Floating quadrature is
not used in its exact algebra or ball integration.

For a component of derivative order d define its representation by

    H_d(r,theta) = R_d(r) sum_(ell,kind,n) w^ell A_(ell,kind,n)(t) T_(kind,n)(theta),
    R_d = r v^(d/2) for even d, and v^((d-1)/2) for odd d.

Here T_c,n=cos(n theta), T_s,n=sin(n theta), n>=0; sin(0 theta)
is omitted. A is a rational polynomial P(t)/D(t), with
D=product_a (1+a(1-t))^N_a and nonnegative integer N_a. Each such
D is strictly positive on [0,1]. Negative modes are folded using cosine
evenness and sine oddness. The exact scaled Cartesian-jet recurrence
from the dependency proof supplies rho and u at d=0 and grad rho at d=1.

## Laurent multiplication with radial coefficient blocks

Consider a cosine field C and sine field S of the above form, with
orders d_C=0 and d_S=1. Group each by ell. Within each group raise every
positive denominator to the componentwise maximum of its powers,
multiplying the numerator by the missing factors. This preserves each
rational function identically and gives polynomial coefficients in t.
Let D_C and D_S be the two common denominators. Let h_C and h_S be
maximum angular frequencies in the respective groups. Write

    Ctilde(z,t)=sum_n P_C,n(t) (z^(h_C+n)+z^(h_C-n)),
    Stilde(z,t)=sum_n P_S,n(t) (z^(h_S+n)-z^(h_S-n)).

With z=exp(i theta), these are 2 z^h_C D_C C_angular and
2 i z^h_S D_S S_angular. The product is antisymmetric about angular
exponent h_C+h_S. If its polynomial coefficient at exponent
h_C+h_S+n is H_n(t), then the sine coefficient of the product is
H_n(t)/(2 D_C D_S). The negative coefficient is -H_n, and the central
coefficient is zero. This also handles n=0 cosine terms, which occur
twice in Ctilde, exactly as the cosine identity requires.

Choose an integer stride strictly greater than the sum of the maximum
radial degrees of the two packed polynomials. Replace each monomial
z^j t^k by Z^(stride*j+k). In a product every radial exponent remains
strictly below stride, so decoding the one-variable product recovers
all bivariate coefficients without a carry between angular blocks.
Only exact rational polynomial multiplication is used. Distinct branch
pairs with the same ell sum, angular center and denominator powers can
be added before decoding. Finally add their decoded rational functions
with exact positive common denominators. This proves the product
algorithm for every finite branch pair, including zero coefficients,
unequal centers, and unequal denominator powers. Its validity does not
depend on a numerical condition number.

For the residual, u_1 is a cosine field and rho_x a sine field; rho_y
is a cosine field and u_2 a sine field. Their radial prefactors multiply
to R_0 because R_0 R_1=R_0. The nonlinear part of F is therefore the
sum of the two Laurent products. For a rho coefficient A with branch
ell, direct differentiation of r w^ell A(t) gives

    r partial_r rho = r w^ell [(1-ell delta t)A+2t(1-t) A'] sin(n theta).

Thus the linear coefficient of F is
c[(1-ell delta t)A+2t(1-t)A']-A. The prime differentiates the full
rational function. This establishes the complete residual identity.

## Cartesian derivatives of the packed residual

For a coefficient A of order d and branch ell, radial differentiation
contributes, after factoring out the target R_(d+1),

    B=(1-(d+ell delta)t)A+2t(1-t)A'   when d is even,
    B=-(d-1+ell delta)A+2(1-t)A'     when d is odd.

The angular contribution has coefficient A for even d and A/t for
odd d, multiplied by the angular derivative of T_kind,n. For odd d,
only n>0 needs this division. Smoothness of the represented field
implies divisibility at t=0 in the actual polynomial identities used
here; the implementation requires exact division and fails if there
is a remainder. For n=0 the angular derivative is zero.

Use partial_x=cos(theta) partial_r-sin(theta) r^-1 partial_theta and
partial_y=sin(theta) partial_r+cos(theta) r^-1 partial_theta, and the
four exact trigonometric product identities. This gives all first and
second Cartesian derivatives. Mixed derivatives must agree exactly.
These formulas follow by differentiating R_d and w, using
r partial_r t=2t(1-t) and r partial_r w=-delta t w. They include the
scale-denominator derivatives through A', so no pole term is omitted.
An independent fixture check will compare this derivative route with
Leibniz differentiation of the defining generator equation through D2F.

## Complete radial norm integrals

At a fixed radius, angular orthogonality makes different trigonometric
modes orthogonal. Each nonzero sine or cosine square integrates to pi
over [0,2pi]; the constant cosine square integrates to 2pi. Expand all
ordered branch pairs with the same mode and trigonometric kind. For
the full ordered d-th derivative tensor, component partial_x^a
partial_y^(d-a) carries multiplicity binomial(d,a). This accounts for
both mixed Hessian entries at d=2.

For each branch sum E combine the entire rational radial coefficient
of this angular square sum exactly. Although individual branch groups
need not be positive, their sum is the squared tensor norm. The radial
Jacobian is r dr=dt/(2v^2). Together with R_d^2, every unweighted
integral has exponent

    b = d-3 + E delta/2 + endpoint_order

and an extra numerator factor t when d is even. For the rF norm,
insert t/v, so increase the numerator t power by one and subtract one
from b. For the P2 norm insert the weight
omega^2=(1+4r^2)^(4/5)=(1+3t)^(4/5) v^(-4/5).

Replace t by 1-v, extract every exact v-zero from each complete
branch-group numerator, and require the resulting b>-1. Apply the
positive-pole exact partial-fraction theorem of
../rational_pole_moments/PROOF.md to each group. It evaluates
int_0^1 v^b P(v)/product_a(1+a v)^N_a dv as an Arb ball, after exact
rational cancellations. This integrability test is sufficient for the
finite sum. If it fails, this algorithm leaves the norm OPEN; it does
not give an integral interpretation to analytic continuation.

For P2 write (1+3t)^(4/5)=(5/2)^(4/5)(1+z)^(4/5), with
z=(3t-3/2)/(5/2) and |z|<=3/5. The degree-56 binomial polynomial W
has uniform absolute error at most

    epsilon=|binomial(4/5,57)| (3/5)^57 /(1-3/5).

Indeed the absolute ratios of all subsequent series coefficients,
after multiplication by |z|, are bounded by 3/5. Multiply the pointwise
bounds W-epsilon <= (1+z)^(4/5) <= W+epsilon by the full nonnegative
squared Hessian density before integration. If S is its unweighted
radial integral including v^(-4/5), and T the integral with W, the
squared P2 interval is

    (pi/2)(5/2)^(4/5) [T-epsilon S, T+epsilon S].

It is legitimate to compute S and T by signed branch groups because
the pointwise inequality was established for their total nonnegative
density. The final ball must prove S>0 and positive endpoints before
taking square roots.

## Dependencies, verification and scope

The exact jet, scaled rational-function algebra, positive-pole moment
proof and complete synthetic norm fixture are the existing N4-305
paths. This new Laurent multiplication will be checked coefficient by
coefficient against direct trigonometric products on manufactured
fields and the six-generator fixture before any production use. The
full candidate reconstruction will bind its exact snapshot and every
code/proof dependency by SHA256. Point values, endpoint orders, field
hashes, radial group counts and integration balls are separate evidence.
A synthetic pass is not a production norm. Independent peer acceptance
is required before a resulting global norm is called certified.
