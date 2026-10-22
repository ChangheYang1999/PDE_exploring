# Horizontal primitive reduction of B2 to a stream equation

Status: CONFIRMED derivation and implementation controls, 2026-10-21T05:32:43.910104+00:00. Numerical search has no accepted candidate. This is an equivalent reformulation under the stated regularity and gauge, not an existence or nonexistence theorem. Written before the implementation.

## Statement, hypotheses, notation and scope

Let beta>2 and a0!=0. Let Psi be a smooth function on the plane, odd in x. Define Omega=-Delta Psi, U=(-Psi_y,Psi_x), V=U-U(0), and W=beta X+V. Require that U arises from the chosen canonical whole-plane inverse, up to the single constant removed in V. A sufficient class used in the numerical representation below is |D^j V|<=C_j<X>^(1-alpha-j), |D^j Omega|<=C_j<X>^(-alpha-j), alpha=1/beta, with the velocity equal to the subtracted whole-plane inverse. The linear stream gauge has no effect on W. No boundary condition is imposed on y=0. Put c=Psi_xy(0)=1+beta/2 and q=Omega_x(0)=4a0/beta. These are imposed exactly by the stream chart.

For every such Psi there is a unique smooth, even temperature with Theta(0,y)=0 satisfying the vorticity equation W.grad Omega+Omega=Theta_x. It is

    F(x,y)=W.grad Omega(x,y)+Omega(x,y),
    Theta(x,y)=int_0^x F(s,y) ds.                         (1)

This temperature has the prescribed leading term a0 x^2. The pair is a B2 profile if and only if it also satisfies the single integral equation

    W1(x,y) F(x,y)+W2(x,y) int_0^x F_y(s,y) ds
                  -(beta-2) int_0^x F(s,y) ds=0.        (2)

Any growth, positivity, smooth angular tail, physical norm, or asymptotic compatibility requirement must still be checked for the temperature in (1). In particular, a trial Psi with suitable slow tails need not yield a temperature in the prompt's final profile class. No claim about existence follows from removing one equation algebraically.

## 1. Smoothness, parity and uniqueness

The reflected vector field has W1 odd and W2 even in x. Omega is odd, Omega_x is even, and Omega_y is odd. Thus F is odd. Write

    Theta(x,y)=x int_0^1 F(tx,y) dt.

Differentiation on the fixed compact t interval proves smoothness jointly in x,y. The primitive of an odd function with lower endpoint0 is even. Also Theta(0,y)=0. The fundamental theorem gives Theta_x=F exactly. Any two such temperatures have x derivative0 and value0 on x=0, so their difference is zero. Substitution into the temperature equation proves the equivalence with (2). These statements require only Psi in C^infinity here; there is no exchange with a far-field limit.

## 2. Axis-divided form and the center jet

Smooth oddness permits the smooth even quotients

    A=W1/x, B=W2, Q=Omega/x.

The quotient identities extend across x=0 by the integral formula h(x,y)/x=int_0^1 h_x(tx,y)dt. Therefore

    F=x H,
    H=(A+1)Q+x A Q_x+B Q_y,
    S(x,y)=int_0^1 t H(tx,y)dt,
    Theta=x^2 S.                                       (3)

The defining relation implies 2S+x S_x=H. It follows either by differentiating the primitive or by integrating d/dt[t^2 H(tx,y)]. Let Sy=int_0^1 t H_y(tx,y)dt. Then the divided temperature residual is

    R_T/x^2=A H+B Sy-(beta-2)S.                         (4)

The grouped divided normalizer required by the prompt is

    N_T/x^2=|A H|+|B Sy|+|(beta-2)S|.                  (5)

The divided vorticity residual is identically0, with grouped terms A(Q+xQ_x), BQ_y, Q, -H. Their sum is0. At the axis, (3)-(5) are evaluated by their smooth extensions, without a fitted cutoff or added denominator floor.

At the center V(0)=0, B(0)=0, A(0)=beta-c=(beta-2)/2=:lambda, Q(0)=q. Thus H(0)=(lambda+1)q=2a0 and S(0)=a0, giving Theta=a0x^2+terms of total degree at least3. This also makes the leading thermal residual zero since 2lambda=beta-2. No y parity is imposed.

## 3. Field derivatives and coefficient differentiation

All entries of A,B,Q and their derivatives are linear in the stream coefficients except the fixed beta terms. Off the axis, at most four spatial derivatives of Psi are required:

    H_y=A_y Q+(A+1)Q_y+x A_y Q_x+x A Q_xy
                         +B_y Q_y+B Q_yy.             (6)

Off the axis Q_yy divides a fourth derivative of Psi by x. Its axis limit is Q_yy(0,y)=Omega_xyy(0,y), which uses a fifth-order stream jet. Uniform derivative estimates through the axis therefore require fifth-order stream control. The parity quotient is taken symbolically and Psi is smooth throughout, so no numerical cancellation at x=0 or unjustified finite-regularity assertion is used.

For a coefficient variation dC, denote the induced linear variations by dA,dB,dQ and so on. The exact differential is

    dH=dA(Q+xQ_x)+(A+1)dQ+x A dQ_x+dB Q_y+B dQ_y,
    dH_y=dA_y(Q+xQ_x)+A_y(dQ+x dQ_x)
        +dA(Q_y+xQ_xy)+(A+1)dQ_y+x A dQ_xy
        +dB_y Q_y+B_y dQ_y+dB Q_yy+B dQ_yy.           (7)

Integrating these variations gives dS,dSy. The differential of (4) is

    dR=dA H+A dH+dB Sy+B dSy-(beta-2)dS.              (8)

For a fixed beta and an affine center-constrained stream chart, H and S are quadratic polynomials in the free coefficients, and the residual is cubic. Formula (8) is the exact Jacobian of that residual. When a fixed numerical quadrature replaces the integrals, the same algebra gives the exact Jacobian of the quadrature residual. It does not prove quadrature accuracy. If beta is free, the beta column must also differentiate the basis exponents, the center chart and the beta factors; a centered finite difference of the entire residual is a separate numerical approximation to that column.

## 4. Whole-plane inverse and gauge of the trial basis

The independent representation from packet108 uses linear combinations of

    x R^(1-alpha-shift) T_i(2R^(-alpha)-1) T_j(y/R),
    R=sqrt(1+x^2+y^2), shift in {0,1},

with each basis stream's derivative Psi_x(0) subtracted as a linear x term. Its velocity is exactly zero at0 in this relative gauge, rather than a fitted independent drift. Every unmodified term has stream growth at most R^(2-alpha), velocity growth at most R^(1-alpha), and the differentiated symbol estimates required above. The subtracted gauge contributes only a constant velocity before relative normalization. Omega has the stated R^(-alpha) derivative bounds. The once-subtracted Biot-Savart integral is absolutely convergent: at infinity its kernel is O_X(|Y|^-2), so its product with Omega integrates as int r^(-1-alpha)dr. Its local 1/|X-Y| singularity is integrable.

The resulting inverse is sublinear. For completeness split its integral into |Y|<=2|X| and |Y|>2|X|; the latter is O(|X|^(1-alpha)), the former after scaling the two kernels is bounded by C(1+|X|^(1-alpha)) using 0<alpha<1. The reconstructed velocity and the explicitly differentiated stream have the same divergence and curl. Their difference is an entire harmonic vector field, of sublinear growth, hence constant: apply the mean-value derivative estimate on balls of radius r and let r tend to infinity. Their value at0 is zero, so the constant is zero. An independently coded physical-space quadrature is still used as an implementation check.

This representation fixes a0 by the exact spatial scaling, but retains arbitrary signs of the free coefficients. Its finite angular/radial resolution is a trial class, not a class reduction theorem.

## 5. Quadrature and far-field limitations

On every fixed compact set, Gauss-Legendre quadrature of the smooth t integrands in (3) and their differentiated versions converges with increasing order. For a finite rule S_N, the relation 2S_N+x(S_N)_x=H generally fails, even though its separately stored intended Theta_x=xH would satisfy the vorticity equation. Therefore an evaluator must distinguish (i) the exact primitive with independently converged quadrature and (ii) the finite quadrature field. Claiming an identically zero discrete vorticity residual by assigning Theta_x=xH without checking the primitive would be circular. Independent Cartesian finite differences of the quadrature-produced temperature and quadrature-order refinements are required.

At large |x| a fixed t rule can miss a core of width O(1/|x|), so compact-set convergence is not a uniform whole-plane bound. Held-out far-field values must use adaptive quadrature or physical-s intervals that resolve the core, and must compare independent orders. The primitive of a smooth decaying F can have an angular far-field limit with inadequate smoothness near horizontal directions. In particular, integrating a homogeneous leading source separately may introduce |y|^(1-2alpha) terms. This is a warning about an unverified tail inference, not an assertion that such a term occurs in every trial. The full prompt's tail and absolute residual diagnostics remain necessary.

## Dependencies and verification plan

Uses elementary parity division, differentiation under compact integrals, the fundamental theorem of calculus, the subtracted whole-plane inverse proved in earlier packets, and the independent basis108/114. Before fitting: exact polynomial manufactured solution, an explicit nonprofile, arbitrary coefficient symbolic identities, high-precision spatial derivatives, analytic Jacobian versus independent coefficient differences, quadrature convergence including a missed-core counterexample, and the independently implemented full-plane inverse. After fitting: held-out residuals using independent derivatives and quadrature, exact center values, temperature/vorticity signs and amplitudes, tail diagnostics and domain/refinement comparisons. These finite checks supplement the derivation and cannot prove an infinite-domain profile.

Written UTC: 2026-10-21T05:19:02.275470+00:00

### Quadrature coordinate chosen before tests

In addition to the linear t rule, use s=sinh(u), u=asinh(x)v, v in[0,1]. The node t=sinh(asinh(x)v)/x has the smooth even limit v at x=0, and the S weight is (asinh(x)/x)t cosh(asinh(x)v)dv with limit v dv. This follows directly from s ds/x^2. All nodes have the same y, so the Sy formula remains exact for the discrete sum. For large |x|, this coordinate resolves a fixed physical core using logarithmic horizontal scale; for |x| of order1 or smaller it is close to the linear rule. Finite-order quadrature still requires error checks.

### Fit weight selected before fitting

For the generic smooth slow-tail ladder, Theta has degree1-2alpha and V has degree1-alpha, so the first transport interaction has degree1-3alpha. Dividing by x^2 gives degree-1-3alpha off the axis. The fit therefore uses the declared weight R^(1+3alpha_ref)/a0, with alpha_ref fixed within each run when beta is free. This is an objective choice, not a pointwise PDE normalizer or a claimed tail estimate. Every reported ratio uses the physical term sum without this weight.
