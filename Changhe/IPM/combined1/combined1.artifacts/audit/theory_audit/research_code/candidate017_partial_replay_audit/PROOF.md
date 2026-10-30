# Candidate017: sixteen dual trials and two residual-mode certificates

Written 2026-10-29T17:43:47.494922+00:00 before the checker. This audit independently reconstructs the exact trial energies and sums all exported interval groups. The source projection and moment enclosure algorithms are dependencies, not newly repeated integrals.

## Exact statement and hypotheses

Let chi be the exact potential C1-N1-017-legqs50-quot013, raw SHA256 7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114, c=4076476460239181/2251799813685248 and delta=1-1/c. On R2 put rho=-partial_y Delta chi, U=(-chi_xyy,chi_xxy), F=(cX+U).grad rho-rho. Let H(F) be the supremum of |int F phi| over real smooth compactly supported phi with ||grad phi||2<=1. It may initially be infinite. Every mode is the exact sine projection of this same F, with no change of scale or c.

For each odd n from1 through31 use the exact rational trial coefficients in the frozen N3_dual record. At n=1,3 also use its distinct N3_hres trial. For either trial set

    psi=u(r)sin(n theta),
    u=sum_i x_i r^3(1+r^2)^(-beta_i)(r^2/(1+r^2))^k_i,
    d=||grad psi||2^2, p=int F psi,
    Z=-u_r sin(n theta)e_r-u_yy cos(n theta)e_theta/(nr), y=log r,
    a=||Z||2^2, b=(pi/n^2)int r f_n u_yy dr.

Require beta_i>3/2, integer k_i>=-1, and 3+2k_i-n a nonnegative even integer. All d,a are positive. For n=1,3 let Q=pi int r^3 f_n^2 dr, with a complete containing interval for this whole-mode square. Retain the exact raw-to-projection and positive-pole moment soundness premises of the frozen source proofs. Every proposed coefficient, group endpoint, denominator and binding is checked; approximate source totals alone are not a premise.

The sixteen distinct dual trials imply

    H(F) > 307209799380023711068567013529/(5*10^29)
         > 0.614419598760.

The n=1,3 residual trials separately enclose the actual H(F_n) by the directed rational endpoints recorded in verification/result.json. These are partial results. They do not imply the whole017 upper bound or E2 interval asserted conditionally in T4-484. Fourteen residual-mode estimates, the other158 Hardy mode squares and the G0,G1,P2 inputs remain unreproduced by this audit. In particular no ordering E2017<E2007 follows.

## Complete analytic argument

At zero, r^(3+2k)sin(n theta) is a harmonic polynomial times a nonnegative integer power of r2. At infinity u and its first two logarithmic derivatives are O(r^(3-2 beta_min)). Thus psi is smooth, grad psi and r Delta psi are square integrable, and a smooth radial cutoff has squared gradient error O(R^(6-4 beta_min)), tending to zero. The explicitly grouped pairing integrals have exponent plus exact zero order greater than -1 at the compactified infinity endpoint; their denominator factors are positive on[0,1]. At zero the smooth radial and angular expressions are integrable. Consequently the ordinary pairings are absolutely convergent and agree with their cutoff limits.

Different frequencies are orthogonal in the gradient inner product. Apply a common radial cutoff to the finite trial sum sum_n(p_n/d_n)psi_n. Its pairing tends to sum p_n^2/d_n and its squared gradient norm tends to the same positive number. By the definition of H,

    H(F)^2 >= sum_n p_n^2/d_n.

This lower argument needs no complete Hardy estimate. Strict positive rational floors for each quotient yield the displayed strict lower bound by exact summation and squaring.

For a single mode put A=-r f_n cos(n theta)e_theta/n. On annuli div A=F_n. The vector field has zero radial flux and its finite squared L2 norm is Q/n2, so the distribution identity extends across zero. It gives H(F_n)<=sqrt(Q)/n. With r2 Delta psi=(u_yy-n2u)sin(n theta), integration by parts gives

    ||r Delta psi||2^2=n2(a+d),
    int r2 F_n Delta psi=n2(b-p),
    R2=||r(F_n+Delta psi)||2^2=Q+2n2(b-p)+n2(a+d).

The endpoint terms vanish by the trial decay just proved. In the gradient completion H(Delta psi)=sqrt(d): one inequality is integration by parts; the opposite inequality follows by cutoff testing with psi. The triangle inequality, the single-mode Hardy bound and duality therefore give

    max(0,sqrt(d)-R/n,|p|/sqrt(d)) <= H(F_n) <= sqrt(d)+R/n.

The two trial families at the same frequency are alternative tests and are never added as orthogonal modes. The sixteen-mode lower sum below uses only the nine-beta dual trials; the eight-beta residual trials are reported separately.

## Exact energies and exported groups

Set t=r2/(1+r2), v=1-t, b_i=beta_i-1 and P_b=sum x_i t^(k_i+1), so u=r sum_b v^b P_b. Define D_b P=(1-2bt)P+2t(1-t)P'. The complete ordered beta-pair formulas are

    d/pi=(1/2)sum_(b,c)int_0^1 v^(b+c-2)[D_bP_b D_cP_c+n2 P_bP_c]dt,
    a/pi=(1/2)sum_(b,c)int_0^1 v^(b+c-2)[D_bP_b D_cP_c+D_b2P_b D_c2P_c/n2]dt.

Every exponent exceeds -1. Independently compute M_j(e)=int_0^1 t^j(1-t)^e dt from M_0=1/(e+1) and M_j=j M_(j-1)/(e+j+1). This differs from the producer's expansion in v and direct reciprocal sums. Integrating the polynomial coefficients against these exact rational moments must reproduce every stored energy group and its complete exact total. All ordered pairs, all labels and all nonzero coefficients are retained.

For the projected F_n=r sum_l v^(l delta/2)A_(l,n)(t), the producer evaluates p,b and Q by complete grouping before integration. The exact rational-pole reduction reconstructs the numerator identity before calling containing Arb arithmetic. Reparse every650digit group at4096bits. Require its exact endpoint condition, positive denominator factors, finite precision and original reconstruction flag. Sum all signed groups before multiplication by pi/2; bound the sum of absolute exported radii by10^-200 and require more than600 relative bits in the resulting pairing. For n=1,3 expand R2 using these containing balls and the independently computed energies. Cancellation must leave a positive containing interval with more than600 bits; a failure cannot be hidden by comparing rounded displays.

For each printed strict rational lower or upper endpoint compare against the newly summed interval endpoints, not merely against an overlapping producer total. The residual-mode lower endpoint is below the maximum of the two recomputed lower expressions and the upper endpoint is above sqrt(d)+R/n. Exact positive floors are squared and summed for the total H lower statement. Confirm source diagnostic containment separately. The current stored hres program does not match the historical code hash in its JSON; historical execution is unobserved. This does not affect the exact proposed-vector verification through the independent formulas.

## Scope and reproducibility

T4-484 supplies the fully stated conditional017 composition and its independently checked residual identity. T4-481 accepts both existing Opus reviews of the general angular Hardy theorem. The source projection and moment proofs are frozen here in full, with the producer code as text only and all194 producer bindings rechecked before and after. No peer code is executed and no field integral is repeated. The source group's enclosing property retains the stated algorithm soundness premise; this audit verifies its complete exported finite composition, energies and directed conclusions. No inverse, correction-distance ordering, nonlinear closure or existence follows. No JavaScript/TypeScript, servers, clusters/RLScience, remote compute or new model client is used. Collaboration continues through the existing Opus theory lanes; their configured model is Opus5.5, and provider identity remains unobservable.
