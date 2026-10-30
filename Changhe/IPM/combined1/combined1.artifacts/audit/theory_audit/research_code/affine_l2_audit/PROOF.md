# The residual threshold in an unweighted L2 affine class

## 1. Statement

Let rho be a smooth real function on R2. Assume its canonical velocity u=U[rho] is smooth and divergence free and, for some gamma<1 and all large r,

    |u(X)|<=C r^gamma,  |grad rho(X)|<=C r^(gamma-1).

Fix a real c and set F_c=(cX+u).grad rho-rho. Suppose for a real q>=-1 and a nonzero smooth real angular function E that

    F_c(r,theta)=r^q E(theta)+o(r^q)                         (1)

uniformly in theta as r tends to infinity. Then there is no h in L2(R2) satisfying the stationary correction equation in divergence form

    F_c+div((cX+u)h)-(2c+1)h+U[h].grad rho
        +div(h U[h])=0                                    (2)

in distributions. Here U[h]=(-R1R2 h,R1^2 h) is defined by the L2 Fourier multipliers, and all products are locally integrable.

This proves N4's theorem for corrections with bounded gradient and strengthens it by removing that hypothesis. The original theorem is independently CONFIRMED. The stated weaker-regularity version is a T4 addition pending independent review.

## 2. Annular test proof

Choose a smooth nonnegative radial eta supported in 1<r<2, not identically zero. Define psi(r,theta)=eta(r)E(theta) and

    phi_R(X)=R^-1 psi(X/R),  A_R={R<|X|<2R}.

All tests are smooth and compactly supported, so no limiting definition of (2) is required. Its weak form is

    <F_c,phi_R>=<h,(cX+u).grad phi_R+(2c+1)phi_R>
                -<U[h],phi_R grad rho>
                +<h U[h],grad phi_R>.                     (3)

Dilation gives

    ||phi_R||2=||psi||2,
    ||cX.grad phi_R+(2c+1)phi_R||2
        =||cY.grad psi+(2c+1)psi||2=:C0,
    ||grad phi_R||2=R^-1||grad psi||2,
    ||grad phi_R||infinity=R^-2||grad psi||infinity.

The background bounds therefore imply, for constants C1,C2 independent of R,

    |<F_c,phi_R>| <= ||h||L2(A_R)(C0+C1 R^(gamma-1))
        +C2 R^(gamma-1)||U[h]||L2(A_R)
        +R^-2||grad psi||infinity
             ||h||L2(A_R)||U[h]||L2(A_R).                  (4)

The multiplier identity ||U[h]||2<=||h||2 makes both annular norms finite and tending to zero as R tends to infinity. Since gamma<1, the entire right side tends to zero. In fact the last term could be bounded using the full L2 norms and still tends to zero. No derivative of h was used.

In contrast, substituting X=RY and (1) gives

    <F_c,phi_R>=R^(q+1)(A+o(1)),
    A=(integral_1^2 r^(q+1) eta(r)dr)
        (integral_0^(2pi) E(theta)^2 dtheta)>0.

For q=-1 this tends to A; for q>-1 it diverges to positive infinity. Both contradict (4). This proves the theorem, including the endpoint q=-1. For corrections with bounded weak gradient, div(h U[h])=U[h].grad h in distributions, so the original N4 formulation is included.

## 3. Exponent rigidity

Assume additionally, uniformly in angle,

    rho=r^gamma Theta(theta)+o(r^gamma),
    X.grad rho=gamma r^gamma Theta(theta)+o(r^gamma),

where -1<gamma<1, gamma is nonzero, and Theta is nonzero and smooth. Suppose F_c0=o(r^gamma) at one exponent c0. Then for c different from c0,

    F_c=F_c0+(c-c0)X.grad rho
       =(c-c0)gamma r^gamma Theta+o(r^gamma).

The theorem applies with q=gamma and nonzero E=(c-c0)gamma Theta. Thus no distributional L2 correction can change c. This is an affine-class fact with no norm-smallness assumption.

## 4. Scope and verification

This theorem applies only after the uniform asymptotic expansion, its nonzero coefficient and the background growth hypotheses have been established for the specific reference. It does not establish those facts from sampled data. For the independently checked state131 expansion, q=2gamma-1>0 and its leading coefficient is nonzero. Hence the unrepaired state has no bounded-gradient L2 correction at its c, or at another c under the stated rigidity hypotheses. The strengthened theorem makes the same conclusion for the divergence-form class (2), once independently reviewed.

The statement does not exclude a non-L2 tail repair, a weighted correction, or a different affine reference. For d2 and exact repaired candidates whose residual begins below -1, this particular obstruction does not apply; the quantitative pure-L2 test is separate. No claim about convergence of a formal exterior series is made.

The frozen N4 source is source/N4_PROOF.md. This proof uses elementary dilation, the weak equation, Plancherel and convergence of L2 tails. No numerical computation or formal proof-assistant run is needed.
