# Controlled scalar nodes localize the nonsymmetric tail obstruction

Status: independently CONFIRMED at A567-A568 after complete source and proof postreads. Existing configured-model exchange continues; no new focused reply is presumed. No pressure equation or global E0 is assumed in the standalone theorem; controlled geometry at every scalar zero is essential.

## 1. Exact statement

Let 2/5<c<1/2, a=1-2c, b0=2(1-c), beta=a/b0 in(0,1/6), A=cI-omega J, omega finite, and Q_t=exp(omega tJ). On D=R3 minus{0}, suppose V in C1alpha_loc for some alpha in(0,1), S in C1, W=curl V, k=(Ax).V and E=grad k satisfy

    div V=0,
    V(exp(tA)x)=exp(-(1-c)t)Q_t transpose V(x),
    S(exp(tA)x)=exp(-b0 t)S(x),
    W.grad S=0,
    grad k cross grad S=0 on {W!=0}.                (1)

At every zero of S assume a C1 coordinate diffeomorphism x=Phi(z) onto a neighborhood, bounded DPhi and inverse on smaller neighborhoods, and positive constants such that

    C^-1 rho^m<=|S(Phi(z))|<=C rho^m,
    rho=|z_normal|, j=dimension(z_normal) in{1,2},
    m>=1, m beta<1 if j1, m beta<1+alpha if j2.     (2)

Charts and exponents can vary. In each chart the entire zero set is exactly the central C1 surface or curve. An empty zero set is allowed. Then every point with W!=0 has both k!=0 and S!=0, and E=0 implies V=0. If all zeros are regular, V in C1 suffices, using only j1,m1 charts. More generally the surface-only conclusion needs only C1 V at any m beta<1. No axisymmetry, pressure equation or helicity hypothesis is required for this standalone result.

For actual full target globally zero-helicity Euler profiles with natural U/DU bounds, the established tail has C1alpha regularity for every alpha<1 and satisfies(1). In this application curve charts may satisfy m beta<2, choosing alpha separately locally. Then all A518/A536 lower escaping-sheet witnesses are excluded: vortical carrier rho=-a and regular vortical zero-g lambda1 remain. No separating or general flat case, uncontrolled node, or bare-decay derivative gap is settled.

## 2. Rank fixes a spatial constant

Differentiating homogeneity and the definition of k gives

    Ax.grad S=-b0 S, Ax.grad k=-a k,
    Ax cross W=aV+E.                               (3)

The last identity follows from Ax cross curl V=grad((Ax).V)-A transpose V-DV Ax and the linear velocity homogeneity. This also checks the rotation sign.

Where W and S are nonzero, grad S!=0 by(3). Rank gives grad k=q grad S, and dotting with Ax gives q=beta k/S. Consequently

    grad(k |S|^-beta)=0.                            (4)

This is a constant on each connected spatial component, not only on a characteristic.

## 3. The controlled nodes force local k0

At a point with S0,W nonzero, shrink its chart so W is nonzero throughout. For j1, its two sides are connected. Equation(4) gives k=C_+/- |S|^beta, so continuity makes k0 on the central surface. Along a normal segment, C1 regularity gives |k|<=C rho. A nonzero integration constant instead gives |k|>=c rho^(m beta), contradicting m beta<1. Both constants vanish.

For j2, the punctured normal disk and hence the entire punctured product are connected. A single nonzero constant would make k have one strict sign off the curve and zero on it. Each curve point is a local extremum, so grad k=0 there. Because V and thus k are C1alpha in the physical coordinates, the Taylor bound |k(x)|<=C|x-x0|^(1+alpha) contradicts the lower power bound in(2) along a normal segment. The C1 coordinate map is locally Lipschitz, which suffices to compare those distances. Hence k0 on this chart as well.

For actual tails with all alpha<1, any strict m beta<2 admits an alpha with m beta<1+alpha. A finite compact cover can use the maximum of its finitely many chosen alpha values; no exponent on all of D is required. Constants outside the selected chart play no role.

## 4. Propagation through one vortical component

Let C be a connected component of the open set {W!=0}. Points where k is zero on a neighborhood in C form an open subset. It is also relatively closed: at a limit point k0 by continuity; if S is nonzero, (4) propagates the zero on a small connected ball, while if S0 Section3 does so. Thus a zero of k or S anywhere in C forces

    k=E=0, aV=Ax cross W throughout C.             (5)

We now exclude this whole-component alternative. No claim is made yet about any other component or an irrotational open region.

## 5. Zero extension retains the actual distributional curl

Set Y=V on C and0 elsewhere in D, and Z=W on C and0 elsewhere. At every boundary point of C, W=0. Indeed any point where W is nonzero has a connected small ball in the open set; a ball meeting C is part of C. Taking boundary limits in(5) then gives V0. Hence Y and Z are continuous.

The extension Y is locally Lipschitz. In a convex ball where V has Lipschitz constant L, two points inside C obey that estimate, two outside give zero difference, and a segment from an inside point x to an outside point y first meets the boundary at q. Since V(q)=0, |Y(x)-Y(y)|<=L|x-q|<=L|x-y|. No boundary regularity is needed.

Its derivative equals DV almost everywhere in C and0 almost everywhere outside C. The latter follows from the usual zero-set derivative fact for Lipschitz functions, proved by absolute continuity on coordinate lines at their density points and Fubini. Thus, on D in distributions,

    div Y=0, curl Y=Z.                             (6)

There is no boundary-supported measure. Since W(exp(tA)x)=exp(-t)Q_t transpose W(x), each scaling orbit is a continuous path inside the same vortical component. It preserves C and its complement. Therefore Y has the same twisted homogeneity as V and, globally on D,

    Ax cross Z=aY, Z.grad S=0.                     (7)

The original S is retained; no pressure for Y is invented. It suffices to prove the next weak version of A547.

## 6. The global degenerate lemma at Lipschitz velocity regularity

Assume a locally Lipschitz Y, continuous actual distributional curl Z, div Y0, the homogeneities in(1), and(7). Suppose each S-zero chart satisfies eta=m beta<j. Then Y0. This uses the imported weighted Harnack theorem at its exact completed-energy scope.

Taking the dot product of(7) with Ax and its cross product with grad S gives

    Ax.Y=0, grad S cross Y=(S/beta)Z.               (8)

For epsilon>0 the weak product rule gives

    curl[(S^2+epsilon^2)^(-beta/2)Y]
       =epsilon^2(S^2+epsilon^2)^(-beta/2-1)Z.       (9)

On a nodal chart |S|^-beta(|Y|+|Z|)<=C rho^-eta, locally integrable since eta<j. The nodal set is null, by its charts and a countable subcover. Dominated convergence makes the right side tend to zero in distributions and the field tend in L1_loc to G=|S|^-beta Y. Therefore curl G0 across all nodes, not merely off them. Also G is locally Lq for some q>1, with q<j/eta chartwise.

Mollify G on larger balls, integrate its smooth closed approximants, normalize their potential means and use Poincare's inequality. This gives local W1q potentials. Since D is simply connected, their additive constants glue globally: subdivide a contracting homotopy into small balls and cancel differences around each elementary loop. We obtain one potential psi with

    grad psi=G, div(|S|^beta grad psi)=0.            (10)

Off S0, G is locally Lipschitz, so psi has a C1 representative. In a nodal chart u=psi composed with Phi obeys |Du|<=C rho^-eta. We must prove membership in the weighted energy completion before using regularity.

For j1, eta<1. Integrating normal derivatives gives two one-sided traces with error C rho^(1-eta). Lift tangential points separated by distance d to height d, compare them using the derivative bound and descend; each trace is continuous with the same modulus. Since u is W1q across the surface, almost-everywhere absolute continuity on normal lines identifies the traces. Leave u unchanged outside |z_normal|<epsilon and interpolate linearly between its values at the two boundary faces. The approximant is Lipschitz on a smaller chart and its weighted gradient error is bounded by

    C integral_0^epsilon s^eta(epsilon^(-2eta)+s^(-2eta))ds
        <=C epsilon^(1-eta) ->0.

The weighted function error also tends to zero.

For j2, integrate from a fixed positive normal cylinder to obtain |u|<=C F_eta(rho), where F_eta is1 for eta<1, 1+|log rho| for eta1 and 1+rho^(1-eta) for1<eta<2. The weighted gradient norm is finite because integral_0^rho0 rho^(1-eta)drho is finite, and the weighted function norm is finite as well. Cut u off to zero below normal radius epsilon. The part of the gradient error containing Du is O(epsilon^(2-eta)). The cutoff derivative costs at most C epsilon^eta F_eta(epsilon)^2, tending to zero as epsilon^eta, epsilon(1+|log epsilon|)^2, or epsilon^(2-eta) in the three cases. Each cutoff function is locally Lipschitz on the smaller chart. Thus u belongs to the completed weighted H1,2 class even where the preliminary bound allowed an unbounded potential.

After the C1 coordinate change, the coefficient matrix in(10) is

    |S(Phi)|^beta |det DPhi| DPhi^-1 DPhi^-transpose.

It is measurable symmetric and comparable to rho^eta I. The weight rho^eta is A2 precisely in the needed range |eta|<j: balls away from the normal plane have weight and reciprocal comparable to their center values; for balls meeting the plane the two average bounds follow from normal radial integration and are C R^eta and C R^-eta. Their product is bounded. A uniformly elliptic matrix factor can be extended outside a smaller chart while preserving these comparisons.

The retained primary Fabes-Jerison-Kenig1982 statement assumes exactly such measurable symmetric coefficients comparable to an A2 weight and weak solutions in the completed weighted H1,2 space. Definition1.3 and the Holder and Harnack statements(1.7)-(1.9), printed154-156, were reread in full with the coefficient assumptions on152. The DOI is10.5802/aif.883. The underlying FKS regularity proof is imported, not independently reproved. Lipschitz tests follow from smooth tests by bounded-gradient mollification, and completed-energy tests follow by density and Cauchy-Schwarz. Therefore the source theorem applies.

It supplies a continuous representative of psi across the nodes. Those local representatives agree on overlaps. By(8), Ax.grad psi0 almost everywhere. The Sobolev chain rule along the smooth flow exp(tA) gives psi(exp(tA)x)=psi(x) almost everywhere for each t; continuity extends it everywhere. Every point scales to the unit sphere, so psi attains a finite global maximum M on D. The nonnegative weak solution M-psi has zero infimum on a small ball centered at a maximum. Local Harnack makes it identically zero on a smaller ball. The maximum set is nonempty, open and closed in connected D, so psi is constant and Y0. This proves the lemma at exactly the zero-extension regularity.

## 7. Finish and profile scope

Apply Section6 to the extension from Section5; (2) implies eta<j. It gives Y0 and hence Z=curl Y0, contradicting the nonempty vortical component C. Thus no such component contains a zero of k or S. If E0,V nonzero at a point, (3) gives W nonzero and Ax.grad k=-a k gives k0, the same contradiction. This completes the standalone proof.

For actual profiles the established pressure, C1alpha tail, scalar transport and rank limits supply(1) on every compact subset of {W!=0}. The additional controlled nodes are still required. Surface orders m<=6 and curve orders m<=12 satisfy the strict inequalities in the target c interval, but order alone is insufficient without charts, comparability and the absence of crossings or flat zeros. A496,A517,A518,A534,A536 then give the stated lower-sheet consequences. A537 inherits only its explicit nearby-vortical-level implication. The remaining rho=-a and lambda1 cases are not excluded. No all-profile nonexistence or universal C2 coverage follows.

## 8. Verification and exchange

The full LIT149 proof was read, including its boundary derivative argument, weighted completion and precise imported theorem. The primary text defining the energy space and stating Harnack was reread locally. The independent reconstruction above is posted for existing configured-model coordinator/Theory Agent C comparison. A focused new reply is not presumed.
