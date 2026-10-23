# Fixed-map dynamic rescaling: residual conversion, coefficient mass matrix and a canonical manufactured state

Written 2026-10-21 before implementing the exact tests. Verifier result 151. This note proves identities needed to test a proposed numerical evolution. It does not claim that the evolution has been implemented, converges or is stable.

## 1. Exact field equation and assumptions

Let rho=y w(r)b(r,theta), where w>0 is a fixed differentiable radial weight and rho is smooth with Setting III parity. Put omega=r w'/w. Let U be the canonical full-plane velocity and define

    E_c = [(c X+U).grad rho-rho]/(y w).

Away from y=0 and r=0, ordinary differentiation gives

    E_c=(c+U_r/r) r b_r+(U_theta/r)b_theta
              +[c-1+U_2/y+(c+U_r/r)omega]b.                (1)

The dynamic rescaling equation rho_tau=c_w rho-(c_x X+U).grad rho is therefore equivalent, for a fixed weight and map, to

    b_tau=-E_(c_x)+(c_w-1)b.                               (2)

All terms on the right are field values. This exact formula explains the sign in the numerical proposal. The expression called residual_fine in the frozen producer source implements the algebra in (1), with its numerical stream. The steady system() routine additionally overwrites rows and appends a spatial gauge equation; those rows are not the physical field residual and cannot be evolved as if they were (2). This source observation does not validate the producer's numerical inverse.

At the origin rho=a y+O(r^3), U=(-cx,cy)+O(r^3), where here c=psi_xy(0) is the strain, not the subscript in E_c. The origin limit of (2) is a_tau=(c_w-c_x-c)a. Thus the slope gauge c_w=c_x+c makes this physical limit zero. A separate fixed far-field amplitude constraint is not part of (2) and must not be silently appended unless an additional rescaling is derived.

## 2. Coefficient versus field derivative

For a fixed compact coordinate t in [-1,1), put sigma=(1+t)/2. Suppose

    b(t,theta)=sum_(k=0)^(M-1) sigma^k beta_k(t) cos(2k theta),
    beta_k(t)=sum_(j=0)^(N-k) u_(k,j) T_j(t).

Let F=-E_(c_x)+(c_w-1)b. Project F angularly and denote its cos(2k theta) coefficient by F_k(t). Choose N+1-k distinct collocation nodes t_i, i>=k, with sigma(t_i)>0 for k>0. The k=0 family may contain t_0=-1. The coefficient derivative that interpolates F at the chosen mode nodes is

    sum_j T_j(t_i) u'_(k,j)=F_k(t_i)/sigma(t_i)^k.           (3)

The matrix on the left is invertible: a polynomial of degree at most N-k with N+1-k distinct zeros is zero, so its evaluation map is injective and square. Equivalently one can solve the mass system diag(sigma_i^k)V_k u'_k=F_k(t_i). For k=0 at the origin, use the finite physical limit just derived. No division by sigma^k at sigma=0 with k>0 is needed.

The frozen producer beta_full implementation evaluates Chebyshev coefficients, as seen directly from its multiplication by Ext[k].T. Its docstring's description of mode values is stale. Its beta_to_u routine expects beta values, so feeding F_k directly without the division in (3) would advance a different field. This is an implementation hazard, not a claim that an as-yet unwritten evolution made that mistake.

If F has modes outside the finite angular span, or its radial coefficients are outside the polynomial span, (3) defines a collocation projection of F. It does not equal the full field derivative everywhere. The projection error must be measured independently. For an F already in the trial space, (3) recovers its coefficients exactly in exact arithmetic. The verification below checks this property with rational nodes and exact Chebyshev evaluations, and verifies that omitting the sigma factor fails on a concrete mode.

## 3. Canonical rational manufactured density

Let s=x^2+y^2 and define on the whole plane

    psi=-xy/[4(1+s)],
    rho=y(s+2)/[2(1+s)^2],
    U=(-psi_y,psi_x).                                    (4)

Both are smooth, with the required parities. The density and velocity are O(r^-1), with the corresponding differentiated estimates at infinity. Consequently the canonical sublinear velocity condition holds. To verify Poisson directly, for any radial function f(s),

    Delta[xy f(s)]=xy[4s f''(s)+12 f'(s)].                (5)

Substituting f(s)=-1/[4(1+s)] gives

    -Delta psi=-xy(s+3)/(1+s)^3.

On the other hand, writing rho=y h(s), h=(s+2)/[2(1+s)^2], gives h'=-(s+3)/[2(1+s)^3] and rho_x=2xy h', the same expression. Thus (4) is the genuine canonical pair, by full-plane uniqueness; no external harmonic strain was added.

At the center,

    a=1, c=-1/4,
    rho=y-(3/2)x^2y-(3/2)y^3+O(r^5),
    psi=-(1/4)xy+(1/4)x^3y+(1/4)xy^3+O(r^6).

For a fixed target C>1 the slope gauge gives

    c_w=1/[4(C-1)], c_x=C/[4(C-1)].                       (6)

At this instant define rho_tau by the exact DR right side. Its linear y coefficient is zero. For C=3, the cubic x^2y coefficient of rho_tau is 9/8 and the cubic y^3 coefficient is 1/8, from direct differentiation or the identities in ../dynamic_rescaling_audit/PROOF.md. Thus it is not a steady state even though slope normalization holds exactly. Dividing the fields by c_w at this instant produces ell*=C and exact center normalization, not an exact profile.

This is an instantaneous manufactured right side. It supplies an exact full-plane test input and a known derivative for one evolution step. We do not assert that the fixed rational family is invariant under DR or that a solution has this form at later times.

## 4. Verification protocol and scope

Use exact fractions to differentiate (4), verify its Poisson identity, calculate U and the Cartesian DR derivative, and compare with the independently organized polar expression (1)-(2). Use rational x,y values away from the axes, and a map r=sqrt(sigma)/[2(1-sigma)] with rational sqrt(sigma), so the fixed-map weight w=1-sigma and omega=-2sigma/(1+sigma) are also exact rationals. This map has kappa=1 and is a manufactured-coordinate test, not an ell=3 far-field representation. The field identity (1) is valid for every such positive radial weight. Center checks use its exact Taylor coefficients instead of a small-radius quotient.

Separately, use exact rational radial nodes and exact Vandermonde solves for (3), with multiple angular modes. Compare recovery of predetermined coefficients and explicitly demonstrate failure if the sigma^k division is omitted. Also show that a steady state test cannot be replaced by the slope identity alone, using the nonzero cubic DR derivative above.

These checks validate algebra, units, projection and coefficient conventions. They do not establish the accuracy or stability of a future time integrator, its full-plane inverse implementation, or an endpoint. A variable map needs the additional chain rule in ../dynamic_rescaling_audit/PROOF.md and is outside (2)-(3).
