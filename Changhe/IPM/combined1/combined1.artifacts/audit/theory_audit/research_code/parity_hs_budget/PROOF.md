# A symmetry-resolved Hilbert-Schmidt budget for the signed low estimate

## Statement and spaces

Let rho be a real smooth function, even in x and odd in y. Assume its first derivatives are bounded and vanish at infinity, and that rho has compact smooth approximations with uniformly convergent gradients and L2-convergent Hessians. These assumptions hold for the finite canonical profiles with sublinear differentiated tails considered in this campaign. Set a=rho_x, b=rho_y and R_j=partial_j(-Delta)^(-1/2), with symbol i xi_j/|xi|. On complex L2(R2) define

    K=(1/2)[R1,[R1,b]]-(1/2)[R1,[R2,a]],
    kappa^2=((log2-1/2)||D rho_x||2^2+(3log2-2)||D rho_y||2^2)/(16pi).

The audited gradient-commutator identity gives K self-adjoint and ||K||HS^2=kappa^2. Let H_{+-} be functions even in x and odd in y, the S1 space. Choose any finite linearly independent family h_0,...,h_{d-1} of even-even L2 functions. Define the Gram matrix G_ij=<h_j,h_i> and the compression matrix B_ij=<K h_j,h_i>. Put

    T=tr(G^-1 B G^-1 B).

Then 0<=T<=kappa^2 and

    ||K restricted to H_{+-}||op <= sqrt(kappa^2-T).        (1)

Thus a certified lower bound T_lo and certified upper bound kappa2_hi improve the signed S1 low estimate whenever T_lo>0. If theta bounds (sqrt(a^2+b^2)-b)/2 on the whole plane and V=cX+U[rho] is complete and globally Lipschitz with div V=2c, then the maximal S1 L2 realization of V.D-1+U[.].D rho, also with any bounded Lipschitz divergence-free S1-compatible perturbation of V, has decay and inverse rate at least

    beta=c+1-theta-sqrt(kappa2_hi-T_lo),                    (2)

provided beta>0 and 0<=T_lo<=kappa2_hi. This is a low-space certificate. It does not provide a high inverse, a strain trace on L2 or a nonlinear existence theorem.

## Orthogonal budget proof

Reflection in x reverses R1 and a and preserves R2 and b. Reflection in y reverses R2 and a and preserves R1 and b. Expanding either double commutator therefore shows that K commutes with both reflections. The four joint parity spaces are orthogonal reducing subspaces. In particular, the even-even space and H_{+-} are orthogonal reducing subspaces.

Let P project onto the span of the chosen h_i, which is contained in the even-even space. In an orthonormal basis extending that finite family, the Hilbert-Schmidt sum of squared matrix entries contains the entire H_{+-} block and the P block as disjoint subsets. Hence

    ||K restricted to H_{+-}||HS^2+||PKP||HS^2<=kappa^2.

Write S:c^d -> L2 for the coefficient map. Then S* S=G and S* K S=B. The map S G^-1/2 is isometric. Its compression is G^-1/2 B G^-1/2, whose squared Hilbert-Schmidt norm is tr(G^-1 B G^-1 B), because B is Hermitian. This proves (1). The formula remains valid for a nonorthogonal family; replacing G by the identity is not allowed.

The signed principal part P0=R1 b R1-(R1 a R2+R2 a R1)/2 satisfies <P0h,h><=theta||h||2^2. Since Sym(U[.].D rho)=P0+K, integration by parts in transport gives (2) on a compact smooth core. Complete Lipschitz transport and bounded perturbation identify the maximal distributional generator and extend the estimate. Integrating the decaying semigroup gives a unique inverse bounded by 1/beta. This is the same audited low-generator argument as in signed_coupling/PROOF.md; no finite-section invertibility is inferred.

## An exact radial compression family

For z>0 let g_z(X)=(z^2+|X|^2)^(-1/2). Define f_n=partial_z^n g_z evaluated at z=1 and h_n=-Delta f_n. These are smooth radial even-even L2 functions. The two-dimensional Poisson identity is

    (-Delta)^(1/2) g_z = z(z^2+r^2)^(-3/2) = -partial_z g_z.

It follows either by the decaying harmonic extension in the additional coordinate z, or by the Fourier identity hat g_z=2pi exp(-z|xi|)/|xi|. The latter is a tempered-distribution identity; its derivatives used here are ordinary L2 functions. Thus

    U1[h_n]=-partial_xy f_n, U2[h_n]=partial_xx f_n,
    Rj h_n=-partial_j f_{n+1}.

Put t=r^2 and use a prime for d/dt. Then

    H_n(t)=h_n=-4(f_n'+t f_n''),
    U1[h_n]=-4xy f_n'', U2[h_n]=2f_n'+4x^2 f_n'',
    R1h_n=-2x f_{n+1}', R2h_n=-2y f_{n+1}'.

For a pair i,j define

    A_ij=-2(H_i f_j''+H_j f_i'')-4f_{i+1}'f_{j+1}',
    D_ij=H_i f_j'+H_j f_i', C_ij=A_ij+2D_ij'.

The bilinear signed-decomposition identity gives

    <K h_j,h_i>=integral [a xy A_ij+b(D_ij-x^2 A_ij)] dX
                 =-integral rho y C_ij(r^2) dX.           (3)

The second equality follows from

    partial_x(xy A)+partial_y(D-x^2 A)=y(A+2D').

All boundary terms vanish: the rational tests and their derivatives decay sufficiently rapidly against the assumed sublinear profile. Formula (3) depends only on the first sine mode of rho. No inverse or nonlinear residual is evaluated by this compression.

The h_n are linearly independent. In Fourier variables they are nonzero common factors |xi| exp(-|xi|) times the distinct monomials (-|xi|)^n, so a finite linear relation vanishes only when its polynomial vanishes. Consequently G is positive definite.

## Exact beta moments for canonical data

Write the first density mode as

    rho_1(r,theta)=r sum_j (1+r^2)^(-a_j) P_j(u) sin(theta),
    u=r^2/(1+r^2), a_j=(j+1)(1-1/c)/2.

Every f_n is a finite rational linear combination of (1+t)^(-p) with half-integer p. Products in H_i H_j and C_ij have integer powers. If C_ij=sum_k c_k(1+t)^(-k), then

    G_ij/pi=integral_0^infinity H_i(t)H_j(t) dt,
    B_ij/pi=-(1/2)sum_{j,k,l} c_k P_{j,l} Beta(l+2,k+a_j-2). (4)

The beta parameters must be positive for every term used. For positive integer m and rational q>0, Beta(m,q)=(m-1)!/[q(q+1)...(q+m-1)] is rational. Also integral_0^infinity(1+t)^(-k)dt=1/(k-1) for k>1. Thus both G/pi and B/pi are exact rational matrices, and T is exactly rational. All cancellations are performed before converting to interval arithmetic.

For n=0, H_0=(2-t)(1+t)^(-5/2), C_00=3(1-t)(1+t)^(-5), and G_00=3pi/4. These provide direct internal checks of the formulas. An exact rational LDL decomposition checks positive definiteness without relying on a floating condition number.

## Dependencies and status

Dependencies: the audited gradient-commutator identity, signed low-generator argument, elementary reflection projections, the displayed Poisson identity and beta integration. The present symmetry-budget theorem and its numerical applications are new and await independent T1/T2 review. Exact arithmetic alone does not independently audit the theorem. Any candidate-specific theta bound remains a separate full-plane input.
