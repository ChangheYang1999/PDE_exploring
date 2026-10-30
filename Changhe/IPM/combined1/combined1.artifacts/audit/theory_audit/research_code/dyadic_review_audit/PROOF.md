# Independent audit of the new dyadic-radius claims

## Setting and scope

Use the exact space Y, cutoffs chi0, chi, constants C0,C1 and normalized ball B_R in ../dyadic_weighted_closure/PROOF.md, whose SHA256 is 906111ef2e54596ca432cf6513b13318dbdba9cb8f766cb784cb8e08d660d365. Let 0<a<2, 0<s<1, q=2+s, c>1 and V=cX+u. The following statements concern T2's independent review of that theorem. The original conditional theorem has now been independently confirmed. This audit separates the new consequences from that confirmation.

The low summand of Y may use w_(R_w)=(1+r^2/R_w^2)^(-a/2) with R_w>=1; keep the dyadic summands at scale1. Assume the same weighted velocity inequality with constant C_U, normalization, and low coercivity rate beta as in the original theorem. For the far-field rate assertion also require u=o(r) and D rho=o(1). These last properties hold for the campaign profiles.

## Plateau lower bounds

On the j-th plateau S_j={2^j<=r<=2^(j+1)}, the density summand obeys

    2^(2(1-a)j) ||chi(.) h(2^j .)||_(H^q)^2
      >= 2^(-2aj) ||h||_(L2(S_j))^2,
    2^(2(1-a)j) ||chi(.) h(2^j .)||_(H^q)^2
      >= 2^(2(2-a)j) ||Delta h||_(L2(S_j))^2.

Indeed the H^q Fourier multiplier dominates both1 and |xi|^4 in squared norm, since q>=2. The cutoff and its derivatives equal1 and0 on the plateau. A change of variables contributes2^(-2j), while two derivatives contribute2^(4j). The identical unscaled argument on r<2 uses chi0. Summing over disjoint plateaux gives both inequalities in T2 Lemma Y1. Since a<2, every factor in the Laplacian inequality is at least1. Therefore

    Y(h)>=||Delta h||_2.

Also w_(R_w)>=w_1 pointwise when R_w>=1, so Y(h)>=||w_1 h||_2 already follows from its low summand. These lower bounds do not imply unweighted L2 membership of h.

## The universal radius ceiling

The weighted energy of L=V.D-1+U[.].D rho on compact smooth S1 functions is

    Re<Lh,h>_(H_a)
     =-(1+c)||h||_(H_a)^2
       +a integral w_(R_w)^2 h^2 V.X/(R_w^2+r^2)
       +<U[h].D rho,h>_(H_a).

For functions supported farther and farther out, the drift quotient converges uniformly to c. The coupling quotient is bounded by C_U times the supremum of |D rho| on the support, hence tends to0. Thus a core inequality with rate beta forces

    beta <= beta_max(a)=1+c-ca.

This is the already confirmed TP-3 bound, here with its extra decay hypothesis stated. High-frequency S1 packets in direction e1 also show C_U>=1: the velocity multiplier has length1 there and the weighted norm has a fixed positive smooth weight on each packet's support.

The nonlinear inequalities (12) of T4-058 are exactly

    M Y(F)<=R,   C1 R(C_U+a)<beta,   C1 R<a0.

Because C1>1/sqrt(8pi) when s<1, all such radii necessarily satisfy

    R < R_univ(a):=sqrt(8pi)(1+c-ca)/(1+a).                 (1)

This is a bound on the sufficient closure scheme. It is not a bound on the size of all exact solutions. It requires beta_max>0, hence a<1+1/c. Replacing C_U by an available certified upper constant yields a smaller sufficient box, not a necessary bound for every possible velocity estimate.

## Rates, inverses, and the direction of a certified bound

The original hypothesis (H) is a uniform bound on the actual low inverse in Y. It is not a contractive energy estimate in Y. A high-frequency energy obstruction does not alone imply failure of (H), nor does it require s<c-1 for (H). The assertion that this inequality is necessary for (H) in T2 R6 is unsupported by its calculation. The valid conclusion is that a contractive order-(2+s) energy must have beta<=c-1-s at the normalized origin. The same distinction applies to the request for a negative packet-rate map along every path.

For an explicit demonstration of the logical distinction, let J=[[0,-1],[1,0]] and L=-b I+t J, b>0. Its numerical-range rate is exactly b, whereas ||L^(-1)||=1/sqrt(b^2+t^2), arbitrarily less than1/b. Positive numerical abscissa is also compatible with a bounded inverse. This example refutes the proposed general implication, not a separately proved IPM-specific inverse obstruction.

T4-022 certifies beta_R>0.02181481 for one weight. A lower bound on beta_R cannot upper-bound every usable rate. One may choose the valid rate

    beta_chosen=2181481/100000000,

and then evaluate (12) with this chosen constant. The resulting necessary condition on M within that particular certified box is legitimate. It must be labelled as using beta=beta_chosen; it is not necessary for every sharper energy estimate at the same weight. The rate-free consequence of (1), with the certified lower bound Y(F)>=25963000000 and a=221/200, is independent of that choice. The adjacent exact/interval calculation checks both distinct numbers.

Likewise the displayed beta0=2.04956566601 in T2 R1 is a truncated representation of an available lower certificate. It is not an upper bound on the best unweighted rate. Any method-window claim using beta<=beta0-ca must identify beta0 as a prescribed input certificate or provide a separate upper bound; otherwise the inequality direction is unjustified.

## The transport model

T2 R7 gives a genuine model counterexample to automatic high regularity from a low inverse. Let lambda>1, V=(lambda x,y), L0=V.D-1, and0<a<(lambda+3)/(2lambda). In H_a with weight(1+r^2)^(-a/2), integration by parts gives rate at least

    (lambda+3)/2-a lambda>0.

The complete flow is Phi_t(x,y)=(e^(lambda t)x,e^t y). Its low inverse is

    L0^(-1) f=-integral_0^infinity e^(-t) f(Phi_t X)dt.

The energy rate makes this integral converge in H_a; differentiating under its finite-time integral and passing to the low limit proves the distributional equation and uniqueness. Take f=x^2 y chi(r), with chi smooth, radial, compactly supported, nonnegative and nonzero. It is S1 and f_y(0)=0. For x>0 its support along the characteristic is eventually empty, and ordinary differentiation gives

    (L0^(-1)f)_y(x,0)=-(1/lambda) integral_x^infinity xi chi(xi)dxi.

This tends to a strictly negative number as x decreases to0. On the y-axis the function is identically0, so its y derivative there is0. The solution is not C1 near the origin and hence is not in Y. Smooth compact f is in Y with its canonical velocity, so this disproves the model's high estimate.

The model does not satisfy the full T4-058 background hypotheses: for lambda=2c-1 its perturbation u=((c-1)x,(1-c)y) is linear rather than sublinear, and its coupling has been removed. Its admissible low-weight window also differs from the state131 window. It is an instructive model, not an IPM-profile counterexample or proof that every possible high inverse needs the same principal energy conditions.

## Truncated far-field conclusions

T2 C1's exact leading sector can be checked directly against a complete residual expansion; the adjacent code independently reconstructs this sector from the potential. Its two angular norms are legitimate finite algebraic quantities. They are distinct from a finite-onset lower bound on the full residual.

T2 C3 uses31 sectors of an infinite expansion. Comparing the other30 terms with the first does not control the omitted remainder. Its finite shell lower estimate is therefore FLOAT, as labelled. T2 C4 further assumes a differentiated asymptotic expansion for an arbitrary correction in Y. Such an expansion does not follow from Y membership alone; even a proved asymptotic leading term would need a quantitative onset and remainder before implying the stated finite norm lower bound. These conclusions remain OPEN. No all-a exclusion of state131 in the dyadic scheme has yet been proved by that argument.

## Dependencies and verdicts

The plateau inequalities, C_U>=1, universal ceiling(1), and the scoped transport-model counterexample are CONFIRMED. The conditional T4-058 theorem is AUDITED by the independent T2 review. The claimed inference from energy packets to a necessary condition for (H) is REFUTED as an inference; actual high solvability remains OPEN. The state131 all-a exclusion based on a truncated series and an assumed correction expansion is OPEN. The chosen-rate arithmetic is separate from any claim about an optimal inverse or energy rate.
