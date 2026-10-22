# Power-decaying vorticity need not satisfy the orbit-integral derivative hypothesis

Date:2026-10-20. Status: CONFIRMED kinematic counterexample. Independent derivation and detailed Opus18 audit checked. This is not a solution of the B2 transport equations.

## Exact statement

Fix beta>0 and any desired real center strain c and vorticity slope b0. There exist smooth fields U and Omega on the plane such that

    div U=0, -curl U=Omega,
    U is bounded, |Omega(X)| <= C/(1+|X|),
    Omega(-x,y)=-Omega(x,y), U1(-x,y)=-U1(x,y), U2(-x,y)=U2(x,y),
    Psi_xy(0)=c, Omega_x(0)=b0, U=(-Psi_y,Psi_x),

where U can be taken to be the ordinary absolutely convergent whole-plane Biot-Savart inverse of Omega. For W=beta X+U(X)-U(0) and its globally defined flow phi_t, there are arbitrarily large starting points Y on the positive y-axis for which

    integral_0^infinity |DU(phi_t Y)| dt = infinity.       (1)

Here any fixed matrix norm may be used. In particular the sufficient scattering hypothesis

    sup_{|Y|>=R} integral_0^infinity |DU(phi_t Y)|dt ->0     (D)

does not follow from smoothness, bounded velocity, zero-order power decay of vorticity, parity, and the center jets. We can set c=1+beta/2 and b0=4/beta and add a smooth compactly supported even temperature with leading term x^2 and zero axis values. These kinematic data still fail the profile transport equations. The velocity derivative DU is unbounded: at the center of block j, its axis derivative has size at least A R_j^3 minus lower-order errors. The construction has extremely fine oscillations at increasing distances. This says nothing against a bootstrap that assumes or derives bounded DU.

## Fixed choices and the vorticity blocks

Choose a nonzero nonnegative smooth function f with compact support in(1,2) and f<=1. Choose a smooth cutoff eta with values in[0,1], eta(z)=1 for |z|<=2pi and eta(z)=0 for |z|>=3pi. Take eta even. Put

    R_j=2^(j+6), epsilon_j=1/R_j, N_j=R_j^4, j=1,2,...,
    k_n=4^n, n=1,2,...,
    A=integral_1^2 f(s)e^(-s)ds >0.

Every N_j is a finite positive integer. Define

    omega_j(x,y)=epsilon_j eta(y-R_j)
        sum_{n=1}^{N_j} sign(x) f(k_n |x|) sin(k_n(y-R_j)).       (2)

At x=0 each summand is set to zero. This is smooth: each f(k_n|x|) vanishes in a neighborhood of0, and the sum defining a fixed block is finite. Within one block the supports in |x| are disjoint, since they lie in(4^(-n),2*4^(-n)). Thus |omega_j|<=epsilon_j, independently of N_j. Its support lies in

    |x|<1/2, |y-R_j|<3pi.

Its support area is bounded by a constant independent of j and N_j. The supports of distinct blocks are separated in y. Consequently

    Omega_tail=sum_j omega_j

is smooth by local finiteness, odd in x, and satisfies |Omega_tail(X)|<=C/(1+|X|). Also ||omega_j||_1<=C epsilon_j, so Omega_tail is integrable. The large frequencies do not affect these zero-order statements.

## A bounded canonical velocity

Let U_j=K*omega_j, where K(Z)=(Z2,-Z1)/(2pi|Z|^2), and put U_tail=sum_j U_j. The elementary split into |Z|<=1 and |Z|>1 gives

    ||U_j||_infinity <= C(||omega_j||_infinity+||omega_j||_1)
                       <= C epsilon_j.                  (3)

The sum therefore converges uniformly to a bounded continuous field. It is the ordinary whole-plane inverse of Omega_tail: at each X the kernel is locally integrable and Omega_tail is bounded, while the distant part is absolutely integrable since Omega_tail is in L1. Fubini or dominated convergence identifies the two definitions.

The velocity is smooth. On any compact set, only finitely many source blocks are nearby. The convolution with each such smooth compactly supported source is smooth. For the remaining blocks, every differentiated kernel is smooth and bounded by C_m dist(X,supp omega_j)^(-m-1); the resulting derivative series converges uniformly on that compact set. This proves all-order smoothness, div U_tail=0 and -curl U_tail=Omega_tail. Reflection parity follows directly by changing x to -x in the kernel. In particular U1(0,y)=0, and the axis is invariant for W.

## Large derivatives on an axis interval

Let I_j=[R_j-pi,R_j+pi]. We first compute the contribution from one n in block j with the y cutoff omitted. At x=0 the second velocity component is an absolutely convergent integral. The elementary Fourier identity

    integral_R sin(k eta)/(x^2+(y-eta)^2) d eta
      = (pi/|x|) exp(-k|x|) sin(ky), k>0,

follows, for example, from the Fourier transform of the one-dimensional Poisson kernel. It can also be verified by the decaying Green function of -d_x^2+k^2: that Green function is exp(-k|x-s|)/(2k), and its derivative at x=0 gives the same result for the odd source in x. The axis velocity for our odd source is therefore exactly

    U2_comparison_n(0,R_j+z)=(epsilon_j A/k_n)sin(k_n z),
    d_y U2_comparison_n(0,R_j+z)=epsilon_j A cos(k_n z).             (4)

For completeness the first identity is obtained directly from the plane kernel by pairing x>0 and x<0:

    U2_n(0,R_j+z)
      = epsilon_j integral_0^infinity f(k_n x)exp(-k_n x)dx sin(k_n z).

The change s=k_n x proves(4) without an unspecified multiplicative factor.

The cutoff error in the derivative is uniformly small on I_j. The derivative of the axis kernel has absolute value at most C |x|/|y-eta|^3. The omitted source has |eta-R_j|>=2pi, while |y-R_j|<=pi. Integration in eta is therefore bounded uniformly, and

    integral_0^infinity x f(k_n x)dx <= C/k_n^2.

Summing the geometric series gives

    d_y (U_j)_2(0,R_j+z)=epsilon_j A S_{N_j}(z)+E_j(z),
    S_N(z)=sum_{n=1}^N cos(4^n z),
    sup_{|z|<=pi}|E_j(z)|<=C epsilon_j.                  (5)

No constant here depends on N_j. The infinite-y comparison source is used only in this absolutely convergent axis calculation. The actual source remains compactly supported in y.

## Elementary lower bound for the lacunary sum

Write mean(h)=(1/(2pi)) integral_{-pi}^pi h(z)dz. Orthogonality gives mean(S_N^2)=N/2. The only relations among four signed frequencies 4^n with zero sum are pair cancellations. Indeed, if the largest index occurs once, its frequency exceeds the sum of the other three; if it occurs twice with equal sign, the two smaller frequencies cannot cancel it. The remaining cases reduce to cancelling equal pairs. Expanding cosines into exponentials, or directly expanding the fourth power, consequently gives

    mean(S_N^4)=3N/8+6 choose(N,2)/4
               =3N^2/4-3N/8 <=3N^2/4.

Hölder applied to |S_N|^(2/3)|S_N|^(4/3) gives

    mean(S_N^2) <= mean(|S_N|)^(2/3) mean(S_N^4)^(1/3).

It follows that

    integral_{-pi}^pi |S_N(z)|dz >=2pi sqrt(N/6).        (6)

Combining(5)-(6) and epsilon_j sqrt(N_j)=R_j yields

    integral_{I_j}|d_y(U_j)_2(0,y)|dy >=C0 R_j-C1/R_j,
    C0=2pi A/sqrt(6)>0.                                (7)

## Contributions from the other blocks

On I_j, the distance to block ell<j is at least cR_j, and the distance to block ell>j is at least cR_ell. The derivative kernel bound C/dist^2, together with ||omega_ell||_1<=C epsilon_ell, gives

    sup_{y in I_j} sum_{ell!=j}|d_y(U_ell)_2(0,y)|
      <= C R_j^(-2) sum_{ell<j}epsilon_ell
          +C sum_{ell>j}epsilon_ell R_ell^(-2)
      <= C R_j^(-2).                                  (8)

Therefore(7) remains true for U_tail, with another harmless lower-order error. In particular, for all sufficiently large j,

    integral_{I_j}|d_y(U_tail)_2(0,y)|dy >=(C0/2)R_j.    (9)

The other blocks cannot cancel the large integrated absolute derivative of the j-th block.

## Divergence of the orbit integral

Since U_tail is bounded, the axis field is b(y)=W2(0,y)=beta y+O(1). It is positive for every sufficiently large y. Axis trajectories starting there increase to infinity and cross every later I_j in finite forward time. Global existence follows from smoothness and the linear bound |W(X)|<=beta|X|+C.

On the axis the operator norm of DU is at least |d_y U2|. The time spent traversing I_j has dt=dy/b(y), and b(y)<=C_beta R_j on that interval. Equation(9) gives a fixed positive lower bound

    integral_{orbit crossing I_j} |DU(phi_t Y)|dt
      >= (1/(C_beta R_j)) integral_{I_j}|d_yU2(0,y)|dy
      >= C0/(2C_beta)>0.                              (10)

The intervals I_j are disjoint. Every sufficiently large positive-axis starting point crosses infinitely many of them, so summing(10) proves(1). This is stronger than a failure of the limit in(D).

## Center adjustment without changing the tail construction

A smooth divergence-free field on the plane has a smooth stream function. Choose the odd-in-x stream function Psi_tail for U_tail. Let chi be a smooth compactly supported radial cutoff equal to1 near the origin, with support in the ball of radius100, disjoint from every tail block. Put

    P(x,y)=cxy-b0 x^3/6,
    deltaPsi=chi(P-Psi_tail),
    U=U_tail+(-deltaPsi_y,deltaPsi_x),
    Omega=Omega_tail-Delta deltaPsi.

The correction is smooth, compactly supported and has the required reflection parity. Near0 the total stream function is exactly P. Hence Psi_xy(0)=c and Omega_x(0)=b0. The velocity remains bounded, and the vorticity retains its power bound and integrability. The velocity remains the ordinary canonical inverse: the Biot-Savart velocity of the compact vorticity correction and its compact stream-derived velocity have the same curl and divergence, decay at infinity, and hence agree by harmonic uniqueness. On the far axis DU is unchanged. The subtraction of U(0) changes b(y) by only a constant, so(10) and(1) still hold.

Taking c=1+beta/2, b0=4/beta and Theta=x^2 chi gives the B2 center jets, temperature parity, zero axis values and polynomial zero-order bounds. The two nonlinear stationary transport equations have not been imposed. Indeed integrability of Omega already contradicts the necessary circulation theorem for a nontrivial full B2 profile, proved separately in packet17; that theorem is not needed for this kinematic construction. Thus this construction cannot refute a bootstrap that uses both transport equations, or a bootstrap that assumes suitable derivative bounds at infinity.

## Dependencies and verification scope

The proof uses only explicit smooth cutoffs, elementary Fourier orthogonality and Hölder, the Poisson kernel/one-dimensional Green function, elementary whole-plane inverse bounds and smooth ODEs. No numerical experiment is used. Packet31 provides the broader relative uniqueness statement, but this example already has an absolutely convergent ordinary inverse. The construction strengthens the earlier bounded oscillatory-shear warning by adding zero-order vorticity power decay. It does not strengthen any B2 nonexistence theorem. No formalization is claimed.

## External audit and independent checks

The actual returned model in opus_reviews/18_decay_without_D was claude-opus-5-5. Its detailed review confirmed the source support, exact Poisson-kernel normalization, finite window error, fourth-moment identity, cross-block bound and orbit integral. These steps were rechecked here. Its scope warning is incorporated: DU itself is unbounded and only axis trajectories were used. Suggested stronger velocity decay is not needed and is not adopted as an additional theorem. No numerical or formal certificate is claimed.
