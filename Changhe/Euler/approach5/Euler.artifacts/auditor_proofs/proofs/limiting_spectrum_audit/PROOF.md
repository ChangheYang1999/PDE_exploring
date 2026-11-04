# Spectral restrictions at point and periodic backward limits

## Statement

Assume H0 and H1-prime, 0<c<1/2 and arbitrary finite omega. Let a have Omega(a)!=0. If Phi_-t(a) tends to a stagnation point p, the largest real part of an eigenvalue of DB(p) is at least 1+c. Thus some eigenvalue has real part at most (2c-1)/2<0. If the alpha-limit is one nonconstant periodic orbit, its largest forward Floquet exponent is at least 1+c, and another exponent is at most 2c-1<0.

The sets of vortical initial points with single-point or single-periodic-orbit alpha-limit are Lebesgue-null. These statements confirm B02-B04. They do not classify general compact alpha-limit sets.

## Point limit

Write b=1+c and x(t)=Phi_-t(a). The nonzero vector

    w(t)=D Phi_-t(a) Omega(a)=exp(-bt) Omega(x(t))

satisfies w'=-DB(x(t))w. Let L=DB(p) and m=max Re spectrum(L). For every epsilon>0 there is a positive definite quadratic norm with logarithmic norm of L at most m+epsilon. For example, solve the Lyapunov integral for the stable matrix L-(m+epsilon)I. Continuity and convergence give logarithmic norm of DB(x(t)) at most m+2epsilon for large t. Therefore

    |w(t)| >= C_epsilon exp(-(m+2epsilon)t).

Omega(x(t)) is bounded on this convergent orbit. The Cauchy relation then forces b<=m+2epsilon, and epsilon tends to zero. Since tr L=3c, the remaining two real parts have sum at most 2c-1, giving the stated negative direction. This proof applies whether or not Omega(p) vanishes.

If Omega(p)=0, one has w(t)=o(exp(-bt)); this does not by itself mean a strictly more negative Lyapunov exponent. The decay factor can be subexponential.

## Periodic limit without assuming convergence of a phase

Parameterize the limiting cycle gamma by forward flow time theta modulo its period T. A sufficiently small tubular neighborhood has a smooth circle-valued phase theta(x) with dtheta(B)=1 on gamma and dtheta(B)=1+o(1) as the distance to gamma tends to zero. Thus on the backward orbit, theta'(t)=-1+o(1). Also DB(x(t))=A(theta(t))+o(1), where A(theta)=DB(gamma(theta)). These estimates are uniform in phase.

Let m be the largest forward Floquet exponent. For k=m+epsilon, the forward fundamental solution Y(theta+u,theta) obeys a uniform bound C exp((m+epsilon/2)u). Define the positive definite T-periodic quadratic form

    P(theta)=integral_0^infinity exp(-2ku)
             Y(theta+u,theta)^T Y(theta+u,theta) du.

It is C^1, uniformly equivalent to the Euclidean norm, and satisfies

    P' + A^T P + P A = 2kP-I.

For V(t)=w(t)^T P(theta(t))w(t), the actual backward equation and phase estimates give

    V'(t) >= -(2k+o(1)) V(t).

Indeed, the principal part is -2kV+|w|^2; all remaining terms are o(1)|w|^2. Hence for every delta>0, |w(t)|>=C exp(-(k+delta)t) for sufficiently large t. Cauchy's formula and boundedness of Omega along the orbit imply b<=k+delta. Let epsilon and delta tend to zero. One Floquet exponent is zero, in the flow direction, and their sum is 3c. The remaining exponent is consequently at most 3c-b=2c-1.

This supplies the phase comparison left implicit in B04. It handles negative or complex Floquet multipliers through the real periodic quadratic form and needs no limiting phase.

## Null basins and the finite-cover point

The local trapping lemma proved in the team records, Section 2, says that a C^1 local map with an expanding derivative direction at a fixed point has a local trapped set contained in a Lipschitz graph of codimension at least one. Apply this to the backward time-one map at each point limit with a negative forward eigenvalue.

The stagnation set N is compact under H1-prime. The subset

    N1={p in N: min Re spectrum(DB(p)) <= (2c-1)/4}

is compact by continuity of matrix spectra. Every vortical point limit lies in N1 by the stronger bound (2c-1)/2. For each p choose a trapping neighborhood O_p and a smaller O'_p with closure inside O_p. A finite collection of O'_p covers N1. Every convergent backward orbit eventually stays in the corresponding O_p, so it belongs to an integer forward image of its null trapped graph. There are only finitely many graphs and countably many time shifts. This proves B03's finite-cover step exactly as claimed.

For cycles, the corresponding transverse return map has an expanding backward direction. The countable rational-tube construction in the same prior proof, Sections 5-6, gives a countable union of null flow-saturated graphs. An uncountable union of individual null cycle basins is never used.

The conditional Liouville conclusion only needs almost every point in the open vortical set to have a point or one cycle as its alpha-limit. No hypothesis on the limits of irrotational initial points is necessary.

Audit recorded: 2026-11-02T18:56:51Z
