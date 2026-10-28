# Audit of the new finite-section construction

This topic refers only to the fixed code snapshot identified in evidence/snapshot.json, taken at the real time recorded there. Later versions require a new audit. The exact normalized modal density is the object of topics 04 and 15. A defect in the test space or a definition does not establish that every matrix entry is numerically inaccurate.

## 1. Test-space conformity

The declared forcing space has squared norm

    ||g||_Y^2 = sum_N (1+(2N+1)^2)^sY
                 integral_R (|G_N(t)|^2+|G_N'(t)|^2) W_Y(t) dt,
    g(r,theta) = r^3 sum_N G_N(log r) sin((2N+1)theta).

The derivative is a weak derivative on the entire real line. The weight W_Y is strictly positive and locally bounded above and below. Let l<u be finite endpoints. A clamped degree-p B-spline system on [l,u] includes a first spline B_0 with B_0(l+)=1 and a last spline B_last with B_last(u-)=1. Extend them by zero off [l,u], as the snapshot's TestSplines does by omitting both infinite cells. In distributions,

    (1_[l,u] B_0)' = 1_[l,u] B_0' + delta_l,

where the last endpoint term is zero if the spline's support does not reach u. The general formula includes -B_0(u-) delta_u as well. A nonzero Dirac mass is not represented by a locally square-integrable function. Thus B_0 and B_last are not in the declared Y, regardless of the smoothness at their internal joins.

Consequently the assembled broken-gradient G_test is not the Y Gram of these test functions, and the row map cannot be identified with the Y orthogonal projection Q_M onto their span. The finite integrals and a finite generalized singular value still define algebraic quantities, but the claimed projection interpretation is false for this snapshot. Deleting the two endpoint splines gives continuous zero extensions and fixes this particular H1 membership defect. The remaining derivative jump is permitted in H1. Exact smooth extensions or a different explicitly stated forcing realization are other possibilities.

## 2. Full TAU direction

Write Theta_0(theta)=sum_(m=0)^(M-1) a_m cos(2m theta), with a_(M-1) nonzero. Exact multiplication by cos(2theta) produces modes through M:

    [Theta_0 cos(2theta)]_M = a_(M-1)/2.

The snapshot's tail_columns allocates Bm of length M and loops only through m=M-1. Hence the resulting TAU is the product with mode M deleted. For the exact modal input M=260, the omitted coefficient equals

    -8059128652303703/20769187434139310514121985316880384.

The scalar repair changes a_0 only and cannot change this coefficient. Proof 13 already derives this exact rational from the original data. Calling the actual truncated vector a separately selected direction is mathematically possible, but calling it the full product is incorrect. Restoring the full product requires enlarging the density-to-sine and velocity mode maps as well; inserting a 261st coefficient into a matrix with only 260 input columns is insufficient.

## 3. Tail compensation identity and membership

Suppose 0<k<1/2, ell=1/k, the background has leading density r^k Theta_0, and the canonical velocities have the corresponding sublinear asymptotics without added harmonic terms. Let a compactly modified tail direction K_P have leading r^k log(r/R_+) Theta_0, and let a column phi have either a lower tail O(r^(2k-1)) or a pure leading angular r^k tail. Terms with the leading power have finite angular expansions, with the differentiated remainder bounds assumed. Then the only r^k term of the full linearized image is

    L phi = (k c[phi]/3) r^k Theta_0 + lower terms,
    L K_P = (ell+k c[K_P]/3) r^k Theta_0 + lower terms.

Indeed (ell r partial_r - 1) annihilates r^k Theta, and on r^k log(r/R_+) Theta_0 it gives ell r^k Theta_0. Each velocity-density interaction is O(r^(2k-1) log r) or smaller. Thus, if 3ell+k c[K_P] is nonzero, the exact coefficient

    d_phi = -k c[phi]/(3ell+k c[K_P])

makes L(phi+d_phi K_P) have no leading r^k term. This is the formula in certify.py. It is correct. For 2k-1<gamma<k, the separate uncompensated images generally fail to belong to Y, since their squared tail factor has integral integral exp(2(k-gamma)t) dt. The compensated image with tail O(r^(2k-1) log r) belongs at infinity since 2k-1-gamma<0. The snapshot's gamma=(3k-1)/2 lies in this interval. Any full image-Gram computation must combine these tails before integrating the infinite interval. A positive interval around a mathematically zero leading coefficient cannot be integrated as though the coefficient were exactly zero.

This leading-power calculation establishes neither the remaining source/origin estimates nor any infinite-dimensional inverse. It also requires an explicit construction of the exact scalar-compensated functions: each c and the denominator are exact reals enclosed by balls, not arbitrary independent choices from the balls.

## 4. Inner Green cancellation

For one stream mode n>=1 and fhat(sigma)=exp(e sigma) p(sigma), write lambda=2n+4+e>0 and S'+lambda S=p. On the inner half-line sigma<=0 the canonical expression is

    A_n(sigma)=exp(4t_a) exp((e+4)sigma) S(sigma).

There is no exp(-2n sigma) term. The generic finite-cell formula instead writes its coefficient as

    A_n(0)-exp(4t_a)S(0).

This is identically zero by the canonical boundary integral. Outward interval evaluation of the two equal terms can leave a nonzero-radius ball containing zero. Retaining that ball gives a valid pointwise enclosure at each fixed sigma, but no finite uniform upper bound on the half-line: exp(-2n sigma) grows as sigma tends to minus infinity. For instance n=1,e=0,p=1 gives A_1(sigma)=exp(4sigma)/6 when t_a=0. Evaluating 1/6-1/6 with separately rounded Arb balls generally gives a nonzero-radius ball. Therefore a rigorous end-cell integral needs an algebraic canonical formula that omits this homogeneous term, or an exact symbolic dependency proof that sets it to zero. Increasing precision alone does not repair an infinite-end membership argument.

The snapshot does not apply this canonical simplification inside green_A_on_cell. This is an unresolved implementation prerequisite for full image norms, not a claim that its finite-cell outward evaluations underestimate the function.

## 5. Scope of the identity and matrix checks

The identity L rho = 2F(rho)+rho+(c[rho]/3-ell) X.grad rho holds algebraically for any background exponent ell, without exact normalization. The fixture loader explicitly uses stored rounded joins and is not the exactly rematched normalized modal trial. The printed difference between its c and 3/k-1 therefore does not refute the normalized full-data strain check.

The snapshot test_identity.py prints finite-point errors but contains no pass/fail assertions and proves no uniform identity by itself. The late code's forward boundary recurrence correctly includes exp(e h) multiplying moment_left(2n+4+e,p,h). Exact equality follows by multiplying the defining integral by exp(-2nh), so this factor must be retained for exponential terms. A test sharing the same incorrect Green data in both sides could miss a common error. Independent kernel or differential and endpoint checks are required.

The algebraic matrix lower-bound device is valid: for SPD G_Y and any real Z,

    G_Y^(-1) - (Z+Z^T-Z^T G_Y Z)
      = (Z-G_Y^(-1))^T G_Y (Z-G_Y^(-1)) >= 0.

Thus B^T(Z+Z^T-Z^T G_Y Z)B-s^2 G_X positive semidefinite gives the finite generalized singular lower bound s when both Grams are the stated positive definite matrices. A verified congruence by an invertible approximate Cholesky factor and a symmetric error E with ||E||_infinity<1 proves positivity, since its eigenvalues have absolute value at most that norm. This does not cure a nonconforming test space, certify the integral assembly automatically, or control any complement block.

## Evidence and verdict scope

check.py independently checks the endpoint counterexample, the exact omitted TAU coefficient, the model Green cancellation and the displayed tail-compensation algebra. It uses a snapshot solely to reproduce the test-space construction on a small exact mesh. No full numerical matrix or inverse bound is certified here. See VERIFICATION_RECORD.md for the dated scoped verdict.
