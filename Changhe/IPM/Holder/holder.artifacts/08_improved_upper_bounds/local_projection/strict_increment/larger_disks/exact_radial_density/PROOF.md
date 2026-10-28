# The exact radial minorant on the inscribed disks

## Statement and dependencies

Use the real or complex homogeneous Euclidean Holder seminorm [f]_alpha, 0<alpha<1, and the positive local projection measure

    mu_(R,beta)=Q_(R,beta)+(1/2-1/pi)delta_0

of mass1/2 from ../../../PROOF.md. The kernel and homogeneous extension are those of ../../../../../01_setup/PROOF.md. The two disks B(+(3R/4)n,R/4) and B(-(3R/4)n,R/4), where n is the negative kernel axis, lie in the support of Q; their exact containment was proved in ../PROOF.md and confirmed in the V195 manifest at ../radial_density/verification/accepted.json.

Set

    J_* = -31/32 + (27/8)log(4/3),
    K_* = -233/1024 + (405/512)log(4/3),
    p=alpha(1-alpha), q=p(2-alpha)(3-alpha).

For any increment length h>0 and R=s h with0<s<2, the proposed improved estimate is

    |mu_(R,beta)*f(x)-mu_(R,beta)*f(y)|
        <= [1/2-p J_* s^2-q K_* s^4] h^alpha [f]_alpha,     (1)
    |x-y|=h.

The gain is uniform in beta. Both J_* and K_* are positive and strictly exceed the corresponding J and K in the earlier radial-density proofs.

For the retained-cutoff construction J_D(alpha,rho) of the accepted finite-part proof, the proposed improvement, now for every0<rho<1/2, is

    D_alpha <= J_D(alpha,rho)
        -p[J_*rho^2-rho^4/(512(1-rho)^2)]
        -q[K_*rho^4-rho^6/(49152(1-rho)^2)].                (2)

Both bracketed quantities are positive throughout this entire radius interval. The proofs of the underlying local decomposition and retained-edge construction are unchanged; the new point is a larger reflection-invariant submeasure that remains positive after the cutoff loss.

## Exact minimization of the density on each circle

Scale R to1 and rotate a selected negative axis to the horizontal coordinate. Write c=3/4, t=|u| in[0,1/4] and v for the cosine of the angle between u and that axis. At a point z=c n+u the magnitude of the negative kernel density is

    (1/(2pi)) g_t(v),
    g_t(v)=[c^2+2ctv+t^2(2v^2-1)]/[c^2+2ctv+t^2]^2.

The negative sign of the lobe is fixed by disk containment; hence no absolute-value sign change occurs in this formula. Its denominator is positive since t<c. For0<t<=c/2, direct differentiation gives

    g_t'(v)=2t[-c^3+3ct^2+2t^3 v]/[c^2+2ctv+t^2]^3 <= 0,
    -1<=v<=1.

Indeed the numerator in square brackets is at most -c^3+3ct^2+2t^3, which increases with t>=0 and equals0 at t=c/2. Our selected disks have t<=1/4<c/2. Thus the minimum occurs at v=1, where

    g_t(1)=1/(c+t)^2.

The case t=0 is immediate. Restoring R, the exact largest radial density about each selected center that is pointwise below Q is therefore

    w_*(r)=1/[2pi R^2(3/4+r/R)^2],     0<=r<=R/4.          (3)

Equality at the outward point of each circle shows exactness of this radial minorant. The other disk has the same calculation by central symmetry. Formula(3) is strictly larger for r>0 than the previous radial lower density, which included the additional factor1-32(r/R)^2/9. That factor came from estimating numerator and denominator separately; their exact correlation makes it unnecessary.

## Symmetric reflection and its second and fourth moments

Remove the radial measure w_* from each disk and couple each to itself by reflection through the diameter perpendicular to the increment direction. The marginal measures remain identical. Leave the remaining positive measure and the atom in the translation coupling. These are finite positive measures, so no principal-value or infinite-mass issue occurs in this step.

As in the already confirmed symmetric-concavity and fourth-moment proofs, the reflected displacement divided by h is1-2u_parallel/h; its absolute value is positive because2|u_parallel|/h<=s/2<1. The even cost function satisfies

    [(1-v)^alpha+(1+v)^alpha]/2 <= 1-p v^2/2-q v^4/24,
    |v|<1.

This follows from its second and fourth derivatives and Jensen's inequality, as proved in ../radial_density/symmetric_concavity/fourth_moment/PROOF.md. Angular integration over two disks gives the saving

    p s^2 [2 integral_0^(1/4) t^3/(3/4+t)^2 dt]
      +q s^4 [(1/2) integral_0^(1/4) t^5/(3/4+t)^2 dt].

The two bracketed terms equal J_* and K_*, respectively. For verification, put c=3/4 and

    B_n=integral_0^(1/4) t^n/(c+t)^2 dt
       =(-c)^n(1/c-1)+n(-c)^(n-1)log(1/c)
         +sum_(j=2)^n binom(n,j)(-c)^(n-j)(1-c^(j-1))/(j-1).

Binomial expansion after the substitution u=c+t proves this identity. In particular

    B_3=-31/64+(27/16)log(4/3),
    B_5=-233/512+(405/256)log(4/3),
    J_*=2 B_3, K_*=B_5/2.

Their defining integrals prove positivity without relying on cancellation in the closed forms. Removing a strictly larger positive radial density increases both moments strictly. This proves(1), conditional only on the established disk containment and decomposition.

## The entire cutoff interval

The retained-edge proof in ../radial_density/cutoff_plan/PROOF.md shows that the Q translation density survives with at most the pointwise loss

    H=1/[2pi(1-rho)^2]

at either marginal. Its construction and marginal argument do not require rho<=1/3; that earlier restriction was used only to show positivity of the older radial lower density. On the selected disks at R=rho, formula(3) gives

    w_*(r)>=1/(2pi rho^2)>H,    0<rho<1/2.

Consequently the full positive radial density w_*-H survives on both disks throughout the admissible interval. Reflection preserves this density as well. Subtracting the constant-density second and fourth moments gives, exactly,

    4pi H integral_0^(rho/4) r^3 dr = rho^4/[512(1-rho)^2],
    pi H integral_0^(rho/4) r^5 dr = rho^6/[49152(1-rho)^2].

The resulting two moments are positive because w_*-H>0 on a disk of positive radius. Replacing those retained edges leaves every other edge and every residual estimate unchanged. This proves(2). It does not subtract a gain from edges already removed by another improvement.

## Scope and verification status

All earlier accepted bounds remain valid. This new proof is OPEN pending independent cross-read and has not yet been used to change a displayed decimal. A numerical update must verify the exact logarithm coefficients, use adverse certified base endpoints, and round the subtracted positive gain in the safe direction. No optimization over radial disk centers or over all possible transport plans is claimed; exactness here refers only to the radial minorant on these fixed disks.
