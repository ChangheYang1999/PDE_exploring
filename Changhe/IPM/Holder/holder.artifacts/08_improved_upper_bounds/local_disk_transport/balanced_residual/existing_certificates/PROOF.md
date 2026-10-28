# Replacing the residual in an accepted local-circle certificate

## Statement and conventions

For real functions on R^2 and 0<a<1, let

    [f]_a = sup_(z!=w) |f(z)-f(w)|/|z-w|^a.

The operators T_xx and T_xy have circular principal-value kernels
cos(2theta)/(2 pi r^2) and sin(2theta)/(2 pi r^2), respectively, and
are extended to the homogeneous Holder space modulo constants by
convergent increments. Their common real operator seminorm is C_a.
Fix delta=1/64, radial endpoints

    r_k=delta+(1/2-delta)k/256,  0<=k<=256,

and phases phi_j=j pi/32, 0<=j<=16. Use the accepted paired local-circle
construction of ../../../paired_local_circles/PROOF.md, with 512 angular
cells on each circle and exact mass unit U=2^44.

For row k and phase j, let m_(k,j,l), 0<=l<512, be the signed integer
angular masses extracted by that construction from the right pole.
The corresponding left masses are their negative central reflections.
Let v_(k,j) be the certified angular total-variation upper bound before
extraction. Define the following real quantities:

    E_(k,j) = log(r_(k+1)/r_k) sum_l m_(k,j,l)/U,
    V_(k,j) = log(r_(k+1)/r_k)
                  [v_(k,j)-sum_l |m_(k,j,l)|/U],
    q_(k,j) = -cos(phi_j)(r_(k+1)^2-r_k^2)/2-E_(k,j).

Here V_(k,j)>=0 and it bounds the right unextracted residual variation.
The residual has signed mass exactly q_(k,j). Suppose outward arithmetic
supplies upper bounds Vhat_(k,j)>=V_(k,j) and Qhat_(k,j)>=|q_(k,j)|.
Set

    B_(k,j)(a) = Vhat_(k,j)(2r_(k+1))^a
       + min(Vhat_(k,j),Qhat_(k,j))
             [(1+2r_(k+1))^a-(2r_(k+1))^a].             (1)

For each phase j, let [L_j^-,L_j^+] be the accepted enclosure of the
local extracted-transport cost plus the former residual cost, summed
over all radial rows. Let [R_j^-,R_j^+] be its separately stored former
residual enclosure. Let M_j and F_j be valid upper bounds for the middle
and exterior regions from the same accepted certificate. Then

    C_a <= S_a + sec(pi/64) max_(0<=j<=16)
           [L_j^+-R_j^-+sum_k B_(k,j)(a)+M_j+F_j],    (2)

where

    S_a = 2^(2+a/2) delta^a/[pi a(a+2)]
            +(1+2delta)^a delta^2/[2(1-delta)^2].      (3)

The same bound holds for [T_xx f]_a/[f]_a and [T_xy f]_a. The statement
requires identity of the extracted integer masses with those underlying
the accepted transport costs. It does not follow merely from similarity
of the reported decimal numbers. No claim about R_1^2 or any improved
numerical endpoint is made here.

## Proof

For the normalized output increment between x=(1/2,0) and y=-x, the
right local density for T_phi=cos(phi)T_xx+sin(phi)T_xy is

    w(r,theta)=[cos(2theta-phi)
             -r^2 Re(exp(i phi)/(1+r exp(i theta))^2)]/(2 pi)

against dtheta dr/r. The extraction bounds are uniform throughout each
radial bin. Therefore its removed right mass in that bin is exactly E,
and its removed variation is log(r_(k+1)/r_k) sum_l|m_l|/U. Subtraction
from the upper variation v gives V. The holomorphic mean-value identity
for (1+z)^(-2) on |z|<1 gives the stated formula for q, as proved in the
parent balanced-residual theorem ../PROOF.md.

The remaining right measure is supported in B(x,r_(k+1)). Its negative
central reflection is the remaining left measure. The parent theorem,
applied with s=r_(k+1), bounds the residual pair by B_(k,j)(a)[f]_a.
Summing over the 256 bins gives the new phase residual cost.

Write P_j for the unchanged extracted-transport cost and R_j for the
former residual cost represented in the accepted interval certificate.
Its independent enclosures give P_j+R_j<=L_j^+ and R_j>=R_j^-, hence
P_j<=L_j^+-R_j^-. Every extracted coupling and its exact integer
marginals is retained. Replacing only the unextracted coupling therefore
gives the local phase cost in (2).

The omitted disks of radius delta contribute at most S_a[f]_a by the
accepted small-disk estimate. This term is uniform in phase and is
separated before interpolation. The middle and exterior contributions
are unchanged. The phase interpolation argument in the paired-circle
proof multiplies the maximum of the other 17 phase costs by sec(pi/64).
It applies because each normalized increment is the scalar product of
a fixed real two-vector with (cos(phi),sin(phi)); each vector direction
is within pi/64 of a sampled direction after the established reflection
symmetries. This proves (2). Circular cancellation at the poles and the
convergent increment at infinity are supplied by the same accepted
completion theorem. No new limiting operation is introduced.

## Certificate requirements and scope

Before numerical use, verify the original sources and all accepted
input hashes, exact coverage of radial rows and phases, and the original
extraction algorithm and precision. Replay the deterministic angular
extraction with its identical source and parameters. Preserve the exact
integer sums and absolute sums for every row and phase, and independently
check the reconstructed old residual enclosures against all source
chunks. Evaluate q and (1) outward, and subtract the *lower* endpoint of
the original stored residual in (2). Round the final upper bound upward.

All ten exponents in the current table use the same angular and radial
geometry, independent of a. Their extracted transport plans and powers
can differ, but the angular mass extraction does not. A single verified
mass replay can therefore support all ten recombinations. The present
proof precedes that replay. Its analytic parent awaits independent lead
cross-read, and no numerical value is accepted by this document alone.
