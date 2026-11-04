# Annular continuation with a punctured local square-integrability hypothesis

Status: independently reconstructed and compared with the existing Theory Agent C  review. Designated verdicts are recorded in the auditor's ledger (AUDIT_LEDGER.md). No computation is needed.

## 1. Statement and exact dependencies

Let R>0, D_R={z in C: |z|<R}, dA be planar Lebesgue area, and partial_bar=(partial_x+i partial_y)/2. Suppose f is a smooth complex-valued function on D_R, all its derivatives at zero vanish, and b is nonnegative, measurable, finite almost everywhere and in L2_loc(D_R minus {0}). Assume |partial_bar f|<=b|f| almost everywhere. Then either f is identically zero or, for every 0<R0<R,

    [integral_(r<|z|<R0) b(z)/|z| dA]/log(R0/r) -> infinity
    as r decreases to zero.                                      (1)

In particular f is zero if b is weak-L2 on D_R, with finite norm

    M=sup_(t>0) t |{b>t}|^(1/2).                                  (2)

A bounded sequence of the normalized annular costs also implies f=0. There is no smallness assumption. Local L2 away from zero remains an independent hypothesis.

The only continuation input is A2470: a smooth function flat at the center of a disc, with a globally L2 coefficient in the same scalar inequality, is zero on that disc. All seven sections of its independent proof, in the team records, were reread. Its Cauchy factor lies in W12, finite powers of its exponential are integrable, and the weak chain rule makes the product holomorphic; arbitrary-order flatness contradicts a nonzero holomorphic factor by disk L2 integrals. This proof uses neither (1) nor the present weak-L2 conclusion. A2473 separately verifies the published theorem's scope. No new primary-source retrieval or novelty claim is made here.

## 2. Positive isolated zeros away from the distinguished center

Let O be the set of points of the punctured disc near which f vanishes identically. It is open. If points of O tend to a point p of the punctured disc, all derivatives of f vanish at p by continuity. Choose a disc centered at p whose closure avoids zero and lies in D_R. Its coefficient is L2. A2470 gives vanishing on this disc, so p belongs to O. Connectedness of the punctured disc makes O either empty or the whole punctured disc. In the latter case continuity also gives f(0)=0 and proves the theorem.

Assume the nonzero alternative. No zero p!=0 can be flat, since A2470 would make O nonempty. Let m>=1 be the first nonzero Taylor degree at p and P_m its homogeneous Taylor polynomial in two real coordinates. On the fixed annulus A={1/2<|w|<2}, put

    f_epsilon(w)=epsilon^(-m) f(p+epsilon w).

Taylor expansion gives convergence to P_m in C1 on the closure of A. The rescaled inequality and change of variables are

    |partial_bar f_epsilon|<=epsilon b(p+epsilon w)|f_epsilon|,
    ||epsilon b(p+epsilon .)||_(L2(A))^2
       =integral_(p+epsilon A) b(z)^2 dA(z) -> 0.                 (3)

The last limit uses absolute continuity of the L2 integral on a fixed disc around p. The C0 norms of f_epsilon remain bounded. Hence partial_bar P_m=0 on A and therefore identically. A homogeneous holomorphic polynomial in one variable is alpha w^m for alpha!=0.

Writing w=z-p, smooth Taylor estimates now give

    f(p+w)=alpha w^m+E(w),
    |E(w)|<=C|w|^(m+1), |DE(w)|<=C|w|^m.                         (4)

Consequently |f(p+w)|>=|alpha||w|^m/2 on a small punctured disc. The zero is isolated. The quotient h(w)=f(p+w)/(alpha w^m) is 1+O(|w|), and differentiating it with (4) gives |Dh|<=C'. Extend h(0)=1. A line segment avoids the center or splits into two segments ending there, so the derivative bound and continuity imply that h is Lipschitz on the whole smaller disc. Shrink once more to keep |h-1|<1/2. A smooth branch of log h then gives

    log|f(p+w)|=m log|w|+g(w),                                  (5)

where g=log|alpha|+Re log h is Lipschitz. The same homotopy of h to 1 proves that the local winding number of f is m>0. No continuous integrating factor for an L2 coefficient was assumed.

## 3. Radial means and the inward winding inequality

There are finitely many zeros in each compact annulus: an infinite sequence would accumulate at another off-center zero, contradicting its isolation. Thus the exceptional radii of circles containing zeros are locally finite in (0,R), although they may accumulate at zero or R.

At a nonexceptional radius rho let k(rho) be the winding of f on the positively oriented circle. The form Im(df/f) is closed where f is nonzero, since d(df/f)=0. Apply Stokes to an annulus with small disks about its finitely many zeros removed. The negative orientations of the holes give

    k(rho2)-k(rho1)=sum_(rho1<|p|<rho2) m_p >=0.                (6)

Define m_f(rho) as the normalized angular mean of log|f(rho exp(i theta))|. Formula (5) makes this integral finite even at exceptional radii. On any compact annulus, subtract the finitely many logarithmic terms m_p log|z-p| using all zeros in a slightly larger annulus. The remainder is Lipschitz locally across each zero and smooth elsewhere. A finite covering bounds its local Lipschitz constants on the compact annulus, which suffices for a Lipschitz radial mean. Each subtracted term has mean log max(rho,|p|). These means are continuous and Lipschitz on a radial interval bounded away from zero. Thus m_f is continuous and locally absolutely continuous on (0,R).

On a zero-free circle the smooth polar identity is

    (partial_rho f)/f+(i/rho)(partial_theta f)/f
       =2 exp(-i theta) (partial_bar f)/f.

The mean of (partial_theta f)/f is i k(rho). Taking real angular means therefore gives, for almost every rho,

    m_f'(rho)-k(rho)/rho
       =mean_theta 2 Re[exp(-i theta)(partial_bar f)/f].         (7)

Fubini transfers the almost-everywhere bound by b to almost every circle. On a compact annulus b is L2 and hence L1, and division by radius is bounded. This proves integrability of the right side for the radial integration below, including across exceptional radii.

Choose a nonexceptional R1<R0 and set K=k(R1). For r<R1, (6) gives k(rho)<=K inward. Integrating (7), using local absolute continuity, yields

    m_f(R1)-m_f(r)
       <=K log(R1/r)+(1/pi) integral_(r<|z|<R1) b/|z| dA.      (8)

This holds also at exceptional r by continuity and absolute continuity of the annular integral on positive-radius intervals. No lower bound on k and no finite count of zeros near zero is required.

## 4. Flatness forces superlogarithmic cost

For each integer N>=0, smooth flatness gives |f(z)|<=C_N|z|^N on a sufficiently small disc, with C_N positive and finite. Hence m_f(r)<=log C_N+N log r. Substitution in (8) gives

    (1/pi) integral_(r<|z|<R1) b/|z| dA
       >=(N-K) log(R1/r)+m_f(R1)-log C_N-N log R1.             (9)

For fixed N take the lower limit after division by log(R1/r), then let N grow. The result is an infinite limit. Positivity of b and log(R1/r)/log(R0/r)->1 prove (1) for every R0. The coefficient's local L2 property ensures finiteness of each fixed annular integral; it is not a bound as the inner radius tends to zero.

If (2) holds, layer cake on a finite-area measurable set E gives

    integral_E b <=integral_0^infinity min(|E|,M^2/t^2)dt
                  =2M sqrt(|E|).                             (10)

The equality splits at t=M/sqrt(|E|), with zero cases immediate. Therefore an annulus a<|z|<2a contributes at most 2sqrt(3pi)M to the integral of b/|z|. Partition inward from R0 into dyadic annuli. The number needed to cover r<|z|<R0 is ceil(log_2(R0/r)); the innermost full annulus may extend below r but stays inside D_R. The total cost is O(log(R0/r)), contradicting (1). Bounded dyadic costs also suffice even without a weak-L2 norm.

## 5. Carrier consequence and arbitrary rotation

Fix 0<c<1/2 and omega real. Set Jx=e3 cross x, A=cI-omega J, L=(1-c)I+omega J and X(x)=Ax. Let U be open in R3, avoid zero, and let V:U->R3 be smooth with W=curl V and

    div V=0, X.V=0, (DV)X=-LV.

Let sigma:D_R->U be smooth with det(sigma_1,sigma_2,X(sigma))!=0, and suppose V is flat at sigma(0). Assume a nonnegative measurable B, finite almost everywhere, is weak-L2(D_R) and L2_loc(D_R minus {0}), and

    |(W.X)(sigma(y))|<=B(y)|V(sigma(y))| almost everywhere.

The exact quotient reduction A2463, reread in Sections1-3 of in the team records, gives smooth local isothermal coordinates z=phi(y), phi(0)=0, and a smooth scalar f, flat at zero, with the same section zero set as V. Before any continuation theorem is applied, its inequality is

    |partial_bar f|<=[C1+C2 B(phi^-1(z))]|f|.                   (11)

All constants are finite on compact smaller coordinate discs. Bounded coordinate Jacobians preserve weak-L2 by change of variables in level sets, and preserve local L2 away from zero by change of variables in integrals. A constant on a bounded disc is weak-L2 and locally L2; the union bound at t/2 handles addition. Sections1-4 therefore give f=0 on a smaller disc and V=0 on a section neighborhood.

The transport equation integrates along finite X-orbit segments to V(exp(tA)x)=exp(-tL)V(x). Transversality makes (y,t)->exp(tA)sigma(y) a local diffeomorphism. It transports the zero section to a three-dimensional neighborhood of sigma(0). This uses no completeness of the V-flow, pressure normalization, boundary term or assumption at infinity. The conclusion is valid for every fixed omega, with no claim that the coordinate constants are uniform as omega varies.

## 6. Exact class extension and the omitted-hypothesis countertest

Every nonnegative b bounded by B2+C0/|z| on a bounded disc, with B2>=0 in L2 and C0 finite, is weak-L2 by Chebyshev and the union bound. On a compact set away from zero, (B2+C0/|z|)^2<=2B2^2+2C0^2/|z|^2 is integrable. Thus the present criterion contains the full C70 coefficient class without the extra local-boundedness restriction needed in LIT338. It also contains the weak-L2, punctured-locally-bounded class of LIT338.

Strictness follows from the confirmed example A2833. Choose smooth 0<=psi<=1 supported in the unit disk and equal to1 on the half disk, z_n=2^-n, A_n=2^(n^2), epsilon_n=A_n^-1 for n>=3, and set b=sum_n A_n psi((z-z_n)/epsilon_n), b(0)=0. The disjoint supports accumulate only at zero, so b is punctured-smooth. For A_(k-1)<t<=A_k, t^2|{b>t}|<=pi A_k^2 sum_(n>=k) A_n^-2<=4pi/3, with the full sum for t<=A_3. Hence b is weak-L2. For every C0 and all sufficiently large n, on the half-radius plateau C0/|z|<=A_n/2. Each plateau contributes at least pi/16 to the integral of (b-C0/|z|)_+^2. Every neighborhood of zero contains infinitely many such disjoint plateaus, so no bound by B2+C0/|z| is possible. This is a coefficient example only.

The additional punctured local L2 hypothesis cannot be dropped from the positive-index argument. At p!=0 take f_*(z)=conjugate(z-p), b_*(z)=1/|z-p|, with any finite value assigned at p. Then partial_bar f_*=1 and |partial_bar f_*|=b_*|f_*| almost everywhere. The weak-L2 norm is at most sqrt(pi), while the local L2 integral diverges at p and the local winding is -1. This is not a counterexample to flat-at-zero continuation, since f_* is not flat at zero. It only refutes that particular inference without its hypothesis.

## 7. Scope and verification record

All eight source sections, all eighteen manual-check entries and the pre-verification plan were read. The source snapshot is745ea7bddcfe778c8ea34368c8981cf2ca928b02a27c3ff2a8a0fa7d3a7802bc. The independent reconstruction includes the scaled L2 cancellation, the Lipschitz quotient, the exceptional-radius integration and the complete class inclusion. No mathematical computation, new model client, subagent or formal build is used for this audit.

In the full common-flat system F, C66 already gives punctured local boundedness of the relevant quotient. Thus A2832 already proves its necessary annular divergence and weak-L2 failure; this result adds no new full-F conclusion. General scalar weak-L2 continuation without the punctured L2 hypothesis, a contradictory Euler upper bound, exclusion of F, and the unrestricted smooth decaying rotating Euler conjecture remain open. The existing configured model comparison is complete as recorded below; actual provider execution is independently unattested.

## 8. Existing model comparison

The complete Theory Agent C  comparison stamped 2026-11-04T03:27Z was read, including every LIT340 item and its final scope and typography notes. It independently checks the scaled L2 identity, use of A2470 only on off-center discs, the Lipschitz quotient, the sign of the winding formula, the radial integration, the exact layer-cake constant, the pre-continuation quotient reduction, the coordinate change and finite transport. All agree with Sections 1 to 5 above.

It also checks the complete C70 class inclusion, the numerical-free bump level-set estimates and the negative-index countertest. The example's weak norm is bounded by sqrt(pi), not necessarily equal on an arbitrary off-center disc. It refutes the positive-index inference without the punctured L2 premise but is not flat at the distinguished center. The existing full-system necessary condition A2832 is unchanged. No additional mathematical hypothesis was silently removed. Its source-only missing spaces do not alter any formula. This supplies the requested existing configured model exchange without a new client, remote job or subagent. No Theory Agent C  mathematical computation is needed or rerun for LIT340.

## 9. Further comparison, exact class relations and source revision

The entire coordinator comparison dated 03:33Z and all ten final log entries were read. Its analytic arguments agree with Sections 1 to 8. The numerical winding test was corrected from an unsigned phase-range calculation to a signed count with a positive control; the comparison also discloses a later NameError run whose log was overwritten. No shared calculation was rerun here. The general proof is independent of these samples.

The coordinator's additional class observation can be proved directly. Fix a centered bounded disc. Let A be its weak-L2 coefficients that are locally essentially bounded off zero; let C be nonnegative coefficients bounded above by g+C0/|z| for some nonnegative g in L2 and finite C0; and let L be weak-L2 coefficients in L2 locally off zero. Then A and C both lie in L. They are incomparable: the previously verified disjoint-bump coefficient b0 belongs to A but not C, while a nonnegative smooth cutoff equal to one near an interior nonzero point zstar times |z-zstar|^(-1/2) belongs to L2 and is not locally bounded at zstar. Write that second coefficient as b1. Its square has singularity 1/|z-zstar|, integrable in two dimensions.

The sum b0+b1 belongs to L: use the half-threshold union bound for weak-L2 and local L2 stability under addition. It is not in A since b1 is unbounded at zstar and b0 is nonnegative. If b0+b1 were at most g+C0/|z| with g in L2, then b0 would obey the same bound, contradicting b0 not in C. Thus L strictly contains the union A union C. This statement compares coefficient classes only; it does not prove the missing Euler coefficient estimate.

A minor finite-disc qualification is needed in the comparison's level-area equalities. On D_R, the exact area of {C0/|z|>t} is pi min(R^2,C0^2/t^2), for C0>0. Hence pi C0^2/t^2 is a valid upper bound for every positive t and the exact area once t>=C0/R. For example t=C0/(2R) gives area pi R^2, not 4pi R^2. For a pole centered off zero, intersect its level disc with D_R; the plane-disc area is again a valid upper bound, with equality when that level disc is contained in D_R. All weak-L2 conclusions and the main comparison remain valid with this qualification.

The status revision 1873f196704ac6eead4847c38b45e0793367d9e4b83f9a2120bae26c2db3e120 was compared line by line with the archived submission, and its confirmation manifest was read. Only the status and added comparison section change. It preserves the punctured-L2 hypotheses, the exact verdicts A2852-A2855 and the separation from pending LIT342. The old closing sentence describing the submitted state is superseded by the status and confirmation section. No equation changes.

## 10. Corrected finite-disc level measure

For C0>=0 and t>0 the set {z in D_R:C0/|z|>t} has area pi min(R^2,C0^2/t^2). In particular the plane value pi C0^2/t^2 is an upper bound, with equality for t>=C0/R. For an off-center singularity the level disc is intersected with D_R, and its area is at most pi/t^2. These elementary set identities are all that the weak-L2 inclusion requires.

The coordinator comparison revision f23e829340eb3f44c7f307c5834b51956c770e673d67b7d02425b3363e154e18 repairs both statements explicitly in items 8 and 9. It preserves the old check log and describes its plane-area calculation accurately. Every changed line was read. A2864 continues to refute the original unqualified equality; the corrected statements and all unchanged inclusion conclusions are confirmed. No computation was repeated.
