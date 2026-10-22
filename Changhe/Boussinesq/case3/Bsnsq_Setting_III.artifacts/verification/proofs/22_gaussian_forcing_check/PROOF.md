# Independent Gaussian forcing and characteristic checks

Status: the analytic external inverse and local coefficients are CONFIRMED. Independent numerical tests are recorded below. The recovered fields solve a forced transport problem; they are not a self-consistent B2 candidate. Whole-plane feedback-strain quadrature is in progress.

## Exact external inverse

Fix s>0, y0!=0 and A, set Y=y-y0, S=x^2+Y^2, a=1/(2s^2), and

    Omega_ext=A x exp(-a S), B(S)=(1-exp(-a S))/S,
    Psi_ext=A s^4 x B(S).

B is analytic at0, with B(0)=a. The velocity is

    U1=-2 A s^4 x Y B'(S),
    U2=A s^4[B(S)+2x^2 B'(S)].

It is the ordinary canonical full-plane velocity, with

    U2(0)=A s^4 B(y0^2),
    c_ext=Psi_xy(0)=-2 A s^4 y0 B'(y0^2).

Proof. Differentiation gives 2B'(S)+S B''(S)=-a^2 exp(-aS). The identity Delta[x B(S)]=x[8B'+4S B''] therefore yields -Delta Psi_ext=4A s^4 a^2 x exp(-aS)=Omega_ext. At infinity B=O(S^-1), so U=O(r^-2). The rapidly decaying smooth vorticity has an absolutely defined ordinary inverse; the difference from this decaying div-curl field is harmonic and sublinear, hence constant, and the decay fixes the constant. Direct differentiation at zero gives the two displayed center formulas. The material drift is the full U2(0); it is subtracted only when forming W.

## Forced equations and source jets

Choose c_ext>2, set beta=2(c_ext-1)>2 and W=beta X+U_ext-U_ext(0). The origin is a hyperbolic source with lambda=(beta-2)/2 and mu=1+3beta/2. This external field is prescribed. The forced equations to be evaluated are

    W.grad Theta=(beta-2)Theta, W.grad Omega+Omega=Theta_x,

without imposing -curl U_ext=Omega. Let A_x(X)=W1/x, smoothly extended to the axis, and d=partial_y A_x(0). The Taylor equations imply

    Theta=x^2[1+f01 y+O(r^2)], Omega=x[b0+g01 y+O(r^2)],
    f01=-2d/mu, b0=4/beta,
    g01=(2f01-d b0)/(2beta+1).

Proof. In W.grad F+2(A_x-lambda)F=0, the coefficient of y is mu f01+2d=0. In the divided vorticity equation (A_x+1)G+W.grad G=2F+x F_x, the constant coefficient gives (lambda+1)b0=2 and the coefficient of y gives (lambda+1+mu)g01+d b0=2f01. Since lambda+mu=2beta, these are exactly the formulas stated.

On the backward basin of the origin, the center-normalized temperature is recovered by transport from this jet; the unique vorticity bounded on each compact backward orbit is

    Omega(X)=int_0^infinity e^(-t) Theta_x(phi_(-t)X) dt.

This last identity follows by integrating the scalar vorticity ODE backward, with the homogeneous term vanishing as e^(-t). It does not imply that every point belongs to the origin basin. A numerical characteristic that fails to reach the source neighborhood is reported as unfinished, not replaced with invented data.

## Independent numerical method

code_independent/gaussian_characteristics.py implements the exact Gaussian inverse above. It integrates each characteristic backward with adaptive DOP853, stopping at radius r_in. It then transports the scalar gradient and vorticity forward along the stored backward path:

    d(grad Theta)/dt=[(beta-2)I-DW^T]grad Theta,
    dOmega/dt=-Omega+Theta_x.

The initial values are the independently derived local jets. Dividing these linear unknowns by the endpoint x coordinate avoids underflow near the invariant axis. The scalar value itself is reconstructed with its exact exponential transport factor. The code uses neither the numerics lane's modal inverse, fixed-step RK4, coefficient basis nor least-squares temperature fit. A separate Cartesian inverse checks the exact external velocity. Separate coordinate finite differences check the transported gradients and both forced equations.

For c_ext=2.5, y0=2.85, s=1, the independent values are

    beta=3, A=31.700448880949384, U2(0)=3.835559286831255,
    d=-2.0854603737059105, f01=.7583492268021493,
    b0=4/3, g01=.6139017550303113.

At six off-grid sample points, the separate Cartesian inverse error is <=1.69e-14 for orders24,48,96. Characteristic runs at r_in=1e-3,3e-4,1e-4 all reach the source neighborhood and converge. With r_in=1e-4, independent fourth-order coordinate finite differences at h=.004,.002 give maximum gradient disagreement1.46e-8, |R_Theta|<=2.63e-7 and |R_Omega|<=1.18e-7. These are sampled floating-point checks; the remaining local-jet/ODE error is not an interval certification. Full point values and tolerances are in verification/gaussian_characteristic_tests.json.

The feedback c_self=(1/pi)int xy Omega/r^4 is evaluated by an independent whole-plane quadrature with r=L(t^(-beta)-1), 0<t<1, and separate Gaussian angular nodes. Both endpoints are part of the transformed full-plane integral; no exterior is set to zero. Its convergence study varies radial and angular orders, map scale L and r_in. Outputs are under verification/gaussian_feedback/. Equality c_self=c_ext would be only a scalar consistency condition on this forced problem, not proof of the full inverse closure or of a B2 profile.

Dependencies: analytic differentiation and harmonic uniqueness; source transport and local jets; SciPy's adaptive DOP853 used as a numerical method. No numerical observation is used as proof of a global solution.
