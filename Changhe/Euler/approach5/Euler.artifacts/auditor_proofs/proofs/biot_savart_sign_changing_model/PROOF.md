# Sign-changing helicity with an independently prescribed carrier

Checked 2026-11-03T01:03:29Z. Verdicts A331-A335. The result below concerns a model with two different velocity fields. It is not an Euler solution.

## Statement, notation and dependencies

Fix 2/5<c<1/2 and any finite real omega. Write
\[
 a=1-2c>0,\qquad \kappa=1+c,\qquad d=3c,\qquad
 A=cI-\omega J,\qquad \gamma=1/c\in(2,5/2).
\]
The confirmed seed A243 supplies smooth fields B_0=Ay+U_0 and W_0 on R^3 such that U_0 is compactly supported,
\[
 \operatorname{div}U_0=\operatorname{div}W_0=0,\quad
 [B_0,W_0]=-\kappa W_0,\quad
 |D^jW_0(y)|\le C_j(1+|y|)^{-\gamma-j}.
\]
W_0 is nowhere zero. The complete backward carrier flow has a compact regular basic hyperbolic attractor K with basin V equal to the complement of a smooth proper line. The complete W_0 orbits in V are its global strong stable leaves; every point of V belongs to the strong stable leaf of a point of K. The seed and these geometric inputs were checked in the team records. Weak stable density for a periodic orbit and its use for continuous observables are the A267/A320 inputs, also explained below. They are dependencies, not new consequences of the Euler equation.

There is a compactly supported volume-preserving diffeomorphism f, equal to the identity near K, such that B=f_*B_0=Ay+U_1 and W=f_*W_0 retain every seed property. The field v=BS(W) is smooth, divergence free, has curl v=W, and satisfies
\[
 |v(y)|=O(|y|^{1-\gamma}),\qquad
 E_v(R):=\int_{|y|<R}|v|^2=O(R^{5-2\gamma}).
\]
There is a unique scalar H up to a constant with
\[
 a v+\nabla H=B\times W.
\]
It can be normalized by H(y) -> 0 as |y| -> infinity. With this normalization H=O(|y|^{2-gamma}) and H is nonconstant on V. The integrable helicity h=v.W has zero total integral and takes both strict signs on nonempty open subsets of V.

The actual velocity U_1=B-Ay differs from v. The model has an explicit nonzero Euler momentum residual and can fail the invariant-measure second-order identity. These failures, and the precise scalar pressure distinction, are part of the statement.

## 1. A local volume-preserving perturbation

Choose p in V outside K and a small ball with closure in V outside K. Since B_0 and W_0 are independent there, alpha_0=(B_0 cross W_0)^flat is nonzero at p. In positively oriented orthonormal coordinates about p arrange alpha_0(p)=q dx_1, q>0. Let chi be a smooth cutoff equal to one near p, supported in the ball, and set
\[
 Z=\operatorname{curl}(0,0,\chi x_2^3/6).
\]
Z is smooth, divergence free and compactly supported. Near p it equals (x_2^2/2,0,0), so Z(p)=0, DZ(p)=0 and Delta Z(p)=e_1. Its time-epsilon flow f is a complete volume-preserving diffeomorphism and
\[
 f(p)=p,\quad Df(p)=I,\quad D^2f(p)=\varepsilon D^2Z(p)
\]
exactly, by the first and second variational equations at its fixed point p.

Push both fields forward. Divergence and bracket are natural under this volume-preserving change; completeness, basin structure and strong stable leaves follow by conjugacy. The fields are unchanged near K and outside the support. Hence U_1 is compactly supported and divergence free and all exterior estimates persist.

The correct contraction order is
\[
 \alpha=(B\times W)^\flat=i_Wi_B\,dy_1\wedge dy_2\wedge dy_3
          =(f^{-1})^*\alpha_0.
\]
Differentiate the pullback at p. Since Df(p)=I and D^2f^{-1}(p)=-D^2f(p),
\[
 \operatorname{div}(B\times W)(p)
 =\operatorname{div}(B_0\times W_0)(p)
   -\sum_i(\alpha_0)_i(p)\Delta f^i(p)
 =\operatorname{div}(B_0\times W_0)(p)-\varepsilon q.
\]
Choose a sufficiently small epsilon avoiding the one forbidden value. The resulting divergence is nonzero. This is an exact affine formula in epsilon, stronger than the first-order version in B's summary.

## 2. Reconstruction, pressure potential and estimates

Define the Newton potential and Biot-Savart field by
\[
 \mathcal A(y)=\frac1{4\pi}\int\frac{W(z)}{|y-z|}\,dz,
 \qquad
 v(y)=\frac1{4\pi}\int\frac{W(z)\times(y-z)}{|y-z|^3}\,dz.
\]
Local singularities are integrable. The Newton integral at infinity converges because gamma>2; the Biot-Savart integral converges there already for gamma>1. Distributional differentiation, a cutoff integration by parts using div W=0, and local elliptic regularity give
\[
 -\Delta\mathcal A=W,\quad \operatorname{div}\mathcal A=0,
 \quad v=\operatorname{curl}\mathcal A,\quad
 \operatorname{div}v=0,\quad\operatorname{curl}v=W.
\]
For example, the integration-by-parts error for div A has size O(R^{1-gamma}) and vanishes. All fields are smooth locally.

For |y|=r large, split the v integral into |z|<r/2, |z-y|<r/2, the remaining region with |z|<=2r, and |z|>2r. The respective bounds are
\[
 Cr^{-2}\int_0^{r/2}(1+s)^{-\gamma}s^2ds,
 \quad Cr^{-\gamma}\int_0^{r/2}ds,
 \quad Cr^{1-\gamma},\quad C\int_{2r}^\infty s^{-\gamma}ds.
\]
Each is O(r^{1-gamma}), since 1<gamma<3. Squaring and integrating in r proves E_v(R)=O(R^{5-2gamma}); the exponent is strictly between zero and one.

The bracket and divergences give
\[
 \operatorname{curl}(B\times W)
 =-[B,W]-dW=(\kappa-d)W=aW.
\]
Thus B cross W-a v is globally curl free. Simple connectivity provides smooth H. Its Laplacian at p is the nonzero divergence obtained in Section 1, so H is nonconstant on V. Since B=O(r), its gradient is O(r^{1-gamma}). Integrating along rays shows that each ray has a finite limiting H. The oscillation on the sphere of radius r is at most C r^{2-gamma}, by a connecting great circle; hence all ray limits coincide. Subtract the common limit. Radial integration now gives |H(y)|<=C|y|^{2-gamma}, uniformly in direction.

## 3. Helicity nonvanishing and its two signs

Suppose h=v.W vanishes on V. Then WH=-a h=0, so H is constant on every complete strong stable leaf. Pick a periodic orbit of K, with backward period T. On the weak stable set of that orbit, H composed with Psi_T equals H: corresponding points at times zero and T lie on the same strong stable leaf after choosing the periodic-orbit phase. For a transitive locally maximal hyperbolic basic set, that weak stable trace is dense in K, by local product structure and transitivity (the A267 input). Continuity extends H composed with Psi_T=H to K. Every point of V is strongly stable to some point of K; leafwise constancy extends this equality to V.

Let Phi be the forward B flow. Choose R_0 containing the support of U_1. Outside this ball, r'=cr, since the rotation is skew. Any orbit leaving the ball escapes to infinity. The measurable set E of nonescaping points stays in the ball for all positive times, while
\[
 |\Phi_tE|=e^{dt}|E|\le |B_{R_0}|.
\]
Thus E has zero volume. Carrier invariance and invertibility turn the periodicity above into H(Phi_{nT}y)=H(y) on V. For almost every y in V the left side tends to zero by escape and the uniform decay of H. Hence H=0 almost everywhere on the open set V, then everywhere there by continuity. This contradicts Delta H(p) != 0. Therefore h is nonzero somewhere in V.

The bound h=O(r^{1-2gamma}) is integrable because gamma>2. Also
\[
 \operatorname{div}(HW)=-a h,\qquad
 \int_{|y|=R}|HW\cdot n|\,dS\le C R^{4-2\gamma}\longrightarrow0.
\]
The divergence theorem gives integral h=0. V has full volume, since its complement is a smooth proper line, so integral_V h=0. A continuous integrable function with zero integral, nonzero at an interior point, cannot have only one sign. Its positive and negative subsets in V are open and nonempty.

## 4. The precise missing velocity and pressure relations

Set D=U_1-v and q_v=|v|^2/2. The scalar consequences of the model Lamb identity use
\[
 g=v\cdot B=-BH/a,\qquad h=v\cdot W=-WH/a,
 \qquad R=H-g.
\]
These satisfy the reduced commutator identity and
\[
 2a h+\operatorname{div}(hB+RW)=0.
\]
Here R is an independent scalar coefficient. If one defines the pressure naturally associated to the actual field v by the displayed Lamb potential,
\[
 P_*=H-q_v-(Ay)\cdot v,
\]
then the physical coefficient is different:
\[
 (P_*-q_v)-R=v\cdot D.                                      \tag{4.1}
\]
Outside the support of U_1 this difference equals -|v|^2 and is not identically zero. Thus the model does not retain the scalar helicity identity with the physical coefficient P_*-q_v merely by retaining the abstract identity with R=H-g. Its physical-coefficient divergence residual is W(v.D). No claim that this last function is everywhere nonzero is needed.

For the Euler profile equation of v, the momentum residual is exactly
\[
 (1-c)v+(Ay+v)\cdot\nabla v+\omega Jv+\nabla P_*
 =a v+\nabla H-(Ay+v)\times W=D\times W.                    \tag{4.2}
\]
Its curl is -[D,W], since div D=div W=0. Equivalently the reconstruction residual
\[
 (aI+[W]_\times)v-(Ay\times W-\nabla H)=D\times W
\]
is the same vector. Certainly U_1 != v: curl U_1 is zero outside a compact set whereas curl v=W is nowhere zero there.

These facts confirm the obstruction for the explicitly listed weaker premises: bracket, divergences, basin geometry, Lamb identity with an independently prescribed B, curl v=W, and the subcritical energy bound. They do not claim that every scalar or pressure-based argument fails. Identifying the carrier velocity U_1 with v, together with the other displayed identities, would yield the Euler equation. Prescribing canonical pressure alone is not proved equivalent to that full vector compatibility.

## 5. The momentum residual cannot vanish accidentally

Because B=Ay outside a compact set, the exterior bracket yields
\[
 W(e^{tA}y)=e^{-t}e^{-\omega Jt}W(y).
\]
Extend this exterior field by rotating dilations to all nonzero radii, obtaining W_h. It is nonzero, has rotating homogeneity -gamma, and is locally integrable at zero since gamma<3. It is distributionally divergence free: its ordinary spherical flux is constant by divergence freedom in annuli and also scales as R^{2-gamma}, so it is zero; subtracting the test function's value at zero leaves an inner boundary error O(R^{3-gamma}).

Let v_h=BS(W_h) on punctured space. The same inversion argument gives curl v_h=W_h, div v_h=0 and rotating homogeneity -beta, beta=gamma-1 in (1,3/2). It is nonzero. Since W-W_h is compactly supported and integrable, v-v_h=O(r^{-2}). If (4.2) vanished throughout the exterior, then v cross W=0 there; along rotating dilations to infinity, this would imply v_h cross curl v_h=0 on punctured space.

The stress T=v_h tensor v_h-|v_h|^2 I/2 would therefore have div T=0. Define the finite spherical integrals
\[
 P_r=\int_{S^2}|v_h\cdot n|^2,\qquad
 P_t=\int_{S^2}|v_h-(v_h\cdot n)n|^2.
\]
Integrate div(Ty)=tr T=-|v_h|^2/2 on an annulus. Rotating homogeneity preserves the spherical integrals and gives
\[
 (3-2\beta)(P_r-P_t)=-(P_r+P_t),
 \quad\text{hence}\quad
 (2-\beta)P_r+(\beta-1)P_t=0.
\]
Both coefficients are positive, forcing v_h=0, a contradiction. This proves that the Euler reconstruction residual is genuinely nonzero somewhere, for every finite omega.

## 6. Second-order invariant-measure failure and the endpoint

Keep B fixed and replace (W,v,H) by s(W,v,H), with s>0. All model properties, geometry and both helicity signs persist. Let mu be the fixed regular-attractor invariant probability, let n=W/|W|, and write
\[
 \ell=n\cdot S_v n,\qquad b=S_vn-\ell n.
\]
Under the scaling, n stays fixed, ell and b are multiplied by s, and
\[
 P_s=sH-s^2q_v-s(Ay)\cdot v.
\]
Its Hessian is O(s) uniformly on compact K. The exact Euler identity A119/B Lemma 6.5 would require
\[
 \int (s^2|b|^2-n\cdot D^2P_sn)\,d\mu
 =2+\int(s\ell-1)^2\,d\mu.
\]
The left side is O(s); the right side is 3+O(s). They differ for all sufficiently small positive s. The necessary Euler mean stretching integral s ell=1 fails as well. This is an explicit failure, not a missing verification.

At c=2/5 the same tail calculation has beta=3/2. The nonzero spherical norm of v_h contributes C dR/R to the energy, with C>0. The cross term with v-v_h=O(R^{-2}) and the square error are integrable in R. Thus
\[
 E_v(R)=C\log R+O(1).
\]
This model does not satisfy the bounded-energy estimate at that endpoint.

## 7. Scope of the accompanying occupation discussion

Section 5 of B's revised note is explicitly analysis rather than a theorem. Absolute continuity of unstable conditionals by itself does not give a uniform density bound after smearing. On a compact regular support, the additional uniform angle and plaque bounds and the exact alpha-length densities can supply it; the complete argument is separately under focused review in the team records. For potentially singular supports from A308 only the separately proved L1 smearing argument is presently available.

A Ledrappier-Young conditional-measure dimension does not by itself identify the Hausdorff dimension of every leaf intersection, nor does either dimension give an eventual occupation estimate proportional to S^{a/kappa} along individual orbits. One needs return statistics or a separate argument. A325 already refutes such a polynomial inference from abstract conservativity alone, without refuting a geometry-specific estimate.

The comparison of the proposed powers, if they hold with the required lower and upper bounds, has contradiction threshold a/kappa>1/3, equivalently c<2/7. The exponent arithmetic is valid. A compatible formal tail is not proof that an actual Euler solution attains an upper bound. A287/A288 also contain convergence and limiting-coefficient information beyond merely restating the L2 bound. Consequently neither the pointwise occupation claim nor the claim of exhaustion of all scalar methods is certified.

## 8. Direct check of the local cylindrical example

This additional exact example from B's Section 3(f) is independent of the preceding model. On the domain r>0, choose 0<c<1/2, omega != 0, b != 0 and R>0. In cylindrical coordinates set
\[
 U_r=-r/2+aR^2/(2r),\quad U_\theta=b(r-R^2/r),\quad U_z=z,
\]
\[
 H=\bigl(b(b-\omega)+a/4\bigr)r^2
 -(2b^2+a^2/2)R^2\log(r/R)-a z^2/2,
 \qquad P=H-|U|^2/2-(Ay)\cdot U.
\]
Then div U=-1+1=0 and Omega=2b e_z. The carrier components are
\[
 B_r=-\frac a{2r}(r^2-R^2),\quad
 B_\theta=(b-\omega)r-bR^2/r,\quad B_z=\kappa z.
\]
Direct differentiation gives
\[
 aU_r+H_r=2bB_\theta,\quad
 aU_\theta=-2bB_r,\quad aU_z+H_z=0,
\]
so aU+grad H=B cross Omega and the exact Euler profile equation holds with the displayed single-valued pressure.

The circle r=R,z=0 has forward angular speed -omega and period T=2 pi/|omega|. If q=r^2-R^2, then q'=-a q and z'=kappa z in forward carrier time. Hence its forward transverse multipliers are e^{-aT}, e^{kappa T}; its backward multipliers are e^{aT}, e^{-kappa T}. The source's listed pair is the backward pair and must be labeled as such. The orbit is a saddle in either time direction. Finally h=2b z has both signs near it. The example is singular on the axis and nondecaying, so it supplies only this local compatibility test, not a global counterexample.

## Verification scope

The full B27 proof, the revised note and the second-order identity excerpt were read. Section 1's perturbation, Sections 2-6's estimates and residuals, and Section 8's cylindrical equations were checked directly without computation. Existing A243 and A267 inputs remain explicit dependencies. Source hashes and retained copies are in the team records; the only copy transformation replaces an absolute shared-root prefix by a relative prefix. The source's last sentence about unavailable model consultation describes its subreview, not this campaign: the Theory Agent B parent records its own checked construction and is configured as model. Collaboration here uses those existing files and the audit feedback. No additional model was invoked.
