# Why two standard Fuchsian theorems do not close the logarithmic problem

Status: CONFIRMED as a direct hypothesis check and algebraic reformulation. This excludes only the direct applications stated below, not all possible Fuchsian methods.

## Statement

In the variable z=r^{-delta}, with 0<delta<1 and gamma=1-delta, the stationary IPM density and Poisson equations have a linear angular second derivative with a nonzero coefficient at z=0. Their indicial stream operator has arbitrarily large positive characteristic exponents. Consequently the direct reformulation below does not satisfy condition C2(iii) of Tahara and Yamane's Theorem4.1 [1]. A first-order spatial system retaining that derivative also fails the vanishing tangential coefficient condition A3 of Tahara's scalar Briot-Bouquet setup [2]; that scalar theorem does not itself cover the coupled IPM system.

These are precise failures of proposed sufficient hypotheses. They are not divergence results and do not refute a reformulation with different function spaces or further cancellations.

## Exact reformulation

Set E=z partial_z and write

\[
 \rho=r^\gamma F(z,\theta),\qquad
 \psi=r^{\gamma+1}G(z,\theta),\qquad
 F=\sum_{n\ge1}f_nz^{n-1},\quad
 G=\sum_{n\ge1}g_nz^{n-1}.
\]

For a radial factor r^s H(z,theta), r partial_r acts as s-delta E. Direct substitution into the stationary equation and -Delta psi=partial_x rho gives

\[
 -(c-1)EF+z\left[((\gamma+1-\delta E)G)F_\theta
       -G_\theta((\gamma-\delta E)F)\right]=0,
 \tag{1}
\]

\[
 -\left[(\gamma+1-\delta E)^2+\partial_\theta^2\right]G
 =(\gamma-\delta E)\cos\theta F-\sin\theta F_\theta.
 \tag{2}
\]

The coefficient c delta=c-1 gives the first term in (1). The quadratic radial weight relative to r^gamma is r^{gamma-1}=z. Thus the coefficient of z^{n-1} in (1) is exactly the ordered stationary recurrence, with i+j=n. Equation (2) is the angular Poisson inverse at every radial degree.

Solving (2) for its highest Euler derivative gives

\[
 E^2G=\frac{2(\gamma+1)}\delta EG
 -\frac{(\gamma+1)^2}{\delta^2}G
 -\frac1{\delta^2}G_{\theta\theta}
 -\frac\gamma{\delta^2}\cos\theta F
 +\frac1\delta\cos\theta EF
 +\frac1{\delta^2}\sin\theta F_\theta.
 \tag{3}
\]

Subtracting the leading pair F(0)=f_1, G(0)=g_1 changes the inhomogeneous terms but leaves the coefficient -1/delta^2 of G_{theta theta}. Replacing EF using (1), when possible, does not remove this linear angular term.

## Direct theorem comparison

Tahara and Yamane [1, Theorem4.1, condition C2(iii), printed page11] require every coefficient of a linear spatial derivative in their right-hand side to tend to zero at least like a positive power of the radial variable. The derivative of the right-hand side of (3) with respect to G_{theta theta} is the constant -1/delta^2. It fails that condition.

Tahara [2, assumption A3, printed page2] assumes that the derivative of the scalar right-hand side with respect to its first spatial-derivative argument vanishes at the radial origin. A first-order spatial reduction of (3), introducing G_theta as another unknown, retains a nonzero coefficient of its spatial derivative. It is not in that scalar theorem's stated class. Both sources are useful models for singular existence arguments, but citing them without addressing this difference would leave the IPM convergence claim unproved.

## The unbounded characteristic exponents

For the homogeneous stream equation, test G=z^s sin(2j theta), j>=1. The characteristic equation is

\[
 (\gamma+1-\delta s)^2=4j^2,
 \qquad
 s=\frac{\gamma+1\pm2j}{\delta}.
\]

The plus branch is positive and unbounded with j. On the series lattice s=n-1 it is exactly n delta=2(j+1), the resonance condition already audited in topic03. Thus the obstruction to the cited finite-order scalar indicial frameworks is visible in the same spectrum that produces the stationary small divisors. This observation does not by itself determine whether the rational polynomial-log series converges.

## References and verification

[1] Hideshi Tahara and Hideo Yamane, *Logarithmic Singularities of Solutions to Nonlinear Partial Differential Equations*, arXiv:math/0703870, 2007. Relevant part: Theorem4.1 and C2(iii).

[2] Hideshi Tahara, *On the Singular Solutions of a Class of Nonlinear Partial Differential Equations*, arXiv:2010.01467, 2020. Relevant part: A1-A3 and the scalar equation in Section1.

The primary PDFs were read directly. Their hashes and retrieval times are in verification/source_record.json. The algebra in (1)-(3) follows from the potential-consistent recurrence in topic01 and can be checked by substituting each monomial z^{n-1}. No external existence theorem is claimed for the IPM system here.
