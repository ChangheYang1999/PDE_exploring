# Constant Bernoulli regions and singular attracting basins

## Exact profile class and claims

Let U belong to C2(R3;R3), let P be C1, and suppose

    div U=0,
    (1-c)U+omega JU+((Ay+U).grad)U+grad P=0,
    A=cI-omega J, J(y1,y2,y3)=(-y2,y1,0).

Write delta=1-2c, kappa=1+c, B=Ay+U, Omega=curl U, H=P+|U|^2/2+(Ay).U, g=U.B, and h=U.Omega. The profile identities used below, previously audited in A003-A004, are

    delta U+grad H=B cross Omega,
    Omega.grad H=-delta h,
    B.grad H=-delta g,
    DU Omega=Omega+omega J Omega+(B.grad)Omega,
    D Psi_t Omega=exp(-kappa t)Omega composed with Psi_t,

where Psi_t is the backward carrier flow. These formulas do not require a particular additive pressure constant. The regularity of grad H follows from the Lamb identity.

Lemma Z, auditing B28. If delta is nonzero and H is constant on an open set V, the closure of V contains no point p with B(p)=0 and Omega(p) nonzero. No decay or global flow assumption is needed. In particular this holds for every 0<c<1/2 and every real omega.

Theorem, auditing B29. Assume 0<c<1/2, arbitrary real omega, and U(y)->0 at infinity. Suppose the backward carrier flow has a compact singular-hyperbolic attractor Lambda with the following exact meaning:

* Lambda is the maximal invariant set in a relatively compact trapping neighborhood and is the omega-limit of a regular orbit in Lambda.
* Every carrier zero in Lambda is hyperbolic, at least one exists, and Omega is nowhere zero on Lambda.
* There is a continuous invariant dominated splitting E^s direct-sum E^cu over Lambda, with dim E^s=1 uniformly contracting and dim E^cu=2 uniformly area-expanding.

Let V be its full topological basin. Then h cannot vanish identically on V. Equivalently there is no profile with this geometric configuration and h=0 throughout V. This conclusion excludes even one such basin; it does not require a global basin-covering result. The zero profile does not realize the hypotheses either, since they require nonzero vorticity on Lambda.

The external singular-hyperbolic results needed for this conditional exclusion have been checked against the actual manuscripts as detailed in section 4. They are established inputs under the displayed hypotheses, not additional unverified assumptions. The existence of such a dominated transitive attracting configuration for arbitrary mixed carrier limit sets is not asserted.

## 1. Proof of the local obstruction

On the constant-H open set, grad H=0, hence h=0 by the scalar Lamb identity. Since h is C1, grad h=0 there as well. Both identities extend by continuity to every point p in its closure. If B(p)=0, the vector Lamb identity and delta nonzero give U(p)=0. Thus

    Dh(p)[Omega(p)]=Omega(p).DU(p)Omega(p)=0.

The vorticity equation at p instead gives DU(p)Omega(p)=Omega(p)+omega J Omega(p). Dotting with Omega and using skew symmetry of J gives |Omega(p)|^2=0. This contradicts a vortical zero and proves Lemma Z. No boundary differentiability of V is used, only convergence of interior points to p.

## 2. Vortex lines and the strong stable direction

Decay makes U bounded, so B and -B have complete flows by linear growth. The topological basin V is open and invariant under every finite Psi time. We first justify the complete vortex action on V without assuming that Omega is bounded on this generally unbounded domain.

The local commutation relation is

    Psi_t Gamma_s y=Gamma_{s exp(-kappa t)}Psi_t y.        (1)

For y in V its sufficiently late Psi orbit lies near the compact Lambda, where short Omega arcs exist for a fixed uniform time and have uniformly bounded speed. Given any fixed real s, take t so large that |s|exp(-kappa t) is inside this short time interval, and define

    Gamma_s y=Psi_{-t}(Gamma_{s exp(-kappa t)}Psi_t y).

Local uniqueness and (1) make the definition independent of increasing t and compatible for neighboring values of s. It extends the Omega solution to every finite s. Applying (1) at still larger times shows that its distance from Lambda tends to zero, so Gamma_s y remains in V. This proves completeness and vortex saturation on the basin. Merely bounded Omega on an open neighborhood would not by itself prove invariance or completeness there.

The APPV physical probability mu has full support Lambda and, almost everywhere, one negative exponent, the zero flow exponent, and one positive exponent; its E^cu exponents are zero and positive. The Cauchy identity and the positive upper and lower bounds of |Omega| on Lambda show that every nonzero Omega vector has Lyapunov exponent exactly -kappa. At mu-regular points it must therefore lie in E^s. Continuity and full support give

    E^s=R Omega throughout Lambda.                        (2)

For x in Lambda, a sufficiently short Omega arc through x shadows Psi_t x with distance at most C|s|exp(-kappa t), uniformly for t>=0, by (1). It is tangent to E^s and is the local strong stable plaque by the uniqueness part of the dominated strong stable manifold theorem. There is no hidden claim that an arbitrary exponentially approaching point belongs to the strongest stable leaf near a singularity. Here the entire invariant Omega arc has the prescribed strong direction and the uniform dominated contraction. Extending by inverse carrier iterates, or directly using (1), identifies the complete strong stable leaf of x with its complete Omega line.

In particular, for each hyperbolic periodic orbit gamma in Lambda, every point in its weak stable manifold has an asymptotic phase q on gamma and belongs to W^ss(q). On that periodic orbit the other two exponents are zero and positive, so this is the ordinary stable-manifold and asymptotic-phase description. This use concerns periodic orbits, not the two-dimensional stable sheet of a singularity.

## 3. Finite periodic stable families force a constant scalar

The AST result supplies finitely many hyperbolic periodic orbits gamma_1,...,gamma_m in Lambda whose weak stable manifolds have dense union in a neighborhood of Lambda. Their union is also dense in V. Indeed, given a nonempty open subset of V, follow one of its points sufficiently far into that neighborhood, shrink to an open image subset there, intersect the dense union, and pull back. Stable manifolds of full periodic orbits are invariant under the full flow.

Suppose h=0 on V. The scalar Lamb identity makes H constant along every complete Omega line in V. Let L_i>0 be the period of gamma_i. By the asymptotic-phase description, a point y in W^s(gamma_i) and Psi_{L_i}y lie on the same Omega line through their common periodic phase. Consequently

    H composed with Psi_{L_i}=H on W^s(gamma_i).

This identity extends to its closure C_i relative to V. Each C_i is closed relative to V and invariant. The finite union of the C_i contains Lambda. Choose a point with dense orbit in Lambda; it belongs to at least one C_j. Invariance and relative closedness imply Lambda is contained in C_j. Therefore H composed with Psi_{L_j}=H on all of Lambda.

Differentiating along the carrier flow yields g composed with Psi_{L_j}=g on Lambda. The function

    Q(x)=integral_0^{L_j}|g(Psi_t x)|^2dt

is continuous and invariant under every Psi time on Lambda: shifting the integration interval preserves it by periodicity. Transitivity makes it constant. At the carrier zero p0 in Lambda, g(p0)=0, hence Q(p0)=0. It follows that g=0 on Lambda. Thus B.grad H=0 there, and transitivity makes H one constant, say a0, on Lambda.

Every y in W^s(gamma_i) is on the complete Omega line of a periodic phase q in gamma_i. Constancy on that line gives H(y)=H(q)=a0. The finite stable union is dense in V, so H=a0 throughout V by continuity. The vortical zero p0 lies in Lambda, hence in the closure of V. Lemma Z gives the contradiction.

This proof uses the zero itself to set Q=0. No energy estimate, decay rate, pressure normalization, finite helicity integral, or pointwise sign of pressure is used. Decay is retained in the stated profile class and provides an immediate global carrier-completeness hypothesis.

## 4. Primary-source hypotheses and localization

The relevant original files are copied to verification with SHA256 hashes in the team records. Their titles, versions, exact statements, and the surrounding definitions were read directly.

APPV: V. Araujo, M. J. Pacifico, E. R. Pujals, M. Viana, Singular-hyperbolic attractors are chaotic, arXiv:math/0511352v3, 22 March 2007. Definitions 1.1-1.3 specify transitive attraction, a one-dimensional stable bundle, and singular hyperbolicity. The paragraph immediately before Theorem B imposes C2 regularity. Theorem B gives the unique ergodic hyperbolic physical probability and a full-volume basin in the topological basin. The paragraph after it specifies zero and positive exponents on E^cu. Theorem C gives full support. These are precisely the features used in section 2. The same inputs were independently audited earlier in A135; the relevant text was reread for this new application. The printed volume-expansion definition has the already recorded sign typo; the present hypothesis is actual positive exponential area expansion.

AST: V. Araujo, A. Souza, E. Trindade, Upper large deviations bound for singular-hyperbolic attracting sets, arXiv:1711.09626v2, 10 December 2018. Section 1.1 specifies C2 fields, codimension-two stable splitting, and hyperbolic singularities. Section 2.2 and Theorem 2.8 construct finitely many return sections and a piecewise C1 expanding quotient with derivative greater than two. Proposition 2.10 gives a finite family of periodic quotient orbits with dense preimages. Remark 2.11(1) lifts them to periodic return-map orbits and dense stable manifolds on the sections; part (2) explicitly states and explains the corresponding dense union of weak stable manifolds in a neighborhood of Lambda. This is exactly the finite-family statement used in section 3. It does not require the stronger, separately unverified assertion that every periodic orbit has a stable manifold dense in the whole attractor.

The connectedness required by the stated Theorem 2.8 causes no extra hypothesis here: Lambda is an omega-limit of a precompact continuous-time orbit. It is the intersection of the nested compact connected closures of that orbit's tails, hence is connected. The particular density conclusion is already established before the later singular stable-manifold density theorem. Neither a large-deviation estimate nor exponential recurrence to singularities is used here.

Both manuscripts use compact boundaryless manifolds. As in A135, preserve the field on a neighborhood of a compact trapping region and extend it by a smooth cutoff in a coordinate chart of S3. This does not change Lambda, its local dynamics, or its local stable family. The full original basin conclusion then follows by finite-time pullback as in section 3. This is a theoretical localization argument, not a modification of the actual profile.

The source check covers the stated theorems and their exact application. It is not an independent reconstruction of the entire APPV proof or of the book lemma cited in AST Proposition 2.10. No claim here relies on the misleading filenames or unrelated PDFs noted in the author's referee source list.

## 5. The area normalization and remaining scope

The parenthetical exact Euclidean E^cu-Jacobian formula in B29 needs a metric qualification. Let theta(x) be the angle between E^s_x=R Omega(x) and E^cu_x, and let b(x)=sin theta(x)>0. Direct comparison of three-dimensional volumes gives

    Jac_Ecu(Psi_t,x)
      =exp(delta t) |Omega(x)|/|Omega(Psi_t x)|
         times b(x)/b(Psi_t x).                          (3)

The angle is bounded away from zero on the compact dominated set, so (3) gives the stated uniform expansion with an additional harmless constant. If area is measured with the quotient flux form i_Omega vol, the scaling is exactly exp(delta t). Equivalently, using orthogonal projection to Omega-perp removes the angle from the comparison of Euclidean quotient areas. The source's formula without the angle should not be presented as the Euclidean area of an arbitrary invariant complement. This qualification does not affect the theorem, which explicitly assumes singular hyperbolicity, or the already audited A134 construction of it under the spectral gap at every zero.

The non-dominated case, nonhyperbolic singularities, and basins on which h changes sign remain outside the theorem. The implication is not a general classification of every mixed backward limit set. For regular basins, the conclusion supplied by Lemma Z requires a separately proved constant-H basin and a vortical zero in its closure; it does not exclude a single regular constant-H basin whose closure has no such zero.

## Verdicts

A365 CONFIRMED: B28, the unconditional local constant-H obstruction for delta nonzero.

A366 CONFIRMED: B29, the conditional exclusion under the precise singular-hyperbolic attractor hypotheses above. The two external inputs are now checked directly. The complete vortex-leaf construction and the area-metric qualification have been made explicit. This is not a proof of the unrestricted nonexistence conjecture.
