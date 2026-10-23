# Scaling covariance and the scope of the SPEC v48 summary

Result 239. This argument precedes its executable checks. It audits SPEC.md v48 against the definitions of the primary class and previously proved results. It does not assume existence of a primary profile.

Let c>1, p=1/c, and let rho be an exact primary profile with a=rho_y(0) nonzero. The canonical inverse is linear and commutes with the positive spatial action rho_lambda(X)=lambda rho(X/lambda), U_lambda(X)=lambda U(X/lambda), psi_lambda(X)=lambda^2 psi(X/lambda). These formulas follow either by changing variables in the modal inverse or by Poisson, parity and the sublinear uniqueness condition. The chain rule gives

    a_lambda=a, b_lambda=lambda^(-2)b,
    K_lambda=lambda^(1-p)K,
    L_lambda=lambda L,  L=(K/a)^(1/(1-p)),
    (bL^2)_lambda=bL^2.

The y-axis theorem gives K/a>0 for an exact primary profile. Hence L is strictly positive and cannot be invariant under any lambda other than 1. The assertion in SPEC F2 that both L_can and b L_can^2 are invariant is false as a covariance identity. Its own Section 5.4 states the correct transformation. Repair F2 to state that L_can scales by lambda and b L_can^2 is invariant. The matched residual law is unchanged: R_lambda(X)=lambda R(X/lambda), with both residual denominators transforming identically. The beta-line is restricted to beta of the original gauge's sign, as already stated in FINAL_REPORT 3.19(i).

Fixing a nonzero K=kappa gives a transverse section only on the component with sign K=sign kappa. The equation lambda^(1-p)K=kappa has a unique positive solution if kappa/K>0, and none if kappa/K<0. L=1 covers both admitted signs. Calling one fixed signed K a global slice for the entire primary class requires a separate exclusion of profiles of the other sign; no such exclusion has been established. This is a missing scope condition, not a construction of negative-slope solutions. In contrast, the two sections K=1 and K=-1 jointly meet all possible signed orbits.

For a concrete check of the transformation law on admissible density fields, use

    rho_s(x,y)=s y(1+x^2+y^2)^(-1/4),  s=1 or -1, p=1/2.

These fields are smooth, have the required parities and sublinear density and gradient growth. Their exact coefficients are a=K=s, b=-s/4 and L=1. At lambda=4, K_lambda=2s, b_lambda=-s/64 and L_lambda=4, while b_lambda L_lambda^2=-s/4. They are only density fixtures, not exact IPM profiles. They demonstrate that the covariance is not a numerical convention and that positive scaling preserves sign. The general proof above applies conditionally to every exact profile.

The remaining findings concern document consistency:

1. SPEC 4.3 says no solver enforces T2. The later weighted cubic fit includes this relation as a penalty. A finite penalty does not enforce exact equality. State instead that T2 must be recomputed independently even when included in the fitting objective; reserve a claim that it was omitted for the particular solver where that is true. A test included in a fit also cannot be described without qualification as an independent condition omitted from the fit. The report's Section 4.7(b) supplies the counterexample to the universal omission claim.
2. F7 says the all-degree resonance bound is open. The fixed-top-harmonic result in FINAL_REPORT 3.9 and research/all_degree_resonances/PROOF.md already proves it. Its hypothesis is essential. For n=2k+1, ell_i=2k+2i(A-1) and

       P_k(a)=sum_(j=0)^k [(2k+1)!/((2j+1)!(2k-2j+1)!)]
                          product_(i=j+1)^k (1-a/ell_i).

   The highest stream harmonic is prescribed to zero in the homogeneous resonance problem. Its nonzero kernel is equivalent to P_k(a)=0, by the triangular Poisson and transport recurrence in that proof. For k=1, P_1=2-a/(2A). For k>=2 and 0<=a<=ell_2, combine the first two terms. Their bracket is 1-a/ell_1+k(2k+1)/3>0, because ell_2/ell_1<2 and k(2k+1)/3>1. All remaining factors are nonnegative and the final term is 1. For a<0 every factor is positive. Thus all real resonances have a>ell_2=4A+n-5 when n>=5; degree3 alone has equality a=4A. This is not a restriction on arbitrary pairs with a free top harmonic, nor an existence or nonexistence theorem for profiles. Replace the finite-degree/open label with this scoped all-degree theorem; finite lists of individual curves remain finite.
3. G41's header records installation as 3.78, but its trailing prose still says “Consequence if confirmed” and “Not in report”. These labels are obsolete. The ODE matching conclusion remains formal with respect to the PDE; updating its installation status must not turn it into a proved full-profile expansion or a NO endpoint. Likewise G42 records an older installation request even though installed draft71 has already been audited. Historical notes may retain their dates, but the current summary should identify the current state unambiguously.

The audit freezes the current SPEC and report. Text searches and exact arithmetic verify provenance and local contradictions; they are not a new proof of every claim in these documents. The existing independent proofs of the canonical inverse, y-axis scale and all-degree resonance bound supply the dependencies. No primary profile, exclusion of a signed branch, or decisive endpoint follows. The principal endpoint stays UNRESOLVED.
