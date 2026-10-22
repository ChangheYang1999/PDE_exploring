# A conditional obstruction to residual error control in the weak center topology

## Statement and hypotheses

Fix L>0 and0<k<1. Let X be the weighted weak H1 space

    ||h||X^2=integral [h^2+r^2|grad h|^2]w(r)dX,
    w(r)=L^6 r^-6(1+r^2/L^2)^(3/2-k).

Assume that an exact stationary canonical profile rho exists with exponent c_l=1/k and Sigma(rho)=3c_l-1, where Sigma(f)=psi[f]_xy(0) and -Delta psi[f]=partial_x f. Assume rho is even in x, odd in y, locally C^{2,alpha} for some alpha>0, and has the continuous even-even factor rho=x^2 y a with a(0)=1. Require the explicit derivative bounds

    |D^j rho|<=A r^(3-j), r<=1, j=0,1,2,
    |D^j rho|<=D r^(k-j), r>=1, j=0,1,2.

Its canonical velocity is locally C1, has the prescribed parity, is divergence free, and is sublinear at infinity. The stationary equation holds pointwise. No such exact profile is constructed or claimed to exist here. The derivative bounds are additional hypotheses beyond a bare continuous center factor.

For a kinematically admissible density f with finite canonical strain, define

    F(f)=(((1+Sigma(f))/3)X+U[f]) dot grad f-f.

Here kinematic admissibility means the specified parity, local C^{2,beta} regularity for some beta>0, continuous even-even center factor of value1, canonical sublinear velocity, and sublinear density/first-derivative growth. It does not impose stationarity. Consider only such f with f-rho and F(f) in X and Sigma(f)=Sigma(rho).

For every eta>0 there is a sequence q_delta in this class with

    0<||q_delta-rho||X<eta,
    ||F(q_delta)||X ->0,
    lim ||q_delta-rho||X=d_s>0.                         (1)

Consequently no estimate ||q-rho||X<=omega(||F(q)||X), with omega(t)->0 as t->0, holds for all these q in any X neighborhood of rho. In particular a finite linear error constant fails in this precisely stated formulation. This is not a claim about distance to the set of solutions, a neighborhood in a stronger norm, a fixed leading far coefficient, or the existence of rho itself. It is not a NO endpoint.

## Dilation and continuity in X

For s>0 put rho_s(X)=s rho(X/s). The stream psi_s(X)=s^2 psi(X/s) solves -Delta psi_s=partial_x rho_s and gives U[rho_s](X)=s U[rho](X/s). Parity and sublinearity identify it with the canonical velocity. Its central derivative is unchanged, so Sigma(rho_s)=Sigma(rho). Substitution into the stationary equation proves F(rho_s)=0. The center factor is s^-2 a(X/s), so J(rho_s)=s^-2.

The explicit end bounds imply rho_s,rho in X. Indeed the squared norm radial integrands have upper bounds Cr near0 and Cr^-2 near infinity. For s in[1/2,2] the same majorants hold uniformly, after making the central disk smaller and the exterior radius larger and bounding the intermediate compact annulus. Pointwise continuity of rho and its first derivatives now gives ||rho_s-rho||X->0 as s->1 by dominated convergence.

For s!=1 this distance is positive. Otherwise continuity of rho_s-rho would give equality everywhere, contradicting its nonzero center factor s^-2-1 on an open punctured neighborhood. Choose s!=1 sufficiently close to1 that0<d_s=||rho_s-rho||X<eta/2, and keep this s fixed for the sequence below. Neither differentiability of the dilation curve in X nor membership of its derivative is needed.

## Compact center repair at fixed strain

Set

    h_delta=x^2 y(1-r^2/delta^2)_+^6,
    b_delta=(4h_delta-h_(2delta))/3,
    t_s=1-s^-2,
    q_delta=rho_s+t_s b_delta.

The canonical Green calculation in graph_center_norm gives Sigma(h_delta)=delta^2/56. Hence J(b_delta)=1 and Sigma(b_delta)=0 exactly. Therefore q_delta has center factor1 and the same strain and exponent as rho. The perturbation is C5 and compactly supported; q_delta has all stated kinematic regularity and growth properties, and its canonical velocity is the sum of the two canonical velocities. The derivative bounds for rho_s satisfy the explicit hypotheses of graph_center_norm with any smaller exponent0<beta<min(alpha,1). Thus

    ||b_delta||X ->0,  ||L_s b_delta||X ->0,              (2)

where L_s is the full linearization of F at rho_s with the same strain convention. This use does not require the background center coefficient to equal1. Its rank-one coefficient is Sigma(h)/3, and that term vanishes for b_delta.

It follows at once that ||q_delta-rho||X->d_s, so the distance is between d_s/2 and eta for all sufficiently small delta. To prove(1) it remains to bound the quadratic term.

## Exact quadratic scaling and an explicit majorant

Write H(Z)=Z_1^2 Z_2(1-|Z|^2)_+^6 and B(Z)=(4H(Z)-8H(Z/2))/3. Then b_delta(X)=delta^3 B(X/delta). The canonical order-zero velocity law gives U[b_delta](X)=delta^3 U[B](X/delta). Therefore, with Q=U[B] dot grad B,

    U[b_delta] dot grad b_delta=delta^5 Q(X/delta).       (3)

This is not a global bilinear estimate for arbitrary X functions. It is a bound for this one explicit scaled family.

The exact unit-bump polynomials provide constants S1=8019, S2=84078 and C_H=693689/84 such that on its support |grad H|<=S1 r^2, |D2 H|<=S2 r, and |U[H]|<=C_H r, |DU[H]|<=C_H on r<=1; outside, the last bounds are C_H r^-3 and C_H r^-4. These follow from coefficient absolute sums and the two exterior stream modes, as fully proved in graph_center_norm. No unknown profile constant occurs in them.

By scaling and the triangle inequality, on r<=2 one has

    |grad B|<=B1 r^2,  |D2 B|<=B2 r,
    |U[B]|<=C_U r,     |DU[B]|<=C_U,
    B1=5S1/3, B2=5S2/3, C_U=8C_H/3.

For1<=r<=2 use r^-3<=r and r^-4<=1 for the unscaled velocity; for the twice-scaled term use its interior bound. Consequently

    |Q|<=A_Q r^3, |grad Q|<=B_Q r^2,
    A_Q=C_U B1, B_Q=C_U(B1+B2).

Q is supported on the closed radius2 disk because grad B is. Its weak first derivatives are classical; B is C5 and U[B] is C1. Put C_w=L^6(1+L^-2)^(3/2-k). For0<delta<=1/2, w(r)<=C_w r^-6 on the support of the scaled Q. Equation(3) and direct integration give

    ||U[b_delta] dot grad b_delta||X^2
        <=4pi C_w(A_Q^2+B_Q^2)delta^6.                  (4)

Indeed the two scaled terms are bounded by A_Q delta^2 r^3 and B_Q delta^2 r^2; integration of the resulting constant weighted density over the disk radius2delta gives4pi delta^2. Every factor of delta in(4) is explicit. A smaller restriction on delta may be used to apply(2).

Since Sigma(b_delta)=0, exact polynomial expansion of F gives

    F(q_delta)=t_s L_s b_delta+t_s^2 U[b_delta] dot grad b_delta.

The background term is zero by its assumed stationarity. Equations(2) and(4) prove F(q_delta) in X and convergence to0. This proves(1) and the asserted impossibility of omega by taking delta->0 while s and d_s>0 are fixed.

## Scope and verification

This theorem is conditional on an exact background with the explicit end derivative bounds. It does not apply F(rho_s)=0 to the nonstationary numerical modal trial. It does not show that the q_delta stay close in a norm controlling the center factor; that norm is deliberately absent. A prescribed leading far coefficient can also exclude rho_s and hence the sequence. There is no exclusion of a meaningful uncertainty ball, no assertion about distance to the solution set, and no existence conclusion.

The proof is written before new computation. Reconstruct the two-scale stream through piecewise Green integration and a separate exact radial ODE matching solve; compare every coefficient, match derivatives through6 at radii1 and2, and check the zero strain. Check the constants and all scaling exponents independently. The exact symbolic and rational checks support the finite arithmetic only; the uniform profile bounds and exact stationarity remain hypotheses. Request actual Opus5.5 review of the quantifiers, strong continuity, canonical scaling and nonlinear estimate, and resolve any substantive objections before finalization.
