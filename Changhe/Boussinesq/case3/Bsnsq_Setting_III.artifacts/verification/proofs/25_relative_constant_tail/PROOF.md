# Constant relative velocity and noninteger endpoint powers

Status: an exact manufactured inverse and conditional far-field algebra. This does not establish that every B2 profile has a nonzero constant in its relative-velocity expansion. It does show that center normalization and the canonical relative inverse do not generally remove such a constant. A pure integer-power compactified tail can omit its transport correction.

## 1. Exact smooth inverse with a constant term at infinity

Fix beta>2, q=1/beta, a=(1-q)/2, c=1+beta/2, and

    d0=(-4/beta-8a)/6,
    s=x^2+y^2, P=cxy+d0 x^3,
    Psi_rel=x[(1+s)^a-1]+P exp(-s),
    V=(-Psi_rel_y,Psi_rel_x), Omega=-Delta Psi_rel.

All fields are smooth and have the B2 x parity, with V(0)=0. Direct differentiation gives

    Omega=-x[8a(1+s)^(a-1)+4s a(a-1)(1+s)^(a-2)]
          -exp(-s)[6d0 x+(4s-12)cxy+(4s-16)d0 x^3].

Thus Omega_x(0)=-8a-6d0=4/beta and Psi_rel_xy(0)=c. These are the two nontrivial center relations for the normalization a0=1. No temperature satisfying the complete system is asserted.

Since Omega=O(r^(-q)) and V=O(r^(1-q))=o(r), the absolutely convergent once-subtracted full-plane inverse equals V. Indeed it has the same divergence and curl; their difference is entire harmonic and sublinear, hence constant, and is zero at the origin. No harmonic strain or free drift has been inserted in the relative field.

Writing X=r(cos theta,sin theta),

    Psi_rel=r^(2-q)cos theta-x+O(r^(-q)),
    V=r^(1-q) v1(theta)+C+O(r^(-1-q)), C=(0,-1),
    v1=(-(1-q)cos theta sin theta,1+(1-q)cos^2 theta),
    Omega=-(1-q)(3-q)r^(-q)cos theta+O(r^(-q-2)).

The Gaussian core has exponentially small far field. The constant C survives because the canonical relative field subtracts its value at the origin. Adding a uniform observer velocity to an absolute representative changes U and U(0) equally, so it does not change V or C. Thus C is not a free fitted drift.

## 2. Conditional transport expansion

This section concerns formal coefficients of a differentiably valid asymptotic expansion. It does not infer such an expansion from pointwise decay alone. Suppose beta is not an integer and the relative velocity has an expansion in homogeneous terms of degrees 1-kq for integer k, together with a constant C. Suppose ordinary leading transported fields are

    Theta0=r^m b(theta), m=1-2q,
    Omega1=r^(-q) a1(theta).

For the ordinary integer ladder write Theta_j of degree m-jq, j>=0; Omega_j of degree -jq, j>=1; and U_j of degree 1-jq. Collecting equal degrees in the profile equations gives

    Theta_j=(1/j) sum_(l+k=j, l>=1,k>=0) U_l.grad Theta_k, j>=1,
    Omega_j=(1/(j-1))[sum_(l+k=j,l,k>=1) U_l.grad Omega_k
                       -partial_x Theta_(j-2)], j>=2.

The signs and denominators follow from beta X.grad-(beta-2) acting on Theta_j as -j, and beta X.grad+1 acting on Omega_j as 1-j. These identities do not include logarithms at resonant Poisson exponents; research/19 records that separate limitation.

The constant C adds terms of degrees m-1 and -q-1. When these degrees do not coincide with another term already present, their required coefficients are

    Theta_C=(1/beta) C.grad Theta0,
    Omega_C=(1/beta) C.grad Omega1.                         (1)

For example, beta X.grad-(beta-2) acts on Theta_C as -beta, which cancels C.grad Theta0. The vorticity operator acts on Omega_C as -beta. Terms coupling C to higher integer-ladder terms occur at later orders. Formula(1) is exactly the first-order translation expansion of a homogeneous field evaluated at X+C/beta. Such a translation does not preserve the prescribed marked center, so it cannot be silently used to erase these terms.

For a vertical C and b(theta)=cos^2 theta,

    partial_y Theta0=(m-2)r^(m-1)sin theta cos^2 theta,

which is nonzero. Its odd-in-y correction is permitted by Setting B2. There is no general y symmetry forcing it to vanish.

## 3. Consequence for the r2 compactification

Consider the finite endpoint representation used in the numerics lane:

    z=1-t=(L^2/(r^2+L^2))^(1/(2 beta)),
    F=z^(beta+2) times a polynomial in z on the last knot interval,
    G=z^(beta+1) times a polynomial in z,

with odd angular modes multiplied by sqrt(1-z^(2 beta)). Polynomial endpoint factors and this square root generate relative radial corrections r^(-j/beta-2n), with nonnegative integers j,n. Multiplication by the exterior factors x^2 or x gives the corresponding Theta and Omega families. This is an asymptotic statement about a finite spline representation, not about limits of refining spline spaces.

At beta=5/2 the relative order r^(-1), equivalently z^(5/2), is absent: j/beta+2n=1 would require j+5n=5/2. The drift correction(1), if nonzero, therefore cannot be represented exactly on the final knot interval by this family. In contrast beta=3 permits the order through j=3. At noninteger beta a z^beta term has finite endpoint differentiability even though the physical field may be smooth at every finite radius. The precise obstruction here is the finite family of generated endpoint exponents. It is not a claim that every factor of this representation is smooth to all orders at the artificial infinity endpoint for every beta. Requiring such endpoint smoothness would itself be an extra restriction, since physical smoothness concerns finite radii.

This observation does not prevent approximate convergence on expanding finite domains. Nor does it imply a nonzero asymptotic residual limit, because the omitted term is subleading. It warns that a convergence study must test the actual outer remainder, rather than assume an integer endpoint ladder is exhaustive. The manufactured inverse in section1 proves only that a nonzero constant is compatible with the canonical law and center identities. Whether it occurs for any converged coupled candidate remains an empirical and analytic check.

Dependencies: explicit differentiation, the subtracted Biot-Savart uniqueness argument, Euler's identity for homogeneous functions, and finite endpoint polynomial expansion. No numerical evidence is used as proof and no B2 candidate is claimed.
