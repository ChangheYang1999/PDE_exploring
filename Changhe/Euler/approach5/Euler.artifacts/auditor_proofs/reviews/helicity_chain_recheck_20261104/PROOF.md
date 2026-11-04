# Repeated audit of the helicity-sign Liouville chain

Status: independent reconstruction of the conditional chain. No new coverage theorem or removal of the sign hypothesis is claimed. The audited report is the approved snapshot with SHA256 3b1fbbc466d810ec9a4ae97a2b5003b0d387faba68fe5a48f224f41943474869, Section 2D through Corollary L.4. Its earlier source audit is in the team records; the current energy audit is in the team records. The current reading is of the displayed proof, not a fresh audit of every external ergodic theorem or every coverage theorem.

## 1. Exact conditional statement and dependencies

Let 2/5<=c<1/2, omega in R, U in C2(R3;R3), P in C1(R3), and U(x)->0 uniformly as |x|->infinity. Let J(x,y,z)=(-y,x,0), A=cI-omega J, B=Ax+U and W=curl U. Assume

    div U=0,
    (1-c)U+DU B+omega JU+grad P=0.

Write a=1-2c>0, kappa=1+c, h=U.W, O={W!=0}, H=P+|U|^2/2+Ax.U. Let Phi denote the B flow and Psi_t=Phi_-t. Suppose a countable family F of compactly supported probabilities is given, each invariant and ergodic for the whole Psi flow, with full measure on {B!=0,W!=0}, Lyapunov spectrum (a,0,-kappa), entropy a for Psi_1, and whose continuous-time basins cover O modulo Lebesgue measure zero. A basin uses all bounded continuous test functions. For nu in F, let D_nu be the union of open subsets V of O with Leb(V minus Bas(nu))=0. Assume h has at most one strict sign on each D_nu. Then U=0.

The proof below uses the previously source-checked Ledrappier-Young implication: on a compact C2 model, the given entropy formula supplies unstable conditional measures equivalent to arclength on local one-dimensional unstable arcs, with positive finite densities. It also uses the independently confirmed energy and pressure construction of Section 2A. Their hypotheses are checked below. It does not derive this family from C2 regularity and decay. The smooth theorem and the finite-r theorem under (G) use their separately confirmed coverage results to provide F.

## 2. Carrier and vortex completeness for every omega

Decay gives M=sup|U|<infinity. Since |B(x)|<=||A|| |x|+M and B is C1, neither time direction of its maximal solution can escape to infinity in finite time. Thus Phi is complete. Variation of constants, using ||exp(tA)||=exp(ct), gives for t>=0

    |Phi_t x|<=exp(ct)(|x|+M/c),
    |Phi_t x|>=exp(ct)(|x|-M/c)+M/c,
    |Psi_t x|<=exp(-ct)|x|+(1-exp(-ct))M/c.

The determinant is det D Phi_t=exp(3ct). Also B(x).x>=c|x|^2-M|x|, so the radial barrier is outward beyond 2M/c. Compact whole-flow invariant sets lie in the closed ball of radius M/c, by applying the Psi bound for arbitrary t to their bounded forward Phi orbits.

Solving the equation for grad P shows P is C2. The exact Lamb identity is

    aU+grad H=B x W.

Taking curl gives [B,W]=-kappa W; hence D Phi_t(x)W(x)=exp(kappa t)W(Phi_t x). No rotation coefficient is discarded: A^T=cI+omega J is what cancels the two explicit omega JU terms in the Lamb computation.

For rho>=0, let m_rho=1+max_{|z|<=rho+1}|W(z)| and delta_rho=1/m_rho. Local W trajectories starting in the rho ball stay in the rho+1 ball for |s|<=delta_rho. Set rho_x=max(|x|,M/c). For any s choose T>=0 with |s|exp(-kappa T)<=delta_(rho_x), and define

    Gamma_s x=Phi_T Gamma^loc_(s exp(-kappa T)) Psi_T x.

Differentiating the conjugated local curve with the Cauchy identity gives the W equation. Uniqueness on overlapping intervals makes this independent of T and gives all real s. Thus W is complete and

    Phi_t Gamma_s=Gamma_(s exp(kappa t)) Phi_t.

For x in a compact set K, take rho=max(max_K|x|,M/c), delta=delta_rho and T=kappa^-1 log(1+|s|/delta). The inner local arc lies in the rho+1 ball, so

    |Gamma_s x|<=(rho+1+M/c)(1+|s|/delta)^(c/kappa).

The complete Gamma flow preserves volume because div W=0. No globally bounded vorticity or bounded vortex line is assumed.

## 3. Recurrence and the sign-to-zero step

Fix a nonzero integer N and a bounded rational ball V. Let V' consist of points in V that never return to V at times jN, j>=1. Its Gamma_(jN) images are disjoint and have equal volume. The first n+1 images lie in a ball of radius C(1+n|N|/delta)^(c/kappa). Therefore

    (n+1)Leb(V')<=C'(1+n|N|/delta)^(3c/kappa).

Since 3c/kappa<1, V' is null. The points having only finitely many returns form a countable union of inverse images of V' and are null. Intersecting the full-measure return sets over rational balls and integers N gives recurrence arbitrarily close to the initial point in both time directions, including integer times.

Dotting the Lamb identity with W gives dH(Gamma_s x)/ds=-a h(Gamma_s x). On a Gamma-invariant open D where h>=0, H along every orbit is nonincreasing. If h>0 somewhere, continuity gives a positive-volume neighborhood with a uniform strict decrease of H over one short time interval. Shrink the neighborhood so its H oscillation is smaller than half that decrease. A recurrent point in it returns after the interval, contradicting monotonicity and the oscillation bound. Thus h=0 on D. Replace (H,h) by (-H,-h) for the opposite sign.

This step needs open invariant domains, rather than a sign only on the singular invariant measure support. It uses neither finite total ambient volume nor recurrence of every orbit.

## 4. Canonical pressure and transported mean decay

The Section 2A energy theorem, valid for C1 profiles, gives E(R)=int_(B_R)|U|^2<=C_E R^beta for R>=1, with beta=5-2/c in [0,1). At c=2/5 the theorem gives U in L2 and one can take C_E=||U||_2^2. In the open range the asymptotic bound gives a finite C_E. Dyadic shells then give

    C_S=2^beta C_E/(1-2^(beta-3)),
    S(rho)=int_(|z|>=rho)|U(z)|^2 |z|^-3 dz<=C_S rho^(beta-3), rho>=1/2.

The source-checked pressure construction gives on B_(2R) a local singular integral N_R of U_i U_j cut off at 4R, an ordinary far kernel integral Far_R, and a constant p_R-c_R. The shell bound makes both far integrals absolutely convergent. Increasing R changes N_R by exactly the removed annular kernel integral and Far_R by its negative. Thus p_R-c_R is a single constant p_inf, rather than a radius-dependent pressure choice. In particular P0=P-p_inf=N_(R/2)+Far_(R/2) on B_R.

The Plancherel tensor estimate gives ||N_(R/2)||_2^2<=M^2 E(2R). The kernel bound gives |Far_(R/2)|<=(4/pi)S(2R) on B_R. Squaring and integrating yields

    int_(B_R) P0^2<=2^(1+beta)M^2 C_E R^beta
      +[2^(2beta+1)/(3pi)] C_S^2 R^(2beta-3)<=C_P R^beta.

Consequently H0=H-p_inf satisfies int_(B_R)H0^2<=C_H R^(beta+2). Its normalized square mean tends to zero since beta<1. This determines p_inf uniquely: a nonzero added constant cannot have vanishing normalized square mean.

For any bounded measurable Q, the Phi image lies in a ball of radius exp(ct) times a fixed constant, and its Jacobian is exp(3ct). Thus

    int_Q H0(Phi_t x)^2 dx<=C_Q exp(c(beta-1)t)=C_Q exp(-2at).

Its average over t in [0,T] is at most C_Q/(2aT). The expanding direction and the Jacobian sign are essential.

## 5. Basin geometry and the conditional-measure input

Basins are Borel in either carrier direction. Indeed use a countable dense family in C0, reduce real times to integers, and impose convergence on that family. A compact cutoff equal to one on supp nu has empirical average tending to one; multiplication by it extends convergence to every bounded continuous test. This argument needs no boundedness of the forward Phi orbit. Birkhoff for Psi_1 applied to int_0^1 f(Psi_t x)dt and whole-flow invariance of the limit give whole-flow genericity; no time-one ergodicity is assumed.

The exact conjugacy gives |Psi_t Gamma_s x-Psi_t x|<=C_x |s|exp(-kappa t) for large t. Both Psi orbits are bounded. Uniform continuity of a test function on their common compact ball then shows Gamma_s preserves Bas(nu). Carrier invariance follows by shifting time averages. Bas(nu) is contained in O since the bounded continuous test min(1,|W|) has positive nu integral and vanishes along any orbit in {W=0}.

For the conditional-measure theorem, cut off -B outside a ball of radius greater than 2M/c+1 and extend by zero to S3. The modified time-one map is C2, agrees with Psi_1 near the compact core, and has the same derivative cocycle there. The radial barrier traps every backward-asymptotic point of a core orbit inside that core. Conversely, an original backward-asymptotic point has bounded integer Phi orbit, then bounded continuous Phi orbit; the lower bound in Section 2 forces every point of that orbit inside radius M/c. Thus the unstable manifolds coincide at regular points. There is no manifold assertion at nonregular points. A smooth metric Euclidean near the core meets the compact-manifold hypothesis.

The supplied exponents and boundedness of B and W on supp nu identify E^s=R W and E^0=R B, using both time directions for B. In particular they are independent, and the unstable tangent is transverse to both. The earlier primary-source audit of Ledrappier-Young gives an unstable local arc gamma through almost every point, with arclength-almost every point generic in both directions and regular. Such points are dense on the arc and lie in the closed support, so the whole arc lies in supp nu.

At a regular base point the map Theta(s,r,tau)=Gamma_tau Psi_r gamma(s) has independent derivatives gamma', -B and W. A small parameter box maps diffeomorphically to an open V inside O. Its Jacobian has positive lower and finite upper bounds. The full-measure set of generic s values times the other two intervals maps to a full-volume subset E of V contained in Bas(nu).

The definition of D_nu and a countable subcover give Leb(D_nu minus Bas(nu))=0 and nu(D_nu)=1. C1 carrier and vortex diffeomorphisms preserve O, Bas(nu) and null sets, so they preserve D_nu. A nonnegative compactly supported test in D_nu with positive nu integral makes every basin orbit enter D_nu, hence Bas(nu) is contained in D_nu. Different such domains are disjoint. Coverage of O by their union uses the explicit coverage assumption on F.

## 6. The zero Bernoulli value on one domain

By Sections 3 and 5, the sign hypothesis gives h=0 on D_nu and H0 is constant along its vortex orbits. For the product box above and every real t, for y=Theta(s,r,tau) in E,

    H0(Phi_t y)=H0(Phi_(t-r) gamma(s)).

The exact conjugacy moves the vortex parameter to tau exp(kappa t); completeness and global D_nu invariance justify this even when it is large. The right side is bounded uniformly by max_(supp nu)|H0| because the whole gamma arc lies in the compact invariant support. Backward-carrier genericity of gamma(s) shows that its square time average is m=int H0^2 dnu. The bounded r shift does not alter the limit.

Dominated convergence on the finite-volume E gives convergence of the spatial integral of these averages to m Leb(E). Section 4 bounds the same quantity by C_V/(2aT), tending to zero. Since Leb(E)>0, m=0. Continuity now gives H0=0 on supp nu and the displayed identity gives H0=0 on every Phi_t E. Density gives H0=0 on every Phi_t V. A test supported near the regular base point in V and positive on the support makes every basin orbit enter V, so H0=0 on Bas(nu). Its density in D_nu gives H0=0 throughout D_nu.

No integration by parts against nu, and no uniform bound on a whole unbounded domain, is used. The one product box provides the finite bound needed for dominated convergence.

## 7. Arbitrary-boundary localization and positive stress

The union of the D_nu is open and has full volume in O, so continuity gives H0=0 on O and grad H0=0 on its closure. At each boundary point of O, W=0, and the Lamb identity gives U=0 there.

Let D_Z=int{W=0}. Every point of its boundary and of {W=0} minus D_Z is in the boundary of O. Paste U on D_Z and zero outside. On each ball this field is Lipschitz with constant bounded by max|DU|: a segment crossing the boundary is split at its first and last crossing, where U=0. Its weak derivative is 1_(D_Z)DU almost everywhere. This remains true on a boundary of positive measure because a Lipschitz map has derivative zero almost everywhere on its zero set, by the density-point and differentiability argument. The pasted field therefore has zero distributional divergence and curl. It is harmonic, smooth, analytic, and zero on the nonempty open O. Thus it is zero everywhere. If O was empty at the outset, bounded harmonicity and decay already give U=0.

It follows that U=0 on {W=0}, grad H0=0 everywhere, and H0=0 by its vanishing mean. Dotting the Lamb identity with B gives U.B=0. The identity H0=P0-|U|^2/2+U.B gives P0=|U|^2/2.

Taking divergence of the full profile equation gives Delta P0+partial_i partial_j(U_i U_j)=0: the linear -omega J drift term and the explicit omega JU term cancel exactly. Test against chi(x/R)psi(x), where chi is a smooth cutoff equal to one on B1 and zero off B2, and psi=(1+|x|^2)^(1/2). Two integrations by parts have compact support. All terms differentiating chi have absolute value at most C E(2R)/R, which tends to zero since beta<1. The other terms are

    chi(x/R)[U^T D2psi U+(|U|^2/2)Delta psi],

with D2psi>=psi^-3 I and Delta psi>0. On every fixed ball this bounds int |U|^2 psi^-3, forcing that integral to vanish as R tends to infinity. Hence U=0.

## 8. Class actually covered and comparison

This proves the conditional implication with a supplied family F. The finite-r result additionally requires the separately established componentwise (G) hypothesis. The C-infinity result uses the separately established smooth coverage theorem; it retains the helicity sign premise. The strengthened levelwise criterion follows from recurrence: a nonzero h on a domain gives a decreasing segment of H and a later return above that segment; an increasing segment then crosses the same open interval of levels. The inverse function theorem at the two strict crossings gives both helicity signs for each level of that interval on one recurrent orbit. This does not say every orbit, domain or level has that property.

The full current Section 2D through L.4, the full earlier auditor proof and all of the existing Theory Agent B  comparison have been read. The Theory Agent B  comparison agrees on completeness, recurrence, pressure constants, product-box transfer, the positive-measure boundary and the stress error. Its R1 and R2 clarifications are present; its smaller 3/2 cutoff coefficient is compatible with the report's valid overestimate 2. The recent A79/A82 comparison supplies the explicit reverse unstable inclusion and the corrected dependency references. No new mathematical discrepancy was found.

This recheck does not re-certify the full Section 2B or 2C coverage development or re-download external sources. Existing configured model coordinator/A-working file comparisons are used; the B agent is configured model. Actual provider runtimes are independently unattested.
