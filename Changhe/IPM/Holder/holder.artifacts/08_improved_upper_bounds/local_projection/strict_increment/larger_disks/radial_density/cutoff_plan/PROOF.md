# A strict saving in the perturbed diagonal cutoff plan

## Statement

Use 0<alpha<1, the homogeneous Euclidean Holder seminorm and the real or complex scalar diagonal transform R_1^2=T_xx-I/2. Its quotient extension and circular principal-value conventions are those of the setup. Define, for 0<rho<=1/3,

    A(alpha)=Gamma((alpha+2)/2)/(2 sqrt(pi) Gamma((alpha+3)/2)),
    E(rho)=-log(1-rho^2)/2,
    N0(rho)=1/2-(2/pi)log(rho),
    L(rho)=max{-log(1-2rho),(1+2rho)log(1+2rho)},
    B_D(rho)=3rho^2/[4(1-rho)^2] [-log(rho)+log2+2/3],
    T(alpha)=(2^(alpha+1)/pi)alpha[1/(1-alpha)+1/2-log(3/2)],
    J_D(alpha,rho)=2A(alpha)rho^alpha/alpha+1/2+2^alpha N0(rho)
                   +(2^alpha-1)E(rho)+T(alpha)
                   +alpha[B_D(rho)+3E(rho)L(rho)],
    J=653/288-(63/8)log(4/3),
    eta_cut(alpha,rho)=alpha(1-alpha)(1+rho/2)^(alpha-2)
                        [J rho^2-rho^4/(512(1-rho)^2)].

The proposed bound is

    D_alpha <= J_D(alpha,rho)-eta_cut(alpha,rho),
    eta_cut(alpha,rho)>0.

It is uniform in the kernel phase used to estimate arbitrary increments. The finite perturbation plan proving the old J_D inequality is in ../../../../../explicit_second_term/linear_remainder/PROOF.md; the radial-density coupling is in ../PROOF.md. This note is OPEN until independently cross-read. No numerical endpoint is asserted.

## Why the original strict saving cannot simply be subtracted

Normalize the output increment to length1 and take the local disk radiusR=rho. The old unperturbed local diagonal plan contains Q_rho translation edges of length1 and the remaining identity atom. The J_D proof then removes source and target deficiencies caused by the cross kernels, and replaces the remaining signed residual by an antipodal plan. A strict saving for the full Q_rho coupling is therefore not automatically a saving for this perturbed plan: some of those edges can have been removed.

We instead extract a guaranteed surviving radial measure from the retained translation edges after the old modification. The old J_D proof, including all its logarithmic error bounds and finite-part cancellation, then remains applicable without change.

## A submeasure that survives the perturbation

The absolute cross-kernel density on either radius-rho pole disk is bounded by

    H=1/[2pi(1-rho)^2].

Let z denote the relative coordinate indexing a Q_rho translation edge. Its original density is q(z). At its source and target, the corresponding positive and negative full old marginal densities are at least q(z), since this edge is one positive component of each marginal. The finite perturbation changes either marginal density by at mostH. Consequently its source and target deficiency fractions are at mostH/q(z) wherever q(z)>0. The old modification retains the minimum of the two available fractions, and hence retains translation-edge density at least

    q(z)-H,

provided the latter is nonnegative. This argument only uses a lower bound on the full marginal density; it does not assume the Q edges are the entire marginal. Atoms are unchanged and play no role here.

Inside each of the two disks of radiusrho/4 centered at distance3rho/4 on the two negative kernel axes, the larger-disk theorem gives support containment. With t=|u|/rho measured from the selected disk center, the radial-density theorem gives

    q(z) >= w_rho(|u|)
      = [1-(32/9)t^2]/[2pi rho^2(3/4+t)^2],  0<=t<=1/4,
    w_rho(|u|) >= 7/(18pi rho^2).

Forrho<=1/3,

    H / [7/(18pi rho^2)]
       = 9rho^2/[7(1-rho)^2] <= 9/28 < 1.

Thus w_rho(|u|)-H is a nonnegative radial density and is dominated by the retained translation-edge density on each disk. Remove exactly this subplan from the already perturbed plan. Its source and target marginals are the translates of the same radial measure. Replace its translation coupling by reflection through the line through the disk center perpendicular to the increment direction. Radial symmetry preserves both marginals exactly; all remaining flows are unchanged and positive. The reflected coupling has finite cost and changes no principal-value normalization.

## Computing the surviving saving

Apply the same quantitative concavity estimate as in the radial-density proof. The transport distance is1-2u_parallel, between1-rho/2 and1+rho/2. The two-disk saving is at least

    alpha(1-alpha)(1+rho/2)^(alpha-2)
      * 4pi integral_0^(rho/4) r^3 [w_rho(r)-H] dr.

The radial-density proof evaluates the first part as J rho^2. The constant part is

    4pi H integral_0^(rho/4) r^3 dr
       = pi H (rho/4)^4 = rho^4/[512(1-rho)^2].

This is eta_cut(alpha,rho). The old perturbed plan has cost at most J_D(alpha,rho); the new one has the same signed marginals and reduces its cost by at least eta_cut. The integral acts on every Holder input, and gives the stated operator bound.

Finally J>7/4608 by the positive-integrand comparison in the parent note. Since rho/(1-rho)<=1/2,

    J-rho^2/[512(1-rho)^2]
       > 7/4608-1/2048 = 19/18432 >0.

Thus the gain is strictly positive at every admitted exponent and radius. All identity terms are kept in the unchanged plan. This proof was written before applying the saving to any rational cutoff certificate.
