# Mixed type near a nonflat W2 direction and its Lipschitz exclusion

Independent audit of Theory Agent B B63-B64. Status: CONFIRMED A2035-A2038 at the stated hypotheses; remaining extensions OPEN A2039. This proof separates the local conditional statements from their application to an actual profile. Source coverage and hashes are in the team records.

## 1. Exact local setting and inherited jets

Fix 2/5<c<1/2 and any finite real omega. Put Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, b=2-2c and q=b/a>6. Let V,P2 be C^2 on an open neighborhood of w!=0. Set W=curl V, k=X.V and S=P2-|V|^2/2. Assume the local tail identities

    div V=0, DV X=-LV, V.W=0,
    -Delta P2=tr((DV)^2), X.grad S=-bS, W.grad S=0,
    grad k cross grad S=0 on VV={W!=0}.

Then X.grad k=-ak, grad k=-aV+X cross W and

    Delta k=-2omega W3-X.curl W,
    Delta S=-tr((DV)^2)-|DV|_F^2+V.curl W.                 (1)

For the strict-rate nonflat configuration assume w lies in the closure of VV and the following point data hold:

    V(w)=W(w)=DW(w)=0, k(w)=S(w)=grad k(w)=grad S(w)=0,
    M=DV(w) is symmetric and trace-free, M X(w)=0, M!=0,
    D=D^2k(w)=-aM.

Let E=X(w)^perp. Its saddle eigenvalues are sigma,-sigma, where sigma>0. The previously confirmed contact argument A1732 supplies a unit null direction e in E, a perpendicular unit f in E, and

    Me=sigma' f, Mf=sigma' e, sigma'=sigma or -sigma,
    H=D^2S(w)=-4sigma^2 f tensor f,                       (2)

with every transverse limiting direction of VV at w contained in the line Re. In particular, writing h=se+uf and r=|h| on the transverse section w+E, one has u=o(r) along VV. These are stated premises for the new local argument, not consequences of arbitrary C^2 tail fields. The complete prior proof of the contact argument has been reread.

The map (t,h) to exp(tA)(w+h) gives a smooth local flow chart since X(w) is transverse to E. Homogeneity transports zero sets and all signs used below. For bounded t it multiplies the relevant scalar quantities by strictly positive factors. Thus estimates on the section extend to a sufficiently small flow box. All asymptotic formulas below use r on that section.

## 2. Vortical points cannot have k=0

Taylor expansion gives, uniformly as r tends to zero,

    V(w+h)=Mh+o(r), grad k(w+h)=Dh+o(r),
    |V|^2=sigma^2 r^2(1+o(1)),
    |grad k|^2=a^2 sigma^2 r^2(1+o(1)).                  (3)

Thus grad k is nonzero away from the orbit through w in a small flow box. Equation (1) and continuity give Delta S<0 there, since Delta S(w)=-4sigma^2. Also Delta k(w)=tr D=0.

Contracting the rank identity with X gives bS grad k=ak grad S on VV. On each connected component C of VV intersect {k!=0} this integrates to

    S=D_C |k|^q                                            (4)

with one finite constant D_C. The integration follows by differentiating S|k|^(-q), which has zero gradient; it does not assert a common constant across components.

Suppose x in VV has k(x)=0. It is off the orbit, because W vanishes on that orbit. Since grad k(x)!=0 and VV is open, choose a coordinate product neighborhood contained in VV with first coordinate k. Each of its two sides is connected and belongs to a single component of {k!=0} intersect VV. Formula (4) holds with one fixed finite constant on each side. Since q>2, its Hessian tends to zero as k tends to zero. Continuity of D^2S gives D^2S(x)=0, contradicting Delta S(x)<0. Therefore every sufficiently near vortical point has k!=0. No uniform bound on the component constants is used in this argument.

## 3. Uniform defect coefficient and negative pressure scalar

At any such point set alpha=qD_C|k|^(q-2). Twice differentiating (4) gives

    S=alpha k^2/q, grad S=alpha k grad k,
    D^2S=alpha[(q-1)grad k tensor grad k+k D^2k].          (5)

Taking the trace and using (3), k=O(r^2), Delta k=o(1) and (q-1)a=1, one obtains

    (q-1)|grad k|^2+k Delta k
          =a sigma^2 r^2(1+o(1))>0,
    alpha=Delta S/[(q-1)|grad k|^2+k Delta k]
          =-4/(a r^2)(1+o(1)).                           (6)

Every error estimate is uniform on the section; division by k was not used in the estimate of the denominator. Thus alpha<0, D_C<0 and S<0 at every sufficiently near vortical point.

By (2) and the limiting-direction condition,

    k(w+h)=-a sigma' su+o(r^2)=o(r^2)                    (7)

uniformly along VV on the section. Uniformity follows by contradiction and compactness of unit directions: a sequence violating u=o(r) would have a limiting direction outside Re. Finally

    D_C=alpha |k|^(2-q)/q tends to -infinity             (8)

along every vortical sequence approaching w, even when its components vary. A fixed component has one finite constant, so it cannot have w in its closure.

## 4. The reduced symbol is indefinite on the whole approach

On a sufficiently small simply connected piece of a component in VV, k!=0 and V.W=0 imply

    curl(V/k)=0, V=k grad phi, X.grad phi=1.

Indeed grad k cross V=(X cross W) cross V=kW. With (4), the remaining divergence and pressure equations are

    div(k grad phi)=0,
    Delta(D_C|k|^q+k^2|grad phi|^2/2)+tr((DV)^2)=0.        (9)

The CO61 calculation was reread and its determinant recomputed: with column weights two for phi and one for k, the principal determinant is |xi|^2 Q(xi), where

    Q(xi)=(qS+|V|^2)|xi|^2-(V.xi)^2.

This is an algebraic coefficient identity at C^2 regularity; no smoothness bootstrap is presupposed. Covectors on the local orbit space annihilate X. On X^perp the eigenvalues are

    lambda1=qS+k^2/|X|^2,
    lambda2=qS+|V|^2.                                    (10)

The projection V_T=V-kX/|X|^2 is nonzero near the approach by (3) and (7). It gives the lambda1 eigendirection; its perpendicular gives lambda2. Substitution of (6)-(7) into (10) yields

    lambda1=-(4k^2/(a r^2))(1+o(1))<0,
    lambda2=sigma^2 r^2(1+o(1))>0,
    |lambda1|/lambda2 tends to zero.                     (11)

Thus Q has exactly two distinct real null lines at every sufficiently near vortical point. The complete determinant retains the positive |xi|^2 factor; it is the Q factor that is hyperbolic. This rules out applying an elliptic regularity theorem to the displayed reduced system on that approach. It does not rule out a different regularity argument using other identities or global information, and it constructs no such configuration.

## 5. A difference-quotient lemma at Lipschitz second derivatives

Let k,S be C^2 near a point w, with locally Lipschitz Hessians K=D^2k and Hx=D^2S. Suppose F=grad k cross grad S vanishes on an open set O accumulating at w. Assume grad k(w)=grad S(w)=0. For a fixed unit vector v, differentiation on O gives

    K_x v cross grad S(x)+grad k(x) cross Hx v=0.

Let Lk,LS be Lipschitz constants on a fixed neighborhood of w. At x in O choose t sufficiently small that x+tv remains in O. Subtract the identities at x+tv and x and divide by t. The terms involving differences of the two gradients converge to

    2K_x v cross Hx v.

The other two terms have norms bounded in the limit by Lk|grad S(x)| and LS|grad k(x)|, respectively. The radius of the admissible segment can depend on x; the resulting bound cannot. Therefore

    2|K_x v cross Hx v|
          <=Lk|grad S(x)|+LS|grad k(x)|.                 (12)

No third derivative is asserted at x or w. Sending x to w through O and using continuity proves

    D^2k(w)v cross D^2S(w)v=0                            (13)

for every v. In particular the argument applies even if O consists of successively thinner components.

In the configuration (2), take v=f. Then Df=-a sigma' e and Hf=-4sigma^2 f, so the left side of (12) tends to 8a sigma^3>0 while its right side tends to zero. This is a contradiction. Thus that configuration cannot have both Hessians locally Lipschitz.

## 6. Tail regularity and exact profile consequence

It suffices that V be C^(2,1) near w. Then k=X.V has locally Lipschitz second derivatives. Also tr((DV)^2) is C^(1,1), hence C^(1,beta) for every 0<beta<1 on compact subsets. Interior Poisson regularity applied to the already normalized P2 gives P2 in C^(3,beta) locally. Its second derivatives are therefore locally Lipschitz. The same is true of D^2(|V|^2/2), so S has locally Lipschitz second derivatives. No endpoint C^(3,1) Schauder assertion is used.

For the actual-profile application retain all earlier W2 assumptions: a full C^2 velocity and C^1 pressure on R^3 satisfying the Euler profile equation, zero helicity, the natural U and DU bounds, an escaping lower-window W2 trace, and its established C^1 scattering convergence. The natural bounds are

    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1),
    p=(1-c)/c.

They give the required tail identities and the scattering identity W(Xi y)=DXi(y)curl U(y), det DXi=1, so the scattering direction is supported. Add V in C^(2,1) on a neighborhood of that direction. A1731 already excludes nonflatness at the equality rate rho=-b under C^2 regularity. At the strict rate rho<-b, A1732 gives (2) and the difference-quotient contradiction applies. At every rate the direction therefore has

    V=DV=W=0, S=P2=0.

This is precisely a finite-jet T0 point. It need not be a point where V or S vanishes to infinite order. No C^(2,1) regularity of the tail is inferred merely from C^2 or C^3 regularity of the original profile.

## 7. Verification and scope

The complete submitted Remarks (lv)-(lvii), Theorem FP item (14), the source setting, and the relevant B59-B61 statements and proofs were read. Both complete prior independent proofs, including all eleven contact sections and all seven CO61 sections, were reread. Every estimate above was checked by hand. No numerical computation or formal build was needed.

The C^2 and C^(2,beta), beta<1, strict-rate configurations remain unexcluded and unconstructed. The difference quotient in (12) requires a bounded quotient of Hessian increments; a merely Holder estimate supplies t^(beta-1), which does not suffice for this proof. No claim is made about the consultation's unclaimed cubic compatibility or scalar sliver model. Global matching, elimination of T0 and the arbitrary-helicity bare-decay theorem remain open. All finite omega are allowed; constants are permitted to depend on omega.

The source agent is configured model and cites an existing the external referee (a second model) consultation. The existing configured model coordinator's CO61 proof has been compared in full, and this endpoint refinement is supplied through the agent notes for follow-up. Provider runtime remains independently unattested. No new model client or agent has been started.
