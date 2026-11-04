# Independent audit: smooth weak-L2 scalar continuation

## 1. Exact statement and audit scope

Let D be a bounded open disc in C, identified with R2 with Lebesgue area dA. Set dbar=(partial_x+i partial_y)/2. Suppose f is a smooth complex-valued function on D and b is nonnegative, measurable and finite almost everywhere, with

    |dbar f| <= b|f| almost everywhere,
    M = sup_{t>0} t [area{z in D:b(z)>t}]^(1/2) < infinity.       (1)

Then either f is identically zero or every zero has finite Taylor order and is isolated. A flat point means a point where every real derivative of f, including f itself, vanishes. In particular, a single flat point forces f=0. On a connected open planar set the same conclusion holds if b has finite weak-L2 norm on every relatively compact disc.

This is a smooth scalar theorem. It asserts neither the corresponding statement for arbitrary Sobolev solutions nor a vector-valued system. No smallness, punctured local L2, sign of a zero index, or removability of a prescribed closed set is assumed. Sections 2 to 8 prove the scalar statement. Section 9 gives its conditional carrier consequence. Section 10 records source and comparison scope.

## 2. Level-set control and finite-order zero geometry

Layer cake, split at M/sqrt(area E), gives for every finite-area measurable E in D

    integral_E b <= 2M sqrt(area E).                            (2)

The zero cases follow directly. Define q=(dbar f)/f where f is nonzero and q=0 on its zero set. Equation (1) implies dbar f=qf almost everywhere, including that set, and |q|<=b almost everywhere. Extend q by zero outside D. It is in L1(C), has bounded support and satisfies (2) with |q| on every finite-area set in C.

Let a be a zero of finite order m>=1, and let P be its nonzero degree-m homogeneous Taylor polynomial. Along a fixed countable positive sequence epsilon tending to zero, put f_epsilon(w)=epsilon^(-m)f(a+epsilon w) and b_epsilon(w)=epsilon b(a+epsilon w). On A={1/2<|w|<2}, f_epsilon converges to P in C1. Change of variables gives

    t^2 area{w in A:b_epsilon(w)>t} <= M^2.                    (3)

The rescaled quotients converge to (dbar P)/P wherever P is nonzero. Remove the union of the null sets for the countable sequence. Fatou's lemma for strict superlevel indicators yields the same bound (3) for |(dbar P)/P| on {P!=0} in A.

Write P(re^(i theta))=r^m p(theta). Polar differentiation gives

    (dbar P)/P = e^(i theta)[m+i p'(theta)/p(theta)]/(2r).       (4)

If the nonzero trigonometric polynomial p vanished at an angle theta0, real analyticity would give p'/p=d/(theta-theta0)+O(1), for an integer d>=1. On a fixed radial strip inside A, the superlevel area of (4) would be at least c/t for all sufficiently large t, contradicting its bound M^2/t^2. Thus p never vanishes. Its positive minimum modulus and Taylor's theorem imply |f(a+w)|>=c|w|^m for small nonzero w. The zero a is therefore isolated among all zeros. The finite-order zeros form a countable set, since each can be assigned a distinct rational basis neighborhood containing no other zero.

## 3. Finite total negative index

Every complex-valued homogeneous polynomial of degree m in the two real coordinates can be written P(z)=sum_{ell=0}^m c_ell z^ell conjugate(z)^(m-ell). Consequently p(theta)=e^(-im theta)Q(e^(2i theta)) for a polynomial Q of degree at most m with no unit-circle roots. Factoring Q shows that its unit-circle winding is the number N of roots inside the disc, with multiplicity. Thus the winding of p is

    k=-m+2N,  0<=N<=m.                                         (5)

Write f(a+w)=P(w)+E(w). Taylor's theorem gives E=O(|w|^(m+1)) and DE=O(|w|^m). Since |P|>=c|w|^m, E/P=O(|w|) and has bounded first derivatives off zero. Extending it by zero at the center gives a Lipschitz function: integrate along segments avoiding the center and pass to the limit for a segment through it. Hence f/P is close to 1 and has zero winding. The integer k in (5) is the local winding of f. Moreover,

    q(a+re^(i theta)) = e^(i theta) A(theta)/r + O(1),
    A(theta)=[m+i p'/p]/2,                                     (6)

uniformly in theta. The error bound follows by differentiating the Lipschitz quotient off zero.

For a fixed small disc about a, (6) gives b>=|A(theta)|/r-C almost everywhere. For large t the region 0<r<|A(theta)|/(t+C) lies in that disc and in {b>t} up to a null set. Integrating its polar area gives

    liminf_{t->infinity} t^2 area({b>t} intersect B_rho(a))
        >= d_a := (1/2) integral_0^(2pi) |A(theta)|^2 dtheta.

Since integral p'/p=2pi i k, mean Re A=(m-k)/2. Cauchy-Schwarz gives d_a>=pi(m-k)^2/4. For any finite collection of zeros choose disjoint such discs, sum the lower limits and compare with M^2. Taking the supremum over finite collections proves

    sum_a d_a <= M^2,
    sum_a (m_a-k_a)^2 <= 4M^2/pi,
    sum_{k_a<0} k_a^2 <= M^2/pi.                              (7)

For the last inequality, (5) gives m_a>=|k_a|. A negative integer has square at least 1, so there are only finitely many negative-index zeros in the whole disc D. Neither the flat set nor the other finite-order zeros need be finite.

## 4. A global Cauchy potential with controlled mean oscillation

Define almost everywhere on C

    s(z)=(1/pi) integral q(zeta)/(z-zeta) dA(zeta).             (8)

For a bounded set of z, the integral of |z-zeta|^(-1) over that set is bounded uniformly for zeta in the bounded support of q. Fubini and q in L1 therefore show that s is locally L1 and finite almost everywhere. The distributional normalization dbar(1/(pi z))=delta0 gives dbar s=q. This normalization follows by integration by parts outside a small circle and letting its radius tend to zero; its boundary integral is the value of the test function at zero.

For B=B(a,r) split s=s_near+s_far by restricting q to 2B and its complement. The far value c_B=s_far(a) is finite since the kernel is bounded there and q is L1. For zeta in 2B, B is contained in B(zeta,3r), so integral_B |z-zeta|^(-1)dA(z)<=6pi r. Using (2) gives

    mean_B |s_near| <= [6/(pi r)] integral_{2B}|q|
                     <= 24M/sqrt(pi).                        (9)

For z in B and |zeta-a|>=2r,

    |1/(z-zeta)-1/(a-zeta)| <= 2r/|zeta-a|^2.

On E_j={2^(j+1)r<|zeta-a|<=2^(j+2)r}, (2) bounds the q mass by 2^(j+3)sqrt(pi)Mr. Its contribution to |s_far(z)-c_B| is at most 2^(2-j)M/sqrt(pi). The geometric sum is 8M/sqrt(pi). Thus

    mean_B |s-c_B| <= 32M/sqrt(pi),
    mean_B |s-s_B| <= K := 64M/sqrt(pi),                       (10)

where s_B is the complex average. This is a direct bound for mean oscillation on every ball of the plane. It uses no exponential integrability theorem.

For concentric balls, (10) implies |s_{B(z,rho)}-s_{B(z,2rho)}|<=4K. Fix a compact set of centers. For 0<rho<=1, double until the radius is in [1,2). All resulting final balls lie in one fixed bounded set and have area at least pi. Their averages have uniformly bounded absolute value by local L1 of s. Summing the differences yields constants C0<infinity and C1=4K/log 2 with

    Re s_{B(z,rho)} >= -C0-C1 log(1/rho)                       (11)

uniformly for these centers. A harmless enlargement of C0 includes the extra doubling. Only an average bound has been proved and will be used.

## 5. Holomorphic and meromorphic representatives away from flat points

Let F be the relatively closed set of flat points of f. Where f is nonzero, q is smooth. To see that s has a smooth representative there, multiply q by a compactly supported smooth cutoff equal to 1 on a smaller disc. Its Cauchy potential is a smooth particular solution, since derivatives may be moved onto the cutoff data. Subtracting it leaves a locally L1 distribution with dbar equal to zero. The local Weyl lemma for dbar makes that distribution holomorphic. One elementary justification is to mollify, use the holomorphic mean bound to obtain local uniform bounds from L1 bounds, and pass to a holomorphic limit which agrees with the original L1 function. Smooth representatives agree on overlaps by their almost-everywhere equality. It follows by classical differentiation that h=f exp(-s) is holomorphic where f is nonzero.

At a finite-order zero a use the notation of Sections 2 and 3. The nonvanishing periodic function p(theta)e^(-ik theta) has winding zero, so it has a smooth periodic complex logarithm psi(theta). Integrating its logarithmic derivative constructs such a logarithm and the zero total increment ensures periodicity. The quotient f/P is close to 1, with a Lipschitz extension equal to 1 at the center. Its small single-valued logarithm g is Lipschitz and smooth off the center. On the punctured disc define

    s_a(w)=(m-k)log|w|+psi(arg w)+g(w).                        (12)

Then exp(s_a)=f(a+w)/w^k. Both log|w| and the bounded smooth angular function have integrable derivatives of size O(1/|w|), and g has bounded derivatives. They are W11 on the full small disc. Integration by parts on a punctured disc proves this directly: the removed-circle boundary term is O(epsilon(1+|log epsilon|)) and tends to zero. There is no angular jump because psi is periodic. Differentiation off zero gives dbar s_a=q; the integrable derivatives and the absence of a point distribution prove the same identity on the full disc.

Thus s-s_a is distributionally holomorphic and has a holomorphic representative a0 on the full disc. On the punctured disc,

    h(a+w)=w^k exp(-a0(w)).                                   (13)

The smooth representatives agree there, so this is a pointwise identity. It extends h meromorphically across a, with order exactly k. This includes k=0 and negative k. Every point in D minus F is either a nonzero point of f or one of these isolated zeros, so the local extensions define a meromorphic h on D minus F.

## 6. Pole cancellation and a uniform estimate near the whole flat set

By (7) the negative-index points are a finite set. Let

    Z(z)=product_{a:k_a<0} (z-a)^(-k_a),                       (14)

with empty product 1. The exponents are positive integers. Formula (13) shows that H=Zh extends holomorphically to D minus F. No extension across F has yet been asserted. On that open set, away from a countable set of zeros,

    log|H|=log|Z|+log|f|-Re s.                                 (15)

On every disc compactly contained in D minus F, H is not identically zero. Indeed f has only isolated zeros there, and Z has finitely many zeros. Thus log|H| is locally integrable and has the holomorphic logarithmic submean inequality. The logarithms on the right are also locally integrable there; finite-order zeros have only logarithmic singularities.

Assume F is nonempty. Choose concentric compact discs K0 in the interior of K1 in D. For z in K0 minus F set delta=dist(z,F). When delta is sufficiently small compared with the boundary margin and 1, there is a nearest a in F intersect K1. A minimizing sequence lies in a compact interior disc, and relative closedness supplies its limit. The disc B(z,delta/2) lies in K1 minus F. For every integer N>=1, Taylor's theorem at a, with uniform order-N derivative bounds on the convex disc K1, gives for w in B(z,delta/2)

    |f(w)| <= C_N |w-a|^N <= C_N(3delta/2)^N.                 (16)

The constants are independent of the chosen point a. We may enlarge them to be positive. Z is bounded on K1. Applying the logarithmic submean inequality at a point with H(z)!=0, then (15), (16) and (11), gives

    log|H(z)| <= C_N' + (N-C1)log delta.                       (17)

At a zero of H the resulting upper bound for its modulus is automatic. Since N can be arbitrarily large, for each real L>0 there is a local uniform constant C_L with

    |H(z)| <= C_L dist(z,F)^L                                (18)

for z close enough to F in K0. The exponent conversion uses delta<1 and an integer N with N-C1>=L. This argument estimates a mean of Re s, never a pointwise exponential. It applies even if F is perfect, has positive area, or has interior.

## 7. Direct extension and scalar continuation

Set H=0 on F. Estimate (18) gives continuity at F. For z outside F at small distance delta, use Cauchy's derivative estimate on B(z,delta/2). Take a slightly larger fixed compact disc when applying (18) on its boundary. Every boundary point w satisfies dist(w,F)<=3delta/2, so

    |H'(z)| <= C_L' delta^(L-1).                              (19)

For any a in F, (18) with L=2 and dist(z,F)<=|z-a| implies |H(z)-H(a)|<=C|z-a|^2 for all nearby z outside F, while the difference is zero for z in F. Hence the extended H is real differentiable at a with derivative zero. Formula (19), with L>1, shows that both real partial derivatives off F tend to zero at F. The extension is therefore C1 throughout D. It satisfies dbar H=0 both off F and on F, hence is holomorphic on D.

For any a in F, (18) and dist(z,F)<=|z-a| show |H(z)|<=C_L|z-a|^L for every L. A first nonzero holomorphic Taylor coefficient of degree j would contradict the estimate for L=j+1. Thus H vanishes on a neighborhood of a, and the identity theorem on the connected disc makes H identically zero. If f were nonzero at a point, that point could not be a zero of Z, since the zeros of Z are zeros of f. There s has a finite smooth representative and Zf exp(-s) is nonzero, a contradiction. Thus nonempty F forces f=0. If F is empty, Section 2 proves the isolation of all zeros.

On a connected open set with the stated local coefficient assumption, a flat point gives a zero neighborhood by the disc result. The set of points having a zero neighborhood is open. At any limit point of that set all derivatives vanish by continuity, so the disc result gives another zero neighborhood. The set is relatively closed and nonempty, hence is the whole connected domain.

## 8. Stress tests and indispensable hypotheses

For f(z)=conjugate(z) on D_R and b=1/|z| away from the center, (1) is an equality almost everywhere. The exact weak norm is M^2=pi, the order is m=1, the winding is k=-1 and d_a=pi. The charge and negative-index constants in (7) are sharp. In this case h has a pole, and the factor Z in (14) is necessary. This is not a flat-function counterexample.

An inverse-distance coefficient centered away from the distinguished center belongs to weak-L2 but not to L2 near its own singularity. Thus the coefficient class strictly includes the class requiring punctured local L2. The theorem makes no extension to nonsmooth f: arbitrary high Taylor estimates along F and the finite-order classification are essential steps as written. It makes no claim about systems, uniform constants in a parameter, or novelty in the literature.

## 9. Conditional carrier consequence and its limits

Fix 0<c<1/2 and omega in R. Let Jx=e3 cross x, A=cI-omega J, X(x)=Ax and L=(1-c)I+omega J. On an open U in R3 avoiding the origin suppose V is smooth, W=curl V and

    div V=0, X.V=0, (DV)X=-LV.                               (20)

Let sigma:D_R->U be a smooth transverse section, so det(partial_1 sigma,partial_2 sigma,X(sigma)) never vanishes. Suppose V is flat at sigma(0) and there is a nonnegative B in weak-L2(D_R) with

    |(W.X)(sigma(y))| <= B(y)|V(sigma(y))| almost everywhere.   (21)

Then V vanishes in a three-dimensional neighborhood of sigma(0).

The sole carrier import is the already confirmed local div-curl reduction A2463-A2464, before its Lp continuation step. On a smaller section chart, smooth isothermal coordinates z=phi(y) and a smooth complex f give |dbar f|<=[C_a+C_b B(phi^(-1)(z))]|f| with finite nonnegative constants. Smooth invertible linear maps relate f to the two section components of V, so f is flat at the center. Bounded Jacobians preserve weak-L2 under the coordinate change. A constant is weak-L2 on a bounded disc, and the union bound at half the threshold proves stability under addition. The scalar theorem gives f=0, hence V=0 on a section neighborhood.

Equation (20) integrates along finite orbit segments to V(exp(tA)sigma(y))=exp(-tL)V(sigma(y)). The flowbox map is a local diffeomorphism by transversality, so the zero section fills an ambient zero neighborhood. The same identity, differentiated in y and t, proves equivalence of section and ambient flatness. No global characteristic completeness, pressure normalization, boundary integral or behavior at infinity is used. The constants need not be uniform in omega.

The full common-flat system (F) already has punctured local boundedness and the previously confirmed weak-L2 obstruction A2832. This theorem gives no stronger necessary condition for (F), no derivation of (21) from Euler, and no solution of the unrestricted rotating-profile conjecture.

## 10. Verification and comparison status

All nine sections of the submitted source 107953fa2eb64535a43268543e8e0a0f3e05d4837b03b3d5e5c4779edcf980a3 and all 32 source self-check entries were read. The proof above reconstructs the main argument independently. The distributional Cauchy normalization, local dbar Weyl lemma and elementary holomorphic mean, Cauchy and identity theorems are explicit analytic dependencies. No exponential chain rule or removability theorem for F is imported.

No mathematical computation, formalization, new model client or subagent was used. The source plan corrects its own unsupported web-access claims; this audit records no new primary-source access and makes no claim that an external paper establishes this endpoint. The existing configured model comparison is now read in full, as recorded in Section 11; actual provider execution is independently unattested. This proof and the comparison were fully read before designated promotion.

## 11. Complete existing comparison and final scope check

The complete Theory Agent C  comparison stamped03:43 was read, including all nine numbered items, all four scope consequences and the optional constant improvement. It agrees with the independent reconstruction above. In particular, the Cauchy-potential estimate is an average estimate, not a pointwise bound on exp(-s). Uniform Taylor control over all nearby flat points converts that estimate through the logarithmic submean inequality into arbitrary-order distance decay. The subsequent Cauchy derivative estimate proves extension directly, with no assumption on the size, topology or measure of the flat set. The local W11 potential has no point distribution; its meromorphic order is the signed winding k. The finite negative-index budget is essential to the finite pole-cancelling product.

The comparison ran no new computation. Its earlier polynomial samples test some finite-order identities but do not establish this continuation argument. The optional sharper kernel integral 2pi r is unnecessary: the explicitly proved6pi r bound gives all stated constants and suffices. Keeping it avoids changing a valid proof merely to optimize an unused constant.

The zero function is the explicit first alternative. If M=0, then b=0 almost everywhere, q=0 and the argument reduces to classical holomorphic continuation. For a nonzero f, the theorem does not bound the positive vanishing order by M: f=z^N with b=0 allows every positive integer N. The negative-index conclusion is separate and has the correct sharp anti-holomorphic test. The argument requires full smoothness for Taylor estimates of arbitrarily large order; no statement for arbitrary C2 or Sobolev solutions is promoted.

The general smooth scalar weak-L2 continuation question left open by the earlier, narrower results is resolved by this proof. The conditional carrier criterion now needs no punctured local boundedness or punctured local L2 assumption. The coefficient-class enlargement is strict: for an off-center a, b=1/|z-a| on a bounded disc is weak-L2 but is not locally L2 at a; f=conjugate(z-a) satisfies the differential inequality and has a finite-order zero, in agreement with the theorem. The full system (F) already had the stronger off-orbit local boundedness, so its previously confirmed necessary obstruction does not strengthen. Deriving the coefficient bound from Euler, excluding (F), and proving the unrestricted rotating-profile conjecture remain open.

## 12. Additional coordinator comparison and source confirmation

The complete coordinator comparison, all nine analytic items and W1-W3, agrees with the proof above. Its twelve-check log and the earlier twelve-check log were read, as was the exact script difference. The deleted empty-generator clause was vacuous; the five actual polynomial tests remain. The label of the final non-monomial example was made explicit. These samples do not prove continuation and no computation was repeated in this agent.

The additional example q=1/conjugate(z) on the unit disc has Cauchy potential log|z|^2 inside and zero outside. Indeed this piecewise function is locally integrable, continuous across the unit circle, has the claimed distributional dbar derivative and vanishes at infinity. Subtracting the Cauchy potential gives an entire distributionally holomorphic function vanishing at infinity, hence zero. This also gives h=1/z and the pole-cancelling factor Z=z. The finite-disc level measure is pi min(R^2,t^(-2)), so the weak norm squared is pi. The sampled mean oscillations are diagnostic only.

The improved near-kernel bound 2pi r follows by integrating the superlevel estimate min(pi r^2,pi/t^2) for the kernel on a disc. The proof's looser 6pi r bound and all constants remain valid. Every zero of the cancelling polynomial is a zero of f, so the final contradiction at a nonzero point of f is legitimate.

The current source revision c69e4ac6c85dd2492e468555a03c62c0d3bf0dfafc3b3849021df4fc7382f27e changes only the status and adds a confirmation section. All changed lines were read. It accurately records A2870-A2873 and explicitly supersedes the old submission wording without changing a mathematical equation or hypothesis. The coordinator's revised opening explicitly places completion after the designated verdict and before reading it. This is consistent with the recorded times; the asserted reading order is not independently observable.


## 13. Supplementary exponential-integrability shortcut

The Theory Agent A  comparison A95, item 2, invokes John-Nirenberg to control exp(-s), then suggests the mean-value inequality for the absolute value of the pole-cancelled function. This needs a qualification that the confirmed proof does not need. A BMO bound of arbitrary size does not imply that exp(-Re s) is locally integrable at exponent one.

An explicit test lies within the present scalar hypotheses. On the unit disc let f(z)=conjugate(z), b(z)=1/|z| away from zero, and assign any finite value to b at zero. Then |dbar f|=b|f| almost everywhere, and the weak-L2 norm of b is sqrt(pi). The coefficient q is 1/conjugate(z), and Section 12 computes its zero-extended Cauchy potential as s(z)=log|z|^2 inside the unit disc and zero outside. This potential has the BMO bound established in Section 4. Nevertheless, on every disc of radius epsilon centered at zero,

    integral exp(-Re s) dA = 2pi integral_0^epsilon r^(-1) dr = infinity.

Thus there is no unqualified exponent-one integral estimate for this exponential, even for this smooth f. The pole-cancelled function in this example is harmless: h=1/z and Zh=1. This refutes the proposed general exponential-integrability implication, not the continuation theorem or the final conclusion of A95. A separate argument using a sufficiently small power might be possible, but none is required or asserted here.

The verified proof instead derives the exact meromorphic form near each finite-order zero from its local W11 potential (Section 5), cancels the finitely many negative poles, and applies the submean inequality to log|H| (Section 6). Only averages of Re s enter. The resulting arbitrary-power distance bound and Cauchy derivative estimates give direct C1 extension (Section 7). These steps are valid for every finite weak norm M.


## 14. The supplementary near/far constant is valid

Item 3 of A95, unlike the unqualified shortcut discussed in Section 13, gives a valid improvement of the elementary BMO estimate. Let B=B(a,r), let q be zero-extended as in Section 4, and write s=s_near+s_far by splitting at 2B. The weak bound gives integral_E |q| <=2M sqrt(|E|) for every measurable set E. Also, for every zeta, integral_B |z-zeta|^(-1) dA(z)<=2pi r by the layer-cake calculation in Section 12. Thus

    mean_B |s_near| <= (2/(pi r)) integral_2B |q| <=8M/sqrt(pi).

On E_j={2^(j+1)r<=|zeta-a|<2^(j+2)r}, j>=0, the kernel difference for z in B is at most 2r/|zeta-a|^2. The area is 3pi(2^(j+1)r)^2, so

    (1/pi) integral_E_j 2r |q(zeta)|/|zeta-a|^2 dA(zeta)
        <=2^(1-j) sqrt(3) M/sqrt(pi).

Summing j>=0 gives |s_far(z)-s_far(a)|<=4sqrt(3)M/sqrt(pi). With c_B=s_far(a), the preceding near bound gives

    mean_B |s-c_B| <=(8+4sqrt(3))M/sqrt(pi).

Since |s_B-c_B|<=mean_B|s-c_B|, it follows that

    mean_B |s-s_B| <=(16+8sqrt(3))M/sqrt(pi)<=30M/sqrt(pi).

The final coefficient inequality is strict because sqrt(3)<7/4; the displayed bound is strict when M>0. For M=0 the potential is zero. All integrals are justified by the global L1 bound on q and the locally integrable Cauchy kernel. This verifies the supplementary constant and also independently reaffirms the original weaker64M/sqrt(pi) bound. The main proof and its recorded constants are unchanged.
