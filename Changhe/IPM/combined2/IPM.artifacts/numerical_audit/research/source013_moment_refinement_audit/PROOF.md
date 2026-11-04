# Independent check of the source013 moment refinement

## Statement and hypotheses

Keep the exact residual F_013, c=4076476460239181/2251799813685248, and W(X)=sqrt(1+4|X|^2) of the fully admitted whole-plane certificate in ../source013_norms/results/whole_plane/PROOF.md and its verification/ACTUAL_REVIEW_v01.md. Let g=WF_013 belong to H^3(R^2), with the unitary Fourier convention of that certificate. The symbol D^j denotes the complete ordered Cartesian derivative tensor, so

    T_j=||D^j g||_2^2=integral |xi|^(2j)|g_hat(xi)|^2 dxi.

Let [L_j,U_j] be its certified rational moment intervals, j=0,1,2,3. If Q is a nonnegative rational with Q^2>=U_0 U_2, replacing U_1 by min(U_1,Q) preserves containment. Put

    B_m^- = sum_(j=0)^m binom(m,j) L_j,
    B_m^+ = sum_(j=0)^m binom(m,j) U_j_new.

Then sqrt(B_m^-)<=||g||_(H^m)<=sqrt(B_m^+) for 0<=m<=3. When B_1^+>0,

    max(sqrt(B_2^-), ((B_2^-)^11/B_1^+)^(1/20))
        <=||g||_(H^(21/10))<=((B_2^+)^9 B_3^+)^(1/20).

The zero g case is interpreted separately and has all norms zero. This audit checks the specific exact rational and displayed endpoints proposed in theory_audit/research/source013_moment_refinement, against the original numerical auditor's moments, without executing the other auditor's code.

## Complete argument

Fourier Cauchy-Schwarz applied to |g_hat| and |xi|^2|g_hat| gives T_1^2<=T_0 T_2. Thus Q bounds T_1 whenever Q^2>=U_0 U_2. This is a whole-plane Fourier identity. It requires no integrations by parts on separate radial panels and discards no boundary terms.

The binomial theorem applied to (1+|xi|^2)^m gives the integer Bessel energies. Holder interpolation at 21/10 between orders 2 and 3 gives the displayed upper twentieth-power inequality. Interpolating order 2 between orders 1 and 21/10, with interpolation parameter 10/11, gives B_2<=B_1^(1/11) B_(21/10)^(10/11), and hence the displayed lower twentieth-power inequality. Monotonicity supplies the lower square-root inequality.

The independent checker reads the already admitted original moment record. It verifies every unchanged endpoint exactly, checks the new rational Q by squaring, reconstructs all four binomial energies, and compares them with the proposed exact record. It checks each exact and printed endpoint through rational square or twentieth-power inequalities. A lower fractional endpoint is valid if either of the two independent lower inequalities proves it. Its source, weight, order and original actual-review binding must agree. Exact arithmetic here authenticates a consequence of previously admitted containing intervals; it is not a new quadrature certificate.

## Dependencies and scope

The source and regional containment hypotheses are inherited exactly from the whole-plane source013 result. AT1418-1420 provide the independent mathematical proposal; this audit supplies a distinct arithmetic implementation. The original wider intervals stay true. The calculation changes no coefficient, parameter, weight or residual. It supplies no P-S2, global Holder S_F, background, near/far operator, inverse, invariant ball or stationary existence assertion. No Lean formalization or build is used. The check result, immutable inputs, hashes and actual times will be retained in verification/.
