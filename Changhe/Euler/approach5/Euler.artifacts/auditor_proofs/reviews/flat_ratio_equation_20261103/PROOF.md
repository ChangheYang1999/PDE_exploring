# A flat-point ratio equation and a closed normalized velocity form

## 1. Statement and dependencies

Fix 0<c<1/2 and a finite real omega. Write Jx=e3 cross x, A=cI-omega J, X(x)=Ax, a=1-2c, b=2(1-c), eta=a/b, q=1/eta and m=1/c. Thus 0<eta<1/2, m>2, b-a=1, 1-2eta=c/(1-c), and eta(m-1)=(m-2)/2. Let G be a smooth X-flowbox around a segment Gamma of the orbit through x0!=0. The transverse section is a small disk and Gamma is its center times an interval.

For the CO57 calculation suppose V,S are smooth on G and satisfy

    div V=0, W=curl V, k=X.V=0,
    X.grad V=-(1-c)V-omega JV, X.grad S=-bS,
    grad k=X cross W-aV, W.grad S=0.             (1)

Suppose S<0 on G minus Gamma, S=0 on Gamma, and V,S vanish to infinite order at x0. Put H=-S, E=|V|², R=E/H off Gamma. For the pressure identity additionally assume

    P=S+E/2, -Delta P=tr((DV)^2).              (2)

We confirm the exact weighted planar m-Laplace reduction, the positive C1,1 ratio criterion, and the coupled second-order identity in CO57. We also prove the following stronger conditional statement. Assume only smooth V on G, its homogeneity and divergence identities in(1), k=0, and infinite-order vanishing at x0. Define the continuous one-form

    alpha=E^(-eta) V.dx where V!=0, alpha=0 where V=0.

If alpha is closed distributionally on G, then V=0 on a smaller flowbox. This last result has no S, pressure, ratio or isolated-zero premise. Sections7-9 prove it and show how the functional dependence R=F(phi) supplies closedness on an isolated punctured flowbox without any upper or lower bound for R.

The external analytic input is planar strong unique continuation for div(|Du|^(m-2)Du)+beta.|Du|^(m-2)Du=0 with locally Lipschitz real beta. Its actual statement is Theorem1.2 of Guo and Kar, Quantitative uniqueness estimates for p-Laplace type equations in the plane, arXiv1512.00673v2, printed page4. The primary pages and a direct first-order proof of the stronger positive Lipschitz-weight result were checked in A1437-A1440, in the team records, Sections4-7 and its verification folder. The critical Sobolev extension is A1444-A1449, in the team records. These citations are analytic inputs, not assumptions about an Euler tail.

## 2. Normal form and exact pressure flux

From k=0 and(1), X cross W=aV. Crossing this equation with grad H on the left, and using W.grad H=0 and X.grad H=-bH, gives

    grad H cross V=q H W.

Thus curl(H^(-eta)V)=0 and X.(H^(-eta)V)=0 off Gamma. Locally V=H^eta grad phi and X.phi=0. No single-valued global phi is yet asserted.

For divergence-free V, tr((DV)^2)=div((V.grad)V). Equations(2) are therefore exactly div F=0 with

    F=grad(E-H)-V cross W
     =(((1-eta)R-1)I+eta V tensor V/H) grad H+H grad R.       (3)

Here V cross W=(eta/H)(E grad H-(V.grad H)V). Since b-a=1, q/(q-1)=b. The two degeneracy levels in the CO56 negative-S flux are therefore R=1 and R=b. The region between them is 1<=R<=b. Formula(3) uses the pressure divergence, not an unproved equation F=0.

## 3. Orbit-space equation and the bounded-ratio extension

Use Psi(t,y)=exp(tA)n(y), where n parametrizes a transverse sphere patch with n(0)=x0. The pulled back metric is exp(2ct)g(y), with g00=|An|², g0i=An.partial_i n and gij=partial_i n.partial_j n. Set mu=sqrt(det g), B^ij=g^ij for i,j=1,2, and z^j=g^0j. The matrix B is smooth positive definite. Write H(Psi(t,y))=exp(-bt)h(y) and phi(Psi(t,y))=u(y). The contravariant components of V have factor exp(-(b eta+2c)t)=exp(-t). The volume density has factor exp(3ct). Thus

    partial_i(mu h^eta B^ij u_j)+(3c-1)mu h^eta z^j u_j=0,
    R=h^(2eta-1)|Du|_B².                                 (4)

If R<=M, then |Du|<=C sqrt(M) h^(1/2-eta). Flatness of H makes this gradient flat to every order. The circulation of H^(-eta)V around a transverse circle tends to zero; it is constant with radius by closedness. It is therefore zero. This is the only period of the punctured flowbox, so phi is single valued. Integration of Du radially and along circles extends u to a C1 function at zero, with u-u(0) and Du flat. In(4) the inner boundary flux is a smooth geometric factor times V; it tends to zero in the distributional integration by parts. Thus(4) holds weakly on the full disk.

The exponent needed here is eta<1/2. The source's stronger eta<1/6 is a fact in the campaign interval, not a restriction needed for its asserted all-c extension.

## 4. Weighted m-Laplace equation and a regular ratio

Put tau=eta/(1-2eta)=(m-2)/2. Solving(4) gives h^eta=R^(-tau)|Du|_B^(m-2). In smooth isothermal coordinates for B inverse, write B=lambda^(-2)I. Then(4) is

    div(w T(Du))+w d.T(Du)=0,
    T(v)=|v|^(m-2)v,
    w=mu lambda^(-m)R^(-tau), d=(3c-1)lambda² z.           (5)

All coordinate factors are smooth, and lambda,mu are positive. If R has a positive C1,1 extension at zero, shrink the disk to give positive lower and upper bounds. Then beta=grad log w+d is locally Lipschitz. Dividing(5) by w is valid weakly and gives the exact Guo-Kar drift equation. The C1 solution u-u(0) is flat at zero, so Theorem1.2 makes it constant. This contradicts H>0 and R>0 off Gamma. The conclusion is a proved conditional exclusion with a verified theorem input; the erroneous number in the original nested citation is not used.

Positive Lipschitz R and, more generally, positive bounded transverse W1,2 R already suffice by A1437-A1449. Their proofs handle the combined weight and drift directly before invoking first-order factorization. Nothing here derives this regularity from the Euler assumptions.

## 5. The coupled Hessian identity

For this section use U=grad phi, G1=grad H and B1=D²phi. Divergence-free V says

    tr B1=-eta (G1.U)/H.

The derivative matrix of V is H^eta B1+eta H^(eta-1)U tensor G1. Hence

    tr((DV)^2)=H^(2eta)|B1|²
       +2eta H^(2eta-1)B1(U,G1)
       +eta² H^(2eta-2)(U.G1)².                           (6)

Differentiating the trace identity along U gives

    U.grad Delta phi=-(eta/H)(D²H(U,U)+B1(U,G1))
                         +(eta/H²)(U.G1)².

In Delta P=Delta(-H+H^(2eta)|U|²/2), apply the product rule and substitute this last formula. The result is

    Delta P=-(1-eta R)Delta H-eta H^(2eta-1)D²H(U,U)
       +H^(2eta)|B1|²+3eta H^(2eta-1)B1(U,G1)
       +eta(2eta-1)(R/H)|G1|²+eta H^(2eta-2)(U.G1)².

Combining with minus(6) gives exactly

    C:D²H=2H^(2eta)|B1|²+5eta H^(2eta-1)B1(U,G1)
       +eta(2eta-1)(R/H)|G1|²
       +eta(1+eta)(V.G1)²/H²,
    C=(1-eta R)I+eta V tensor V/H.                       (7)

This is a direct identity, independently of the source's finite symbolic tests. The eigenvalue in the V direction is 1; the two perpendicular eigenvalues are 1-eta R. Therefore R<=b implies C>=2cI for every 0<c<1/2. The estimate 2c>4/5 belongs only to the campaign interval.

## 6. What ellipticity alone does not supply

The right side of(7) has no fixed sign even under its trace constraint. At a point let H=1, U=(sqrt(R),0,0), G1=(0,g,0), B1=0, with R>0 and g!=0. The trace constraint holds, and the right side is eta(2eta-1)R g²<0. Conversely G1=0 with nonzero trace-free B1 makes it positive. These are algebraic jet tests, not Euler profiles or local solutions. They show why the displayed ellipticity bound alone is not a signed scalar inequality for H. They do not prove that every possible use of the coupled system fails.

## 7. A closed normalized velocity gives a flat invariant potential

Now use only the hypotheses for alpha in Section1. Since |alpha|=|V|^(1-2eta), alpha is continuous, and infinite-order flatness of V makes its coefficients flat to every order at x0. Its distributional closedness gives a C1 potential psi on a small ball. To justify this at zeros of V, mollify the continuous closed form on a slightly larger ball. Each mollified closed form has a smooth potential, obtained by integration along radial segments and normalized at x0. The potentials and their gradients converge uniformly on a smaller ball, giving grad psi=E^(-eta)V everywhere with the stated zero convention.

Because k=0, X.psi=0. Shrink to an X-flowbox inside this ball; psi(Psi(t,y))=v(y). Subtract psi(x0). Radial integration of the flat gradient proves that v and Dv are flat to every order at zero. This step requires no regularity of any scalar S and allows arbitrary additional zeros of V.

The power relation is exact:

    V=|grad psi|^(m-2)grad psi.                          (8)

Indeed |grad psi|=|V|^(1-2eta), and (1-2eta)(m-1)=1. Both sides vanish on the zero set of V. Thus div V=0 is a weak three-dimensional m-Laplace equation for psi.

## 8. Reduction to smooth drift and continuation

Since psi is invariant under X, its contravariant gradient in the above coordinates has factor exp(-2ct). Its norm has factor exp(-ct), so the contravariant components of(8) have factor exp(-mct)=exp(-t). Consequently the orbit-space equation is

    partial_i(mu |Dv|_B^(m-2)B^ij v_j)
      +(3c-1)mu |Dv|_B^(m-2)z^j v_j=0.                 (9)

This is the same geometric reduction as(4), now with no ratio weight. In isothermal coordinates it is(5) with R^(-tau) replaced by1. Thus w0=mu lambda^(-m) is smooth positive, d is smooth, and the divided drift grad log w0+d is smooth. The weak formulation follows either by testing div V=0 in flow coordinates or directly from(8); no omitted interior boundary is present. The C1 flat v is an admissible weak Wloc^(1,m) solution of the exact planar theorem. Unique continuation yields Dv=0 near zero, and(8) yields V=0 on a smaller flowbox. This proves the stronger statement in Section1.

## 9. Functional ratios need no bound and either scalar sign is allowed

Return to(1), but let S have either fixed strict sign off Gamma and vanish on Gamma. Set H=|S|. Suppose V is flat at x0. Assume R=E/H>0 off Gamma and that locally there R is a positive continuous function F(phi) of a potential satisfying V=H^eta grad phi. Different patches may use different choices of the additive constant in phi; this is a local functional-dependence assumption. No upper or lower bound for R and no extension of phi at Gamma is imposed.

On each such patch,

    alpha=E^(-eta)V.dx=R^(-eta)dphi=d(T(phi)),
    T'(s)=F(s)^(-eta).

A positive continuous F has a C1 primitive on every compact subinterval of its domain. This proves local distributional closedness off Gamma, even if F is not differentiable. Moreover alpha is smooth there because E>0 and V is smooth. It is the same globally defined one-form on every overlapping patch.

Its size tends to zero to every order toward Gamma, independently of R. To see the needed uniformity along a compact orbit segment, use homogeneity of V and the uniformly bounded derivative of the smooth flowbox map. A transverse circle of radius epsilon has period bounded by C epsilon sup|alpha|, which tends to zero. Closedness off Gamma makes this period constant, so it vanishes. Equivalently, distributional integration by parts on the flowbox with a tube of radius epsilon removed has boundary error bounded by C epsilon sup|alpha| on compact test support. This tends to zero. Hence alpha is closed on the full flowbox. Sections7-8 apply and exclude a nontrivial flat germ.

In the smooth positive-ratio setting, the local condition may instead be stated as grad R cross V=0. Indeed the normal form gives

    curl(E^(-eta)V)=-eta E^(-eta)(grad log R cross V).

This criterion also needs no ratio bounds. It is an extra alignment assumption, not a consequence asserted for a general tail. The transformation's flatness is controlled by |V|^(1-2eta); it does not require that the original u extend or that F have a positive limit at the puncture.

## 10. Verdict and limits

CO57(a)-(d) are confirmed with the precise local hypotheses above and the actual Guo-Kar citation. The all-c continuation uses eta<1/2 and ellipticity constant2c. The functional-dependence case has the stronger proof in Sections7-9. Every positive constant ratio is included, even inside 1<=R<=b and for either strict scalar sign.

The new normalized-form criterion can also be used when S changes sign or has extra zeros, but only if its distributional closedness is separately established. The functional-ratio deduction in Section9 retains the isolated scalar-zero orbit and positivity of R off it. General measurable bounded ratios, uncontrolled zero sets and nonzero-k branches are not excluded. No universal bound on constants in omega is claimed. The unrestricted common-flat problem and the campaign conjecture remain open.

All six source sections and all ten independent proof sections were read. There was no numerical computation or formal build. The source is the configured model coordinator's hand comparison with an the external referee (a second model) answer; the requested nested model consultation did not run. The configured model is recorded, while provider runtime remains unattested. The new Sections7-9 are submitted for continued comparison through the existing agents.
