# Assembled report scope audit and a correction to the analytic corollaries

Status: the front matter, Sections3-10 and the exact earlier proofs cited below have been checked. This is not yet a certification of every line of the assembled report or its appendices. The immutable report snapshot and its real capture time are in the team records.

## 1. Setting and notation

The pressure and tail statements below concern 2/5<c<1/2, any finite real omega, U in C2(R3;R3), P in C1(R3), and

    div U=0,
    (1-c)U+DU(Ay+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1),
    A=cI-omega J, Jx=(-x2,x1,0), p=(1-c)/c.

Write Omega=curl U, B=Ay+U, H=P+|U|^2/2+(Ay).U, and let Pinf be the canonical pressure constant. The actual tails on D=R3 minus0 are V,W=curl V,P2, with k=(Ax).V and S=P2-|V|^2/2. Write Z=int_D{k=0}, V0=1_Z V and E0=supp(V0 restricted to S2). Let T0 be the supported unit-sphere points where V=DV=S=P2=0.

The smooth-vorticity corollary in Section6 needs only 2/5<=c<1/2, global C2 U and C1 P, the equation, decay and the stated helicity sign. It does not require these natural derivative bounds.

## 2. The Bernoulli pressure constant must be explicit

The profile equation and every velocity-based object are unchanged when a constant C0 is added to P. The quantities H and Pinf both increase by C0, whereas

    Q=P-Pinf-|U|^2/2, H-Pinf, grad H

are unchanged. The report defines the unnormalized H in Section0.2 and correctly uses H=Pinf on the regular nodal leaves in Remark7.1(i). Its Remark7.1(ii) subsequently writes H=Q=U.B=0 on critical leaves without changing this convention.

The pressure-independent statement there is

    H-Pinf=Q=U.B=0.

Alternatively the report may explicitly fix Pinf=0 before using H=0. Derivative and Hessian statements about H require no change. An arbitrary pressure shift demonstrates why an unannounced zero-value normalization is not a consequence of the equation. This is a correction to the formula and its proof scope, not an actual nonzero Euler counterexample.

## 3. Two different zero-set boundaries

The complete independent A1050-A1057 proof establishes

    boundary E0 subset T0,
    boundary Z subset {V=DV=W=0} intersect supp W.

The first inclusion is angular; the second is on D and can be restricted to the sphere. Its proof of S=0 is specific to boundary E0. If S is nonzero near such a point, the elliptic representation of the extended tangential field Y=|S|^eta grad f gives unique continuation from an open region where Y=0. This contradicts membership in its support E0.

At a point of boundary Z outside E0, that last contradiction is unavailable: V0 may already vanish on the entire neighborhood. Neither set definition nor A1053 establishes boundary Z subset boundary E0. Thus Remark7.1's statement that every boundary-Z point is in T0 does not follow from its cited theorem. It should be restricted to boundary E0, while retaining the independently proved V=DV=W=0 statement for boundary Z.

This audit rejects the inference, not the possible stronger theorem. Pressure vanishing at every remaining boundary-Z point is open at the stated baseline regularity unless an additional confirmed local hypothesis applies. For example, the later A1185-A1186 result covers a point with DW nonzero. No topological model is presented as an actual Euler counterexample.

## 4. The ambient meaning of local boundedness at the core

Let Xi:E -> D be the actual scattering diffeomorphism, K=R3 minus E its compact null core, and Gamma_s the complete original vortex flow. Define

    K_Omega={y in K: Gamma_s(y) in K for every real s},
    O=R3 minus K_Omega, F=S composed with Xi on E.

A736-A740 construct the unique C1 vortex-invariant extension Ftilde to O and prove Ftilde(Phi_t y)=exp(-2(1-c)t)Ftilde(y). The precise sufficient boundedness hypothesis is:

    For every z in K_Omega there are r_z>0 and M_z<infinity
    such that |Ftilde(y)|<=M_z for every y in O intersect B(z,r_z).

The same condition may be stated for F on E intersect B(z,r_z). Indeed E is dense, since K is null, and Ftilde is continuous on O; approximate each point of O intersect the ball by points of E. The bound then extends to Ftilde there. A slight radius reduction avoids the sphere boundary if necessary.

Compactness of K_Omega supplies a finite such cover. Continuity supplies a bound on the remaining part of each compact trapping ball. A nonzero Ftilde value would grow exponentially along the bounded backward carrier trajectory, a contradiction. Thus S=0 and the confirmed scalar pressure theorem gives U=0. The empty-core case uses continuity on the whole trapping ball directly.

By contrast, local boundedness only at points of E is automatic for the continuous F and gives no new criterion. Theorem7(d) is correct with the ambient boundedness interpretation above, which its statement should make explicit. This is a quantifier clarification, not a refutation of A740.

## 5. Runtime and two elementary statement repairs

The immutable draft was assembled at 2026-11-03T13:37Z. Its introduction calls itself the final report of a run ending 2026-11-04T17:05Z, a future time at capture. The scheduled team interval from November2 18:05:30Z to November4 17:05:30Z is47hours; the additional report-finalization hour makes the total48hour budget. A working report should state its actual assembly time and label the end times as planned. The final report must use the actual completed times. No elapsed runtime may be inferred from the future schedule.

Corollary5.2's phrase a nonzero profile as in Theorem5 formally retains Theorem5's sign assumption and hence has an empty antecedent. Its intended necessary statement concerns the equation, regularity and decay hypotheses of Theorem5 without its sign assumption. That exclusion should be explicit.

The theorem table's vorticity Lorentz condition must retain 1<=q<infinity when it quotes A054. The older c/4 smallness and isolated-leading hypotheses remain valid sufficient conditions, but the later confirmed improvements should be distinguished from open problems.

## 6. Smooth original vorticity already gives smooth velocity

Lemma. If U is a C2 vector field on R3, div U=0, and Omega=curl U is C-infinity on R3, then U is C-infinity on R3.

Proof. The vector identity curl curl U=grad div U-Delta U gives Delta U=-curl Omega in distributions and classically initially. Fix a ball B and a larger ball B1 with compact closure. Multiply the smooth right side by a smooth compactly supported cutoff equal to1 on B1. Convolve this smooth compactly supported function componentwise with the fundamental solution of Delta. The convolution is smooth: any derivative can be moved onto the compactly supported smooth factor, and the locally integrable fundamental solution defines the resulting convolution. Its Laplacian is the chosen right side. The difference from U is therefore distributionally harmonic on B1, and the harmonic mean-value regularity theorem makes it smooth there. Thus U is smooth on B. Since B was arbitrary, U is smooth globally.

Corollary. Let 2/5<=c<1/2, omega be any finite real number, and let U in C2 and P in C1 solve the exact profile equation, with U decaying. If Omega is globally smooth and U.Omega has one sign everywhere, then U=0. The same holds for one sign on each essential vortical basin, with signs allowed to differ. In particular it holds when Omega is globally real analytic and U.Omega=0.

Proof. The lemma supplies U in C-infinity. A308 supplies the essential basin domains, and the independently confirmed A309/A479 helicity-sign theorem applies with precisely its equation, decay, range and sign premises. No natural derivative rate, smooth tail, analytic scattering map, nodal condition or finite-order tail condition is needed.

This corollary is a direct use of an earlier stronger theorem, not a new independent proof of that theorem. Its foundational coverage and helicity-sign proofs are explicit dependencies.

## 7. Correction of the auditor's own earlier scope statement

A1170 and Section6 of in the team records incorrectly leave global original analyticity open in the helicity-free class. Section6 above settles that particular global hypothesis using the already confirmed smooth theorem. The local theorem A1168 and the conditional implication A1169 remain true. Their hypotheses are simply stronger than necessary when analyticity is global. Their proofs remain valid independent tail arguments.

Likewise, any corollary that assumes global smooth U and global zero helicity is already contained in A309 under decay. Additional all-order natural estimates, analyticity of Omega, or factorial bounds do not enlarge that class. The exterior-only smooth/factorial or quasi-analytic assumptions of A1193/A1195 are different: the compact original core is still only C2, so the global smooth theorem cannot be substituted without an additional argument.

Analyticity only near preimages of T0 need not imply global smooth U. The local analytic-original criterion A1165 retains its separate smooth-tail hypothesis, and local component-finiteness A1168 retains its exact region assumption. No original-to-tail analytic regularity is inferred.

## 8. Updated conditional frontiers

Theorem7(e)'s leading-isolation premise can now be removed by A1147-A1151 and the full LIT214 audit A1199. The sufficient condition is smooth V of finite first nonzero Taylor order at every point of T0. Degenerate finite leading terms are excluded by the repeated-factor pressure calculation, not left as a surviving branch. The regularity and helicity assumptions of Section1 remain.

The original statement that no hypothesis on U is known to imply finite tail order must be replaced by an exact scope statement. Uniform exterior factorial bounds give analytic V, and the larger log-convex quasi-analytic derivative class in A1192-A1194 excludes infinite-order supported zeros. Separate constants at each derivative order yield smoothness alone and do not supply that conclusion.

For bounded exact C2 profiles the improved exterior-vorticity argument A1171-A1175 replaces the factor2 by c_K<1.77963978. It proves derivative growth for every gamma>c_K W0. Its strict smallness gap is omega_inf<c delta_star/c_K, with delta_star=min(5/4,1/c,(1+kappa)/2) and kappa=1+c. The convenient bounded-velocity threshold is c/(2c_K); with natural velocity decay the threshold is1/(2c_K). These are strict sufficient conditions, not endpoint theorems or sharpness assertions.

## 9. Verification scope and pending complete text audit

The immutable front and Sections3-10 were read. The full scalar-core proof A736-A740, the boundary-of-support argument A1050-A1057, the analytic-original proofs A1163-A1170, and the exact statements and prior proof audits A308-A309/A479 were reread for these findings. Sections2A-2D and all appendices of this snapshot require the separate complete-text pass; previous audits of earlier versions do not silently certify their current contents.

No computation, formal build, new external model client, outside-agent edit or publication has been performed. The coordinator's existing configured model agent is asked to compare these corrections through the agent notes. Actual provider runtime remains unattested. The arbitrary-helicity bare-decay conjecture is still open.
