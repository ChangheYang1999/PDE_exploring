# Temperature on the source basin when beta>2

Status: proved, under the smoothness and parity assumptions below. Independent audit of the lead's Proposition B on 2026-10-20. This is not a full-plane exclusion.

## Statement

Let beta>2, lambda=(beta-2)/2, and mu=1+3 beta/2. Let W be C^2, with W(0)=0, DW(0)=diag(lambda,mu), and W1 odd in x. Let R be the basin of backward convergence to zero, and assume the flow exists for the times used. For B2 this follows from sublinearity. Let Theta be C^2 on R, even in x, vanish on the y-axis, and solve

    W.grad Theta=2 lambda Theta,
    Theta(x,y)=a x^2+o(|(x,y)|^2),    a!=0.

Then there is a C^1 function xi on R satisfying

    xi(X)=lim_{t->infinity} exp(lambda t) (phi_{-t}(X))_1,
    xi=x+o(|X|),    W.grad xi=lambda xi,
    Theta=a xi^2.

For every X in R, xi(X) has the sign of x, and xi(X)=0 if and only if x=0. The prescribed quadratic jet determines Theta uniquely among C^2 solutions on R. In particular Theta has the sign of a off the y-axis in this basin; no sign conclusion is made outside the basin.

## Proof

Since the linearization is a positive diagonal matrix, for every sufficiently small eta>0 the backward flow contracts near zero at rate lambda-eta in the Euclidean norm. Indeed, writing W(X)=DX+O(|X|^2), D=diag(lambda,mu), gives

    d/dt |phi_{-t}(X)|^2 <= -2(lambda-eta)|phi_{-t}(X)|^2

inside a sufficiently small ball. This ball is invariant under backward time. Every point of R enters it after finite backward time. Consequently its backward orbit Z(t) obeys |Z(t)|<=C_X exp(-(lambda-eta)t).

Oddness of W1 and C^2 regularity give W1(x,y)=x A(x,y), where A is C^1 and A(0)=lambda. Thus

    Z1(t)=x exp(-lambda t - integral_0^t [A(Z(s))-lambda] ds).

Since |A(Z)-lambda|<=C |Z| near zero, the integral converges absolutely. The limit defining xi exists, and

    xi(X)=x exp(-integral_0^infinity [A(phi_{-s}(X))-lambda] ds).

The exponential factor is finite and strictly positive, proving the sign and zero-set assertions.

The same contraction argument applied to the variational equation gives |D_X phi_{-t}(X)|<=C exp(-(lambda-eta)t), locally uniformly on R after a finite initial time. Since DA is bounded near zero, differentiation of the integral is justified by an integrable bound. Hence xi is C^1. The integral tends to zero as X tends to zero, so xi=x+o(|X|). Shifting time in the limit gives xi(phi_s X)=exp(lambda s)xi(X); differentiate at s=0 to obtain its transport equation.

Because Theta vanishes on the y-axis and is even in x in the B2 setting, it has the local factorization Theta=x^2 F with F continuous and F(0)=a. More generally this factorization follows here if the x derivative also vanishes on the axis, as guaranteed by the imposed B2 parity. Along the backward orbit,

    Theta(X)=exp(2 lambda t) Z1(t)^2 F(Z(t)).

Taking t to infinity gives Theta(X)=a xi(X)^2. At x=0 the same equality follows from both sides being zero.

For the uniqueness assertion it remains useful to avoid assuming factorization of a difference. The formula above implies |Z1(t)|<=C exp(-lambda t). Initially |Z(t)|<=C exp(-(lambda-eta)t). The second component satisfies

    Z2'(t)=-mu Z2(t)+O(|Z(t)|^2).

Variation of constants and mu>2 lambda give |Z2(t)|<=C exp(-2(lambda-eta)t). Choose eta<lambda/2. This is faster than exp(-lambda t), so |Z(t)|<=C exp(-lambda t). If two C^2 temperature solutions have the same quadratic jet, their difference D is o(|X|^2). Therefore

    D(X)=exp(2 lambda t) D(Z(t)) -> 0.

This proves uniqueness on R.

## Hypothesis clarification

The factorization step explicitly uses evenness of Theta in x, in addition to its vanishing on the axis. Both are hypotheses of B2. The statement is to be read with that parity assumption; no sign information follows for arbitrary non-even solutions merely vanishing on the axis. The C^2 uniqueness proof itself does not require parity, once the specified second-order jet and the W1 factorization hold.

## Dependencies and scope

Only the C^2 local source dynamics, B2 parity, and temperature transport equation are used. The lead's stronger C^(2,alpha) uniqueness hypothesis is sufficient. A generic node asymptotic need not be cited because the factorized horizontal ODE gives the exact limit directly. This result does not prove that R is the whole plane.
