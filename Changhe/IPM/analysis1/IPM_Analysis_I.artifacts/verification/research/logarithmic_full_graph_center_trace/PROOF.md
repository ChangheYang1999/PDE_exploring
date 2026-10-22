# Center normalization in the full linearized logarithmic graph norm

This standalone argument is written before new finite checks. Its status is OPEN until independent verification, actual Claude Opus5.5 review, resolution of objections and later own adjudication. It strengthens the frozen-graph result207 for orders below4. It does not give an inverse or a PDE exclusion.

## Exact statement

Let rho be the exactly joined and canonically normalized modal_v2 density, with the coefficient data and dependent join definitions of modal_repair. In particular rho is not the literal unjoined coefficient formula. Let ell=1/k and V=ell X+U[rho], where -Delta psi[f]=partial_xf and U[f]=(-psi_y,psi_x) use the full-plane sublinear gauge. Define Sigma(f)=psi[f]_xy(0) and

 Lh=V.grad h-h+U[h].grad rho+(Sigma(h)/3)X.grad rho.

For x>0 put z=log x, beta=1/2-b, and ||h||Y_(b,s)=||x^beta h||H^s(R²_(z,y)). Fix any real b<5/2 and any0<=s<4. There are smooth compact densitiesh_delta, even inx and odd iny, with a smooth compact factorh_delta=x²y a_delta, such that

 J(h_delta)=a_delta(0,0)=1, Sigma(h_delta)=0,
 U[h_delta] is compact,
 ||h_delta||Y+||Lh_delta||Y <= C_(b,s) delta^(5/2-b) ->0. (1)

Here0<delta<=1 and C_(b,s) is finite; no numerical ceiling for it is claimed. In particular this holds at s=153/50. The proof uses only local coefficients on a fixed compact rectangle and the exact compact potential; no far-field tail is estimated.

Define D_test to consist of smooth compact even-x/odd-y densities with a smooth compact x²y factor, Sigma=0, and h,Lh inY. Equip it with the full graph norm ||h||Y+||Lh||Y. Then J is not closable on D_test, its zero subspace is not closed and is dense relative to D_test, and the affine setJ=1 is not closed. Any closed linear realization ofL whose domain contains the constructed sequence has the same obstruction to a closed scalar-valued extension ofJ. This does not assert that L has any particular closed realization, and it does not exclude stronger norms that control the trace.

## Local regularity of the actual background

The exact finite modal representation has rho=x²y plus finitely many homogeneous terms of degrees5,7,...,17 with smooth angular factors, and terms of degreebi+3 times log polynomials of degree at most6, wherebi>50. Exact order-six joining and degree-seven splines with simple knots giveC6 on compact annuli. Direct differentiation of the inner terms proves rho inC^(4,alpha) on every compact set for each0<alpha<1.

Here is a direct regularity argument for the canonical velocity, avoiding differentiation of unspecified asymptotics. The leading Poisson source ispartial_x(x²y)=2xy, a degree-two polynomial. A degree-four polynomial stream particular solution is -x³y/3, since -Delta(-x³y/3)=2xy. Each remaining source term has degree at least4 with a smooth finite angular expansion, or has degreebi+2 times logs. Solving its finite radial ODE produces stream powers of degree at least6, possibly with additional finite log powers at resonances. The canonical regular interior homogeneous solutions are r^n sin(n theta), n even andn>=2, and hence Cartesian polynomials. There are only finitely many angular modes. Thus near0 the velocity is a polynomial of degree at most3 plus a remainder whose derivatives of ordersj=0,...,5 obey

 |D^j R_U| <= C r^(5-j)(1+|log r|^M).                   (2)

Higher-degree harmonic polynomials are included in that remainder. The finite terms withbi>50 satisfy(2). The C6 annular regularity ofU follows from the radial second-order equation withC5 source, as in205. In particular there is no interface singularity.

For completeness, a punctured smooth function with the bounds(2) extends asC^(4,alpha) at0 for everyalpha<1. Derivatives through4 extend, with fourth derivatives bounded by Cr(1+|log r|^M). For two points at distance t, if their radii are comparable andt is at most half the smaller radius, integrate the fifth derivative along their segment; the difference of fourth derivatives is at most Ct(1+|log t|^M). Otherwise both relevant radii areO(t), and their separate bounds give the same estimate. The constants on a fixed small ball are finite, and t(1+|log t|^M)<=C_alpha t^alpha. This proves the asserted local regularity ofU; the identical argument without logs applies torho. Bounds at positive radii come from the annular formulas.

Oddness of V1 inx now gives the exact quotient formula

 p(x,y)=V1(x,y)/x=integral_0^1 partial_xV1(tx,y)dt.     (3)

Consequently p isC^(3,alpha) on compact rectangles, including the line x=0. Derivatives through3 and their Holder differences can be passed under the integral; (tx,y) is uniformly Lipschitz fort in[0,1]. The other coefficients V2,rho_x,rho_y are alsoC^(3,alpha). A compact smooth cutoff equal to1 on[-2,2]² extends each of these four coefficients to a bounded C^(3,alpha) function onR². Their norms need not be small.

## The elementary multiplier estimate

A bounded function c with bounded derivatives through m, whose derivatives throughm are globally alpha-Holder, acts boundedly by multiplication onH^(m+theta)(R²) when0<theta<alpha<1. At integer orders bounded derivatives suffice. We need this only withm<=3.

To verify the fractional assertion, use the product rule throughm. For every coefficient derivativea and every corresponding derivativeg ofF, write

 a(v+w)g(v+w)-a(v)g(v)
 =a(v+w)(g(v+w)-g(v))+(a(v+w)-a(v))g(v).

The first term is bounded by||a||infinity times the fractional seminorm ofg. The squared second term, integrated against|w|^(-2-2theta)dvdw, is bounded by||g||2² times a finite constant: use |a(v+w)-a(v)|<=C min(|w|^alpha,1). The small-radius integral is proportional to integral_0^1 r^(2alpha-2theta-1)dr, and the large-radius integral to integral_1^infinity r^(-2theta-1)dr. Both are finite. The Fourier identity for this difference seminorm follows by Plancherel and rotation/scaling of integral|exp(i xi.w)-1|²/|w|^(2+2theta)dw; its positive finite value is a constant times|xi|^(2theta). Combining with integer derivatives gives the inhomogeneousH^(m+theta) estimate. This argument also covers lower derivatives using bounded higher derivatives and the same global Holder bound.

For each fixed s<4 choose m=floor(s) and, if theta=s-m>0, choosealpha intheta<alpha<1. The four extended physical coefficients above are therefore multipliers after the following pullback, uniformly indelta. Choose a fixed bounded smooth function phi(w)>0 equal toe^w forw<=log2, with all derivatives bounded and withphi(w)<=3. For an extended coefficientc, put

 c_delta(w,y)=c(delta phi(w),y).                        (4)

Chain and product rules through3, and the globally bounded derivatives ofphi, show uniform C^(3,alpha) norms for0<delta<=1. Holder bounds follow by composition with a uniformly Lipschitz map and by products with bounded smooth factors. Thus the multiplier norms of the four c_delta onH^s are bounded uniformly indelta. On the supports used belowphi(w)=e^w, so (4) equals the physical coefficientc(delta e^w,y). No assertion is made about a pullback that grows likee^w for all positivew.

## Compact potential and its exact scaling

Choose the smooth even cutoffchi of207, equal to1 on[-1,1] and0 outside[-2,2], and eta(y)=ychi(y). Set

 f_delta=-x^4 chi(x/delta)eta(y)/12, h_delta=-Delta f_delta.

The proof207 and its gauge clarification establish the smooth compact x²y factor, J=1, Sigma=0, and compact canonical velocity

 U1[h_delta]=-f_xy, U2[h_delta]=f_xx.

These facts can also be seen directly: near0h_delta=x²y and f_xxy=-x², whilepsi=f_x is compact and solves the exact Poisson equation. The sublinear uniqueness proof uses harmonicity of the difference, the mean-value gradient bound and component parity, and excludes any harmonic xy strain.

Putu=x/delta, a=5/2-b and

 H2=(partial_u²[u^4chi]/12)eta,
 H3=(partial_u[u^4chi]/12)eta',
 H4=(u^4chi/12)eta''.

For w=logu defineF_j(w,y)=e^(beta w)H_j(e^w,y). Direct differentiation gives, withz=w+logdelta,

 x^beta h_delta(z,y)=delta^a F2(w,y)+delta^(a+2)F4(w,y),
 x^beta U1[h_delta](z,y)=delta^(a+1)F3(w,y),
 x^beta U2[h_delta](z,y)=-delta^a F2(w,y).               (5)

Both velocity signs in(5) are part of the claim. Nearu=0 the profilesF2,F3,F4 are respectivelyu^a,u^(a+1),u^(a+2) times fixed smooth functions ofu,y. All their mixed w,y derivatives have the same powers. They vanish foru>2 and|y|>2. Sincea>0, all derivatives are square integrable withdwdy=dudy/u. Hence all three profiles lie in every finiteH^N, and their first w,y derivatives lie inH^s. Translation inw is unitary onH^s. No loss delta^(-s) occurs becausey is not rescaled.

## Full graph convergence

WriteF_delta(w,y)=delta^aF2+delta^(a+2)F4. The weighted local transport term, after translationz=w+logdelta, is exactly

 p_delta(partial_w-beta)F_delta
 +V2_delta partial_yF_delta-F_delta.                  (6)

This follows fromxpartial_x=xpartial_z/x=partial_z and the weight conjugation. The coefficient pullbacks equal the actual coefficients whereverF_delta or its derivatives are nonzero. The uniform multiplier estimates and fixed profile norms give anH^s bound Cdelta^a for(6).

The weighted nonlocal coupling, under the same translation, is exactly

 delta^(a+1)(rho_x)_delta F3-delta^a(rho_y)_delta F2.  (7)

ItsH^s norm is at most Cdelta^a, again by the uniform coefficient multiplier estimates. There is no separate tail: U[h_delta] is compact. The rank-one scaling term is zero exactly becauseSigma(h_delta)=0. Combining(5)--(7) proves(1). The support ofLh_delta is contained in the same compact rectangle, since all three local factors and the compact velocity vanish outside it.

## The trace conclusion and its scope

Everyh_delta belongs toD_test by(1), and (h_delta,Jh_delta) tends to(0,1) in the graph topology timesR. Any closed linear scalar extension agreeing with these values would contain(0,1), contradicting linearity at0. ThusJ is not closable in this graph topology.

The sequenceh_delta-h1 hasJ=0 and converges to-h1 withJ=-1, so the zero-J subspace is not closed. For anyh inD_test, h-J(h)h_delta belongs toD_test, hasJ=0 and converges toh in graph norm, proving relative density. The setJ=1 is not closed becauseh_delta tends to0. This reasoning deliberately does not claim that every compact zero-strain density hasLh inY at all negativeb: D_test includes image membership in its definition.

The theorem is local and qualitative. It does not computeC_(b,s), establishL closed or invertible, identify any spectrum, prove a uniform bound ofL onY, or exclude an exact IPM profile. It does not assert the endpoint s=4 or any larger order. The weaker frozen graph result207 remains valid for all finite orders. A Banach formulation for normalized profiles must separately justify a trace-controlling topology or a selected domain.

## Planned verification

The parent chain identifies the exact normalized trial and its finite end expansions. Independent rawNPZ versus integerhex/fmpq checks will verify the actual inner exponent and order data and finite derivative/scaling identities. The primary symbolic route and a second exact polynomial-jet route will check the signs and powers in(5), transport(6), and coupling(7). Finite algebra is not proof of the multiplier estimate or the graph-topology conclusion. Those are complete analytic arguments above and require an actual model review followed by independent adjudication. No new ball arithmetic or heavy CPU job is required.
