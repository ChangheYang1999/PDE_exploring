# Repeated audit of canonical pressure, transported means and dynamical closure

Date: 2026-11-03T23:43:38.978213+00:00

## 1. Statement, scope and notation

Fix 2/5 <= c < 1/2 and any finite real omega. Let J be the skew matrix generating rotation around the third axis, A=cI-omega J, a=1-2c>0 and kappa=1+c. Assume U is C2 on R3, P is C1, div U=0, U(y) tends to zero as |y| tends to infinity, and the full profile equation

    (1-c)U + (B.grad)U + omega J U + grad P = 0,    B=Ay+U.

Write Omega=curl U, O={Omega != 0}, Z=R3 minus O, h=U.Omega, Phi_t for the flow of B, Psi_t=Phi_-t and Gamma_tau for the flow of Omega. Put beta=5-2/c in [0,1). The following assertions are confirmed: the canonical pressure and Bernoulli quadratic mean bounds of report Lemma7, transported mean decay of Lemma8, the use of a product box in Lemma14, zero extension in Lemma15, localization in Lemma16 and the positive stress conclusion of Lemma17. The box and its measure hypotheses are stated in Section4. This does not silently prove the coverage hypothesis for an unrestricted profile.

The exact report is pinned at dfddefdf656192b952476a92ac384e412a7fdfa3a3d9b11df2282c961928d5ee. This is a repeated audit of specified arguments, not a new certification of every external source cited in Sections2C and2D. The real comparison artifacts are in the team records and in the team records. The latter reports the existing coordinator comparison and its two accepted clarity corrections. No fresh model client or remote computation was used; configured model identity is not independent provider attestation.

## 2. Pressure normalization and the quadratic mean

The energy theorem in Section2A, previously audited, gives E(R)=integral over B_R of |U|2 <= C_E R^beta for R>=1. At c=2/5 it gives U in L2 and C_E=||U||2^2; this is an actual input, not a consequence of boundedness. At c>2/5, its limit L and error C_A give C_E=2^beta(L+C_A/2). Let M=sup|U|<infinity. Dyadic annuli imply

    S(rho)=integral_{|z|>=rho} |U(z)|2 |z|^-3 dz
          <= C_S rho^(beta-3),
    C_S=2^beta C_E/(1-2^(beta-3)),    rho>=1/2.

Indeed each annulus of radii 2^k rho and 2^(k+1)rho is bounded by 2^beta C_E rho^(beta-3)2^(k(beta-3)); its upper radius is at least one. The geometric series converges. For smaller positive rho the additional compact annulus is integrable because U is bounded.

The full equation is necessary to normalize pressure. Here is the mechanism used in Section2A Lemma2.2. Let T_ij have Fourier multiplier -xi_i xi_j/|xi|2 and F_ij=U_i U_j. For a compactly supported smooth test phi, T_ij partial_k phi is integrable: it is L2 on compact sets and is O(|x|^-4) at infinity by the off-support kernel formula and integration by parts. Thus the canonical gradient G_k is the distribution

    <G_k,phi> = -sum_ij integral F_ij T_ij partial_k phi.

The pressure Poisson equation shows partial_k P-G_k is harmonic. To eliminate this harmonic remainder one pairs the momentum equation at scale R with a radial mean-value test centered at any fixed x. Integration by parts gives a term linear in U(Rz) against a fixed smooth test and two quadratic terms bounded by O(M2/R). The linear term tends to zero by decay and dominated convergence. Translated tests phi(. - x/R) converge in L1 with their relevant derivatives; T commutes with translations. Therefore the mean value of the harmonic remainder tends to zero, so the remainder vanishes pointwise. A solution of the Poisson equation alone would not justify this step.

Let K_ij=partial_i partial_j(1/(4pi|x|)) away from zero. Its contraction with a vector satisfies |sum K_ij(w)u_i u_j|<=|u|2/(2pi|w|3). Set

    N_R = sum_ij T_ij(F_ij 1_{|z|<4R}),
    Far_R(x)=integral_{|z|>=4R} sum_ij K_ij(x-z)F_ij(z) dz,
    c_R=integral_{|z|>=4R} sum_ij K_ij(-z)F_ij(z) dz.

The tail estimate makes these integrals absolutely convergent for |x|<2R. Section2A Lemma2.3, obtained from the canonical gradient, gives P=(p_R-c_R)+N_R+Far_R there. For R'>R the difference N_R'-N_R is T applied to the compactly supported annular tensor. On B_2R its kernel formula has no singularity and equals Far_R-Far_R'. Hence p_R-c_R has a single value p_inf independent of R. This verifies consistency; no independent pressure constants are combined without justification.

Put P0=P-p_inf. On B_R use N_(R/2)+Far_(R/2). Plancherel gives ||N_(R/2)||2^2<=M2 E(2R). The far field is at most (4/pi) C_S (2R)^(beta-3). Consequently

    integral_B_R P0^2 <= C_P R^beta,
    C_P=2^(1+beta)M2 C_E+2^(2beta+1)C_S^2/(3pi),    R>=1.

The second contribution initially has power 2beta-3, which is no larger than beta. Define H0=P0+|U|2/2+(Ay).U. Since |Ay|2<= (c2+omega2)|y|2,

    integral_B_R H0^2 <= C_H R^(beta+2),
    C_H=3[C_P+M2 C_E/4+(c2+omega2)C_E].

Thus its normalized quadratic mean tends to zero. If H0+k has the same property, the triangle inequality in the normalized L2 norm gives |k|<=||H0+k||+||H0|| tending to zero. The normalization is unique. None of these constants is claimed uniform in unbounded omega.

## 3. Completeness and transported mean decay

Bounded U gives |B(y)|<=||A|| |y|+M. Standard continuation on compact sets and Gronwall give complete forward and backward B flows. The radial rotation contribution vanishes, so |Phi_t y|<=e^(ct)(|y|+M/c) for t>=0. Since div B=3c, the Jacobian is e^(3ct). For any bounded measurable Q contained in B_R', R'>=1, change variables and apply Section2:

    integral_Q H0(Phi_t y)^2 dy
      <= C_H (R'+M/c)^(beta+2) e^(c(beta-1)t)
      = C_Q e^(-2at).

Time integration gives its average at most C_Q/(2aT). No pointwise Bernoulli limit and no pressure surface term at infinity are assumed. The C2 regularity used below also follows for P from the full equation, since its right side gives grad P in C1.

## 4. The product-box argument with its exact inputs

For this step fix a compactly supported probability nu invariant and ergodic under the full Psi flow, with nu(B!=0,Omega!=0)=1, simple exponents a,0,-kappa and entropy a for Psi_1. The report's audited entropy and unstable-disintegration inputs supply conditionals equivalent to arclength on local unstable arcs. Define Bas(nu) as the points of O whose forward Psi time averages converge to the nu integral for every compactly supported continuous test. Define D_nu as the union of all open subsets V of O with Leb(V minus Bas(nu))=0. The additional facts used here are: D_nu is invariant under both complete flows, contains Bas(nu), and Bas(nu) has full Lebesgue measure in D_nu. Assume h=0 on D_nu. These are explicit premises of the local closure argument; their separate coverage over O is not deduced here.

Choose a full nu-measure Borel set G of two-sided generic regular points with B and Omega nonzero, contained in supp nu. Conditional equivalence supplies an unstable arclength arc gamma and a full-length set T with gamma(T) in G. Since T is dense and the support is closed, the entire arc is in supp nu. At a regular base point, the three derivatives of

    Theta(s,r,tau)=Gamma_tau Psi_r gamma(s)

lie respectively in E^u, E^0 and E^s and are nonzero. The inverse function theorem gives a relatively compact open image V in O of a small rectangular box, with its Jacobian bounded above and below by positive constants. The image E obtained by restricting s to T is Borel and has full Lebesgue measure in V. Basin invariance under the two flows makes E a subset of Bas(nu). These facts use equivalence of unstable conditionals, not merely an unspecified singular conditional probability.

The rotating Lamb identity is aU+grad H0=B cross Omega. It implies Omega.grad H0=-a h, so H0 is constant on each complete vortex orbit in D_nu. The exact flow conjugacy is

    Phi_t Gamma_tau=Gamma_(tau exp(kappa t)) Phi_t.

For y=Theta(s,r,tau) in E this yields

    H0(Phi_t y)=H0(Phi_(t-r) gamma(s)).

The right side remains on the invariant compact support of nu and is bounded. Two-sided genericity of gamma(s), applied to a compactly supported continuous extension of H0^2, gives the time average of this expression squared equal to m=integral H0^2 dnu. A fixed shift r changes the average by at most 2|r| times the supremum norm divided by T. Dominated convergence on E now gives m Leb(E) as the limiting integral of the time averages. Section3 and Tonelli bound the same integral by C_V/(2aT), so m=0.

Continuity and the definition of support imply H0=0 everywhere on supp nu. The displayed identity then gives H0(Phi_t y)=0 for every y in E and real t. Density of E in V extends this to Phi_t(V). Their union E0 is open and invariant. A nonnegative continuous test supported in V and positive at its base point has positive nu-integral. Every point of Bas(nu) has a forward Psi visit to V by genericity, so lies in E0. Finally Bas(nu) is dense in D_nu, and H0=0 on D_nu. This supplies all steps of Lemma14 without integrating by parts against a measure singular in the vortex direction.

## 5. Zero extension and localization with arbitrary boundaries

Assume O is nonempty, U is C1, div U=0 and U=0 on partial O. Put D=int Z. Since Z is closed and its complement is O, partial D and Z minus D are contained in partial O. Define V=U on D and V=0 elsewhere. On a ball let L bound ||DU||. For x in D and y outside, the first exit p of the line segment from D lies in partial D and U(p)=0, so |V(x)-V(y)|<=L|x-y|. For two points in D whose segment leaves D, use the first exits from each endpoint; the sum of their distances is at most the full segment length. The other cases are immediate. Therefore V is locally Lipschitz.

At almost every point of its zero set a differentiable Lipschitz function has zero derivative: a nonzero derivative would give a cone of positive relative volume on which the value is nonzero, contrary to density one of the zero set. Hence DV=1_D DU almost everywhere, including any positive-volume boundary. Thus div V=curl V=0 in distributions and Delta V=0. Weyl's lemma and analyticity imply V vanishes everywhere since it vanishes on the nonempty open set O. It follows that U=0 on all Z. No boundary regularity or finite perimeter has been assumed.

If H0=0 on an open subset of O whose complement there has measure zero, continuity gives H0=0 and grad H0=0 on O and grad H0=0 on its closure. At a boundary point Omega=0; the Lamb identity and a>0 imply U=0 there. The preceding extension then gives U=0 on Z and the Lamb identity gives grad H0=0 on Z. Thus H0 is a global constant, and its canonical normalized mean makes it zero. Dotting the Lamb identity with B gives U.B=0. Since H0=P0-|U|2/2+U.B, one obtains P0=|U|2/2. If O is empty, bounded harmonicity of U and decay already give U=0.

## 6. Positive stress without an unproved boundary limit

Take the divergence of the full equation. The two terms containing omega cancel exactly, while div U=0 removes the scalar linear terms. Therefore

    Delta P0 + partial_i partial_j(U_i U_j)=0.

With P0=|U|2/2, test this distribution against chi_R psi, where 0<=chi<=1 is smooth, equal to one on B1, supported in B2, chi_R(y)=chi(y/R), and psi=(1+|y|2)^(1/2). Twice integrating by parts has compact support. The terms differentiating chi_R have absolute integral at most

    C_chi R^-1 E(2R),
    C_chi=3||grad chi||inf+3||D2chi||inf+2||Delta chi||inf.

The three coefficients follow by expanding the Hessian and Laplacian products, using |grad psi|<=1 and psi<=3R on the annulus for R>=1. The last coefficient could be 3/2; the displayed 2 is a valid upper bound. The error tends to zero since beta<1. The remaining integrand is

    chi_R [ U^T D2psi U + (|U|2/2) Delta psi ],
    D2psi >= psi^-3 I,    Delta psi=(2|y|2+3)/psi^3>0.

For each fixed rho and R>=max(rho,1), its integral dominates integral_B_rho |U|2 psi^-3. The latter is bounded by C_chi C_E 2^beta R^(beta-1), so is zero. Arbitrary rho and continuity give U=0. There is no claim of prior global integrability of the positive integrand.

## 7. Verdict boundary and comparison

The two report edits since 8e779993 identify the critical-case L2 input and the invariant-support use in Section4; the complete 4580-character delta contains no new mathematical step. The companion B review and coordinator reconciliation find no gap. The constants, pressure normalization, measure passage, arbitrary boundary and arbitrary finite omega were independently checked above.

If the separately established carrier family covers O almost everywhere and helicity vanishes on each carrier, Sections4-6 give the conditional conclusion U=0. Deriving zero helicity from a sign on each carrier uses the separately audited recurrence argument. Deriving the covering family uses the separately audited dynamical hypotheses. Neither is removed by this repeat audit, and the unrestricted conjecture remains OPEN. The B67 inherited-hypothesis defect A2559 concerns a separate report table and is not repaired by this 2D delta. No numerical computation or formal build was used.
