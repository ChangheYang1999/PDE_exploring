# C50 and B58: current scope and asymptotic repairs

## 1. The claim being checked

This is a review of every change in Theory Agent C C50 and Theory Agent B B58 from their previously audited immutable sources. It confirms the revised wording and the two new explanatory calculations below; it does not claim a new exclusion theorem. The baseline proofs are the complete standalone arguments in the team records and in the team records. Those establish A1414-A1428 with their exact hypotheses. The current files and full differences are pinned under verification.

For C50 the class remains the full natural-tail helicity-free similarity profile class in A1414: 2/5<c<1/2, every finite omega, U in C2 and P in C1, with the specified natural velocity and derivative bounds, canonical pressure and scattering quantities. Write a=1-2c, b=2-2c, q=b/a, H for the normalized rotating Bernoulli scalar, g=U.B, Q=H-g and y_t for a B-orbit. The tail quantities are V, W, k, S and the first pressure correction p1.

## 2. The resonance and sphere-mean scope

The current C50 explicitly imposes c!=3/7 on all of Theorem1, including part(c), and on every assertion involving p1, S1 or sigma1. At c=3/7, h(x)=|x|^(-5)P4(x3/|x|) is a nonzero harmonic function on the punctured space, invariant under axial rotations and of the same twisted scaling as p1. Thus those homogeneity and Poisson conditions do not define a unique p1 there. Proposition2 and the sphere-mean Lemma3 retain the whole campaign interval.

The revised sharpness statement agrees with A1419-A1420. A C1 vector field vanishing at zero is O(r), so a premise |v|<=Cr^m with 0<m<1 still has effective order one. The exact sufficient threshold for the sphere-mean coefficient is delta>1/(2max(m,1)); the swirl with exponent max(m,1) attains equality. For m>=1, v=rho^(m-1)Jx and pi=|v|²/(2m) are C1 and satisfy the stationary pressure identity. For 0<m<1 this same formula is not C1, which is why the earlier unrestricted sharpness wording failed. At delta=1/(2m), the strengthened vanishing v=o(r^m) also suffices by the zero-endpoint monotonicity argument in A1420. These conditions are now recorded correctly.

## 3. The hypothetical low-multipole transform

The revised Remark2 states a precise pre-A623 calculation. Suppose k(x0)=S(x0)=0 and, hypothetically,

    Q(y_t)=exp(-3ct)(f(t)+o(1)),

where f is the bounded angular value of the lowest pressure multipole. From BH=-ag=-aH+aQ,

    (exp(at)H(y_t))'=a exp(at)Q(y_t).

The terminal coefficient is zero because k(x0)=0. Since 3c-a=5c-1>0, integration from t to infinity gives

    exp(3ct)H(y_t)
       =-a integral_0^infinity exp(-(5c-1)u)f(t+u)du+o(1).

The integrated remainder tends to zero because its tail supremum tends to zero and the kernel is integrable. Subtracting exp(3ct)Q yields

    exp(3ct)g(y_t)
       =-f(t)-a integral_0^infinity exp(-(5c-1)u)f(t+u)du+o(1).

Thus a sign law would constrain the displayed integral transform, rather than f alone. In the actual profile class A623 already makes the pressure multipoles zero. The repaired text correctly says pressure multipoles, not all raw moment tensors. No hypothetical surviving multipole is asserted.

## 4. Original orbits determine component ratios only at nonzero k

The revised Section5.3 correctly distinguishes the linear A-orbit exp(tA)x0 from the nonlinear profile orbit y_t. For a sufficiently small r, uniform rescaled pressure convergence on the closed ball gives

    average_(partial B_r(x0)) P2
       =lim_(t->infinity) exp(bt)
           average_(partial B_(exp(ct)r)(exp(tA)x0))(P-Pinf).

The radii are a fixed fraction of the distance of the linear center from zero. The displayed pointwise orbit coefficients have not supplied a lower bound for those sphere averages.

For a vortical tail component with k!=0, let x be any point in it and y=Xi^(-1)(x). The leading limits are exp(bt)Q(Phi_t y)->S(x) and exp(at)H(Phi_t y)->k(x). Since aq=b,

    D=S(x)/|k(x)|^q
      =[lim exp(bt)Q(Phi_t y)]/|lim exp(at)H(Phi_t y)|^q.

This correctly identifies D from the orbit through a point of the component. At a common-flat point k=S=0 these limits instead give an indeterminate ratio and do not bound neighboring component constants. The repaired paragraph limits its nonimplication statement to what the displayed argument has established. The quantitative negative-D alternative and dense-component criterion are the already proved A1336 statements and remain accurately scoped.

## 5. Higher jets and zero-work neighborhoods

The current Section5.2 conditions convergence of all rescaled jets on the all-order exterior derivative bounds of C48(a). Smoothness of the tail alone is not asserted to imply those original bounds. The underlying finite-regularity scattering theorem is used only at its established orders.

The revised Remark4 and Section5.4 treat Proposition2(b) as an exclusion criterion: a forward-invariant open neighborhood with g=0 would give H=Q=0 and k=S=0 on its scattering image, so P2=|V|²/2 there and the sphere-mean theorem excludes a supported T-flat point. No such neighborhood is constructed. The weaker g<=0 would give k<=0 and S>=0 on k=0, excluding the negative-S open k-zero branch but not arbitrary open k-zero sets with S>=0. Every repaired quantifier is necessary and now present.

## 6. B58 finite time versus a scattering limit

The current B58 withdraws the claimed finite-time identity Q=D_C|g|^q. The rank identity dH wedge dg=0 and BH=-ag do not imply it, as the exact scalar countertest H=h, g=2h, B=-2ah partial_h shows. That countertest is not an Euler profile.

What does follow for an orbit scattering to x with k(x)!=0 is

    Q(y_t)/|g(y_t)|^q
       =[exp(bt)Q(y_t)]/|exp(at)g(y_t)|^q
       ->S(x)/|k(x)|^q=D_C,

again because aq=b and exp(at)g(y_t)->k(x). The revised current text and verdict note say precisely this. The confirmed tail component geometry and its unbounded accumulating constants remain unchanged; no uniform cusp estimate or supported W2 exclusion is added.

## 7. Evidence and remaining scope

Every line of both full differences was read against the original audit proofs. The C50 resonance, sharpness, multipole transform, component ratio, higher-jet and invariant-neighborhood repairs all pass. The B58 asymptotic repair passes. These changes resolve A1419 and A1427 as wording defects in the current versions, while the historical REFUTED entries remain in the ledger.

The configured model C agent has read and adopted the sharper C1 threshold, providing a substantive comparison through existing files; its provider runtime remains unattested. The B agent is configured model, and its failed earlier nested model request is not treated as a model response. No new client, computation or formal build was used. The common-flat, supported finite-regularity W2 and unrestricted campaign conclusions remain open.
