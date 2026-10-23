# Forced source geometry and the exact scaling test

Status: CONFIRMED for the algebra and explicitly conditional statements after independent checks and completed actual Opus5.5 reviews16 and19. Their suggestions have been checked and incorporated. Date: 2026-10-20.

## Statement and hypotheses

Let ell>1, L>0 and phi(r)=(1+r^2/L^2)^(-2). A forced state is a smooth parity-compatible density with its canonical velocity satisfying

    (ell X+U) dot grad rho-rho=mu*y*phi(r).

Assume a=rho_y(0)!=0. This is a different differential equation from the primary problem unless mu=0. Put c=psi_xy(0), A=2ell-1, Delta=ell+c-1, alpha=ell-c and beta_y=ell+c.

Then

    a Delta=mu, alpha=A-Delta, beta_y=1+Delta,
    alpha+beta_y=2ell, Bf=alpha-beta_y=-2c.

In particular the source matrix is diag(alpha,beta_y), not diag(A,1) when mu!=0. The word source requires alpha,beta_y>0. A scalar forced amplitude of order one cannot be silently omitted in an indicial analysis.

Write the Taylor terms

    rho=a*y+b*x^2*y+e*y^3+O(r^5),
    psi=c*x*y+q1*x^3*y+q2*x*y^3+O(r^6), H=q1-q2.

They obey

    q1+q2=-b/3,
    (2A-Delta)b+3a q1=-2mu/L^2,
    (2+3Delta)e+a q2=-2mu/L^2,                 (1)
    (a-4A+2Delta)b=3a H+4mu/L^2.              (2)

The formula (2) is a compatibility relation, not an existence or smoothness theorem.

## Direct derivation

Parity gives U=(-c*x,c*y)+O(r^3). The coefficient of y in the forced equation is a(ell+c-1), while phi(0)=1. This proves the first assertion. The quadratic Taylor coefficient of phi is -2r^2/L^2. The x^2*y coefficient of transport is (2alpha+beta_y-1)b+3a q1=(2A-Delta)b+3a q1. The y^3 coefficient is (3beta_y-1)e+a q2. Poisson gives 6(q1+q2)=-2b. Substituting q1=(H-b/3)/2 in the x^2*y equation gives (2). No origin relation from the unforced equation was used.

## Local homogeneous and Sobolev comparisons

For fixed ell and mu, a noninteger homogeneous perturbation h of degree d>1, with homogeneous stream chi of degree d+1, has leading coupled equation

    (alpha*x*d_x+beta_y*y*d_y-1)h+a*chi_x=0,
    -Delta chi=h_x.                           (3)

A change of mu adds an integer-degree smooth forcing and does not change this homogeneous noninteger block. Changing ell is likewise a separate smooth column. Equation (3) is a local necessary block, not a global canonical inversion of a superlinear homogeneous density.

Applying the Laplacian, without assuming Bf is nonzero, gives

    (alpha*x*d_x+beta_y*y*d_y+2beta_y-1)Delta h
                    +(2Bf-a)h_xx=0.           (4)

Assume now Bf!=0. For nonresonant transverse power branches the singular density exponents at the x-axis and y-axis are respectively

    kappa=(alpha*d-1)/Bf,
    p_y=(1+a-beta_y*d)/Bf.                     (5)

At the x-axis, h behaves as x^(d-kappa)y^kappa and the stream contribution has two additional transverse powers, giving alpha*d-Bf*kappa-1=0. At the y-axis, local Poisson inversion gives chi_x=-h at leading singular order; the coefficient is beta_y*d+Bf*p_y-1-a. These balances alone do not classify exceptional integer powers or logarithms.

For alpha>beta_y>=1, kappa-d=(beta_y*d-1)/Bf>0. Thus the algebraic envelope of min(d,kappa,p_y), over d>1, is

    (1+a)/alpha                 if a>alpha-1,
    (1+a-beta_y)/Bf             if a<=alpha-1. (6)

At equality both expressions equal 1. This is the supremum of the formal exponent envelope; the second line is approached as d tends to 1 from above. It is not an optimization over admissible function-valued branches. In the quoted example p_y<-1 throughout d>1, so a nonzero raw power branch would not even be locally integrable; distributional powers or exceptional cancellations require separate treatment. Promoting it to a sharp regularity theorem requires the distributional matching argument, with all exceptional cases treated. It does not apply when Bf<=0 or beta_y<1 without redoing the maximization. It gives no global kernel, singular-value estimate or nonlinear family. On a small forced branch tending to zero density the matrix tends to ell times the identity and Bf tends to zero, so (5)-(6) are not uniform in that limit. The exact energy formula below remains valid when Bf=0.

There is also an exact norm identity. For a Schwartz function with Fourier support compact and away from zero, and any real s,

    Re <Lambda^s Lh,Lambda^s h>
      = integral [s(alpha*w1^2+beta_y*w2^2)
                  -1-(alpha+beta_y)/2-a*w1^2]
                   |k|^(2s)|hat h(k)|^2 dk,   (7)

where L is the density operator in (3), w=k/|k|, and the Fourier measure matches Plancherel. Fourier transformation gives

    hat Lh=-(alpha*xi*d_xi+beta_y*zeta*d_zeta)hat h
                 -(alpha+beta_y+1+a*w1^2)hat h.

Integration by parts contributes (alpha+beta_y)/2 and s(alpha*w1^2+beta_y*w2^2), proving (7). For alpha,beta_y>0, strict positivity in every frequency direction is equivalent to

    s>(1+ell+a)/alpha,  s>(1+ell)/beta_y.

These are frozen Sobolev energy thresholds, not Fredholm theorems.

## Numerical example and the scope of the objection

The lead reports a forced state at ell=3, a about 1.1385, Delta about 1.7397. Its actual source eigenvalues are about (3.2603,2.7397), rather than (5,1). The formal quantity in the second line of (6) is about -1.15, whereas the unforced expression a/(A-1) is about 0.285. These decimal inputs are quoted observations pending independent recomputation, not certified parameters. The exact algebra already refutes the identification of the forced-state source with the unforced source. A correlation between the unforced expression and a raw coefficient Jacobian singular value is not a derivation of a degeneracy mechanism.

## Forced scaling and zero sets

Let S_lambda rho(X)=lambda*rho(X/lambda). The canonical inverse scales in the same way, so its unforced residual obeys

    R[S_lambda rho](X)=lambda R[rho](X/lambda).

For the forced equation this sends L to lambda L and leaves mu and ell unchanged. If a physical density functional N satisfies N(S_lambda rho)=lambda^sigma N(rho), sigma!=0, then its value beta transforms by lambda^sigma. For a dimensionless coefficient B0(infinity) defined after choosing a basis length L, the physical functional is L^(1-p) B0(infinity); changing both L and the profile can instead leave the dimensionless coefficient fixed. These two beta conventions must not be interchanged.

For an exact state rho_* with N(rho_*)!=0 and mu=0, its scaling orbit supplies a zero-forcing solution at every beta of the same sign, at the same ell. The required lambda is (beta/N(rho_*))^(1/sigma). If N(rho_*)=0, this gauge does not intersect nonzero-beta slices and this conclusion does not cover that profile.

Consider a connected interval I of beta values of one sign and a continuous curve (rho(beta),mu(beta)) of forced solutions with fixed ell,L. Fix a working topology invariant under the scaling maps and assume lambda -> S_lambda rho is continuous there and N is continuous. Assume PARAMETRIC local uniqueness in the joint (rho,mu) variables: near each zero-forcing point, for every nearby beta, there is only one nearby solution state satisfying N(rho)=beta, at the fixed ell,L. An invertible derivative in a suitable Banach formulation is one sufficient hypothesis, but is not established here for IPM. Then the zero set of mu on I is closed by continuity and open because the exact scaling orbit is a competing nearby solution curve. Connectedness implies it is empty or all of I. Pointwise isolation in each fixed-beta fiber is insufficient: mu(mu-(beta-beta0))=0 has isolated solution fibers, yet mu=beta-beta0 has one isolated zero and intersects the identically zero branch.

For radial phi with phi(0)=1, the smooth solution of the linear forced equation ell X dot grad rho-rho=mu*y*phi(r) is

    rho_lin=(mu/ell)*sin(theta)*r^p integral_0^r s^(-p)phi(s) ds,
    p=1/ell.

Its center slope is mu/(ell-1). Integrating the radial first-order equation proves the formula; the omitted homogeneous term r^p Theta cannot be smooth at zero for 0<p<1. For the stated phi the tail coefficient is

    K_lin=mu*L^(1-p)*Beta((1-p)/2,(3+p)/2)/(2ell).

For any first-sine-mode density rho=y*g(r) of this growth, rho_x=(r*g'(r)/2) sin(2theta). In the canonical mode-2 Green formula its quadratic stream coefficient is (1/8) integral_0^infinity g'(r) dr=-g(0)/8; the inner integral contributes only O(r^4). Since r^2 sin(2theta)=2xy, the strain is -g(0)/4. Both endpoints converge because g is even smooth at zero and g=O(r^(p-1)) at infinity. Hence c_lin=-a_lin/4=-mu/[4(ell-1)]. If a nonlinear expansion rho=mu*rho_1+O(mu^2) is controlled in a topology where the center slope and canonical strain are continuous, it follows that

    a=mu/(ell-1)+O(mu^2),
    c=-mu/[4(ell-1)]+O(mu^2),
    Bf=mu/[2(ell-1)]+O(mu^2).

For fixed ell>1 and sufficiently small positive mu this determines Bf>0, beta_y>=1 and a<alpha-1, so the second line of (6) applies. Smallness depends on ell and the unproved remainder constants; it is not uniform as ell approaches 1 or infinity. Negative forcing is not an equivalent sign convention: the velocity transport term is quadratic under rho -> -rho, and Bf<0 at small negative mu, outside the scope of (6). The formal envelope in (6) tends to negative infinity, with leading term -2(ell-1)^2/mu. Its singularity is a limitation of that anisotropic parametrization, not a degeneracy theorem. Without the controlled nonlinear expansion only the displayed linear coefficients are established.

This constructs only the linear forced solution. A nonlinear O(mu^2) expansion in a controlled function space is a further hypothesis. Under such an expansion and parametric uniqueness over the whole connected beta interval, the small positive branch cannot acquire a zero of mu. Finite positive samples or finite-matrix invertibility do not establish those hypotheses. A change of invariant parameters between two numerically located zeros at different beta values can also arise from selecting different exact profile branches. It refutes identification of those points as the same scaling orbit, but by itself does not show either point to be a numerical artifact. A scaling robustness test must control solution lineage.

## Dependencies and verification scope

Canonical scaling: ../scaling/PROOF.md. Fourier energy calculation: ../frozen_sobolev/PROOF.md, generalized here to both source eigenvalues. Other steps use Taylor expansion, Fourier differentiation and a connectedness argument. The cubic equations and frozen-symbol algebra are checked independently over exact rational data in verification/. No claim of a primary YES or NO endpoint follows.
