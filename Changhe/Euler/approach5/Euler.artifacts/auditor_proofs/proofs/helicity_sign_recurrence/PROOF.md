# Recurrence rules out one-signed nonzero helicity on vortex-invariant domains

## Exact statement

Let 0<c<1/2, omega be any finite real number, and U in C2(R3;R3), P in C1(R3) solve the divergence-free rotating profile equation with U=o(|y|) uniformly at infinity. Put A=cI-omega J, B=Ay+U, Omega=curl U, a=1-2c, kappa=1+c, h=U.Omega, and H=P+|U|^2/2+Ay.U. Let Gamma be the complete Omega flow.

If an open set D is invariant under every forward Gamma time and h has one sign throughout D, then h=0 on D. There is also a full-Lebesgue-measure set R such that, for every x in R with h(x)!=0, h(Gamma_t x) takes both strictly positive and strictly negative values at arbitrarily large positive and arbitrarily large negative times.

Consequently the pointwise zero-helicity premise on each vortex-invariant basin in A273 or A278 can be replaced by a one-sign premise, independently for each basin. All other hypotheses of those conditional theorems, including the existence of the specified measures and almost-everywhere basin coverage, remain in force.

## 1. The complete recurrent flow

We reproduce the needed A048-A049 argument. The full profile equation implies

    [B,Omega]=-kappa Omega,
    a U+grad H=B cross Omega,
    Omega H=-a h.                                        (1)

Uniform sublinearity makes B at most linear, and outside a large ball B.y>0. Thus its complete flow Phi has all negative semiorbits from a given compact set in one fixed compact ball. On a neighbourhood of that ball the local Omega flow has a uniform existence time delta>0. For any finite s, a sufficiently large T gives the globally consistent definition

    Gamma_s x=Phi_T Gamma_(s exp(-kappa T)) Phi_-T x.

The local bracket identity verifies that this solves the Omega equation, and uniqueness makes all choices of T agree. The allowed time intervals exhaust the line, proving completeness and

    Phi_t Gamma_s=Gamma_(s exp(kappa t)) Phi_t.             (2)

For any epsilon>0, sublinearity gives

    |Phi_t z|<=exp((c+epsilon)t)(|z|+C_epsilon/(c+epsilon)), t>=0.

Take T=kappa^-1 log(1+|s|/delta) in the preceding construction. The inner local-flow point stays in a compact set, uniformly for x in a fixed compact K. Hence

    sup_(x in K)|Gamma_s x|<=C_(K,epsilon)(1+|s|)^d,
    d=(c+epsilon)/(1+c).

Choose epsilon so that 3d<1, possible because c<1/2. Since div Omega=0, Gamma preserves Lebesgue measure. For a bounded measurable set E, let W consist of points of E having no strictly future return to E under Gamma_1. Its images Gamma_n W are pairwise disjoint. The first N+1 images lie in a ball of volume at most C(1+N)^(3d). Therefore

    (N+1)Leb(W)<=C(1+N)^(3d),

and Leb(W)=0. Points in E with only finitely many returns lie in the union of inverse iterates of W, hence also form a null set. Apply the same proof to Gamma_-1. A countable basis of bounded rational balls gives a full-measure set R of points returning arbitrarily close to themselves in both integer-time directions. This argument uses neither finite total volume nor bounded individual vortex orbits.

## 2. One sign on a forward-invariant open set

Suppose h>=0 on D and is positive somewhere. Continuity gives a nonempty open ball V contained in D with h>0. Select x in V intersect R. Forward invariance of D and (1) make H(Gamma_t x) nonincreasing for all t>=0. Its derivative is initially strictly negative. Thus for some t0,eta>0,

    H(Gamma_t x)<=H(x)-eta, t>=t0.

Positive-time recurrence supplies n_j tending to infinity with Gamma_(n_j)x tending to x. Continuity of H contradicts the displayed strict gap. Hence h=0 throughout D. Replace H by -H for the other sign.

Only forward invariance is needed. No boundary condition, compactness, integrability of h or pressure normalization enters.

## 3. Both signs along a recurrent nonzero-helicity orbit

Fix x in R with h(x)>0. Choose delta,m>0 and a neighbourhood V of x such that h(Gamma_s z)>=m for z in V and 0<=s<=delta. Write f(t)=H(Gamma_t x) and eta=a m delta. At each sufficiently close recurrence time n,

    |f(n)-f(0)|<eta/4,
    f(n+delta)<=f(n)-eta<f(0)-3eta/4.

Choose a later close recurrence time n'>n+delta. Then f(n')>f(0)-eta/4, so f increases somewhere between n+delta and n'. By the mean-value theorem f' is positive at some intermediate time, and (1) gives h<0 there. The recurrence times themselves give positive h arbitrarily far in the future. This proves both signs arbitrarily late.

If h(x)<0, reverse the sign of H. For negative times apply the same proof to the reversed flow Gamma_-t and the function -H, whose derivative is again -a h along that reversed flow. The two-sided recurrence defining R gives the required negative-time sequence. No uniform lower bound on the size or frequency of the sign excursions is asserted.

## 4. Conditional basin applications

The regular basins of A273 are unions of complete Omega orbits, by their strong-stable representation. The essential SRB basins in A278 are invariant under every Gamma_s by (2), invariance of the continuous-time carrier basin under finite vortex shifts, and maximality of its full-volume open domain. Thus the one-sign theorem applies to every such basin separately. Their signs need not agree.

A273 then yields its original sublinear conclusion under regular mixing basin coverage; A278 yields its decaying-profile conclusion under the stated given-SRB properties and coverage, without mixing. Global one-signed helicity gives h=0 globally, but these arguments alone still do not establish global nonexistence without the remaining basin hypotheses or another Bernoulli argument.

## Dependencies and scope

The complete recurrence proof is independently checked in the team records and reproduced here. The two basin theorems are in the team records and in the team records. This confirms LIT60 with exactly its conditional applications. The arbitrary finite rotation rate drops out of the radial and volume estimates. No numerical calculation, formal build or new external theorem is used.
