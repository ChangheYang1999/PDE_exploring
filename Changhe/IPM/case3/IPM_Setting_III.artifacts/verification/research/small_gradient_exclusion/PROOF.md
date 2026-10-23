# A global gradient lower bound for smooth sublinear profiles

Date: 2026-10-20. Status: independently reconstructed theorem. The original12 exact checks passed17:58:01Z. The expanded36 exact checks passed at2026-10-20T18:07:00.214203Z. This is a quantitative necessary condition for every exact primary profile, and an exclusion of a specified uniformly small family. It is not nonexistence in the full primary class.

## 1. Statement and notation

Let ell>=1 and suppose smooth fields on R^2 satisfy

    (ell X+U).grad rho=rho,
    div U=0, curl U=-rho_x,
    U is the canonical full-plane inverse of rho, U=o(r), rho=o(r).

Suppose, for some p in (0,1), rho and U have exterior differentiated bounds through order three,

    |D^j rho(X)|+|D^j U(X)| <= C_j r^(p-j), 0<=j<=3, r>=1.

For the exact primary class of PROMPT these bounds follow from the separately proved local continuation and exterior regularity theorem in ../local_ipm_continuation/PROOF.md. The present estimate can instead take these bounds as explicit hypotheses. It does not assume Hdyn, a density sign, a finite equilibrium set, a special spatial scale or smallness of the origin slope. The parities are required only for the identification of a possible polynomial at the end; sublinear growth by itself also excludes every nonconstant such polynomial.

Tensor derivatives are ordered: |D^k f|^2 is the sum over all ordered spatial derivative indices and, for a vector, its components. Matrix norms in pointwise estimates are Frobenius norms. Define

    R = sup_X |grad rho(X)|,
    V = sup_X |DU(X)|,
    C_G = 2+sqrt(2), C_* = 6+3sqrt(2)/2.

The norms R and V are finite. If rho is nonzero and has the required odd-y parity, then

    2ell-1 <= 3V+R+3 C_G sqrt(VR) <= C_*(V+R).             (1)

In particular, no such nonzero profile can obey

    C_*(R+V)<2ell-1.                                      (2)

For a family with ell=1+D, D>0, and R+V<=M D with M independent of D, there are no nonzero profiles for

    0<D< min(1, 1/(2 C_* M)),                             (3)

when M>0. If M=0 the density gradient and velocity derivative vanish, and parity directly forces the zero profile. Formula (3) is only a convenient sufficient interval; no sharp threshold is claimed. More generally every nonzero smooth primary family with D tending to zero satisfies

    liminf_(D->0) (R+V) >= 1/C_*.                         (4)

Thus a small origin slope a0=O(D) does not describe a globally weak smooth profile unless a larger derivative occurs away from the origin. The estimate gives no location for such a region.

## 2. Derivative integrability and canonical multiplier

The exterior estimates imply D^3 rho,D^3 U are square integrable: their squared radial majorant has integral proportional to integral_1^infinity r^(2p-5) dr. They also imply D^2 rho,D^2 U are in L4. Every derivative is bounded on compact sets by smoothness. No L2 assumption on rho or U is made; each can grow at infinity.

The canonical velocity has Fourier multipliers

    m_1(xi)=xi_1 xi_2/|xi|^2,
    m_2(xi)=-xi_1^2/|xi|^2.

Their squared Euclidean sum is xi_1^2/|xi|^2<=1. Applying the multiplier to the L2 third derivatives, with the ordered derivative sum giving |xi|^6, yields

    ||D^3 U||_2 <= ||D^3 rho||_2.                         (5)

Here the low-frequency prescription is the canonical one. Equivalently one can commute three derivatives with its cancellation integral in the distribution sense, use the displayed multiplier away from zero frequency, and use square integrability to remove any remaining distribution supported at zero. Such a distribution would be a polynomial in physical space and cannot be a nonzero L2 derivative. A free harmonic strain is neither chosen nor fitted.

## 3. The interpolation estimate needed for the middle commutator

Let v be either grad rho or the vector containing every component of DU. It has bounded norm, Dv in L4 and D^2v in L2. For a compactly supported smooth vector the product rule gives

    integral |Dv|^4
      = -sum_(a,i) integral v_a v_(a,ii) |Dv|^2
        -2sum_(a,i,b,j) integral v_a v_(a,i) v_(b,j) v_(b,ij).

For the first term, |Delta v|<=sqrt(2)|D^2v|. For the second, set

    q_i=sum_a v_a v_(a,i),
    s_i=sum_(b,j) v_(b,j) v_(b,ij).

Then |q|<=|v||Dv| and |s|<=|Dv||D^2v|. Cauchy-Schwarz in space therefore proves

    ||Dv||_4^2 <= C_G ||v||_infinity ||D^2v||_2.          (6)

If ||Dv||_4 is zero the conclusion is immediate; otherwise divide by its square. The same identity applies to the present noncompact v by inserting an expanding smooth radial cutoff before the integration by parts. On an annulus of radius L the only added flux has magnitude bounded by a constant times

    L^(-1) integral_annulus |v||Dv|^3
      <= C L^(4p-6),

using v=O(r^(p-1)), Dv=O(r^(p-2)) and area O(L^2). This tends to zero since p<1. All other terms converge absolutely: |Dv|^4 is integrable, while |v||Dv|^2|D^2v| is integrable by the bounded v and the L4/L2 properties already proved. Thus (6) holds with the same constant and no boundary term at the origin.

Applying it to the two choices of v gives

    ||D^2 rho||_4^2 <= C_G R ||D^3 rho||_2,
    ||D^2 U||_4^2 <= C_G V ||D^3 U||_2.                  (7)

This proof uses only derivatives present in the hypotheses; it does not assume bounded density or a globally bounded first-order potential.

## 4. Third derivative energy identity

Write W=ell X+U, F=D^3 rho and E=||F||_2^2. Differentiate transport three times. With ordered indices i,j,k, the result is

    W.grad rho_(ijk)+(3ell-1)rho_(ijk)
      + U_(l,i)rho_(ljk)+U_(l,j)rho_(lik)+U_(l,k)rho_(lij)
      + U_(l,ij)rho_(lk)+U_(l,ik)rho_(lj)+U_(l,jk)rho_(li)
      + U_(l,ijk)rho_l = 0,

summing l over the two velocity components. Pair with rho_(ijk) and sum i,j,k. Since div W=2ell, integration of the undifferentiated transport subtracts ell E. The resulting coefficient is 3ell-1-ell=2ell-1.

This integration is valid with an outer cutoff. Its error is bounded by C times the L2 mass of F in the annulus, because |W|<=C(1+r), and hence tends to zero. The differentiated profile is smooth everywhere, so there is no inner boundary. Each remaining pairing is absolutely integrable by the estimates below.

There are three terms with one derivative on U. Tensor contraction and the Frobenius bound give a total at most 3V E in absolute value. The three terms with two derivatives on U give at most

    3 ||D^2 U||_4 ||D^2 rho||_4 E^(1/2).

The last term gives at most R ||D^3 U||_2 E^(1/2). From (5) and (7), the middle quantity is at most 3 C_G sqrt(VR) E, and the last is at most R E. Therefore

    (2ell-1)E <= [3V+R+3 C_G sqrt(VR)] E.                (8)

If E>0, division proves the first inequality of (1). If E=0, smoothness makes every third derivative vanish identically, so rho is a polynomial of degree at most two. A sublinear polynomial is constant; odd-y parity makes this constant zero. Hence E>0 for every nonzero profile in the stated class. Finally sqrt(VR)<=(V+R)/2 and 3V+R<=3(V+R) give the second inequality of (1) with the displayed C_*.

## 5. Scaling and small-D consequences

Under the genuine dilation rho_lambda(X)=lambda rho(X/lambda), U_lambda(X)=lambda U(X/lambda), both R and V are invariant, as are ell and a0. The norm E transforms as E_lambda=lambda^(-2)E, so both sides of (8) transform equally. Thus the exclusion cannot be removed by choosing a different representative of a scaling orbit.

If R+V<=MD and D satisfies (3), C_*(R+V)<1/2<1+2D=2ell-1, contradicting (1). Taking a liminf in the same inequality proves (4). The origin normalization only gives DU(0)=diag(D,-D), so V>=sqrt(2)D and R>=|a0|. These lower bounds do not imply upper bounds of order D. Accordingly neither bounded a0/D nor a small forced center defect implies the hypotheses of (3).

The finite-regularity homogeneous modes of degree d in (1,2) from ../finite_regularity_and_concentration/PROOF.md are not excluded by this argument. Wherever their third derivative is nonzero, its squared radial integral near zero is proportional to integral_0^1 r^(2d-5) dr, which diverges. If every third derivative vanished, the mode would be a polynomial, contradicting its noninteger homogeneity and nonzero value. Thus the required energy regularity fails for these modes. A nonlinear weak profile, if one is ever constructed, requires its own assessment; no existence follows from the local linear modes.

## 6. General ordered derivative identity and the second derivative bound

For an integer k>=2 assume the exterior differentiated estimates through k (through every order for the assertion for every k). Then D^k rho and D^k U lie in L2: the exterior radial integral is integral_1^infinity r^(2p-2k+1) dr, which converges since p<1 and k>=2. Define E_k=||D^k rho||_2^2 and the ordered tensor commutator

    [D^k,U.grad]rho = D^k(U.grad rho)-U.grad(D^k rho).

Commuting the dilation gives D^k(ell X.grad rho)=ell X.grad D^k rho+k ell D^k rho. The differentiated equation and div W=2ell therefore imply

    ((k-1)ell-1) E_k = -<D^k rho,[D^k,U.grad]rho>.       (9)

One can first use a cutoff on the equation. The transport cutoff flux is bounded by the annular L2 mass of D^k rho because W=O(r). Every commutator product is integrable: its j-th term has exterior size |D^k rho| |D^j U| |D^(k+1-j)rho|=O(r^(3p-2k-1)), 1<=j<=k, whose radial integral converges for p<1 and k>=2. Smoothness controls the interior. This proves (9), without assuming an L2 density. The Fourier contraction in Section 2 gives ||D^k U||_2<=||D^k rho||_2 for the same reason as (5).

For k=2, the three terms of the commutator are

    U_(l,i)rho_(lj)+U_(l,j)rho_(li)+U_(l,ij)rho_l.

Their inner products with rho_(ij), summed over ordered i,j, have absolute sum at most (2V+R)E_2. Consequently every nonzero profile obeys

    ell-1 <= 2V+R.                                      (10)

If E_k=0, rho is a polynomial of degree at most k-1. Sublinear growth then forces rho to be constant, and the transport equation makes that constant zero. Thus E_k>0 for every nonzero profile here. In particular, saying E_k=0 implies an affine density is only an intermediate conclusion for k=2; for general k the polynomial degree is k-1 before sublinearity is used.

## 7. The excluded ell=1 endpoint and the growth exponent

A separate elementary argument needs no differentiated far-field expansion. Let ell>0, suppose U is smooth with U=o(r), rho is smooth and satisfies transport, and |rho(X)|<=C(1+|X|)^gamma for a fixed gamma>=0. At every epsilon>0, |U(X)|<=epsilon |X|+C_epsilon. Thus W has linear growth, its smooth flow exists for every finite time in either direction, and its forward trajectories satisfy

    1+|Phi_t(X)| <= C_(X,epsilon) exp((ell+epsilon)t), t>=0.

This follows directly by scalar Gronwall applied to |Phi_t(X)|, or to its smooth upper regularization followed by a limit. Along the trajectory, transport gives rho(Phi_t(X))=exp(t)rho(X). If rho(X) is nonzero, the growth hypothesis then gives

    exp(t)|rho(X)| <= C C_(X,epsilon)^gamma exp(gamma(ell+epsilon)t).

Letting t tend to infinity yields 1<=gamma(ell+epsilon); letting epsilon decrease to zero gives gamma>=1/ell. Hence ell=1 permits no nonzero profile with a fixed strictly sublinear growth exponent gamma<1. This argument excludes that endpoint itself; it does not exclude profiles with ell decreasing to 1 and nonuniform constants or exponents tending to 1. No assertion of uniform compactness in that limit is made.

## 8. Dependencies and audit scope

The argument was independently reconstructed after reading P6 of the lead's separate slow1 audit. It uses the canonical multiplier, exterior smoothness theorem, elementary product rules and Cauchy-Schwarz. No shooting output enters it. The general small-D hierarchy, the sign of a0, Hdyn, nonlinear existence and the whole-class nonexistence question remain unresolved. Exact code checks of the commutator coefficients support only the algebra; the integration and boundary arguments above are the proof.
