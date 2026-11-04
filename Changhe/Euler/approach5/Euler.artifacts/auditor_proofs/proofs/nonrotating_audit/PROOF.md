# Independent proof audit of the nonrotating Liouville theorem

## Exact result

Let `d=2` or `d=3`, `0<c<1/2`, and let `U,P` be `C^1` on `R^d`. Suppose

\[
 (1-c)U+(cy+U)\cdot\nabla U+\nabla P=0,
 \qquad \operatorname{div}U=0,
 \qquad |U(y)|=o(|y|)
\]

uniformly at infinity. Then `U` is spatially constant. If `U(y)->0`, then `U=0` and `P` is constant.

This is a theorem about the nonrotating equation. It confirms the stated scope of approach1's Theorem L2 and, at the lower `C^1` regularity, Theorem 1.1 of the Liu manuscript archived in the team records. It supplies no nonrotating-to-rotating reduction.

## Notation

Set `V=cy+U`, `A=DV`, `a=1-2c>0`, and let the antisymmetric matrix

\[
 W_{ij}=\partial_i U_j-\partial_j U_i
\]

represent the vorticity two-form. Thus `W=A^T-A`; this convention differs by a sign from some cross-product matrix conventions. Define

\[
 H=\tfrac12|V|^2+P-\tfrac12c(1-c)|y|^2,
 \qquad Z=\{V=0\}.
\]

The direct first-derivative identity is

\[
 \nabla H=-(aI-W)V,
 \qquad V\cdot\nabla H=-a|V|^2,                              \tag{1}
\]

and antisymmetry gives

\[
 a|V|\le |\nabla H|\le(a+\|W\|)|V|.                       \tag{2}
\]

## 1. Flow and backward limit sets

The linear-growth and radial arguments in the team records, section 6, apply with `omega=0`. They use only `C^1` regularity. The complete flow is denoted `Phi_s`. Every backward orbit is eventually confined to a fixed compact ball. Its alpha-limit set `K` is nonempty, compact, connected and fully invariant.

Along `z(t)=Phi_-t(y)`, identity (1) gives

\[
 \frac d{dt}H(z(t))=a|V(z(t))|^2.
\]

Since the trajectory is bounded, this increasing function has a finite limit `h`. Thus `H=h` on `K`; invariance and (1) imply `K subset Z`. The zero set itself is compact by the outward radial inequality. No pressure behavior at infinity is used.

## 2. Transport at precisely C^1 regularity

Let `alpha=U dot dy`. Differentiating a pulled-back one-form along the `C^1` flow, using the equation, gives

\[
 \mathcal L_V\alpha+a\alpha=d(\tfrac12|U|^2-P),
\]

and therefore

\[
 e^{as}\Phi_s^*\alpha
 =\alpha+d\int_0^s e^{a\sigma}
       (\tfrac12|U|^2-P)(\Phi_\sigma y)\,d\sigma.              \tag{3}
\]

All spatial first derivatives of the flow are continuous. The integral is `C^1` locally in its initial label, by differentiation under a finite-time integral. Taking the distributional exterior derivative is legitimate: a `C^1` map can be approximated locally in `C^1` by smooth maps; the classical pullback identity passes to the distributional limit. The resulting forms are continuous, so the identity is pointwise:

\[
 D\Phi_s(y)^T W(\Phi_s y)D\Phi_s(y)=e^{-as}W(y).              \tag{4}
\]

Consequently `W` is differentiable along each trajectory even though its spatial derivatives need not exist. Differentiating (4) gives

\[
 \frac d{ds}W(\Phi_s y)=-A^T W-WA-aW.                       \tag{5}
\]

This establishes the transport needed below without silently assuming `U in C^2`.

## 3. Equilibria without negative eigenvalues

At an equilibrium `p`, (5) gives

\[
 A(p)^T W(p)+W(p)A(p)+aW(p)=0.
\]

If every eigenvalue of `A(p)` has nonnegative real part, then

\[
 W(p)=e^{-at}e^{-tA(p)^T}W(p)e^{-tA(p)}.
\]

The matrix exponentials grow at most polynomially: this follows directly from real or complex Jordan form when the eigenvalues of `-A(p)` have nonpositive real part. The right side tends to zero. Hence `W(p)=0`, and `A(p)` is symmetric positive semidefinite because `W=A^T-A`.

More generally, suppose a backward limit set `K` consists entirely of such equilibria. Compactness and continuity imply

\[
 \operatorname{sym}A\ge -\tfrac a4 I
\]

on a neighborhood of `K`. The whole sufficiently late backward tail lies there. Taking the Frobenius product in (5),

\[
 \tfrac12\frac d{ds}|W|_F^2
 \le -(a+2\lambda_{\min}(\operatorname{sym}A))|W|_F^2
 \le -\tfrac a2|W|_F^2.                                    \tag{6}
\]

For a fixed endpoint `s_0` in this tail and `s<s_0`,

\[
 |W(\Phi_{s_0}y)|_F^2\le e^{-a(s_0-s)}|W(\Phi_sy)|_F^2.
\]

The last factor is bounded on the compact tail. Letting `s -> -infinity` proves `W(Phi_s0 y)=0`; (4) propagates this zero to `y`.

## 4. Backward convergence to an equilibrium with a negative eigenvalue has a null basin

Here is a direct local graph argument, so the proof does not depend on an imprecise invocation of center-stable manifolds.

At such an equilibrium, the reversed linearization `L=-A(p)` has a nonzero unstable subspace `E^u`. Split into real generalized eigenspaces `E^cs` and `E^u`, and use a direct-sum norm. Choose positive constants `epsilon<eta<beta` and `M` so that, for `t>=0`,

\[
 \|e^{tL_{cs}}\|\le M e^{\epsilon t},\qquad
 \|e^{-tL_u}\|\le M e^{-\beta t}.
\]

In a sufficiently small convex neighborhood, write the reversed field as `Lz+r(z)` after translating the equilibrium to zero. Because `Dr(0)=0`, the Lipschitz constant `delta` of `r` can be made arbitrarily small.

For the difference `w` of two forward reversed-flow trajectories remaining in this neighborhood forever, variation of constants in `E^cs`, and the terminal variation formula in `E^u`, give, with

\[
 D=\sup_{t\ge0}e^{-\eta t}|w(t)|,
\]

\[
 D\le M|w_{cs}(0)|
       +M\delta\big((\eta-\epsilon)^{-1}+(\beta-\eta)^{-1}\big)D.
\]

The terminal formula is valid because `w` is bounded and `e^{-tL_u}` decays. Choose `delta` so the last coefficient is at most one half. Then `D<=2M|w_cs(0)|`. In particular, projection of the trapped set to `E^cs` is injective with a Lipschitz inverse. This set lies in a Lipschitz graph of dimension at most `d-1` and is Lebesgue null. A coordinatewise Lipschitz extension, if needed, makes the graph over the full subspace.

For every equilibrium with a negative eigenvalue choose such an open neighborhood. Their union has a countable subcover because Euclidean space is second countable. Every backward orbit converging to one of these equilibria eventually remains in one selected neighborhood, and at some integer backward time belongs to its local null trapped set. The global basin is therefore contained in countably many forward images of null sets. Each finite-time `C^1` diffeomorphism preserves null sets, by local Lipschitz bounds on a countable compact covering. The basin is null.

Neither isolation of equilibria, uniform hyperbolicity, nor countability of the equilibrium set has been assumed.

## 5. A nonpoint backward limit set has rank at most d-2

Assume `K` contains more than one point. No point `p in K` can have `rank DV(p)=d`: the inverse function theorem would make it isolated in `K`, contrary to connectedness.

Suppose instead `rank DV(p)=d-1`. Select `d-1` components `G` of `V` with independent differentials. Complete these by one linear coordinate `tau`; the inverse function theorem supplies a `C^1` product chart `y=chi(tau,xi)` with

\[
 G(\chi(\tau,\xi))=\xi.
\]

All zeros of `V` in the chart lie on its axis `xi=0`. Shrink the chart so that some point of `K` lies outside its closure.

The set `K` contains a nondegenerate one-sided interval of the axis through `p`. To prove this, if both sides had missing points arbitrarily close to `p`, choose one missing endpoint on each side and a thin closed cylinder between them. Its lateral boundary contains no zero of `V`, and its cap centers are outside `K`; hence the entire boundary misses `K`. The portion of `K` inside would be nonempty, proper, relatively open and relatively closed, contradicting connectedness. Equivalently, absence of such endpoint pairs forces one entire side interval into `K`.

Choose an interior point `q` of this critical interval and a smaller product box around it. Its whole axis consists of zeros with `H=h`. The coordinate identity and `C^1` bounds give

\[
 |\xi|\le |V(\chi(\tau,\xi))|\le C_0|\xi|.
\]

Integrating `grad H` along the transverse coordinate segment, using (2) and bounded first derivatives of `chi`, gives

\[
 |H(\chi(\tau,\xi))-h|\le C_1|\xi|^2.
\]

Consequently, near `q`,

\[
 |H-h|^{1/2}\le C|\nabla H|,\qquad |\nabla H|\le M|V|.        \tag{7}
\]

These bounds use only `C^1` regularity. No Hessian, analyticity, or Morse-Bott theorem is required.

To finish the contradiction, put `e(t)=h-H(z(t))`. Where `e>0` and the orbit remains near `q`,

\[
 -\frac d{dt}\sqrt{e(t)}
 =\frac{a|V(z(t))|^2}{2\sqrt{e(t)}}
 \ge\frac a{2CM}|V(z(t))|.
\]

At a sufficiently late return close to `q`, both the distance to `q` and the resulting bound `(2CM/a)sqrt(e)` on the remaining path length are smaller than one quarter of the chosen ball radius. A first exit would require more length, so no exit occurs. The tail has finite length and converges. If `e` reaches zero at finite time, the tail is already stationary. Both cases contradict that `K` is nonpoint. Hence

\[
 \operatorname{rank}DV(p)\le d-2\quad(p\in K).                \tag{8}
\]

## 6. Finish in dimensions two and three

In dimension two, (8) would imply `DV=0` on `K`, contradicting `tr DV=2c>0`. Thus nonpoint limit sets cannot occur.

In dimension three, (8) and `tr DV=3c>0` imply rank one. A rank-one matrix with nonzero trace satisfies `A^2=(tr A)A` and has spectrum `{3c,0,0}`. Section 3 therefore shows that it is symmetric positive semidefinite on `K`. The estimate (6) then gives `W=0` along every trajectory with a nonpoint backward limit set.

For trajectories with a point backward limit, section 3 gives `W=0` unless the equilibrium has a negative-real-part eigenvalue. Section 4 puts all remaining trajectories in a null set. Thus `W=0` almost everywhere, and continuity makes it zero everywhere.

Curl and divergence imply `Delta U_i=0` in distributions. Weyl's lemma makes each component harmonic. For fixed `x`, the interior gradient estimate gives

\[
 |\nabla U_i(x)|\le \frac{C_d}{R}\sup_{B_R(x)}|U_i|=o(1)
 \quad(R\to\infty).
\]

Thus `U` is constant. The exact pressure for `U=b` is `P=-(1-c)b dot y+constant`; decay forces `b=0`.

## Adversarial checks and scope

- Pressure: only local first derivatives and values on compact trajectory sets are used. No harmonic-pressure normalization is imposed.
- Completeness: follows from uniform sublinearity and is proved before using negative infinite time.
- Connectedness: the cylinder argument uses connectedness, not local connectedness or path connectedness.
- Regularity: continuous vorticity transport is supplied by (3)-(5); the rank proof needs no second derivatives.
- Null basins: a countable cover of neighborhoods replaces any countability assumption on equilibria.
- Circularity: harmonic Liouville is used only after vorticity vanishes.
- Rotation: identity (1) fails in this form for `omega != 0`. The rank argument cannot be imported without another monotone function.
- Provenance: this is an independent mathematical audit, not machine verification and not a novelty or priority claim.
