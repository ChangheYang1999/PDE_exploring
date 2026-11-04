# Exact spherical Poisson defect of the independent-carrier reconstruction

Checked 2026-11-03T01:04:59Z. A336-A338. This is a diagnostic of a specified model, not a universal nonexistence theorem.

## 1. Exact flux theorem

Let 1<beta<2 and let v be a nonzero real C2 divergence-free field on R3 minus the origin. Suppose that for every R>0 a rotation Q_R satisfies
\[
 v(RQ_R\theta)=R^{-\beta}Q_Rv(\theta)\quad(\theta\in S^2).
\]
No assumption at the origin is made. Set
\[
 P_r=\int_{S^2}|v\cdot n|^2,\quad
 P_t=\int_{S^2}(|v|^2-|v\cdot n|^2),\quad
 C_\beta=(2-\beta)P_r+(\beta-1)P_t>0.
\]
Then, with W=curl v,
\[
 \int_{|y|=R}(v\times W)\cdot n\,dS=-C_\beta R^{1-2\beta},       \tag{1}
\]
\[
 \int_{|y|=R}\operatorname{div}(v\times W)\,dS
       =(2\beta-1)C_\beta R^{-2\beta}>0.                       \tag{2}
\]
In particular div(v cross curl v)=0 is impossible in this class. This scalar premise is weaker than the force-free premise v cross curl v=0 used by the earlier annular stress argument.

### Proof

Rotations preserve spherical measure and radial components. Consequently the radius-R integrals of |v.n|2 and of its tangential squared magnitude are P_r R^{2-2beta} and P_t R^{2-2beta}. With q=|v|2/2 and T=v tensor v,
\[
 v\times\operatorname{curl}v=\nabla q-\operatorname{div}T.
\]
Differentiate the spherical average written on the unit sphere, using C2 regularity:
\[
 \int_{|y|=R}\nabla q\cdot n\,dS
 =R^2\frac{d}{dR}\int_{S^2}q(R\theta)\,d\theta
 =-\beta(P_r+P_t)R^{1-2\beta}.                                \tag{3}
\]
This uses averaged homogeneity, not a false pointwise radial derivative of a rotating profile.

Since Dn=(I-n tensor n)/R,
\[
 \operatorname{div}(Tn)=(\operatorname{div}T)\cdot n+T:Dn.
\]
Integrating this identity on an annulus and differentiating its outer radius yields
\[
 \int_{|y|=R}(\operatorname{div}T)\cdot n\,dS
 =\frac{d}{dR}\int_{|y|=R}|v\cdot n|^2dS
    -R^{-1}\int_{|y|=R}(|v|^2-|v\cdot n|^2)dS
 =\bigl((2-2\beta)P_r-P_t\bigr)R^{1-2\beta}.                  \tag{4}
\]
Subtracting (4) from (3) proves (1). The divergence theorem on annuli and a second outer-radius derivative give (2). Both coefficients in C_beta are positive; nonzero v has positive P_r+P_t by the rotating law, so C_beta>0. All integrations avoid the origin.

## 2. Application to the regular model and its compact coordinate perturbations

Let 2/5<c<1/2, omega be any finite real number, A=cI-omega J, a=1-2c, and beta=1/c-1 in (1,3/2). Use the A243 seed or the A331 compactly perturbed model:
\[
 B=Ay+U_1,\quad \operatorname{div}U_1=\operatorname{div}W=0,
 \quad[B,W]=-(1+c)W,
\]
where U_1 is compactly supported and W is nowhere zero, smooth and decays with derivatives as |y|^{-1/c}. Let v=BS(W), and choose the global potential
\[
 a v+\nabla H=B\times W.
\]
Define the Lamb-derived pressure
\[
 P_*=H-|v|^2/2-(Ay)\cdot v,
\]
and its scalar Poisson defect
\[
 D_P=-\Delta P_*-\sum_{i,j}(\partial_i v_j)(\partial_jv_i).
\]
There is a nonzero rotating-homogeneous leading field v_h of degree -beta, with W=curl v_h in the exterior, and
\[
 v-v_h=O(R^{-2}),\qquad D(v-v_h)=O(R^{-3}).                    \tag{5}
\]
These are the directly verified Newton/Biot-Savart estimates in A245 and A331. Extend exterior W by rotating dilations; its degree -(beta+1) is locally integrable at zero, its distributional divergence is zero by the zero spherical flux, and its Biot-Savart inverse is v_h. The compact integrable difference of the two vorticities gives (5). The available zero-mean improvement is unnecessary.

Then for all sufficiently large R,
\[
 \int_{|y|=R}D_P\,dS
 =(2\beta-1)C_\beta R^{-2\beta}+O(R^{-\beta-2})>0,             \tag{6}
\]
with C_beta formed from v_h as above. In particular P_* fails the actual Euler pressure Poisson equation in the exterior, and a pressure constant cannot repair it.

### Proof

A332 gives the exact vector residual
\[
 E=(1-c)v+(Ay+v)\cdot\nabla v+\omega Jv+\nabla P_*
   =(U_1-v)\times W.
\]
Taking divergence, div v=0 removes the dilation and zeroth-order terms; the -omega J part of A cancels the divergence of omega Jv. Thus
\[
 \operatorname{div}E=\sum_{i,j}(\partial_i v_j)(\partial_jv_i)+\Delta P_*.
\]
In the exterior U_1=0, so this is exactly
\[
 D_P=\operatorname{div}(v\times W).                           \tag{7}
\]
From (5), W=O(R^{-beta-1}) and DW=O(R^{-beta-2}), the difference between the right side of (7) and div(v_h cross curl v_h) is O(R^{-beta-4}). Integration over the sphere gives O(R^{-beta-2}). Formula (2) proves (6); its leading term dominates because beta<2.

## 3. Preservation of the stronger any-pressure obstruction

A245 proves the following construction-specific statement: the Biot-Savart velocity V of its marked regular pair cannot be an Euler profile at any nonzero real amplitude, for any pressure. Its proof uses the complete bracket flows, positive constant carrier divergence, backward boundedness, ambient vortex recurrence, a proper exceptional vortex line with full complementary basin, a transitive compact attractor, and a compact characteristic leaf on the boundary of a trapping neighborhood. These are the exact abstract hypotheses in the team records.

Every one is preserved by B27's compact volume-preserving diffeomorphism. Completeness, recurrence, the bracket, the exceptional line, basin and transitive orbit are preserved by conjugacy. Volume preservation keeps both divergences and ambient null sets. The image of the compact trapping neighborhood remains trapping, and the image of its characteristic leaf remains a compact characteristic leaf. Compact support of the diffeomorphism preserves backward boundedness and the exterior rotating field.

For clarity, the final A245 deduction also applies directly. If lambda v, lambda != 0, were an Euler profile with any pressure, its vorticity equation, minus the B,W bracket, would give
\[
 [\lambda v-U_1,W]=0.
\]
The two fields have zero divergence, so their cross product is globally curl free and equals grad F for a smooth F. It is orthogonal to W, hence WF=0. Exterior decay gives grad F=O(R^{1-2/c}); radial integration and shrinking spherical oscillation normalize F to zero at infinity. The A245 decaying-first-integral theorem gives F=0. Thus v cross W=0 in the exterior, and the homogeneous leading field satisfies v_h cross curl v_h=0. Formula (1), or the earlier annular stress argument, contradicts this. No pressure can repair any nonzero amplitude of this particular compactly conjugated model.

This stronger result is an application of the explicit A245 topological hypotheses. It does not follow from the scalar defect (6) alone and does not extend to arbitrary decaying Euler profiles, arbitrary independent fields, or arbitrary changes of carrier and vorticity.

## Verification evidence

The entire LIT72 proof and the entire earlier A245 proof were read. The spherical derivatives, signs of both rotation terms and error orders were derived independently. The exact LIT72 input and its hash are in the team records. The application relies on A243/A245/A331/A332, while the flux theorem in Section 1 is independent of their topological construction. No numerical computation or new model client was used.
