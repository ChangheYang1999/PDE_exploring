# Bernoulli mean decay and helicity-free vortical basins

Status: independently checked below. The spatial estimate is unconditional within the stated decaying profile class. The basin and global conclusions retain the explicit measure and helicity assumptions. They do not establish the campaign's unconditional conjecture.

## 1. Statement and notation

Let 2/5 <= c < 1/2, let omega be any finite real number, and set A=cI-omega J, where J is the skew matrix generating rotations about the third axis. Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0,
    (1-c)U+(Ay+U).grad U+omega JU+grad P=0,
    U(y)->0 uniformly as |y|->infinity.

Write B=Ay+U, Omega=curl U, O={Omega!=0}, a=1-2c>0, kappa=1+c, beta=5-2/c in [0,1), and q=|U|^2/2. Denote the complete B flow by Phi, its reverse by Psi_t=Phi_-t, and the complete Omega flow by Gamma.

There is a unique pressure constant p_infinity for which

    H0=P-p_infinity+q+Ay.U

has vanishing spatial quadratic mean. More precisely, for R>=1,

    integral_(|y|<R) |H0|^2 <= C R^(beta+2).                 (1)

For every bounded measurable Q there is a finite C_Q such that

    integral_Q |H0(Phi_t y)|^2 dy <= C_Q exp(-2a t), t>=0.  (2)

In particular the positive-time integral of this square is finite for almost every initial point.

For the next conclusion assume a GIVEN compactly supported full-flow-ergodic probability nu for Psi with nu(O)=1. Assume its regular points have simple Lyapunov spectrum (+,0,-), center direction R B and stable direction R Omega, and its local unstable conditional measures are equivalent to arclength with positive density. The unstable local plaques are C1. These are the precise properties of a given vortical SRB measure used here. Let D_nu be the maximal open subset of O having full basin volume, as constructed in A223. Thus, with Bas(nu) the continuous-time basin,

    Bas(nu) subset D_nu,
    Leb(D_nu minus Bas(nu))=0,
    nu(D_nu)=1.

If U.Omega=0 throughout D_nu, then

    H0=0 on supp(nu) and on D_nu.                          (3)

Finally, if the essential basins of such given measures cover almost every point of O and U.Omega=0 on every one of those basins, then U=0. No existence or coverage theorem for these measures is asserted. No mixing, uniform hyperbolicity of their whole supports, density of O, or C3 regularity is an assumption of this conditional conclusion.

## 2. A fixed pressure representative

The independently proved pressure normalization A031 and energy bound A040 apply to the hypotheses above. They give the canonical double-Riesz pressure gradient and

    E(R)=integral_(|y|<R)|U|^2 <= C R^beta, R>=1.          (4)

Only this upper bound from the stronger A040 theorem is needed. Put M=||U||_infinity. Dyadic summation of (4) gives

    integral_(|z|>R)|U(z)|^2 |z|^-3 dz <= C R^(beta-3).     (5)

Indeed the shell from 2^j R to 2^(j+1)R contributes at most C(2^j R)^(beta-3), and beta<3.

Let

    K_ij(z)=(3 z_i z_j-delta_ij |z|^2)/(4 pi |z|^5).

Define

    P0(x)=-|U(x)|^2/3+pv integral K_ij(x-z) U_i(z)U_j(z) dz.

The far integral converges absolutely by (5), with a harmless finite-region adjustment for a fixed x. Near x, subtract U_i(x)U_j(x), use the spherical cancellation of K and local C1 regularity, and integrate the resulting O(|x-z|^-2) majorant. This proves the local principal value exists. Local regularity and the uniformly convergent far part make P0 continuous. Testing its gradient against compact smooth tests identifies it with the canonical gradient of A031. Consequently P=P0+p_infinity for one spatial constant.

For |x|<R split the source at |z|=2R. The near part is the full double-Riesz transform of the truncated tensor, including its local distributional term. Its L2 norm is at most

    C ||U tensor U||_(L2(B_2R)) <= C M E(2R)^(1/2).

The far part is bounded pointwise by C R^(beta-3), since |x-z|>=|z|/2. Therefore

    integral_B_R |P0|^2 <= C R^beta+C R^(2beta-3).           (6)

This is one fixed representative on the entire space. No annulus-dependent pressure constants have been combined.

Also integral_B_R q^2<=C M^2 E(R), and integral_B_R |Ay.U|^2<=||A||^2 R^2 E(R). These estimates prove (1). Dividing by the volume of B_R shows its normalized quadratic mean tends to zero because beta<1. If two pressure constants had this property, the normalized L2 triangle inequality would force their constant difference to vanish. This proves uniqueness.

## 3. Exact volume expansion

Bounded U makes B at most linear, so its C1 flow is complete in both directions. Since exp(At) is exp(ct) times an orthogonal matrix, variation of constants gives

    |Phi_t y| <= exp(ct)(|y|+M/c), t>=0.

The flow Jacobian is exp(3ct), since div B=3c. For bounded Q choose R_Q>=1 with Phi_t Q subset B_(R_Q exp(ct)). Changing variables and applying (1) gives

    integral_Q |H0(Phi_t y)|^2 dy
       <= exp(-3ct) C (R_Q exp(ct))^(beta+2)
       <= C_Q exp(c(beta-1)t)=C_Q exp(-2a t).

Tonelli on each initial ball, followed by a countable union, gives the almost-everywhere finite time integral. This does not imply pointwise decay of pressure or velocity derivatives at infinity.

## 4. Complete vortex transport and essential-basin invariance

The exact identities, verified directly from the profile equation, are

    [B,Omega]=-kappa Omega,
    a U+grad H0=B cross Omega,
    Omega H0=-a U.Omega.                                  (7)

Every negative B semiorbit starting in a compact set stays in a fixed compact ball. This follows from B.y=c|y|^2+U.y>0 outside a sufficiently large ball. On a neighbourhood of that ball the local Omega flow exists for a uniform short time. For a prescribed finite s, choose T large and define

    Gamma_s y=Phi_T Gamma_(s exp(-kappa T)) Phi_-T y.

The local transport identity from (7) and uniqueness make these definitions consistent as T increases. They extend the Omega solution through any finite positive or negative time. Thus Gamma is complete and consists of C1 diffeomorphisms, with

    Phi_t Gamma_s=Gamma_(s exp(kappa t)) Phi_t.             (8)

This is the A048 completeness argument and uses no global bound on Omega.

Every finite Gamma_s preserves Bas(nu). In fact (8) under Psi_t has the factor exp(-kappa t); on the compact backward trap the resulting Omega displacement tends uniformly to zero. The time averages of every bounded continuous observable are therefore unchanged. The same reasoning with -s proves equality of the basins. Each Gamma_s preserves O and null sets. The maximal definition of D_nu as a union of open sets with full basin volume now proves Gamma_s D_nu=D_nu. Carrier invariance follows in the same way. Under the helicity assumption, (7) consequently makes H0 constant along every complete Gamma orbit in D_nu.

## 5. A positive-volume set with support-orbit values

Full-flow ergodicity gives a full nu-measure set of points generic for H0^2 in both Phi and Psi time. Here H0^2 can be multiplied by a compact cutoff equal to one on the invariant compact support. Positive unstable conditional density supplies a local unstable C1 arc gamma(s) on which a full-arclength subset T consists of such regular points in supp(nu) intersect D_nu.

At a regular base point the unstable tangent, -B and Omega are independent. After shrinking the arc and time intervals, the map

    C(s,r,tau)=Gamma_tau Psi_r gamma(s)

is a C1 diffeomorphism from an open bounded box onto an open set V contained in D_nu. On a smaller box its Jacobian is bounded above and below by positive constants. The image E of T times that smaller time rectangle therefore has positive volume and full volume in the smaller box image. Rename that smaller image V.

For y=C(s,r,tau) with s in T and any real t, conjugacy and constancy along Gamma give the exact equality

    H0(Phi_t y)=H0(Phi_(t-r) gamma(s)).                    (9)

The right side lies on the compact invariant support for all t and hence is bounded uniformly in y and t. Its positive-time square average tends to the common number m=integral H0^2 dnu. Dominated convergence over E yields

    lim_(T0->infinity) (1/T0) integral_0^T0
             integral_E |H0(Phi_t y)|^2 dy dt = Leb(E)m.

By (2), the left side is zero. Thus m=0. Continuity makes H0 vanish on the entire support, including any exceptional support points.

The use of two-sided generic support points is essential. The proof does not assert that all points in a forward physical basin are generic in reverse time, nor does it integrate a derivative against a measure singular in the vortex direction.

## 6. Propagation to the complete essential basin

Since H0 vanishes on supp(nu), (9) makes it vanish on Phi_t E for every real t. Each such set has full volume in Phi_t V, so continuity makes H0 vanish on Phi_t V. Set E0 to be the union of these open sets over all real t. It is open, invariant, contained in D_nu, and H0=0 there. It contains a support point and hence has positive nu measure. In fact ergodicity gives full measure, although only positive measure is needed for the next argument.

Choose a nonnegative compactly supported continuous function f inside E0 with integral f dnu>0. Every point in Bas(nu) has a positive limiting time average of f and hence enters E0 under Psi. Invariance puts the original point in E0. Thus Bas(nu) subset E0. Since the basin has full volume in D_nu, continuity gives H0=0 on D_nu. This proves (3). One such box suffices; no uncountable union of exceptional null sets is used.

## 7. Coverage implies the global conclusion

Under the stated coverage hypothesis, grad H0=0 on an open full-measure subset of O. Continuity gives grad H0=0 everywhere on O. We include the localization step to make clear that no density assumption on O is being inserted.

Let Z={Omega=0} and D=int Z. If O is empty, each component of U is entire harmonic and decays, so U=0. Otherwise, at every boundary point of O, (7), continuity and a>0 give U=0. In particular U vanishes on the boundary of D. Extend U restricted to D by zero outside D. This extension is locally Lipschitz: across the boundary use the local bound on DU and the distance to the boundary. Its weak derivative equals 1_D DU almost everywhere. On the remaining zero set its derivative is zero almost everywhere, as holds for any Lipschitz function on its zero set. Consequently the extension has zero distributional divergence and curl and is entire harmonic. It vanishes on the nonempty open set O, so unique continuation makes it identically zero. Thus U=0 on D and, by the boundary observation, on all of Z.

Equation (7) now gives grad H0=0 on Z as well. Hence H0 is globally constant, and (1) forces that constant to be zero. Dotting (7) with B gives U.B=0. Since

    H0=P0-q+U.B,

we obtain P0=q. The pressure equation becomes

    partial_i partial_j(U_i U_j)+Delta q=0.

Test this distributional equation against chi(y/R) sqrt(1+|y|^2), where chi is nonnegative, smooth, compactly supported and equal to one on the unit ball. The terms differentiating chi have absolute value at most C R^-1 E(2R), which tends to zero by beta<1. The remaining integrand is

    chi(y/R) [U^T D2 sqrt(1+|y|^2) U
                   +q Delta sqrt(1+|y|^2)].

It is nonnegative and strictly positive wherever U!=0. On any fixed ball its integral is bounded by the vanishing cutoff error for sufficiently large R. Therefore U=0 everywhere.

## 8. Dependencies, scope and evidence

The pressure normalization and energy estimate were reread in full in the team records and in the team records. The given-measure inputs were reread in the team records and in the team records. The exact complete-flow construction is A048; the arbitrary-boundary localization is A266 and is reproduced above. No external generalized SRB existence theorem enters.

This independently verifies LIT59 in the literature agent. All finite omega are permitted; constants may depend on omega, but the decay exponent is independent of it. The result removes mixing and global-rank premises in the decaying class. It retains pointwise zero helicity on the given essential basins and their separate almost-everywhere coverage for global nonexistence. It says nothing decisive about a profile with nonzero helicity on a basin or without the specified measures.

No numerical calculation, formal build or server was used. A focused challenge was sent to the existing configured model coordinator through the shared notes. Configuration is not provider attestation; the mathematical verification here does not assume an unreceived review.
