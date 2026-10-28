# Clarifications forming part of the V239 proof

The full independent audit is preserved in evidence/xaudit_V239_V240.md. Every finding has been checked independently. The proof's statements remain valid with the following explicit conventions and details.

1. The point Q and its small flow box are distinct objects. Require V1(Q) != 0 and (V.grad chi)(Q) != 0 at an off-axis point in a smooth region. Every general noncompactness statement and the concluding scope sentence use this hypothesis. No genericity assertion or statement about cancellation in a sum of patches is made. The sequence also witnesses noncompactness of the graph embedding localized by V.grad chi. The ordinary annular lower bound, when |Q| >= 1, is 2 R_j^(alpha-beta)|V.grad chi(Q)|/pi^alpha for an annulus containing Q in its interior. The local factor gives the stated E2 bound for |Q|<2; these alternatives overlap.

2. Write Sigma for a fixed compact set containing all packet supports and the correction q. It is separated from the axes. In (1) C_K means C_Sigma, distinct from the patch operator K. The constants depend on this set and the fixed cutoffs. Intermediate annuli in the commutator proof are finite in number; the global ordinary C^alpha bound of W and bounded Lipschitz grad rho0 control each. At large radii integrate derivative bounds along annular paths of length comparable to the point separation, or split close and distant pairs using enlarged annuli and the supremum. This proves the claimed R^(k-4) scaled bound. Its weighted integrability needs only gamma>2k-6, which follows from gamma>4k.

3. In the patch section denote the exact full-column extension by L_delta^M=V_delta.grad-1+B_delta^M, where B_delta^M u=chi_*(X/delta){U[u].grad rho0+c[u]M0}, and chi_* equals one on B_(1/2) and vanishes outside B1. This is proof 217's A_delta. Its inverse is R_delta. Choose supp chi compactly contained in the open B_(delta/2), eta equal one on the closed B_delta and supported in B2. Then V_delta=V and chi_*=1 on a neighborhood of supp chi. The displayed identity is V_delta.grad u=u+eta f-B_delta^M u. The local and full expressions agree there for every E2 input. All patch mapping and maximal-domain arguments use this full coupling. The exact support gives eta f_n=f_n and chi eta=chi, so the error is also A0K-chi.

4. The integration-by-parts estimate for c[u_n] is valid to every order because the smooth amplitude is compact in the transverse variable. Only c[u_n]->0 is required. The correction can be a compact reflected bump off the axes and boxes with nonzero strain, divided by that strain. No annular set disjoint from its coordinate axes is asserted.

5. A graph-bounded K with ||A0K-I||<1 supplies the right inverse K(I+A0K-I)^(-1), hence onto only. A lower bound or left inverse is separately needed for injectivity. Neither this proof nor the audit establishes a global inverse, a middle-annulus estimate, or compactness/noncompactness of a complete sum of patches. The later proof 227 is a separate range obstruction.

No optional numerical sanity check in the audit is used as a certified number. Proof 222's original audited hash has since changed only through V244's explicit clarifications; evidence/check.json records that dependency history.

Recorded 2026-10-28T15:33:00.633736+00:00.
