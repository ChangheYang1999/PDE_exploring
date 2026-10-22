# Incoming endpoints and the sign-independent local Gevrey obstruction

Status: CONFIRMED for candidatev3 after independent proof, exact controls, actual-source checks, and the model exchange recorded in verification/. This is a conditional local theorem. It is not a full nonexistence result for smooth B2 profiles.

## 1. Exact local theorem

Use oriented orthonormal coordinates (s,z) centered at p=0. Let W=(W_s,W_z) and Omega be smooth on a full disk about0. Assume

 div W=4, Omega=-(partial_s W_z-partial_z W_s), W(0)=0, DW(0)=diag(0,4),

and every derivative of Omega vanishes at0. By the implicit function theorem W_z=0 is the graph z=k(s) near0, with k(0)=k'(0)=0. Define f(s)=W_s(s,k(s)). Assume f=0 on a negative interval and f(s)!=0 for every sufficiently small s>0. Its sign on the positive interval is immaterial. Let sigma be smooth, sigma(0)=sigma'(0)=0, and assume Omega=0 on the full open side O'={s>sigma(z)} in a neighborhood of0.

Then the following hold.

(a) There is no real analytic vector field V on a full neighborhood of0 agreeing with W on a measurable subset N of O' such that N has positive area in every disk about0.

(b) There are no epsilon,C,A>0 and no fixed unit vector e for which |partial_e^n W|<=C A^n(n!)^2 on O' intersect B_epsilon for all integers n>=0. Bounds on one sufficiently small tangent disk {s>L(s^2+z^2)} contained in O' already give a contradiction.

(c) For every unit vector e, every disk B about0 in the original domain and every A>0,

 sup_n sup_B |partial_e^n Omega|/[A^n(n!)^2]=infinity.

In particular neither U=W-2X+constant nor Omega can have Gevrey order in[1,2] on a full neighborhood of0. No result about Gevrey orders greater than2, all smooth fields, or temperature Gevrey bounds is asserted.

These hypotheses include the common endpoint jet assumptions. Saying that only three features of the basin and of the endpoint type enter does not discard these common assumptions: the additional features are the full harmonic side, its tangent graph, and the nonvanishing of f on a positive interval.

## 2. Proof of the local theorem

The div-curl identities give Delta W_s=Delta W_z=0 on O'. Hence W is real analytic there. Choose a small square Q such that |sigma(z)| is less than half its horizontal radius. The side O' intersect Q is connected, by horizontal segments to a vertical segment near the right edge. A real analytic scalar function vanishing on a positive-area subset of a connected open set vanishes everywhere on that set: on an interior rectangle with positive-area zeros, Fubini gives a positive-measure family of slices with positive-length zero sets; one-dimensional analytic uniqueness in each variable then gives zero on the rectangle and continuation gives zero on the connected domain. Apply this to the two components of V-W. Thus V=W on O' intersect Q. All derivatives agree at0 by smoothness and open equality.

The analytic nullcline V_z=0 is z=k_V(s). Its Taylor jet equals the jet of k, since the recursive implicit equations have the same coefficients and partial_z V_z(0)=4. The analytic function V_s(s,k_V(s)) consequently has the zero Taylor series of f. It is identically zero near0. For positive small s, k_V(s)=O(s^2) and sigma(k_V(s))=O(s^4)<s. Thus this nullcline lies in O', where V=W and uniqueness of the nullcline gives k_V=k. This implies f(s)=0 there, contradicting its assumed nonvanishing. The sign of f has not entered. This proves(a).

For(b), write w=s+iz, partial_bar=(partial_s+i partial_z)/2 and

 K=W_s-iW_z+4iz, S(w)=w-K(w)/2,
 Sstar(w)=conjugate(S(conjugate(w))), R(w)=conjugate(S(w)).

Direct differentiation gives partial_bar K=i Omega/2, partial_bar S=-i Omega/4 and W_s+iW_z=2(w-R(w)). Also S(w)=w+O(|w|^2). All maps are smooth on full neighborhoods. Put E(w)=Sstar(S(w))-w=R(R(w))-w.

Choose B,C so |S(w)-w|<=B|w|^2 and |sigma(z)|<=Cz^2. For sufficiently large M>B+4C the entire disk D_M={Re w>M|w|^2} is contained in O'. For w in D_M, |S(w)|<=2|w| and Re S(w)>(M-B)|w|^2>sigma(-Im S(w)); therefore S(D_M) lies in the reflected side Ostar. S and Sstar are holomorphic on their respective sides, so E is holomorphic on D_M. Taking M larger places every required point in an arbitrarily small prescribed neighborhood.

Since partial_bar S is flat at0, every homogeneous Taylor polynomial of S is holomorphic. The same is true of Sstar and E. On the negative zero arc w=s+ik(s), f=0, so R(w)=w and E=0. A first nonzero homogeneous term d_m w^m of E would restrict to d_m s^m+o(|s|^m), impossible. Thus E is smoothly flat at0. This uses finite Taylor expansions, not convergence of a formal series.

Let kappa(s)=s+ik(s), s>0. The velocity identity gives R(kappa)=kappa-f(s)/2. Since f=o(s) and k=O(s^2), the horizontal segment between these two points lies in O' for every sufficiently small s. When f<0, its real part is at least s; this is an even stronger inclusion, since its fixed imaginary part is k(s) and sigma(k(s))=O(s^4)<s. The fundamental theorem of calculus, with partial_s R=conjugate(S') on this segment, gives

 E(kappa(s))=-f(s)/2 [1+integral_0^1 conjugate(S'(kappa(s)-t f(s)/2))dt]
            =-f(s)(1+O(s)).

It is nonzero for small positive s of either sign of f. For fixed M these evaluation points lie in D_M, because M|kappa(s)|^2=O(s^2)<s.

Assume the directional bounds in(b). Holomorphicity gives partial_e^n K=(e_s+i e_z)^n K^(n), with a factor of absolute value1. Thus K,S and Sstar have uniform complex derivative bounds C_1 A_1^n(n!)^2 on the needed pieces. For holomorphic b,h, ordered Taylor compositions give

 |(b composed h)^(n)| <= C_b A_h^n(n!)^2 x(1+x)^(n-1), x=A_b C_h, n>=1,

provided |b^(j)|<=C_b A_b^j(j!)^2 and the analogous h bounds. Indeed after division by n!, the term of length k contains k! product j_i!, with j_i>=1 and sum j_i=n. This product is at most n!: transfer units to the largest entry, then use k!(n-k+1)!<=n!. There are binomial(n-1,k-1) ordered compositions. Summing gives the displayed estimate. Applying it to E proves uniform Gevrey2 derivative bounds on D_M. Only S bounds at D_M and R(D_M) enter; this follows from (Sstar)^(j)(S(w))=conjugate(S^(j)(R(w))).

Here is the critical uniqueness argument. If a holomorphic G on D_M is smoothly flat at0 and |G^(n)|<=C A^n(n!)^2, Taylor's integral remainder on the radial segment gives |G(w)|<=C A^n n! |w|^n. Choosing n=floor(1/(2A|w|)) and enlarging the constant on the remaining part of the disk yields |G(w)|<=C' exp(-c/|w|). The map zeta=1/w identifies D_M with Re zeta>M. Therefore P(zeta)=G(1/zeta) is holomorphic and |P(zeta)|<=C' exp(-c|zeta|) on that entire half-plane.

If P is nonzero, analytic uniqueness gives a real x0>M with P(x0)!=0. Set d=x0-M and g(u)=P(M+d(1+u)/(1-u)). The subharmonic mean inequality for log|g| on |u|<1 gives

 log|g(0)| <= log C' - c/(2pi) integral_-pi^pi |M+d(1+r exp(it))/(1-r exp(it))|dt.

For 1-r<=t<=1/4 and r sufficiently close to1, the integrand is at least d/(2t)-M. The integral tends to infinity; the remaining integrand is nonnegative. This contradicts g(0)!=0. Hence G=0. Apply this to E and contradict its nonzero values at kappa(s). This proves(b).

If the derivative bounds hold only on D_L={s>L|w|^2} contained in O', choose M>B+4L and sufficiently large for the preceding domains. Then D_M and R(D_M) are contained in D_L, since Re R(w)>(M-B)|w|^2>4L|w|^2>=L|R(w)|^2. The proof still applies. This does not establish a similar result from bounds only on a proper sector or an individual line.

For(c), suppose Omega has the asserted directional Gevrey2 bounds on a full disk. Choose a compact cutoff chi equal to1 near0 with Gevrey2 bounds in direction e. Such a cutoff is obtained by a product in the e and perpendicular coordinates: in the first, convolve an interval indicator with a normalized rescaling of exp(-1/(1-t^2)) on |t|<1, extended by0; use an arbitrary smooth cutoff in the second. To check the derivative bound for this bump, put d=1-|t| and take a complex disk of radius c0 d. On it the bump has absolute value at most exp(-c1/d). Cauchy's estimate is n!(c0 d)^(-n)exp(-c1/d)<=C_2^n(n!)^2; each fixed derivative tends to0 at the endpoints. Rescaling and convolution preserve the bound. Leibniz gives the same order for q=i chi Omega/2.

The Cauchy transform Tq(w)=pi^(-1) integral q(zeta)/(w-zeta)dA(zeta) has partial_bar Tq=q. This distributional kernel identity follows by integration by parts outside a disk of radius epsilon and the inner boundary integral as epsilon tends to0. Derivatives transfer to the compact smooth q: partial_e^n Tq=T(partial_e^n q). The kernel is locally integrable, and its absolute integral over a disk of radius R is2R after the factor1/pi. Hence Tq has the same directional bounds near0. K-Tq is holomorphic there and has ordinary Cauchy bounds on a smaller disk. Therefore K and W have directional Gevrey2 bounds there, contrary to(b). This proves(c). The affine difference between U and W preserves these local bounds. Since (n!)^s<=(n!)^2 for1<=s<=2, the lower-order corollaries follow.

## 3. Why the incoming hypothesis supplies a full side

In B2, reflection S(x,y)=(-x,y) conjugates the W flow and exchanges the endpoints of gamma. In positively oriented endpoint frames with outward tangent tau_minus=S tau_plus, the local coordinates transform(s,z) to(s,-z); the tangential reduced functions obey f_minus(s)=f_plus(s). It preserves the inward or outward direction of the exterior center drift, so one incoming endpoint implies that both are incoming, by the already checked4.7(iv) and(xiii)(d). Neither is accumulating. A finite cover using the regular interior and the nonvanishing exterior drifts therefore isolates all of gamma. The asymptotic W=2X+o(|X|) bounds the zero set, so global isolation of each remaining zero makes their number finite. This explicitly supplies the finiteness premise; the inference would fail from isolation only near one endpoint without the reflection hypothesis.

The global incoming-endpoint basin theorem is an explicit dependency: lead4.7(xiv)(a),(b), independently proved and audited in verifier P177 and P178. Its hypotheses include the global B2 equations and the endpoint setting of4.7(iii), an incoming endpoint, and isolation of EVERY zero of W off the zero arc gamma. It is not a theorem under only local isolation near p. It states that the exterior center orbit C_+ splits the side of the strong unstable curve C beyond p into two sectors. In a common sufficiently small disk each sector lies in an open backward basin of a zero off gamma. Each sector has Theta=L and Omega=0. The zeros for the two sectors can differ.

This yields the FULL side, not only two narrower wedges or a sequence of sectors. The sectors are precisely the two components of that side after removing C_+. Choose the smaller of their admissible disk radii. Their union is O' minus C_+. Continuity gives Theta=L and Omega=0 on C_+ as well, since every point of this curve sufficiently near p is approached by points in a sector. It gives the same values on the bounding curve C. Thus Omega=0 on all of O' near p. The side O' is exactly {s>sigma(z)} by the smooth strong unstable graph, whose tangent at p is the z axis. In particular sigma(0)=sigma'(0)=0. This graph property is the separately audited4.7(xiii) dependency.

For clarity, the vanishing of Omega in an open basin follows directly from transport. Theta is the constant Theta(q) there because backward orbits converge to q; it equals L because the sector accumulates at p. Therefore Theta_x=0 on the open invariant basin. Along a backward orbit, Omega(Y)=exp(-T)Omega(phi_-T(Y)), and boundedness near its limiting zero forces Omega(Y)=0. The full-side conclusion depends on the previously proved global finite-basin geometry. It cannot be inferred merely from the eigenvalues0,4 or from the sign of f.

The common endpoint theorem supplies W(0), DW(0), flatness of Omega, and f=0 on the negative interval. Incoming case(iv)(c) gives f<0 on a positive interval. All hypotheses of the local theorem are now present. Consequently(a) to(c) extend to these incoming endpoints. No outgoing area chart is used anywhere in this argument.

## 4. Version-specific scope

The candidate addition Y1 toY7 extends only(a),(b),(c). It explicitly does not extend(d), whose whole-fiber formula uses the outgoing chart of4.7(xviii)(a). It does not exclude general incoming endpoints with nonisolated zeros off gamma or accumulating endpoints. This says the stated endpoint hypotheses do not cover those cases, not that every auxiliary restriction on such profiles is compatible.

The v1 blanket sentence saying that(a) to(c) exclude no profiles without outgoing endpoints is inconsistent with this extension. Candidatev2 deletes it, and the requestedv3 retains that deletion. Version3 changes only heading reflow inY1 and the Y6 conjunction and punctuation before the separate nondegeneracy assumption; the mathematical statements and the other scope amendments are unchanged. The revised summary and Scope name both outgoing endpoints and incoming endpoints with the global isolation condition. The orders concern U or Omega near an endpoint, not only their analytic values inside the harmonic side. These are restricted exclusions. Neither the smooth beta2 branch nor the full B2 class is decided.

## 5. Dependencies and verification

P203 supplies an independently written proof of the outgoing version; the proof above rechecks the sign-sensitive steps and restates the complete(a) to(c) argument. P174/P175 supply the endpoint jet and strong unstable curve; P177/P178 supply the global incoming basin theorem. The current actual report entries are frozen and checked in verification/. No formal proof assistant source or build is claimed, and none is run. The numerical data in other packets play no role in this theorem.

Audit completed 2026-10-21T20:29:54.420600+00:00. Candidatev3 SHA256 8b4738719bea8792cd45334dc1dc52522890294be492758869dedff125ab449b.
