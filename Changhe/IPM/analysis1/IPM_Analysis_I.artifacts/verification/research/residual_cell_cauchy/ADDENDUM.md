# Pre-computation clarifications and review resolutions

Dated 2026-10-21, before any cell derivative computation.

The only selected cells are 4102, 4125 and 4211. The thirteen-point result supplies the input certificates; this extension will not claim thirteen-cell coverage. For 1<=n<=261, write H_{n-1,q} and H_{n,q} for coefficients in z. The recurrences in PROOF.md mean

    (q+1) I_{n,q+1} = h[-(2n+4)I_{n,q}+H_{n-1,q}],
    (q+1) J_{n,q+1} = h[(2n-4)J_{n,q}-H_{n,q}],

with H_261 identically zero. The accepted point preparation already checks knots[span]<=l<t_c<r<=knots[span+1] and the exact midpoint equality. Repeat those inequalities here and pin that preparation.

For the independent density computation it is economical to set K_n=exp(2t)I_n and M_n=exp(2t)J_n. Direct differentiation gives

    K_n'=-(2n+2)K_n+exp(2t)H_{n-1},
    M_n'=(2n-2)M_n-exp(2t)H_n.

Thus the scaled coefficient recurrences replace their right sides by h times the displayed expressions and divide by q+1. The full velocity coefficients are

    p_n=-n(M_n-K_n),
    q_n=[2n(M_n+K_n)-exp(2t)(H_{n-1}+H_n)]/2.

These weighted density moment ODEs are algebraically equivalent to the I/J equations and retain the independently inherited I/J center boxes. The physical calculation uses the A/B Green ODEs and their forcing, with ordinary ball polynomial exponential convolutions. Neither calculation imports the other's jets.

Finite Taylor bounds use max(abs(lower),abs(upper)) of each coefficient box, or of a proved overlapping intersection. Any disjoint comparison is a hard failure. The two methods will compute their own disk majorants. Retain all positive factors, including h^(-i), with outward rounding. The fixed radius4 and degree64 are selected before computation, and the initial disk-majorant and tail magnitudes are recorded before polynomial multiplication. A large bound is reported honestly; no radius or degree tuning is hidden.

The proof reviewer correctly requested explicit recurrence indices and output obligations. Its statement that the earlier certificate checked only the center was factually incorrect: research/residual_point_jets/code/check_preparation.py already has the full cell-in-span assertion. Its mathematical conclusion remains conditional on completed arithmetic. This addendum makes no numerical certificate claim.
