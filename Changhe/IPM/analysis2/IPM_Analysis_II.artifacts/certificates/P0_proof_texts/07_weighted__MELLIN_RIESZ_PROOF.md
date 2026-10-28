# Radial weighted Riesz bounds from the first-order complex derivatives

## Statement

Let B be the Fourier multiplier exp(2i arg xi) on the plane, with the value at xi=0 irrelevant. Let U=(-R1 R2,R1²), where Rj has multiplier i xi_j/|xi|. For R>0 and real beta write

    omega_(beta,R)(X)=(1+|X|²/R²)^(beta/2).

For arbitrary scalar functions take a=1 and |beta|<1. For centrally odd functions, f(-X)=-f(X), take a=2 and |beta|<2. In the respective class the canonical multiplier extends boundedly to the weighted L2 completion, and

    ||r^beta Bf||_2 <= (a+|beta|)/(a-|beta|) ||r^beta f||_2.       (1)

This pure-power bound is sharp in the indicated full angular class. For beta nonzero set

    H_a(beta)=2^(|1-|beta||/2) (a+|beta|)/(a-|beta|),
    C_a(beta)=(1+H_a(beta))/2.

Then, with the same domain restrictions,

    ||omega Bf||_2 <= H_a(beta) ||omega f||_2,
    ||omega U[f]||_(L2;R²) <= C_a(beta) ||omega f||_2.          (2)

At beta=0 use the exact constants1 for B and U. The bounds in(2) are not asserted sharp. They hold for every radius R with no radius-dependent factor.

Useful safely rounded consequences are

    beta=4/5, arbitrary f:       C_1(beta)<16/3;
    beta=4/5, centrally odd f:   C_2(beta)<9/5;
    beta=-1/5, arbitrary f:      C_1(beta)<3/2;
    beta=-6/5, centrally odd f:  C_2(beta)<8/3.                (3)

Thus the constants256 and2048 in the earlier weighted derivative proofs can be replaced by these smaller values whenever their stated input parity matches. In particular the top Hessian inputs D_ij h are centrally odd, whereas first derivatives of h are centrally even.

## Polar derivation of the pure-power bound

Put D_+=partial_x+i partial_y and D_-=partial_x-i partial_y. Their multipliers satisfy D_+/D_-=B. For a smooth compact input f use the canonical potential

    g=D_+ Delta^-1 f,

so D_-g=f and D_+g=Bf. This identity also fixes the behavior at infinity. The derivatives of g have the ordinary singular-integral interpretation, including any local term in B.

For an angular mode g_n(r) exp(in theta),

    D_-g=exp(i(n-1)theta)(g_n'+n g_n/r),
    D_+g=exp(i(n+1)theta)(g_n'-n g_n/r).

Set t=log r and g_n(r)=r^(-beta)v_n(t). The two weighted radial squared norms, after suppressing their common angular factor2pi, are

    int_R |v_n'+(n-beta)v_n|² dt,
    int_R |v_n'-(n+beta)v_n|² dt.                            (4)

For n nonzero the relevant boundary limits vanish. At the origin smoothness gives g_n=O(r^|n|); at infinity the canonical inverse gives the corresponding decaying modes. If f is arbitrary, the nonzero relevant n have |n|>=1, and |beta|<1 suffices. If f is centrally odd, g is centrally even, its nonzero n have |n|>=2, and |beta|<2 suffices. The far-field mean cancellation for a centrally odd compact input gives g=O(r^-2). These assertions also follow directly by expanding the kernel (X-Y)/|X-Y|² outside a disk containing the support. The compact-input case with support touching the origin follows by the same smooth expansion there.

For n=0 the two expressions before the substitution in(4) are identical. No integrability of v_0 itself is needed; this handles, in particular, a nonzero constant term of g at the origin. For n nonzero, one-dimensional Fourier transformation in t gives the squared ratio

    [tau²+(n+beta)²]/[tau²+(n-beta)²].                       (5)

The supremum over tau is max(1,|n+beta|²/|n-beta|²). Maximizing over both signs of n and over |n|>=a gives ((a+|beta|)/(a-|beta|))². Orthogonality of angular modes gives(1). Smooth cutoffs in t, increasingly long and slowly varying, with n having the maximizing sign and |n|=a, approach this ratio. They produce compact smooth annular inputs f=D_-g in the appropriate angular class. Hence the bound is sharp.

The argument initially applies to finite angular sums. Angular Fourier truncations converge in the radial weighted L2 norm. The uniform bound gives the extension, and agreement with the canonical Fourier multiplier follows by distributional convergence on test functions. Smooth compact functions away from the origin are dense in the weighted space. In the centrally odd case the extension is taken only on that closed parity subspace, and the zero-mean cancellation used above is preserved.

## From pure powers to a regular radial weight

It suffices to take R=1, since B commutes with dilations. For b=|beta|>0 set a_b(r)=(1+r²)^b and v_b(r)=1+r^(2b). Concavity for0<b<=1 and convexity for b>=1 give

    min(a_b,v_b) <= max(a_b,v_b)
        <=2^|1-b| min(a_b,v_b).                            (6)

The pure-power estimate and the unweighted bound||B||=1 imply the same bound(a+b)/(a-b) on L2(v_b dX), because the norm squared is the sum of its unweighted and pure-power terms. Applying(6) gives the first line of(2) for beta>0.

For beta<0 use duality. The adjoint of B on unweighted L2 is B^-1. Thus the norm of B on L2(omega^(-2)dX) equals the norm of B^-1 on L2(omega²dX). Reflection of the angular coordinate conjugates B and B^-1 and preserves both radial weights and central parity. The already established positive-beta bound therefore applies. This duality is inside the centrally odd subspace when that version is used. The radius R again follows by dilation.

## The velocity pair and its identity term

Let C=(B+B^-1)/2 and S=(B-B^-1)/(2i). Their symbols are cos2theta and sin2theta. The velocity multipliers are

    U_1=S/2, U_2=-(I+C)/2.                                (7)

For a real input, C f and S f are real, so

    ||omega C f||²+||omega S f||²=||omega Bf||².

For a complex input the left side is half the sum of the corresponding B and B^-1 squared norms, and obeys the same upper bound. By Cauchy-Schwarz and(7),

    4||omega U[f]||²
       =||omega f||²+||omega C f||²+||omega S f||²
          +2 Re <omega f,omega C f>
       <=(1+H_a(beta))²||omega f||².

This proves(2), with the local identity contribution in R1² retained. The arithmetic in(3) is independently checked at384-bit precision in `verification/mellin_riesz_constants.py` and its JSON output.

## Scope

These are weighted L2 operator bounds for the actual Riesz velocity, not coefficient bounds or inverse estimates. They are valid on the full weighted completions and do not require support on one annulus. The sharpness assertion concerns(1) on the full centrally odd class or unrestricted class; no sharpness is asserted on the narrower even-x, odd-y class or for the velocity pair. Replacing a constant in a subsequent energy theorem still requires recomputing that theorem's scalar inequalities.
