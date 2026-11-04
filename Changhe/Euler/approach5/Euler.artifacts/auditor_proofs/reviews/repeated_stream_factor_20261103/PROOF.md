# Repeated stream factors and the smooth finite-order conditional theorem

Status: independent audit of LIT212, CO51 and CO52, with their combined consequence. The isolated-leading condition can be removed from the smooth finite-order theorem. No smoothness or finite order is inferred for a general actual C^(1,alpha) tail.

## 1. Exact local hypotheses

Fix 2/5<c<1/2 and arbitrary finite omega. Set Jx=(-x2,x1,0), A=cI-omega J, X=Ax, a=1-2c, b=2(1-c), q=b/a>6. On a neighborhood of x0!=0 let V and Pi be smooth, W=curl V, k=X.V, S=Pi-|V|^2/2, and suppose

    div V=0, -Delta Pi=tr((DV)^2),
    DV X=-[(1-c)I+omega J]V,
    grad k=X cross W-aV,
    X.grad S=-bS, W.grad S=0.                  (1.1)

Assume V(x0)=DV(x0)=S(x0)=0, V has a finite first nonzero Taylor term V_m, m>=2, and every derivative of k vanishes at x0. The new conclusion is that the leading stream polynomial has no repeated real linear factor, so V_m is nonzero on every nonzero vector perpendicular to X0=X(x0). Its transverse projected-vorticity index is at most zero. Only q>2 is needed for this local proof when the other identities hold.

These local premises do not require support of W, a global profile, or a full k-zero neighborhood. The global consequence below adds the exact actual-profile hypotheses.

## 2. The polynomial equations under flat k

Let ell=|X0| and use positively oriented coordinates (t,s,z3) with e3=X0/ell. The lowest homogeneity term gives partial_3 V_m=0. The degree m term of k gives e3.V_m=0. Divergence therefore supplies a nonzero homogeneous planar polynomial psi of degree N=m+1 such that

    V_m=(-psi_s,psi_t,0), W_(m-1)=(Delta psi)e3.

The exact vector decomposition is

    W=(X.W)X/|X|^2-[a(X cross V)+X cross grad k]/|X|^2.

Take its scalar product with grad S and use both scalar transports:

    -a(X cross V).grad S
       =b(X.W)S+(X cross grad k).grad S.       (2.1)

The last term is flat, since grad k is flat and all factors are smooth. Let H_l be the first nonzero S term, if there is one with l<=2m. The scalar homogeneity gives partial_3 H_l=0. Degree m+l-1 in (2.1) yields

    grad psi.grad H_l=qH_l Delta psi.          (2.2)

For l<2m the pressure equation gives Delta H_l=0. If all lower terms vanish, the degree2m polynomial H, possibly zero, obeys (2.2) and

    Delta H=2det D^2psi-Delta(|grad psi|^2/2).  (2.3)

These are finite polynomial consequences, so using them does not identify a flat smooth function with its zero Taylor series on a neighborhood.

## 3. Scalar multiplicity on a repeated real line

Suppose psi has a repeated real line factor. Rotate the plane so that its exact multiplicity is j>=2 along t=0:

    psi=t^j Q(t,s), Q(0,1)!=0.

For any nonzero homogeneous polynomial H of positive degree satisfying (2.2), write H=t^d R(t,s), with d>=0 and R(0,1)!=0. Near (0,1),

    psi_t=j t^(j-1)Q(0,s)+O(t^j),
    Delta psi=j(j-1)t^(j-2)Q(0,s)+O(t^(j-1)).

If d=0, the left side of (2.2) has no t^(j-2) coefficient, while its right side has a nonzero one. This is impossible. If d>=1, tangential derivatives of psi keep their t^j factor, so the coefficient of t^(j+d-2) gives

    j d Q(0,1)R(0,1)=qj(j-1)Q(0,1)R(0,1),
    d=q(j-1)>2(j-1)>=2.                      (3.1)

Thus d is an integer strictly larger than2. If q(j-1) is nonintegral, no such nonzero polynomial H exists.

A nonzero planar homogeneous harmonic polynomial of positive degree has only simple real line factors: its angular part is A cos(l theta)+B sin(l theta), and all its angular zeros are simple. A first S term of degree l<2m would therefore have multiplicity0 or1 along the line, contradicting (3.1). All S terms below2m vanish. Equation(2.3) now applies to H=H_2m, including the initially possible zero polynomial.

## 4. Pressure forces an incompatible multiplicity

Along t=0,

    |grad psi|^2=j^2 t^(2j-2)Q(0,s)^2+O(t^(2j-1)).

Twice differentiating the explicit polynomial expansion gives the exact leading normal term

    Delta(|grad psi|^2/2)
       =j^2(j-1)(2j-3)Q(0,1)^2 t^(2j-4)
                                           +O(t^(2j-3)).

The tangential second derivative cannot lower the t order. Also psi_tt,psi_ss,psi_ts have normal orders at least j-2,j,j-1, respectively. Thus det D^2psi has order at least2j-2 and does not affect the displayed term. The right side of (2.3) has exact order2j-4, with nonzero negative coefficient

    -j^2(j-1)(2j-3)Q(0,1)^2.                  (4.1)

This proves H!=0. By (3.1), its multiplicity is d=q(j-1)>2. Its Laplacian has exact normal order d-2, with coefficient d(d-1)R(0,1)!=0; again the tangential derivative has higher order. Equation(2.3) forces d-2=2j-4, or d=2(j-1). Together with (3.1), this forces q=2, a contradiction. This proves the repeated-line exclusion. The proof covers j=2, where (4.1) is a nonzero constant, and j=N, where Q is constant.

## 5. Leading isolation and index

If grad psi vanishes at a nonzero point, Euler's identity N psi=t psi_t+s psi_s makes psi vanish there too. Rotate that point to (0,1). The dehomogenized polynomial psi(t,1) then has both value and first derivative zero at0, so t^2 divides it. Homogeneity transfers this to a repeated linear factor of psi. Section4 excludes it. Thus grad psi is nonzero on the unit circle, and compactness gives |V_m(y)|>=d0|y|^m, d0>0. The smooth Taylor remainder makes the full V nonzero on a small punctured transverse disk.

For completeness, the nonpositive-index input can be checked at the same polynomial level. Write psi=r^N g(theta). The gradient is e^(i theta)(Ng+i g'); all g zeros are simple. If there are2j0 of them, index(grad psi)=1-j0: the factor Ng+i g' crosses the positive imaginary ray downward at the j0 zeros with g'>0, giving winding -j0. With no zeros it stays in a half-plane and the index is1.

Positive index therefore requires g to have one strict sign. Change sign to g>0 and choose a minimum, where g'=0,g''>=0. For a scalar term r^l h, equation(2.2) is

    g'h'=[q(N^2g+g'')-Nl g]h=:D_l h.

For l<=2N-2 and i=0,1,2,

    D_l-i g''=N(qN-l)g+(q-i)g''>0.

A first lower harmonic scalar term must have h=0 at this angle; differentiating once forces h'=0, impossible for a nonzero harmonic angular polynomial. Thus all lower terms vanish. At l=2m, the equation and its first two derivatives force h=h'=h''=0. But

    Delta H=-(psi_tt-psi_ss)^2-4psi_ts^2
                                 -grad psi.grad Delta psi,
    grad psi.grad Delta psi=N(N-2)g(N^2g+g'')>0

there, so Delta H<0 whereas l^2h+h''=0. This contradiction proves index<=0 for q>2.

The transverse projection F=W-[(W.e3)/(X.e3)]X has first nonzero term (a/ell)grad psi: project X cross W=aV+grad k, whose last term is flat. Consequently F has the same index. This verifies the leading field and does not assume the unprojected W begins at order m rather than m-1.

## 6. Actual finite-order supported zeros automatically satisfy isolation

Now suppose V,Pi are actual tails in the HF/natural class specified in Section7. At a supported flat zero with S=0, smooth V makes Pi smooth locally by Poisson. If V has finite first order m>=2, A1139-A1140 prove that k is flat: the leading Delta S has negative circular mean, so S has a nonzero term l<=2m; every derivative of the smooth rank defect k grad S-qS grad k vanishes at the supported point; a first k term of degree s>=m would imply (l-qs)H_l K_s=0, impossible for q>2. This argument does not need isolated leading directions.

Sections2-5 now supply those directions automatically. A1142 then gives a full k-zero neighborhood and puts the sphere point in the interior of E0. Thus every smooth finite-order T0 point lies in the interior of E0, with isolated full angular velocity zero and nonpositive index when k is zero near it. The earlier explicit isolated-leading hypothesis has been removed.

Independently, at a smooth boundary point of E0 the scalar k is flat by continuity of each derivative from Z. A1053 gives V=DV=S=0 there. Finite V order would invoke Sections2-5 and make its angular zero isolated, contradicting the selector theorem A1133. Both proofs give the same boundary exclusion.

## 7. Global conditional theorem and the exact remaining obstruction

Fix 2/5<c<1/2 and arbitrary finite omega, and suppose U in C^2(R^3;R^3), P in C^1(R^3) solve

    div U=0, (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1),
    p=(1-c)/c, C finite.

Let V,P2 be their actual tails. Assume that at every point of

    T0={V=DV=S=P2=0 on S^2} intersect supp(curl V),

V is smooth on a neighborhood and has a finite first nonzero Taylor term. No isolated-leading hypothesis is imposed. Then U=0.

Indeed Section6 supplies the isolated-leading premise at every T0 point, so the already confirmed all-branch theorem A1144 applies. To spell out its branch logic: every T0 point is interior to E0; boundary E0 is contained in T0, so E0 has no boundary. If E0 is empty, a nonzero U would still supply a T0 point by A1057, a contradiction. If E0=S^2, continuity gives k=0 globally, and the finite isolated-leading index count A1119 contradicts total index2. This is a complete conditional proof.

If the actual tail is smooth at every T0 point and U!=0, at least one such point must be flat to infinite order. Under the global nodal condition N, E0 is empty, so every T0 point at which V is smooth must be of infinite order. At a boundary point of E0, smooth V must also have infinite order. These statements do not force E0=S^2 for an arbitrary nonzero smooth tail: an infinite-order point can remain in the empty or intermediate branch.

In particular a smooth original profile with all-order natural derivative estimates |D^j U(y)|<=C_j(1+|y|)^(-p-j) has smooth tails by A1145. If its T0 zeros all have finite order, it is zero. The all-order bounds do not themselves supply finite order. Bare decay, helicity removal and the natural derivative premise remain outside this theorem.

There is also a real-analytic-tail corollary. If V is real analytic near every T0 point, each such zero has finite order: an infinite-order analytic zero would make V vanish on a neighborhood, hence W vanish there, contrary to support. Thus the theorem gives U=0 without a separate finite-order premise. This concerns analyticity of the actual tail, not analyticity of the original profile through Xi.

One sufficient original condition is the explicit factorial natural estimate: U is smooth and, for all integers j>=0,

    |D^j U(y)|<=C_* L^j j! (1+|y|)^(-p-j), C_*,L>0.

The rescaling argument A1145 transfers |D^j V(x)|<=C_* L^j j! |x|^(-p-j). On a ball with |x|>=r=|x0|/2, the Taylor remainder along a displacement h is bounded by C_* r^(-p)(L|h|/r)^(j+1). It tends to zero for |h|<r/L, after also restricting to the ball. Therefore V is real analytic locally on D. In particular an infinite-order zero would give V=0 on a full ball. With the same exact HF profile hypotheses and campaign parameters, these factorial natural estimates imply U=0. No analyticity of Xi is required. A mere assertion that original U is analytic, without the uniform derivative estimates or another justified tail-analyticity argument, does not supply this corollary.

## 8. Full source and focused model comparison

All seven LIT212 sections were read and independently checked in Sections2-5. The full coordinator CO51 note was read: its rescaling derivative bound, compactness, transverse Taylor argument, compact discrete T0 and its older three-branch assembly agree with A1134/A1138/A1144/A1145. The full five-section CO52 note was also read: it explicitly checks the negative mean identity, smooth defect, support rather than density, the Rolle cylinder and the local-to-global transfer, and independently makes the S!=0 extension. These agree with A1139-A1143.

This is a received focused comparison from the coordinator configured with the primary model, with runtime still unattested. Its nested completed proof was the external referee (a second model) and its model credential attempt failed; that failure is not counted as a review. The configured coordinator's actual written hand-check is counted. The present repeated-factor and weakened finite-order global combination still need that same focused follow-up. No new model client or agent is requested.

CO52's final sentence says everything remaining with smooth tails is in the globally k-zero branch. That is stronger than its proof: the arguments put finite isolated-leading points inside E0, but do not eliminate empty or intermediate branches whose required T0 points fail the extra hypothesis. Section7 gives the corrected scope. This is a wording inference correction, not a counterexample to CO52's local theorem.

No symbolic computation or formal build is needed for these polynomial identities; the coefficients and normal orders are derived explicitly. All constants may depend on finite omega. The main unrestricted Euler conjecture remains open.
