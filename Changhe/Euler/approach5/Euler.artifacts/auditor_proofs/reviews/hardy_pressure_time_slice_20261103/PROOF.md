# Hardy pressure cancellation and countable time slicing

Recorded: 2026-11-03T16:45:12.014254+00:00. Independent audit of LIT258, verdicts A1714-A1719. All six submitted sections, all fifteen pages of Chae arXiv:0809.0743v6, and Wilson's printed pages 201-204 were read. Wilson's Theorem A on page 201 was also inspected as an image to resolve the inclusive endpoints obscured by OCR.

## 1. Exact statement and external input

Let n>=2, 0<q<=1, and H^q(R^n) be the real global Hardy space, with its radial Schwartz maximal-function definition. The external input is the usual atomic characterization, including its equivalence with the Poisson nontangential maximal definition used by Wilson, *On the atomic decomposition for Hardy spaces*, Pacific Journal of Mathematics 116 (1985), Theorem A, p. 201. Put gamma=n(1/q-1), L=floor(gamma). Each atom a is supported in a cube of side ell, obeys ||a||_2<=ell^(n/2-n/q), and has moments zero through degree L inclusive. An element p has an expansion sum lambda_j a_j convergent in tempered distributions, with sum |lambda_j|^q<=C||p||_Hq^q. These inclusive bounds, including q=1, appear in the rendered original. We use this standard external theorem rather than claim a new proof of it.

Spatial theorem: if v is real and belongs to L^2(R^n;R^n), p belongs to H^q, and div div(v tensor v+p I)=0 in distributions, then v=0 a.e. No incompressibility hypothesis is needed for this spatial statement.

Time theorem: let I be an open interval and nu>=0. Suppose v is measurable in L^1_loc(I;L^2_sigma), v tensor v is locally integrable in space and time, p(t) is weakly measurable in tempered distributions, p(t) belongs to H^q a.e. and ||p(t)||_Hq is locally integrable in time. If partial_t v+div(v tensor v)+grad p=nu Delta v holds distributionally, then v=0 a.e. No global time integral of total energy is assumed.

## 2. Pressure tests at expanding scales

For Psi in C_c^infinity set Psi_R(x)=Psi(x/R). If ell<=R, subtract its Taylor polynomial of degree L about the atom's cube center. Cancellation and Cauchy-Schwarz give

    |<a,Psi_R>| <= C R^(-L-1) ell^(L+1) ||a||_1
                 <= C R^(-L-1) ell^(L+1-gamma)
                 <= C R^(-gamma).

The derivative bound is global, so the estimate is uniform in cube location. If ell>=R, Cauchy-Schwarz instead gives

    |<a,Psi_R>| <= C ell^(-gamma-n/2) R^(n/2) <= C R^(-gamma).

Since q<=1, sum |lambda_j|<=(sum |lambda_j|^q)^(1/q). Absolute convergence of the scalar pairings agrees with the distributional atomic series. Thus

    |<p,Psi_R>| <= C_Psi,n,q R^(-gamma) ||p||_Hq.

For q<1 this tends to zero. For q=1, each fixed atom has zero mean and the first estimate is C ell/R for large R. The uniform bound and summable coefficients give convergence to zero by dominated convergence in the series. Integer gamma presents no problem since L+1-gamma>0. Pressures with q<1 are never treated as integrable functions.

## 3. Spatial coercivity

Choose chi in C_c^infinity equal to 1 near zero, put psi(x)=|x|^2 chi(x)/2 and psi_R(x)=R^2 psi(x/R). The Hessians D^2 psi_R are uniformly bounded and tend pointwise to I. Also Delta psi_R=Psi_R for the fixed test Psi=Delta psi. The distributional stress relation gives

    integral (v tensor v):D^2 psi_R + <p,Delta psi_R> = 0.

Velocity integrability permits dominated convergence of the first term to ||v||_2^2. Section 2 makes the second tend to zero. Hence v=0. Only the sequence R=1,2,... is required. This argument explains why no divergence constraint on v is needed here: positivity comes from the trace of v tensor v.

## 4. Time slicing before the spatial limit

For each positive integer R, test the evolution equation with eta(t) grad psi_R(x). Divergence freedom annihilates both the time-derivative pairing integral v.grad psi_R and the viscosity pairing integral v.grad Delta psi_R. They are time-integrable by the stated L^1_t L^2_x premise. The remaining identity is

    integral eta(t) [ integral (v tensor v):D^2 psi_R
                       + <p(t),Delta psi_R> ] dt = 0.

The first bracketed term is locally time-integrable by the explicit local spacetime product hypothesis, and the second by Section 2 and the Hardy norm hypothesis. The bracket vanishes for almost every time. Intersect these sets over integer R, and with the sets where v(t) is in L^2 and p(t) in H^q. For each resulting time, the sequence of spatial cutoff identities holds and Section 3 proves v(t)=0. No spatial limit was interchanged with a time integral of total kinetic energy.

## 5. Exact primary-source comparison

Chae's v6 Definition 1.1, p. 2, displays L^1_t L^2_sigma. The proof on p. 7 instead says L^infinity_t L^2_sigma holds "by hypothesis", and uses time integrability of total energy. That does not follow from the displayed definition alone. The source's Hardy argument on p. 11 also needs a precise convention for its homogeneous Holder dual notation at integer gamma. Sections 2-4 repair these issues in the natural weak class with locally integrable quadratic products; they do not refute the stated Liouville conclusion.

The repair has an explicit dependency on atomic Hardy theory and equivalence of its standard definitions. The endpoint and moment normalizations are verified against the actual Wilson statement. No MHD conclusion is certified here. The finite-L^1-pressure case and its separate spatial Fourier identity remain as previously audited in A1651-A1652.

## 6. Rotating-profile scope and verdicts

For a divergence-free rotating Euler profile, taking divergence yields Delta P=-div div(U tensor U): the simultaneous rotation terms cancel, as do the linear dilation divergence terms. Consequently the spatial theorem applies for every finite omega if U is in L^2 and the actual pressure representative is in global H^q for some 0<q<=1. The pressure class fixes an additive constant; adding an arbitrary constant is not allowed while retaining this hypothesis. Neither finite energy nor global Hardy pressure is inferred from U tending uniformly to zero.

A1714 CONFIRMED: atomic rescaled-test cancellation, Section 2, with the external input of Section 1. A1715 CONFIRMED: spatial theorem, Section 3. A1716 CONFIRMED: time-slice theorem at the exact stated weak regularity, Section 4. A1717 CONFIRMED: primary-source proof mismatch and repair scope, Section 5. A1718 CONFIRMED: conditional all-omega profile corollary, Section 6. A1719 OPEN: derivation of the extra global integrability premises from bare decay.

No numerical computation, flow-completeness assumption, server or formal build is involved.
