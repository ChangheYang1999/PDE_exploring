# Far-field derivation extract for the 860-generator handoff

Prepared2026-10-23 from the earlier read-only audits; source identities are in [the provenance record](../../metadata/farfield_derivation_provenance.json). This portable note contains the mathematical deductions needed for the next experiment. It is not a copied old optimization recommendation. The newly agreed [research plan](../NEXT_RESEARCH_PLAN_860.md) supersedes any earlier proposal to hard-match far-field coefficients before enlarging the basis.

## Formal ladder and first three conditions

Let \(\gamma=1/c_l\), \(\lambda=1-\gamma>0\), \(\alpha_j=\gamma-j\lambda\).
Assume a differentiated asymptotic expansion
\(\rho\sim\sum_jr^{\alpha_j}F_j(\theta)\),
\(\psi\sim\sum_jr^{\alpha_j+1}\Phi_j(\theta)\), with adequate remainder and canonical-inverse control. This is an assumption for the following necessary identities, not a theorem that every exact profile has the expansion.

Since
\[
U_r=-\psi_\theta/r,\quad U_\theta=\psi_r,\qquad
U\cdot\nabla\rho=(\psi_r\rho_\theta-\psi_\theta\rho_r)/r,
\]
and
\(\partial_x(r^\alpha F)=r^{\alpha-1}(\alpha\cos\theta F-\sin\theta F')\),
the Poisson equation gives
\[
-\Phi_j''-(\alpha_j+1)^2\Phi_j
=\alpha_j\cos\theta F_j-\sin\theta F_j'.
\]
Symmetry requires \(F_j(0)=0,\ F_j'(\pi/2)=0,\ \Phi_j(0)=\Phi_j(\pi/2)=0\).
F has odd sine harmonics; Phi has even sine harmonics.

The identities
\(\alpha_i+\alpha_j-1=\alpha_{i+j+1}\) and
\(c_l\alpha_N-1=-N(c_l-1)\) give
\[
\mathcal E_N=-N(c_l-1)F_N+
\sum_{i+j=N-1}\big[(\alpha_i+1)\Phi_iF_j'-\alpha_j\Phi_i'F_j\big].
\]
A formal exact solution requires the full angular function \(\mathcal E_N=0\). The first three relations are
\[
(c_l-1)F_1=(\gamma+1)\Phi_0F_0'-\gamma\Phi_0'F_0,
\]
\[
2(c_l-1)F_2=(\gamma+1)\Phi_0F_1'-(2\gamma-1)\Phi_0'F_1
+2\gamma\Phi_1F_0'-\gamma\Phi_1'F_0,
\]
\[
\begin{split}
3(c_l-1)F_3={}&(\gamma+1)\Phi_0F_2'-(3\gamma-2)\Phi_0'F_2\\
&+2\gamma\Phi_1F_1'-(2\gamma-1)\Phi_1'F_1\\
&+(3\gamma-1)\Phi_2F_0'-\gamma\Phi_2'F_0.
\end{split}
\]
Given F0 these equations determine higher layers recursively when the Poisson solves are nonresonant; a finite candidate need not satisfy them. **The first860 campaign measures these defects and does not impose them as hard constraints or penalties.**

## Angular support, scale and residual interpretation

For a homogeneous potential \(r^s C\), the complete density/stream coefficient maps are in [BASIS_860_SPEC.md](../BASIS_860_SPEC.md). With highest potential index M, the leading density reaches harmonic2M+1 and stream function2M+2. Their nonlinear product can reach4M+3. At M=9 this is density harmonic39, while a uniform m≤9 correction supplies only through19. This is a structural nonclosure, not an optimization failure. Recursive support bounds can lead to potential cutoffs9,19,29,39 in layers0..3, but this is a possible later escalation.

Under exact spatial dilation L,
\[
F_{j,L}=L^{(j+1)\lambda}F_j,\quad
\Phi_{j,L}=L^{(j+1)\lambda}\Phi_j,\quad
\mathcal E_{j,L}=L^{(j+1)\lambda}\mathcal E_j.
\]
Thus raw coefficient norms change under dilation; for a fixed angular norm with nonzero F0,
\[
I_j=\frac{a_{\rm ref}^{\,j}\|\mathcal E_j\|}{\|F_0\|^{j+1}}
\]
is invariant. Report absolute norms and these diagnostics separately from pointwise relative PDE residuals. The quotient coefficient is \(\mathcal E_j/\sin\theta\), evaluated by finite Fourier identities, not division on the axis:
\(\sin((2h+1)\theta)/\sin\theta=1+2\sum_{\ell=1}^h\cos(2\ell\theta)\).

A nonzero first defect gives \(R_\rho\sim r^{2\gamma-1}\mathcal E_1\). At accepted278 this exponent is0.105587864228..., so the original density residual grows. Under the stated differentiated expansion, absence of larger unlisted branches, canonical growth assumptions and **full** E1 cancellation, the next density residual is \(O(r^{3\gamma-2})\), which decays for \(\gamma<2/3\). A projected low-mode match or small whole-axis loss does not establish this conditional conclusion.

## Inverse-even branches, resonance and canonical multipoles

Compactified radial factors also give
\(\alpha_{jq}=\gamma-j\lambda-2q\), q≥0; collect equal physical powers before writing independent equations. In the noncolliding power-only case the double-lattice recurrence is
\[
\mathcal E_{jq}=-[j(c_l-1)+2c_lq]F_{jq}
+\sum_{\substack{a+b=j-1\\u+v=q}}
[(\alpha_{au}+1)\Phi_{au}F_{bv}'-\alpha_{bv}\Phi_{au}'F_{bv}].
\]
The unforced j0/q1 condition requires F01=0, below the first three fractional corrections at the current parameter. This does not imply that all inverse-even moments must vanish. Later nonlinear forcing, coincident powers and multipoles require separate accounting.

On a stream sine harmonic n=2,4,..., Poisson resonance is
\(b=\alpha+1=\pm n\). A source coefficient \(S r^{b-2}\sin(n\theta)\) then requires
\(-S r^b\log r\sin(n\theta)/(2b)\) unless its resonant projection is zero.
Here b=0 is not a resonance. No first-four-layer resonance occurs at the present accepted parameter; check future parameters and all retained branches anew.

The canonical full-plane inverse is
\[
\psi_n(r)=\frac1{2n}\left[
r^{-n}\int_0^r t^{n+1}S_n(t)\,dt+
r^n\int_r^\infty t^{1-n}S_n(t)\,dt\right].
\]
Exterior \(r^{-n}\) multipoles may occur with coefficients fixed by the whole source, using finite-part moments where necessary. They are not freely chosen harmonic additions: a global decaying harmonic is singular at the origin; a growing even harmonic conflicts with the stipulated subquadratic class. The earliest allowed n2 multipole interacting with the leading density has residual power gamma−4, below E1/E2/E3, so it cannot cancel their defects. The current finite noninteger algebraic potential has no separate integer-power multipole branch; this restricts the ansatz, not every possible canonical IPM solution.

## Which candidate supports which statement?

- The original 2026-10-22 derivation/matching audit examined **accepted64**, SHA25684ce7010f07b90dcd1c0810357b45aa7090959430c28b0af647d9b93a8ae01b2. Its algebraic derivations and embedding identities are candidate-independent at generic parameters; its numerical tables are not current.
- The08:36 follow-up examined **accepted165**, SHA2560cc1081baeb271d53f8d2f8fccda54fd3d8159bde8cdab74f91f681fc0a8999e. Its0.145222% unresolved E1 L2 norm fraction beyond harmonic19 belongs only to that candidate; it is not an energy fraction or an accepted278 prediction.
- **accepted278** is the handoff incumbent, SHA256812d34466c078e2ce643c49671299f4359f764fe2e1d925426762ba962d6e955. Its present far-field evidence is [verification/farfield.json](../../verification/farfield.json), with reported leading density coefficient L2 norm about0.440353421495 and the positive exponent above. No old parameter-specific fraction is substituted for a fresh current computation.

The notes do not assert asymptotic completeness, existence of a global profile, continuous supremum bounds, good conditioning of a future chart or exact compatibility of any saved candidate.

