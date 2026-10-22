# A smooth coefficient chart for a free-beta stream search

Written 2026-10-21T02:57:07.475194+00:00, before implementation. Status: representation and derivative identities proved below; no existence or nonexistence claim. This extends packet108 to a genuinely free beta and exact desingularized evaluation on the axis.

## Problem and representation

The target is B2-P on the full plane, with W=beta X+V, V=U-U(0), -Delta Psi=Omega, V=(-Psi_y,Psi_x), Theta even in x, Omega and Psi odd in x, Theta(0,y)=0, and a0=1. The fixed a0 uses the exact spatial scaling of the prompt; it does not fix beta. The search below restricts beta to a disclosed finite interval above2 and uses a finite trial space. Failure in that space excludes nothing in the full class. At integer beta it tests only the represented branches, not missing logarithmic tails.

Let R=sqrt(1+x²+y²), s=1/beta, u=2R^-s-1 and z=y/R. For finite indices i,j and shifts d in{0,1}, set

    p_ijd = x R^(1-s-d) T_i(u) T_j(z),
    psi_ijd = p_ijd - x partial_x p_ijd(0),
    theta_ijd = x² R^(-1-2s-d) T_i(u) T_j(z).

Then Psi=sum C_ijd psi_ijd, Theta=sum D_ijd theta_ijd and Omega=-Delta Psi. All basis fields are smooth for finite beta>2. Their x parity is exact, and V(0)=0 by the displayed determined subtraction. This is the stream function of the canonical relative inverse. It is not an independently fitted drift or the physical B1 condition U(0)=0. The raw velocity grows O(r^(1-s)) and Omega=O(r^-s). The full-plane relative Biot-Savart integral therefore converges; its difference from V is entire harmonic and sublinear, hence constant, and zero at0. This proves canonical relative inversion exactly for the analytic fields, as in packet108. Floating-point evaluation still needs its separate controls.

## A coefficient chart that is smooth in beta

Use the pivot stream basis functions (i,j,d)=(0,0,0) and(0,1,0), and the pivot temperature function(0,0,0). Direct Taylor expansion gives their columns in the stream center matrix (strain,b0):

    [[0,1],[-4(1-s),0]],

and the temperature a0 column is1. The determinant4(1-s) is nonzero for beta>2. Given every nonpivot C and D coefficient, solve this2x2 matrix for the two stream pivots to impose

    Psi_xy(0)=1+beta/2, Omega_x(0)=4a0/beta,

and solve the scalar temperature constraint for Theta_xx(0)/2=a0. The resulting coefficient map C=Cbase(beta)+Cmap(beta)c, D=Dbase+Dmap d is smooth in beta. Unlike an arbitrary numerically oriented null-space basis, this fixed-pivot coordinate chart has no sign or rotation ambiguity as beta varies. Direct evaluation of the original center rows, rather than only the elimination formula, will check its implementation.

## Exact removal of parity factors

In the implementation each term is a generalized monomial x^a y^b R^q, with integer nonnegative a,b and possibly noninteger q. Every term of V1 has at least one factor x, every term of Omega has at least one, and every term of Theta has at least two. The termwise division is an exact identity, not polynomial approximation. More intrinsically, writing Psi=x G(R,y), with G equal to the smooth cofactor minus its center value, gives V1/x=-partial_y G and Omega/x=-Delta G-2 G_R/R. Here Delta is the full Cartesian Laplacian and G_R is the partial derivative at fixed y. Divide these exact factors to define smooth functions

    A=beta+V1/x, B=beta y+V2, f=Theta/x², g=Omega/x.

These definitions extend to x=0 without numerical division. The defining PDE is equivalent off the axis to

    R_f=A(2f+x f_x)+B f_y-(beta-2)f,
    R_g=A(g+x g_x)+B g_y+g-(2f+x f_x),

and smoothness gives the exact axis limits. At the center A=(beta-2)/2, B=0, f=a0, g=4a0/beta, so both residuals vanish by the imposed constraints. The code must also record near-center and nonzero-axis residuals; checking the center alone does not certify the axis equations.

The pointwise normalizers are the sums of the absolute values of the three displayed R_f terms and four displayed R_g terms. If N=0, use ratio0 only if R=0; otherwise infinity. No denominator floor is allowed. Away from x=0, also evaluate the original Cartesian equations independently from the stream and temperature derivatives. Their absolute residuals matter separately.

## Coefficient derivatives and beta

At fixed beta, variations in stream coefficients give delta A,delta B,delta g, and variations in temperature coefficients give delta f. Differentiation of the displayed residuals gives

    delta_C R_f=delta A(2f+x f_x)+delta B f_y,
    delta_D R_f=A(2delta f+x delta f_x)+B delta f_y-(beta-2)delta f,
    delta_C R_g=delta A(g+x g_x)+A(delta g+x delta g_x)
                 +delta B g_y+B delta g_y+delta g,
    delta_D R_g=-(2delta f+x delta f_x).

These are exact derivatives of the raw finite-dimensional residual at fixed beta. In chart coordinates apply delta C=Cmap delta c and delta D=Dmap delta d. They do not differentiate the nonsmooth pointwise normalizers. The beta column will be a symmetric finite difference that rebuilds the basis, the center chart and any beta-dependent weights. It is a numerical approximation, not an exact derivative. Independent directional differences at two steps, and manufactured controls with a known zero, are required before the search. A fixed reference-beta envelope can be used in the optimization; pointwise diagnostic normalizers always use the actual beta and fields. Comparing objective values under different envelopes does not measure profile quality.

## Scope and planned evidence

Run several initial beta values and spatial resolutions; save all coefficient data as exact binary-rational JSON and retain original inputs and hashes. Report beta bounds reached, center errors, regional Cartesian and divided residuals, amplitudes, optimization history, and conditioning diagnostics where affordable. A small training objective is not acceptance. A finite angular basis cannot contain an exact admissible profile by packets83-84/lead4.24; it can still approximate one, and that exclusion provides no positive residual floor.

Dependencies: the prompt; packet108 analytic basis/inverse proof; direct polynomial differentiation and the elementary harmonic Liouville argument. No numerics-lane code is used. No JavaScript/TypeScript, servers/listeners, RLScience cluster, Lean/Lake, or GPU execution.

## Integer-beta basis dependence

At beta=m an integer, R^-1=(R^-s)^m=((u+1)/2)^m. Therefore every shift1 basis element whose radial index i satisfies i+m<ni is a linear combination of shift0 elements of the same angular index, by expanding ((u+1)/2)^m T_i(u) in Chebyshev polynomials. The same holds for both Psi and Theta, including the determined affine gauge because evaluation at the origin is linear. Thus the two-shift basis has exact coefficient kernels at these integer beta values and can have near kernels nearby. Smoothness of the center-elimination chart does not remove this separate representation dependence. A conditioning table must disclose it, and no claim that beta is well determined follows from convergence of an optimizer.


## Refinement after the written model review

At beta=m and with both shifts using i=0,...,ni-1, the radial kernel at each angular index has dimension max(0,ni-m). Indeed, after factoring the common nonzero term, a dependence is P(t)+t^m Q(t)=0 with polynomials P,Q of degree at most ni-1 in t=R^-s; Q must have degree at most ni-1-m. It therefore has exactly that many free coefficients. The shift conversion from u to t is invertible. The same exact identities vanish in the center rows and survive the fixed-pivot elimination. This is a lower bound for the kernel of the gauged stream basis: gauge subtraction can create further directions whose raw stream is exactly affine. At noninteger beta, a dependence of the two raw shift families would imply t^beta=-P(t)/Q(t). The order at t=0 of a nonzero rational function is an integer, which contradicts noninteger beta. Angular coefficients can be separated on an open (t,z) domain. This raw-family independence does not by itself establish independence after gauge subtraction.

The horizontal components U1 and V1 coincide by x-reflection, since U1(0)=0. Thus the review's claim that this particular constant need not vanish is incorrect; using V throughout is nevertheless clearer. The no-B1 distinction concerns the vertical component. The reviewed identities and qualifications do not approve a candidate.
