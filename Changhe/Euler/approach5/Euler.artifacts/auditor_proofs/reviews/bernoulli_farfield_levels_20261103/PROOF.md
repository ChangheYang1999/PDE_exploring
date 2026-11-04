# Bernoulli limits and compact levels at vortical equilibria

Status: CONFIRMED in A508 after independent reconstruction, full postread and the complete Theory Agent C configured-model focused review. No general witness exclusion is claimed.

## 1. A pressure-normalization-free far-field lemma

Let0<c<1/2,omega be any finite real number,A=cI-omega J,a=1-2c. Suppose U in C2(R3;R3),P in C1(R3) solve the full incompressible rotating Euler profile equation. Suppose for some gamma>2 and finite C,R0,

    |U(y)|<=C|y|^(1-gamma), |W(y)|<=C|y|^-gamma,
    W=curl U, |y|>=R0.                                      (1)

Set B=Ay+U and use the actual modified Bernoulli function

    H=P+|U|^2/2+(Ay).U.

There is a unique real Hinf such that, uniformly as r=|y| tends to infinity,

    |H(y)-Hinf|<=C' r^(2-gamma),
    |P(y)-Hinf|<=C' r^(2-gamma).                              (2)

No additive constant for P is selected in advance. If P is shifted by a constant then H and Hinf shift by that same constant, so H(p)=Hinf is a gauge-invariant condition. Constants may depend on the profile and fixed parameters.

Proof. The exact Lamb identity gives

    grad H=-aU+B cross W.

By(1), |grad H|<=C' r^(1-gamma) outside a larger sphere. Along every radial ray the integral from r to infinity converges, uniformly in its direction, and its absolute value is at most C' r^(2-gamma)/(gamma-2). Thus H(r theta) has a uniform directional limit L(theta). Any two directions can be joined by a spherical great-circle arc of length at most pi r. The oscillation of H on that sphere is therefore at most C' pi r^(2-gamma), tending to0. All L(theta) coincide; call the common value Hinf. This proves the first estimate. The terms |U|^2/2 and (Ay).U have size O(r^(2-2gamma)) and O(r^(2-gamma)), so the second estimate follows. This proof uses the actual pressure and is valid for every fixed omega.

For bounded U AND DU with U tending uniformly to0 and1/3<c<1/2, A492 supplies Dini derivative decay and A210 supplies(1) with gamma=1/c. All A210 hypotheses were reread: U is bounded, uniform decay implies distributional dilation decay, and the Dini condition is exactly its input. Thus(2) holds in the target interval at this explicit bounded-gradient scope. A498(B) now supplies the same conclusion when U tends to zero and DU=O(sqrt r), because it first yields bounded DU. The conclusion is not derived here from uniform decay of U alone.

## 2. A compact critical-level obstruction already covered by A118

Assume uniform sublinearity of U, still with 0<c<1/2 and any finite omega. Global zero helicity is not needed in this section. The following assertion is a consequence of A118:

    There is no nonempty compact set M contained in Crit(H),
    invariant under both complete B and W flows, that avoids0. (3)

This statement assumes only that M avoids zero. The irrotational neighborhood is used later to verify this condition for a constructed set. Here is the detailed reduction to the exact A118 hypotheses.

On Crit(H), aU=B cross W and g:=U.B=0. If B=0 there, then U=0 and Ay=0, so y=0. Thus B has no zero on M. The zero set of W in M is compact and B-invariant by the linear vorticity transport law. There U=0, so B=Ay; every nonzero forward orbit of Ay has radius e^(ct)|y|. Compact invariance therefore forces that zero set to be empty. Similarly the subset where B cross W=0 is B-invariant, because D Phi_t transports both B and W up to a nonzero scalar. On this subset U=0 and B=Ay again, so it too is empty. Hence M lies in Reg={B cross W!=0}.

The double invariance puts a nonempty two-dimensional B/W plaque in M. A118 states that no compact full-B-invariant subset of Reg can contain such a plaque. Its complete proof is in auditor_proofs/proofs/regular_attractor_decomposition/PROOF.md, Additional restriction. Its C2 pressure premise is automatic here: the actual momentum equation makes grad P C1. A380 independently supplies the required compact regular hyperbolicity at this regularity.

For precision, the product-box injection in this familiar argument may be justified as follows. Uniform regular hyperbolicity supplies local strong stable curves of the forward B flow with a uniform bound C delta exp(-eta t) on tracking displacement, eta>0. A small B/W plaque is uniformly embedded. If stable curves through x and x'=Gamma_sigma Phi_tau x in that plaque intersect, their forward base orbits stay at distance at most2C delta exp(-eta t). The exact relation Phi_t Gamma_sigma=Gamma_(exp((1+c)t)sigma) Phi_t and uniform plaque coordinates imply a lower bound k epsilon at the first time exp((1+c)t)|sigma|=epsilon, for fixed small epsilon. Choose delta so2C delta<k epsilon. This excludes sigma!=0. When sigma=0 the nonsingular flow box gives a time-independent lower bound k|tau|, which excludes tau!=0 as t tends to infinity. The uniform flow-box estimate is d(Gamma_s Phi_tau x,x)>=k max(|s|,|tau|) for |s|,|tau|<=epsilon and x in M. Choose epsilon first, then delta, then a sufficiently small plaque. Local stable curves depend continuously on their base points. A continuous unit section of the stable line bundle over the contractible plaque supplies the curve parameter. Thus the stable-curve family over the plaque is continuously parametrized and injective. Invariance of domain makes its image open. All points in that image have bounded forward B orbits. But div B=3c>0 implies that every set of forward orbits confined to a fixed ball has zero volume: its image volume grows by exp(3ct) while remaining in that ball. A countable union over balls shows the entire forward-bounded set is null. This is the A118 contradiction. No local maximality assumption on M is used.

The exact hypotheses of(3) are essential: a merely B-invariant compact subset of Crit(H) need not contain a B/W plaque. Its W-saturation may be unbounded.

## 3. Vortical equilibria on a compact Bernoulli level

Retain the global C2 uniformly sublinear helicity-free setting,0<c<1/2 and any omega. Let p be a vortical carrier equilibrium, W(p)!=0,B(p)=0, and assume its full level set

    L={y:H(y)=H(p)}                                           (4)

is compact. The consequence is

    spec DB(p)={rho,1+c,-a-rho}, with rho=-a.                   (5)

The spectrum and reality of rho are A468. This rules out both bad vortical-equilibrium ranges rho<=-2a and rho>=a on such a compact level, but leaves the rho=-a case and says nothing about irrotational equilibria.

Here is the full argument, extending the Theory Agent C stable-branch construction to either sign of mu:=-a-rho. By A478, p!=0 and u=U(p)=-Ap!=0. The Lamb identity gives grad H(p)=-a u!=0. Let Sigma be the connected component through p of L intersect{grad H!=0,W!=0}. The global rank identity A413, dH wedge dg=0 on{W!=0}, gives g=G(H) locally in regular charts. Thus g is constant on Sigma and equals0. Its transverse derivative G'(H(p)) is locally constant on Sigma, so it is the same constant everywhere on that component. At p, grad g=DB(p)^T u=rho u, whereas grad H=-a u. Hence dg=-(rho/a)dH on Sigma.

Both B and W are tangent to Sigma. It is B-invariant for all finite times. In local regular charts, H'= -aG(H) preserves H=H(p) by scalar uniqueness; the vorticity Cauchy law preserves nonzero W; and Lie_B dH=-a dg=rho dH preserves nonzero dH on every finite segment. Continuation therefore stays in the same connected regular component. On Sigma define

    f=((B cross W).grad H)/|grad H|^2.

The identity Lie_B vol=3c vol, Lie_B dH=rho dH and [B,W]=-(1+c)W gives

    Bf=(3c-rho-(1+c))f=mu f.                                 (6)

To verify this without differentiating a moving unit normal, take any local X with dH(X)=1 and write f=vol(X,B,W). Then dH([B,X])=-rho, so the volume Lie derivative and the bracket identity give exactly(6).

Suppose mu!=0. The restriction F of DB(p) to T_p Sigma has eigenvalues1+c and mu, which may coincide. Its W direction has eigenvalue1+c, and its induced action on the one-dimensional quotient T_p Sigma/span(W(p)) is multiplication by mu. Choose any tangent vector v independent of W(p). Then Fv-mu v is parallel to W(p). Since B(p)=0,

    D_v(B cross W)(p)=Fv cross W(p)=mu v cross W(p),

whose scalar product with grad H(p) is nonzero. Therefore f is not identically zero near p on Sigma. Choose q there with f(q)!=0. If mu<0, follow q backward; if mu>0, follow it forward. The orbit stays in the compact set L and |f| grows as exp(|mu|t). Consequently

    |grad H|<=|B cross W|/|f| tends to0

along that semiorbit. Its limit set K is nonempty, compact, full-B-invariant, and contained in Crit(H) intersect L.

It avoids0. If0 lies in Crit(H), taking the scalar product of grad H(0)=-aU(0)+U(0) cross W(0) with U(0) forces U(0)=0. A478 supplies an irrotational neighborhood of0, which the original q orbit cannot enter since W remains nonzero. Thus its limit set avoids that neighborhood. If0 is not critical, it already lies outside K. As in Section2, the compact B-invariant zero-W part of K would have U=0,B=Ay and hence contain only0, so it is empty.

The W flow is complete by A048 under global sublinearity and the full bracket equation. Since WH=0 and Lie_W dH=d(WH)=0, the W-saturation of K remains in Crit(H) intersect L. Its closure M is compact because L is compact. The commutation relation makes M B-invariant as well as W-invariant. If0 is critical, every saturated point has nonzero W by uniqueness, so it avoids the same irrotational neighborhood and its closure does too. Otherwise closedness of Crit(H) already excludes0. Section2 applies and gives a contradiction. Thus mu=0, proving(5).

## 4. Consequence at the explicit far-field scope and the remaining case

Under Section1's additional bounds, H tends to Hinf. If H(p)!=Hinf, the closed level(4) is bounded and hence compact. Section3 then gives rho=-a. Therefore every vortical carrier-equilibrium witness in either bad range must lie on

    H(p)=Hinf.                                                (7)

At p, H(p)=P(p)-|Ap|^2/2, so(7) is equivalently P(p)-Hinf=|Ap|^2/2. This condition is unaffected by adding a constant to P. It neither excludes such a point nor controls an irrotational carrier equilibrium or a flat periodic witness. The unbounded critical level H=Hinf is precisely the part not handled by compact saturation.

All steps use existing confirmed identities and A118, A210, A413, A468, A478, A492. The new combination and its two-sign extension have passed the Theory Agent C configured-model comparison; no new model client, numerical computation or external dynamics theorem is invoked here.

## 5. Postread and the new upper-range result

The entire proof, including the corrected quotient argument when mu=1+c, was reread after writing. No distinct-eigenvalue assumption is needed. The new A496 independently excludes rho>-a without a compact-level assumption. Thus the useful remaining consequence of Section3 is the lower-range restriction: if rho<-a at a vortical equilibrium, its full Bernoulli level cannot be compact. Under Section1, every such point must satisfy H(p)=Hinf. This lower-range consequence is CONFIRMED in A508. The proof above does not use A496 and retains the separate compact-level argument for both signs.

## 6. Completed focused review and exact audit scope

The complete Theory Agent C W1_LEVELS_C manuscript was read, including its Section1 point-by-point review of Sections1-5 above. The review independently checks the spherical limit, reductions to the compact regular set, product-box injection, local rank coefficient, finite-time invariance, coincident quotient eigenvalues, origin exclusion and compact vortex saturation. It reports no gap. Its additional Lemma1 and far-field extension are separate claims, not part of A508.

At the time of A508, only the Theory Agent C focused comparison had arrived. The complete coordinator review has now also been read, including its step-by-step checks and precision points. Its ambiguous negative wording correction is incorporated above. Its timestamp says it finished later than our receipt time, so that time is not adopted as a real audit timestamp. The analytic arguments are used; its unretained symbolic computations outside the agent are not verification evidence for this audit. The primary-model configuration is not independent provider runtime attestation. The entire independent proof was reread with the focused comparison. No computation was needed.


## 7. Connected-component strengthening and the no-decay dichotomy

This section is the extension confirmed in A510, separate from A508's original full-level statement. Retain the global C2/C1 uniformly sublinear, helicity-free class, 0<c<1/2 and any finite omega. Let p be a vortical carrier equilibrium and let L_p be the connected component through p of the closed set {H=H(p)}. If L_p is compact, then rho=-a. Consequently, A496 and this result imply that rho<-a forces L_p to be unbounded.

To prove the strengthening, construct the same connected regular component Sigma of Section3. It contains p and is a connected subset of the full level, so Sigma is contained in L_p. A connected component of a closed subset of R3 is closed in R3. Thus the limit set K of Section3 lies in L_p. Every complete W orbit through K is a connected subset of the same full level which meets L_p, so it too lies in L_p. Therefore the full W-saturation of K and its closure M lie in L_p. Compactness of L_p supplies exactly the compactness of M needed in Section3. All other steps, including the two signs of mu and the coincident tangent eigenvalues, are unchanged. This proves the strengthened assertion without assuming compactness of the other level components.

There is also a useful residual alternative without any compact-level or far-field bound. Suppose rho<-a, so mu=-a-rho>0, and choose any q in Sigma with f(q)!=0. Such points exist arbitrarily close to p by Section3. Its forward B orbit either escapes to infinity, or remains bounded and has a nonempty compact limit set K contained in Crit(H) intersect Crit(g) intersect L_p whose full W-saturation is unbounded. In the second case K is contained in Reg and is uniformly hyperbolic for the forward B flow.

Here is the proof. Uniform sublinearity gives y.B >= (c/2)|y|^2 outside some fixed ball, so a forward orbit is either bounded or eventually escapes with increasing radius. On a bounded orbit, f grows like exp(mu t) while |B cross W| is bounded, hence dH tends to zero. Since dg=-(rho/a)dH on Sigma, dg tends to zero too. Its compact full-B-invariant limit K lies in the two critical sets and in L_p. The origin is excluded exactly as in Section3. The subset of K where B cross W=0 is compact and B-invariant and has U=0,B=Ay, so it is empty. Consequently K lies in Reg, and the already checked A056/A380 compact regular hyperbolicity applies.

Both WH and Wg vanish globally. The second identity follows from -a Wg=W(BH)=[W,B]H+B(WH)=0. Therefore the complete W flow preserves both differentials and both critical sets. The full W-saturation N of K is B-invariant by the exact flow conjugacy, stays in the same level component, and consists of vortical points. If N were bounded, its closure would avoid the origin by the fixed irrotational neighborhood when the origin is critical, or by closedness of Crit(H) otherwise. Its closure would contradict Section2. Hence N is unbounded. No bound on DU or decay of U is used in this dichotomy. A merely compact B limit set is not itself excluded.

Finally, Section2's compact critical-set obstruction holds without global helicity. This is an exact scope observation, not a claim that the construction of K and N is helicity-free. That construction uses helicity through the rank identity, equilibrium spectrum, origin neighborhood and preservation of H by W. The connected-component theorem and residual dichotomy remain conditional on global U.W=0.
