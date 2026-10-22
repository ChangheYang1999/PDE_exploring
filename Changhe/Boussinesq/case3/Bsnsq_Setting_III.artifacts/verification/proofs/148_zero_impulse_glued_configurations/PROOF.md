# Compact residual configurations with exactly zero affine impulse

Status: CONFIRMED conditional construction by the independent verifier. Written 2026-10-21 during shift5, before computation. This combines the continuous signed-reference family147 with the independently checked gluing estimates135 and impulse expansion145. It supplies nonprofiles satisfying one necessary compact-repair condition, not a solution or a nonexistence theorem. Fresh model reviews of the parameter-continuity step returned no written text; their availability limitation is recorded below.

## Statement

Fix beta>2, a0>0 and a prescribed disk D. Let the family147 retain the exact polynomial B2 core on D and share the same anisotropic relative exterior stream outside one disk B_N0. For every sufficiently large radius R there exists a smooth whole-plane configuration with the canonical relative inverse, exact thermal equation, same polynomial core, smooth compactly supported nonzero vorticity residual f, and

    integral f=integral y f=integral x f=0.

It obeys the prompt's x-reflection symmetry and polynomial tail class, and its vorticity changes sign. The source has support outside D and inside B_(8R). The first two moment identities follow from oddness in x; the third is a genuine choice of the family parameter. This is not a profile because f is not identically zero.

## 1. Why the gluing argument applies to this family

Write s=1/beta, m=1-2s and delta=R^-s. All references of147 have the same beta, identical streams outside B_N0, exact thermal transport, the same polynomial core and smooth global fields. They have uniform symbol bounds at every fixed order over t in[0,1]. Their reference velocities and vorticities on |X|>=R>N0 are identical. Their temperatures there vary continuously in the weighted norms used in135: the exterior drift is fixed, and the exterior scalar transport is linear in its smooth incoming trace. The cylindrical transport estimates in147 bound that solution operator at each fixed order.

The inverse, scalar transport, contraction, compactness and smoothness arguments of135 use only those bounds, outward radial drift in the exterior, and the positive damping determined by beta. They do not use the sign of the reference vorticity. That sign is used only to conclude global positive vorticity, a conclusion omitted here. More explicitly,135 equations(I)-(VI) involve absolute values of the inverse and transport coefficients and source terms. Its high-derivative recurrence chooses the single smallness condition32delta²L<=1 with L determined by the uniform low norms. Compactness of the parameter interval supplies one L and one exterior threshold Rcrit. The higher reference constants may depend on derivative order but do not change the required smallness of R. The final canonical-inverse check uses sublinear growth and the center value, both unchanged. Thus one Rcrit works for the entire family, and135 yields a smooth exact-thermal glued configuration for each t and R>=Rcrit.

For completeness, all references are positive-temperature squares. The glued temperature follows exact scalar transport from their incoming traces, so it remains nonnegative, positive off the axis and smooth. Inside B_R the reference is unchanged. Exterior radial drift is positive for the same uniform choice of R, so the global backward-basin property also persists. Global nonnegative vorticity is neither used nor asserted.

## 2. Continuous dependence of the fixed point

Fix R>=Rcrit. On the exterior scaled domain |z|>=1, v_R and omega_R are independent of t, since the exterior streams agree. Let B be the same closed strong ball of odd sources e vanishing on B5 used in135, with its weak weighted C-alpha metric d. The Picard maps T_t:B->B have a uniform contraction constant kappa<1.

The reference temperature trace on |z|=1 and its weighted derivatives depend continuously on t. For fixed e in B, the exterior drift w_e=beta z+delta v_R+delta²v[e] is independent of t. Scalar transport is linear in the incoming temperature trace. The estimates135(III)-(V), applied to the difference of these traces, give continuity of theta_t,e in its weak weighted C^(1,alpha) norm, uniformly over e in B. The source g_R,t depends continuously on t in the same required weighted norm. The remaining vorticity source coefficients are fixed. Applying the zero-trace scalar transport inverse in the definition of T_t therefore gives

    sup_{e in B} d(T_t(e),T_t0(e))->0 as t->t0.       (1)

This assertion uses finitely many trace and reference derivatives, all bounded uniformly by147. It does not require continuity of arbitrarily high solution derivatives. Let e_t be the unique fixed point. Then

    d(e_t,e_t0)<=kappa d(e_t,e_t0)
                +sup_{e in B}d(T_t(e),T_t0(e)).

Dividing by1-kappa proves continuity of e_t in the weak metric. The inverse estimates make v[e_t] locally C1-continuous. On B2 the potential Qe_t is harmonic, with sources separated by distance at least3, so all its derivatives on this compact disk depend continuously on e_t in the weighted weak norm. Hence the compensator b[e_t]=-Delta((chi-1)Qe_t) is continuous in every fixed compact Cj norm. The scalar transport difference estimates then give local C1 continuity of the glued temperature difference h_t=theta_t,e_t-theta_R,t.

## 3. Continuity of the residual impulse without derivative loss

The exact identity145 yields, after integrating the compact compensator term by parts,

    I_R(t)/R^(3-2s)
      = integral z1(1-rho)[g_R,t+delta v[e_t].grad omega_R-partial_1h_t]
        -integral(delta v_R,1+delta²v[e_t]_1)b[e_t].  (2)

Every integral is over B8. The correction terms vanish on B1, while g_R,t is a smooth reference quantity on B8 for the fixed finite R. The compact compensator has zero first moment; that exact cancellation is why(2) contains no derivatives of e_t. The continuity established in section2 makes the right side continuous in t. Thus I_R(t) is a continuous real function on[0,1]. This avoids inferring continuity in a strong derivative norm merely from a weak fixed-point theorem.

## 4. Opposite signs and an exact zero

The two endpoint references in147 have moments m1(0)<0<m1(1). Their common exterior stream is the same shifted anisotropic formula as in145, with a fixed relative linear term. Consequently its homogeneous leading stream is even in y. The leading angular x-moment of V_hom.gradOmega_hom is zero by this leading-field parity, exactly as in145 Proposition C. This uses no y-reflection of the actual fields or temperature. The references retain the full temperature remainder O_symbol(r^(m-s)) and the same vorticity/velocity symbol expansions;145's residual-rate argument therefore applies to these signed references without change. Their cutoff rho is the same, so C_rho>0 is the same. By145, for each of these two fixed references,

    I_R(j)=R^(3-2s)[C_rho m1(j)+O_j(R^-s)], j=0,1.

Choose R1 sufficiently large that both endpoint signs persist for every R>=R1, and also R1>=Rcrit. Only two endpoint constants are needed; a uniform asymptotic over all t is unnecessary. For any such fixed R, continuity from section3 and the intermediate value theorem give t_R in(0,1) with I_R(t_R)=0. This is an exact existence argument, not a numerical cancellation or merely a zero leading coefficient. No continuity or convergence of t_R as R changes is asserted.

The resulting residual is compactly supported and odd in x. Therefore its zeroth moment and its y moment vanish by reflection, and its x moment is zero by construction. All three integrals are absolutely finite.

## 5. Why the configuration is still not a profile

Take R>N0. The nonempty annulus N0<|X|<R retains the common analytic shifted anisotropic relative stream. Packet124 proves that this prescribed analytic stream cannot satisfy both B2 transport equations with any C2 temperature on any nonempty open set. All present configurations have the exact thermal equation. If f were identically zero, both equations would hold on that annulus, contradicting124. Hence f is nonzero. Its support is contained in the annulus between the retained exact core D and B_(8R), by the construction135.

The negative-vorticity point proved in146 lies in the common bounded auxiliary region for each parameter, and restoration leaves it untouched. Taking R beyond the common restoration radius makes gluing leave that point untouched too. Thus the final configuration is sign-changing in the right half-plane. This does not violate the broad prompt, which explicitly permits sign changes, but it excludes the positive-vorticity strengthening of4.34.

## 6. Dependencies and scope

Dependencies:126 for the initial reference;124 for the analytic-stream nonprofile obstruction;135 for the gluing construction and its quantified contraction estimates;145 for the exact residual identity and endpoint impulse rate;147 for a continuous family with fixed exterior stream and opposite angular moments. Section1 states precisely the sign-free extension of135 used here. Sections2-3 prove the parameter continuity rather than assuming it.

This result does not solve the compact repair problem. In particular affine-moment cancellation is only necessary. Packet144 concerns a separate linearization on a polynomial patch and is not an obstruction proved for the annular residuals constructed here; further compatibility for these residuals remains open. It proves no small norm of the remaining source, no limiting profile as R tends to infinity, and no YES or NO endpoint.

## 7. Consequence for the actual exterior dipole

The sign-free gluing argument of section1 retains all three full spatial symbol bounds of135. Its fields satisfy both B2 equations outside8R, so150 applies to their relative streams. For beta outside Z={M/N>2: M,N coprime positive integers, N<=3},149 and150 give integral x f=2pi(1-3beta)D. The configuration constructed above therefore has exactly D=0, with D its actual degree-1 exterior dipole coefficient. Thus this new necessary dipole condition also coexists with the nonzero compact residual, exact thermal equation, all center relations, canonical full-plane inverse, and a whole-plane backward source basin. This is a nonprofile construction and does not assert that the remaining nonlinear compatibility can be repaired.

Initial complete draft saved 2026-10-21T08:34:02.599798+00:00. Final independent verification completed 2026-10-21T09:30:38.893111+00:00. The argument is conditional on the complete statements of the listed dependencies, all checked separately. No new numerical PDE solution is claimed. Its exact compensator formula and endpoint rate use145's independently tested identities;147 has18 additional manufactured controls. ActualOpus228 and earlier whole-argument requests returned no written audit, not an adverse mathematical finding and not an endorsement. The weak-metric continuity and compact integral argument are independently proved in sections2-4; no convergence of high derivatives from a weak contraction is assumed.
