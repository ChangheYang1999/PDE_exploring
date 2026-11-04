# Physical measures without a transitivity assumption

## Exact conditional statement

Let 0<c<1/2 and finite omega be given. Let U in C2 and P in C1 solve the full rotating profile equation on a neighborhood of a compact full invariant set K and a relatively compact trapping neighborhood V. Put B=(cI-omega J)y+U, Omega=curl U, Psi_t=Phi_-t, b=1+c and a=1-2c. Assume:

1. Omega never vanishes on K.
2. K contains a zero of B, every such zero is hyperbolic, and every eigenvalue of DB there other than its specified eigenvalue b along Omega has real part less than b.
3. V is a genuine compact trapping neighborhood: Psi_t(V) is contained in V for t>=0, Psi_T(closure V) is contained in V for some T>0, and K is the intersection of Psi_t(closure V) over t>=0.

Then K carries finitely many full-flow-ergodic physical probabilities mu_1,...,mu_k whose continuous-time basins cover V up to a null set. Each has entropy a for Psi_1. Every flow-invariant probability on K has entropy at most a; equality holds exactly for the convex hull of the mu_i. In particular the topological entropy is a. No uniqueness, transitivity, or physicality of a nontrivial mixture is asserted. Velocity decay is not needed for this conditional result.

## Source and hypotheses checked

The actual manuscript read is V. Araujo, A. Souza and E. Trindade, Upper large deviations bound for singular-hyperbolic attracting sets, arXiv:1711.09626v2. The retained PDF is in the team records. I read the definitions on printed pages 3-5, Theorem 1.7 on page 8, and its proof in Section 2.3 on pages 18-20.

Theorem 1.7 applies to a C2 singular-hyperbolic ATTRACTING SET, without transitivity. We impose compact trapping explicitly. The printed page-3 definition uses only positive invariance of an open V and K=Inv(V); taken literally, that weaker wording allows extra transient components whose forward limits lie on the boundary of V. It is insufficient to conclude full basin coverage of V. The rendered page is retained in the team records. Our stronger hypothesis removes this ambiguity. Its first part gives a finite family of ergodic physical/SRB measures covering the trapping region almost everywhere. Its second part characterizes an ERGODIC full-flow-invariant probability by the central-Jacobian entropy formula. Its third part describes all formula-satisfying flow probabilities as the finite convex hull. The ergodicity qualifier must be retained. We do not use a large-deviation conclusion of Theorem A, which has additional assumptions.

The source proof contains a normalization error in its displayed basin averaging argument for (c) implies (a). The needed implication is simpler: two physical basins for different probabilities are disjoint, and the given finite family covers V almost everywhere. Any further physical basin meets V in positive measure by trapping and flow invariance, so its probability equals one member of the family. This repairs the displayed averaging step. It does not independently reconstruct the global return-map theorem supplying finiteness and full basin coverage.

A134 proves the required dominated splitting Es=R Omega and dim Ecu=2, with uniform contraction on Es and area expansion on Ecu. Hypothesis 2 supplies exactly the hyperbolic singularities and domination required by the source definitions. A cutoff extension preserving a neighborhood of the trapping region embeds this local C2 flow into a compact boundaryless three-manifold, as in A135. No extra global dynamical hypothesis results from that extension.

## Exact central Jacobian and entropy

For x in K let rho(x)>0 be the absolute Euclidean volume formed by the unit vector Omega/|Omega| and any orthonormal frame of Ecu. This does not depend on the frame orientation. Set q(x)=|Omega(x)|rho(x), a continuous function bounded above and away from zero.

Cauchy transport and constant divergence give

    D Psi_t Omega(x)=exp(-bt)Omega(Psi_t x),
    det D Psi_t=exp(-3ct).

Taking the volume of the transported frame gives

    Jcu_t(x)=exp(at) q(x)/q(Psi_t x).                 (1)

Hence integral log Jcu_1 dnu=a for every flow-invariant probability nu on K. The source entropy formula makes each mu_i have entropy a.

For the converse upper bound, a flow-ergodic probability is either a point mass at one of the finitely many hyperbolic zeros, with entropy zero, or gives full mass to regular points. A130 excludes B parallel to Omega at every regular point of K. A037 therefore gives the regular backward exponents -b,0,a. Ruelle's inequality gives entropy at most a, and flow-ergodic decomposition extends this bound to every flow-invariant probability.

Equation (1) now identifies equality h_nu=a with the source's entropy formula. Its third part gives exactly the convex hull in the statement. Finally, averaging any Psi_1-invariant probability over flow times in [0,1] preserves its time-one entropy and produces a flow-invariant probability. This follows from commuting conjugacy and the harmonicity of entropy on invariant probabilities. The variational principle therefore gives topological entropy a as well.

## Scope

This confirms LIT30 with the explicit compact-trapping qualification above and removes transitivity from A135's conditional physical-measure conclusion, replacing uniqueness by a finite family. It does not produce V for a general mixed limit set, remove the spectral bound, handle zeros of Omega, or prove nonexistence. The source's finiteness theorem is an explicit external dependency, not an independently reconstructed theorem of this campaign.
