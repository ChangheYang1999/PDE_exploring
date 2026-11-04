# Smooth and quasi-analytic actual tails

Status: complete independent proof of the regularity and flatness assertions in the revised C48, with a self-contained quasi-analyticity argument. The pressure-deficit assertion is proved separately in the indexed high-order pressure review. The full LIT214 and LIT215 sources are also compared here.

## 1. Exact Euler class and hypotheses

Fix 2/5<c<1/2 and finite real omega. Let Jx=(-x2,x1,0), A=cI-omega J, p=(1-c)/c, a=1-2c, b=2(1-c) and q=b/a. Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0, (1-c)U+DU(Ay+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1).

C is finite. Use the canonical pressure constant Pinf, complete carrier flow Phi_t of B=Ay+U, escaping set E and actual C1 scattering diffeomorphism Xi:E->D=R3 minus0. Define

    u_t(x)=exp((1-c)t)exp(omega tJ)U(exp(tA)x),
    p_t(x)=exp(bt)(P(exp(tA)x)-Pinf), z_t=exp(-tA)Phi_t.

Their unique C1 local limits are V,P2,Xi. Put W=curl V, X=Ax, k=X.V, Z=int_D{k=0}, S=P2-|V|^2/2, Q=P-Pinf-|U|^2/2, H=P-Pinf+|U|^2/2+(Ay).U and M=integral_0^infinity exp(ar)Q o Phi_r dr. A1180-A1182 supply the exact Kelvin identities and C1 convergence. Tail homogeneity and Poisson give

    V(exp(tA)x)=exp(-(1-c)t)exp(-omega tJ)V(x),
    X.grad S=-bS, -Delta P2=tr((DV)^2).

The confirmed finite-order theorem A1151 says U=0 if V is smooth near every point of

    T0={V=DV=0, S=P2=0} intersect supp W

and its first nonzero Taylor term is finite there. The sphere and its transported D version are equivalent. No isolated-leading hypothesis is needed.

The exterior all-order condition means U is smooth for |y|>R0 and, for every j>=0, |D^jU(y)|<=C_j |y|^(-p-j) there, with separate finite C_j. Derivative norms are Euclidean multilinear operator norms. The global version also requires U smooth on R3 and natural bounds there. A quasi-analytic exterior condition is

    |D^jU(y)|<=C_* L^j M_j |y|^(-p-j), |y|>R0, all j>=0,
    M0=1, M_j>0, M_j^2<=M_(j-1)M_(j+1),
    sum_(j>=1) M_(j-1)/M_j=infinity,

with the same finite positive C_*,L for all orders and points. Its j=0,1 cases plus compact C2 regularity supply both global natural bounds even if those are not separately assumed.

## 2. Exterior smoothness and convergence of the tails

Orthogonality of exp(-omega tJ) and cp=1-c give on every fixed compact subset of D, for all sufficiently large t,

    |D^j u_t(x)|<=exp((1-c+jc)t) C_j |exp(tA)x|^(-p-j)
                 =C_j |x|^(-p-j).

On slightly larger compact neighborhoods, one extra derivative gives equicontinuity at each finite order. Arzela-Ascoli and the unique C1 limit show that every subsequential Cj limit is V. Thus the entire family converges in each local Cj norm; V is smooth, and all displayed bounds pass to V. Only exterior smoothness is used.

The original profile equation gives smooth grad P in the exterior. Its divergence is

    -Delta P=tr((DU)^2).

The terms tr(DU A) and omega tr(JDU) cancel, because div U=0 and A=cI-omega J. Rescaling gives exactly

    -Delta p_t=tr((Du_t)^2), b+2c=2.

The right side has bounded norms of every finite order on nested compact balls, and p_t is locally C0 bounded by its known C1 convergence. Interior Poisson estimates therefore bound p_t at every order. Compactness and uniqueness again give p_t->P2 in C-infinity locally. Equivalently smoothness of P2 alone follows by subtracting a Newton potential of a smooth local source and using harmonic regularity. No bound on original pressure derivatives was assumed.

## 3. Smooth scattering requires smoothness along the original flow

Under the GLOBAL all-order hypothesis, B and its finite-time flow are smooth. For F_t(z)=exp(-tA)U(exp(tA)z),

    d_t z_t=F_t(z_t), |D^jF_t(z)|<=C_j exp(-t)|z|^(-p-j).

On a compact subset K of E, all z_t(K) eventually lie in one compact annulus. The differentiated flow equation at order n is

    d_t D^n z_t=DF_t(z_t)D^n z_t+R_n,

where R_n is a finite sum of higher derivatives of F_t multiplied by lower derivatives of z_t. Starting with the known C1 control, induction and Gronwall with the integrable coefficient exp(-t) bound every D^n z_t. The equation then makes d_t D^n z_t=O(exp(-t)), uniformly on K. Consequently z_t converges in every local Cn norm and Xi is smooth. Its determinant is1 by the confirmed C1 theory, so its inverse is smooth too.

Set q_t=p_t-|u_t|^2/2. The composition q_t(z_t)=exp(bt)Q o Phi_t converges smoothly to Sigma=S o Xi. Split M at a large finite time t1. The finite integral is smooth and the remaining integrand is exp(-r)q_r(z_r), whose every Cn norm is bounded by a constant times exp(-r). Differentiation under that integral proves M smooth. An exterior-only smoothness condition does not justify a smooth flow through a merely C2 core; the stronger premise here is essential to this proof.

## 4. A self-contained one-dimensional quasi-analyticity lemma

Let f be smooth on an interval and suppose |f^(j)|<=M_j for all j on a compact segment. Assume the weight conditions of Section1. Define mu_j=M_j/M_(j-1), so log convexity says mu_j is nondecreasing. Define the continuous function

    B_f(x)=sup_(j>=0) |f^(j)(x)|/(e^j M_j), 0<=B_f<=1.

Continuity follows because the terms with j>=N are bounded uniformly by exp(-N), while the finite initial maximum is continuous. For an integer q>=1 and a segment from x to x+h in the interval, Taylor's formula gives

    B_f(x+h)<=max(B_f(x),exp(-q)) exp(e mu_q |h|).           (4.1)

Indeed, for j<q expand f^(j) through order q-j-1. Log convexity bounds M_(j+k)/M_j by mu_q^k. The initial terms are bounded by B_f(x) times the corresponding exponential series in e mu_q|h|. The remainder uses the uniform bound |f^q|<=M_q and is bounded, after division by e^jM_j, by

    exp(-q) (e mu_q |h|)^(q-j)/(q-j)!.

Replacing both prefactors by their maximum proves(4.1) for j<q; for j>=q the crude exp(-j)<=exp(-q) suffices.

Suppose all derivatives vanish at0, but B_f(x*)>0 at a point x*>0 of the segment. Choose n0 with exp(-n0)<B_f(x*). For each n>=n0 let t_n be the first point of [0,x*] where B_f=exp(-n). Continuity gives 0<t_(n+1)<=t_n. Applying(4.1) from t_(n+1) to t_n with q=n+1 yields

    t_n-t_(n+1)>=1/(e mu_(n+1)).

Summing disjoint intervals contradicts divergence of sum1/mu_j. The negative side follows by reflection. Thus flatness at one point forces f=0 throughout any such interval segment. Bounds C L^jM_j reduce to these bounds by dividing f by C and rescaling the independent coordinate; local segment constants suffice. This proves the exact Denjoy-Carleman implication needed here without relying on a book theorem number or an unverified external statement.

## 5. Quasi-analytic tails and the Euler corollary

Section2 passes the same weight bound to V:

    |D^jV(x)|<=C_* L^j M_j |x|^(-p-j).

On a closed line segment in D at distance at least rho>0 from0, any scalar component restricted to the line has derivative bound C_* rho^(-p)(L/rho)^j M_j. Section4 therefore applies. If V is flat at x0, restrict to every line through x0 in a small ball in D. Every component vanishes along each diameter, so V=0 on the ball.

The set of points where all derivatives of V vanish is relatively closed by continuity, and the previous argument makes it open. Since D is connected, it is empty or all of D. In the latter case V=W=0 and the established tail recovery gives U=0. For a hypothetical nonzero U it is empty, so every zero of V has finite order. In particular every T0 point meets A1151, which again gives U=0, a contradiction. Hence the quasi-analytic exterior hypothesis implies U=0 at the exact HF/natural Euler class for every finite omega.

The source example M_j=j^j(log(j+e))^j, M0=1, is valid. The function x log x+x log log(x+e), continuously extended at0, is convex: the second derivative of its second term is

    ((x+2e)log(x+e)-x)/((x+e)^2 log(x+e)^2)>0.

Thus the sequence is log convex. For j>=2 its ratio mu_j is at most e^2 j log(j+e), using (1+1/(j-1))^(j-1)<=e and the mean-value bound on log(j+e)-log(j-1+e). Hence sum1/mu_j diverges. Finally M_j/j!>=(log(j+e))^j, so this example is not bounded by any fixed geometric multiple of j!. It allows derivative-bound sequences growing beyond every geometric multiple of the factorial sequence. Arbitrary separate C_j or Gevrey weights with exponent greater than1 give no such conclusion here.

## 6. Factorial and conic-holomorphic sufficient conditions

For M_j=j!, Section5 applies directly. The explicit elementary analytic proof in LIT215 also passes: on a ball about x0 with r0=|x0|/2,

    |D^jV|<=C_* r0^(-p)(L/r0)^j j!.

The degree-n Taylor remainder on a segment of displacement h is at most C_*r0^(-p)(L|h|/r0)^(n+1). It tends to0 for |h|<r0/[2max(1,L)]. This proves real analyticity of V using EXTERIOR-only factorial bounds, with no original-core or scattering-map analyticity. The j=0,1 cases provide the global natural bounds by compactness. A1156 or A1151 then gives U=0.

A holomorphic extension of U to |Re z|>R0, |Im z|<delta|Re z| with |U(z)|<=C|Re z|^(-p), delta>0 fixed, also supplies exterior factorial bounds. At real x with |x| sufficiently large, a complex polydisc of radius a fixed small multiple of min(delta,1)|x| stays in that domain and has real part of size comparable to |x|. Multivariable Cauchy estimates bound each partial derivative by C' L'^j j! |x|^(-p-j). Converting finitely many components and tensor norms costs a geometric factor in j, absorbed into L'. This is another sufficient exterior condition, not a consequence of unquantified real analyticity.

## 7. Infinite flatness on the original orbit and its limit set

Assume the global all-order condition. If V is flat at x0, homogeneity makes it flat at exp(tA)x0 for every finite real t. The same holds for W and k. Smooth Xi and its inverse and

    W o Xi=DXi Omega, Omega=curl U

then make Omega flat at every y_t=Phi_t(Xi^(-1)x0). Each derivative of Omega is continuous on R3 and vanishes on the backward half-orbit, so it vanishes on its closure. The alpha-limit set is nonempty, compact and invariant because that half-orbit is bounded. Every forward orbit in it stays in this compact set, hence it lies in the carrier core K. This statement does not require that the closure of the entire backward half-orbit itself lie in K.

The Kelvin identities

    U-grad M=DXi^T V o Xi, H+aM=k o Xi

make both left sides flat at every y_t. The smooth convergence in Section3 gives convergence of all finite jets of exp(bt)Q o Phi_t to Sigma at the original preimage. A1163 already gives size flatness of original Omega with only C1 Xi; the stronger global hypotheses here justify all derivative and closure assertions directly.

## 8. Formal pressure jets: the exact freedom and its limits

At an infinite-order V zero, |V|^2 and tr((DV)^2) are flat. Consequently S and P2 have the same Taylor series T, which is harmonic term by term. Since X.grad S=-bS, if H_l is its lowest nonzero homogeneous term at x0 then

    Delta H_l=0, X0.grad H_l=0, X0=Ax0!=0.

It is a planar harmonic homogeneous polynomial in X0-perpendicular coordinates. Degree0 is permitted at a general flat V zero; at T0 it is excluded because S=0 there.

Conversely, any such H_l extends to a FORMAL harmonic series obeying this homogeneity. If H_j is already harmonic, put F_j=-((Ah).grad+b)H_j. This is homogeneous and harmonic: Euler dilation and rotations commute with the Laplacian up to its scalar weight. Seek H_(j+1) harmonic with X0.grad H_(j+1)=F_j. In coordinates (n,zeta), X0=ell e_n, set I=integral_0^n F_j(n',zeta)dn'. Then Delta I=partial_n F_j(0,zeta). Choose a homogeneous planar polynomial G of degree j+1 satisfying

    Delta_zeta G=-ell^(-1)partial_n F_j(0,zeta).

The planar Laplacian is onto between these polynomial degrees. One elementary verification is to solve a monomial by twice integrating in one variable and canceling the resulting lower exponent in the other variable recursively; the recursion terminates. For j=0 the source is zero and take G=0. Then H_(j+1)=ell^(-1)I+G has the required derivative and Laplacian. Recursion proves the formal extension. Rank identities containing only the flat coefficients W,k,grad k have identically zero formal series at this point.

This proves freedom to choose the LOWEST planar harmonic term subject to these identities. Higher terms still obey the displayed recurrence, the series need not converge, and no actual smooth tail or global Euler profile has been constructed. The result does not justify an unrestricted assertion that arbitrary pressure jets or all possible formal arguments are unconstrained.

If {W!=0} is dense on a neighborhood and S has finite order, the rank identity k dS=qS dk holds everywhere there. With smooth flat k, the established scalar lemma A1141 makes k=0 on a neighborhood. This confirms C48(d5), including the case S(x0)!=0. Neither local density nor finite order of S has been established generally.

## 9. Full LIT214 comparison and dependency closure

All nine LIT214 sections were read. The finite scalar term follows from the explicit strictly negative circle mean of Delta S at order2m-2. The smooth rank defect vanishes to every order at a supported point even without neighborhood density; its lowest product gives (l-qs)H_lK_s=0, impossible since l<=2m<qs. Thus k is flat and the leading velocity is planar. A repeated stream factor t^j, j>=2, would force scalar normal multiplicity q(j-1), while the exact nonzero pressure coefficient -j^2(j-1)(2j-3)Q0^2 forces multiplicity2(j-1). Since q>2 these are incompatible. The leading transverse velocity is therefore isolated. This matches the complete independent A1139-A1151 proof and removes LIT214's submitted dependency caveat.

The global support assembly retains both its phases: every T0 lies in the interior of E0=supp(1_Z V restricted to the sphere), boundary E0 is contained in T0, and the common-zero theorem gives T0 nonempty for nonzero U. Thus E0 is the whole connected sphere. The globally k-zero finite-index theorem then contradicts Poincare-Hopf. The pressure smoothness deduction, local non-density argument and analytic-tail corollary all match their exact confirmed premises. This is a conditional theorem on the explicit smooth finite-order hypothesis, not on isolated leading directions.

All five LIT215 sections were read; Section6 independently checks its full exterior-only statement and explicit radius. These hypotheses do not follow from bare velocity decay, original smoothness or qualitative original analyticity. The unrestricted main conjecture remains open.

## 10. Scope and verification

Every assertion is at the exact global HF/natural class of Section1 or at the explicitly stated one-dimensional or formal local class. No symmetry or smallness of finite omega is imposed. Smooth tail convergence, smooth scattering and quasi-analytic nonexistence have different premises and are not conflated. C48's former unsubmitted irrational-parameter analytic argument is superseded and is not used.

The revised seven-section C48 was read in full, including all new parts(d1)-(d5). Sources and this proof are retained with checksums after post-read. The quasi-analytic implication is proved directly above; the source's Hormander theorem number is not separately certified. C48 is from the configured model agent, runtime unattested. A focused comparison of the direct lemma and formal-scope clarification is requested through existing agents. No computation, formal build, new model client or new agent is used.
