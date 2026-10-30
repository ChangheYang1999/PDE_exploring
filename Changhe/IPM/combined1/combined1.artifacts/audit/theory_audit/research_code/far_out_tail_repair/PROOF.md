# An integrable tail can be repaired at arbitrarily small L2 cost

## Exact statement

Let -3<q<-1, and let A(theta) be a finite real linear combination of
cos(2m theta), m nonnegative integers. Let b(s)=exp(-1/s) for s>0 and
b(s)=0 for s<=0, and fix the smooth radial cutoff

    zeta(r)=b(r-1)/(b(r-1)+b(2-r)).

Thus zeta=0 on r<=1 and zeta=1 on r>=2. Define

    chi_1(X)=-zeta(|X|)|X|^(q+3) A(arg X),
    h_1=-partial_y Delta chi_1,
    psi_1=partial_x partial_y chi_1,
    v_1=(-partial_y psi_1,partial_x psi_1).

All four functions are defined to be zero near X=0. For every L>=1 set

    chi_L(X)=L^(q+3) chi_1(X/L),
    h_L=-partial_y Delta chi_L,
    psi_L=partial_x partial_y chi_L,
    v_L=(-partial_y psi_L,partial_x psi_L).                (1)

Then h_L is smooth and S1 (even in x, odd in y), belongs to L2(R2),
and its canonical IPM velocity is exactly v_L. Both h_L and v_L
vanish on |X|<=L. On |X|>=2L their density and velocity are the exact
homogeneous fields obtained by differentiating -r^(q+3)A(theta).
For every nonnegative integer k and real beta with

    q+1+beta-k<0,

let C_(beta,k)=|| |X|^beta D^k h_1 ||_2, where D^k is the full ordered
Cartesian derivative tensor (D^0 h=h). This finite, explicitly defined
constant is independent of L. One has the exact identity

    || |X|^beta D^k h_L ||_2
       = L^(q+1+beta-k) C_(beta,k),                      (2)

and the inhomogeneous bound

    || (1+|X|^2)^(beta/2) D^k h_L ||_2
       <= 2^(max(beta,0)/2) L^(q+1+beta-k) C_(beta,k).    (3)

The same statements hold with h replaced by v. In particular, given
any epsilon>0, choosing

    L>max{1,(C_(0,0)/epsilon)^(1/(-q-1))}

makes ||h_L||_2<epsilon while retaining the prescribed homogeneous
density and velocity tail. If C_(0,0)=0 the conclusion is immediate.
No stationary equation or inverse is asserted in this statement.

## Proof of smoothness, canonical velocity and scaling

The function b is smooth with all derivatives zero at0. The denominator
in zeta is everywhere positive for r>=0, so zeta is smooth, constant
near the origin, and has the stated values. The finite angular factor
is smooth off the origin. Multiplication by zeta removes the origin
singularity of the nonintegral homogeneous power. Evenness of chi in
both Cartesian variables gives S1 parity of h.

Every derivative of order j of chi_1 is O(r^(q+3-j)) outside radius2.
Thus h_1 and v_1 are O(r^q); their derivatives of order k are
O(r^(q-k)). The condition in (2) is exactly integrability of
r^(2(q-k+beta)) r dr at infinity. There is no singularity at zero,
since the fields vanish near zero.

The field v_L is divergence free, and its curl is
Delta psi_L=partial_x partial_y Delta chi_L=-partial_x h_L.
The canonical L2 IPM multiplier has these same divergence and curl
identities and is bounded on L2. The difference is therefore a
harmonic L2 vector field on the whole plane and is zero. Equivalently,
its Fourier transform vanishes off the origin and is an L2 function,
so is zero almost everywhere. This identifies the complete canonical
operator, including its local/contact term. No nonlocal term has been
silently dropped merely because the fields vanish on an interior disk.

The chain rule in (1) gives exactly

    h_L(X)=L^q h_1(X/L), v_L(X)=L^q v_1(X/L).

Apply k derivatives and the substitution X=LY. Its Jacobian is L^2;
the homogeneous weight contributes L^beta. This proves (2). On the
support |X|>=L>=1, for beta>=0 one has
(1+|X|^2)^(beta/2)<=2^(beta/2)|X|^beta; for beta<0 the same inequality
holds with factor1. This proves (3) and the stated epsilon choice.
For |X|>=2L, homogeneity cancels the scaling factor in chi_L, so the
exterior potential is exactly -r^(q+3)A(theta), independently of L.

## Residual perturbation bound with all constants specified

Let c>1, gamma=1/c and let rho be a smooth S1 reference with canonical
velocity U_0. Assume for r>=R_0>=1 that

    |U_0(X)|<=V r^gamma, |grad rho(X)|<=G r^(gamma-1),

where V,G are finite nonnegative constants. Define

    F(rho)=c X.grad rho-rho+U_0.grad rho,
    C_lin=||c X.grad h_1-h_1||_2,
    C_grad=|| |X|^gamma grad h_1||_2,
    C_vel=|| |X|^(gamma-1) v_1||_2,
    C_quad=||v_1.grad h_1||_2.

All four constants are finite. For L>=R_0,

    ||F(rho+h_L)-F(rho)||_2
      <= L^(q+1) C_lin
         +L^(q+gamma)(V C_grad+G C_vel)
         +L^(2q) C_quad.                               (4)

Proof. Linearity of the canonical velocity and expansion of the
quadratic transport term give

    F(rho+h_L)-F(rho)
      =c X.grad h_L-h_L+U_0.grad h_L
         +v_L.grad rho+v_L.grad h_L.

Every term is zero on r<=L. Apply the assumed exterior bounds and
(2) to the two mixed terms. The last term scales pointwise as
L^(2q-1)(v_1.grad h_1)(X/L), hence has L2 norm L^(2q) C_quad.
The linear term scales as L^q. The triangle inequality proves (4).
Its exponents q+1,q+gamma,2q are all negative. Thus both the reference
change and the residual change tend to zero in L2 as L tends to
infinity. This is a stability statement for the residual, not a claim
that the residual itself tends to zero.

## Application to the audited campaign tail

Use the exact coefficients A1_m of data/{007,013,014}_tail_repair.json
and put A(theta)=sum_m A1_m cos(2m theta),

    q=4gamma-5=-11375183046454913/4076476460239181.

The audited construction in ../forced_integrable_tail/PROOF.md shows
that -r^(q+3)A has density coefficient -Theta_(4,1) and stream
coefficient -Psi_(4,1). Therefore rho+h_L has zero density and stream
(4,1) coefficients. All leading ladder sectors and all other original
single-field sectors remain unchanged at infinity, since this new
correction is exactly homogeneous outside2L.

For each of the three references, the first uncancelled residual sector
remains (9,0), exponent

    e_9=1-9delta=-12345613358746216/4076476460239181<-3.

Indeed, the old linear (4,1) residual is cancelled exactly. Mixed terms
involving h_L have largest possible exponent q+gamma-1=5gamma-6,
which is below e_9, and the quadratic self term has exponent2q-1,
also below e_9. The exact reference has no intervening nonzero sector.
Thus the new residual is O(r^e_9), belongs to
E_a=L2((1+r^2)^(-a)dX) at infinity for every a>-2, and the (9,0)
coefficient is unchanged. Smoothness gives local membership as well.
Every origin jet and velocity normalization is unchanged, because
both correction fields vanish on the entire disk r<=L.

The correction remains outside E_a when a<=q+1, and belongs to E_a
when a>q+1. The nonzero prescribed angular tail proves this exact
threshold by the radial power integral; at equality the divergence
is logarithmic. Hence the operation changes the finer weighted
affine class, although its unweighted L2 cost can be arbitrarily small.
It does not contradict the audited weighted-affine obstruction.

For the graded high norm beta=11/5,k=2, the exponent in (2) is
q+6/5<0. For the sharp weight's exterior power beta=8/5,k=2 it is
q+3/5<0. Therefore this same tail repair can be arbitrarily small in
both corresponding weighted Hessian norms and in the lower derivative
L2 components. No negative-order norm or background operator bound is
claimed without a separate argument.

## Consequences and limitations

A large norm for the specific global polynomial correction of T4-295
does not give a lower bound for all corrections that cancel its tail.
Equations(1)-(3) supply explicit counterexamples to such a lower bound.
This construction requires a radial cutoff outside the present finite
polynomial basis. It is an analytic reference-design operation, not an
accepted campaign snapshot or a new fit. Since the original residual
is unchanged throughout r<=L and changes by arbitrarily little in L2,
this does not remove the already certified finite-radius weak
obstructions when L is sufficiently large, or produce a stationary
solution. More precisely, let S be the same fixed-c set of exact
normalized stationary profiles in the original affine L2 class. The
triangle inequality gives

    dist_L2(rho+h_L,S)>=dist_L2(rho,S)-||h_L||_2.

Taking an infimum preserves the inequality, including when S is empty.
If a certified lower distance d0 exceeds a proposed ball radius r0,
every choice with ||h_L||_2<d0-r0 preserves that exclusion. Numerical
certificates for other quantities at the altered reference still
require fresh validation.

The neighboring checker only verifies the exact campaign exponents
and source coefficients. The general proof above is analytic and
requires independent Opus review before being called AUDITED.
