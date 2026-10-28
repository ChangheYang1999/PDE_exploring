# Canonical operator, normalization, and scaling

## Function class and canonical inverse

Start with a real smooth density h on R^2, even in x and odd in y, which is Schwartz. Let G=-(2 pi)^(-1)log r and define psi[h]=G*partial_x h. Set U[h]=(-partial_y psi, partial_x psi). Then, in the Fourier convention with partial_j represented by i xi_j,

    U[h]=(-R_1 R_2 h, R_1^2 h),     R_j=partial_j(-Delta)^(-1/2).

Indeed, psi=partial_x(-Delta)^(-1)h, and commuting derivatives gives the two components. Thus R_1^2 has multiplier -xi_1^2/|xi|^2. The parity of psi is odd in both x and y; U_1 is odd in x and even in y; U_2 is even in x and odd in y. At zero U=0 and

    DU[h](0)=diag(-c[h],c[h]),      c[h]=psi_xy(0).

For a growing background, require an explicitly fixed extension of the same inverse with the following properties: linearity, these parities, no harmonic velocity term, dilation covariance, and enough local differentiability for the displayed jets. A sufficient uniqueness condition for an already existing stream function is subquadratic growth of psi with the given odd/odd symmetry. The difference of two such entire harmonic stream functions is affine, by the mean-value derivative bounds applied on disks of radius tending to infinity, and parity eliminates every affine function. This is a uniqueness statement, not a construction of the inverse for every possible growing density.

For the numerical potentials, rho=-partial_y Delta chi and psi=partial_x partial_y chi imply -Delta psi=partial_x rho identically. The finite generators have chi=O(r^(3+gamma)) and psi=O(r^(1+gamma)), where 0<gamma<1. Thus their stream functions satisfy the preceding uniqueness condition when competing inverses have the same growth. The normalization does not permit adding an arbitrary harmonic strain.

## Exact origin identity

Let rho=a y+O(r^3) at zero, with a != 0, and let F(rho,c_l)=(c_l X+U[rho]) dot grad rho-rho. Put d=c[rho]. The background field has derivative diag(c_l-d,c_l+d) at zero. Direct Taylor expansion gives

    F(rho,c_l)=(c_l+d-1)a y+O(r^3).

Therefore an exact stationary profile with nonzero a satisfies c_l+d=1. For an approximate background this is not inferred from smallness of the residual: its precise defect is

    partial_y F(0)=a(c_l+d-1).

The archived checkpoint imposes d=1-c_l through exact center elimination. Its other Taylor residual coefficients can remain nonzero.

## Full derivative

On the normalized chart set c_l[rho]=1-c[rho]. Since c is linear, its variation is delta c_l=-c[h]. For Vbar=cbar_l X+U[rhobar], the Frechet derivative, whenever the function-space realization makes the products and c continuous, is

    L h = Vbar dot grad h-h + (U[h]-c[h]X) dot grad rhobar.                 (1)

This follows by expanding F(rhobar+h,cbar_l-c[h]); the exact remainder is

    Q(h)=(U[h]-c[h]X) dot grad h.                                        (2)

At fixed c_l the derivative instead lacks the term -c[h] X dot grad rhobar. A proof for that different operator does not prove a bound for (1).

The formulas (1)-(2) are algebraic identities on smooth functions. Calling (1) a bounded Frechet derivative on a Banach space additionally requires mapping estimates, including control of the derivative in (2). No such Banach-space conclusion is asserted here.

## Frozen origin and the first jet

Under exact center normalization, DVbar(0)=diag(lambda,1), lambda=2cbar_l-1, and grad rhobar(0)=(0,a0). Keeping both the frozen coefficients and the normalized rank-one term gives

    L_frozen h = lambda x h_x + y h_y-h+a0 R_1^2 h-a0 c[h] y.              (3)

The translation-invariant nonlocal principal part conventionally called L0 is (3) without its last term. These are distinct operators.

For a smooth h with the stated parity, U_2[h]=c[h]y+O(r^3). Hence (U[h]-c[h]X) dot grad(a0 y)=a0(R_1^2 h-c[h]y)=O(r^3). The left side is not identically zero. Its first jet is zero. Consequently partial_y(Lh)(0)=0 for any smooth h in the normalized chart. The forcing range therefore has a center compatibility condition if the topology retains a y-derivative trace. A surjectivity assertion onto unrestricted smooth odd forcing is false.

## Scaling and residual covariance

Let S_t rho(X)=t rho(X/t), t>0. The canonical inverse obeys U[S_t rho](X)=t U[rho](X/t) and c[S_t rho]=c[rho]. Thus c_l is unchanged and

    F(S_t rho)(X)=t F(rho)(X/t).

Differentiating at t=1 gives, with K=rho-X dot grad rho,

    L_rho K=F(rho)-X dot grad F(rho).                                    (4)

At an exact solution the right side is zero. At an approximate numerical state it must not be discarded. The same scaling leaves the coefficient a=rho_y(0) unchanged, so imposing a cannot remove this kernel direction.

If rho=r^gamma Theta(theta)+o(r^gamma), then S_t rho has leading angular profile t^(1-gamma)Theta. Suppose a Banach realization carries Theta in a normed angular space E and a bounded linear functional ell:E->R satisfies ell(Theta)!=0. The phase ell(Theta)=constant is transverse to scaling because its derivative on K is (1-gamma)ell(Theta), nonzero for gamma != 1. Merely writing this phase without proving continuity of the tail trace does not produce a normalized Banach domain.

## Dependencies and status

The center strain formula, including its local term, is proved in `../04_singular/PROOF.md`. The numerical normalization is independently checked in `../source_audit/recover_state.py`. All identities above are proved under the explicit smoothness, inverse, and growth hypotheses stated; existence or surjectivity of a global linear inverse remains open.
