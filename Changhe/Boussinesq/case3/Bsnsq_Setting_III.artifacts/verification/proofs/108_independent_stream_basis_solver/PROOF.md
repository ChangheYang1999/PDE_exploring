# A smooth stream-function trial space with the canonical relative inverse

Written UTC: 2026-10-21T02:14:19.069068+00:00
Status: exact trial-space properties proved before implementing a separate numerical solver. No candidate or small-residual claim.

## Definition and normalization

Fix a noninteger beta>2 and a0=1. The B2 spatial scaling is Psi_L(X)=L²Psi(X/L), Omega_L(X)=Omega(X/L), Theta_L(X)=L Theta(X/L), V_L(X)=L V(X/L). Direct differentiation preserves both PDEs, beta and Psi_xy(0); it sends a0 to a0/L and b0=Omega_x(0) to b0/L. Thus L=a0>0 fixes a0_L=1 and preserves b0_L=4a0_L/beta. In particular b0 is not invariant under this scaling. This normalization restricts no a0>0 profile if all spatial shapes are allowed; a finite trial family is only a restricted search space. Put s=1/beta, R=(1+x²+y²)^(1/2), t=R^(-s), eta=y/R. For finite real coefficient arrays C and D define

    Psi_raw=x R^(1-s) sum_(i,j,delta) C_(i,j,delta)
                  T_i(2t-1)T_j(eta) R^(-delta),
    Theta=x² R^(-1-2s) sum_(i,j,delta) D_(i,j,delta)
                  T_i(2t-1)T_j(eta) R^(-delta),
    Psi=Psi_raw-x (Psi_raw)_x(0),
    Omega=-Delta Psi, V=(-Psi_y,Psi_x), W=beta X+V.     (1)

Here T_i is the ordinary Chebyshev polynomial, and delta is0 or1. No y-reflection constraint is imposed. The delta1 block allows degrees shifted by one physical inverse radius; these include the constant-velocity-induced terms which do not occur in a pure integer-s ladder at noninteger beta. A finite block does not supply a complete asymptotic expansion or a solution. Generic compact source moments can also require inverse multipole terms such as r^-1 cos(theta) in Psi. Such exponents need not lie in a chosen finite ladder, although rational s can produce exponent coincidences; no universal absence of multipoles is asserted for this trial family.

Impose the three linear coefficient constraints

    Psi_xy(0)=1+beta/2,
    Omega_x(0)=4/beta,
    Theta_xx(0)/2=1.                                  (2)

All other center identities required by parity follow from oddness of Psi/Omega and evenness of Theta. Since Psi_raw has an x factor, its y derivative vanishes at0, and the gauge subtraction makes V(0)=0. Thus W(0)=0. Conditions(2) impose the prompt's center strain and vorticity compatibility exactly at the formal coefficient level. Finite arithmetic enforcement must be checked separately.

## Smoothness, growth and canonical inversion

Every R power in(1) is smooth on the full plane because R>=1. Theta is even in x and vanishes on x=0; Psi and Omega are odd in x. The finite Chebyshev expansions show that every stream term before gauge is a finite sum of

    x y^j (1+x²+y²)^[ (1-(i+1)s-j-delta)/2 ],          (3)

with i,j nonnegative. Differentiation shows for every fixed derivative order k

    D^k Psi_raw=O(r^(2-s-k)),
    D^k Omega=O(r^(-s-k)),
    D^k Theta=O(r^(1-2s-k))                            (4)

for r>=1. Individual terms can have faster decay. The linear gauge only adds a constant to velocity. Thus V=O(1+r^(1-s))=o(r), and Omega has the regularity and decay required to define the canonical full-plane relative kernel

    B[Omega](X)=int [K(X-Y)-K(-Y)]Omega(Y)dY,
    K(Z)=(Z2,-Z1)/(2pi|Z|²).

The integral is locally integrable and absolutely convergent at infinity. Here 0<s<1, and the difference kernel is O(|X|/|Y|²) for |Y|>2|X|; multiplying by Omega=O(|Y|^-s) is integrable in two dimensions. Splitting at distances comparable to|X| gives B[Omega]=O(1+r^(1-s)). Distributionally it has divergence0 and curl -Omega. The difference V-B[Omega] is an entire harmonic vector field of sublinear growth. The derivative estimate on balls of radius L tends to0 as L->infinity, so the difference is constant. Both fields vanish at0, so the difference is0. Consequently (1) uses exactly the canonical relative inverse, with no adjustable affine or harmonic velocity. Independent quadrature on manufactured and final fields remains an implementation check, not an extra mathematical assumption.

## Independent derivative representation

Expand each Chebyshev polynomial by its three-term recurrence. Store each monomial as

    coefficient * x^a y^b (1+x²+y²)^nu,
    nu=(n_s s+n_c)/2,

with integer exponents a,b,n_s,n_c. Exact formal differentiation uses

    d_x[x^a y^b R2^nu]
      =a x^(a-1)y^b R2^nu+2nu x^(a+1)y^b R2^(nu-1),

and the analogous y rule. Repeated application through order3 supplies Omega and its gradient. The integer exponent pair avoids approximate merging of radial powers. This evaluator does not import the numerics lane's spline, differentiation or inverse code and does not use the lead's generating-function jets.

The two physical residuals are

    F=W1 Theta_x+W2 Theta_y-(beta-2)Theta,
    G=W1 Omega_x+W2 Omega_y+Omega-Theta_x.              (5)

Their coefficient Jacobians follow directly from product rules because all fields depend linearly on C,D and W depends affinely on C. A solver minimizing (5) is a finite-dimensional nonlinear least-squares search only. In particular, its training weights are not the prompt's diagnostic normalizers. Independent held-out residuals, actual physical term normalizers without floors, center errors, far-field checks and refinement are required before any candidate claim.

## Scope and verification plan

The finite angular and radial truncations may obstruct exact solutions and can create false minima. The physical shift block addresses one known representation obstruction only. Integer beta, with its logarithmic inverse resonance, is not covered by the first pilot implementation. No statement about absence of full-plane profiles follows from solver failure. The independent solver is intended to test a different discretization and strengthen the numerical audit.

The constraints and inverse property in this note are exact analytic statements. Floating-point computed coefficients are input data, not proof. Store coefficients and beta/a0 in exact JSON, keep all code hashes and verification reports alongside, and report a failed or unfinished solve as such. No JavaScript, servers, cluster access or Lean/Lake execution is used.

## Manufactured forcing calibration

For fixed beta, trial basis and center-constrained coefficient vector zstar, define the smooth forcing fields fstar(X)=F(zstar;X), gstar(X)=G(zstar;X) from(5). For lambda in[0,1] consider F(z;X)-lambda fstar(X), G(z;X)-lambda gstar(X). At lambda=1, z=zstar is an exact PDE zero on the whole plane, including held-out points, because the forcing is a function defined from the same trial state, not an interpolation of training data. Its coefficient Jacobian is exactly the unforced Jacobian, since fstar,gstar are independent of z. The existing regularizer reg*z does not vanish at a nonzero zstar, so the full regularized least-squares objective has no asserted zero. A reg=0 control and a reg=1e-5 comparison separate this issue. Their PDE mismatch and regularization are reported individually.

The forcing is artificial and does not turn a forced solution into a B2 profile. Reducing lambda to0 can locate another finite-space minimum. Success at lambda1 is an implementation/optimization control, not proof that continuation to0 is possible; failure or turning alone gives no nonexistence theorem. Each state retains the same defining B2 physical normalizers when its unforced residual is reported. For the forced equations, adding lambda|fstar| or lambda|gstar| to the corresponding normalizer is the actual sum of absolute terms of those forced equations. No denominator floor is introduced.
