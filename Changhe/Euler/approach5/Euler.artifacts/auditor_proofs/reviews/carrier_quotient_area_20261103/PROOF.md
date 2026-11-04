# Independent audit of the carrier quotient and its area obstruction

Status: A2437-A2443 CONFIRMED at their stated local scopes; A2444 OPEN. The existing coordinator comparison agrees with the independent derivation. The conclusions concern the pressure-free linear carrier system only.

## 1. Exact class and source

Fix 0<c<1/2 and omega in R, let Jx=e3 cross x, A=cI-omega J, L=(1-c)I+omega J, X(x)=Ax, a=1-2c and delta=3c-1. A carrier is a smooth vector field V on an open set away from the origin satisfying

    div V=0, X.V=0, (DV)X=-LV.                       (C)

There is no assumed scalar S, scalar transport, pressure, Poisson equation, common flat point, whole-space extension or decay. These omitted conditions are essential when comparing with the Euler campaign.

The complete six-section LIT302 source is retained as in the team records with its original hash. The separate six-section auditor proposal about the exact quotient equation and section changes was reread and retained. LIT301 A2428-A2430 supplies the independent flat sine example used only in Section 7 below.

## 2. General flowbox correspondence, including the converse

Let Phi(y,t)=exp(tA)sigma(y) be a smooth X-flowbox from D times I onto G, with 0 in I and D an open planar disc. Put

    rho0=|det(sigma_1,sigma_2,X(sigma))|>0,
    beta_i=X(sigma).sigma_i/|X(sigma)|^2.

The coordinate density is rho=exp(3ct)rho0. The bracket computed in Cartesian coordinates is [X,V]=(DV)X-A V=-V. Thus the contravariant coordinate field has form Vhat=exp(-t)(v(y),h(y)). Since exp(tA) is a Euclidean similarity, X.V=0 is equivalent at every t to X(sigma).D sigma v+|X(sigma)|^2 h=0, or h=-beta(v).

The coordinate divergence formula gives

    div V=exp(-t)[rho0^(-1)div_y(rho0 v)+delta h].

Consequently (C) is equivalent to

    div_y(rho0 v)=delta rho0 beta(v),                 (Q)

with the exact inverse

    V(Phi(y,t))=D Phi_(y,t) exp(-t)(v(y),-beta(v)).    (I)

Necessity follows from the preceding calculation. Conversely, start with any smooth solution v of (Q) and use (I). The same orthogonality and divergence formulas hold, while [X,V]=-V implies (DV)X=(A-I)V=-LV. Thus this is a genuine bijection, not a necessary condition alone.

Differentiating X.V=0 yields (DV)^T X=-A^T V. The vector identity X cross curl V=(DV)^T X-(DV)X now gives X cross curl V=(L-A^T)V=aV. This curl equation adds no further condition to this carrier class.

Expanding (Q), div_y v=(delta beta-grad log rho0).v. The coefficient is smooth and bounded on every compact smaller disc. Hence every quotient satisfies |div v|<=C|v| there, with a finite constant depending on the geometric patch and parameters.

## 3. Section changes and curvature

For sigma_tau=exp(tau(y)A)sigma(y), direct differentiation yields sigma_tau,i=exp(tau A)(sigma_i+X(sigma) tau_i). Added flow-direction columns do not change the determinant and the similarity factor cancels in beta. Therefore

    rho0,tau=exp(3c tau)rho0,
    beta_tau=beta+d tau,
    v_tau=exp(-tau)v.                               (T)

The last identity is for contravariant transverse components: the new section evaluates the old exp(-t)v at t=tau(y), while the quotient coordinate y is unchanged. Substituting (T) into (Q) reproduces that equation, since 3c-1=delta. In particular d beta is unchanged. Quotient coordinate changes simply pull the one- and two-forms back.

Take sigma=n on the unit sphere. Then rho0=c times the sphere area density, because X(n).n=c. In spherical coordinates (theta,phi), with D0=c^2+omega^2 sin(theta)^2,

    beta=-omega sin(theta)^2/D0 d phi,
    d beta=-2 omega c^2 sin(theta)cos(theta)/D0^2 d theta wedge d phi
           =-2 omega c^2 cos(theta)/D0^2 dArea.

The coefficient differentiation is exact: the omega^2 terms cancel. The last expression is smooth at the poles. For nonzero omega, d beta is nonzero away from the equator, so it is not identically zero on any nonempty open sphere patch.

Every local section can be compared with a sphere section by the linear X-flow, since |exp(tA)x|=exp(ct)|x|. This comparison only uses X and sigma; V need not extend outside its original flowbox. Thus the same curvature obstruction holds for any smooth transverse section.

## 4. Universal scalar densities, with necessity checked

On the sphere write j=rho0. A positive C2 function m is a universal density multiplier if div(mjv)=0 for every local smooth solution of (Q), on every smaller patch of its domain. The product rule gives

    div(mjv)=mj [d log m+delta beta](v).              (U)

To deduce an equality of one-forms, the allowed solution values must span the tangent plane. This is not an automatic consequence of notation. Put F=jv in any small coordinate rectangle. For F=(f,0), equation (Q) is partial_1 f=delta beta_1 f. A scalar ODE with nonzero smooth initial data supplies a smooth solution with nonzero first-coordinate value. The analogous ODE for F=(0,g) supplies the other coordinate direction. Thus solution values span at each point, and universality is equivalent to

    d log m=-delta beta.                            (G)

If delta omega!=0, differentiating (G) contradicts the curvature in Section 3 on every open patch. If omega=0, beta=0 on the sphere, and if delta=0, equation (Q) has no drift. In either case m=1 works. Therefore the universal multiplier exists exactly when omega=0 or c=1/3 in the stated parameter interval.

Under a section change its transformed value is m_tau=exp(-delta tau)m: then m_tau rho0,tau v_tau=m rho0 v. This proves that the existence issue is unchanged by sections. It concerns scalar invariant densities for the entire local solution class. It does not exclude other transformations or a density selected for one particular solution on a smaller region.

## 5. Exact annular cycle and the individual-density obstruction

Assume delta omega!=0. Choose a small sphere coordinate disc whose closure avoids the equator and the poles; d beta has one strict sign there. Use positively oriented polar coordinates (r,theta) in this disc and select an interior circle r=R. On a thin open annulus containing it, write beta=beta_r dr+beta_theta d theta and j>0 for the transformed coordinate volume density. All coefficients are smooth and periodic in theta.

Define

    B(r,theta)=delta integral_R^r beta_r(s,theta) ds,
    w(r,theta)=delta exp(B(r,theta))
                    integral_R^r exp(-B(s,theta)) beta_theta(s,theta) ds,
    v^r=w/j, v^theta=1/j.

Differentiation of the displayed integral gives w_r=delta beta_r w+delta beta_theta and w(R,theta)=0. Since jv^theta=1, the planar divergence in (Q) is exactly w_r and the right side is delta(beta_r w+beta_theta). Thus v solves (Q) exactly, and is nowhere zero because v^theta>0.

The circle r=R is a v-periodic orbit of period integral_0^(2pi) j(R,theta) dtheta. Near it, theta is a valid flow parameter and the radial equation is dr/dtheta=w. Linearization at R gives h'=delta beta_theta(R,theta)h. The transverse first-return derivative is therefore

    M=exp(delta integral_C beta).

Stokes' theorem gives integral_C beta=integral_disc d beta!=0. Hence M is positive and different from one. This is a hyperbolic periodic orbit of the two-dimensional quotient. The disc and annulus can be chosen arbitrarily small about an off-equator non-pole point; the assertion is existential, not a construction about every possible center. Reversing v reverses the traversal and replaces M by M^(-1), supplying the opposite stability.

For this individual field, a positive C1 multiplier on a neighborhood containing the whole circle would satisfy v(log m)=-delta beta(v) by (U). Integrating for a full v-period gives 0=-delta integral_C beta, a contradiction. Thus an individual density also fails for this particular annular field on such a neighborhood. This strengthens the universal obstruction only at that explicit scope. A density on a smaller region not containing the entire cycle is not excluded.

## 6. The lift is a spiral, not a closed three-dimensional orbit

The sphere parametrization Phi(t,y)=exp(tA)n(y) is injective on R times the annulus: its radius exp(ct) determines t, and then the sphere point determines y. The inverse is smooth, so its image is an open X-saturated region. Use (I) to lift the annular field to this region. Section 2 proves every identity of (C) and X cross curl V=aV there.

Along a lifted trajectory over r=R, the common factor exp(-t) cancels when dividing the t- and theta-components. Consequently

    dt/dtheta=-beta_theta(R,theta),
    Delta t=-integral_C beta!=0

after one quotient turn. Each such turn occurs in finite physical V-time, since on a finite theta interval t is finite and j is positive and smooth. The Euclidean radius changes by the factor exp(-c integral_C beta)!=1. Therefore the lifted trajectory is not periodic. It spirals on the X-saturation of the quotient circle. No completeness of the V-flow for infinite time is claimed or needed.

This distinction prevents an invalid application of circulation or closed-loop arguments to the three-dimensional lift. The construction neither fills the quotient annulus nor extends the field through the spatial origin. It has no flat common orbit, scalar S or pressure candidate.

## 7. The LIT301 sine field fails every smooth carrier quotient

For each integer M>=1, A2428-A2430 verifies that the smooth planar field f_M=exp(-1/|z|^2) conjugate(sin(1/z)^M), extended by zero at zero, has div f_M/|f_M|=2/r^3 at positive radii with sin(1/r)=1. The ratio is unbounded as these radii approach zero.

But Section 2 would require div f_M=B0.f_M, with B0=delta beta-grad log rho0 smooth near the central point of a flowbox. This would bound that ratio in absolute value on a compact smaller disc. Thus f_M cannot be the quotient of any smooth carrier on an X-flowbox about a nonzero spatial point.

This conclusion is coordinate invariant. Under a smooth nonsingular quotient coordinate change, a positive smooth density stays positive and smooth, and the first-order coefficient remains smooth. If the transformed field were a quotient, pulling its equation back would supply just such an equation for f_M. No singular coordinate substitution is admitted in this assertion.

## 8. Dependencies, pass criteria and open scope

All six LIT302 source sections and all six original proposal sections were read in full, and their quotient and curvature formulas agree with the independent calculations above. The proof uses the explicit linear flow, elementary differentiation, a coordinate divergence formula, local scalar ODEs, the radial variational equation and Stokes' theorem. No numerical computation, formal build or unverified analytic-existence theorem is used.

The mathematical pass criteria are the inverse correspondence, exact factor delta, all section laws, the local-solution spanning argument for universality, the displayed ODE for w, the nontrivial return multiplier, and the nonclosed lift. Source and dependency hashes are retained. The existing configured model coordinator read the proposal and LIT302 in full and independently checked the signs, inverse, annular ODE, return multiplier and nonclosed lift in the team records, Sections 2 and 5. That comparison is pinned as in the team records, with no discrepancy. Provider execution remains independently unattested.

None of these statements bounds the inner degree of a flat carrier with negative off-center indices, supplies the scalar or Poisson equations of F, decides the positive-trace endpoint, or proves unrestricted smooth decaying rotating-profile nonexistence. Those questions remain open. Even a future degree bound would eliminate only accumulating off-orbit zeros in the LIT301 dichotomy, not the central flat orbit itself.
