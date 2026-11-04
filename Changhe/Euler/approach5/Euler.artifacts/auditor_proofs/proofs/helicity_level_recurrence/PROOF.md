# Helicity of opposite signs on the same Bernoulli levels

Status: CONFIRMED at the exact scopes of A326-A328. The full configured-model review was read and its conservativity, saturation and global-conclusion clarifications incorporated. Every claim is analytic; no computation is used.

## 1. Exact abstract recurrence statement

Let Gamma be a complete C1 flow on R3 preserving Lebesgue measure. Suppose almost every point returns arbitrarily close to itself at arbitrarily large positive integer times. Let D be open and forward Gamma-invariant, let H be C1 on D, let h be continuous on D, and suppose

    d/dt H(Gamma_t x)=-a h(Gamma_t x),   a>0.

If h is nonzero somewhere in D, there is a nonempty open interval I of real numbers such that, for every b in I, one and the same recurrent orbit in D contains points x_b^+,x_b^- with

    H(x_b^+)=H(x_b^-)=b,
    h(x_b^+)>0,   h(x_b^-)<0.                              (1)

Consequently, if each level set D intersect {H=b} carries at most one sign of h, with that sign allowed to depend on b, then h=0 throughout D. Empty levels are irrelevant. This condition is weaker than requiring one sign on all of D. No integrability, finite total volume, bounded H or compact vortex orbit is assumed.

## 2. Proof of the same-level statement

Choose a recurrent point x in an open region where h is strictly positive; if the available sign is negative, replace H and h by their negatives. Put q(t)=H(Gamma_t x). For a sufficiently small delta>0, q is strictly decreasing on [0,delta], with q'(t)<0. Choose numbers ell<u strictly between q(delta) and q(0).

Recurrence and continuity give an integer N>delta with q(N)>u. Let t_u be the first time in [delta,N] at which q reaches u. Let t_ell be the last time before t_u at which q equals ell. These times exist by continuity, and

    ell<q(t)<u   for t_ell<t<t_u.

The mean value theorem supplies t_* in this interval with q'(t_*)>0. Thus h(Gamma_(t_*)x)<0 and q(t_*) lies strictly in (ell,u). The strictly decreasing initial segment has a unique s_* in (0,delta) with q(s_*)=q(t_*), and h(Gamma_(s_*)x)>0.

The ordinary one-variable inverse function theorem at s_* and t_* gives two short time intervals on which q is a diffeomorphism onto open value intervals. Their intersection contains q(t_*) and therefore contains a nonempty open interval I. Taking the corresponding inverse times gives(1) for every b in I. Every point used remains in D by forward invariance.

A nonzero h in D always permits the initial recurrent x because its strict-sign set is open and has positive volume, while the recurrence set has full volume. The levelwise one-sign condition contradicts(1), proving the consequence.

## 3. Euler consequence under supplied smooth coverage

Let U in C-infinity(R3;R3), P in C1 solve div U=0 and (1-c)U+(B.grad)U+omega JU+grad P=0, with U(y)->0 uniformly, 2/5<=c<1/2 and arbitrary finite omega. Here J(y1,y2,y3)=(-y2,y1,0). Put B=(cI-omega J)y+U, Omega=curl U, a=1-2c, h=U.Omega, and H=P+|U|2/2+((cI-omega J)y).U.

A048-A049 give the complete recurrent Omega flow. Their proof uses only uniform sublinearity, the exact bracket and divergence, and works for C2 profiles. The Lamb identity gives Omega H=-a h. A308 and A207/A223 supply countably many invariant open essential vortical basins D_i covering {Omega!=0} modulo a null set.

Assume that for each i and each real b, h has at most one sign on D_i intersect {H=b}. The sign may vary with i and b. Section2 gives h=0 on every D_i. The remainder of the A309 proof then gives U=0: A278 uses a full-arclength generic unstable plaque, short carrier/vortex product coordinates and the canonical L2 Bernoulli decay to obtain H0=0 throughout each D_i. Coverage and continuity give grad H0=0 on {Omega!=0}. At its boundary the Lamb identity gives U=0. Extend U on the interior of {Omega=0} by zero; the extension is locally Lipschitz, distributionally divergence-free and curl-free, hence entire harmonic and zero on a nonempty open set, so it vanishes. If Omega was identically zero, decay and harmonicity already give U=0. Thus grad H0=0 globally. Its vanishing normalized square mean forces H0=0, and the Lamb identity gives U.B=0 and P0=|U|2/2. Testing partial_i partial_j(U_i U_j)+Delta(|U|2/2)=0 against chi(y/R)sqrt(1+|y|2) yields a nonnegative strictly positive velocity stress, with cutoff error bounded by C E(2R)/R tending to zero. Hence U=0. These are exactly the canonical-pressure, boundary-localization and global positive-stress steps of A309, not an inference from one constant-H basin alone. The new premise uses H only through its level sets and is unchanged by adding a pressure constant.

Equivalently, any nonzero profile in this smooth decaying class must have an essential basin and a nonempty open interval I of Bernoulli values such that every value in I is attained with both helicity signs, along one recurrent vortex orbit in that basin. This does not prove nonexistence when such same-level sign changes occur. It does not assert this for every basin or every Bernoulli value. It gives no C2 coverage theorem.

The same deduction holds for a C^r decaying profile under the confirmed finite-r coverage criterion A312. At C2 with a separately given family of vortical SRB basins covering the vortical region, it is again a conditional conclusion.

## 4. Conservative coboundaries with one integrable sign

This section generalizes the already confirmed A114/A123 return-tower argument; total-helicity cancellation alone is not a new claim. Let T be an invertible measure-preserving transformation of a sigma-finite measure space, conservative in both directions. Let G be measurable and finite almost everywhere and F=G composed T-G. If either F_plus or F_minus is integrable, both are integrable and

    integral F_plus=integral F_minus.                     (2)

No integrability of G is required. Choose an increasing finite-measure exhaustion E_n and put A_n=E_n intersect {|G|<=n}. These sets are increasing and cover the space modulo null sets. Their invariant saturations S_n=union_(j in Z)T^j A_n likewise increase and exhaust. Almost every point of A_n returns both ways. The first-return map T_A preserves its finite measure, and G is bounded on A_n. Thus

    Q_A=G composed T_A-G,   integral_A Q_A=0.

For bases A_k={x in A:first return=k}, the levels T^j A_k,0<=j<k, are disjoint and partition S_A modulo null sets. Coverage uses the most recent past visit to A; disjointness uses the first-return definition. Backward conservativity makes the past visits unbounded below almost everywhere on A, and thus on its two-sided saturation. Consequently the forward return towers cover that entire two-sided saturation modulo null sets, not just a possibly smaller forward union. Suppose F_minus is integrable. By Tonelli the accumulated negative part N_A up to first return has integral equal to integral_(S_A) F_minus, which is finite. The accumulated positive part P_A satisfies P_A-N_A=Q_A pointwise, because return times are finite. It follows that P_A is integrable and its integral equals that of N_A. Applying the tower formula again gives

    integral_(S_A) F_plus=integral_(S_A) F_minus.

Monotone convergence through S_n proves(2) and global integrability of F_plus. Replace G by -G for the other sign. In particular every integrable conservative coboundary has integral zero. This proof also covers restriction to any invariant measurable subspace.

## 5. Signed helicity balance in every Borel Bernoulli band

Let U in C2(R3;R3), P in C1 satisfy the same exact divergence-free profile equation, now with 0<c<1/2, every finite omega, and U(y)=o(|y|) uniformly. Keep a=1-2c, h=U.Omega and H=P+|U|2/2+((cI-omega J)y).U. Let E be any measurable set invariant under all Gamma times. No Dini derivative decay, helicity integrability or bounded H is assumed. For every Borel set I in R,

    integral_(E intersect {H in I}) h_plus
       =integral_(E intersect {H in I}) h_minus,           (3)

where equality is in [0,infinity]. Thus both sides are finite and equal, or both are infinite. Equivalently, the two possibly infinite positive measures h_plus dy and h_minus dy on E have identical pushforwards under H. When h is integrable on E this is the ordinary finite signed-pushforward identity from A302, now needing only that integrability. The whole-space I=R case already follows from A123.

Here is the complete localization argument. More generally let phi be any bounded Borel function and put

    G(s)=-(1/a) integral_0^s phi(v)dv,
    k(x)=phi(H(x))h(x).

The primitive G is globally Lipschitz. For every fixed x, q(t)=H(Gamma_t x) is C1. The one-variable chain rule gives

    G(q(1))-G(q(0))=integral_0^1 k(Gamma_t x)dt.           (4)

For precision concerning an arbitrary Borel phi: G'=-phi/a outside a null set of values. On the open set where q'!=0, countably many local inverse-function intervals pull that exceptional value set back to a null set of times. At a time with q'=0, the Lipschitz bound on G makes the derivative of G composed q equal to zero directly. The composition is locally Lipschitz, so its almost-everywhere derivative integrates to(4). This also handles individual exceptional level values without an unproved pointwise chain rule.

A049 proves Lebesgue conservativity for the time-one map Gamma_1 in both directions by the polynomial-growth wandering-image argument; topological recurrence alone is not being substituted for conservativity here. Restriction to the invariant measurable E preserves this property and volume preservation. Thus T=Gamma_1 restricted to E is conservative and measure preserving. Set F=G(H) composed T-G(H), A_plus=integral_0^1 k_plus composed Gamma_t dt and define A_minus similarly. All are finite pointwise on each compact orbit segment, since h is continuous and phi bounded. Equation(4) gives F=A_plus-A_minus. If integral_E k_minus is finite, invariance and Tonelli give integral_E A_minus=integral_E k_minus, while F_minus<=A_minus. Section4 gives F integrable with integral zero. Hence A_plus=F+A_minus is integrable, and Tonelli gives

    integral_E k_plus=integral_E k_minus.

The other one-sided assumption follows by changing signs. Therefore the positive and negative integrals of k are always either equal and finite or both infinite. Taking phi=1_I gives(3).

If h is in L1(E), bounded phi makes k integrable and gives integral_E phi(H)h=0 for every bounded Borel phi directly. Under Dini, A302 has already supplied h in L1(R3), so its finite-measure conclusions follow for all invariant E. Dini is not used for(3).

## 6. Independent review and scope

The coordinator's full focused review independently checks Section2's same-level crossing, Section4's return towers and Section5's Borel chain rule and one-sided integrability argument. Its explicit A049 conservativity citation, two-sided saturation clarification and A309 global-conclusion correction are incorporated above. Literature agent independently checked the same arguments. Received review text and configured model identity are retained in the team records; configuration is not provider attestation. Section4 is a general measurable-primitive form of the existing A114/A123 method, not a claim that total cancellation was missing.

Both deductions preserve arbitrary finite omega. They do not establish a helicity sign, exclude unrestricted sign-changing helicity or close the main conjecture. The signed integrals in(3) may both be infinite; no integrability is derived from velocity decay. The smooth-coverage consequence retains the explicit levelwise sign premise and gives no automatic C2 coverage. These recurrence and balance refinements use H only through Omega H=-ah. They do not distinguish the actual Euler H from every other scalar with its correspondingly defined h. The Liouville consequence additionally uses the genuine canonical-pressure and energy inputs of A309.
