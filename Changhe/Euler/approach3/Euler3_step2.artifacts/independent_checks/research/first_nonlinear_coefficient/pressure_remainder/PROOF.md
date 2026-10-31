# The full pressure remainder of a rotating homogeneous tail

Status: an informal proof under the exact hypotheses below. No numerical pressure error is bounded here. This result supplies the analytical hypothesis left open in the parent first-coefficient proof. The already registered numerical sources and their parent proof are not changed.

Subtracting the leading velocity from a finite profile leaves one additional inverse power of radius. The useful integrable quantity is the corresponding difference of the quadratic velocity tensors. Applying the Newton kernel to its double divergence gains three inverse powers in pressure and four in its gradient. The proof below establishes the gradient bound directly, without assuming a finite first moment of that tensor.

## A quantitative kernel lemma

Let 3 < p < 4. Let R = (R_ij) be a real 3 by 3 tensor whose entries belong to L1(R3) and to C2 on {x : |x| > 0}. Require

    B = sum_ij integral_R3 |R_ij(x)| dx < infinity,
    A = sum_ij sum_(a=0)^2 sup_(|x|>=1) |x|^(p+a) |D^a R_ij(x)| < infinity.

For derivatives use the Euclidean component norm, with the Frobenius norm for a Hessian. Set Gamma(x) = 1/(4 pi |x|), so -Delta Gamma = delta_0. Define

    Pi R = sum_ij (partial_i partial_j Gamma) * R_ij

as a distribution. At x != 0 its value is the principal-value convolution including the delta contribution. Then its gradient is a classical continuous function away from zero, and, for every |x| = r >= 2,

    |grad Pi R(x)| <= 16384 (A+B) r^(-4).                 (1)

This assertion requires no moment cancellation in R. The integrability of R, rather than a first-moment condition, is the reason that the right side contains r^(-4).

## Proof of the kernel lemma

Write K_ij = partial_i partial_j Gamma. Direct differentiation away from zero gives

    K_ij(s) = [3 s_i s_j - delta_ij |s|^2]/(4 pi |s|^5).

As a distribution this is its radial principal value minus delta_ij delta_0/3. The coefficient of the delta term follows by integrating twice by parts outside a ball of radius epsilon and passing to its limit: the boundary mean of s_i s_j/|s|^2 is delta_ij/3. The principal-value part has integral zero on every spherical annulus. Its pointwise magnitude is at most |s|^(-3)/pi. A further derivative obeys

    |partial_k K_ij(s)| <= (6/pi) |s|^(-4).             (2)

Indeed its numerator is the sum of -15 s_i s_j s_k and the three terms 3 delta_ij s_k |s|^2, 3 delta_ik s_j |s|^2, 3 delta_jk s_i |s|^2, divided by 4 pi |s|^7. This gives (15+9)/(4 pi).

Fix x with r >= 2. We split the convolution at this fixed point, rather than differentiating a cutoff that moves with x. Choose chi(s) = phi(8|s|/r), where phi(t) is one for t <= 1, zero for t >= 2, and on 1 <= t <= 2 equals

    1 - 10(t-1)^3 + 15(t-1)^4 - 6(t-1)^5.

This is a C2 radial cutoff, constant near zero. The elementary bounds |phi'| <= 15/8 and |phi''| <= 6 give

    |grad chi| <= 15/r,    |D^2 chi| <= 512/r^2.

For the Hessian bound its radial eigenvalue is at most 384/r^2 and the two tangential eigenvalues at most 120/r^2, so their Euclidean component norm is less than 512/r^2. Its support is |s| <= r/4, and chi = 1 for |s| <= r/8.

First consider one tensor entry and one gradient component. In the convolution of partial_k K_ij with R_ij(x-s), the part multiplied by 1-chi is nonsingular. By (2) and |s| >= r/8 on its support, its absolute value is at most

    (24576/pi) r^(-4) ||R_ij||_L1
      <= 8192 r^(-4) ||R_ij||_L1.                     (3)

For the local part, move the distributional derivative onto the C2 test function chi(s) R_ij(x-s). It equals K_ij applied to

    h(s) = chi(s) partial_k R_ij(x-s)
           - partial_k chi(s) R_ij(x-s).

Put A_ij = sum_(a=0)^2 sup_(|z|>=1) |z|^(p+a) |D^a R_ij(z)|. On the support of chi, |x-s| >= 3r/4 >= 1. Since (4/3)^(p+a) < 6 for a <= 2,

    |D^a R_ij(x-s)| <= 6 A_ij r^(-p-a).

The product rule therefore gives

    |grad h(s)| <= 6(1+30+512) A_ij r^(-p-2)
                 = 3258 A_ij r^(-p-2).

Also h(0) = partial_k R_ij(x). In the principal-value integral over |s| <= r/4, subtract h(0). The annular mean-zero identity just proved leaves the value unchanged. The mean-value inequality and the bound on K_ij give

    |PV integral K_ij(s) h(s) ds|
      <= 3258 A_ij r^(-p-2) integral_(|s|<=r/4) |s|^(-2)/pi ds
      = 3258 A_ij r^(-p-1).

The delta term contributes at most A_ij r^(-p-1)/3. Thus the whole local part is at most 3260 A_ij r^(-p-1), and hence at most 3260 A_ij r^(-4), since p > 3 and r >= 1. Together with (3), summing the nine entries bounds each gradient component by

    [8192 B + 3260 A] r^(-4).

Taking the Euclidean norm of the three components multiplies this by at most sqrt(3), which is bounded by the coefficient 16384 in (1). The same local subtraction gives continuous dependence on x on every compact set away from zero. The nonsingular terms are controlled by L1 integrability and dominated convergence. This proves the lemma, including the asserted classical interpretation of the gradient.

## Pressure theorem

Let 1 < alpha < 3/2, let kappa != 0, and put beta = 2 alpha + 1. Let Q_t be the rotation through angle t about the third axis. Let U belong to C4(R3;R3), be divergence free, and let U0 belong to C4(R3 minus {0};R3), be divergence free there, and satisfy, for every lambda > 0 and x != 0,

    U0(lambda Q_[-kappa log lambda] x)
      = lambda^(-alpha) Q_[-kappa log lambda] U0(x).    (4)

Assume that there is C < infinity such that, for derivative orders a = 0,1,2 and |x| >= 1,

    |D^a(U-U0)(x)| <= C |x|^(-alpha-1-a).             (5)

Let P be the unique C2 full-space pressure that tends to zero at infinity and solves

    -Delta P = tr((DU)^2).

Equivalently it is the Newton integral with Gamma as defined above. Let P0 be the homogeneous pressure constructed in the parent proof: on the sphere expand s(n) = tr((DU0(n))^2) in orthonormal complex spherical harmonics, put q_m = -2 alpha + i m kappa, and set

    p_lm = s_lm/[l(l+1)-q_m(q_m+1)],
    P0(r n) = r^(-2 alpha) sum_lm p_lm Y_lm(Q_[kappa log r] n).

The definition is immediate for the finite angular sums used in this campaign. More generally it is the smooth solution of this sphere equation; only the finite case is needed here. Suppose U0 is one of those finite harmonic fields. Define R_ij = U_i U_j - U0_i U0_j. Then R meets the kernel lemma with p = 2 alpha + 1. For its constants A and B,

    |grad(P-P0)(x)| <= 16384(A+B)|x|^(-4), |x| >= 2. (6)

No Euler momentum equation is assumed. The estimate is about the exact whole-space pressure, with no added harmonic term.

## Proof of the pressure theorem

First check the integrable tensor difference. Formula (4), compactness of the sphere and differentiation give |D^a U0(x)| <= C_a |x|^(-alpha-a) for a <= 2. Near the origin U and its derivatives are bounded, while U0 is O(r^(-alpha)). Hence R is O(r^(-2 alpha)), which is integrable because 2 alpha < 3. For r >= 1, write

    R = U0 tensor (U-U0) + (U-U0) tensor U0
        + (U-U0) tensor (U-U0).

The product rule, (5), and the bounds on U0 give D^a R = O(r^(-2 alpha-1-a)) for a <= 2. Thus A and B in the lemma are finite, with p = 2 alpha + 1 in (3,4).

The Newton pressure P exists: U is smooth and DU = O(r^(-alpha-1)), so its source is bounded and O(r^(-2 alpha-2)). The kernel integral converges absolutely. For its second derivatives, subtract the source value in a small ball about x in the principal-value K_ij formula; the source is C2, so the remaining singularity is integrable and depends continuously on x. This gives a C2 solution. To check decay, divide the integral into |z| < r/2, |x-z| < r/2, and the part outside both balls. These pieces are bounded respectively by a constant times ||f||_L1/r, r^(2-q), and r^(2-q), where f = tr((DU)^2) and q = 2 alpha + 2 > 4. Thus P tends to zero. Two such solutions differ by an entire harmonic function tending to zero and hence agree by the maximum principle on expanding balls. Since div U = 0,

    tr((DU)^2) = sum_ij partial_i partial_j(U_i U_j).

Integrating the Newton integral twice by parts shows P = Pi(U tensor U). Boundary terms at large radius vanish by the displayed decay of U and DU; the small sphere around the kernel singularity gives exactly the delta part of K_ij already included in Pi. Thus this identity uses the full pressure with the stated normalization.

It remains to identify Pi(U0 tensor U0) with P0. The convolution defining Pi(U0 tensor U0) is well defined away from zero. Near the tensor's origin its singularity r^(-2 alpha) is integrable. At infinity the integrand is O(r^(-2 alpha-3)), and near the kernel's origin the principal-value subtraction applies to a smooth function. A change of variables in the convolution, including its delta part, shows that it is a scalar rotating-homogeneous function of degree -2 alpha. It is smooth away from zero and solves

    -Delta Pi(U0 tensor U0) = tr((DU0)^2)

there. Subtract P0. The difference H is harmonic away from zero and obeys

    H(r n) = r^(-2 alpha) h(Q_[kappa log r] n).

In spherical harmonics, harmonicity requires

    [l(l+1)-q_m(q_m+1)] h_lm = 0

for each integer l >= 0 and |m| <= l. If m != 0, the imaginary part of q_m(q_m+1) is m kappa(1-4 alpha), which is nonzero. If m = 0, the real number 2 alpha(2 alpha-1) lies strictly between 2 and 6 and is unequal to every l(l+1). Thus every h_lm vanishes, proving H = 0. This argument also rules out a hidden homogeneous harmonic addition; it does not discard one by convention.

By linearity,

    P-P0 = Pi(U tensor U-U0 tensor U0) = Pi R.

Apply the quantitative kernel lemma to obtain (6).

## Application and scope

For the exact finite representation in ../../represented_tail_decay/PROOF.md, with positive R0,R1, a nonnegative integer damping order, finite real coefficients and 2/5 < c < 1/2, take alpha = (1-c)/c and kappa = omega/c. The leading A,C potentials define U0. The identity xi = 1-4R0/(sqrt(r^2+R0^2)+R0) gives xi = 1+O(r^-1) with differentiated bounds. The radial envelope and twist differ from their leading homogeneous forms by differentiated O(r^-2). Consequently A,C contribute U-U0 = O(r^(-alpha-1)), including the first two derivatives. B,D start at r^(-2 alpha-1), and the nonzero E channels start at r^-4. These are faster than r^(-alpha-1). The smoothness at the origin and the derivative bounds are exactly those established in that finite-representation proof. The hypotheses of the theorem therefore hold.

Since beta < 4, (6) is o(r^(-beta)). It supplies the pressure-remainder hypothesis in ../PROOF.md. In combination with that proof's separation of the other radial exponents, the coefficient of the primitive residual at velocity order r^(-beta) is Greq-G. This does not say that the lower-order A,C residual coefficients vanish, that Greq-G is zero, or that a numerical estimate of it is accurate.

The constant A+B is not evaluated for any checkpoint. The theorem supplies a decay rate, not a usable certified pressure error bar at a specified finite radius. It does not establish that r^-4 is attained: the leading pressure correction can cancel for particular tensors. It uses no first moment of R, which generally is not absolutely integrable at these exponents. No formalization or numerical test is presented as a proof.

## Dependencies and provenance

This proof follows up the lead's 2026-10-29T23:42:57Z note, item 6(b). That note supplied the integrable-tensor strategy and explicitly called its pressure argument a sketch. The cutoff estimate, explicit constant, pressure identification and scope checks above are the verifier's completed argument. The exact source note and dependency hashes are retained in verification/. Read the finite-representation decay proof, the source-moment identity, and the parent first-coefficient proof before this result. The pressure normalization is the one in ../../pressure_consistency/PROOF.md. This file is an informal mathematical proof; formal_sources/ records that no Lean or Lake build was run.
