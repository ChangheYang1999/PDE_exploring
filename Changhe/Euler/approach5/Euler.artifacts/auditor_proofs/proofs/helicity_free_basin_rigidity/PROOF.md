# Conditional rigidity from helicity-free basin geometry

## 1. Statements

Let 0<c<1/2, omega be finite and real, A=cI-omega J, B=Ay+U, W=curl U, a=1-2c and kappa=1+c. Let U in C2(R3;R3), P in C1 solve the divergence-free rotating profile equation, and set

    H=P+|U|^2/2+(Ay).U, O={W!=0}.

The following two sufficient sets of additional assumptions are distinct.

(A) Assume U tends to zero. Let the basins V_A of the regular basic hyperbolic backward attractors from A115 cover almost every point of O. Assume U.W=0 on every V_A and that, for each attractor A and each x in A, its complete strong stable leaf meets A densely. Then U=0. No implication from mixing to the stated leaf-density hypothesis is included in this theorem.

(B) Assume U in C3, uniform sublinearity, U.W=0 everywhere, and O dense in R3. Then a global function K exists with

    dK=(BH)dH, BK=(BH)^2.

In particular BH vanishes on every compact invariant-probability support and tends to zero along every backward B orbit. Every given vortical full-flow-ergodic SRB probability with the positive unstable densities specified in A207/A223 has H constant on its entire open essential basin domain. If these domains cover almost every point of O, no such profile exists: the profile must be constant, contradicting the density of O. Under decay the resulting rigidity conclusion is U=0.

Part (B) asserts no SRB existence or coverage theorem at C3. Its global rank hypothesis is obtained using dense O; it is not inferred merely from rank on an arbitrary basin.

## 2. Part (A)

The exact Lamb identity is

    a U+grad H=B cross W.

Thus WH=-a U.W=0 on every V_A. The complete strong stable leaves through A are its vortex lines, and V_A is the union of those complete lines by A115 and the verified vortex completeness argument. Consequently H is constant on each such line. Choose x in A. Its line meets A densely, so continuity makes H equal to H(x) throughout A. Every line through A then has this same H value, and hence H is constant on V_A. The constant may depend on A.

The covering assumption and continuity give grad H=0 on O. The localization theorem A265-A266 then makes U constant, and decay gives U=0. If O is empty, the same conclusion follows immediately from harmonic Liouville and decay. This proves part (A). Neither dense weak stable leaves nor transitivity alone substitutes for the strong stable density assumed here.

## 3. The abstract global rank argument

Suppose more generally B is complete C2, all its backward orbits are precompact, H is C3, G=BH and dG wedge dH=0 on R3. The C1 one-form G dH is closed and hence exact on R3. An explicit primitive is

    K(y)=integral_0^1 G(t y) grad H(t y).y dt.

Differentiation using the closedness identity gives dK=G dH. Evaluating on B gives BK=G^2.

For a compactly supported invariant probability nu, invariance and differentiation on its compact invariant support give int BK dnu=0. Therefore G=0 almost everywhere and, by continuity, everywhere on its support. On that support H is orbit invariant. If nu is full-flow ergodic, H is constant almost everywhere, and continuity makes it constant on the entire support.

On the backward orbit of y, K is bounded and monotone in forward B time. Thus integral_(-infinity)^0 G(Phi_s y)^2 ds is finite. The derivative BG is bounded on the compact orbit closure, so G(Phi_s y) is uniformly Lipschitz in s. A sequence of values with absolute value at least epsilon as s->-infinity would give disjoint intervals of a fixed positive length on which the absolute value is at least epsilon/2, contradicting that finite square integral. Hence G(Phi_s y)->0, and continuity puts every backward limit point in {G=0}.

## 4. Why zero helicity gives the rank identity on O

For the Euler application, the equation upgrades P to C3, H is C3 and G is C2. Uniform sublinearity makes B complete and traps every compact initial set under backward B time in a compact ball. The bracket [B,W]=-kappa W and the Lamb identity imply

    WH=0, WG=W(BH)=[W,B]H+B(WH)=0.

Both H and G are global C2 first integrals of W.

Here is the full recurrence input. For every small epsilon>0, forward carrier growth is bounded by C exp((c+epsilon)s)(1+|y|). Conjugating a uniform short W-flow on the compact backward trap by that carrier flow proves W-flow completeness and, on every compact initial set Q,

    sup_(x in Q)|Gamma_t x|<=C_(Q,epsilon)(1+|t|)^((c+epsilon)/kappa).

Choose epsilon so that 3(c+epsilon)<kappa. Since div W=0, the W flow preserves volume. If a bounded set had disjoint first N images under Gamma_1, their total volume would be proportional to N while they all lie in a ball of volume O(N^(3(c+epsilon)/kappa)), a contradiction unless the set is null. The last-return decomposition and a countable basis then give almost-everywhere topological recurrence. This is the A048-A049 argument and requires no vorticity decay assumption.

There are no nonconstant periodic W orbits. A period T would be transformed by backward carrier time s to period exp(-kappa s)T, all inside one compact ball. If L bounds |DW| there, periodic Wirtinger and the Lipschitz inequality imply T>=2pi/L for every nonconstant periodic orbit in that ball. To check the inequality, subtract the orbit mean zbar, use int z'=0, and write

    int |z'|^2=int (W(z)-W(zbar)).z'
       <=L ||z-zbar||_2 ||z'||_2<=LT/(2pi) ||z'||_2^2.

The shrinking periods contradict it.

If (H,G) had rank two at a point of O, that rank-two locus would contain an open ball. Sard's theorem at C2 regularity says its globally critical values have planar measure zero. In submersion coordinates, Fubini says the inverse images of those values have zero spatial measure in the rank-two locus. Choose there a recurrent point with globally regular value. Its fiber is a closed embedded one-dimensional manifold and the W orbit remains on one component. On a line component, or an interval of a circle separated by zeros, a nonzero flow orbit is ordered and cannot return to its initial point. A zero-free circle yields a forbidden periodic orbit. A regular-level chart precludes other fiber sheets from accumulating at the initial point. This contradicts recurrence.

Thus dG wedge dH=0 on O. Density of O and continuity extend it to all R3. Section3 applies. This is exactly where the dense-vorticity premise is used.

## 5. Propagating constancy from a given measure to its basin

Let nu be a given vortical SRB probability as in part (B). Section3 gives H=h on its support. Positive unstable conditional densities give, on a suitable local unstable arc gamma, a full-arclength subset T consisting of support points generic for nu. Near a regular point, the vectors gamma-prime,-B,W are independent. Hence

    C(s,t,tau)=Gamma_tau(Psi_t gamma(s))

is a C1 diffeomorphism on a small box. Here Psi is backward B time. For s in T, the inner point remains on the invariant support, and W preserves H. Therefore H(C(s,t,tau))=h on a full-volume subset of this box. Continuity makes H=h throughout its image V.

This equality also holds on every flow image Psi_r V, even though H has not been assumed B-invariant away from the support. Indeed completeness of W and exact conjugacy give

    Psi_r C(s,t,tau)=Gamma_(tau exp(-kappa r)) Psi_(r+t) gamma(s).

For s in T, its rightmost point belongs to the support and the W shift preserves H. Thus H=h on a full-volume subset of Psi_r V, hence everywhere there.

Take the union E of these transported boxes over a countable family covering nu-almost every typical point, and all real carrier times. Second countability makes it a countable union of open sets for the null-set arguments. It is open, invariant, has full nu measure, and H=h throughout E. Every basin point enters E: a nonnegative compactly supported continuous function in E with positive nu integral has positive limiting time average on each basin orbit. Invariance then places the entire basin in E. Since A223's open essential basin D_nu differs from its basin only by a null set, E has full volume in D_nu. Continuity extends H=h to all D_nu.

If such domains cover almost every point of O, A266 gives a spatially constant U. This proves (B) with every additional hypothesis retained.

## 6. Scope

Part (A) uses the strong stable density as an explicit premise. The unverified claim that all mixing basic flows have the required density is not used. Part (B) avoids that premise but requires global zero helicity, C3 regularity, dense O, and separate measure existence and coverage. If W vanishes on an open region, the two first-integral equations are vacuous there and do not prove global closedness of G dH. Closedness only on a nonsimply connected vortical region would also leave periods uncontrolled. None of these results proves the original nonexistence conjecture without its extra assumptions.
