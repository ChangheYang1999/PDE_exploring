# Precision audit of Section 2B, D4-D6

Status: targeted independent reconstruction and comparison with the existing Theory Agent C  review. This is not a fresh audit of all of D0-D6 or of the external dynamical-systems sources. The source snapshot and the complete seven-item comparison are in `verification`.

## 1. Setting and conclusions

The source assumes 0<c<1/2, omega real, U in C2, P in C1, the rotating Euler profile equation and uniformly sublinear U. Set B=(cI-omega J)x+U, Omega=curl U, phi the complete B-flow, psi_t=phi_{-t}, and F=psi_1. A compact ball D traps all backward orbits. The core Lambda is the intersection of F^n(D). The closed flux form sigma=i_Omega(dx1 wedge dx2 wedge dx3) obeys F^*sigma=exp(1-2c)sigma. These already audited identities are premises here.

Two precise formulations complete the steps flagged by the Theory Agent C  review. In D4(ii), the time-zero flow box must be chosen to be the particular box containing the initial disk, and this disk must meet each plaque of the corresponding larger box at most once. In D6.2, K must be the omega-limit set of the stated precompact orbit throughout. The theorem applications already permit these choices. The remaining five items are notation and citation-scope clarifications, detailed below.

## 2. Flow-box injectivity in D4(ii)

Assume Omega has no zero on Lambda. By nested compactness choose N so that K=F^N(D) and a neighbourhood of it contain no vorticity zero. The finite family of C1 Omega-flow boxes consists of a smaller box inside each larger one. Choose constants C and eta uniformly so that same-plaque points in a smaller box are joined in the larger box by a plaque arc of length at most C times their ambient distance, and any plaque arc of length less than eta starting in a smaller box stays in its larger box. Shrinking product boxes gives these properties.

The set K has interior, since it is the diffeomorphic image of a ball. Choose a small transverse disk S inside that interior and inside one particular smaller box V0. Choose it to be a graph over the transverse coordinate of the corresponding larger box W0. Consequently it meets each plaque of W0 at most once. Orient S so that sigma is positive, and let A0 be its positive flux.

Let L bound the derivative of F inverse on all the finitely many larger boxes, whose closures lie in the neighbourhood under consideration. Choose delta so that every subset of K of diameter at most 2delta lies in a smaller box and 2LCdelta<eta. For E equal to S intersected with a Bowen ball through times 0,...,n, choose a smaller box containing F^j(E) at each time j>=1. At time zero choose V0, regardless of the box the Lebesgue-number rule might otherwise select.

Suppose two points of F^n(E) have the same transverse coordinate in its larger box. Join them there by a plaque arc of length at most 2Cdelta. Its F-inverse image is tangent to Omega, has length at most 2LCdelta, and starts in the preceding smaller box. It therefore stays in that preceding larger box. Both endpoints are in the preceding smaller box on one plaque, so replace the image arc by a short plaque arc and repeat. At time zero the resulting endpoints lie on one plaque of W0 and both belong to S. The graph property of S makes them equal. Invertibility of F then gives equality of the original points.

The projection onto transverse coordinates is thus injective on F^n(E). It is a local C1 diffeomorphism on F^n(S), since transport preserves transversality. In a box sigma=g(q,z)dq1 wedge dq2, with uniformly bounded g and bounded transverse coordinate area. The change-of-variables formula on the injective subset gives an upper bound M on its flux, independent of n and E. A finite Bowen-ball cover then yields exp((1-2c)n)A0<=M r_{n+1}(K,delta). This is the same entropy estimate as the source. The terminal-to-initial induction does not require the arbitrary time-zero box to equal W0: it explicitly chooses V0 at that time.

This verifies the proposed repair. It changes no profile hypothesis or conclusion. The report should say "meeting each plaque of the corresponding larger box at most once" and explicitly state the time-zero box choice.

## 3. Exact entrance lemma and its proof

Let Y be a C1 vector field on an open set containing the compact closure of a positive orbit x(t), t>=0. Let p be a hyperbolic equilibrium in that open set. Write K=omega_Y(x), assume K is not a singleton, and assume W^s_Y(p) intersect K is contained in {p}. Then p does not belong to K.

Suppose otherwise. Choose a sufficiently small closed ball Dp centered at p so that each positive orbit remaining in Dp for all future times lies in the local stable manifold. The local stable-manifold theorem at a hyperbolic equilibrium provides such a neighbourhood, which may be decreased to a ball. Choose the radius also so that K has a point outside Dp.

There are arbitrarily late visits of x(t) outside Dp and arbitrarily late visits tending to p. Choose t_n tending to infinity with x(t_n) tending to p and an outside visit after time n but before t_n. Let s_n be the last entry through the boundary of Dp before t_n. Then s_n>n, x([s_n,t_n]) lies in Dp, and |x(s_n)-p| equals its radius r0. A local bound |Y(z)|<=L|z-p| and Gronwall applied to the radius give

    |x(t_n)-p| >= r0 exp(-L(t_n-s_n)).

Hence t_n-s_n tends to infinity. By boundary compactness pass to a subsequence with x(s_n) tending to z in the boundary. Since s_n tends to infinity, z is in the actual omega-limit set K. Continuous dependence, first on any fixed finite time interval and then on all such intervals, shows that the positive orbit of z remains in Dp. Thus z belongs to W^s_Y(p) intersect K, but z differs from p. This contradiction proves the lemma.

For D6 take Y=-B and K=alpha_B(a)=omega_Y(a). If the two eigenvalues of DB(p) other than 1+c have negative real parts, p is hyperbolic for Y with a one-dimensional stable manifold. The identity

    psi_t gamma_p(tau)=gamma_p(exp(-(1+c)t)tau)

makes the vortex line through p this local stable manifold; invariance gives its global stable continuation. D6.1 shows that this vortex line meets K only at p. The lemma therefore applies with exactly the required omega-limit set. The report already uses that application, so the repeated definition of K in the lemma is a statement defect with a direct repair, not a counterexample to D6.

## 4. The five further wording items

The disk in D4(i) is centered at the point a and normal to Omega(a). Adding a comma or writing "centered at a, with normal Omega(a)" resolves the current wording. Continuity and Stokes then give its nonzero circulation; no new estimate is needed.

The scalar a=1-2c in D4(ii) can be renamed kappa0 to avoid collision with a point a used elsewhere in Section 2B. It is positive and remains the same exponent in the flux and entropy estimates.

In D5.7-D5.10 the symbols N, N_y and the extension neighbourhood N are local neighbourhoods, while D0 reserves N for the zero set of B. Rename them N_G, W_y and V_N, respectively. The N in the closing-lemma step of D5.8 is a sufficiently small trapping neighbourhood of A, obtained from D5.7, not the zero set of B. The ball D in D6.2 is the small ball Dp from Section 3 above, not the global trapping ball. These are distinct objects with the properties explicitly used by their proofs.

The sentence after Corollary D5.12 should separate the cited half-vortex escape result A158 from Lemma D5.13, whose proof is displayed immediately afterwards. The latter is not being accepted here as an uncited external theorem.

The spectrum in D6 allows lambda2=0. In that case the equilibrium is not hyperbolic, though it still has one positive and one negative eigenvalue. Calling it a saddle must not implicitly add hyperbolicity. The numerical eigenvalue statement, the expanding inequality -lambda3>lambda2 and the conditional strongest-stable-direction assertion remain as printed. Hyperbolicity is used in Section 3 only under the contradiction assumption that both remaining eigenvalues of DB(p) have negative real parts; there is no circular application at lambda2=0.

## 5. External-source remarks and verification limit

The optional compactification clarification for the Bowen-Ruelle and Ledrappier-Young remarks is appropriate: multiply the nonlinear field by a cutoff equal to one near the compact core, use the linear field near infinity, and compactify as in D4(i). The map agrees on a neighbourhood of the invariant set in question. This addresses the ambient compact-manifold setting. It is not a new proof of either external theorem or of all their remaining hypotheses.

Every numbered finding and the scope paragraph in the existing Theory Agent C  comparison were read. Its separate affine calculations and source audits were not rerun or independently certified by this targeted review. No numerical computation or formal build was needed. The agent is configured as model; actual provider execution and a specific runtime version remain independently unattested. The coordinator's separate configured model comparison supplies continuing collaboration. No new client, agent or remote computation was used.
