# A sharp odd Beurling bound for decreasing radial weights

## 1. Statement

Let R>0, 0<a<2, and w_R(x)=(1+|x|^2/R^2)^(-a/2) on R2. Let B be the complex Beurling operator with Fourier symbol (xi_1-i xi_2)^2/|xi|^2. On the complex centrally odd subspace of L2(w_R^2 dx), B has the exact norm

    ||B||=(2+a)/(2-a).                                      (1)

Here centrally odd means f(-x)=-f(x). The operator is initially defined on compact smooth odd functions and then extended by continuity. For real centrally odd h, the canonical IPM velocity U[h]=(-R1 R2 h,R1^2 h), with Rj symbol i xi_j/|xi|, consequently satisfies

    ||w_R U[h]||2 <= 2/(2-a) ||w_R h||2.                     (2)

The left side is the Euclidean vector L2 norm. The constant in (1) is optimal on the complex odd space. Optimality of the constant in (2), or of a restricted real S1 operator norm, is not asserted.

The same upper bounds hold for any positive radial weight w such that p(t)=-d(log w(e^t))/dt exists weakly and satisfies 0<=p<=a almost everywhere. The logarithm is assumed locally absolutely continuous. No derivative of p is needed. For a=0, both upper bounds are one by the ordinary unweighted multiplier identities; the proof below assumes a>0.

This is new T4 work prompted by T1 R1-008. It improves only the weighted operator constants in T4-041. It supplies no global signed-energy certificate, weighted high inverse, or existence statement. It remains CLAIMED until independently reviewed.

## 2. Angular reduction and the one-dimensional operators

For a finite angular sum write f(r,theta)=sum_m f_m(r) exp(i m theta). Under polar measure r dr dtheta, the radial isometry to the t=log r line is F(t)=r f_m(r), up to the constant angular norm. The operator B sends mode m to mode m-2. Put n=m-1. Directly solving the first-order polar equation for (partial_x+i partial_y)^-1 and applying (partial_x-i partial_y) gives its radial block

    F(t)-2n int_0^infinity exp(-nv)F(t+v)dv,  n>0,
    F(t)+2n int_0^infinity exp(nv)F(t-v)dv,   n<0,
    F(t),                                   n=0.             (3)

For example, the radial intermediate equation is g'-ng/r=f_m; the endpoint is decay at infinity when n>0, regularity at zero when n<0. These are the same blocks independently audited in T1 R1-008. Equation (3) also follows by differentiating its integral and checking those endpoints.

After multiplication by w(t)=w(e^t), the future kernel in (3) has ratio w(t)/w(t+v), and the past kernel has ratio w(t)/w(t-v). Because 0<=p<=a,

    w(t)/w(t+v)<=exp(av),  w(t)/w(t-v)<=1.                   (4)

If n>a, the future integral H is an L2-bounded operator, with norm at most 1/(n-a), by Young's inequality. It satisfies

    H'=(n-p)H-F,   G=F-2nH,
    F=-H'+(n-p)H, G=-H'-(n+p)H.                            (5)

The letter F now denotes the weighted input. Since p is bounded, H belongs to H1(R). These identities are valid in distributions and hence almost everywhere. The past block with k=-n>0 has an L2-bounded integral H of norm at most 1/k, and

    H'=F-(k+p)H,
    F=H'+(k+p)H, G=H'-(k-p)H.                              (6)

Initially the identities can be checked on compact smooth weighted inputs, then passed to all L2 inputs. Local absolute continuity of w and (4) justify the same argument for a general weight.

## 3. The positive-square identity

All norms and integrals in this section are on the t line. For H in H1(R), Re integral H' conjugate(H)=0. This follows by approximation by compact smooth functions in H1. In particular it does not require differentiating p.

For the future block put K_n=(n+a)/(n-a). From (5),

    ||G||2^2-||F||2^2=4n integral p |H|^2.                  (7)

Define D=-H'+(a-p)H. Then F=D+(n-a)H and the constant-coefficient cross term gives

    ||F||2^2=||D||2^2
              +(n-a) integral (n+a-2p)|H|^2.              (8)

Combining (7),(8) yields the exact identity

    K_n^2||F||2^2-||G||2^2
      = [4na/(n-a)^2] *
        [ ||-H'+(a-p)H||2^2
          + ((n^2-a^2)/a) integral (a-p)|H|^2 ].           (9)

Every term in the last brackets is nonnegative because n>a and 0<=p<=a. Thus the future block has norm at most K_n. This resolves the sign problem in a pointwise expansion involving p': the derivative term stays inside the nonnegative square instead of being estimated separately.

For the past block, (6) gives directly

    ||F||2^2-||G||2^2=4k integral p |H|^2 >=0.              (10)

Thus every past block is a contraction. The n=0 block is the identity. Central oddness restricts m to odd integers and therefore n to even integers. All positive n satisfy n>=2>a, and K_n decreases as n increases. Outputs from distinct m remain orthogonal because they have distinct angular indices m-2. Summing squared norms proves the upper bound (1) on finite sums, and density extends it to the whole odd space. The same argument proves the general-weight assertion.

## 4. Sharpness for the regularized power weight

For w_R one has

    p(t)=a exp(2t)/(R^2+exp(2t)),  p(t)->a as t->infinity.

Fix n=2 and a nonzero smooth chi supported in (-1,1). Set

    H_L(t)=L^(-1/2) chi((t-L^2)/L),
    F_L=-H_L'+(n-p)H_L, G_L=-H_L'-(n+p)H_L.

These functions have compact support, ||H_L||2=||chi||2, and ||H_L'||2=L^-1||chi'||2. On their supports p converges uniformly to a. Therefore

    ||F_L||2 -> (n-a)||chi||2,
    ||G_L||2 -> (n+a)||chi||2.

The forward integral associated to F_L in (5) is exactly H_L: their difference satisfies H'=(n-p)H, and the only such L2 function is zero because n-p>=n-a>0. Taking the angular mode m=n+1=3 gives compact smooth functions supported on annuli in R2. Their weighted norm ratio tends to (2+a)/(2-a). Together with the upper bound this proves equality in (1).

## 5. Velocity, contact term and scope

For a real input h the exact multiplier identity is

    U2[h]+i U1[h]=-(I+B)h/2.

Indeed U2 has symbol -xi_1^2/|xi|^2 and U1 has symbol xi_1 xi_2/|xi|^2. The two components are real, so their Euclidean magnitude equals the modulus of the displayed complex expression pointwise. Multiplication by the real weight and the triangle inequality now give (2).

The identity retains the identity-operator term in B and therefore retains the canonical local contact contribution -(1/2)h in U2. No change in velocity normalization is made. The canonical extension is the same as T4-041 because both are limits of the same compact smooth inputs, and weighted L2 convergence implies L2 convergence on each compact set.

If z is real and odd and g has ||grad g||infinity<=D, then

    ||w_R U[z].grad g||2 <= [2D/(2-a)] ||w_R z||2.

Thus the low contraction constant in Section 6 of T4-041 improves to

    [2D/(2-a)]/(beta-aD)

when beta-aD>0 and when the other, separately required high-space and invariant-ball hypotheses hold. The compactness theorem, its kernel, the signed principal matrix and its certificate requirements do not change. This bound is stated only in the odd space; the unrestricted even angular block n=1 would require a<1 for this proof.

Dependencies: the elementary polar block formulas, Young's inequality, H1 approximation, angular orthogonality, and the Fourier multiplier identity for U. No numerical approximation is needed to establish the inequalities. A short symbolic verification of (7)-(10) is provided separately and is not a substitute for the functional-analytic argument.
