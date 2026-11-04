# Annular divergence at a flat zero and the weak-L2 carrier obstruction

Status: CONFIRMED at the exact planar and conditional carrier scopes, A2831-A2833. The unqualified class-containment sentence is REFUTED A2834; the intended common-class statement is confirmed. General scalar weak-L2 and Euler application remain OPEN A2835.

## 1. Exact planar statement

Let R>0 and D_R={z in C:|z|<R}. Write partial_bar=(partial_x+i partial_y)/2 and let dA be planar Lebesgue area. Suppose f:D_R->C is smooth and flat at zero, meaning every derivative including order zero vanishes there. Let b:D_R->[0,infinity] be measurable, finite almost everywhere and locally essentially bounded on D_R minus {0}. Assume

    |partial_bar f|<=b|f| almost everywhere.

Then either f is identically zero, or for every 0<R0<R,

    I_b(r,R0)/log(R0/r) -> infinity as r decreases to zero,
    I_b(r,R0)=integral_(r<|z|<R0) b(z)/|z| dA.

In particular the first alternative holds if b is weak-L2, with convention

    M=sup_(t>0) t |{z:b(z)>t}|^(1/2)<infinity.

A bounded subsequence of the displayed normalized annular integrals already forces the first alternative. No smallness is assumed. The local boundedness on the punctured disc is an independent hypothesis, not a consequence of weak-L2 membership.

## 2. Local factorization and positive zero indices

Put q=(partial_bar f)/f where f!=0 and q=0 elsewhere. The differential inequality gives partial_bar f=qf and |q|<=b almost everywhere, including the almost-everywhere statement on the zero set. On every relatively compact smooth domain O in the punctured disc, q is essentially bounded. Extend its restriction to O by zero and define

    s(z)=(1/pi) integral_O q(w)/(z-w) dA(w).

The Cauchy fundamental solution and the Lp boundedness of its other derivative give s in W1p locally for every finite p>1 and partial_bar s=q on O. Its continuous representative follows, for example, by choosing p>2 and Sobolev embedding. These exact analytic inputs were already checked in A2467; the same bounded-data factorization is Lemma4.2 of Pan and Zhang, arXiv2608.22698v1, printed pages17-18. They are external analytic theorems, not formalized here.

The Sobolev chain and product rules, locally where s is bounded, give partial_bar(exp(-s)f)=0. Weyl's lemma makes h=exp(-s)f holomorphic, with equality of continuous representatives. Thus locally f=exp(s)h. If f vanishes on an open subset, local holomorphic uniqueness propagates this property through the connected punctured disc. Continuity then gives f=0 on D_R. Otherwise the zeros of f in the punctured disc are isolated, with local positive integer index equal to the order of the corresponding holomorphic zero. The exponential factor has a continuous logarithm and index zero. The order is independent of the local factorization: two such holomorphic factors differ by a nowhere-zero holomorphic function, since their logarithmic factors have the same partial_bar derivative.

There are finitely many zeros in any compact annulus. Indeed infinitely many would have an accumulation point there and force local holomorphic vanishing. Consequently only countably many radii meet a zero. For zero-free circles define k(r) as the winding number of theta->f(r exp(i theta)). A single-valued factorization on a slightly larger annulus and the holomorphic argument principle give

    k(r2)-k(r1)=sum_(r1<|z|<r2) ord_z(f)>=0.

A multiply connected annulus causes no problem: s is supplied by the integral on the whole annulus, so exp(s) has winding zero on both boundary circles. We do not assert a uniform bound on the number of zeros accumulating at zero.

## 3. Radial means and the inward inequality

Let m(r) be the normalized angular mean of log|f|. This is finite even when the circle passes through a zero. On a compact annulus a holomorphic factor has finitely many zeros, so it can be divided by their polynomial factors. Its remaining logarithmic modulus is smooth. Each removed factor contributes a multiple of log|z-z_j|, whose gradient is locally integrable. Together with Re(s), this shows log|f| is W11 locally on the annulus. Polar Fubini therefore supplies a locally absolutely continuous radial mean. It agrees with every circle mean: the normalized angular integral of each log|r exp(i theta)-z_j| is log max(r,|z_j|), and the continuous remaining terms have continuous means.

For almost every zero-free radius, divide the polar differential equation by f:

    (partial_r f)/f+(i/r)(partial_theta f)/f=2 exp(-i theta)q.

The angular mean of (partial_theta f)/f is i k(r). Taking real parts gives

    m'(r)-k(r)/r=mean_theta 2 Re(exp(-i theta)q).

Choose a zero-free R1<R0 and put K=k(R1). Monotonicity gives k(r)<=K inward. Integrating the last identity from r to R1 yields

    m(R1)-m(r)<=K log(R1/r)+I_b(r,R1)/pi.

The sign is essential. It is an upper bound for the inward winding numbers, which remains valid if they tend to minus infinity. The factor1/pi comes from twice the normalized angular mean and dA=r dr dtheta.

Flatness gives, for every integer N>=0, |f(z)|<=C_N |z|^N near zero with C_N>0. Hence

    I_b(r,R1)/pi >= (N-K)log(R1/r)
                    +m(R1)-log C_N-N log R1.

First take a lower limit after division by log(R1/r), with N fixed. Then let N increase. The lower limit is infinite, which is the full limit to positive infinity. Positivity and log(R1/r)/log(R0/r)->1 give the result for the original R0. This proof needs no unjustified differentiation through a zero and no passage across infinitely many zeros in a fixed compact annulus.

## 4. Weak-L2 gives only logarithmic annular cost

For any finite-area measurable E, layer cake and the weak distribution bound imply

    integral_E b <= integral_0^infinity min(|E|,M^2/t^2) dt
                 =2M |E|^(1/2).

The M=0 case is immediate. For M>0 the integral splits at t=M/sqrt(|E|). On a<|z|<2a, the bound 1/|z|<=1/a and the area3pi a^2 therefore give

    integral_(a<|z|<2a) b/|z| dA <=2sqrt(3pi)M.

Cover r<|z|<R0 by at most ceil(log_2(R0/r)) such annuli, starting at R0 and proceeding inward. The last may extend below r; this is permitted by positivity. The normalized cost is bounded, contradicting Section3 for a nonzero flat f. Uniformly bounded dyadic annular costs suffice without weak-L2. Conversely, nonzero flatness forces the average of the successive dyadic costs to diverge. It need not force every individual annular cost to diverge.

## 5. Precise carrier consequence

Fix0<c<1/2 and any real omega. Put Jx=e3 cross x, A=cI-omega J, L=(1-c)I+omega J, X(x)=Ax and a=1-2c. Let U be open in R3, avoiding zero, and V:U->R3 be smooth, with W=curl V and

    div V=0, X.V=0, (DV)X=-LV.

Let sigma:D_R->U be a smooth transverse section, so det(sigma_1,sigma_2,X(sigma))!=0. Suppose V is flat at sigma(0). If B>=0 is measurable, weak-L2 on D_R, locally essentially bounded away from zero, and

    |(W.X)(sigma(y))|<=B(y)|V(sigma(y))| almost everywhere,

then V=0 on a three-dimensional neighborhood of sigma(0).

Here is the exact dependency in the reduction. A2463 and the proof before the integrability step of A2464 give a smooth positive quotient metric g, a one-form theta pulled back from V.dx, and two equations: d(*_g theta) is a smooth linear function of V, while d theta is a smooth linear function of V plus a smooth multiple of (W.X)(sigma). Smooth orientation-preserving isothermal coordinates z=phi(y), phi(0)=0, write theta=alpha1 dz1+alpha2 dz2. For f=alpha1-i alpha2 the two equations imply

    |partial_bar f(z)|<=(C1+C2 B(phi^-1(z)))|f(z)|.

On a smaller compact coordinate neighborhood the constants are finite and nonnegative, f is flat, and f=0 exactly when V(sigma)=0. This is an algebraic and coordinate consequence of the two equations; the earlier Lp premise is not used to obtain it. A2467 supplies the smooth isothermal theorem at these hypotheses.

A bounded Jacobian for phi shows that composition with phi^-1 preserves weak-L2: the distribution function increases by at most that Jacobian bound. Addition of C1 on a bounded disc and multiplication by C2 preserve weak-L2, by splitting distribution levels at2C1. The coefficient remains locally bounded off zero. Sections1-4 make f zero on a coordinate disc. Finally,

    V(exp(tA)x)=exp(-tL)V(x)

along every finite orbit segment remaining in U. This follows by differentiating in t. The map (y,t)->exp(tA)sigma(y) has invertible differential at(0,0), so the zero section fills a neighborhood. Only local finite times are used. No completeness of the V-flow or global injectivity of sigma is assumed, and no omega-uniform coordinate constants are claimed.

## 6. Full conditional setting and local boundedness at off-orbit zeros

For the stronger necessary condition assume a smooth X-flowbox G=Phi(D times I), with D a disc, I an interval, Phi_t=X(Phi), center orbit Gamma=Phi({0} times I), and x0 in Gamma. Assume smooth V,S obey the carrier equations of Section5 and

    X.grad S=-b0 S, b0=2(1-c), X cross W=aV, W.grad S=0,
    P=S+|V|^2/2, -Delta P=tr((DV)^2),
    S=0 on Gamma, S<0 on G minus Gamma,

and V,S are flat at x0. This is the entire setting F, not a consequence asserted for every global profile. Let H=-S and eta=a/b0.

A2404-A2406, proved in the separate carrier-flat-set audit under precisely these hypotheses, give flatness of V on Gamma, no open zero subset of G, equality of the zero sets of V and W, and isolated off-Gamma zero orbit segments. Those statements use the scalar and Poisson equations. They cannot be imported for a bare carrier system.

Off Gamma, ell=grad log H is smooth with ell.X=-b0 and ell.W=0. Taking its cross product with aV=X cross W yields a ell cross V=b0 W, hence

    W=eta grad(log H) cross V.

This equality remains valid when V=0, without any division by V. For any section through x1 in Gamma put B=|W.X|/|V| where V!=0 and B=0 elsewhere. Then

    B<=eta |X||grad log H|

off Gamma, so B is locally bounded there even near off-orbit zeros. Shrink the section to meet Gamma only at its center. The coefficient B is then locally bounded on its punctured parameter disc, and the differential inequality used in Section5 holds also at zeros since W=0 there. The associated scalar f is flat but cannot vanish on any neighborhood, since transport would give an open zero subset of G.

## 7. Coordinate annuli and all three necessary divergences

Apply the scalar theorem to b(z)=C1+C2 B(phi^-1(z)) on an arbitrarily small coordinate disc. It has divergent normalized annular cost. Fix a smaller section radius R0 and choose R1 with the closed z-disc contained in phi(D_R0). On this neighborhood choose positive l,M,Jmax with

    l|y|<=|phi(y)|<=M|y|,  det Dphi<=Jmax.

The lower distance bound follows from a bounded derivative of the inverse after a sufficiently small disc restriction. Changing variables gives

    I_b(r,R1)<=2pi C1 R1
                +(C2 Jmax/l) integral_(r/M<|y|<R0) B(y)/|y| dA.

The inner cutoff follows from |phi(y)|<=M|y|; the reciprocal weight uses the other bound. If C2=0, the scalar theorem already contradicts nonzero flatness with a bounded coefficient. Otherwise put r=M rho and divide by log(R0/rho). Since log(R1/(M rho))/log(R0/rho)->1, the original section's normalized annular cost tends to infinity. Positivity extends the conclusion to any larger allowed section disc.

On a compact smaller section, B<=sup|X| |W|/|V| with zero assigned at common zeros. The same annular divergence follows for |W|/|V|. The triple product also gives

    B=eta |X||n.grad log H|,
    n=(V cross X)/(|V||X|),

off the zero set. The exceptional section points are countable: off-Gamma zero orbits are locally isolated by A2406 and transverse to the section, and Gamma contributes only the center after shrinking. Assigning zero on this set gives equality almost everywhere. Thus all three quantities have divergent normalized annular cost and fail to be weak-L2 in every neighborhood of the center. The constants can depend on the section, c and omega. The conclusion holds for every fixed real omega.

## 8. Strictness of the coefficient class, with its exact qualification

Within the common class of coefficients locally bounded off zero, weak-L2 is strictly broader than admitting an upper bound b<=B2+C0/|z| with B2>=0 in L2 and C0>=0. Inclusion follows from Chebyshev for B2, the distribution bound |{C0/|z|>t}|<=pi C0^2/t^2, and {B2+C0/|z|>t} contained in the union of the two level sets at t/2.

For strictness choose a smooth0<=psi<=1 supported in the unit disc and equal to1 on the half disc. For n>=3 set z_n=2^-n, A_n=2^(n^2), epsilon_n=1/A_n and

    b(z)=sum_(n>=3) A_n psi((z-z_n)/epsilon_n), b(0)=0.

The support discs are disjoint and accumulate only at zero, since epsilon_n<=2^(-n-3) and successive centers are2^(-n-1) apart. Thus b is smooth and locally bounded on the punctured disc. If A_(k-1)<t<=A_k, the level set is contained in the discs with n>=k, and

    t^2 |{b>t}|<=pi A_k^2 sum_(n>=k) A_n^-2<=4pi/3.

For t<=A3 use the sum starting at n=3. The last bound uses A_(n+1)/A_n>=2. Hence b is weak-L2. For each fixed C0, sufficiently large plateaus |z-z_n|<epsilon_n/2 satisfy |z|>=2^(-n-1) and C0/|z|<=A_n/2. On each plateau,

    integral (b-C0/|z|)_+^2 dA >=pi/16.

All sufficiently large plateaus lie in every neighborhood of zero, so their disjoint contributions prove (b-C0/|z|)_+ not in L2 there. Therefore no proposed upper bound by B2+C0/|z| exists.

The common local-boundedness qualification matters for a literal set inclusion: an arbitrary L2 function may be unbounded at a nonzero point. For example, a cutoff times |z-z_*|^-1/2 at z_*!=0 is L2 in two dimensions but not locally essentially bounded there. Thus weak-L2 plus punctured local boundedness does not contain the unrestricted upper-bound class. The source's first sentence in Section7 should state the common class explicitly. The example and every planar or carrier theorem above are unaffected. This is a coefficient example only, not a nonzero f, carrier field or Euler profile.

## 9. Source and audit boundaries

The actual primary manuscript Pan and Zhang, arXiv2608.22698v1, was inspected at its title, introductory scope, Lemma4.2 and the one-dimensional radial-mean proof of Theorem4.1 on printed pages17-18. The author names, date and27-page length agree with the retained primary PDF. This is selected-passage verification, not an independent full-paper audit. A web open attempt returned an internal retrieval error; the existing local primary copy supplied the inspected text. The paper studies continuation at infinity. The inward annular theorem and its carrier application above have been reconstructed separately, rather than attributed to a theorem not present in that paper. No novelty claim is made.

The entire eight-section LIT338 source was read. The exact A2404-A2408 and A2463-A2467 dependencies were checked, including the quotient reduction before its Lp step and the flowbox scope. No mathematical computation, new model client, subagent or formal verification was used. The complete existing Theory Agent C 03:12 comparison and03:13 qualifier were read and agree with Sections1-8. General scalar weak-L2 without punctured local boundedness, any Euler upper bound that contradicts the necessary divergence, exclusion of F, and the unrestricted decaying rotating Euler theorem remain open.

## 10. Existing model comparison and designated scope

The entire Theory Agent C 03:12 comparison, including Sections2-8, agrees with the independent argument above. Its explicit sign test f=(z-0.3)^2 exp(z zbar+zbar^2) has q=z+2zbar, m(r)=2log max(r,0.3)+r^2 and k=0 or2 according as r<0.3 or r>0.3. Thus m'-k/r=2r, confirming the inward sign without a numerical experiment. Its03:13 follow-up agrees that the strict containment claim needs a common punctured-local-boundedness class.

A2831 confirms the scalar annular theorem and weak-L2 consequence. A2832 confirms the carrier sufficient criterion and the full-F necessary divergence at exactly Sections5-7. A2833 confirms the coefficient example and strict inclusion within the common class. A2834 refutes only the unqualified literal set containment in the original source Section7, with the off-center L2 singularity of Section8. A2835 leaves general weak-L2 continuation without punctured local boundedness, an Euler upper bound, exclusion of F and the full rotating conjecture open.

The comparison is through existing configured model working files. Actual provider execution is independently unattested. No new model client, agent, computation or formal verification was used.


## 11. Corrected common-class wording

The revised source10ab74243d1d0904ee2d5fd73f8454e57f1e12871548084160b2563834eaf74a was compared with the retained original and every changed line was read. Section7 now explicitly compares the two coefficient conditions within the class locally bounded off zero. Its inclusion argument uses Chebyshev and the union bound exactly as in Section8 above. New Section9 records the positive results A2831-A2833, the original literal wording defect A2834, and the open extensions A2835. This resolves the requested wording correction without strengthening any theorem. The original countertest remains valid for the unqualified sentence only.
