# Retaining the exact denominators in the exterior tail

## Statement and scope

Fix 0<alpha<1. Use the real or complex scalar homogeneous Euclidean Holder seminorm on R^2, the circular principal-value kernels K_xx(z)=(z_1^2-z_2^2)/(2pi|z|^4) and K_xy(z)=z_1z_2/(pi|z|^4), and the increment extension modulo constants in ../../../01_setup/PROOF.md. Let C_alpha be the norm of T_xx, equivalently T_xy, and let D_alpha be the norm of R_1^2=T_xx-I/2.

In the accepted explicit finite-part inequalities of ../PROOF.md, ../linear_remainder/PROOF.md and ../sharp_deficiency/PROOF.md, replace their common exterior term

    T(alpha) = 2^(alpha+1) alpha/pi [1/(1-alpha)+1/2-log(3/2)]

by

    T_exact(alpha) = 2^(alpha+1) alpha/pi S(alpha),
    S(alpha) = sum_(n>=0) (n+1)4^(-n)/[(2n+1-alpha)(2n+1)].       (1)

The resulting inequalities remain valid. The series is positive and converges for every 0<alpha<1. It is strictly smaller than T(alpha). It changes no other term or coupling, and may therefore be combined with the accepted sharper local deficiencies and the retained reflection savings.

For an integer N>=1, define the entirely finite upper bound

    S_N^+(alpha) = sum_(n=0)^(N-1) (n+1)4^(-n)/[(2n+1-alpha)(2n+1)]
        + (4/3)4^(-N)(N+1)/[(2N+1-alpha)(2N+1)].                (2)

Then S(alpha)<=S_N^+(alpha). The finite sum without its final term is a lower bound. Every rational alpha has rational bounds (2), so only the common powers and pi require transcendental interval evaluation.

For a uniform linear envelope over 0<alpha<=epsilon<1 at any fixed admissible pole radius rho, replace the tail contribution

    2^(epsilon+1)/pi [1/(1-epsilon)+1/2-log(3/2)]

in the accepted coefficient K_C or K_D by 2^(epsilon+1) S_N^+(epsilon)/pi. All its other terms are unchanged. This assertion concerns the same exact second terms C0=1/2+(log(2)-1)/pi and 2C0 in the accepted envelopes. It is not a claim that the new tail series is an optimal exterior transport cost.

## Exact positive-series estimate

Use the centered unit increment with poles at (1/2,0) and (-1/2,0), and let nu_phi be the difference kernel for an arbitrary phase phi. For r>1 its convergent expansion is the real part, after multiplication by a unit complex phase, of

    (1/pi) sum_(n>=0) (n+1)4^(-n) r^(-2n-3) exp(-i(2n+3)theta).

Each nonzero integer cosine frequency has angular absolute integral 4. The triangle inequality therefore gives

    integral_0^(2pi) |nu_phi(r,theta)| dtheta
        <= (4/pi) sum_(n>=0) (n+1)4^(-n)r^(-2n-3).

The antipodal transport cost uses (2r)^alpha. After subtracting its base weight 2^alpha, the positive exterior excess is at most

    (2^(alpha+1)/pi) integral_1^infinity (r^alpha-1)
                         sum_(n>=0)(n+1)4^(-n)r^(-2n-2) dr.

All summands are nonnegative. Tonelli's theorem allows interchange, and the integral of its nth summand is

    1/(2n+1-alpha)-1/(2n+1)
      = alpha/[(2n+1-alpha)(2n+1)].

This proves (1) directly with the same phase-uniform bound and the same normalization as the parent proof. At n>=1 the parent estimate used 2n+1-alpha>=2n, with strict inequality for alpha<1, and summed

    sum_(n>=1)(n+1)4^(-n)/[2n(2n+1)]=1/2-log(3/2).

Every omitted difference is positive, so T_exact(alpha)<T(alpha). No principal-value operation is present in this exterior region. The pole decomposition, local identity term and convergence of the complete operator remain those of the parent theorem.

## Certified finite remainder and the uniform envelope

For x>=1 let f_alpha(x)=(x+1)/[(2x+1-alpha)(2x+1)]. Its logarithmic derivative is

    1/(x+1)-2/(2x+1-alpha)-2/(2x+1)<0,

because 1/(x+1)<2/(2x+1) and the remaining subtracted term is positive. Hence for n>=N the rational factor is at most f_alpha(N). Summing the geometric weights gives

    sum_(n>=N) 4^(-n)f_alpha(n)
        <= (4/3)4^(-N)f_alpha(N),

which proves (2). The difference between the finite upper and lower bounds is exactly the displayed positive remainder, whether or not that bound is sharp.

Every summand of S(alpha) is increasing in alpha. Consequently, for 0<alpha<=epsilon,

    T_exact(alpha)/alpha
      <= 2^(epsilon+1)S(epsilon)/pi
      <= 2^(epsilon+1)S_N^+(epsilon)/pi.

The accepted envelope proof bounds the exterior term only through this quotient. Its substitution is therefore valid without changing the estimates for the local expansion, the middle part or the deficiencies. The retained-reflection modification acts on separate local edges and may be subtracted from the original bound exactly once.

## Dependencies and status

The analytic dependencies are the accepted finite-part decomposition and antipodal exterior estimate, the sharp-deficiency refinement if used, and the existing uniform-envelope proof for its application. All series, cutoffs and constants above are explicit. No numerical value is asserted here. Written before numerical evaluation; OPEN pending independent lead cross-read.
