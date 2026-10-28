# The unweighted potential pairing cannot be positive at the S2 saddle

Status: analytical identity and scoped counterexample proved below. These are obstructions to one energy method, not to invertibility or profile existence.

## Statement

Let rho and U[rho] be C^1 near the supports used below, with div U[rho]=0, and put V=ell X+U[rho]. For a real compact smooth potential phi, let h=-Delta phi. Its canonical stream is psi[h]=partial_x phi, because -Delta(partial_x phi)=partial_x h and this stream has decaying velocity and the prescribed symmetry. Hence U[h]=(-phi_xy,phi_xx). Define the fixed-scalar linearization

    L_0 h=V.grad h-h+U[h].grad rho.

Then

    -integral (L_0 h)phi dX=integral grad(phi)^T M(X)grad(phi)dX,
    M=(1+2ell)I+sym(DU[rho])
        + [[rho_y,-rho_x/2],[-rho_x/2,0]].                 (1)

If rho has zero first derivatives at zero and c[rho]=3ell-1, then

    M(0)=diag(2-ell,5ell).                                 (2)

For ell>2, the quadratic form in (1) takes strictly negative values on compact smooth even-x, odd-y potentials supported away from both axes. Their densities h have a smooth factor x^2y b, vanish near zero, and satisfy J(h)=c[h]=0. The same negative pairing therefore holds for the full normalized linearization on these tests. There cannot be a positive lower bound of this particular pairing by a positive multiple of integral |grad phi|^2 on a domain containing the tests.

## Proof of the identity

Since div V=2ell, integration by parts gives

    -integral(V.grad h)phi
       =integral h(V.grad phi+2ell phi).

Substitute h=-Delta phi. The term containing V is

    integral grad(phi)^T DV^T grad(phi)
      + (1/2)integral V.grad(|grad phi|^2).

The second term is -ell integral |grad phi|^2, and the 2ell phi term gives +2ell integral |grad phi|^2. Thus the total transport contribution is integral grad(phi)^T(2ell I+sym DU)grad(phi). The term +integral h phi supplies one more identity matrix.

Divergence freedom of U[h] gives

    -integral U[h].grad rho phi
      =integral rho(-phi_xy phi_x+phi_xx phi_y).

Integrating the first term in y gives (1/2)integral rho_y phi_x^2. Integrating the second term in x gives -integral rho_x phi_x phi_y-integral rho phi_x phi_xy; integrating this last expression in y gives the other half of integral rho_y phi_x^2. This is exactly the last matrix in (1). All boundary terms vanish by compact support.

At zero, DU=diag(-c,c) by parity. Substitute c=3ell-1 and grad rho(0)=0 to obtain (2). For a held scalar with defect, the actual matrix is instead diag(1+2ell-c,1+2ell+c).

## Actual parity-compatible negative tests

By continuity and ell>2, choose a small rectangle Q in the first quadrant, bounded away from both axes, where M_11<=-eta<0. Let b be a nonzero real C_c^infinity(Q). Set phi_N=N^{-1}b cos(Nx) on Q and reflect evenly in x and oddly in y onto the other three quadrants. The supports are disjoint, and the reflected coefficients of M transform so that the four quadratic integrals agree when rho has the S2 parities. Alternatively choose Q and its reflections all sufficiently close to zero that M_11<0 on each; bounded off-diagonal and M_22 entries suffice.

On each support, phi_{N,x}=-b sin(Nx)+O(N^{-1}) and phi_{N,y}=O(N^{-1}), with uniform L^2 bounds for the error. Therefore the energy tends to (1/2)integral M_11 b^2, summed over the reflected supports, which is negative. The oscillatory cos(2Nx) term tends to zero: approximate the integrable coefficient M_11 b^2 in L^1 by smooth compact functions and integrate those by parts. This proves negativity for all sufficiently large integers N.

Every phi_N vanishes near zero and both axes. Thus h_N=-Delta phi_N does too and divides smoothly by x^2y after extension by zero across these neighborhoods. Its canonical strain is c[h_N]=phi_{N,xxy}(0)=0. Consequently the rank-one term in L contributes nothing, and the construction applies to the complete normalized expression as claimed.

## Limits of constant anisotropic potential weights for the frozen transport

A useful additional calculation concerns the pure frozen operator T h=BX.grad h-h with B=diag(b_1,b_2). Let m(xi)>0 be C^1 off zero, even in both frequency coordinates, homogeneous of degree -2, and comparable to |xi|^{-2}. Give compact smooth potentials the energy E_m(h)=integral m|hat h|^2 with h=-Delta phi. Suppose m is smooth enough that Bxi.grad m is bounded by a constant times m; this holds for any positive smooth angular weight. Fourier integration by parts yields

    -Re integral m Fourier(T h) conjugate(hat h)
      =integral m [1+tr(B)/2-(Bxi.grad log m)/2]|hat h|^2. (3)

Indeed Fourier(T h)=-Bxi.grad hat h-(tr B+1)hat h. Integrate the directional derivative against m and collect the divergence tr B. On the horizontal frequency axis, homogeneity gives Bxi.grad log m=-2b_1, so the coefficient in brackets is

    1+tr(B)/2+b_1.

For the normalized S2 saddle, b_1=1-2ell, b_2=4ell-1 and tr B=2ell. This value is 2-ell<0. By continuity it remains negative in a cone around the horizontal axis. Thus a fixed positive smooth angular modification of an order-minus-two potential energy cannot make the pure frozen transport energy uniformly positive.

For a direct test with the S2 axis factor, use the same compact potential phi_N above and h_N=-Delta phi_N. Its Fourier transform is a finite sum of shifted Schwartz transforms multiplied by |xi|^2/N. Changing variables to each carrier frequency and using rapid decay shows that its normalized energy in (3) concentrates at the horizontal directions. Contributions near xi=0 cause no singularity because |xi|^4 m=O(|xi|^2). The terms from distinct carrier frequencies vanish by rapid decay. The quotient of (3) by E_m tends to 2-ell. This supplies axis-compatible tests without using a function supported exactly on a frequency axis.

This last result is about constant homogeneous Fourier weights and the pure frozen transport. It does not classify variable matrix weights, stronger orders, cross energies with additional variables, or inverse estimates obtained without a positive energy identity.

## Dependencies and scope

The proof uses integration by parts, elementary Fourier differentiation and rapid decay of Fourier transforms of compact smooth functions. No numerical data are needed except to place a chosen ell above two. The full nonlinear PDE and all possible alternative symmetrizers remain outside the conclusion.
