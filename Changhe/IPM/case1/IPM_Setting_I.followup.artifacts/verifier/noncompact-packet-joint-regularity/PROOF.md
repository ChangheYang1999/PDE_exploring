# A smooth scalar packet trace without joint C1 regularity

Date: 2026-10-21. Status: CONFIRMED by independent proof, exact scaling checks and completed actual Claude Opus5.5 review.

## Statement, notation and scope

Use the explicit packet from ../noncompact-packet-counterexample/PROOF.md. Namely, for t>0 let

    u(t)=t^(-1/2) exp(-(log t)^2) sin(2pi log t),
    Phi(t)=u(t), Phi(-t)=-u(t), Phi(0)=0,
    c_F=(2pi)^(-2),
    V(s,y)=-4c_F integral_0^infinity sin(yr)r^(-2)
                  integral_0^infinity u(t)sin(s t r^2)
                                     (1+t^2r^2)^(-1/2)dt dr.       (1)

Then V is real and continuous on R^2, has at most linear growth, and is not C1 on any neighborhood of (0,0). Both coordinate partial derivatives at (0,0) nevertheless exist and are zero. Its scalar first trace G(s)=partial_y V(s,0) exists and is smooth on R, with nonzero G'(0), as proved in the preceding result. Thus that smooth scalar trace does not give joint C1 regularity.

No claim about Frechet differentiability at the single point, a sharp positive Holder class, smoothness off the origin, a coupled IPM profile or an endpoint is made. The point (0,0) here is the origin of a frozen source packet, not the physical normalized center of an IPM profile.

## Absolute moments, continuity and polynomial growth

The preceding proof establishes that u is nonzero and that every absolute power moment integral_0^infinity |u(t)|t^p dt is finite. This follows directly on setting t=exp(z): the integrand is bounded by exp(-z^2+(p+1/2)z). We only need the moments with p=1 and p=-1 here.

For 0<r<=1, use |sin(s t r^2)|<=|s|t r^2 and the bound1 for the weight and the other sine. The absolute double integral of (1) on this range is bounded by

    |s| integral_0^1 dr integral_0^infinity |u(t)|t dt.

For r>=1, use (1+t^2r^2)^(-1/2)<=1/(tr) and bound both sines by1. The absolute double integral is bounded by

    integral_1^infinity r^(-3)dr
                       integral_0^infinity |u(t)|t^(-1)dt.

Both bounds are finite, locally uniform in (s,y), and pointwise in the joint integration variables. Dominated convergence gives continuity, and the same estimates give

    |V(s,y)|<=C(1+|s|)<=C(1+|(s,y)|).                    (2)

Equation (1) also gives V(s,0)=V(0,y)=0, so both coordinate partial derivatives at zero exist and equal zero. This does not assert continuity of either derivative in a neighborhood.

## The Fourier density and its extension

Use fhat(xi,eta)=integral exp(-i(s xi+y eta))f(s,y)dsdy, with inverse factor c_F. Away from eta=0 the Fourier density is

    D(xi,eta)=sgn(eta)|eta|^(-4)
       (1+xi^2/eta^2)^(-1/2) Phi(xi/eta^2).             (3)

Here the extension is the limit with |eta|>epsilon. We justify both existence and identification rather than assuming a compact-support theorem applies to Phi.

For a Schwartz test function f, use xi=t r^2, eta=plus or minus r and then pair positive and negative t. The truncated pairing equals the integral over r>epsilon,t>0 of

    r^(-2) u(t)(1+t^2r^2)^(-1/2)
       [f(t r^2,r)-f(t r^2,-r)
        -f(-t r^2,r)+f(-t r^2,-r)].                   (4)

For r<=1, the bracket is at most4 t r^3 ||partial_xi partial_eta f||_infinity by two applications of the fundamental theorem of calculus, even when t r^2 is large. Consequently the absolute integrand is bounded by4r |u(t)|t times that seminorm. For r>=1, the bracket is at most4||f||_infinity and the weight gives the bound4r^(-3)|u(t)|/t times that seminorm. The moment bounds prove convergence and continuity in finitely many Schwartz seminorms. Thus (4) defines a tempered distribution.

Fourier inversion of the doubly paired expression gives exactly (1), because the two odd frequency pairings each supply2i sin. The interchange with a Schwartz spatial test function is justified by the same estimates used for (2), after integrating its absolute value against1+|s|. Therefore the distribution (4) is the Fourier transform of the continuous function V. No choice of an additional distribution on eta=0 is left implicit.

## A compact frequency projection detects the nonsmooth component

At t_0=exp(1/4), u(t_0)>0. Choose a nonnegative, nonzero smooth multiplier theta(zeta,nu) supported in a sufficiently small compact neighborhood of (t_0,1), on which nu>0, zeta>0 and u(zeta/nu^2)>0. For integers n>=0 define

    theta_n(xi,eta)=theta(2^(-2n)xi,2^(-n)eta),
    T_n V=FourierInverse(theta_n D).

These products are supported away from eta=0, so they use only the ordinary density (3). Changing variables xi=2^(2n)zeta, eta=2^n nu yields exactly

    2^(2n) (T_n V)(0,0)
      =c_F integral theta(zeta,nu) nu^(-4)
               (2^(-2n)+zeta^2/nu^2)^(-1/2)
                      u(zeta/nu^2) dzeta dnu.          (5)

The Jacobian is2^(3n); the density prefactor is2^(-4n); the angular weight contributes2^(-n). Their product is2^(-2n). On the fixed support of theta both nu and zeta have positive lower bounds. Dominated convergence in (5) gives

    2^(2n) (T_n V)(0,0) -> H_0,
    H_0=c_F integral theta nu^(-4)(zeta^2/nu^2)^(-1/2)
                                         u(zeta/nu^2) >0.          (6)

Positivity follows from the chosen support and nonzero nonnegative theta. There is no oscillatory cancellation in (6), although the complete packet has vanishing scalar weighted moments.

## Consequence of hypothetical local C1 regularity

Suppose V were C1 on a neighborhood of zero. Choose a compactly supported smooth cutoff chi, equal to1 near zero and with support in that neighborhood. Put f=chi V and w=(1-chi)V. Then f is globally C1 with compact support, and w vanishes on a fixed ball and satisfies the linear growth bound (2).

Let K be the inverse Fourier transform of theta. It is Schwartz. The kernel of T_n is

    K_n(s,y)=2^(3n) K(2^(2n)s,2^n y).

For Y outside the ball where w vanishes, the scaled Euclidean distance is at least2^n|Y|. For any desired L>0, choose N>3+L and N>3. Schwartz decay gives

    |(T_n w)(0)|
      <=C_N 2^(3n) integral_(|Y|>=delta)
             (1+2^n|Y|)^(-N)(1+|Y|)dY
      <=C'_N 2^((3-N)n)=O(2^(-Ln)).                  (7)

The last integral after extracting2^(-Nn) is finite because |Y|>=delta>0 and N>3. Polynomial growth makes the convolution absolutely convergent.

Because theta is supported away from zeta=0, the multiplier

    b(zeta,nu)=theta(zeta,nu)/(i zeta)

is smooth and compactly supported. Write B=FourierInverse(b) and B_n(s,y)=2^(3n)B(2^(2n)s,2^n y). Then B is Schwartz, integral B= b(0,0)=0, and the Fourier derivative identity gives

    T_n f=2^(-2n) B_n * partial_s f.                    (8)

The function F=partial_s f is continuous with compact support, hence uniformly continuous and bounded. After changing variables to the unscaled kernel and using integral B=0,

    (B_n*F)(0)=integral B(Z)
                [F(-2^(-2n)Z_1,-2^(-n)Z_2)-F(0)]dZ ->0.          (9)

For completeness, on each fixed bounded Z-set uniform continuity makes the bracket uniformly small, while the complement has arbitrarily small L1 mass of B and bracket bounded by2||F||_infinity. This proves (9) without a rate assumption.

Combining (7)-(9), with L>2, gives

    2^(2n)(T_n V)(0)=o(1)+O(2^((2-L)n)) ->0,

contradicting the strictly positive limit (6). Thus V cannot be C1 on any neighborhood of zero.

## Dependencies and verification

The explicit noncompact packet and its smooth scalar trace are in ../noncompact-packet-counterexample/PROOF.md. The compact frequency projection method extends the idea in ../packet-sharpness-audit/PROOF.md, but all estimates needed for this noncompact data and the weaker polynomial growth bound are given above. The proof uses no full-plane nonlinear inverse estimate and no compact support for Phi.

Own code will check the exact scaling powers and the positivity/approach of the projected amplitude for one explicit compact multiplier. Numerical quadrature is only an illustration of (5)-(6), not the proof of positivity or of non-C1 regularity. Review evidence and source pins belong in verification/. No formal proof assistant build is used.
