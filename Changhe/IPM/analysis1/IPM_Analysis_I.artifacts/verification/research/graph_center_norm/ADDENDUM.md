# Explicit constants and the normalization consequence

2026-10-21. Read with PROOF.md and REVIEW_RESOLUTIONS.md. These additions do not change any hypothesis or make a claim about an actual retained matrix.

Let p=3/2-k>0 and choose

    C_w=L^6(1+L^(-2))^p.

For r<=1, w=L^6 r^(-6)(1+r^2/L^2)^p <= C_w r^(-6). For r>=1, use 1+r^2/L^2<=r^2(1+L^(-2)) to get w<=C_w r^(-2k-3). No restriction on the relative size of L and1 is needed.

The exact polynomial computations give constants

    S0=729, S1=8019, S2=84078,
    C_H=693689/84,

such that |H|<=S0 r^3, |grad H|<=S1 r^2 and |D2 H|<=S2 r on the unit disk. Each coefficient sum is taken in Cartesian monomials. A monomial of degree d>=q has absolute value at most r^d<=r^q there. The sums of absolute first and second derivative coefficients dominate their Euclidean norms. The same reasoning bounds the operator norm of DW by C_H. Since W(0)=0, integration along the segment from0 toZ gives |W(Z)|<=C_H |Z|.

Outside the unit disk the stream coefficients are exactly

    psi_2=-(1/4032)r^(-2),  psi_4=-(1/13440)r^(-4).

A harmonic mode c r^(-n) sin(n theta) has gradient norm n|c|r^(-n-1) and Hessian operator norm n(n+1)|c|r^(-n-2). This follows by writing it as the imaginary part of a constant multiple of the holomorphic function z^(-n); the real Hessian is traceless and its two eigenvalues have the magnitude of the second complex derivative. Thus the sums 1/1260 and1/336 bound the respective exterior velocity and derivative constants. Both are below C_H. The radial stream functions match through derivative6 at1. Their Cartesian representations and exterior harmonic modes therefore give at least C2 stream regularity across the circle, which is more than needed for continuity of W and DW.

Explicit sufficient constants in the original bounds are

    ||h_delta||_X <= (S0+S1)sqrt(pi C_w) delta,
    C1=[B(2S1+S2)+S0+S1]sqrt(pi C_w),
    C2=3 C_H sqrt(2pi C_w [A^2/(2alpha)+A^2/(8-2alpha)+D^2/9]),
    ||G||_X <= 3sqrt(2pi C_w [A^2/(2alpha)+D^2]).

For the first two bounds use |F|+r|grad F| and integrate r over(0,delta). For Q_delta the sum |Q_delta|+r|grad Q_delta| is bounded by three times the relevant product of constants in each region. Its squared sum dominates Q_delta^2+r^2|grad Q_delta|^2. Integrating the three radial powers in PROOF.md gives C2. The replacement delta^12<=delta^(4+2alpha) uses delta<=1 and alpha<1. No uniform constant as alpha tends to0 is claimed. These constants are exact expressions in assumed background constants; they do not enclose those constants for a numerical profile.

There is a useful consequence that does not require a kernel. On a linear domain D_L with the hypotheses of PROOF.md, for a fixed finite C the inequality

    ||h||_X <= C||Lh||_X

holds for all h with J(h)=0 if and only if it holds for all h in D_L. The reverse implication is restriction. For the forward implication, apply the inequality to h-J(h)h_delta and pass to the limit in both X norms using graph convergence. Consequently the algebraic condition J=0 cannot reduce the best constant for this specific estimate in this graph topology. This does not concern a graph domain given a stronger topology, a stronger image norm, a factor norm or an additional closed constraint.

For K in D_L, the same limit gives the necessary bound ||K||_X<=C||LK||_X. If LK=0 and K is a nonzero X equivalence class, the inequality fails. If an independently proved scaling identity gives LK=epsilon-X dot grad epsilon at a trial and the image norm is positive, the necessary lower bound on C is ||K||_X/||epsilon-X dot grad epsilon||_X. This is conditional on membership and on the identity. No quotient for the actual profile is evaluated here.
