# Low-pressure regions at critical contraction points

## 1. Exact local and profile hypotheses

Fix 2/5<c<1/2 and any real omega. On an open G containing x0!=0 let V,P be smooth. Put Jx=e3 cross x, A=cI-omega J, X=Ax, L=(1-c)I+omega J, a=1-2c, b=2(1-c), q=b/a>6, W=curl V, k=X.V, E=|V|^2, S=P-E/2 and Q=P+E/2. Assume

    div V=0, V.W=0, DV X=-LV, -Delta P=tr((DV)^2),
    grad k=X cross W-aV, X.grad S=-bS, W.grad S=0,
    k grad S=qS grad k on supp W.                       (1)

All supports, interiors and closures below are relative to G. For fixed 0<delta<1/2 write Z_delta={P<delta E}. On supp W intersect {k!=0} write D=S|k|^(-q).

For the actual-profile consequence only, additionally require that (V,P) is the tail pair (V,P2) of a whole-space C2 velocity, C1 pressure rotating Euler profile with zero helicity, |U(y)|<=C(1+|y|)^(-p) and |DU(y)|<=C(1+|y|)^(-p-1), p=(1-c)/c. The pressure tail is formed after subtracting the finite pressure limit at infinity. Retain the smoothness in G already assumed. This is the C47/A1180 class. Its previously proved C49/A1321 consequence is

    P2>=0 at every supported common zero of V and W.     (2)

The proof of that consequence, including its support transport, original-orbit work sign, pressure normalization and tail limits, was reread. No local Poisson argument is substituted for it.

## 2. Inverse rank and a forced scalar zero

On the open set int(supp W) intersect {S!=0}, differentiating k|S|^(-1/q) in (1) gives zero gradient. It is constant on each connected component. If k=0 at one such point, k and grad k vanish on a neighborhood, and aV=X cross W there.

Now suppose W(y)!=0 and V(y)=0. Then k(y)=0 and grad k(y)=X(y) cross W(y). If this gradient is nonzero, the rank identity gives S(y)=0. If it is zero, X(y) is a scalar multiple of W(y), so -bS(y)=X(y).grad S(y)=0. Thus S(y)=P(y)=0 in either case. Such a point is outside Z_delta.

These conclusions use the full rank relation only where it is given. In particular local constancy is asserted on the interior of the support, not on an arbitrary support boundary.

## 3. Classification of supported k-zeros in Z_delta

Every point of Z_delta has S<0, including E=0 where the defining inequality reads P<0. At a supported point with k=0, the rank identity and S!=0 force grad k=0.

If W!=0, Section2 excludes V=0. Its inverse-rank conclusion applies on a full neighborhood because {W!=0} is open and lies in int(supp W). Thus k=0 nearby and X cross W=aV!=0. If W=0, grad k=-aV gives V=0, and P=S<0.

The first type forms exactly the open set

    N_delta=Z_delta intersect {W!=0} intersect int{k=0}.

This set is disjoint from closure{k!=0}, hence from the closure of every component of {W!=0,k!=0}. The second type consists of supported common V/W zeros with negative pressure. These are the only alternatives.

## 4. Actual tails and the remaining complement sets

Under (2), the second type is impossible. Suppose x0 is a common infinite-value-order zero of V and S in the closure of a component C of {W!=0,k!=0}. The earlier C55/A1744 conclusion gives x0 in closure Z_delta. For every Dbar>0 it also gives a sufficiently small radius r such that Z_delta intersect B_r(x0) lies in

    int{W=0}, or {supp W,k=grad k=0},
    or {supp W,k!=0,D<-Dbar}.

Its proof uses the double-divergence-free stress tensor and the flat positive-semidefinite tensor lemma; these were reread. Applying Section3 and (2) replaces the middle set by N_delta. Without the actual-profile hypothesis, the common-zero negative-pressure alternative must be retained.

For clarity, the radius controlling the last alternative can be chosen so Dbar sup|X|^q E^(q/2-1)<=1/2-delta. At k!=0, the inequality P<delta E yields |D|>(1/2-delta)|X|^(-q)E^(1-q/2), so D<-Dbar there. No uniform control of component constants is asserted. The theorem classifies necessary low-pressure points and excludes none of the three remaining types.

## 5. An irrotational local example for every omega

Work on a small ball about x*=(1,0,0), using a branch of log z for z=x1+i x2. Let lambda=-a/(c-i omega), k=Re(z^lambda), V=-grad k/a and P=-|V|^2/2. Then k is harmonic and X.grad k=-ak. Hence X.V=k, div V=0, W=0 and

    DV X=-(aI+A^T)V=-LV.

Also Delta V=0 and DV is symmetric, so -Delta P=|DV|_F^2=tr((DV)^2). The gradient contraction identity holds with W=0. Since X.grad E=-bE and S=-E, the scalar homogeneity holds. Both helicity and W.grad S vanish and the support rank condition is vacuous.

Here E=|lambda z^(lambda-1)|^2/a^2>0 and Q=0. Thus P=-E/2<delta E on the ball. This is a smooth local solution of every identity (1) in the irrotational low-pressure region. It has no flat velocity zero and supplies no global profile.

## 6. A vortical local example and arbitrary S/E

Use smooth cylindrical coordinates rho,theta near x*. Put sigma=c^2+omega^2,

    gamma=1+ac/sigma, eta=a omega/sigma,
    u=A0 rho^(-gamma)exp(eta theta), A0!=0,
    V=u(omega e_rho+c e_theta),
    h=Re(z^mu), mu=-b/(c-i omega),
    P=-sigma gamma u^2/[2(gamma^2+eta^2)]+B h,

where B is any real number. The identities c eta=omega(gamma-1), c(gamma-1)+omega eta=a and c gamma+omega eta=1-c give div V=0 and

    W=-(a u/rho)e3!=0, k=0, X cross W=aV.

The rotating cylindrical basis contributes exactly -omega JV to DV X, while X.grad u=-(1-c)u. Thus DV X=-LV. In that basis the planar derivative matrix is (u/rho) times

    [-omega gamma, omega eta-c;
     -c gamma, c eta+omega].

Its trace is zero and determinant is -sigma gamma, so tr((DV)^2)=2 sigma gamma u^2/rho^2. Since Delta(u^2)=4(gamma^2+eta^2)u^2/rho^2 and h is harmonic, the specified P has precisely the required Poisson equation. Both u^2 and h have X-degree -b, hence so does S. All scalars are independent of x3 and W is parallel to e3, proving W.grad S=0. Helicity vanishes, and the rank condition is identically zero because k=grad k=0.

At x*, E=sigma A0^2 and

    S/E=-1/2-gamma/[2(gamma^2+eta^2)]+B/(sigma A0^2).

It takes any prescribed real value. If chosen below delta-1/2, continuity places a smaller ball wholly in N_delta. This example works also at omega=0, has nonzero V and W everywhere in its ball, and is only a local tail-system example. The analytic computation suffices; the submitting agent's numerical test was not rerun and is not proof evidence for this verdict.

## 7. Minimum principle and C55 wording repairs

On int{W=0}, the harmonic Q and Delta E=2|DV|_F^2 give

    Delta(P-delta E)=-(1+2delta)|DV|_F^2<=0.

On a bounded open set compactly contained in G with W=0, its minimum is on the boundary. A nonnegative boundary value therefore implies a nonnegative interior value. This does not localize the low-pressure obstruction near x0: X-homogeneity makes Z_delta invariant along every orbit segment remaining in G. An orbit through any point of Z_delta intersect B_r(x0), r<|x0|, exits that ball in finite forward time because its distance from the origin grows as exp(ct). Until the first exit it stays in the same component. Thus the component closure already meets the sphere about x0.

The five-section C55 errata is correct. Its stress statement means M/E has a uniform positive lower bound, while M itself tends to zero at x0. The sharper eigenvalue-ratio bound is (3-2epsilon)/(1-2epsilon). Only nonzero constant multiples can be excluded from being semidefinite. A zero gauge satisfies a ratio inequality, so the correct flat-gauge conclusion includes positive semidefiniteness and says the gauge vanishes. For G_f=D2f-(Delta f)I, div G_f=0; its normal spherical mean is -2F'/r and its trace mean is -2F''-4F'/r. Such a vanishing gauge makes f affine. The swirl formula for D requires both omega and its amplitude nonzero. Finally the superalgebraic statement is conditional on a sequence in the indicated third set, not existence of such a sequence. These are the precise interpretations used by A1741-A1746.

## 8. Verdict and verification

C56(a)-(e), the minimum-principle remark at its exact scope, and all C55 errata are confirmed by the arguments above. The Frobenius discussion is a pointer to CO64 and is not a new theorem audited here. There is no exclusion of a common flat point, proof of global extendibility of either example, or bare-decay conclusion. Pressure signs from actual profiles remain separate from the local Poisson system.

All four submitted C56 sections, the five-section errata and this eight-section reconstruction were read. Source snapshots, hashes and reading coverage are recorded in verification. No computation or formal build was used. Existing configured model Theory Agent C supplied the submission and receives these findings through files; actual provider runtime is not independently attested.
