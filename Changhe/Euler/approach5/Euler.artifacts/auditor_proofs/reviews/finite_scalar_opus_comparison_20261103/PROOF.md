# The configured coordinator comparison for finite scalar order

## 1. Exact setting and provenance

Use the smooth local tail system of A1288-A1291: 2/5<c<1/2, arbitrary finite omega, X=(cI-omega J)x, a=1-2c, b=2(1-c), q=b/a>2, eta=1/q, div V=0, W=curl V, k=X.V, S=P2-|V|²/2, twisted velocity and scalar homogeneity, -Delta P2=tr((DV)²), W.grad S=0 and grad k cross grad S=0 on {W!=0}. Let x0!=0 be an infinitely flat V zero, with S(x0)=0 and a finite first nonzero Taylor order l. For a contradiction at the end, x0 belongs to supp W.

The complete four-section coordinator note in the team records was read and archived. Its author agent is configured for the primary model; provider runtime is not independently attested. The nested the external referee (a second model) answers are not counted as model reviews. The coordinator explicitly rederives the statements by hand. This proof checks that rederivation, including its shorter support-component argument. No new model client or agent is used.

## 2. Strict superharmonicity on the finite scalar sectors

The pressure identity gives Delta S=-tr((DV)²)-|DV|²-V.Delta V, which is infinitely flat at x0. Homogeneity shows that the first scalar jet S_l is constant in the X0 direction. Its Laplacian vanishes, so in an orthonormal transverse coordinate z it is Re(Cz^l), C!=0. On a transverse disk, |S|<=C1 r^l and |grad S|>=C2 r^(l-1), uniformly including points close to the nodal arcs. The full gradient is used. For every N, |Delta S|<=C_N r^N.

Consequently

    S Delta S-(1-eta)|grad S|²<0

on every sufficiently small punctured sign sector. Under exp(tA), both terms scale by exp(-2(b+c)t), so the inequality persists on a common short flowbox. For f=|S|^eta it gives Delta f<0 wherever S!=0. This is exactly the numerator argument of A1288; no division by a lower bound for |S| near its nodal sheets is used.

## 3. A shorter proof that k is harmonic on the whole flowbox

Put K=supp W relative to the flowbox. K is the closure of the open set {W!=0}, hence K=closure(int K). On a connected scalar sector C let h=k/f. The rank identity and homogeneity give grad h=0 on {W!=0}, so all positive derivatives of h vanish on K intersect C by continuity. Outside K, W=0 on a neighborhood and grad k=-aV, hence Delta k=0.

At y in boundary K intersect C, continuity from the complement gives Delta k(y)=0. The positive derivatives of h vanish there, so

    0=Delta k(y)=h(y)Delta f(y).

Strict negativity of Delta f gives h(y)=0. Now consider a connected component O of C intersect int K. It is open because an open subset of Euclidean space is locally connected. If O is a proper subset of connected C, it has a relative boundary point inside C. Such a point cannot belong to int K: a small connected ball in int K would connect it to O and put it inside O. Thus it belongs to boundary K, where h=0. Since h is constant on O, h=0 on O.

If O=C, use an interior radial direction toward the sector vertex: f is bounded below by a positive multiple of r^(eta l), while k is infinitely flat. The constant h is again zero. Thus k=0 on int K off the nodal set, then on all of int K and K by continuity. The nodal set has no interior near this finite harmonic jet. Delta k is zero on int K and outside K, a dense open set; by continuity it is zero on the entire flowbox.

Harmonic analyticity and infinite flatness of k make k=0 on a smaller full neighborhood of x0. This argument does not require support of W at x0 or a separate assumption about accumulation of irrotational sets. It supplies the requested focused comparison of A1289 and a shorter route to its conclusion.

## 4. The finite-order continuation step

With k=0, the exact equations give X cross W=aV and grad S cross V=qSW. Therefore curl(V/|S|^eta)=0 on each sign sector. The full transverse reduction of A1260-A1263, independently compared in A1274, gives a scalar equation

    div(|h|^eta A grad u)+|h|^eta b.grad u=0,

with smooth positive principal matrix, bounded drift, a finite harmonic leading term for h, and zero Dirichlet trace on both nodal sides. The drift frequency estimate in A1290 gives V=0 on a full neighborhood after the finite-sector assembly. Equivalently, apply LIT220 once Section3 has supplied an open k-zero neighborhood. Support of W then gives a contradiction. A1288-A1292 are confirmed, including the disappearance of the former finite-S/irrotational-patch alternative.

## 5. The optional regular-nodal propagation argument

The coordinator also checks a second route when an open irrotational patch is present. On k=0, W=0 implies V=0. Away from the nodal sheets the scalar elliptic equation has smooth positive coefficients, so a zero open set propagates within each connected sector. At a regular nodal sheet bordering a zero sector, all derivatives of V vanish on the sheet. Since eta in (0,1), dividing by |S|^eta and extending by zero yields a smooth curl-free vector field. A local potential has a constant value on the sheet and can be normalized to be flat there.

In Euclidean Fermi coordinates (y,s) to the sheet, S=s sigma with sigma smooth and nonzero. The potential equation is

    div(|s|^eta M grad u)=0,

where M=|sigma|^eta sqrt(det g)g^(-1) is smooth, positive and block diagonal between s and y. At the base point, orthonormal coordinates and division by one positive scalar make M(0)=I. Let rho=|(y,s)|, mu=Mx.x/rho² and Z=Mx/mu. The block structure gives Z_s/s=M_ss/mu=1+O(rho), and for the sphere-tangential correction tau=Mnu-mu nu, tau_s/s=(M_ss-mu)/rho=O(1). These are the potentially singular weight derivatives.

For H=integral_sphere |s|^eta mu u², D=integral_ball |s|^eta grad u.Mgrad u and E=integral_sphere |s|^eta(Mgrad u.nu)²/mu, the height and Rellich identities in three dimensions are

    H'=(2+eta)H/rho+2D+O(H),
    D'=(1+eta)D/rho+2E+O(D).

One may first integrate off |s|<=epsilon. All cut fluxes tend to zero, since the field and its derivatives are smooth and the factor epsilon^eta tends to zero. Cauchy-Schwarz gives D²<=HE. Hence N=rho D/H satisfies N'>=-CN. A positive H therefore has a polynomial lower bound, contradicting flatness. If H=0, the weighted energy identity directly gives u=0. This proves continuation across the regular sheet. Cyclic adjacency of the finitely many sectors propagates zero around the vertex.

This optional route is valid at its stated extra-patch scope. It is not required for A1291. Normalizing M(0) and retaining the block property make explicit two choices needed in the abbreviated coordinator calculation.

## 6. Both-flat pressure information and component constants

For the common-flat case, the exact tensor T=V tensor V+P2 I satisfies partial_i partial_j T_ij=0. Integration over a ball centered at x0 gives

    integral_ball (|V|²+3P2)=r integral_sphere(P2+(V.nu)²).

If integral_sphere P2>=delta integral_sphere |V|² at every small radius for one fixed delta>0, let F(r) be the volume integral of the left-hand integrand. The radial identity gives F>=0, and common flatness makes F infinitely flat. Also

    F'=integral_sphere(|V|²+3P2)
       <=(3+1/delta) integral_sphere P2
       <=(3+1/delta)F/r.

Thus r^(-3-1/delta)F is nonnegative and nonincreasing from zero, forcing V=0. This verifies the spherical-mean form in the coordinator note and keeps the direction of the differential inequality explicit.

At a supported common-flat point, take delta=1/4. Open low-pressure sets {P2<|V|²/4}, equivalently {S<-|V|²/4}, accumulate. Either open irrotational sets among them accumulate, or open k-zero sets among them accumulate, or there are x_j approaching x0 with W(x_j),k(x_j) nonzero and

    S(x_j)=D_j |k(x_j)|^q,
    -D_j>|V(x_j)|^(2-q)/(4 sup|X|^q).

To justify the alternative, if the first two types do not accumulate, shrink to a neighborhood avoiding both open interiors. The nonzero-W and nonzero-k sets are then dense open, so their intersection meets each nonempty open low-pressure set. Since V is flat, -D_j |x_j-x0|^m tends to infinity for every fixed m. No bound on these component constants follows from smoothness alone.

Conversely, if the components with S=D|k|^q are dense and have one common lower bound D>=-D*, then S>=-D* sup|X|^q |V|^q>=-|V|²/4 near the flat point. The pressure identity gives a contradiction. This conditional result keeps both density and the uniform bound explicit.

## 7. Verdict and scope

The focused configured-model comparison agrees with A1288-A1292. Its support-component argument is a verified simplification, and its optional regular-nodal propagation argument is valid with the explicit normalization above. The both-flat calculations reproduce A1200-A1201 and A1088; they do not supply the missing lower bound on component constants or exclude open k-zero regions. The common-flat problem remains open. No numerical or formal verification is claimed.
