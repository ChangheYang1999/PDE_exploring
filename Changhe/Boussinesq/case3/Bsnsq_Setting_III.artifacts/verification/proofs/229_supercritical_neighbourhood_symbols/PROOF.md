# Supercritical separated temperature near the entire axis under symbol bounds

## Statement, status and dependencies

Fix beta>2. Let W,Theta,Omega be smooth on R2. Assume div W=2beta, Omega=-curl W=partial_y W1-partial_x W2, W(0)=0, W=beta X+o(|X|) uniformly at infinity, and the two equations

    W.grad Theta=(beta-2)Theta,
    W.grad Omega+Omega=Theta_x.

Assume B2 x reflection: Theta,W2 even, Omega,W1 odd. Assume Theta(0,y)=0 and Theta(x,y)=a0 x²+O(|X|³) at0, a0!=0. In addition assume the following axis derivative bounds, each with its own finite constant and sufficiently large radius:

    |partial_x^j Theta(0,y)| <= C_j |y|^(1-2/beta-j),       j>=0,
    |partial_x^j W2(0,y)| <= D_j |y|^(1-1/beta-j),          j>=1.       (S)

Then there is no open neighbourhood N of the ENTIRE axis, positive function rho:R->(0,infinity), and function H defined on an interval containing0 and all x/rho(y) represented in N, with Theta(x,y)=H(x/rho(y)) on N. No initial regularity of rho or H is required.

This is a restricted representation theorem. Its complete argument is below, written before independent algebra controls and model review. The explicit(S) theorem and the broad polynomial-vorticity application of Section9 are CONFIRMED by the verifier after independent derivation, 53 exact algebra controls and 23 rescaling/dependency controls. Four requests to actual Claude Opus5.5 returned no written audit; this availability limitation is recorded in verification/review_adjudication.md and is not an endorsement. A separate lead-lane audit of this new theorem remains pending. The broad-target application uses the previously audited class reduction and all-order symbol estimates, checked explicitly in Section9. The theorem with explicit(S) is self-contained, using ordinary calculus and ODE facts. No analyticity, exact convergent Taylor series, global strip width or full-plane numerical inverse is assumed. General B2 temperatures remain outside the representation.

## 1. Smoothness and transport coordinates

As in the independent bootstrap P227, the slice y=0 gives H(k)=Theta(k rho0,0) near0, where rho0=rho(0)>0. Thus H is smooth and even near0, H''(0)=2a0rho0²!=0. For every fixed y, differentiating in x at0 gives Theta_xx(0,y)=H''(0)/rho(y)². Hence rho=sqrt(H''(0)/Theta_xx(0,y)) is smooth and positive everywhere. Set a=rho/rho0 and h(k)=H(k/rho0), then relabel h as H; a(0)=1 and A0:=H''(0)=2a0. If A0<0, use S(x,y)=(x,-y), Wnew=S W(SX), Thetanew=-Theta(SX), Omeganew=-Omega(SX). These preserve all assumptions including(S) and map N to S N, while reversing A0. Assume A0>0.

Write k=x/a(y), A(y)=integral_0^y a, alpha=(beta-2)/2, L=2beta-alpha=1+3beta/2, and define near0

    q(k)=(beta-2)H(k)/H'(k), d(k)=2beta-q'(k).

Hadamard division by k, using H''0!=0, shows q is smooth odd, q(0)=0, q'(0)=alpha. Thus d is smooth even and d(0)=L. For any compact axis segment [-Y,Y], a positive-width rectangle in(k,y) lies in the original open neighbourhood. Shrink its k width so H'!=0 at nonzero k. Define V(k,y)=W2(ka(y),y), Q=W1(ka(y),y)-k a'(y)V. The identities

    W.grad Theta=H'Q/a,
    Q_k+(aV)_y=2beta a

give Q=a q and

    aV=d(k)A+C(k),
    W1(ka,y)=a q+k a' V,                  (1)

where the SAME germ C(k)=W2(k,0) is used on every compact segment. Indeed integration from0 to y stays in that rectangle and a(0)=1. C is smooth even and C(0)=0. Every identity of k jets below therefore holds at every y with common constants. It requires no uniform strip width as |y| tends to infinity.

## 2. The scale is coercive and has a precise logarithmic exponent

Let phi(y)=W2(0,y)=L A(y)/a(y). It has the sign of y, only zero0, and phi'(0)=L. The global sublinearity gives phi(y)/y->beta at both ends. On the positive end

    A'/A=L/phi,  y A'/A->delta=L/beta=3/2+1/beta.

For every sufficiently small epsilon>0, integrate (delta-epsilon)/y<=A'/A<=(delta+epsilon)/y from a fixed large point. Combining a=L A/phi with phi comparable to beta y gives constants c,C>0 such that

    c y^(gamma-epsilon)<=a(y)<=C y^(gamma+epsilon),
    gamma=delta-1=1/2+1/beta in(1/2,1).                    (2)

On the negative end apply the same argument to a(-t), -A(-t), -phi(-t), t>0. Thus(2) holds with |y| at both ends. In particular a tends to infinity at both ends and a=o(|y|). No derivative of the asymptotic phi~beta y was taken.

## 3. Every higher temperature jet vanishes

For each integer j>2, the representation gives the exact axis identity

    partial_x^j Theta(0,y)=H^(j)(0)/a(y)^j.

If H^(j)(0)!=0, the upper bound for a in(2) and(S) imply

    c |y|^(-j gamma-j epsilon)<=C |y|^(1-2/beta-j).

But the difference between the lower-bound exponent and the upper-bound exponent is

    j(1-gamma)-(1-2/beta)-j epsilon
      =(j/2-1)(1-2/beta)-j epsilon.

It is positive when epsilon is chosen small, since j>2 and beta>2. This is impossible as |y| grows. Thus H^(j)(0)=0 for every j>2. With H(0)=H'(0)=0 and H''(0)=A0, the function H(k)-A0 k²/2 is flat at0. Consequently q(k)-alpha k and d(k)-L are flat there, by smooth division by k. This is a statement about jets only; no equality of H with a quadratic on an interval is inferred.

## 4. Only finitely many jets of C survive

For integer j>=1, differentiate the second component of(1) in x at0. Since all positive-order derivatives of d at0 vanish,

    partial_x^j W2(0,y)=C^(j)(0)/a(y)^(j+1).             (3)

If C^(j)(0)!=0, the same lower-bound argument with(S) gives exponent difference

    j-1+1/beta-(j+1)gamma-(j+1)epsilon
      =j(1/2-1/beta)-3/2-(j+1)epsilon.

For j>3beta/(beta-2) this is positive for small epsilon, a contradiction. Thus every derivative C^(j)(0) above that finite threshold vanishes. Let

    P(k)=sum_{0<=j<=floor(3beta/(beta-2))} C^(j)(0) k^j/j!.

P is a finite even polynomial with P(0)=0, and C-P is flat at0. Equality C=P near0 is neither claimed nor needed.

## 5. The quadratic coefficient of C is nonzero

Write C(k)=c2 k²+O(k4). Since d-L is flat, direct negative curl in(1) gives

    eta(y):=Omega_x(0,y)=-phi''(y)-2c2/a(y)^3.          (4)

Differentiating the vorticity equation in x on the axis, using parity and div W, gives

    phi eta'+(2beta+1-phi')eta=A0/a².

Since phi'=L-phi a'/a and 2beta+1-L=beta/2, put r=a eta to obtain

    phi r'+(beta/2)r=A0/a.                             (5)

For the backward scalar flow y'=phi(y), the trajectory from y0 stays between0 and y0 for all negative time and tends to0. It is defined for all negative time because it stays in a compact set, and phi has no other zero. Integrating(5) with exp(beta s/2), the bounded endpoint term vanishes at negative infinity. Hence

    r(y0)=A0 integral_{-infinity}^0 exp(beta s/2)/a(y(s)) ds>0.

The positive minimum of a on that compact interval ensures convergence. Thus eta>0 on R. If c2>=0, (4) makes phi''<0 on R. For y<0, phi'(y)>phi'(0)=L, so phi(y)<L y and phi(y)/y>L>beta. This contradicts phi(y)/y->beta. Therefore c2<0. In particular P has a highest nonzero even degree n>=2.

## 6. A polynomial residual follows from flat jets, not analyticity

Build a global smooth comparison field using the same positive a but the polynomial P:

    D=L A+P(k),
    Wtilde2(ka,y)=D/a,
    Wtilde1(ka,y)=a alpha k+k a'D/a,
    Thetatilde(ka,y)=A0 k²/2.

It obeys div Wtilde=2beta and the temperature equation everywhere by the coordinate calculation of Section1. Do NOT assume Wtilde is sublinear. We will use only the already established coercivity of a.

For each fixed y, in a neighbourhood of k=0, W-Wtilde is flat in k, with every mixed y derivative also flat. This follows directly from(1): q-alpha k, d-L and C-P are common flat germs, with coefficients smooth in y. The same holds for Theta-Thetatilde, Omega-Omegatilde, and their differentiated PDE residuals, where Omegatilde is the physical negative curl. Since the original vorticity equation vanishes, the residual of Wtilde,Thetatilde,Omegatilde has every k derivative zero at0 for each y.

However that comparison residual, multiplied by a(y), is a FINITE POLYNOMIAL in k. Write B=a''/a-2a'^2/a². Direct physical differentiation gives

    Omegatilde(ka,y)=L k a'+k D B-(1+k²a'^2)P'/a².      (6)

The exact multiplied residual is

    a alpha k partial_k Omegatilde
      +D partial_y|k Omegatilde+a Omegatilde-A0 k.       (7)

All its coefficients must vanish because every derivative at0 vanishes. Thus(7) is identically the zero polynomial for every y, even if the original flat remainders were nonzero. This is finite polynomial algebra, not analytic continuation of the original fields.

## 7. The highest polynomial degree gives the contradiction

Let p_n!=0 be the coefficient of k^n in P, n>=2. Put p=a'/a, so B=p'-p². In(6) the coefficient of k^(n+1) is

    p_n(B-n p²).

The unique contribution at degree2n+1 in(7) comes from P partial_y Omegatilde; all other terms have degree at most n+1. It is

    p_n² [B'-n(p²)']
      =p_n² [p''-2(n+1)p p'].

Hence p'-(n+1)p²=K for one real constant K on R. The positive smooth function v=a^(-(n+1)) then obeys

    v''+(n+1)K v=0.

By Section2, v tends to0 at both ends of R. No nonzero solution of this constant-coefficient ODE can do so. If K=0 it is affine; if K>0 it is a sine/cosine combination and cannot tend to0 at either end unless zero; if K<0 it is a linear combination of exp(mu y) and exp(-mu y), with mu=sqrt(-(n+1)K)>0, and the two end conditions annihilate both coefficients. This contradicts v>0. The theorem follows.

## 8. Application and limits

The only additional assumption beyond smooth B2 and the representation is(S). In a class where full symbol bounds Theta in S^(1-2/beta) and U-U(0) in S^(1-1/beta) have been independently established, (S) follows by evaluating Cartesian derivatives on the axis; partial_x^j(beta y)=0 for j>=1. The existing verifier P150 proof of finite exterior expansions explicitly checks these symbol bounds through P36 local smooth continuation and the self-similar rescaling. Its broad-target applicability also uses the separately audited polynomial-vorticity class reduction. Those dependency statements should be frozen and checked before advertising the corollary for every polynomially controlled target profile.

The beta2 endpoint is outside the jet-threshold argument because 1/2-1/beta vanishes there; it has the separate P227 proof. A representation near only a bounded axis segment does not provide the large-|y| identities and is not excluded here. No general separated finite sum, approximate separation, or arbitrary smooth temperature is excluded. No numerical state establishes any part of this proof.

## 9. Checked deduction of(S) in the broad polynomial-vorticity target

Assume the original smooth B2 target, beta>2, U=o(r) uniformly and |Omega|<=C(1+r)^k for some finite k>=0. The canonical relative field is V=U-U(0); no assertion U(0)=0 is made. P40, whose complete local logarithmic-strain and characteristic proof was independently checked, yields |Omega|<=C_delta r^-delta for every 0<delta<1/beta and identifies V with the absolutely convergent once-subtracted whole-plane kernel. Its hypotheses require no derivative decay and no temperature bound. The B2 parity, axis and nonzero center jet are retained. This is precisely the power-decaying class to which P33 applies.

For s=1/beta and m=1-2s, P33 gives

    |V|<=C r^(1-s), |DV|<=C r^-s, |Omega|<=C r^-s,
    |Theta|<=C r^m, |grad Theta|<=C r^-2s.

P33 and its temperature-limit dependency give uniform angular limits of the two scalars; P35 proves local uniform convergence of the rescaled velocity by the canonical inverse. P36 proves the local all-spatial-derivative lemma directly with shrinking compact cutoffs and the same-cutoff div-curl estimate; it does not assume global Sobolev norms, boundary data, or bounded derivatives of the original profiles at infinity. Its induction uses only the displayed first-derivative and amplitude bounds on compact physical annuli, then gives every higher spatial derivative there. The preexisting P36 proof is the dependency for that analytic step, not a numerical test.

Here is the rescaling and its gauge check explicitly. Put t=-tau<0 and

    u_tau(z)=tau^(beta-1)V(tau^-beta z),
    omega_tau(z)=tau^-1 Omega(tau^-beta z),
    theta_tau(z)=tau^(beta-2)Theta(tau^-beta z).

Differentiation gives omega_t+u.grad omega=tau^-2[Omega+(beta X+V).grad Omega]=tau^-2 Theta_x=theta_z1, and theta_t+u.grad theta=tau^(beta-3)[-(beta-2)Theta+(beta X+V).grad Theta]=0. Also div u=0 and -curl u=omega. Thus these are exact physical vorticity/temperature equations for the relative field, which is what P36 uses. This is an auxiliary rescaling justified directly by the equations; it does not reset the canonical observer velocity or impose a stationary material center in the original physical reconstruction.

On any fixed compact annulus away from z=0, the displayed estimates give uniform bounds on u,Du,omega,theta,grad theta. For example Du_tau=tau^-1 DV(tau^-beta z) and grad theta_tau=tau^-2 grad Theta(tau^-beta z); their powers of tau cancel. The angular limits and P35 give local uniform scalar and velocity limits. P36 therefore bounds every D_z^j derivative uniformly on a slightly larger fixed annulus. For r=tau^-beta and |z|=1,

    D_z^j u_tau(z)=r^(s-1+j) D_X^j V(rz),
    D_z^j omega_tau(z)=r^(s+j) D_X^j Omega(rz),
    D_z^j theta_tau(z)=r^(-m+j) D_X^j Theta(rz).

Consequently for every finite j>=0, with its own constant,

    |D_X^j V(X)|<=C_j |X|^(1-s-j),
    |D_X^j Omega(X)|<=C_j |X|^(-s-j),
    |D_X^j Theta(X)|<=C_j |X|^(m-j).

No differentiation of a mere pointwise asymptotic is involved. Evaluating at X=(0,y), and noting partial_x^j(beta y)=0 for j>=1, proves(S). Hence the theorem excludes an entire-axis neighbourhood representation for every smooth profile in the polynomial-vorticity broad target at beta>2. It continues to be only a representation exclusion. There is no restriction on general smooth temperatures outside that family, and no full NO endpoint follows.
