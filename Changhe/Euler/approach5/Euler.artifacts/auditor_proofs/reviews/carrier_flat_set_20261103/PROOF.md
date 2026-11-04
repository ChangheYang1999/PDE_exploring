# The flat set in the common-flat-orbit setting

## 1. Exact theorem and hypotheses

Fix0<c<1/2 and any real omega. Let Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, b=2(1-c), eta=a/b. Let G be the image of a smooth X-flowbox Phi:D0 times I0 to G, where D0 is an open disc about0 in R2, I0 an open interval, and Gamma=Phi({0} times I0) contains x0!=0. Thus G and G minus Gamma are connected, Gamma is closed relative to G and has empty interior, and X is nonzero on G.

Let V:G to R3 and S:G to R be smooth, W=curlV, E=|V|^2 and P=S+E/2. Assume on G

    divV=0, k=X.V=0, (DV)X=-LV, X.gradS=-bS,
    gradk=X cross W-aV, W.gradS=0, -Delta P=tr((DV)^2).

Assume S<0 on G minus Gamma, S=0 on Gamma, and V,S vanish to infinite order at x0. Flatness means all derivatives, including order0, vanish. All norms are Euclidean, with Frobenius norm for matrices. Write H=-S. These are the complete local assumptions called F, not a consequence asserted for every decaying profile.

Then the flat set of V is exactly Gamma, and the flat set of W is the same. V and W have the same zero set in G. If p in G minus Gamma is a zero, there are C>0, an integer N>=1, a disc D about0, t1>0 and a smooth flowbox

    Psi(y,t)=exp(tA)(p+O(y1,y2,0))

with O a proper orthogonal matrix, image in G minus Gamma and Psi(0,0)=p, such that

    |V(Psi(y,t))|>=C|y|^N for y in D and |t|<t1.

Thus its zeros in this neighborhood form exactly one X-orbit segment. V is zero on no nonempty open subset of G. Neither one-sided flat carrier field constructed in C65 can satisfy F on any choice of such G with a base point at which it is flat. The general existence or exclusion of F remains open.

The new source is Theory Agent C C66, pinned as in the team records, SHA256 c70118a8e174ee243629326543887d1e7094f04c7e9c5c6ec66c5aa3af837416. Source Sections1-4 were read completely, along with C60's exact setting and C64's complete proof Steps1-4. The displayed source hash agrees with the retained bytes. No computation is required.

## 2. A local relation between V and W off Gamma

On G, gradk=0 gives aV=X cross W. Off Gamma, H>0, so ell=grad logH is smooth. The two scalar transport relations give ell.W=0 and ell.X=-b. The triple-product identity therefore gives

    a ell cross V=ell cross (X cross W)
                  =X(ell.W)-W(ell.X)=bW,
    W=eta ell cross V.

On any sufficiently small ball with closure in G minus Gamma, |ell| has a finite maximum M. Consequently |W|<=eta M|V| there. This uses no division by V or W; it holds at their zeros as well. Combined with aV=X cross W, it proves equality of their zero sets off Gamma.

The local unique continuation theorem A2348 applies as follows: if V is smooth near a nonzero point p, divV=0, X.V=0 and (DV)X=-LV, and |W|<=kappa|symDV|+C0|V| with0<=kappa<sqrt2, then flatness at p forces V to vanish near p. Here kappa=0 and C0=eta M suffice. That theorem has no S or P hypotheses; its exact proof and primary quasiconformal inputs are retained in the A2347-A2352 audit. Section4 below records the part of its proof needed without flatness.

## 3. Connectedness, pressure and the exact flat set

Let F0 be the flat set of V relative to G minus Gamma. Continuity of every derivative makes it closed there. If p belongs to F0, Section2 and A2348 give a neighborhood on which V=0. Every point of this neighborhood is flat, so F0 is open. Connectedness of the punctured flowbox makes F0 empty or all of G minus Gamma.

In the latter case continuity gives V=0 on G. Then P=S and Delta S=0. Since S<=0 and S(x0)=0 at an interior point of connected G, the harmonic maximum principle makes S=0 throughout G. This contradicts S<0 on its nonempty punctured flowbox. Thus F0 is empty. Notice that this step is where the pressure equation is used; it cannot be discarded from the full claim.

For each p in Gamma choose tau with p=exp(tau A)x0. The compact orbit segment from x0 to p lies in G, so a sufficiently small neighborhood of x0 and every intermediate time stay in G. Integrating the vector transport equation there gives

    V(exp(tau A)x)=exp(-tau L)V(x).

The two matrices are invertible and the change of variables is linear. The chain rule therefore propagates every vanishing derivative from x0 to p. V is flat at every point of Gamma. Since W=curlV, W is flat at every such point. Conversely aV=X cross W makes flatness of W imply flatness of V by the Leibniz rule. Their flat sets are exactly Gamma. This also finishes equality of the zero sets on Gamma.

If V vanished on an open nonempty O in G, every point of O would be flat and O would lie in Gamma, impossible because Gamma has empty interior. No global completeness, boundary integration, pressure normalization, far-field decay or uniform estimate in omega is used here.

## 4. Transverse factorization and a polynomial lower bound

Fix a zero p off Gamma. The bounded estimate of Section2 holds on a ball U about p. Choose O with Oe3=X(p)/|X(p)|. In translated rotated coordinates, X3>0 on a smaller ball. On its transverse plane put xi=(X1,X2)/X3, v=(V1,V2), and Q with first two rows I2 and third row -xi^T. The relations X.V=0 and (DV)X=-LV give

    V=Qv, DV=Q(Dv)Q^T+K, |K|<=C1|v|,
    divv=-xi^T(symDv)xi-trK,
    (curlV)3=partial1 v2-partial2 v1.

These formulas and their coefficients are smooth and bounded locally. Let f=v1+i v2. Then

    2 f_z=divv+i curlv,
    |symDv|^2=2|f_barz|^2+(divv)^2/2.

On a sufficiently small disc |xi|<=delta. Using |curlV|<=C0|V| and the displayed trace identity gives, exactly as in A2348,

    |g_barz|<=k|g_z|+C4|g|, g=conjugate(f),
    k=delta^2/(sqrt2-delta^2)<1.

Choose delta small enough that its denominator is positive and k<1. None of these steps uses flatness.

For completeness, this inequality admits bounded measurable mu,alpha with |mu|<=k, |alpha|<=C4 and g_barz=mu g_z+alpha g. Where |g_barz|<=k|g_z| take alpha=0 and the quotient for mu, with zero assigned if both derivatives vanish. On the other set g!=0; choose mu g_z to have the phase of g_barz and modulus k|g_z| and put the residual divided by g into alpha. Extend both coefficients by0 off a smaller disc. The already checked inhomogeneous Beltrami theorem gives continuous s in W^(1,p)_loc for some p>2 satisfying s_barz-mu s_z=alpha. The product rule shows h=exp(-s)g solves h_barz=mu h_z. Its continuous representative has the factorization

    h=F composed chi,

where F is holomorphic and chi is a quasiconformal homeomorphism. The inverse of chi is locally Holder. These are precisely the primary inputs checked in A2347-A2348, with their manuscript passages retained there. They are used before any flatness conclusion.

If F were identically0 on the connected image disc, v would vanish on a transverse disc. The local transport formula would then give V=0 on a neighborhood of p, contradicting Section3. Thus F is not identically0. Since v(0)=0, F has a zero of a finite integer order m>=1 at zeta0=chi(0). Shrinking its neighborhood gives constants d1>0,rho>0 with |F(zeta)|>=d1|zeta-zeta0|^m. Local Holder continuity of chi^-1 supplies0<beta<=1 and M1>0 with

    |y|<=M1|chi(y)-zeta0|^beta.

Continuity of s on a compact smaller disc gives d0=min|exp(s)|>0. Combining these inequalities yields

    |v(y)|>=d0 d1 M1^(-m/beta)|y|^(m/beta).

The inverse Holder estimate is used in the lower-bound direction here; no differentiability of chi or its inverse is asserted.

The map Psi(y,t)=exp(tA)(p+O(y,0)) has invertible derivative at(0,0), since X(p) is transverse to the chosen plane. On a sufficiently small product it is a diffeomorphism into G minus Gamma, and V(Psi(y,t))=exp(-tL)OQ(y)v(y). Q^TQ=I2+xi xi^T gives |Qv|>=|v|. The maximum M2 of ||exp(tL)|| for |t|<=t1 is finite, so |V(Psi(y,t))|>=|v(y)|/M2 uniformly there. Choose D of radius<=1 and N=ceil(m/beta)>=1; then |y|^(m/beta)>=|y|^N. This proves the theorem with C=d0d1 M1^(-m/beta)/M2. At y=0 the transport formula gives V=0, and at y!=0 the lower bound gives V!=0. Hence the zero set is exactly the stated orbit segment. All constants can depend on the point, fields, c and omega.

## 5. Exclusion of the C65 examples and the singular coefficient

For the first C65 field, g(theta)=exp(-1/(theta0-theta)) when theta<theta0 and0 otherwise. Its remaining coefficients are linear functions of g and an integral from theta0, so it is zero on theta>=theta0 and flat on the cone theta=theta0. It is nonzero on theta<theta0 because g>0. Thus any open G containing a flat base point contains an open nonempty subset with V=0: immediately if theta(x0)>theta0, and by moving a small distance in the e_theta direction if theta(x0)=theta0. This contradicts Section3. The other field has the same argument with the inequalities reversed. This excludes BOTH particular fields from F, including the positive-trace field, for every possible choice of the additional scalar S and flowbox. It does not exclude a different positive-trace field with a flat set consisting only of Gamma.

The estimate |grad logH|<=C0 off Gamma is local to points away from Gamma. It cannot be upgraded even to C/|y| on a punctured affine transverse disc about x0. Such a bound would give, on each fixed radial ray and fixed r0>0,

    logH(r)>=logH(r0)-C log(r0/r),
    H(r)>=H(r0)(r/r0)^C.

Flatness of positive H at the center implies H(r)=O(r^N) for every integer N and contradicts this bound for N>C. The bounded-coefficient unique continuation proof therefore does not reach Gamma by this argument.

## 6. Dependencies and unresolved claims

The full C66 source, exact F setting, C64 Steps1-4 and complete independent A2347-A2352 and A2375-A2379 proofs were read. Source pins and their hashes are in the team records. No symbolic or numerical calculation was needed; the issue is a local factorization and hypothesis check. No formal build is supplied.

C66 Remark4 reports a separate the external referee (a second model) whose exact formulas the source says it has not rechecked. This audit does not certify that construction. The abstract observation that a flat surface or an open flat region cannot equal the one-dimensional Gamma follows from Section3, without that example. The source's main theorem, Corollary and the logarithmic-coefficient obstruction have complete proofs above.

The endpoint tr((DV)^2)>=0 in the full setting F, the existence or exclusion of F itself, any uniform transverse exponent near Gamma, and the unrestricted smooth decaying arbitrary-helicity, arbitrary-rotation profile theorem remain OPEN. The finite exponent N above is local to a zero off Gamma; it does not bound orders near the distinguished flat orbit.
