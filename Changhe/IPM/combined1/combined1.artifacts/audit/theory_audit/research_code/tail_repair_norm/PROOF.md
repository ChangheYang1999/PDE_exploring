# L2 norm of the particular global polynomial tail repair

## Statement

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
t=r^2/(1+r^2) and p=2gamma. For each reference007,013,014 use its exact
forty coefficients A1_m in data. Define

    chi_eta=-(1+r^2)^p sum_(m=0)^39 A1_m t^(m+4)(1-t)cos(2m theta),
    eta=-partial_y Delta chi_eta.

The assertion under audit is Opus R1-034's claim ||eta||_2>4373.34 for
each of these three exact repairs. It concerns this specific global
polynomial repair only. The alternative in ../far_out_tail_repair/PROOF.md
has a different radial shape; no lower bound for all tail repairs is
inferred here.

## Complete norm calculation

The polar derivative formulas in ../weak_probe_audit/PROOF.md transform
the exact finite potential to

    eta(r,theta)=r (1-t)^(2delta) sum_(n odd) D_n(t)sin(n theta).

They are independently implemented there from the Euler radial
operator and trigonometric product identities. The cancellation of
the leading branch coefficient implies D_n(1)=0 exactly. This is
checked by exact polynomial division, D_n(t)=(1-t)E_n(t).
Orthogonality gives int_0^(2pi)sin(n theta)sin(m theta)dtheta=pi delta_nm.
Since r^2=t/(1-t) and r dr=dt/[2(1-t)^2],

    ||eta||_2^2=(pi/2) sum_n int_0^1 t(1-t)^(4delta-1) E_n(t)^2 dt.    (1)

The exponent b=4delta-1 is greater than-1. There are finitely many
polynomials, hence the entire integral is absolutely convergent.
Writing E_n^2=sum_j a_(n,j)t^j, each integral is the complete finite sum

    sum_j a_(n,j) B(j+2,b+1).

The Beta values are rational for rational b and integral j, with
B(2,b+1)=1/[(b+1)(b+2)] and recurrence
B(j+3,b+1)=B(j+2,b+1)(j+2)/(j+b+3).
The checker forms polynomial squares exactly and sums their rational
coefficients against outward Arb enclosures of these exact Beta values.
It verifies positivity, sufficient relative accuracy and overlap with
every Opus enclosure. This yields a rigorous full-plane norm; no mesh,
truncation or asymptotic substitution occurs in (1).

## Dependencies and scope

The source JSON files are copied from the accepted exact tail-repair
construction and hash-bound. The own polar differentiation helper and
the independent peer output are separately hash-bound. This verifies a
new numerical claim from the peer review. It does not prove the new
reference is closer to a stationary profile, nor that its residual is
small, nor that an inverse exists there.
