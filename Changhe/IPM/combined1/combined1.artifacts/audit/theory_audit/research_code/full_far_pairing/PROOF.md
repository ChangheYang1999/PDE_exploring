# Independent whole-plane pairings and finite-model errors

## Exact statement

Fix the independently verified canonical C1-N1-007 potential, with
c=4076476460239181/2251799813685248 and delta=1-1/c. Put t=r^2/(1+r^2),
v=1-t, rho=-partial_y Delta chi, psi=partial_xy chi and
u=(-partial_y psi,partial_x psi). The full residual is
F=(cX+u).grad rho-rho. For each integer K listed in the frozen N4
result, including K=0 and indices as large as10^10, define

    phi_K=r v^2 t^K sin(theta), I_K=int F phi_K.

This audit encloses I_K using independently reconstructed polar
background fields and integration by parts. It also encloses the
error of the finite q<=3, exponent>=-7 homogeneous first-sine model.
All statements concern this exact rational candidate and the specified
finite list of K. There is no claim about a uniform error for untested
indices, a maximizing index, a norm certificate, or an exact solution.

## Background fields and the weak identity

Use the audited polar field identities of ../weak_probe_audit/PROOF.md:

    rho=r sum_(j,n) v^a_j R_jn(t) sin(n theta),
    psi=r^2 sum_(j,m) v^a_j S_jm(t) sin(m theta),
    a_j=(j+1)delta/2,
    D_jm=(2-2a_j t)S_jm+2tv S'_jm.

Thus u_r=-r sum m v^a_j S_jm cos(m theta) and
u_theta=r sum v^a_j D_jm sin(m theta). The polynomials R,S are
reconstructed from the exact canonical potential, without reading
any peer residual projection or polynomial cache.

The probe is smooth at the origin. At infinity, it is O(r^-3) and
its gradient is O(r^-4), for each fixed K. The background and velocity
are O(r^gamma), gamma=1/c<1. Consequently the boundary integral of
rho phi_K(cX+u) vanishes at infinity: its linear part is O(r^(gamma-1))
and its nonlinear part is O(r^(2gamma-2)). The origin boundary also
vanishes by smoothness. Using div u=0 gives

    I_K=-int rho[(2c+1)phi_K+(cX+u).grad phi_K].          (1)

No numerical cutoff is needed. Define

    q_K=1-4t+2K v=q_0+2K v.

Then r partial_r phi_K=q_K phi_K, while the angular derivative
has cosine rather than sine and the same radial factor.

## Independent angular assembly

Angular orthogonality in the linear part of (1) gives the polynomial
contributions, with ell=j+1,

    A_ell += -R_j1[(2c+1)+c q_0],
    B_ell += -2c v R_j1.

The nonlinear part can contribute to sine1 only when |n-m|=1.
Put sigma=sign(n-m). Product-to-sum gives angular factor pi/2 and
therefore, at ell=j+k+2,

    A_ell += R_kn[sigma m S_jm q_0-D_jm]/2,
    B_ell += sigma m v R_kn S_jm.

All ordered stream/density pairs satisfying the condition are included.
With b_ell=ell delta/2>0 and r dr=dt/(2v^2), these formulas prove

    I_K=(pi/2) sum_ell int_0^1
         t^(K+1) v^(b_ell-1) [A_ell+K B_ell]dt.          (2)

This uses background fields and their first derivatives, independently
of the peer's Cartesian full-residual projection.

## An exact residual polynomial from the weak assembly

Every B_ell is divisible by v. Integrating its term in (2) by parts,
using K t^(K+1)=t partial_t(t^(K+1))-t^(K+1), gives

    P_ell=A_ell-2B_ell-t B'_ell
                     +(b_ell-1)t B_ell/v.               (3)

The quotient is an exact rational polynomial. The boundary term is
zero since b_ell>0 and K>=0. Formula (2) therefore also equals

    (pi/2) sum_ell int_0^1 t^(K+1) v^(b_ell-1) P_ell dt.  (4)

Moreover (3) is the first-sine residual polynomial: the angular
integration by parts that led to (2) applies to every smooth compactly
supported radial probe. The fundamental lemma for distributions then
identifies the smooth radial coefficients. Thus Pi_1 F is exactly
r sum_ell v^b_ell P_ell(t) sin(theta).

## Finite positive Beta recurrences

For a rational polynomial Q(t)=sum_i q_i t^i, the integrals in (2) or
(4) are finite sums q_i B(K+i+2,b). The starting value is
Gamma(K+2)Gamma(b)/Gamma(K+2+b), with all arguments positive, and

    B(K+i+3,b)/B(K+i+2,b)=(K+i+2)/(K+i+2+b).

Every recurrence step has a positive exact rational ratio. Arb balls
enclose all conversions, Gamma values, and operations. Large K is
only a scalar parameter. No polynomial of degree K is constructed.
Agreement between (2), (4), and both independently computed peer
endpoint formulas is required, as is more than150 relative bits in
each complete nonzero pairing.

## Exact finite model and its error

For r>1, put z=r^-2. The ell-th first-sine term is
r^(1-ell delta)(1+z)^(-b_ell)P_ell((1+z)^-1). Therefore its q-th
coefficient is

    a_(ell,q)=sum_i p_(ell,i) binom(-b_ell-i,q),
    e_(ell,q)=1-ell delta-2q.                            (5)

This convergent expansion is justified in ../omitted_far_sector/PROOF.md.
Retain only q<=3 and e>=-7, skipping exact zero coefficients. Compare
every retained exponent and coefficient exactly with the frozen peer
model, and separately compare the nonzero ell=1,q=4 coefficient.

The finite model pairing is

    J_K=(pi/2) sum a_(ell,q)
           B(K+(e_(ell,q)+3)/2,(1-e_(ell,q))/2),          (6)

whenever both arguments are positive, which is checked. Formula (6)
includes the artificial interior extension of the homogeneous model.
The ball I_K-J_K therefore encloses the actual global pairing error,
including the exterior truncation remainder and the interior difference.
For I_K nonzero, |I_K-J_K|/|I_K| is well-defined; the model cancellation
fraction is |J_K|/sum|its terms|. Each is compared with the peer result.
Their sizes alone do not provide a spatial convergence radius or an
error estimate for a different norm.

## Dependencies and verification scope

Only the independently audited canonical source and polar background
primitive are shared with earlier T4 calculations. The peer residual
cache is neither imported nor trusted by this computation. Proof,
code, canonical input, and frozen comparison files are hashed. A
successful independent comparison confirms only the listed pairings,
finite-model coefficients and corresponding error intervals.
