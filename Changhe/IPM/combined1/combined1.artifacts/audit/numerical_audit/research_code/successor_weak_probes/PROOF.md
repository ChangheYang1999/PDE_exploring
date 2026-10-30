# Frozen weak probes for successor candidates

## Statement and hypotheses

For each exact canonical candidate in the verification records, let c>1,
gamma=1/c, delta=1-gamma, rho=-partial_y Delta chi, and
u=(-partial_x partial_y^2 chi, partial_x^2 partial_y chi). The candidate
audits establish smoothness, div u=0, and rho,u=O(r^gamma) at infinity.
Let F=(cX+u).grad rho-rho. We test the exact frozen rational probes of
angular modes n=1 and n=7 specified by their source hashes.

Suppose h is a real L2(R2) correction at this fixed c whose canonical
velocity satisfies ||U[h]||2<=||h||2 and which solves

    F+div((cX+u)h)-(2c+1)h+U[h].grad rho+div(U[h]h)=0

in distributions. Put t=r2/(1+r2), v=1-t, and

    phi=r v2 P(t) sin(n theta),
    I=int_R2 F phi,
    M=||(2c+1)phi+(cX+u).grad phi||2,
    C=||phi grad rho||2,
    H>=||grad phi||infinity.

The polynomial P is rational and divisible by t^((n-1)/2). The source
records fix P and a positive rational H. Define

    R=2|I|/(M+C+sqrt((M+C)^2+4H|I|)).

Every such correction satisfies ||h||2>=R. The numerical task is to
enclose I,M,C,R outward, and give a rational strict lower bound for R,
separately for each candidate and probe. No candidate is an exact
solution, and these necessary distance bounds do not prove existence.

If only the linearized equation F+Lh=0 is imposed, the same argument
gives ||h||2>=|I|/(M+C). This is a necessary lower bound on any Newton
correction, conditional on its existence in this L2 class.

## Weak testing

The divisibility condition writes every term of phi as the imaginary
part of (x+iy)^n times an integer power of r2 divided by an integer
power of 1+r2. Thus phi is smooth. At infinity phi=O(r^-3) and
grad phi=O(r^-4). In particular M,C are in L2. Test the distributional
equation with phi times a smooth radial cutoff and let the cutoff
radius tend to infinity. The terms involving h and U[h] converge by
Cauchy-Schwarz, their quadratic product by L1 integrability, and the
cutoff errors vanish. This is the cutoff argument proved in
../angular_weak_probes/PROOF.md. Integration by parts then gives

    |I|<=(M+C)||h||2+H||h||2^2.

The right side increases on nonnegative arguments. Solving this
quadratic inequality proves the stated bound. Omitting the quadratic
term proves the conditional linearized bound.

## Two whole-plane pairing formulas

For each radial branch j, set alpha_j=(j+1)delta/2. The independently
differentiated canonical candidate has the exact finite expansions

    rho=r sum_(j,m) v^alpha_j R_(j,m)(t) sin(m theta),
    u_i=r sum_(j,m) v^alpha_j V_(i,j,m)(t) trig_m(theta),
    partial_i rho=sum_(j,m) v^alpha_j W_(i,j,m)(t) trig_m(theta).

All polynomials are rational. They are obtained from the original
radial derivative numerators by exact division by t2, whose zero
coefficients are checked. Frequencies and branches are retained.

First, project the full residual algebraically onto the single
sine mode n. In the derivative representation
S^p_j r^-3 P_(j,m)(t), where S=1+r2 and
p_j=(3+gamma-j delta)/2, its linear numerator is

    L_(j,m)=c[2tP'_(j,m)-3P_(j,m)
                    +2t(p_j P_(j,m)-tP'_(j,m))]-P_(j,m).

Retain m=n and divide this numerator by t2. In each nonlinear
Cartesian product use
cos(l theta)sin(m theta)
=[sin((m+l)theta)+sin((m-l)theta)]/2. Retain every pair with
m+l=n or |m-l|=n, with its correct sign. Sum these products at
branch ell=i+j+2 and divide by t4, checking exact divisibility.
The resulting projection is

    F_n=r sum_ell v^(ell delta/2) A_ell(t) sin(n theta).

Angular orthogonality and r dr=dt/(2v2) give

    I_direct=(pi/2) sum_ell int_0^1
                 t v^(ell delta/2-1) A_ell(t) P(t) dt.          (1)

Second, compute M as a signed field before taking its norm:

    Mfield=(2c+1)phi+(cX+u).grad phi
          =r v2 sum_(ell,m) v^(ell delta/2)
                         B_(ell,m)(t) sin(m theta).

Since F=div((cX+u)rho)-(2c+1)rho and div u=0,
integration by parts gives I=-int rho Mfield. The boundary integral
on a large circle is bounded by O(R^(gamma-1))+O(R^(2gamma-2)),
which vanishes because gamma<1. The products are integrable; the
origin has no boundary term by smoothness. Hence

    I_parts=-(pi/2) sum_(j,ell,m) int_0^1
              t v^((j+1+ell)delta/2-1)
              R_(j,m)(t) B_(ell,m)(t) dt.                    (2)

Only matching sine frequencies enter (2). Formula (1) differentiates
the residual and projects its nonlinear terms; formula (2) never
assembles the residual. Both include the full plane. Their Arb
enclosures must overlap with at least150 bits of relative accuracy.
There is no truncation of radial or angular integrals.

## Norm and gradient bounds

The Cartesian derivative formulas, product assembly, exact
Bernstein cover, and squared norm identities are proved in
../angular_probe_audit/PROOF.md. Briefly, with
Q=(1-4t)P+2tvP',

    partial_x phi=(v2/2)[(Q-nP)sin((n+1)theta)
                                      +(Q+nP)sin((n-1)theta)],
    partial_y phi=(v2/2)[(Q+nP)cos((n-1)theta)
                                      +(nP-Q)cos((n+1)theta)].

Multiply these by the exact Cartesian velocity for Mfield, and
multiply phi by the exact density derivatives for C. Check both
constructions at three rational Cartesian points against the direct
polar gradient and candidate jets.

For a field r v2 sum_(ell,m) v^(ell delta/2) B_(ell,m)(t) trig_m,
its squared L2 norm is

    (pi/2) sum_(ell,ell',matching m) int_0^1
        t v^(1+(ell+ell')delta/2) B_(ell,m)(t) B_(ell',m)(t) dt.

Every unequal radial pair appears twice. The two Cartesian C fields
are squared separately and added. This accounts for every mode.
The angular maximum of |grad phi| is v2 max(|Q|,n|P|).
An exact rational Bernstein subdivision bounds both polynomials
v2 Q and n v2 P on a finite dyadic tiling of [0,1]. Every accepted
leaf must have its maximum absolute control coefficient strictly
below the frozen H.

All integrals are finite sums of beta moments. After substituting
v=1-t, evaluate each moment
int_0^1 v^b(1-v)dv=1/((b+1)(b+2)), b>-1,
and its successive powers, using outward Arb arithmetic at2048 bits.
This avoids spatial quadrature. The implementation reuses the
audited beta recurrence and records its source hash.

## Verification, dependencies and scope

Candidate007 is a calibration: both new pairing paths, M,C and the
radius must overlap the previously independently confirmed mode1
and mode7 records. The other candidates use their own exact
canonical coefficients, not a copied007 field. Inputs, helpers,
proof and code are hashed in every result. Polynomial field hashes
and counts are recorded without large new coefficient caches.

Dependencies are the exact candidate canonicalization and sector
audits, ../radial_fourier/PROOF.md, the angular weak testing proof,
and the previously audited field, norm and Bernstein helpers.
Own successor results remain OPEN for independent peer reproduction.
Confirmation concerns these exact backgrounds and the stated
fixed-c correction class. It makes no statement about a larger
far-field chart or an inverse bound in another norm.
