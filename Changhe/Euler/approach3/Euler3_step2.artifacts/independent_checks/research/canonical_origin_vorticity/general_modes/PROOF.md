# Exact origin vorticity residual with general azimuthal modes

## Statement

Let T and S be finite sums of regular real solid harmonics of degrees ell >= 1 multiplied by real functions smooth in q = |y|^2 near q = 0. All azimuthal orders are allowed. Let

    U = curl(T y) + curl curl(S y),   Omega = curl U,
    J y = (-y2,y1,0),
    R_Omega = Omega + D Omega [(c I - w J)y + U] + w J Omega - DU Omega,

where c,w are real constants. The derivatives below require the indicated smooth radial functions, so U and Omega are smooth near the origin. Write the degree-one and degree-two harmonic parts of the potentials as

    T(y) = a.y + (1/2) y^T H y + higher terms,
    S(y) = b.y + (1/2) y^T G y + q v.y + higher terms.

Here a,b,v belong to R^3; H,G are real symmetric trace-zero 3 by 3 matrices. The vector v is the derivative at q=0 of the degree-one radial coefficient vector of S, after incorporating the smooth twist. The omitted terms may include a degree-three harmonic polynomial in S. They may also include arbitrary higher harmonic terms and higher radial powers of the stated harmonics. Equivalently, a and H are respectively the linear harmonic coefficients and quadratic harmonic Hessian of T at q=0; b and G have the same meaning for S. This definition of v is unambiguous because q times a linear harmonic polynomial has nonzero Laplacian unless that polynomial is zero.

For x in R^3 let [x]_cross denote the matrix z -> x cross z. Then

    U(0) = 2 b,                         DU(0) = [a]_cross + 3 G,
    Omega(0) = 2 a,                     D Omega(0) = 3 H - 10 [v]_cross,

and the exact origin identity is

    R_Omega(0) = 2 a + 6(H b - G a) - 20(v cross b) + 2 w J a.       (1)

Thus, if any component of (1) is nonzero, this exact finite field cannot satisfy the rotating momentum equation on a neighborhood of zero with a C2 pressure. The claim is about this represented field only. It excludes neither nearby fields nor rotating Euler profiles in general.

## Proof from the potentials

For a homogeneous harmonic polynomial K of degree ell, with h = grad K, direct differentiation and y.h = ell K give

    curl(f(q) K y) = f(q) (h cross y),
    curl curl(g(q) K y)
       = [(ell+1)g(q)+2q g'(q)] h - 2 ell g'(q) y K.                (2)

In particular, the toroidal velocity has degree ell at its lowest nonzero radial order. The poloidal velocity at radial order zero is (ell+1)g(0) grad K, of degree ell-1. Its radial corrections have degree at least ell+1. Therefore the only terms contributing to U(0) are the degree-one poloidal coefficients, and the only terms contributing to DU(0) are the degree-one toroidal coefficients and degree-two poloidal coefficients. Equation (2) gives U(0)=2b and DU(0)=[a]_cross+3G.

Curling the toroidal velocity gives its poloidal counterpart (2), so its contribution to Omega(0) is 2a and to D Omega(0) is 3H. Each component of h cross y is harmonic and homogeneous of degree ell: the cross terms in its Laplacian cancel by symmetry of the Hessian of K. As div curl = 0 and curl commutes with the Laplacian,

    curl curl curl(g(q) K y)
       = -Delta(g(q)(h cross y))
       = -[4q g''(q)+(4ell+6)g'(q)] (h cross y).                  (3)

This vanishes at y=0 for every ell>=1. Its only possible linear term has ell=1 and is -10(v cross y). Higher harmonics and higher radial powers do not contribute to D Omega(0). This proves all four derivative formulas, including the factor and sign of the radial contribution.

At y=0 the transport velocity equals U(0)=2b. Substitute the four formulas in the definition of R_Omega. The term [a]_cross a vanishes, giving (1). No assumption of a stagnation point, an axial velocity or an axial vorticity has been used. The explicit w J Omega term generally survives.

Finally, for the incompressible velocity given by these potentials, direct Cartesian differentiation gives curl R_u = R_Omega. The identities used are curl((y.grad)U)=Omega+(y.grad)Omega, rotation covariance for JU-(Jy.grad)U, and curl((U.grad)U)=(U.grad)Omega-(Omega.grad)U. The pressure contributes zero because mixed second derivatives commute for C2 P. A nonzero component of (1) is incompatible with R_u identically zero on a neighborhood.

## Exact coefficient formula for the campaign representation

Use the real orthonormal harmonics without the Condon-Shortley sign. Set

    nu1 = sqrt(3/(4 pi)),   nu2 = sqrt(5/(16 pi)),
    nu22 = sqrt(15/(16 pi)).

The degree-one harmonics in Cartesian order are nu1 x, nu1 y, nu1 z. The degree-two harmonics are

    H20 = nu2 (2z^2-x^2-y^2),
    H21c = 2 nu22 xz,       H21s = 2 nu22 yz,
    H22c = nu22 (x^2-y^2),  H22s = 2 nu22 xy.

For channel Q and label (ell,m,kind), let s_Q be the alternating sum sum_k (-1)^k Q_k at that label. A missing column or empty channel gives zero. Let s_A1 and s_C1 be the three degree-one sums in Cartesian label order (1,1,cos), (1,1,sin), (1,0,0). Under the damping hypothesis d>=1 below, B, D and E vanish at q=0. Thus B does not enter a or H, and D and E do not enter b or G. Then a=nu1 s_A1 and b=nu1 s_C1. H is the Hessian of the linear combination of the five displayed degree-two harmonics with coefficients s_A2; G uses s_C2. For example the H20 contribution is nu2 s_A20 diag(-2,-2,4), and each H21 or H22s contribution has its indicated off-diagonal entries equal to 2 nu22 times its coefficient. The H22c contribution is 2 nu22 s_A22c diag(1,-1,0).

Assume the campaign envelopes and mappings exactly as specified, with R0>0, R1>0, c!=0, alpha=(1-c)/c, integer correction damping d>=1, and all saved finite binary64 numbers interpreted as exact real numbers. If the saved channel configuration has R1=None, set R1=R0, as in the radial definition. A configuration with d=0 is outside this statement and must be rejected by this coefficient reader; without damping the correction channels require a separate origin calculation. Define

    xi(q) = 2 q/(sqrt(q+R0^2)+R0)^2 - 1,
    psi(q) = (w/(2c)) log(1+q/R0^2).

The main poloidal radial envelope for ell=1 is (sqrt(q+R0^2)/R0)^(-alpha). Let t_C1 be the Cartesian vector of sums sum_k (-1)^(k-1) k^2 C_k. Then

    v = nu1/(2 R0^2) [t_C1 - alpha s_C1 - (w/c) J s_C1]
          + 1_{d=1} nu1/R1^2 s_D1.                               (4)

To check (4), xi'(0)=1/(2R0^2), T_k'(-1)=(-1)^(k-1)k^2, and the envelope derivative is -alpha/(2R0^2). The twist phi+psi rotates the Cartesian coefficient vector by Q_{-psi}, so its derivative is -(w/(2cR0^2)) J s_C1. The D damping has derivative 1/R1^2 when d=1 and zero when d>=2. Its envelope equals one at zero; its envelope and twist derivatives multiply a damping factor that is already zero there. E has no degree-one component in the campaign definition. The B channel contributes neither a nor H because its damping vanishes at zero. This proves (4).

The formulas use exact real R0^2 and R1^2, not independently rounded approximations to these squares. They define the canonical smooth field associated with the saved coefficients and parameters. Agreement with a floating-point evaluator is a separate numerical check.

## Relation to the even-mode result and interval arithmetic

When all azimuthal orders are even, a,b,v are axial and H,G have no xz or yz entries. Both v cross b and J a vanish. Equation (1) becomes

    2 nu1 [s_A10 + 12 nu2(s_C10 s_A20 - s_A10 s_C20)] e3,

which is the previous exact even-mode formula. This reduction checks the constants 2 and 6 and the H20 normalization, and retains the origin transport term. The radial and rotation contributions and the H21/G21 normalizations vanish in this symmetry class; their constants and signs require the preceding general-mode proof and separate nonaxial controls.

All coefficient sums, alpha, w/c, the factors R0^-2 and R1^-2 are exact rational operations on finite binary64 inputs. Enclose pi using the proved 64-term Machin formula in the parent proof, and enclose the three positive square roots on the fixed 10^-60 grid. Apply interval addition, multiplication and exact-rational scaling component by component to (1) and (4). These operations produce outward intervals for the exact canonical components. A component interval excluding zero gives the stated obstruction. An interval containing zero is inconclusive; it does not prove cancellation. The construction does not provide a neighborhood-size estimate or a global norm bound.

## Dependencies and verification scope

The vector identities and coefficient derivatives are proved above. The normalization convention is explicit. Input decoding reuses the bounded independent exchange decoder, which already admits general harmonic labels; the parity restriction belongs to the old evaluator and is not removed there. Qualification must separately check exact polynomial curls, manufactured radial and odd-mode terms, twist signs, even-mode reduction, interval arithmetic and actual input identities. Formal verification is not claimed; Lean and Lake builds are prohibited. No saved unrestricted-mode result is asserted in this proof.
