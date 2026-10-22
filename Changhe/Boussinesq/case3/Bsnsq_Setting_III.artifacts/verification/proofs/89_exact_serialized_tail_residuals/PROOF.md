# Exact far-field residual coefficients of the serialized spline fields

Date: 2026-10-20. Status: independent complete informal derivation, written before computation. This is an audit of finite representations, not a theorem excluding the unrestricted B2 class.

## 1. Representation and statement

Let b>2 be the basis exponent, beta>=2 the separate PDE exponent, L>0 the map scale, s=1/b, m=1-2s and k=2-s. Set

    t=1-(1+r^2/L^2)^(-1/(2b)), eta=-sin(theta).

The stored fields are Theta=x^2 F and Omega=xG, where F and G are finite cosine sums in phi=theta+pi/2. Their radial factors are (1-t)^(b+2) and (1-t)^(b+1), respectively. Odd angular indices also have the smooth factor r/sqrt(L^2+r^2). A finite clamped spline multiplies each mode. Let C_F,j and C_G,j be its endpoint value (j=0) and first derivative (j=1) at t=1. Define real angular polynomials

    H_j=cos(theta)^2 sum_n C_F,j,n T_n(-sin(theta)),
    A_j=cos(theta)   sum_n C_G,j,n T_n(-sin(theta)).       (1)

Here T_n is the ordinary Chebyshev polynomial, equivalently cos(n phi). The velocity source may be Omega itself or a specified linear combination of stored vorticities using the same b,L and representation. Denote its leading angular polynomial by A_S. Let F_S be the unique periodic solution

    -(F_S''+k^2 F_S)=A_S.                              (2)

It exists uniquely because 3/2<k<2 is not an integer. Its Fourier coefficient at frequency n is (A_S)_n/(n^2-k^2). There is no free harmonic strain. Define

    E_T=(3 beta s-2)H_1 + L(k F_S H_0'-m F_S' H_0),
    E_O=(2 beta s-1)A_1 + L(k F_S A_0'+s F_S' A_0)
                           -m cos(theta)H_0+sin(theta)H_0'. (3)

For the canonical centered full-plane velocity of that specified source, the actual Cartesian residuals satisfy, uniformly with their fixed finite angular derivatives,

    R_Theta=2(1-beta s)L^(1+2s) r^m H_0
                       +L^(1+3s)r^(m-s)E_T+O(r^(m-2s)),
    R_Omega=(1-beta s)L^(1+s)r^(-s)A_0
                       +L^(1+2s)r^(-2s)E_O+O(r^(-3s)). (4)

Consequences are exact statements about this represented continuation to infinity:

1. If beta!=b and H_0 is not identically zero, sup_R2 |R_Theta| is infinite because m>0. This holds for either of the specified velocity sources. It is stronger than a finite-grid rejection, but says nothing about profiles outside this basis.
2. If beta=b>3 and E_T is not identically zero, the same supremum is infinite, since m-s=1-3/b>0. At beta=b=3 the residual instead tends to L^(1+3s)E_T, which need not be small. At 2<b<3 this term decays; no divergence is inferred.
3. Nonzero coefficients in (4) prove failure of the exact PDE for that stored field. They supply no lower bound on an arbitrary approximation sequence and no nonexistence conclusion for the original problem.

## 2. Complete derivation

Write z=1-t. Then

    z=L^s r^(-s)(1+O(r^-2)),
    C(1-z)=C(1)-z C'(1)+O(z^2).

The latter Taylor expansion holds on the final polynomial spline interval and is differentiable to every order there. The odd-index prefactor is 1+O(r^-2). Since 2>s, it does not affect either displayed term. Thus

    Theta=L^(1+2s)r^m H_0-L^(1+3s)r^(m-s)H_1+O(r^(m-2s)),
    Omega=L^(1+s)r^(-s)A_0-L^(1+2s)r^(-2s)A_1+O(r^(-3s)). (5)

The corresponding source expansion has first coefficient L^(1+s)A_S. The regular whole-plane modal Green formulas, or the centered relative kernel with the source split into its leading homogeneous tail and a faster remainder, give

    V=L^(1+s)r^(1-s)(-F_S' e_r+k F_S e_theta)+o(r^(1-s)). (6)

The scalar remainders in (5) obey these big-O estimates after any fixed number of r partial_r and angular derivatives: they arise from a finite polynomial on the final spline cell and explicit smooth radial envelopes. No arbitrary little-o term is differentiated. The velocity remainder in (6) can be strengthened to O(r^(1-2s)), with all fixed angular derivatives, by the source split below and local elliptic estimates on rescaled exterior annuli. For clarity, the inverse statement needs only a source smooth near finite points and with the explicit differentiable exterior expansion above. A smooth cutoff subtracts r^-s A_S outside a disk. Its inverse has the displayed homogeneous part, plus lower powers and at most a centered constant at this order; the remainder source is O(r^-2s), whose centered velocity is O(r^(1-2s)) for b>2, possibly with a smaller constant. Hence it is o(r^(1-s)). A difference between the explicit inverse and the canonical relative law is an entire sublinear harmonic vector, therefore constant, and centering removes it. No finite-box boundary condition is used. Interior finite-spline regularity is sufficient for this leading-tail calculation; no assertion of global C-infinity regularity of generic spline coefficients is needed.

On a homogeneous scalar r^q B(theta), the leading vector in (6) acts by

    V.grad(r^q B)=L^(1+s)r^(q-s)(-q F_S' B+k F_S B').

Also partial_x(r^m H_0)=r^(m-1)(m cos(theta)H_0-sin(theta)H_0'), with m-1=-2s. Applying beta r partial_r-(beta-2) to the two temperature terms in (5) gives multipliers 2(1-beta s) and 2-3 beta s. Applying beta r partial_r+1 to the two vorticity terms gives 1-beta s and 1-2 beta s. Combining these identities proves (3)-(4). The velocity remainder and all products involving a second scalar term are of strictly lower order. This also proves all three consequences by fixing any angle where the relevant nonzero angular polynomial is nonzero.

## 3. Exact arithmetic and its limits

Treat each stored binary coefficient, the reconstructed binary knot values, L and b,beta as its exact rational value. The source-combination weights must likewise be rational; all source weights used here are the stored binary values interpreted as exact rationals. When an archive supplies cG_f_effective, its binary entries themselves are the exact source coefficients. A prior bitwise check verifies their agreement with the stored floating-point product lambda*cG_f; this does not assert equality to an unrounded rational product. At a clamped degree-p endpoint,

    C(1)=c_last,
    C'(1)=p(c_last-c_previous)/(1-t_last_internal).       (7)

Here t_last_internal is the left endpoint of the final positive knot span, immediately before the clamped endpoint block; for an interval without internal knots it is the left boundary. In the own reader it is exactly edges[-2], not the endpoint 1. This follows from the standard polynomial recurrence for the derivative spline: only the final coefficient survives at the clamped endpoint. It can also be checked on the last Bernstein cell. The origin mask leaves both last coefficients unchanged for the archives under audit.

In the variable w=exp(i theta), cos(theta)=(w+w^-1)/2 and sin(theta)=(w-w^-1)/(2i). Equations (1)-(3) use only finite Laurent-polynomial operations, differentiation w.r.t. theta (multiplication of the nth coefficient by i n), and division by the nonzero rational numbers n^2-k^2. Hence H_j,A_j,F_S,E_T,E_O have exact rational real and imaginary Fourier coefficients. Their identically-zero status can be decided without evaluating at a large radius, subtracting nearly equal floating-point fields, or choosing a residual denominator floor. The positive factors L^(1+js), possibly irrational, were factored out explicitly in (4); they do not affect nonvanishing.

This is an exact check of the specified serialized representation and reconstructed knots. It is not an interval enclosure of uncertainty in a continuum profile, and it does not certify the solver's characteristic integration or its fit coefficients as approximations to a solution. Numerical cross-checks against the independent Cartesian residual grids are supplementary consistency checks only. Formula (2) independently enforces the leading full-plane inverse, while earlier physical-space inverse manufactured tests cover the finite-radius implementation.

## 4. Manufacture and horizontal limits

For L=1 and C_F,0=C_G,0=1 in mode0, all other endpoint coefficients and all first derivatives zero, H_0=cos^2(theta), A_0=cos(theta), F_S=-cos(theta)/(k^2-1) for the self source. At beta=b,

    E_T=3 sin(theta)cos^2(theta)/(k^2-1),
    E_O=2 sin(theta)cos(theta)/(k^2-1)
                         -m cos^3(theta)-2sin^2(theta)cos(theta). (8)

These follow by direct one-mode differentiation and provide independent sign and product checks. In particular E_T is nonzero, although it vanishes on the horizontal ray; testing that ray alone would miss the obstruction.

When H_0(0) and A_0(0) are nonzero and beta!=b, the leading horizontal pointwise-normalized limits are

    |R_Theta|/N_Theta -> |beta m-(beta-2)|/(beta |m|+|beta-2|),
    |R_Omega|/N_Omega -> |1-beta/b|/(1+beta/b).          (9)

At y=0 the dilation terms contain only x differentiation, and the lower-order velocity terms vanish after normalization, proving (9). They reproduce packet16 for the newer r2 map; the map changes lower powers, not these leading limits.

Dependencies: explicit endpoint expansion, finite Fourier algebra, elementary homogeneous polar differentiation, and the canonical modal inverse already independently proved in packets03/38. No model review or computation is claimed until recorded in verification/. No Lean or Lake build is permitted. The full B2 endpoint remains open.

Audit clarification 2026-10-21T00:05:12.982662+00:00: adopted the valid differentiated-remainder, endpoint-knot and rational-source precision points from the lead referee audit89. No coefficient output changed.
