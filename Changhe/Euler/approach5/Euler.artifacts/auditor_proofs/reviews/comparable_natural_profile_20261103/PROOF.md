# Conditional profile exclusion from a comparable actual tail scalar

## 1. Exact profile theorem

Fix2/5<c<1/2, finite real omega, p=(1-c)/c in(1,3/2), Jx=e3 cross x, A=cI-omega J and L=(1-c)I+omega J. Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, LU+DU(Ax+U)+grad P=0,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1)                       (1)

with a finite constant C. Let V and P2 be the actual velocity and pressure tails, Pinf the actual common pressure limit, D=R3 minus{0}, X=Ax, W=curl V, E=|V|^2, S=P2-E/2 and k=X.V. Each of the following additional sets of hypotheses implies U=0 and P constant.

I. On D, k=0 and W.grad S=0, and fixed constants0<r_-<=r_+<infinity satisfy

    r_-|S|<=E<=r_+|S| on S2.                       (2)

II. U.curl U=0 everywhere, (2) holds, and grad k cross grad S=0 on {S!=0}. The latter may be replaced by density of {W!=0,S!=0} in {S!=0}.

III. U.curl U=0 everywhere, {curl U!=0} is dense in {|x|>R0} for some finite R0, and for fixed positive finite constants r_-,r_+ and R1,

    r_-|P-Pinf-|U|^2/2|<=|U|^2
                         <=r_+|P-Pinf-|U|^2/2|      (3)

at every |x|>R1. This includes the zero sets with the same constants. No global helicity premise is included in I. The density in III rules out the resulting zero field, so III actually proves incompatibility of its entire hypothesis list.

These are conditional whole-profile statements. No comparison, rank, transport or full-gradient bound is inferred from bare velocity decay. Constants may depend on the fixed omega; no uniform estimates as its magnitude increases are asserted.

## 2. Regularity and rank inputs

The complete previously audited A533/A538/A539 give, with F_t=exp(tA),

    u_t=exp((1-c)t)exp(omega tJ)U(F_t x)->V,
    p_t=exp(2(1-c)t)[P(F_t x)-Pinf]->P2,

locally on all D in C^(1,alpha) and C^(2,alpha), respectively, for every alpha<1. They require precisely the full natural bounds in(1), not a differentiated asymptotic expansion. In particular

    div V=0, DV X=-LV, Delta P2=-tr((DV)^2),
    X.grad S=-2(1-c)S.                             (4)

No harmonic pressure addition remains: P2 is the limit normalized by Pinf. Choosing2/c-4<alpha<1 is possible and supplies exactly the root threshold in the confirmed natural-pressure removal theorem A1847-A1851. No C2 velocity-tail premise is added.

For globally zero-helicity profiles, A531 gives div(SW)=0. Since S is C1, W is continuous and div W=0, this is W.grad S=0 pointwise. A413 is the global C2 rank theorem under uniform sublinearity, which follows from(1). Its complete proof was reread. In its notation H=P+|U|^2/2+(Ax).U, G=(Ax+U).grad H=-a U.(Ax+U), a=1-2c, it gives dG wedge dH=0 on {curl U!=0}. As H-U.(Ax+U)=P-|U|^2/2, this is

    grad H cross grad(P-|U|^2/2)=0
                         on {curl U!=0}.           (5)

The theorem uses global helicity, complete recurrent vortex dynamics and C2 Sard; it is not a local conclusion from two first integrals. The later dense-set primitive part of A413 is unnecessary here.

The actual C1 convergence in(4)-(5) gives grad k cross grad S=0 wherever W!=0, as independently checked in A604. Indeed at a fixed point with W!=0, curl u_t=exp(t)exp(omega tJ)curl U(F_t x) is nonzero for all sufficiently large t. The scaled two scalar gradients then have zero cross product there, and their limits are grad k and grad S. Density on {S!=0} extends this identity by continuity only there. No extension across arbitrary open irrotational holes has been assumed.

## 3. Reduction of the three cases to tail vanishing

In I, equations(2),(4), k=0 and W.grad S=0 are exactly the global natural-pressure theorem poisson_ratio_removal_20261103, A1847-A1851. Its removal, exact potential and global-maximum Harnack proof gives V=S=P2=0. That theorem requires no original-profile helicity condition.

In II the preceding zero-helicity input gives W.grad S=0. Full rank and comparison activate global_rank_flux_20261103, A1866-A1871, at natural regularity. It first derives k=0 by zero annular flux, then gives V=S=P2=0. The excluded exponent1/3 is outside the present range. The stated density alternative gives the required rank precisely on S!=0.

In III, rotate and scale(3). At every fixed x in D and sufficiently large t it becomes

    r_-|p_t-|u_t|^2/2|<=|u_t|^2
                            <=r_+|p_t-|u_t|^2/2|.

Taking the locally uniform limit gives(2) everywhere on D with the same constants. It remains to derive full rank. Both original gradients in(5) are continuous, and exterior vorticity density extends(5) to the entire indicated exterior BEFORE taking a limit. Define R=P-|U|^2/2 and

    h_t=exp(at)[H(F_t x)-Pinf],
    r_t=exp(bt)[R(F_t x)-Pinf], b=2-2c.

The exact identities are

    h_t=X.u_t+exp(-t)(p_t+|u_t|^2/2)->k in C1_loc,
    r_t=p_t-|u_t|^2/2->S in C1_loc.                (6)

For every compact K in D, |F_t x|=exp(ct)|x| puts F_t K entirely in the exterior for all large t. The same invertible transpose F_t^T acts on both original gradients in the chain rule, up to nonzero scalar factors. Thus their linear dependence gives grad h_t cross grad r_t=0 on K. Passing to the C1 limit proves full rank on D. Case II now gives V=S=P2=0.

This establishes III without a false inference of density from uniform convergence. The stronger separately confirmed scattering-density equivalence is not needed.

## 4. Canonical pressure and the exact faithful-tail implication

The complete natural_tail_pressure_gradient_20261103 proof was reread. A516 uses full momentum and uniform decay to identify the actual canonical pressure gradient, then a Newtonian split at radius |x|/8. The near source tr((DU)^2)=O(r^(-2p-2)) and the remote stress ball integral O(r^(3-2p)) give

    |grad P|<=C r^(-2p-1), |P-Pinf|<=C r^(-2p).      (7)

The strict inequality2p<3 controls the stress ball integral. Radial integration and spherical arcs give the same Pinf in every direction. This input needs no zero helicity, symmetry or decay estimate for D2U. Arbitrary Poisson solutions would not suffice because a harmonic remainder would be uncontrolled; actual momentum is essential to the canonical identification.

Set q=2p+1>3 and N=DU U+grad P. Then |N|<=Cr^-q. The exact full equation gives, for every large fixed x,

    d/dt[exp(tL)U(F_t x)]=-exp(tL)N(F_t x).

Since L has scalar part1-c and skew part omega J,

    |exp(tL)N(F_t x)|<=C|x|^-q exp(((1-c)-cq)t)
                              =C|x|^-q exp(-t).

The bracket tends to the actual tail V(x), now zero. Integrating on0<=t<infinity yields

    U(x)=integral_0^infinity exp(tL)N(F_t x)dt,
    |U(x)|<=C|x|^-q.                               (8)

Only the complete explicit linear flow is used. This estimate concerns U itself; no derivative of an asymptotic remainder is taken. The compact core is bounded by C2 regularity, so(8) implies U in L2(R3).

## 5. Energy identity with all three vanishing boundary terms

Dot full momentum with U. Since div U=0, div X=3c, and (JU).U=0, the exact identity is

    (1-5c/2)|U|^2+
       div[(X+U)|U|^2/2+(P-Pinf)U]=0.             (9)

Take a smooth radial chi_R equal to1 on B_R, zero outside B_(2R), with |grad chi_R|<=C/R. The rotation part of X is tangent to every centered sphere, so (-omega Jx).grad chi_R=0 identically. The remaining linear-drift, cubic and pressure cutoff terms are bounded, using(7)-(8), by

    C R^(3-2q), C R^(2-3q), C R^(2-2p-q),

respectively. All exponents are strictly negative. Dominated convergence in the first term of(9) gives

    (1-5c/2) integral_R3 |U|^2=0.

The coefficient is nonzero since c>2/5, even though it is negative. Hence U=0 and momentum gives grad P=0. This completes all three profile conclusions, with finite energy proved rather than inserted as a premise. The calculation agrees with the full reread of A570 Section6.

## 6. Pressure constants and exact scope

The comparison(3) is invariant under P->P+C because Pinf changes by the same constant. Omitting Pinf would change its hypotheses. No sign of S or of P-Pinf is presumed, and the removal theorem allows arbitrary scalar zeros. All ratios are controlled by fixed global or exterior constants; merely pointwise finiteness is insufficient.

I does not infer original zero helicity from tail transport. II does not infer full rank from vortical rank across open irrotational regions. III extends rank in the ORIGINAL dense exterior before dilation. Its hypotheses are mutually incompatible because the forced U=0 violates its density premise; its nonexistence conclusion is still a valid conditional theorem.

The contrapositive says that a nonzero globally zero-helicity natural profile cannot satisfy both exterior vorticity density and(3). It is neither existence of such a profile nor a complete classification of ways the bare-decay conjecture might fail.

## 7. Verification and verdict

LIT269 cases I-III and the faithful-tail energy implication are CONFIRMED at the exact hypotheses above. All six submitted sections and seven independent sections were read. Dependencies A413, A516, A531, A533/A538/A539, A604, LIT267 and LIT268 retain their scopes; complete A413, pressure, direct rank transfer and A570 faithful-tail proofs were reread. The natural regularity dependencies were already fully reconstructed and checked, including their configured-model comparisons.

The canonical-pressure, full-gradient, global-helicity where stated, scalar comparison and full-rank or density assumptions remain visible. Bare-decay arbitrary-helicity nonexistence and local continuation under only bounded ratios remain OPEN. No computation, formal build or new model client was used. The submitted source and its hash are retained in the team records. Existing configured model agent exchanges supply model comparison; provider runtime is not independently attested.
