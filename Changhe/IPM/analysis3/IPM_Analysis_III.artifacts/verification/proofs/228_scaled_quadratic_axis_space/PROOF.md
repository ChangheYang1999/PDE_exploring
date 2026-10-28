# Scaled quadratic axis norms: mapping and an actual auxiliary exterior inverse

## Exact space and theorem

Use the exact joined normalized IPM trial rho0, k=1615536043799051/9007199254740992, ell=1/k, p=2k-1, and the canonical U,c,H0,M0 of topics217/222. Fix 0<alpha<1, p<beta<k, gamma>4k. Let chi be a fixed smooth radial function in [0,1], one on B2 and zero outside B4. Write w_gamma=(1+r^2)^(-gamma/2).

For an annulus A={R<=r<=4R}, define directional seminorms with both points in A:

 [h]_(x,alpha;A)=sup_(y fixed) |h(x,y)-h(x',y)|/|x-x'|^alpha,
 [h]_(y,2,alpha;A)=sup_(x fixed, x!=0)
             |h(x,y)-h(x,y')|/(x^2 |y-y'|^alpha),
 N_R(h)=||h||Linf(A)+R^alpha[h]_(x,alpha;A)
                     +R^(2+alpha)[h]_(y,2,alpha;A).

Only nonidentical pairs enter the suprema. Let Z2 consist of continuous physical-parity functions, even in x and odd in y, zero on x=0, with

 ||h||Z2=||chi h||E2+sup_(j>=0) 2^(-j beta) N_(2^j)(h)
                                  +||h||L2(w_gamma),      (1)

where E2 is the global bounded directional norm

 ||u||E2=||u||infinity+[u]_(x,alpha;R2)+[u]_(y,2,alpha;R2).

This retains a scaled quadratic axis condition on every annulus. It is distinct from the isotropically scaled Z of proof 222 and from the globally unscaled E2 target of proof 213.

The following qualitative assertions hold.

(a) Z2 is Banach, embeds boundedly into proof 222's Z, and c is bounded. The full coupling C0 h=U[h].grad rho0+c[h]M0 is bounded Z2->Z2. So are Cren=U[.].grad rho0+c[.]H0 and the unnormalized coupling. The residual F0 belongs to Z2. With a smooth radial cutoff tau_R, zero on B_R and one outside B_(2R),

 ||tau_R C0||_(Z2->Z2)
 <=C{R^(k-1)+R^(beta+k-gamma/2)
       +(R^(p-beta)+R^(2k-gamma/2))(1+log R)} ->0.          (2)

T=V.grad-1, V=ell X+U[rho0], and A0=T+C0 are closed on the same exact maximal domain

 D2={h in Z2:V.grad h is in Z2 distributionally}.          (3)

(b) On the exterior Omega_R={r>R}, let F_R^(2) consist of continuous physical-parity functions on its closure, zero on the vertical axis there, with

 ||h||F_R^(2)=sup_(j>=0) r_j^(-beta) N_(r_j)(h)
                         +||h||L2(Omega_R,w_gamma),
 r_j=2^j R.

There is no prescribed value on r=R. For every sufficiently large R, the ACTUAL exterior transport T_R=V.grad-1 is a closed bijection from

 D_R^(2)={h in F_R^(2):V.grad h is in F_R^(2) distributionally on Omega_R}

to F_R^(2), with inverse bounded uniformly in R.

(c) Fix smooth radial eta_R in [0,1], zero for r<=5R/4 and one for r>=2R. Put E_R h=eta_R h on Omega_R and zero inside, and P_R=exterior restriction. For large R,

 A_R^(2)=T_R+P_R C0 E_R:D_R^(2)->F_R^(2)                  (4)

is a closed bijection with a uniformly bounded inverse. It agrees with A0(E_R h) for r>=2R. Its transition discrepancy is explicit and remains to be matched globally.

No numerical constant or radius is supplied. No global inverse, Fredholm theorem, normalization or nonlinear closure follows from (a)-(c). The fractional-power forcings of proof 227 are excluded by (1). The local cubic coefficient J is still nonclosable on smooth zero-strain inputs in the A0 graph. This space is a candidate for further global work, not an existence theorem.

## Annular comparisons, axis values and multiplication

Put N=||h||Z2. Odd-y parity gives, by comparing (x,y) and (x,-y) in the same annulus,

 |h(x,y)|<=C N x^2 R^(beta-2), R<=r<=4R.                 (5)

This also holds at y=0 because h(x,0)=0. Scaled directional bounds imply ordinary scaled C^alpha bounds on fixed enlarged annuli. For close pairs, change one coordinate at a time; the intermediate points remain in a slightly enlarged comparable-radius annulus. The vertical difference is at most C N R^(beta-alpha)|Delta y|^alpha because x^2<=C R^2 there. For pairs with distance comparable to R use the supremum. Dyadic overlap supplies the enlarged-annulus directional bounds: pairs with comparable radii within ratio two share a dyadic annulus; for more separated radii use the supremum, and for the divided vertical difference use (5) at both endpoints. On any fixed enlargement all constants are uniform in R. The identical argument compares dyadic grids R2^j and 2^j.

These facts prove Z2->Z continuously. They also prove Banach completeness by local uniform convergence and passage of each directional difference bound to the limit, with the weighted L2 limit identified locally.

A smooth radial cutoff supported on a fixed multiple of an annulus, with scale-R derivative bounds, maps its directional norm to the global E2 norm after rescaling, with a fixed operator constant. For the vertical product difference, a factor from the cutoff is multiplied by |h|/x^2, bounded by (5). Thus the missing factor x^2 is preserved even for a pair crossing the cutoff boundary. The horizontal product uses the ordinary supremum and horizontal seminorm. The same proof gives the multiplier bound for any even-even coefficient a satisfying

 ||a||infinity+R||Da||infinity<=C

on comparable annuli. Separated pairs use the supremum. In particular multiplication by a, a^(-1), or a smooth cutoff is bounded uniformly whenever these bounds and a positive lower bound hold. Parity of the multiplier preserves the input parities.

## Divided velocity bounds on distant annuli

For R>=2, the following bounds hold on every fixed comparable-radius annulus, including directional pairs in that annulus:

 ||U[h]||infinity+R^alpha[U[h]]_(C^alpha)<=C N R^beta,
 ||U1[h]/x||infinity+R^alpha[U1[h]/x]_(y,alpha)
                                          <=C N R^(beta-1),
 [U2[h]]_(y,alpha)<=C N R^(beta-alpha).                   (6)

The quotient at x=0 has its continuous extension. The first bound already follows from proof 222 and Z2->Z. Here is a separate proof of the divided bound, so it is not inferred from ordinary C^alpha velocity regularity.

Split the input using smooth radial cutoffs into an inner region |Y|<R/4, comparable radii, and an outer region |Y|>8R, with overlapping transitions. The comparable-radius input, after rescaling X=R Z and dividing its amplitude by R^beta, has bounded GLOBAL E2 norm by the cutoff result above. It has physical parity. Proof 214's directional velocity estimates apply: on a fixed rescaled annulus, U1/x is bounded and uniformly C^alpha in the vertical variable, and U2 has a bounded vertical C^alpha norm. Those estimates use only the E2 norm; any compact auxiliary weighted L2 norm is automatically bounded. Scaling back gives precisely the last two estimates in (6) for this part. The canonical velocity is homogeneous of order zero under this dilation; parity fixes its subtraction constant.

For the inner part, beta>-2 gives an L1 mass bound C N R^(beta+2). Its separated kernel and first two output derivatives are bounded respectively by C R^-2, C R^-3 and C R^-4. Near the vertical axis, use odd-x parity and integrate the first x derivative along the horizontal segment from (0,y) to (x,y); that segment remains separated from the inner input because y is comparable to R. This gives |U1/x|<=C N R^(beta-1) and its y derivative at most C N R^(beta-2). Away from the vertical axis, |x| is comparable to R and division directly gives the same bounds. These two regions overlap, proving the bounds throughout the annulus. For distant vertical pairs use the supremum; for nearby pairs integrate the derivative on the comparable-radius segment. This yields the vertical Holder estimate in (6). The U2 estimate is the undivided separated-kernel bound.

For the outer part, the canonical subtracted kernel has size O(R|Y|^-3), with first and second output derivatives O(|Y|^-3) and O(|Y|^-4). The input bound |h(Y)|<=C N |Y|^beta, beta<1, gives the corresponding velocity and derivative bounds. Odd-x parity supplies U1/x just as above; the horizontal segment is always separated from the outer input. Thus (6) holds for every piece. This proof needs -2<beta<1, satisfied by the stated range.

## Complete coupling, tails and exact domains

On far annuli, the exact background divisions satisfy

 a1=rho0_x/x=O(R^(k-2)), a2=rho0_y/x^2=O(R^(k-3)),

with one more derivative costing R^-1. The ordinary gradient has size R^(k-1) with its scaled Lipschitz bound. The divided coupling identity is exact:

 (U[h].grad rho0)/x^2=a1(U1[h]/x)+a2 U2[h].               (7)

Equations (6),(7) give the vertical cofactor seminorm C N R^(beta+k-3-alpha), while the ordinary horizontal seminorm is C N R^(beta+k-1-alpha) and the supremum C N R^(beta+k-1). Therefore

 N_R(U[h].grad rho0)<=C N R^(beta+k-1).                  (8)

The local E2 factor is the already proved proof 222 localization identity using [chi,U]:Z->C^(1,alpha); Z2->Z supplies its input bound. This does not assume that h belongs to the globally unscaled E2 space. The weighted L2 output is integrated directly from its extra background-gradient decay, giving the tail C N R^(beta+k-gamma/2). Together with (8) and the cutoff multiplier bound this gives the first two terms in (2), including crossing pairs.

The exact residual has far size r^p times a smooth finite angular factor, divisible by x^2, with differentiated cofactor order r^(p-2). Thus N_R(F0)<=C R^p. Its local E2 and weighted L2 membership follow from proof 213, with the exact weighted threshold gamma>4k. Hence F0 belongs to Z2. The full M0 has the same smooth axis division, with far bound

 N_R(M0)<=C R^p(1+log R).

Proof 217 supplies its local E2 membership and the exact differentiated modal tail. Its weighted L2 tail is C R^(2k-gamma/2)(1+log R). Strict beta>p therefore gives precisely the remaining terms of (2). All four exponents are negative. Bounded strain follows from Z2->Z and proof 222. The compact H0 is in Z2 by its regularity and x^2 factor. This proves all coupling bounds.

Convergence in Z2 implies local uniform and distributional convergence, so the maximal transport realization (3) is closed. Subtracting the bounded C0 identifies the maximal full-expression domain with (3) and proves closedness of A0. The smooth zero-strain J=1 packets of proof 214 have compact support, and their Z2 input and actual transport-image norms tend to zero by their E2 bounds and fixed-compact norm comparisons. Bounded C0 gives the same for the full graph. J is therefore not closable here either.

## Time change preserving the quadratic vertical seminorm

An ordinary C^alpha composition estimate does not suffice for (b), because a general flow changes the x coordinate when y is varied. Use the exact positive time change

 a(X)=V1(X)/x=ell+O(r^(k-1)), q=1/a,
 W=V/a=(x,y b(X)/a(X)), b=V2/y.                         (9)

For sufficiently large r, a>=ell/2 and b/a is positive. All quotients extend through their axes by parity. The finite outer modal formulas give, through the derivative orders below,

 W=X+O(r^k), DW=I+O(r^(k-1)),
 q=k+O(r^(k-1)), Dq=O(r^(k-2)), div W=2+O(r^(k-1)).       (10)

The field W is defined on a fixed exterior r>=R0/2. Its radial component is at least r/2 there after enlarging R0. Let Psi_t be its forward flow. For every R>=R0 and starting radius r>=R, it stays outside R and satisfies, with constants uniform in R,

 c r exp(t)<=|Psi_t X|<=C r exp(t),
 ||D Psi_t(X)||<=C exp(t),
 c exp(2t)<=det D Psi_t(X)<=C exp(2t).                    (11)

Indeed the error integrals are bounded by C r^(k-1) integral_0^infinity exp(-(1-k)t/2)dt. Gronwall and Liouville then give (11). Crucially,

 (Psi_t(x,y))_1=exp(t)x                                  (12)

EXACTLY, independent of y.

Let m_t(X)=exp(-integral_0^t q(Psi_s X)ds). Equations (10),(11) give

 c exp(-kt)<=m_t<=C exp(-kt),
 |D m_t(X)|<=C exp(-kt) r^(k-2).                         (13)

For the derivative bound, differentiate the integral in the exponent and bound its integrand by C r^(k-2)exp((k-1)s), which is integrable. The functions m_t are even in each coordinate. All needed bounds also hold on starting segments in r>=R0/2 used to compare nearby points; the input f itself is evaluated only at exterior points.

## Scaled directional characteristic bound

The annular part of F_R^(2), denoted ||.||ann, obeys

 ||f(Psi_t .)||ann<=C exp(beta t)||f||ann.                (14)

For a close horizontal pair, the flow difference is at most C exp(t) times the input distance by (11); the ordinary scaled C^alpha comparison already proved from the directional norm gives the required horizontal estimate. For a close vertical pair with the same x, (12) gives exactly the same horizontal coordinate exp(t)x at both images. Their vertical difference is at most C exp(t)|y-y'|. Thus the input vertical seminorm bounds their difference by

 C N (exp(t)x)^2 (r exp(t))^(beta-2-alpha)
                     (exp(t)|y-y'|)^alpha
 =C N x^2 r^(beta-2-alpha)exp(beta t)|y-y'|^alpha.

Nearby starting segments stay in r>=R0/2, where the variational bound is valid. For distant vertical pairs, use the quadratic value bound (5) at the two images and |y-y'| comparable to r; no flow along a segment crossing the excluded interior is used. The horizontal distant-pair estimate uses the supremum. Enlarged-annulus comparisons cover both images uniformly. This proves (14), including negative beta.

The multiplier bound following (5), applied with (13), shows that multiplication by m_t costs at most C exp(-kt) in this annular norm. Multiplication by 1/a is uniformly bounded. Hence the exact candidate inverse

 Q_R f(X)=-integral_0^infinity m_t(X)
                         (f/a)(Psi_t X)dt               (15)

converges locally uniformly and satisfies

 ||Q_R f||ann<=C||f||ann/(k-beta).                       (16)

Every quadratic factor and both directional differences have been retained; no differentiability of f is used.

## Weighted L2 bounds and maximal-domain identities

The Jacobian comparison (11) and radius comparison give

 ||f(Psi_t .)||L2(Omega_R,w_gamma)
 <=C exp((gamma/2-1)t)||f||L2(Omega_R,w_gamma).

Combining with (13) proves the weighted bound in (15) with denominator k+1-gamma/2 when gamma<2+2k. For gamma>=2+2k, use (16)'s pointwise r^beta bound instead:

 ||Q_R f||L2(w_gamma)
 <=C||f||ann R^(beta+1-gamma/2)
                     /((k-beta)sqrt(gamma-2beta-2)).     (17)

Here gamma-2beta-2>=2(k-beta)>0 and the power of R is at most beta-k<0. These two regimes cover all gamma>4k, with constants independent of large R. No weighted velocity theorem is used. The exterior space is Banach by the same difference-limit argument as Z2, and its maximal transport operator is closed.

The cocycle identity for m_t gives, along every W orbit, the derivative

 W.grad(Q_R f)=q Q_R f+f/a.

Multiplication by a yields V.grad(Q_R f)=Q_R f+f. The continuous characteristic identity implies the same distributional equation by C1 flow boxes, as in proof 223's clarification. Thus Q_R f belongs to the exact maximal domain and T_R Q_R f=f. Conversely a domain element obeys this orbit identity. Its weighted endpoint is bounded by C exp((beta-k)t) and tends to zero, so Q_R T_R h=h. No density of smooth functions in the Holder norm is assumed. Continuity on r=R follows from the locally uniform convergent formula. This proves the actual transport bijection in (b), with no imposed inner trace.

## Cutoff extension and auxiliary nonlocal inverse

The extension E_R and restriction P_R are uniformly bounded between F_R^(2) and Z2. The annular cutoff comparison after (5) includes pairs crossing the zero collar and retains the x^2 factor; the local chi factor of E_R vanishes for R>=4. Weighted L2 does not increase. The dyadic-grid comparison proves the restriction bound. The same coefficient multiplier estimate shows E_R maps D_R^(2) to D2, because

 V.grad(E_R h)=eta_R V.grad h+h V.grad eta_R

and V.grad eta_R is O(1) with scale-R derivative bounds on the transition shell.

Equation (2), with an output tail that is identically one on Omega_R, gives

 ||B_R||_(F_R^(2)->F_R^(2))<=C epsilon(R/4)->0,
 B_R=P_R C0 E_R,

where epsilon is the right side of (2). If K is the uniform bound for Q_R and R is large enough that K||B_R||<1, then

 (A_R^(2))^(-1)=Q_R(I+B_R Q_R)^(-1)                     (18)

is a genuine left and right inverse on D_R^(2), with norm at most K/(1-K||B_R||). Bounded perturbation preserves the exact maximal domain and closedness. On Omega_R the precise discrepancy is

 A0(E_R h)-A_R^(2)h=(eta_R-1)T_R h+h V.grad eta_R.

It vanishes for r>2R and by continuity at r=2R. Matching this transition expression to the inner and middle regions is not supplied. No statement about a complete assembled error, injectivity on the whole plane or a complement inverse is made.

## Dependencies and scope

Topics214 and222 supply the explicitly stated directional velocity estimates and local commutator localization. Topics35/117/217 supply finite divided background and column derivatives. Proof 213 supplies local residual and exact weighted membership. Proof 214 supplies the global zero-strain normalization packets. The new scaled quadratic norms, velocity localization, time change, every directional flow comparison, weighted bound and exact auxiliary inverse are proved above. There is no numerical computation or new certified constant. The isotropic scaled counterexamples of proof 227 have |f_sigma|/x^2 unbounded on a fixed far axis segment, so are outside this space by (5). Their exclusion alone is not evidence of a global inverse.
