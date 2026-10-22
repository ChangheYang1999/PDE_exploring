# Log-radial residual jets and the current modal assembly

Date: 2026-10-21. Status: exact mathematical identities proved below;
source linkage and independent finite checks OPEN until adjudication.
This is a local algebra theorem, not a physical enclosure certificate.
Read after topics 16, 69, 101, 118 and 122. Those topics supply context;
the identities below do not assume their unfinished numerical claims.

## Statement, notation and hypotheses

Let I be an open real interval, t=log r, r>0, and theta the polar angle.
Fix an integer M>=1. Suppose R_j in C^5(I), 0<=j<=M, and set

    rho(r,theta) = sum_(j=0)^M R_j(t) sin((2j+1)theta).

Put w_j=2j+1. Define f_n(t), 1<=n<=M+1, by the finite sine expansion

    partial_x rho(r,theta) = sum_n f_n(t) sin(2n theta),

with the explicit coefficient formula proved below. Set g_n=e^(2t) f_n.
Suppose A_n and B_n solve

    A_n' = -2n A_n + g_n,       B_n' = 2n B_n - g_n

on I, and define

    psi_n = (A_n+B_n)/(4n),
    psi(r,theta) = sum_n psi_n(t) sin(2n theta),
    U = (-partial_y psi, partial_x psi).

No canonical endpoint condition is implicit: these local ODE solutions
may contain harmonic homogeneous terms. A physical Green inversion is
an additional hypothesis whenever the formula is applied to a trial.
For an arbitrary constant c, let

    epsilon = (c X+U).grad rho - rho,
    P_n = -n e^(-2t) psi_n,
    Q_n = e^(-2t) (B_n-A_n)/4.

For n>=1 and j>=0 define

    N1(n,j)=j+n,
    N2(n,j)=j-n and s(n,j)=+1, if n<=j,
    N2(n,j)=n-j-1 and s(n,j)=-1, if n>j.

For arrays a_n and b_j let S_+(a,b) be the odd-sine coefficient array
obtained by adding a_n b_j at N1 and s(n,j) a_n b_j at N2, for every
pair. Define S_-(a,b) by reversing only the N2 sign. Extend R_j and its
derivatives by zero for j>M. Then for every 0<=i<=4,

    partial_t^i epsilon_N
      = c R_N^(i+1) - R_N^i
        + sum_(l=0)^i binom(i,l) [
            S_+(P^l,R^(1+i-l))_N
            + S_-(Q^l,(w_j R_j^(i-l))_j)_N ].                 (1)

Here superscript i denotes derivative order, including order zero,
not an ordinary power. In (1), the notation R_N^i means R_N^(i).
The coefficients vanish for N>2M+1. An allocated row N=2M+2 is harmless
zero padding in exact algebra. There are no zero or even sine modes.

The auxiliary derivative identities are

    A_n^(i+1) = -2n A_n^i + g_n^i,
    B_n^(i+1) =  2n B_n^i - g_n^i,                           (2)
    P_n^i = -n e^(-2t) sum_(l=0)^i binom(i,l)(-2)^(i-l) psi_n^l,
    Q_n^i = e^(-2t)/4 sum_(l=0)^i binom(i,l)(-2)^(i-l)(B_n-A_n)^l. (3)

They hold for every derivative appearing in (1). For a finite local
exponential-polynomial representation with sigma=t-t_a,

    R_j(t) = e^(3t_a) sum_alpha e^((3+alpha)sigma) C_(alpha,j)(sigma),
    f_n(t) = e^(2t_a) sum_alpha e^((2+alpha)sigma) F_(alpha,n)(sigma),

one has, as exact identities,

    R_j^i = e^(3t_a) sum_alpha e^((3+alpha)sigma)
                        (D+3+alpha)^i C_(alpha,j),
    g_n^i = e^(4t_a) sum_alpha e^((4+alpha)sigma)
                        (D+4+alpha)^i F_(alpha,n),           (4)

where D is ordinary polynomial differentiation. A finite family of real
exponents is allowed. The source may enclose them by intervals, but that
arithmetic assertion is separate from this exact identity.

The finite audit target is M=260, n=1..261, j=0..260, all 68121 pairs,
all five derivative orders, all derivative splits l=0..i, and the current
frozen cert_resid.py hash
1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053.
It must distinguish identities, selected source expressions, and actual
function enclosures. No numerical jet coefficient is certified here.

## Proof of the Cartesian derivative and Poisson sign

The polar differential operators are

    partial_x = e^(-t)(cos(theta) partial_t - sin(theta) partial_theta),
    Delta = e^(-2t)(partial_t^2 + partial_theta^2).

For one mode R_j sin(w_j theta), the first formula and the two elementary
product-to-sum identities give

    partial_x[R_j sin(w_j theta)]
      = e^(-t)/2 [ (R_j'-w_j R_j) sin((w_j+1)theta)
                 +(R_j'+w_j R_j) sin((w_j-1)theta) ].        (5)

The lower term is zero for j=0 because its sine frequency is zero.
The upper term contributes to n=j+1; the lower term, when j>=1,
contributes to n=j. This proves the asserted expansion for f_n, including
its endpoints and normalization. If R_j has the displayed representation,
then its derivative has polynomial (D+3+alpha)C. Formula (5) therefore
has factor e^(2t_a)e^((2+alpha)sigma) and polynomial coefficients

    upper: ((D+3+alpha)C_j - w_j C_j)/2,
    lower: ((D+3+alpha)C_j + w_j C_j)/2.                    (6)

The ODEs imply

    psi_n'=(B_n-A_n)/2,
    psi_n''=n(A_n+B_n)-g_n=4n^2 psi_n-g_n.

Thus -Delta psi = sum_n e^(-2t)g_n sin(2n theta)=partial_x rho.
The sign of the g term in the B equation is essential. These local
identities do not select the admissible harmonic component.

## Proof of transport and frequency assembly

The rotated gradient has polar components

    U_r=-r^(-1) partial_theta psi,
    U_theta=partial_r psi=r^(-1) partial_t psi.

Consequently

    U.grad rho = e^(-2t)(-psi_theta rho_t + psi_t rho_theta).

For one n,j pair this is

    -2n e^(-2t) psi_n R_j' cos(2n theta) sin(w_j theta)
    +e^(-2t) psi_n' w_j R_j sin(2n theta) cos(w_j theta).

Use

    2cos(a)sin(b)=sin(b+a)+sin(b-a),
    2sin(a)cos(b)=sin(b+a)-sin(b-a).

The radial coefficient is P_n R_j'. Since psi_n'=(B_n-A_n)/2,
the tangential coefficient is Q_n w_j R_j. The positive sum frequency
is 2(j+n)+1. The odd difference frequency is 2(j-n)+1, never zero.
If n<=j it is positive; otherwise it equals -[2(n-j-1)+1]. Sine is odd,
which gives exactly s and its reversal. This proves (1) for i=0.
The maximum sum index is M+(M+1)=2M+1. A difference index is at most M,
so no additional high frequencies arise. Finally X.grad=partial_t.

All sums are finite and the assumed regularity permits four t derivatives
of the residual. Repeated Leibniz differentiation gives (1) for i=1..4.
Differentiating the two first-order ODEs proves (2) inductively. Applying
Leibniz to e^(-2t) times psi_n or B_n-A_n proves (3). Applying the product
rule once to e^(beta sigma)C gives e^(beta sigma)(D+beta)C; induction proves
(4). The last formulas require independent derivative models or exact
exponential-polynomial input. They cannot be obtained by differentiating
a merely uniform C0 Taylor-model remainder.

## Independent finite verification design

One exact method represents sine and cosine by Gaussian-rational Laurent
polynomials in z=e^(i theta), multiplies them, and extracts sine coefficients.
A second method uses the recurrence for sin(k theta)/sin(theta), namely
U_0(x)=1, U_1(x)=2x, U_(k+1)=2xU_k-U_(k-1), x=cos(theta), together with the
cosine recurrence T_0=1,T_1=x,T_(k+1)=2xT_k-T_(k-1). Both reduce the same
product to exact finite coefficient maps. The second method can use
exact modular evaluation at enough distinct integers to prove a polynomial
identity, provided the degree and coefficient-size bound plus enough primes
prove that zero residues imply integer zero; otherwise it must retain exact
integer polynomial coefficients. Sampled floating trigonometry is insufficient.

For all five derivative orders, a separate free differential-algebra expansion
of e^(-2t) times the two scalar mode products verifies the binomial split
coefficients against successive differentiation. The exponential-polynomial
recurrences are checked on a complete monomial basis, with symbolic exponent,
and compared with the closed binomial derivative formula. Source linkage must
extract the actual AST expressions and execute or compare only the selected
pure expressions in a restricted namespace; merely repeating comments is not
linkage. All dimensions, derivative ranges, signs, and zero-padding endpoints
must be explicit in the evidence.

## Limits and open dependencies

This theorem proves exact local algebra. It does not prove that the saved
A,B,T or exponential constants enclose their canonical values, that a floating
Taylor product or convolution encloses the function, or that any _last_eps
array is the derivative of the physical residual. It does not verify a BLAS
kernel, full coefficient/remainder propagation, Bernstein transform, cutoff
composition, weak gluing, global inverse or closing inequality. Topic122 H0,
H1,H2 and the separate B3 suprema therefore remain open after this theorem.

A sound way to obtain jets is to construct separate models from (2)-(4) and
apply (1), with proved enclosures at every operation. Agreement of exact
identities is necessary but does not supply those error bounds. Any finite
source result here must be published with precisely this limitation.
