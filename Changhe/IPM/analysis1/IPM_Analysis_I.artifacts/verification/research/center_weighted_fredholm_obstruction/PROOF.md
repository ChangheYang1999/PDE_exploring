# Consequences of the center sequence for compact remainder estimates

This argument is conditional on the construction and estimates in the preceding result, center_weighted_quasimodes/PROOF.md. That parent is still under review when this proof is first written. No application is accepted here until the parent and this proof have final independent verdicts. This result concerns one specified weighted Hilbert norm, not the existence of an IPM profile.

## Statement and spaces

Fix 0<k<1/2 and L>0. Let X be the real Hilbert space of even-x, odd-y functions with weak first derivatives and norm

    ||h||_X^2 = integral_R2 (|h|^2+r^2|grad h|^2) w(r) dX,
    w(r)=L^6 r^-6(1+r^2/L^2)^(3/2-k).

The gradient is the Cartesian weak gradient. The norm identifies functions equal almost everywhere. Let Y=H^{5/2}(R2), with its usual Fourier norm. For the linearized normalized canonical IPM operator

    L_rho h=(ell X+U[rho]) dot grad h-h
              +U[h] dot grad rho+(Sigma(h)/3) D rho,
    ell=1/k, D=X dot grad, Sigma(h)=-partial_x U[h]_1(0),

assume exactly the background hypotheses and the construction proved in center_weighted_quasimodes/PROOF.md. Explicitly, rho=x^2 y+O(r^5), |grad rho|=O(r^2), |Hess rho|=O(r) near0, rho is C^{4,a}_loc for some a>0, U[rho] is C2 near0 with derivative diag(-(3ell-1),3ell-1), and the background and its first two scaled derivatives have order at most r^k at infinity. U[h] is the canonical Darcy velocity. J(h) is the center factor value in h=x^2 y b.

Then there are smooth compact perturbations h_j with the required reflections and smooth global even-even factors, supported in the fixed disc r<=2 and vanishing near0, such that

    J(h_j)=Sigma(h_j)=0,
    ||h_j||_X=1,
    ||L_rho h_j||_X ->0,
    ||h_j||_Y ->0,
    h_j converges weakly to0 in X.                         (1)

Their leading far coefficients vanish. On every perturbation domain containing this sequence, the following conclusions hold.

1. For any bounded linear operator B:X->X,

       sup_{h in domain, ||h||_X=1} ||h-B L_rho h||_X >=1.  (2)

   Thus a defect bound strictly below1 in this norm is impossible for such B.
2. No finite C gives ||h||_X<=C(||L_rho h||_X+||h||_Y) on the domain, or even on its smooth compact elements.
3. For any Banach space Z and any compact linear K:X->Z, no finite C gives

       ||h||_X<=C(||L_rho h||_X+||K h||_Z).                (3)

   This assumes compactness of K on X; it does not assert compactness of any particular embedding.
4. Any closed linear realization T:D(T) subset X ->X containing this sequence and satisfying T h_j=L_rho h_j fails to have both closed range and finite-dimensional kernel. In particular it is not Fredholm.

The last statement is about closed realizations. It neither establishes closedness of a proposed realization nor asserts a spectrum for an unspecified realization. Other domain or forcing norms and domains excluding this sequence are not covered.

## Hilbert completeness

For clarity, the stated X is complete. If h_n is Cauchy in X, then h_n is Cauchy in L2(w dX) and its two derivatives are Cauchy in L2(r^2 w dX). These three weighted L2 spaces are complete. On any fixed bounded disc the two weights have positive lower bounds away from their possible infinite value at0: they are continuous and positive off0 and tend to infinity at0. Hence convergence also holds in ordinary L2 of every such disc. Testing against smooth compact functions identifies the two derivative limits with the distributional derivatives of the function limit. The weighted limits have finite norm and yield convergence in X. Reflections define a closed subspace because the radial weights are reflection invariant. The displayed quadratic form supplies the inner product.

## Strengthening the diagonal choice

Write the two-parameter family from the parent proof as

    f_(e,N)=r^2 eta_N(log r) F_e(theta),
    v_(e,N)=f_(e,N)-Sigma(f_(e,N)) b,

where b is the fixed smooth strain-correcting bump supported in1<r<2, J(b)=0 and Sigma(b)=1. The angular factors satisfy

    A(F_e) -> A(F)>0, A(G_e)->0,
    A(Z)^2=integral_circle (5Z^2+(Z')^2), G_e=T_angular F_e.

The parent proof gives, for each fixed e>0 and all sufficiently large N,

    ||v_(e,N)||_X >= c sqrt(N+t0-2) A(F_e)-C_e,
    ||L_rho v_(e,N)||_X <= C sqrt(N) A(G_e)+C_e,           (4)

with c=L^3>0, t0 fixed, C independent of e,N, and finite constants C_e allowed to depend on e. It also proves, by the dyadic H^{5/2} estimate and the bounded velocity multiplier,

    sup_N ||f_(e,N)||_Y < infinity,
    sup_N |Sigma(f_(e,N))| < infinity.                   (5)

Since b is smooth and compact, (5) implies

    sup_N ||v_(e,N)||_Y <= M_e < infinity.               (6)

No constant in (5)-(6) is claimed uniform as e tends to0.

Choose e_j tending to0 so that A(F_(e_j)) stays bounded below by a fixed positive number and A(G_(e_j)) tends to0. For each j choose N_j large enough that the lower bound in (4) is positive, that all terms C_(e_j) divided by this lower bound tend to0 as j increases, and that M_(e_j) divided by the same lower bound is at most1/j. Such choices exist because the lower bound tends to infinity for each fixed e_j. In addition, for sufficiently large N_j, sqrt(N_j) divided by that lower bound is bounded by a constant independent of j, since A(F_(e_j)) has a uniform positive lower bound. Normalize

    h_j=v_(e_j,N_j)/||v_(e_j,N_j)||_X.

Equations (4)-(6) prove the first four assertions in (1). The support and exact constraints are unchanged by normalization. This is an explicit order of choices: first the angular cutoff e_j, then a sufficiently long annulus N_j.

## Weak convergence in X

The Fourier Cauchy-Schwarz estimate

    ||g||_infinity+||grad g||_infinity <= C||g||_(H^{5/2})

follows from the integrability of (1+|xi|)^2(1+|xi|^2)^(-5/2) in two dimensions. Hence h_j and grad h_j converge uniformly to0. Fix any g in X and any small s>0. The X inner product on r<s has absolute value at most

    ||h_j||_(X,r<s) ||g||_(X,r<s) <= ||g||_(X,r<s).

The last quantity tends to0 as s tends to0 by integrability of g's norm density. On the fixed annulus s<=r<=2 both weights are bounded and its measure is finite, so uniform convergence of h_j and its gradient gives ||h_j||_(X,s<=r<=2)->0. Cauchy-Schwarz controls the inner product there. On r>2 both h_j and its weak gradient vanish. First take j to infinity for fixed s and then s to0. This proves <h_j,g>_X->0 for every g, the final assertion of (1). It uses no compact embedding claim.

## Approximate inverse and remainder estimates

For bounded B:X->X, the reverse triangle inequality gives

    ||h_j-B L_rho h_j||_X >=1-||B|| ||L_rho h_j||_X ->1.

Taking the supremum proves (2), including the case of an infinite supremum. Substitution of (1) directly contradicts the estimate in item2.

If K:X->Z is compact, weak convergence h_j->0 implies ||K h_j||_Z->0. Indeed, otherwise a subsequence has norms bounded below by a positive number. Compactness gives a further subsequence converging in Z to z. For every bounded linear functional z* on Z, weak convergence gives z*(K h_j)->0, so z*(z)=0. The Hahn-Banach separation property implies z=0, contrary to the lower bound. Substitution in (3) is then impossible. This proves item3 without attributing compactness to any particular nonlocal term.

## Closed realizations

Suppose T is closed and contains the sequence, with T h_j=L_rho h_j. Equip D(T) with the graph inner product

    <u,v>_G=<u,v>_X+<Tu,Tv>_X.

Closedness makes D(T) complete: graph-Cauchy sequences converge in X in both entries and the closed graph identifies the pair. Thus it is a Hilbert space. By (1), ||h_j||_G->1 and h_j converges weakly to0 in this graph space, because for each g in D(T)

    <h_j,g>_G=<h_j,g>_X+<T h_j,Tg>_X ->0.

Assume for contradiction that ker T is finite dimensional and ran T is closed in X. Let P be the graph-orthogonal projection onto ker T. Choose a finite graph-orthonormal basis of that kernel. The weak convergence just proved makes every projection coefficient tend to0, so ||P h_j||_G->0.

The map T from (ker T)^perp_G to ran T is a bounded bijective linear operator between Banach spaces. It is bounded by the graph norm, injective by definition of the orthogonal complement, and surjective by subtracting P from any preimage. Its inverse is bounded by the Banach inverse theorem. Consequently there is C<infinity such that

    ||h-P h||_G <= C||T h||_X  for h in D(T).

Applying this to h_j makes the right side tend to0, while the left side tends to1. This contradiction proves item4. Density of D(T) in X is not needed for this argument; any definition of Fredholm used here at least requires closed range and finite kernel.

## Dependencies, actual application and scope

The only problem-specific dependency is the parent center construction and its canonical-background application. Its bounds (4)-(5), support and exact constraints must be accepted, not inferred from a numerical sample. The remaining arguments are the explicitly proved Hilbert and weak convergence steps, Fourier Cauchy-Schwarz, and the standard Banach inverse and Hahn-Banach theorems. No computation of a spectral value is involved.

The distinguished canonical trial is an application only after the parent's scalar, regularity and canonical-definition pins are verified and its actual-review verdict is FINAL. This topic also requires complete actual Claude Opus5.5 review, later independent adjudication and pin verification. It supplies an obstruction to particular proof strategies in the diagnostic X norm. It does not prove absence of X3, rule out an inverse in the prompt's other admissible norms, or constitute a decisive endpoint of IPM Analysis I.
