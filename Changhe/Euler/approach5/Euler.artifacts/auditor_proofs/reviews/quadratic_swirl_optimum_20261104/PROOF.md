# Exact pressure optimum for a fixed quadratic swirl

Status: CONFIRMED A2702-A2703; scope OPEN A2704. Complete source and independent reconstruction read; existing coordinator comparison completed.

## 1. Exact statement

Set rho^2=x^2+y^2, Q=z(-y,x,0), and E=|Q|^2=rho^2 z^2 on R3. Among all real homogeneous quartic polynomials P with

    -Delta P=tr((DQ)^2),

and all real gamma satisfying P>=gamma E everywhere, the largest gamma is

    gamma_ax=(6-sqrt(30))/24.

It is attained by

    P_star=a rho^4+b rho^2 z^2+d z^4,
    a=(sqrt(30)-5)/160,
    b=(5-sqrt(30))/20=-8a,
    d=(sqrt(30)+5)/60=(1+16a)/6.

The conclusion applies even if an initially admissible P has no rotation symmetry. The pair is a kinematic Poisson pair, not a stationary or similarity Euler pair.

## 2. Reduction without assuming pressure symmetry

Direct differentiation gives

    DQ=[[0,-z,-y],[z,0,x],[0,0,0]],
    div Q=0, tr((DQ)^2)=-2z^2.

Thus the equation is Delta P=2z^2. Average P over all rotations in the xy-plane. The source and E are rotation invariant, and the Laplacian commutes with these rotations. The average is a homogeneous quartic polynomial satisfying the same equation and inequality. Conversely, each rotation-invariant admissible polynomial is among the original admissible polynomials. Hence this averaging does not change the optimal gamma.

A planar rotation-invariant homogeneous polynomial of degree k restricts to a constant on the unit circle and so equals a multiple of rho^k away from zero. It can be a polynomial only for even k unless it is zero. Expanding a homogeneous quartic in powers of z therefore gives precisely

    P_bar=a rho^4+b rho^2 z^2+d z^4.

The three Laplacians are 16rho^2, 2rho^2+4z^2 and 12z^2. Matching the equation yields b=-8a and d=(1+16a)/6. Only pressure was averaged; averaging velocity would not preserve the quadratic source or E and is not used.

## 3. Exact nonnegative-quadrant condition and maximization

At z=0 the inequality forces a>=0. At rho=0 it forces d>=0, already automatic from a>=0. For a>0 let u=rho^2 and v=z^2. The defect equals

    a u^2+(b-gamma)uv+d v^2.

It is nonnegative for all u,v>=0 exactly when gamma<=b+2sqrt(ad). Sufficiency follows by completing the square. Necessity follows by choosing u/v=sqrt(d/a) with v>0. At a=0 the defect is -gamma uv+v^2/6, so its optimal gamma is zero. Thus the full optimization is that of

    F(a)=-8a+2sqrt(a(1+16a)/6), a>=0.

For a>0,

    F'(a)=-8+(1+32a)/sqrt(6a(1+16a)).

Both sides of the critical-point equation are positive before squaring. Squaring is therefore reversible and gives 5120a^2+320a-1=0. Its unique positive root is a_star=(sqrt(30)-5)/160. The derivative is positive near zero and continuous with just this one zero. Also F(a) tends to minus infinity because its linear asymptotic coefficient is -8+8/sqrt(6)<0. Consequently a_star is the unique global maximizer, including the boundary a=0.

At this root d_star=(sqrt(30)+5)/60, a_star d_star=1/1920 and 2sqrt(a_star d_star)=sqrt(30)/120. Substitution gives F(a_star)=(6-sqrt(30))/24. Moreover

    P_star-gamma_ax E
      =(sqrt(a_star)rho^2-sqrt(d_star)z^2)^2.

This identity proves attainment and nonnegativity on the axes as well as away from them. The averaging reduction proves optimality against every quartic pressure for this Q, not only symmetric pressures.

## 4. Consequence for the all-quadratic constant and exact limitations

The unit-sphere averages satisfy <z^4>=1/5 and <x^2z^2>=1/15. Indeed z is uniform on [-1,1] under normalized sphere area, and expanding (x^2+y^2+z^2)^2=1 with rotation symmetry gives the mixed moment. Hence <E>=2/15.

Set Q_normalized=sqrt(15/2)Q and P_normalized=(15/2)P_star. Their energy mean is one; both sides of the Poisson relation scale by 15/2 and the pressure ratio is unchanged. They are therefore feasible in the compact problem defining Gamma2 in the smooth-threshold proof, so

    Gamma2>=gamma_ax>1/60, gamma_ax<1/6.

The strict lower comparison follows from sqrt(30)<28/5, and the upper one from sqrt(30)>2. Neither Gamma2<=1/6 nor global optimality of this velocity follows.

For every c and omega, at (0,0,z) with z nonzero the field Q vanishes, its derivative along the axial dilation vanishes, the rotation vector Jx vanishes, and Q's nonlinear transport vanishes. Every velocity term in the rotating similarity equation is therefore zero there. But grad P_star=(0,0,4d_star z^3) is nonzero. Thus this pair satisfies neither that equation nor stationary Euler. It also grows at infinity. It cannot be a counterexample to the campaign's decay-only conjecture.

## 5. Dependencies and verification boundary

The proof uses direct polynomial differentiation, integration over planar rotations, an elementary square identity, one-variable differentiation and sphere moments. These are reproduced completely above. No floating optimization, nonnegative-polynomial theorem or numerical experiment is a proof dependency. No mathematical computation, formal build or model client was run for this audit. The existing configured model comparison is pending; actual provider runtime remains independently unattested.

## 6. Completed existing coordinator comparison

All eight coordinator items and the complete shared check log were read. The source hash matches the pinned snapshot. The averaging argument changes pressure only, the one-variable nonnegativity condition includes a=0, and the positive critical root is unique. Exact algebra verifies a_star d_star=1/1920, gamma_ax=(6-sqrt(30))/24 and the square defect. The sampled curve values in the supplied log are unnecessary for the maximum proof. The observation that the displayed LIT317 pressure itself has a somewhat larger bound than 1/60 is consistent with LIT317 making only that weaker claim.

The all-quadratic constant receives a lower bound only. A better velocity, such as a separately audited poloidal-swirl candidate, cannot refute this fixed-Q optimum. No discrepancy was found. Existing configured model file collaboration is completed; actual provider runtime remains independently unattested.
