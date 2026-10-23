# A qualitative residual floor under fixed compactness bounds

Status: CONFIRMED, 2026-10-23T07:22:03.609291+00:00. Complete informal proof. This checks lead THEORY_NOTES.md section 8 after Theorem L2 removed the previous stagnation-margin assumption. It supplies no numerical value for the floor.

## Exact statement and notation

Fix 0<c<1/2 and K>=1. Set d=1-1/c and <y>=(1+|y|^2)^(1/2). Use Euclidean vector norms and Hilbert-Schmidt derivative tensor norms. Consider U in C3(R3;R3) with

    div U=0,
    |D^j U(y)| <= K <y>^(d-j), j=0,1,2,
    ||D^3 U||_infinity <= K,
    ||D^2 U||_infinity = 1.

There is epsilon_0(c,K)>0 such that for every such U and every P in C1(R3),

    ||(1-c)U + DU(cy+U) + grad P||_infinity >= epsilon_0(c,K).

The assertion is vacuous if the class is empty. It is a lower bound for this global absolute residual norm under fixed class bounds, not for any finite-grid or term-normalized loss. No symmetry, stagnation-set condition, pressure bound or pressure gauge is required. The only theorem dependency is the exact C2 sublinear obstruction proved in ../uncountable-stagnation/PROOF.md.

## Proof

Suppose no positive epsilon_0 exists. There are U_n in this class and P_n in C1 with residual R_n tending uniformly to zero. The derivative bounds make U_n, DU_n and D2U_n uniformly bounded and equicontinuous on every compact ball: the D3 bound gives a common Lipschitz bound for D2. Arzela-Ascoli and a diagonal subsequence give U_n -> U in C2 on every compact set. The limit is C2 and divergence free, and all three pointwise envelope bounds pass to U. Because d<0, U tends to zero at infinity.

The normalization survives. Put R_N=(2K)^(1/(2-d)). For |y|>=R_N, negativity of d-2 gives

    |D2U_n(y)| <= K |y|^(d-2) <= 1/2.

Each continuous D2U_n therefore attains its global norm 1 inside the fixed compact ball of radius R_N. Uniform convergence there gives max |D2U|=1. In particular U is not zero or affine.

To reconstruct pressure, set F_n=(1-c)U_n+DU_n(cy+U_n) and F=(1-c)U+DU(cy+U). The C2 convergence implies F_n -> F in C1 on compact sets. Since F_n=R_n-grad P_n, curl F_n=curl R_n in distributions. Uniform residual convergence implies curl F=0. As F is C1, this identity holds pointwise.

An explicit global pressure is

    P_*(x) = -integral_0^1 F(tx).x dt.

Indeed differentiation in x_j and equality partial_j F_i=partial_i F_j turn the derivative of its integrand into d/dt[t F_j(tx)]. Thus partial_j P_*=-F_j(x). Since F is C1, P_* is C2. The pair (U,P_*) solves the exact incompressible profile equations globally and U decays. The exact obstruction gives U=0, contradicting ||D2U||_infinity=1. This proves existence of epsilon_0.

## Why deleting all fixed second-derivative continuity control fails

Choose a nonzero smooth compactly supported divergence-free W with ||D2W||_infinity=1. Such a W is obtained by taking the curl of a nonconstant compactly supported smooth potential and scaling its amplitude. For 0<ell<=1 set U_ell(y)=ell^2 W(y/ell), P_ell=0. Then

    DU_ell=ell DW(y/ell),
    D2U_ell=D2W(y/ell),
    D3U_ell=ell^(-1) D3W(y/ell).

For a fixed sufficiently large K, the three weighted bounds through order two hold uniformly: all supports lie in one fixed ball and the three amplitudes are bounded. The curvature norm stays exactly one. With x=y/ell, the residual is

    R_ell(y)=ell^2[(1-c)W(x)+c DW(x)x] + ell^3 DW(x)W(x).

It tends to zero uniformly as O(ell^2). D2U_ell has no common modulus of continuity and D3 diverges. Thus uniform C2 bounds without equicontinuity of D2 do not establish the stated floor. This does not mean that a D3 bound is the only possible hypothesis: a prescribed local modulus for D2, including a common Holder seminorm, gives the same compactness proof.

## Extensions and limits

A joint positive floor holds for ||R_m||_infinity+||div U||_infinity when exact divergence freedom is omitted from the class. If their sum tended to zero, the same limit would be divergence free and the same contradiction applies.

One may replace curvature norm equality by any fixed positive lower bound while retaining the upper envelopes and localization argument. Under exact Euler spatial scaling U_a(y)=a U(y/a), D2U_a=a^(-1)D2U(y/a), so curvature normalization is a legitimate scale choice for a non-affine field with finite nonzero curvature. It does not normalize vorticity amplitude freely.

For c varying in a compact subinterval of (0,1/2), the same proof uses a convergent subsequence c_n -> c_* and uniform negative tail exponents. It fails to give a uniform floor as c approaches 1/2 or as K diverges. A finite set of sampled derivative maxima does not certify the global K bounds. A decreasing residual may approach a positive floor; it does not by itself imply degeneracy or force a free exponent to increase.

## Verification evidence and provenance

The supplied floor1 report, archived at ../../snapshots/floor1-f4c73485061e3f4b.md, proved the compactness argument with an extra uniform stagnation margin using the earlier countable-zero theorem. The present proof uses L2 and drops that margin. Lead section 8 and the independent proof above agree. See ../../THEORY_V3_AUDIT.md and ../../FLOOR_AUDIT.md. No numerical tolerance, novelty, exact profile construction, stability result, or blowup conclusion is asserted.
