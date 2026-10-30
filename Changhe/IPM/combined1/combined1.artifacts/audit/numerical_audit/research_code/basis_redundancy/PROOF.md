# Exact generator redundancy and finite Gauss-Newton diagnostics

## Statement and exact input

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma and p_j=(3+gamma-j delta)/2. For the immutable candidate C1-N1-007-d2w-j7-e2bal, consider all2982 optimized generators in its coefficient JSON. This statement concerns the generator parameterization, independent of the particular coefficient values. The JSON declares n_free=2982 and n_fixed=0. The frozen run_pair.py and gn_spectrum.py pass the complete generator list to Problem3 without a fixed-coefficient list.

Set s=x^2+y^2, t=s/(1+s), H_m=Re(x+iy)^(2m). A monomial generator and a Legendre generator have the common factor H_m(1+s)^(p_j-m), multiplied respectively by

    mono(w): t^w,
    leg(w,n): t^w P_n(2t-1),

where P_n is the Legendre polynomial normalized by P_n(1)=1. All these functions are smooth. Within each(j,m), let B_(j,m) be the integer matrix whose columns are the ordinary t coefficients of these radial polynomials. Let d_(j,m) be its number of columns and r_(j,m) its exact rational rank. Then the linear map from generator coefficients to the potential has kernel dimension

    sum_(j,m) [d_(j,m)-r_(j,m)],

provided the finite branch labels have no integer difference(j-j')delta/2 for j!=j'. The checker verifies this exact rational condition, all ranks and explicit kernel vectors. Without that nonresonance condition the same sum is still a lower bound on the kernel dimension.

If v is any such kernel vector, chi(a+epsilon v)=chi(a) for every real epsilon. Thus rho=-partial_y Delta chi, U1=-chi_xyy and U2=chi_xxy, the residual F, every derivative or weak-pairing residual row and every background-field penalty are unchanged exactly. All constraint rows obtained from the strain, tail coefficients or origin Taylor jets annihilate v. In the exact mathematical constrained Gauss-Newton problem, these vectors are genuine zero directions of the coefficient representation. They represent the zero function and supply no near-kernel element of the PDE linearization on functions.

## Integer polynomial identity and rank calculation

Rodrigues' formula after the substitution x=2t-1 gives

    P_n(2t-1)=(1/n!) d^n/dt^n [t^n(t-1)^n]
             =sum_(k=0)^n (-1)^(n-k) binom(n,k) binom(n+k,k) t^k.

Indeed the coefficient of t^(n+k) before differentiation is(-1)^(n-k)binom(n,k); differentiating n times and dividing by n! multiplies it by(n+k)!/(k!n!)=binom(n+k,k). This constructs the matrix by integers, independently of the Legendre recurrence in the canonical converter.

Exact Gaussian elimination over Q gives its rank and a basis of its kernel. For a transparent independent check, the largest degree in each block and the number of monomial columns give respectively an upper and lower rank bound. When a block contains only Legendre columns with a fixed shift w and distinct n, their distinct degrees and nonzero leading coefficients give rank equal to the column count. Mixed blocks can often use the complete monomial subset as an exact spanning family. The checker verifies each claimed spanning relation as an integer coefficient identity and records independent kernel vectors with a unit coefficient in distinct nonpivot columns. Unit nonpivot coordinates make these vectors linearly independent.

For example, whenever the three corresponding generators occur,

    leg(w,0)-mono(w)=0,
    leg(w,1)+mono(w)-2mono(w+1)=0.

These identities hold on the whole plane, including the origin and far field. They are not sampled or asymptotic relations.

## Why different blocks do not cancel

Angular orthogonality separates different m. For a fixed m, write u=1/(1+s). The radial factors are u^(m-p_j) times polynomials in1-u. For each nonzero such polynomial choose its lowest u power k_j. The leading exponent is m-p_j+k_j. Distinct branches cannot have equal such exponents when(j-j')delta/2 is not an integer. Among finitely many nonzero branches there is therefore a unique least exponent, with nonzero leading coefficient. Divide the sum by that power of u and let u tend to zero. The result is nonzero. Thus no nontrivial cancellation across j is possible. This proves that the potential-space rank equals the sum of the block ranks and proves the displayed kernel dimension.

This argument does not assert that a chosen potential representation is injective after applying the density or velocity differential operators. The identified zero-potential directions are enough to demonstrate representation redundancy in every downstream field.

## Consequences for the frozen spectrum diagnostic

For an exact finite residual-row Jacobian J and an exact orthonormal basis Z of the homogeneous linearized constraint space, G=J^T J and G_Z=Z^T G Z. Every exact redundant vector is in the constraint kernel and is annihilated by J. Hence G_Z has at least the computed redundancy dimension of zero eigenvalues whenever all generators remain variable and the constraints depend only on physical fields. Positive diagonal rescaling preserves rank; it does not eliminate these zero directions. Individual coefficients of a redundant vector can be large even though its potential is identically zero.

The frozen gn_spectrum.py instead forms binary64 normal matrices, chooses the constraint rank by a floating relative threshold and clips negative eigenvalues of G_Z and its rescaling to zero before taking square roots. A reported zero singular value from this procedure is a numerical value of that processed finite matrix. Without a bound on matrix assembly, constraint projection and eigensolver errors, it does not resolve a small positive singular value of JZ. Indeed forming J^T J squares the ratio of extreme singular values in exact arithmetic. These statements follow directly from the spectral identity for a Gram matrix; no specific candidate spectrum is asserted without its retained output.

A useful continuation first removes exact polynomial redundancy, with a well-conditioned basis for the same polynomial span, then reports raw negative eigenvalues and numerical error scales. A function-space inverse claim still requires the infinite-dimensional complement and normalization estimates. This note makes no such claim and does not assert that removing redundant coordinates alone improves the residual.

## Verification and scope

Freeze the candidate, N1 source files and this proof before executing the checker. Construct all polynomials by the displayed binomial formula, compare them with a separate three-term recurrence, compute exact block ranks, prove every recorded kernel relation by direct multiplication, and check block nonresonance rationally. Retain all block dimensions and source hashes. Candidate-specific totals remain OPEN pending independent reproduction. No optimizer, server, cluster, remote model or formal proof-assistant build is run.
