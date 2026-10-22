# Finite separated representations at an outgoing endpoint

## Precise local statement

Use positively oriented orthonormal coordinates (s,z) centered at0. Let W be a C-infinity real vector field on a disk about0, with W(0)=0 and DW(0)=diag(0,4). Suppose its normal nullcline is the smooth graph z=k(s), with k(0)=k'(0)=0, and put f(s)=W_s(s,k(s)). Assume f(s)=0 for s<=0 and f(s)>0 for all sufficiently small s>0. Here W_s and W_z denote vector components, not derivatives. Let sigma be smooth with sigma(0)=sigma'(0)=0. On the open side O={s>sigma(z)} near0 assume

 div W=4, curl W=0.

For all sufficiently small eps, define

 S_eps={0<s<eps, |z|<eps, sigma(z)<s}.

There is no finite representation W(s,z)=sum_(j=1)^N a_j(s)B_j(z) on S_eps, where N is a positive integer, B_j are arbitrary real vector-valued functions of z, and a_j are arbitrary real functions of s on (0,eps). In particular the exclusion holds under the draft's stronger continuity and C1 assumptions on a_j. No assertion is made outside the specified fixed coordinates or for a general smooth W without such a representation.

The explicit 0<s condition is necessary for the syntax of the draft: its a_j are only defined on [0,eps), whereas sigma may take negative values, so sigma(z)<s<eps alone can include negative s. The proof uses only positive s. Replacing the draft's set by S_eps repairs it and does not weaken the contradiction. An assumption sigma>=0 is neither needed nor justified by the listed local hypotheses.

## Why the B2 outgoing endpoint supplies these hypotheses

For beta=2 the stationary temperature equation is W.grad Theta=0. The outgoing endpoint geometry established in the earlier local normal-form packet gives a smooth strong unstable curve C={s=sigma(z)}, tangent to the z-axis. The zero half-arc is {s<=0,z=k(s)}, and all sufficiently nearby points on the other side have backward orbits staying nearby and tending to the endpoint. The functions k,sigma vanish to order at least2 at0. For s<0,

 sigma(k(s))=O(s^4), hence s<sigma(k(s))

after decreasing the neighborhood: |O(s^4)|<|s|/2 suffices, regardless of its sign. The zero half-arc therefore lies on the negative side of C, and the basin side is {s>sigma(z)}. A sufficiently small disk is divided by the embedded graph C into these two components. Choosing eps smaller than the radius divided by3 places S_eps in that disk.

Write L=Theta(0). Transport and continuity along each backward orbit show Theta=L throughout this basin. On the basin, therefore, (W.grad+1)Omega=0. If Phi_t is the flow, then for t>0,

 Omega(q)=exp(-t)Omega(Phi_(-t)(q)).

The orbit tends to0 and Omega is continuous, so the right side tends to0. Thus Omega=0 there, and curl W=-Omega=0. Divergence is4. At the endpoint every vorticity derivative vanishes by continuity from this open basin, in particular Omega(0)=0. The null direction is tangent to the zero arc; divergence and zero curl give DW(0)=diag(0,4) in the stated coordinates. These facts depend on the actual outgoing basin classification, not merely on the eigenvalues0,4 at a zero. They are established for the B2 setting in the previously audited packet188.

A C1 field with div W=4 and curl W=0 is real analytic on O. An explicit proof in two dimensions is included next, so no elliptic regularity theorem is needed here.

## Finite rank gives a smooth analytic trace

Suppose a representation on S_eps exists and set a(s)=(a_1(s),...,a_N(s)). Let E be the finite-dimensional span in R^N of all a(s), 0<s<eps. If E={0}, W=0 on S_eps, contradicting div W=4 there. Choose s_1,...,s_m in (0,eps) whose vectors form a basis of E. Since sigma(0)=0 and min s_i>0, continuity gives delta>0 such that |z|<delta implies sigma(z)<min s_i. Decrease delta below eps. Each slice

 T_i(z)=W(s_i,z)=sum_j a_j(s_i)B_j(z)

is real analytic on (-delta,delta), because the slice is in O. For each s, write a(s)=sum_i c_i(s)a(s_i). Then the analytic vector function A_s(z)=sum_i c_i(s)T_i(z) equals W(s,z) whenever |z|<delta and sigma(z)<s. For every fixed s>0 this set includes an open interval about z=0.

The coefficients c_i need not have any assumed regularity. Instead reduce the T_i to a linearly independent basis T_1^*,...,T_d^* of their space of analytic vector functions on (-delta,delta). A finite collection of their derivatives at0 determines a member of this space uniquely. To prove this, let K_M be the subspace whose two component derivatives through order M vanish at0. The subspaces K_M decrease as M increases. If no K_M were zero, their nonnegative integer dimensions would eventually be constant and positive. The nested subspaces would then coincide from that index onward, yielding a nonzero analytic function with every derivative zero at0. Analyticity makes that function identically zero, a contradiction. Thus some finite M has K_M={0}. Select d scalar derivative-evaluation functionals of orders at most M for which the d by d evaluation matrix Q of the chosen basis is invertible.

Let j(s) be those d derivatives of the actual smooth field W(s,z) at z=0. Because A_s=W(s,.) near0 for s>0, the unique basis coefficients are b(s)=Q^-1 j(s). The function j extends smoothly to s=0 from the actual smooth W on its full disk. Hence b also extends smoothly to [0,eps). Define

 V(s,z)=sum_(i=1)^d b_i(s)T_i^*(z)

on [0,eps) times (-delta,delta). It is smooth in s, analytic in z, and equals W on S_eps intersect this half-rectangle. In particular V(0,z) is an analytic vector-valued function of z. This argument proves the announced stronger version with arbitrary a_j. 

## Analytic extension across the endpoint

For each fixed s in (0,eps), div V-4 and curl V are analytic functions of z. They vanish on the interval about0 where V=W in the open set O. The real analytic identity theorem therefore gives div V=4 and curl V=0 for all |z|<delta. Set w=s+i z and

 K(w)=V_s(s,z)-i V_z(s,z)+4 i z.

Its real and imaginary parts obey the Cauchy-Riemann equations: partial_s V_s=4-partial_z V_z and partial_z V_s=partial_s V_z. Since V is C1, K is holomorphic for s>0. The same calculation applied directly to W shows its real analyticity in O, as used above.

K is continuous up to s=0, and its trace F(z)=K(i z) is real analytic there. Complexify its convergent power series near0 to obtain a holomorphic F_c. Put G(w)=F_c(-i w), so G(i z)=F(z) for small real z. On a small half-disk, K-G is holomorphic and continuous up to the imaginary diameter, where it vanishes. Extend it by zero to the other half-disk. This is continuous. The integral around a triangle crossing the diameter is zero: cut the triangle a distance h from the diameter on each side, use Cauchy's theorem on each portion, and let h decrease to0. Uniform continuity bounds the errors on the short connecting pieces, and the integrals along the common cut cancel in the limit. Triangles wholly on either side also have zero integral. Morera's theorem therefore makes the extension holomorphic. It vanishes on an open half-disk, so it vanishes throughout. Thus K=G on the original half-disk.

Consequently

 W^an(s,z)=(Re G(s+i z), 4z-Im G(s+i z))

is real analytic across0, equals V for s>0 near0, and equals W on the positive-s part of O there. This last set is open and contains (s,0) for every sufficiently small s>0. Every derivative of W^an-W vanishes on that open set, and continuity of each derivative gives equality of all jets at0.

## Flatness contradicts the analytic continuation

The normal component of W^an has z-derivative4 at0. The analytic implicit function theorem supplies an analytic graph z=k_an(s), with k_an(0)=k_an'(0)=0, on which (W^an)_z=0. Define the analytic scalar f_an(s)=(W^an)_s(s,k_an(s)). The smooth and analytic normal equations have identical jets at0. Implicit differentiation at each order solves for the next derivative of their graph by dividing by the common nonzero z-derivative4, so the graph jets agree at every order. Composition then gives the same jets for f_an and f. Since f=0 on a negative interval, all its derivatives at0 vanish. Hence f_an is analytic and flat, so f_an=0 near0.

For s>0, k_an(s)=O(s^2) and sigma(k_an(s))=O(s^4)<s. Thus (s,k_an(s)) lies in the region where W=W^an. Its normal W component is zero; uniqueness of the smooth implicit graph gives k_an(s)=k(s). Its tangential component is therefore f(s)=f_an(s)=0, contradicting f(s)>0. This finishes the local exclusion.

## Polynomial and velocity cases

A vector polynomial in z of bounded degree is a finite separated sum, using the fixed functions z^j e_s and z^j e_z. This case is excluded even if the polynomial is required only on S_eps. At beta=2, W=2X+U-U(0). The position X is affine in the orthonormal coordinates (s,z), and a constant and the two coordinate-linear terms give finite separated sums. Therefore a finite separated representation of U would give one of W, and is excluded too. These are restrictions in fixed local Cartesian coordinates. They do not automatically apply to finite angular expansions about a different center, general compactified radial splines, or arbitrary smooth fields.

## Type of the area-chart equations

Separately, in the original physical Cartesian plane let X(a,r) be a smooth area-preserving chart with det(X_a,X_r)=1 and r!=0, satisfying the previously derived identity

 omega=4 partial_r(r X_a.X_r)-4r partial_a(|X_r|^2).

Here omega=Omega composed with X, rho=|X_r|>0, e=(cos phi,sin phi), e_perp=(-sin phi,cos phi), and alpha=(X_a.X_r)/rho^2. Since det(e_perp,e)=-1, the determinant condition gives exactly

 X_r=rho e, X_a=alpha rho e-rho^-1 e_perp.

Equating the e and e_perp components in X_ar=X_ra gives

 rho_a=rho alpha_r+alpha rho_r+rho^-1 phi_r,
 phi_a=alpha phi_r+rho^-3 rho_r.

Substitute X_a.X_r=alpha rho^2 and |X_r|^2=rho^2 in the curl identity, then use the first compatibility equation. This gives

 omega=4alpha rho^2-4r alpha_r rho^2-8r phi_r,
 alpha_r=alpha/r-2rho^-2 phi_r-omega/(4r rho^2).

Substitution back gives the final system

 rho_a=alpha rho_r-rho^-1 phi_r+alpha rho/r-omega/(4r rho),
 phi_a=alpha phi_r+rho^-3 rho_r,
 alpha_r=alpha/r-2rho^-2 phi_r-omega/(4r rho^2).

For fixed nonzero r the first two equations have principal r-matrix [[alpha,-rho^-1],[rho^-3,alpha]], whose eigenvalues are alpha plus or minus i rho^-2. Their 2 by2 real principal determinant is positive at every nonzero real covector. For the full three-variable system, the principal matrix at covector (xi,eta), dual to (a,r), is

 [[xi-alpha eta, rho^-1 eta, 0],[-rho^-3 eta,xi-alpha eta,0],[0,2rho^-2 eta,eta]].

Its determinant is eta[(xi-alpha eta)^2+rho^-4 eta^2]. It vanishes at the conormal (1,0) of C={a=0}. Thus the pair is elliptic, while the full system with the constraint is not an elliptic square system. The label "an elliptic system with a constraint" needs this distinction, which the displayed symbol supplies. The exact integral is omega(a,r)=(theta'(a)/4) integral_0^1 u^(-3/4) rho(a,ur) sin(phi(a,ur)) du, since the physical y component of X_r is rho sin(phi). For fixed prescribed theta, this contains no derivatives of rho,phi. Its linearization replaces the integrand by delta rho sin(phi)+rho cos(phi) delta phi, so it remains a zeroth-order integral in those two variables. Indeed the operator A g=(1/4) integral_0^1 u^(-3/4)g(ur)du has sup norm at most1 and satisfies (4r partial_r+1)A g=g for smooth g. This calculation does not replace the integral by a freely specifiable forcing. If theta is also unknown, theta' introduces a further derivative and the displayed three-variable symbol does not classify that enlarged system. At r=0 the undivided curl identity instead imposes alpha rho^2=omega/4; the formulas divided by r are not used there. Nothing here proves solvability, nonsolvability, well-posed evolution in a, or convergence of formal endpoint jets.

## Verdict and dependencies

The v1 K1 statement is REFUTED as written because of its undefined negative-s domain. K1-K3 of v2, which uses max(0,sigma(z))<s, are CONFIRMED, and the stronger arbitrary-coefficient variant is proved above. K4 is CONFIRMED when "contains the polynomial case" means it also excludes the earlier polynomial subclass; it does not assert that a side-only polynomial field satisfies the earlier full transverse-analyticity hypotheses. K5 is CONFIRMED for r!=0 with the distinction between the elliptic pair and the constrained full symbol. K6 is CONFIRMED subject to the same positive-s and coefficient-scope qualifications in all summaries. The report's count five requires the actual fifth consultation entry; its source is the frozen endlocal3 record.

Dependencies are the already audited outgoing basin geometry (packet188), elementary transport along complete local backward orbits, finite-dimensional linear algebra, the Cauchy-Riemann equations, the one-variable analytic identity theorem, Morera's theorem, the analytic implicit function theorem, and explicit chart differentiation. This is a restricted local obstruction, not a full B2 NO endpoint. It gives no numerical YES endpoint.

## Verification evidence

UTC 2026-10-21T19:24:02.579709+00:00. Lead candidate v2 SHA256 8f83b20ab28fe53d0574c979e40654ccf3a88b5d8ee2323d0146b34aa4eb8e39.

Verdict: K1-K6 of work/enter_xiid/text_v2.md are CONFIRMED within their stated local scope. The v1 negative-s representation domain was undefined for its a_j and was REFUTED as written; v2 uses max(0,sigma(z))<s and fixes it. The analytic trace is that of the auxiliary V, not an asserted value trace of W. This is approval of the inspected draft, not an uninspected later insertion.

Independent standalone proof: at a smooth outgoing endpoint, no finite separated representation sum a_j(s) B_j(z) exists on {0<s<eps, |z|<eps, sigma(z)<s} in the fixed orthonormal endpoint coordinates. The proof actually allows arbitrary a_j and B_j. Finite positive-s slices yield a finite-dimensional space of analytic transverse functions; finitely many component derivatives recover smooth reduced coefficients from the smooth W. Its analytic trace gives a holomorphic extension, whose analytic normal nullcline and flat tangential restriction contradict f(s)>0. This stronger version is available in PROOF.md; the lead's continuous/C1 version is valid without adopting the strengthening.

K2 side geometry follows from sigma(k(s))=O(s^4) and the actual outgoing basin property, as in188; mere eigenvalues0,4 are not enough. K3 polynomial W/U exclusions follow by adding the affine2X term. K4 comparison is an exclusion of the earlier polynomial subclass, not an implication of its full transverse-analyticity hypotheses. K5 independently gives X_a=alpha rho e-rho^-1 e_perp and the three displayed equations. The pair has speeds alpha plus/minus i rho^-2. The full determinant is eta[(xi-alpha eta)^2+rho^-4 eta^2], hence characteristic at the conormal da of C. For prescribed theta, omega=theta' A(rho sinphi) is a bounded zeroth-order integral; unknown theta and r=0 require the stated qualifications. K6 summaries have the regularity cross-reference and remain restricted. The five-consultation count is checked from the new endlocal3 question and the four previously frozen scope headers.

Controls: 58 exact symbolic checks, elapsed4.394704801s, PASS. They include independent physical-Cartesian curl through Jacobian inversion for three nonlinear area-preserving charts; rho/phi compatibility and the full principal determinant; analytic vectors whose independent jets first reach full rank at order11; exact recovery with arbitrarily cancelling coefficients; polynomial holomorphic trace signs; the integral ODE for both signs ofr; and concrete negative-s points in v1's set. Six rational chart samples accompany them. These are finite controls of the calculations; the analytic and finite-dimensional arguments are proved in PROOF.md. No NUM code was reused and no formal build was run.

The complete original proof was written19:16:37 before the controls and is retained with its original SHA256. Actual Opus371 and373/374 completed written reviews;372 supplied no audit text. The one incorrect follow-up caveat was rejected and withdrawn. B2 smooth beta2 and beta>2 branches remain OPEN. No decisive endpoint is authorized.
