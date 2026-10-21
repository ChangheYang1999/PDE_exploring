# Audit of the norm, counterexamples, and radius

**Verdicts.** The sufficiency of the weaker anchored tail norm, failure of bare \(C^2\) tail control, origin threshold, and radius formula are **CONFIRMED**. An identification of the monomial and polynomial remainder norms is **REFUTED**. The advertised simple radii are **CONFIRMED in both norms**, using the original constants for the former and the repaired constants for the latter.

## Hypotheses and dependencies

Let \(A>2\), \(\beta=2/A\), \(e>0\), and use the compatible trace functional \(B\) and differential from `../01-differential/PROOF.md`. References in the counterexamples are smooth through both endpoints. The local estimates and constants come from `../02-remainder/PROOF.md`; their uniform margins are \(\sigma>b_+\) and \(\theta+b_->1\).

Denote by \(N_{\rm mon}\) the norm using \(R_{\rm mon}=v-\sum c_ju^j\) and by \(N_\phi\) the norm using \(R_\phi=v-\sum c_j\phi_j\). Both use the same three coefficients, the same tail supremum, and the same anchored tail seminorm.

## 1. The norm discrepancy is substantive

The original `01-differential` uses \(R_\phi\) in its jet decomposition, correctly. The original `02-remainder`, equation (12), explicitly defines its norm with \(R_{\rm mon}\). Its numerical certificate estimates \(z,D_z,J_z\) from the three monomials, and therefore uses \(N_{\rm mon}\). The report switches to \(R_\phi\) when stating the same constants.

For an explicit distinction take \(v=\phi_3=u^3-4u^9+3u^{11}\), \(r=1/2,\sigma=1\). Then \(R_\phi=0\), whereas
\[
u^{-6}R_{\rm mon}''=-288u+330u^3.
\]
This expression is decreasing and negative on \((0,1/2]\), so its absolute supremum is \(102.75\). Every other term in the two norms agrees. Consequently
\[
N_{\rm mon}(\phi_3)=N_\phi(\phi_3)+102.75. \tag{N1}
\]
They are not the same norm.

More generally at these \(r,\sigma\), the corresponding weighted polynomial corrections for \(j=3,5,7\) have suprema \(102.75,80.5,58.25\). Thus
\[
N_{\rm mon}(v)\le N_\phi(v)+102.75\sum|c_j|\le103.75N_\phi(v),
\]
\[
N_\phi(v)\le103.75N_{\rm mon}(v). \tag{N2}
\]
This already gives a conservative way to translate a radius, but it would lose a factor \(103.75\). The direct repair in (R11) avoids that loss. It is therefore incorrect to attribute the original unchanged constants to the report's norm; it is also incorrect to infer from this discrepancy that the simple exclusion radii must fail. No counterexample to those radii is furnished by (N1).

## 2. Why the full tail Hölder norm is not necessary

The origin zeroth and first derivative bounds follow from the weighted second derivative bound by (R1). For a fixed remainder convention, this is an equivalent simplification of those origin terms of the earlier \(X\)-norm, not a reduction of their essential weight.

On the tail, every estimate in the preceding proof uses only \(S(v'')\) and comparisons of \(v''(u)\) with \(v''(1)\). A full two-point Hölder seminorm is genuinely stronger. For example, for \(s=1-u\) prescribe
\[
v''(1-s)=s^\theta\sin(s^{-p}),\quad p>0.
\]
Integrating twice from 1 gives a \(C^2\) function with \(v(1)=v'(1)=0\). Multiplying \(v\) by a cutoff equal to one near 1 and zero near 0 makes a compatible direction; in the cutoff region the function is smooth. The anchored bound is finite. Choose two nearby phases differing by \(\pi\): their separation is comparable to \(s^{p+1}\), while the second derivative difference has size comparable to \(s^\theta\). The two-point Hölder quotient has size comparable to \(s^{-p\theta}\), which diverges. This proves strict weakening.

The modulus generalization is also correct. For increasing continuous \(\omega(s)\to0\), require
\[
L_\omega=\sup_{0<s\le\ell}s/\omega(s)<\infty,\qquad
I_\omega=\int_0^\ell\omega(s)s^{b_--2}\,ds<\infty.
\]
Replace the anchored denominator by \(\omega(s)\), replace \(\ell^{1-\theta}\) by \(L_\omega\), the averaging factor \(1/(1+\theta)\) by 1, and \(I_t\) by \(I_\omega\). These substitutions follow respectively from \(s\le L_\omega\omega(s)\), \(\omega(ts)\le\omega(s)\), and the actual tail integral. The product seminorm inequality is unchanged.

For instance \(\omega(s)=s^{1-b_-}/\log(e/s)^2\) satisfies both conditions. Its reciprocal logarithmic integral is finite, while it permits larger deviations than every power \(s^\theta\) with \(\theta>1-b_-\) near zero. Thus the claim of a sufficient weaker family is justified; a uniquely weakest norm is not established or needed.

## 3. Bare \(C^2\) tail control: equation (30)

Choose \(0<\gamma\le1-\beta\), and prescribe near the source
\[
v''(1-s)=s^\gamma.
\]
Integrate from 1 and cut off away from the source as above. This is a compatible \(C^2\) direction, zero near the origin. Its small real multiples preserve trace negativity and the simple source.

Consider \(w_t=w_0+tv\) and its reconstructed \(g_t\), with \(g_{t*}=g_t(1)>0\). The removable quotients obey
\[
\delta j=\frac{s^\gamma}{1+\gamma},\qquad
\delta a=-\frac{s^{1+\gamma}}{(1+\gamma)(2+\gamma)}.
\]
The relative variation of \(g_t(1-s)/g_{t*}\) from the reference endpoint expansion begins at order \(s^{1+\gamma}\). Expanding \(Q_t\) about the endpoint therefore gives the leading nonsmooth term
\[
Q_t(1-s)-Q_t(1)
=t\left[\frac1{2A(1+\gamma)g_{t*}^2}
-\frac e{2g_{t*}^3}\right]s^\gamma+o(s^\gamma). \tag{N3}
\]
Terms inherited from the smooth reference are \(O(s)=o(s^\gamma)\), since \(\gamma<1\). At first order in \(t\), this is exactly (30). The coefficient at \(t=0\) can vanish for at most one \(\gamma\); choose another \(\gamma\) in the nonempty interval \((0,1-\beta]\). Continuity of \(g_{t*}\) keeps it nonzero for sufficiently small nonzero \(t\).

Because \(K_t\) is a positive constant times \(s^{\beta-2}(1+o(1))\), the integral diverges like
\(\int_0 s^{\gamma+\beta-2}\,ds\). This is a divergence of the nonlinear functional for actual nearby compatible traces, not just a formal divergence of one term of a differential.

## 4. Smooth-through-source directions: equation (30a)

To keep each direction smooth through 1, take \(\varphi\ge0\), smooth and supported in \((1,2)\), and set
\[
v_\epsilon''(1-s)=\varphi(s/\epsilon)
\]
near 1. Integrate from 1 and apply a fixed remote cutoff to \(v_\epsilon\). The resulting directions have bounded \(C^2\) norm, zero origin jets, and smooth endpoints.

The leading singular terms in \(D_wB\), before multiplication by its nonzero reference prefactor, are
\[
\int_0^{s_0}s^{\beta-2}
\left[\frac1{2Ag_*^2s}\int_0^s\varphi(t/\epsilon)\,dt
-\frac e{2g_*^3}\varphi(s/\epsilon)\right]ds.
\]
Fubini gives
\[
\int_t^{s_0}s^{\beta-3}\,ds
=\frac{t^{\beta-2}-s_0^{\beta-2}}{2-\beta}.
\]
Thus the leading coefficient is
\[
\left[\frac1{2Ag_*^2(2-\beta)}-\frac e{2g_*^3}\right]
\epsilon^{\beta-1}\int_1^2\varphi(t)t^{\beta-2}\,dt. \tag{N4}
\]
The prefactor omitted here is exactly
\(\kappa A^{\beta-2}g_*^{1-\beta}\).

The remainder estimates can be made explicit. For \(s\gtrsim\epsilon\),
\(\delta j=O(\epsilon/s)\), \(\delta a=O(\epsilon)\). The endpoint-subtracted reconstruction satisfies
\[
|\eta(1-s)-\eta(1)|
\le C\epsilon[1+\log_+(s/\epsilon)].
\]
It is zero for \(s<\epsilon\), before any remote cutoff contribution. Integrating this against \(s^{\beta-2}\) gives \(O(\epsilon^\beta)\); integrating the \(O(\epsilon)\) quotient errors from \(s=\epsilon\) gives the same order. Smooth reference coefficient errors insert an additional factor of \(s\). Remote-cutoff terms and terms with the global constant \(\eta(1)\) contribute at most \(O(\epsilon|\log\epsilon|)\) after endpoint cancellation. All are \(o(\epsilon^{\beta-1})\).

Hence the derivative is unbounded on this bounded \(C^2\) family whenever
\[
e\ne g_*/[A(2-\beta)].
\]
This is the original (30a), and holds at both rational references. At the exceptional equality the preceding smooth-bump leading coefficient cancels; the argument does not claim otherwise. The nonlinear counterexample in section 3 still applies by choosing \(\gamma\) away from its cancellation.

## 5. Origin weight: equation (31)

At the origin \(g=u^2(1+O(u^2))\), \(w=-Au(1+O(u^2))\), and \(K=A^{\beta-2}u^{-\beta}(1+O(u^2))\). The most singular term of the differential before integration by parts is
\[
-\frac{\kappa e A^{\beta-2}}2u^{-6-\beta}v''
=\frac{e(1-\beta)}{6A}u^{-6-\beta}v''.
\]
For directions compactly supported in \((0,1)\), two integrations by parts give
\[
\lambda(u)\sim
\frac{e(1-\beta)(6+\beta)(7+\beta)}{6A}\,u^{-8-\beta}. \tag{N5}
\]
The terms containing \(a_v/(2g^2)\), \(vQ/w\), and the adjoint reconstruction yield at most order \(u^{-6-\beta}\) after transferring derivatives to the weight. They cannot cancel the displayed leading term. Its coefficient is positive because \(e>0\) and \(0<\beta<1\).

For nonnegative nonzero \(\phi\in C_c^\infty((1,2))\), set \(v_t(u)=t^{7+\beta}\phi(u/t)\). The pairing with (N5) tends to a positive constant, whereas its weighted second derivative norm has size \(O(t^{\beta-\sigma})\); its jets and tail terms vanish. For \(\sigma<\beta\) this norm tends to zero, so the derivative cannot be bounded.

At \(\sigma=\beta\), choose disjoint geometrically separated bump supports with scales tending to zero, all far inside the origin interval. Each response is eventually positive and bounded below. Finite sums of the bumps have uniformly bounded weighted supremum norm, while their derivative responses grow with the number of bumps. Each finite sum is smooth and identically zero near zero. This proves failure at the critical unmodified supremum weight. Both arguments apply to \(N_{\rm mon}\) and \(N_\phi\), because all their jets vanish.

## 6. Radius formula (32)

Let \(0<b_0\le|B(A_0,e_0,w_0)|\), let \(D_A,D_e\) bound the reference parameter derivatives, and use the constants from the preceding proof in one fixed norm convention. Put
\[
P=D_Ah+D_eh'+\tfrac12K_{AA}h^2+K_{Ae}hh',\qquad
m=b_0/2-P,
\]
\[
D=D_N+K_{Av}h+K_{ev}h'.
\]
The differential and (27) imply
\[
|B-B_0|\le P+Dt+R_{vv}t^2.
\]
If \(m>0\) and
\[
\epsilon=\min\{\delta_0,m/[2(D+R_{vv}\delta_0)]\},
\]
then for the closed ball \(t\le\epsilon\),
\[
|B-B_0|\le P+m/2=b_0/2-m/2<b_0/2\le|B_0|/2.
\]
This proves the exact strict inequality claimed in (32). If \(m\le0\), this particular budget gives no positive radius. A single large isotropic \(C_2\) can erase the positive budget at the prescribed parameter widths; retaining the anisotropic constants is legitimately necessary for these numerical certificates.

## 7. Reference bounds behind the arithmetic

The scalar arithmetic does not certify its own analytic inputs. We checked those inputs as follows, for \(w_0=-A_0u(1-u^2)/(1+u^2)\), \(g_0=u^2/(1+u^2)\), \(r=1/2\).

At the origin,
\[
z_0=\frac{1-u^2}{1+u^2},\quad
D_0=-\frac{4u^2}{(1+u^2)^2},\quad
J_0=-\frac{4(3-u^2)}{(1+u^2)^3},\quad E_0=-\log(1-u^2).
\]
Absolute power series at \(R=r^2=1/4\) give
\[
Z,n\le(1+R)/(1-R),\quad
D\le4R/(1-R)^2,\quad J\le4(3+R)/(1-R)^3,\quad
E_o\le R/(1-R).
\]
Every omitted power has degree at least six, so these series sums really bound the weighted algebra norm, including its remainder.

On the tail \(a_0/A_0=u(1+u)/(1+u^2)\) is increasing, since its derivative has numerator \(1+2u-u^2>0\). This gives the claimed \(a_*\). Bounding that numerator by 2 gives the claimed \(H_a\). The function \(k_0=2/[u(1+u^2)]\) is decreasing; its derivative magnitude \(2(1+3u^2)/[u^2(1+u^2)^2]\) is decreasing, giving the claimed \(K_0,H_k\).

The formula
\[
w_0''=4A_0u(3-u^2)/(1+u^2)^3
\]
is positive and decreasing for \(u\ge1/2\), because its derivative has numerator \(1-6u^2+u^4<0\). The positive derivative majorant uses \((1+6t+t^2)/(1+t)^4\), whose derivative numerator is \(2-16t-2t^2<0\) for \(t\ge1/4\). These give the displayed \(S_w,H_w\). The functions \(g_0^{-p}=(1+u^2)^p/u^{2p}\) and their derivative magnitudes decrease, giving the displayed \(S_p,H_p\). A derivative supremum bounds an anchored \(\theta\)-seminorm because \(s^{1-\theta}\le1\).

The reference weight is
\[
u^{-b}(1+u)^{b-2}(1+u^2)
=\frac{1+u^2}{(1+u)^2}(1+1/u)^b.
\]
Both factors decrease in \(u\le1\), and the second increases in \(b\). Bounding \(b\le1\) at \(u=r\) gives the certificate's \(W_0\le(1+r^2)/(r(1+r))\). All these are bounds on suprema, not sampled assertions.

For the parameter slice the exact finite-part identity is
\[
B_0=(5/(6A)-5e)I_3+(1/(2A)+e)I_2,\qquad
I_n=\mathrm B(n-\beta/2,\beta).
\]
It follows by the stated integration by parts and beta recurrence; all removed powers are nonintegral and no zero-endpoint constant remains. Direct substitution gives \(Q=(1-6Ae)u^{-5}+(1+2Ae)u^{-3}\), checking the starting expression and signs.

To check that finite-part step explicitly, let
\[
F(u)=u^{1-\beta}(1-u^2)^{\beta-1}.
\]
Then
\[
F'=(1-\beta)u^{-\beta}(1-u^2)^{\beta-2}(1+u^2),
\qquad \kappa K=-F'/(3A).
\]
Integration by parts therefore gives \(B_0=(3A)^{-1}\operatorname{FP}\int_0^1Q'F\). At 1 its discarded product is \(O(s^\beta)\); at zero it has no constant term. Substitution \(t=u^2\) produces the beta finite parts with first arguments \(-2-\beta/2\) and \(-1-\beta/2\). The recurrence
\[
\mathrm B(x+n,\beta)=\mathrm B(x,\beta)
\prod_{k=0}^{n-1}\frac{x+k}{x+\beta+k}
\]
follows by integrating a derivative, with the same cutoff convention. For \(x=-m-\beta/2\), \(n=2m+1\), the product is \(-1\): reflect its indices \(j=-m,\ldots,m\). There are no zero factors. Taking \(m=2,1\) converts the two negative-argument finite parts to \(-I_3,-I_2\) and yields the claimed coefficients.

Let \(b_l=2/A_+\), \(b_h=2/A_-\), \(p=n-1-b_h/2>0\). Differentiating the convergent beta integral inserts
\(\log(1-t)-\frac12\log t\). Its absolute first moment is bounded by
\[
b_l^{-2}+(p+1)^{-2}+(b_l+1)^{-1}.
\]
The first term is the full \(-\log(1-t)\) moment. For the \(-\frac12\log t\) moment, split at \(1/2\): bound \((1-t)^{b_l-1}\le2\) on the first half and \(-\log t\le2(1-t)\) on the second, then extend the elementary integrals to \((0,1)\). Squaring with
\((|a|+|b|/2)^2\le2a^2+b^2/2\) gives exactly
\[
4b_l^{-3}+2(p+1)^{-3}+2(b_l+2)^{-1}
\]
for the second moment. The zero moment is at most \(b_l^{-1}\). The product and chain rules then give the original code's \(D_A,D_e,K_{AA},K_{Ae}\); absolute extrema of the affine-in-\(e\), monotone-in-\(A\) prefactors are attained at rectangle corners.

Finally
\[
B_0=\frac{16-\beta}{3A(4+\beta)}
\mathrm B(2-\beta/2,\beta)(1-S_Ae),\quad
S_A=\frac{6A(4A-3)}{8A-1}.
\]
At both references \(1-S_Ae>0\). Since \(t^{1-\beta/2}\ge t\), the beta factor is at least \(1/[\beta(1+\beta)]\). This proves the positive rational lower bound \(b_0\), independently of decimal quadrature.

These checks validate the original certificate in \(N_{\rm mon}\). Substituting the three bounds (R11) validates the repaired certificate in \(N_\phi\). The exact output, including the strict budget comparison for each simple radius, is stored alongside the preceding proof.

## Scope

Neither the large upper bound for the dual norm nor three numerical directional tests locate the optimal norm accurately. Large bump responses are compatible with a bounded derivative because their weighted origin norms are also large. Sampled bump norms and numerical lower tests remain numerical evidence; they should not be relabeled as certified estimates by this audit.
