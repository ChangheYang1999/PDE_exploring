# Global matrix positivity by compactified polynomial certificates

## Statement and inputs

Let rho_bar be either the state88 or state131 exact finite potential background reconstructed in `../source_audit/PROOF.md`. The canonical coefficient hashes are respectively

    3c2195906835db3f0207302ae1ef818e284fe3d60940bd0ecff72b79d0e63c3d
    4d80cf85ea1746d41c3fcfbdc622c74465cff5b9358e68614e521531ea78fb01.

Write c for the exact stored exponent, gamma=1/c, delta=1-gamma, and let

    rho_bar=-partial_y Delta chi,  psi_bar=partial_x partial_y chi,
    M=(2c+1)I+sym DU_bar+[[rho_bar,y,-rho_bar,x/2],[-rho_bar,x/2,0]].

Then, on the entire plane,

    M(X) >= (19/5) I.                                           (1)

This includes the origin, all axes and infinity. The proof uses rational polynomial identities and outward Arb enclosures at 256-bit precision. It does not use a numerical angular grid, a truncation at a finite radius, or a numerical derivative. The certificate is for the exact finite potential, not for an uncertainty neighborhood of its coefficients.

Consequently the generator-domain fixed-exponent operator in `FIXED_EXPONENT_INVERSE_PROOF.md` is bijective on the specified parity homogeneous H^-1 space and

    ||L_fix^(-1)|| <= 5/19.                                     (2)

The normalized operator, its growing rank column, and its scaling phase are not included in (2).

## Exact compactification

The potential is the finite sum

    chi=sum_(j,m,k) a_(j,m,k) r^(2k) (1+r²)^(p_j-k) cos(2m theta),
    p_j=(3+gamma-j delta)/2,  j=0,1,2,3,  m<=9,  m<=k<=26.

All a_(j,m,k), p_j and c are rational. Set

    t=r²/(1+r²),  z=cos(2theta),  w=(1-t)^(delta/2).

The first quadrant maps into 0<=t<1, -1<=z<=1. Matrix eigenvalues are unchanged by either coordinate reflection: diagonal entries are even in both variables, while the off-diagonal entry changes sign. It therefore suffices to cover this compact rectangle, with its continuous t=1 limit.

Consider a term after d Cartesian differentiations, represented as

    r^(2k-d) (1+r²)^(p_j-k) sum_l b_l t^l C_n(theta),

where C_n is a sine or cosine. For its l-th summand, radial differentiation r partial_r replaces its radial factor by

    [s+2u t] times that factor,
    s=2k-d+2l,  u=p_j-k-l.                                     (3)

The exact polar identities partial_x=cos(theta)partial_r-sin(theta)partial_theta/r and partial_y=sin(theta)partial_r+cos(theta)partial_theta/r then give the following recurrence. For an x derivative, the coefficients of frequency n+1 and n-1 at the same l are (s-n)/2 and (s+n)/2, and both receive u at l+1. For a y derivative of a cosine, these two coefficients belong to sine n+1 and sine n-1, with a minus sign on the latter, including its u term. For a y derivative of a sine, they belong to cosine n+1 and cosine n-1, with a minus sign on the former. Negative sine frequencies change sign; negative cosine frequencies do not.

Applying this recurrence four times gives the exact identity

    r^(2k-4) (1+r²)^(p_j-k) t^l
       = w^(j+1) t^(k-2+l).                                   (4)

The apparently negative t powers cancel exactly. The script checks this over the rationals. The resulting t degree is at most28 and the angular frequency at most22. Even cosine modes equal Chebyshev polynomials T_n(z). Even sine modes equal sqrt(1-z²) U_(n-1)(z) in the first quadrant. Thus there are exact bivariate rational polynomials P_(a,j), P_(b,j), P_(d,j), each of t degree at most28 and z degree at most11, such that

    M11=2c+1+sum_(j=0)^3 w^(j+1) P_(a,j)(t,z),
    M22=2c+1+sum_(j=0)^3 w^(j+1) P_(b,j)(t,z),
    M12=sqrt(1-z²) sum_(j=0)^3 w^(j+1) P_(d,j)(t,z).             (5)

Here the derivative identities are

    M11=2c+1-2chi_xxyy-chi_yyyy,
    M22=2c+1+chi_xxyy,  M12=chi_xxxy.

The recurrence and Chebyshev conversion are implemented in `verification/compact_matrix.py`. The rational polynomials are saved in `state*_compact_polynomials.json`. Six points per state also overlap independent Cartesian-jet enclosures, but those point checks are diagnostics rather than the proof of (4)-(5).

## Bernstein enclosure

For a degree-n polynomial in a variable on [l,h], its Bernstein coefficients are obtained from its monomials by

    T_(i,k)=sum_(q=0)^min(i,k)
               binom(k,q) l^(k-q) (h-l)^q binom(i,q)/binom(n,q).

This follows by expanding (l+(h-l)u)^k and using the exact monomial-to-Bernstein identity. The tensor product of the two transforms gives the coefficients on the (t,z) rectangle. Bernstein basis functions are nonnegative and sum to one, so a polynomial is bounded between the least and greatest coefficient. Matrix operations in Arb enclose the exact rational transformed coefficients.

The certificate subdivides either t or z at its exact rational midpoint. The left and right de Casteljau matrices are

    L_(i,k)=binom(i,k)/2^i for k<=i, and zero otherwise,
    R_(i,k)=binom(n-i,k-i)/2^(n-i) for k>=i, and zero otherwise.

These follow directly by restricting a Bernstein polynomial to [0,1/2] or [1/2,1]. Multiplying the coefficient matrix on the appropriate side gives valid child coefficients. No coefficients are re-fitted from samples.

On a leaf t in [t_l,t_h], w lies in the rigorously enclosed interval

    [(1-t_h)^(delta/2),(1-t_l)^(delta/2)].

At every tensor coefficient index, the sum over the four branches in (5) is a degree-four polynomial in w with zero constant term. Applying its degree-four Bernstein transform on that interval, and taking the hull over all three coefficient indices, bounds the complete branch sum. This treats w and t independently and hence may overestimate, but cannot omit any actual value with w=(1-t)^(delta/2). The fractional powers and all matrix operations are Arb ball operations.

Let [a_l,a_h], [b_l,b_h], [d_l,d_h] be the resulting entry corrections. Let s_* be the maximum of sqrt(1-z²) on the exact z interval. It equals1 when the interval contains0, and otherwise equals sqrt(1-min(|z_l|,|z_h|)²). Put D=s_* max(|d_l|,|d_h|). Gershgorin gives

    lambda_min(M) >= 2c+1+min(a_l,b_l)-D.                       (6)

A second valid bound is

    lambda_min(M) >= 2c+1+(a_l+b_l-sqrt(E²+4D²))/2,              (7)

where E bounds |a-b| on the product interval. The script takes the larger of (6) and (7), using an Arb lower comparison with the exact rational19/5. All comparisons must certify the inequality; an overlapping ball causes subdivision.

## Coverage and results

`verification/compact_certificate.py` starts from the full rectangle [0,1] times[-1,1]. An unresolved rectangle is replaced by exactly its two midpoint children. A leaf is accepted only after its lower bound exceeds19/5. The completed files contain255 accepted leaves for state88 and244 for state131, no failed leaves, and no pending leaves. `verification/audit_compact_certificate.py` separately checks the entire path tree, exact rational boxes, lower bounds, input hashes, polynomial degrees, and origin identities.

The smallest recorded leaf bounds are enclosed by

    state88: [3.8001018415565253483601888810652192222248646839830 +/- 2.43e-50],
    state131:[3.8006422634536009742242947253497744823137700534244 +/- 2.74e-50].

Only the common rational bound19/5 is claimed in (1). The observed pointwise infimum c+2 is not claimed to be the exact global infimum. The t=1 edge has w=0 and M=(2c+1)I; the origin is included by continuity and is additionally checked by exact rational identities.

## Scope and dependencies

Dependencies are the source reconstruction, canonical potential formulas, and energy identity proved in the neighboring notes. The machine calculation consists of finitely many rational transformations and Arb-certified arithmetic. All coefficients and accepted boxes are saved, and both states can be reproduced locally without external data or any server. The formal finite-family exclusion remains applicable: matrix positivity does not make either finite background an exact profile.
