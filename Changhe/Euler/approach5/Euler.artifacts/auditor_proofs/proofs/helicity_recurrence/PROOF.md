# Helicity cancellation from recurrent vorticity flow

## Statement

Let U in C2(R3;R3), P in C1(R3) solve the rotating Euler profile equation, with div U=0, U=o(|y|) uniformly, 0<c<1/2 and arbitrary finite omega. Put Omega=curl U and h=U dot Omega. Then h has both signs unless it vanishes identically. If h belongs to L1(R3), its total integral is zero.

Neither derivative decay nor pressure normalization is assumed. Absolute integrability of h is an explicit extra condition for the integral statement. Neither conclusion implies Omega=0.

## Primitive and recurrence

Set a=1-2c and

    G=-(P+|U|^2/2+c y.U-omega(Jy).U)/a.

The exact momentum identity a(U-grad G)=B cross Omega gives

    Omega.grad G=h.

The complete Omega flow psi_t preserves Lebesgue measure. By A048-A049 it is conservative: the image of a compact set at time t lies in a ball of radius C(1+|t|)^beta, where beta=(c+epsilon)/(1+c) can be chosen with 3 beta<1. A positive-measure wandering set would have N disjoint equal-volume images inside a ball of volume O(N^(3 beta)), impossible. The same applies to inverse time. Thus the time-one map T=psi_1 is recurrent on every bounded measurable set, and almost every point is topologically recurrent.

If h>=0, G(psi_t x) is nondecreasing. At any recurrent x choose integers n_j tending to infinity with T^(n_j)x tending to x. Continuity gives G(T^(n_j)x)->G(x). Monotonicity then forces G(psi_t x)=G(x) for every t>=0, so h(x)=0. This holds almost everywhere and continuity makes h identically zero. Apply the same reasoning to -G if h<=0.

## Integrable coboundaries on the infinite-volume space

Suppose F=G o T-G is in L1. Fix a ball A. Almost every point of A has a finite first return r_A, and the induced return map T_A preserves measure on A. The latter follows by partitioning A according to r_A and using the unique previous visit to A. Since G is continuous, it is bounded on the closed ball, and

    integral_A (G o T_A-G)=0.

The sets T^j{x in A:r_A(x)>j}, j>=0, are disjoint and cover the full two-sided saturation S_A of A up to a null set. Disjointness follows because an overlap would give a premature return to A; coverage follows from the most recent past visit. Hence measure preservation and absolute integrability give

    integral_A sum_{j=0}^{r_A(x)-1}|F(T^j x)| dx
      = integral_{S_A}|F| < infinity.

Telescoping is therefore legitimate under the integral, and

    integral_{S_A}F=integral_A(G o T_A-G)=0.

Increasing balls have increasing saturations exhausting R3. Dominated convergence yields integral F=0. No integrability of G on the whole space is needed.

Finally, if h is in L1, the primitive identity gives

    F(x)=G(Tx)-G(x)=integral_0^1 h(psi_t x) dt.

Tonelli gives ||F||_1<=||h||_1, and Fubini and volume preservation give integral F=integral h. Thus integral h=0.

## Dependencies and scope

The proof uses the exact primitive already checked in A059, complete conservative frozen flow A048-A049, and the return-tower argument supplied here. It strengthens the cancellation step of A083 by replacing its derivative hypotheses with h in L1 itself. It does not supply that integrability from velocity decay, nor a new exclusion of the possible chaotic core. This confirms LIT24.

## One-sided integrability strengthening (LIT26)

Under the same C2 profile, uniformly sublinear velocity, 0<c<1/2 and arbitrary finite omega hypotheses, let h=U dot Omega and h_plus=max(h,0), h_minus=max(-h,0). If either signed part is integrable, then both are integrable and their integrals agree. Thus the only possibilities are two equal finite signed integrals or two infinite signed integrals. In particular, one sign outside a compact set implies h in L1 with integral zero.

Here is a complete one-sided version of the conservative-coboundary argument. For an invertible conservative measure-preserving map T and a continuous finite G, put F=G composed with T-G. Suppose F_minus is integrable. On a ball A let r_A be the first return time and T_A the induced map. Conservativity in both directions makes T_A measure preserving on A. The first-return tower levels T^j{x in A:r_A(x)>j} are disjoint and cover the full saturation S_A up to a null set. The past-return property supplies coverage; the first-return property supplies disjointness.

Since G is bounded on A, Q_A=G composed with T_A-G is bounded and has integral zero on A. Define N_A and P_A to be the sums of F_minus and F_plus up to the first return. Tonelli gives integral_A N_A=integral_{S_A} F_minus<infinity. The finite telescoping sum gives P_A-N_A=Q_A, so P_A is integrable and has the same integral as N_A. Tonelli again gives integral_{S_A} F_plus=integral_{S_A} F_minus. Increasing balls have increasing saturations covering the space. Monotone convergence therefore gives global integrability and equal integrals. Replacing G by -G proves the other one-sided case. No integrability of G or of return times is used.

Apply this with T=psi_1, the complete conservative vorticity flow from A048-A049, and the exact primitive G satisfying Omega dot grad G=h. Let

    A_plus(x)=integral_0^1 h_plus(psi_t x) dt,
    A_minus(x)=integral_0^1 h_minus(psi_t x) dt.

These are finite pointwise, and F=A_plus-A_minus. If h_minus is integrable, measure preservation gives integral A_minus=integral h_minus and F_minus<=A_minus. The discrete lemma gives F in L1 with integral zero. Hence A_plus=F+A_minus is integrable, and Tonelli gives h_plus in L1. Fubini now gives integral h=integral F=0. The other sign is identical. If h has one sign outside a compact set, the opposite signed part is compactly supported and bounded, so this hypothesis holds.

This strengthens the integrability premise only. It does not derive one-sided integrability from velocity decay and does not force vanishing vorticity.
