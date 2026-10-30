# Independent polar reproduction of the successor dyadic tests

## Statement and scope

Fix an exact single-scale S1 campaign potential chi at rational
c=4076476460239181/2251799813685248, and put delta=1-1/c. The source
canonical hash is checked against the immutable numerical audit. Define
rho=-partial_y Delta chi, psi=partial_x partial_y chi,
U=(-partial_y psi,partial_x psi), and F=(cX+U).grad rho-rho.
For S={1,3,7} and a>=0 define

    J_S(a)^2=sum_(n in S) integral (1+r^2)^(2-a)
                                      |Delta Pi_n F|^2 dX.

Here Pi_n is the full-circle sine projection. The scalar quantity is a
lower bound on the full weighted Laplacian norm; it is not an upper
bound and discards no contributing input mode.

Under all realization, domain, input, dyadic partition and absorption
hypotheses of the audited T4-146 origin inverse theorem, and provided

    1<c<2, chi_xxyy(0)=1-c, rho_y(0)>=5c-4,

the registered scheme requires

    5^((a-2)/2) J_S(a)
       < H(c-1)(1+c-ca)/(1+a),  0<a<1+1/c,             (1)

where H(d)=max_(0<s<d)(d-s)sqrt(4pi s(1+s)). An independently certified
strict violation on every cell excludes that sufficient scheme for
0<a<2 and0<s<1 at every fixed finite weight radius. It does not prove
nonexistence in other spaces or failure of other inverse theorems.
The continuous norm and inverse-floor proofs are in
../origin_dyadic_inverse/PROOF.md and its frozen Opus reviews. This note
supplies the independent finite-polynomial and arithmetic application.

## Polar construction independent of the peer fields

Let t=r^2/(1+r^2), v=1-t, a_j=(j+1)delta/2. Differentiate the original
potential polynomials to obtain

    rho=r sum_(j,n) v^a_j R_(j,n)(t) sin(n theta),
    psi=r^2 sum_(j,m) v^a_j S_(j,m)(t) sin(m theta).

The canonical conversion is proved in ../weak_probe_audit/PROOF.md.
Write T_(a,k)P=(k-2at)P+2t(1-t)P'. The polar velocity components of
one stream term are -r v^a mS cos(m theta) and
r v^a T_(a,2)S sin(m theta). The radial and angular density derivatives
are v^b T_(b,1)R sin(n theta) and v^b nR cos(n theta).

For selected output mode q, its residual polynomial with branch label
ell receives the following exact contributions:

    ell=j+1: c T_(a_j,1) R_(j,q)-R_(j,q);
    ell=i+j+2, n+m=q:
        [n R T_(a_j,2)S-m S T_(a_i,1)R]/2;
    ell=i+j+2, |n-m|=q:
        -sign(n-m)[n R T_(a_j,2)S+m S T_(a_i,1)R]/2.

These follow by multiplying the two polar components and using the
sine-cosine product identities. The loop retains every stream-density
pair satisfying either condition. Thus
Pi_q F=r sum_ell v^(ell delta/2) P_(ell,q)(t) sin(q theta)
is exact, with no quadrature or residual projection input from the peer.

## Laplacian, endpoint cancellation and whole-plane moments

For d=ell delta/2, apply r partial_r twice and subtract q^2. Exact
polynomial division must give

    T_(d,1)(T_(d,1)P)-q^2 P=t L.

Then Delta Pi_q F=r sum_ell v^(d+1)L_(ell,q)(t)sin(q theta).
For each nonzero L(1-v), let k_ell be its exact first nonzero power.
The diagonal integrability condition at a=0 is

    ell delta+2 k_ell-2>0.                            (2)

This ensures each branch belongs to the normed space, hence every
cross term is integrable by Cauchy-Schwarz. It is checked before any
floating conversion. Squaring the entire sum gives

    J_{q}(a)^2=(pi/2) sum_(ell,k) integral_0^1
        v^(a+(ell+k)delta/2-3)(1-v)L_ell(1-v)L_k(1-v)dv.

All products and cancellations are performed over the rationals, and
unordered off-diagonal pairs get multiplicity2. Each resulting monomial
integrates to its exact rational coefficient divided by a positive
affine rational expression in a. Only the final scalar sum and pi use
2048-bit outward ball arithmetic. This covers v=0, spatial infinity,
without truncation. Angular orthogonality then sums the three squared
mode norms.

## Seven-cell proof and comparison

Put d=c-1, A=1+1/c. Differentiation of (d-s)^2 s(1+s) gives
(d-s)[d+(2d-3)s-4s^2], so the unique positive maximum is at

    s*=(2d-3+sqrt((2d-3)^2+16d))/8.

Evaluate H(d) there with outward arithmetic. J_S(a) decreases in a,
5^((a-2)/2) increases, and (1+c-ca)/(1+a) decreases. On each cell[l,h],
any e>=h therefore satisfies

    left side of(1)>=5^((l-2)/2)J_S(e),
    right side of(1)<=H(d)(1+c-cl)/(1+l).

Use endpoints0,1/4,...,3/2,A, with e=h except e=7/4 on the final cell.
A strict positive difference of the two containing balls proves failure
throughout the cell. For A<=a<2 the required positive far-field rate
already fails. No finite grid is mistaken for a continuous cover.

The checker compares all24 independent mode norms with the peer's
frozen records, and all seven lower, upper, gap and ratio balls. Input
and helper hashes bind each write-once result. Agreement is a check of
the numerical implementation, while the displayed construction gives
the independent mathematical derivation. The peer uses Cartesian
field products and outward polynomial products; this reproduction uses
polar stream products and exact rational polynomial products.
