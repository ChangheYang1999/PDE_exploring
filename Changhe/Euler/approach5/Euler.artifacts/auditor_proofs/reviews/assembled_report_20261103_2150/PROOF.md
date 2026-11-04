# Scope audit of coordinator Notes 131 and 132

## 1. Exact assertion and evidence

This audit concerns the mathematical front matter, Sections 0-10 and Appendix A of this report at SHA256 3f495bd85a58cad414b885a3bcb8887f4fdfd653c7917d6de0696d9ce91921f4, 6789 lines. Its cumulative mathematical approval is relative to the qualified approval A2414 of pin 59817261. The covered portion is lines 1-5207. Historical Appendix B retains only its individual, expressly scoped audits. The false Section 9 reference isolated in A2412 is still excluded, and the scope of the complete-sector obstruction remains A2411.

All five complete differences from the Note 130 snapshot were read: this report, in the team records, THEOREM_ATTEMPTS.md, PROOF_OBSTRUCTIONS.md and in the team records. Their current bytes and hashes are retained in the team records; README has no difference. The four foundation blocks 2A-2D were compared byte for byte and are unchanged, with their hashes in the team records. The changes add Theory Agent C C66, distinguish two matrix domains in the linear-weight statements, and split summary row 8 into five alternatives. They add no unconditional theorem about the target problem.

The two entire seven- and six-section proofs comparable_natural_profile_20261103 and upper_pressure_removal_20261103 were reread. The exact statements of A476-A477, A492 and A498 were rechecked, without claiming a new reading of their complete proofs. The C66 and linear endpoint proofs were fully read in their preceding audits and are used at those scopes. Their hashes are recorded in the team records. Existing configured model coordinator and theory-agent exchanges, particularly Note A67, supplied the model comparison. Provider execution remains independently unattested. No numerical computation, model client or formal build was run.

## 2. The common flat orbit row

Use the exact setting F of auditor_proofs/reviews/carrier_flat_set_20261103/PROOF.md. Here 0<c<1/2, omega is any finite real number, X=(cI-omega J)x, a=1-2c, b=2(1-c), and a smooth flowbox G at a nonzero point x0 has a central orbit Gamma with connected G minus Gamma. The smooth scalar S is zero on Gamma and negative elsewhere. V and S are flat at x0, V is divergence free, k=X.V=0, DV X=-((1-c)I+omega J)V, W=curl V, X.grad S=-bS, W.grad S=0, and the actual scalar P=S+|V|^2/2 satisfies -Delta P=tr((DV)^2). Flatness means vanishing of every derivative, including order zero.

The exact algebraic identity grad k=X cross W-aV gives aV=X cross W. Off Gamma let H=-S>0. Scalar transport and W.grad S=0 give

    W=(a/b) grad(log H) cross V.

On each sufficiently small compact neighborhood off Gamma this gives |W|<=C|V| with a finite local C. A2348 with kappa=0 therefore continues a flat zero of V to a neighborhood on which V is zero. The flat set is relatively closed and open in connected G minus Gamma. If it were nonempty, V would vanish on all G by continuity. The Poisson equation would then make S harmonic, with maximum zero on Gamma and negative values off it, violating the strong maximum principle. Thus V is flat at no point off Gamma. The explicit invertible linear transport propagates flatness of V along Gamma. Flatness of W follows by differentiation, and aV=X cross W supplies its converse. This proves the exact common flat set.

The same two identities show that V=0 if and only if W=0 off Gamma; both are zero on Gamma. At any zero off Gamma the quasiconformal factorization used in A2348 has a nonzero holomorphic factor. Its finite zero order and the inverse Holder estimate give |V(Psi(y,t))|>=C|y|^N in a smaller flowbox, for an integer N>=1, with the zero orbit at y=0. The constants and N are local; no uniformity as the zero approaches Gamma follows.

Both explicit pressure-free C65 fields vanish on an open subset accumulating at each relevant flat point. Such a subset intersects G minus Gamma and contradicts the preceding conclusion. Neither can be completed to F with any S. This excludes these particular fields, including the positive-trace example, without excluding all possible positive-trace F configurations. The bound for grad log H off Gamma has no established extension to Gamma, and the proposed C/|y| estimate is already excluded by A2408 at its precise assumptions.

The new Appendix A row, its ASSUMPTIONS copy and the shorter descriptions in Section 10, T38(k) and O12 preserve these distinctions. In particular, an isolated zero orbit off Gamma is not an isolated zero point in three dimensions. A2409 remains OPEN for existence or exclusion of F, its positive-trace endpoint and uniform orders near Gamma.

## 3. Two different matrix domains

Let S be a real symmetric trace-free 3 by 3 matrix, with Frobenius norm |S|, and let W be in R3. Define

    K_lambda={S: lambda_min(S)>=-6/5},
    K_F={S: |S|^2<=54/25}, M^2=103/100.

Each is combined with the same constraint |W|^2<=M^2. The linear weights of SF.3 have the form (a,b,gamma t), with a>0, b and gamma real, t=|W|^2. The C67-C68 theorem concerns K_lambda: a strictly admissible linear weight exists precisely for 0<c<c_lin, with c_lin the specified degree-nine algebraic number. At c_lin a nonnegative weight exists, is unique up to positive scale, and has nonzero zeros, so strict admissibility fails. For c_lin<c<2/3 no such nonnegative linear density exists on that product domain. All these are statements about the displayed density family, not necessity of a bound for a profile.

To check the domain distinction independently, write lambda_min(S)=-m with m>=0. The other two eigenvalues sum to m, so their squares sum to at least m^2/2. Hence |S|^2>=3m^2/2. Therefore |S|^2<=54/25 implies m<=6/5, proving K_F is contained in K_lambda. Equality on the boundary m=6/5 forces the other eigenvalues to equal 3/5. The intersection with that eigenvalue face is thus the orthogonal conjugacy orbit of diag(3/5,3/5,-6/5), rather than the whole face. The word point in a sorted eigenvalue parametrization refers to this single eigenvalue triple.

The sorted triples (x,6/5-x,-6/5) used by SF.10 at x=63/100 and x=31/50 have squared norms respectively 10809/5000 and 2701/1250. These exceed 54/25=10800/5000=2700/1250. Thus those Farkas witnesses do not belong to K_F. Nonnegativity on the larger domain implies nonnegativity on the smaller, but its failure on the larger does not imply failure on the smaller. The existence construction transfers to K_F by inclusion; its exact threshold, endpoint uniqueness and above-threshold impossibility do not transfer by that argument. The floating scan in Note A67 is not used as proof.

The corrected Theorem 8 phrase explicitly names the lambda_min pair. Both detailed rows explicitly restrict linear nonexistence to its product set, then state only existence transfer to the Frobenius form. These changes are correct. The previously confirmed nonlinear criterion still covers both pairs for 0<c<=1/2, with the full profile and Hb assumptions, and is not altered here. No bound on S or W is obtained from U tending to zero.

## 4. Summary condition 3 without original helicity

Fix 2/5<c<1/2 and finite real omega. Let U belong to C2(R3;R3), P to C1(R3), satisfy the full rotating incompressible profile equations, and tend uniformly to zero at infinity. Assume |DU(y)|<=C(1+|y|)^(1/2). No original-profile helicity condition is imposed in this section.

A498 gives DU tending uniformly to zero. A476-A477 then give the natural derivative bound |DU(y)|<=C'(1+|y|)^(-1/c). The natural velocity bound follows by integration from infinity along each ray: since 1/c>1,

    |U(r theta)| <= integral_r^infinity C' s^(-1/c) ds
                  <= C'' r^(-(1-c)/c).

Together with compact-core regularity these are precisely the full natural bounds in LIT269. None of these derivative-gap inputs requires helicity. Their constants can depend on the fixed profile and omega. The alternative small exterior vorticity condition in Theorem 7 has its own audited derivative implication and does not change the following tail argument.

Put p=(1-c)/c, D=R3 minus {0}, X=(cI-omega J)x, W=curl V, E=|V|^2, S=P2-E/2 and k=X.V. Here V and P2 are the actual normalized tails, with the actual pressure limit Pinf subtracted before scaling. A533/A538/A539 give V in C_loc^(1,alpha), P2 in C_loc^(2,alpha) for every alpha<1, the divergence and linear transport identities, -Delta P2=tr((DV)^2), and X.grad S=-2(1-c)S. A533/A538/A539 do not require original helicity. Since 2/c-4<1, choose alpha strictly between that number and 1.

Assume additionally the exact three parts of summary condition 3:

    E<=r_+ |S| on the entire unit sphere,
    r_- |S|<=E on a neighborhood of {V=S=0} in D,
    k=0 and W.grad S=0 everywhere on D,

for fixed positive finite constants r_-, r_+. This is the localized-lower comparison of A2020-A2026. The upper comparison extends over D by the common scaling of E and S. A2020-A2022 show that beta=|S|^(-eta)V, extended by zero on S=0, is a continuous distributionally closed form, locally in W^(1,t) for the specified t, where eta=(1-2c)/(2-2c). They use the Poisson regularity and upper comparison to remove arbitrary scalar zero sets. Global simple connectivity gives a C1 potential phi, and k=0 gives X.grad phi=0.

For completeness, the global vanishing mechanism is explicit. If V is nonzero, phi has different sphere extrema, which are global by the explicit linear flow. Each boundary point z of either extremal set has V(z)=S(z)=0. On N={V!=0}, define R=E/|S| and tau=(1/c-2)/2. The divergence equation becomes

    div(q |grad phi|^(1/c-2) grad phi)=0,
    q=R^(-tau) on N,

with a fixed positive extension of q off N. The upper comparison gives q>=q0>0. The local lower comparison bounds q near z. A2023's local Harnack inequality, valid for this locally integrable q and exponent 1/c>2, then makes phi constant near z, contradicting its being an extremal boundary point. Hence V=0. The harmonic and homogeneous pressure argument in A2025 gives S=P2=0.

The faithful-tail implication uses the actual pressure estimate and full momentum, not helicity. With q1=2p+1, one has |DU U+grad P|<=Cr^(-q1) and the exact linear-flow integral from zero limiting tail gives U=O(r^(-q1)). The radial-cutoff energy identity has errors bounded by CR^(3-2q1), CR^(2-3q1) and CR^(2-2p-q1). All vanish. It follows that (1-5c/2) integral |U|^2=0, and c>2/5 makes the coefficient nonzero. Thus U=0 and P is constant. Finite energy is derived here, not assumed.

Summary condition 3 therefore states a valid conditional theorem without original zero helicity. The scalar identity W.grad S=0 is supplied explicitly, so it has not been illicitly obtained from an omitted helicity condition.

## 5. Summary condition 2 and the remaining alternatives

Under the same baseline and derivative bound, condition 2 adds U.curl U=0 and, in its comparison alternative, grad k cross grad S=0 on the whole set {S!=0}. Original zero helicity supplies W.grad S=0 by A531. The global upper comparison and Poisson structure first remove the scalar zeros as above. The resulting potential is invariant up to an additive Ct along the linear flow. If C were nonzero, its compact regular level surrounding the origin would have velocity flux of a strict sign, whereas divergence freedom and twisted homogeneity give zero flux through every centered sphere because 3c-1 is nonzero. Thus C=0 and k=0. The same local lower comparison and faithful-tail argument finish the proof. No rank extension through an arbitrary open irrotational region is inferred: it is a displayed hypothesis on all S!=0.

The alternative finite-order tail conditions retain their smooth-tail and T0 quantifiers; the split row does not weaken them. The helicity-sign basin theorem retains either C-infinity or the separate finite-regularity growth condition G. Endpoint integrability retains the exponent and space in Corollary A.4. The small-vorticity, strain and weighted-enstrophy alternatives retain the exact bounds of Theorem 8. The row is explicitly a summary pointing to their full statements, and does not promote these conditional results to the unrestricted class.

The localized lower comparison is sufficient for the two vanishing arguments in Sections 4-5. It is not known sufficient for the separate sector-forcing assertion, which still uses the global two-sided comparison on the sphere. The summary's next-step row preserves this limitation and cites A2066. Neither comparison nor the derivative bound is derived from bare decay.

## 6. Verdict and limits

The C66 insertion is CONFIRMED at A2404-A2408, the matrix-domain correction is CONFIRMED, and the revised summary alternatives 2 and 3 are CONFIRMED at their exact hypotheses. The mathematical approval of the covered portion of pin 3f495bd8 transfers from A2414 with these additions. The excluded editorial sentence A2412 is still false at this exact pin. Statements that the complete sector formulas fail to extend continuously to the origin are interpreted as A2411; matching only an exterior restriction to a different interior remains OPEN. Infinite energy by itself is not a violation of the target hypotheses.

No conclusion here excludes arbitrary smooth decaying rotating Euler profiles in 2/5<c<1/2, establishes existence of such profiles, completes the finite-order scalar germs, or settles the common-flat-orbit endpoint. Those remain OPEN. The report's unconditional and conditional labels must retain the stated hypotheses, with every real omega allowed but no uniformity of all constants in omega asserted.
