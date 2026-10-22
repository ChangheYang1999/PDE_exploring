# Resonant logarithms and angular compatibility in the global-source class

Date: 2026-10-20. Status: CONFIRMED by independent derivation and exact algebra, with actual Opus 5.5 audit69 checked and its smooth-remainder correction adopted.
This is a necessary-condition theorem in G, not an existence or nonexistence endpoint.

## 1. Statement, notation and dependencies

Let a smooth full-plane B2 profile satisfy the prompt's polynomial source-tail and canonical sublinear relative-velocity assumptions. Suppose beta>2, a0>0 and W=beta X+V has exactly one zero, at0. This is subclass G. Use the smooth area coordinates Xi=(xi,eta) constructed in packet48, normalized by Xi(0)=0 and DXi(0)=I, with det D Xi identically1, parity xi odd and eta even in x, and xi>0 exactly on {x>0}. Write

    lambda=(beta-2)/2, mu=(3beta+2)/2,
    W.xi=lambda xi, W.eta=mu eta+kappa xi^k,
    Theta=a0 xi^2.

When kappa is nonzero, k=mu/lambda is an even integer at least4. Here restrict to these resonant exponents, allowing kappa=0 also:

    beta=2(k+1)/(k-3), k even, k>=4.

Put alpha=lambda/beta and gamma=mu/beta=k alpha, so alpha+gamma=2. Packet61 proves that the canonical escape map Phi and its inverse are smooth away from0; detDPhi=1 and Phi(phi_tY)=exp(beta t)Phi(Y). Both Phi and Xi preserve orientation and commute with S(x,y)=(-x,y). Packet66 gives the smooth angular temperature tail h, positive off the vertical directions, with positive quadratic zeros there, and the exact identity Theta(Phi^{-1}(r e(theta)))=r^(2 alpha)h(theta), where 2 alpha=(beta-2)/beta. Define smooth functions q,g on the circle by

    (q(theta),g(theta))=Xi(Phi^{-1}(e(theta))),
    e(theta)=(cos theta,sin theta).

The two maps preserve the open half-planes and commute with S. Thus q>0 on (-pi/2,pi/2), q<0 on the other open semicircle, q is odd under theta -> pi-theta, and g is even under that reflection. In particular q is odd about each vertical direction and g is even there.

Then, for every r>0,

    xi(Phi^{-1}(r e(theta)))=r^alpha q(theta),
    eta(Phi^{-1}(r e(theta)))=
        r^gamma [g(theta)+(kappa/beta)q(theta)^k log r],                 (1)
    q=sign(cos theta)sqrt(h/a0),
    alpha q g' - gamma q' g -(kappa/beta)q^k q'=1.                    (2)

Both vertical zeros of q are simple. At theta_-= -pi/2 and theta_+=pi/2,

    g(theta_-)<0<g(theta_+),
    -gamma q'(theta0)g(theta0)=1, theta0 in {theta_-,theta_+}.       (3)

For either vertical direction theta0 define the finite Taylor coefficient

    Res(q;theta0)=[s^k] (s/q(theta0+s))^(k+1).                        (4)

The quotient in(4) extends smoothly and is nonzero at0. The notation [s^k] means the k-th derivative at0 divided by k!, not an assumption of analyticity. The same resonant coefficient must satisfy

    kappa=-beta Res(q;theta_-)= -beta Res(q;theta_+).                  (5)

Thus a proposed temperature tail in G at a resonant beta has a necessary matching condition at its two axis endpoints. At k=4, beta=10, write a=q'(theta0), q3=q'''(theta0), q5=q'''''(theta0). Then

    kappa=beta [q5/(24 a^6) - 5 q3^2/(12 a^7)].                      (6)

This is a condition involving the normalized source coordinate xi, whose scale is fixed by DXi(0)=I. It is not independent of a0 when h alone is prescribed.

On either open half-plane the corrected angular function

    ghat=g-(kappa/lambda)q^k log|q|                                  (7)

has exactly one zero. This statement concerns the linearized C^(k-1) fast coordinate eta-(kappa/lambda)xi^k log|xi|. The uncorrected g need not obey the same monotonic quotient equation.

If kappa!=0, on each sufficiently large scattering circle {Phi(Y)=r e(theta)}, eta(Y) has exactly one zero in each open half-plane. On the right its angle approaches the lower vertical if kappa>0, and the upper vertical if kappa<0. If theta0 is that endpoint, its distance s_r to the endpoint within the right semicircle satisfies

    s_r=[beta/(gamma |kappa| |q'(theta0)|^(k+1))]^(1/k)
             (log r)^(-1/k) [1+O((log r)^(-2/k))].                  (8)

No analogous assertion is made here about zeros of vorticity or critical points of temperature.

## 2. The exact radial logarithm and area equation

The explicit triangular flow in source coordinates is

    xi_t=e^(lambda t) xi,
    eta_t=e^(mu t)(eta+kappa t xi^k).

The equality mu=k lambda is the only reason the second formula has a factor t. Apply the two conjugacies to the point Phi^{-1}(e(theta)) with t=log r/beta. This proves(1). The temperature representation from packet66 immediately identifies q with the signed square root of h/a0, and gives simple vertical zeros because h''>0 there.

Write L(theta)=(kappa/beta)q^k. The polar Jacobian determinant of H=Xi o Phi^{-1} is

    det(partial_r H,partial_theta H)
      =r^(alpha+gamma-1) [alpha q g'-gamma q'g-Lq'
                         +(alpha q L'-gamma q'L)log r].

The logarithmic coefficient is zero because gamma=k alpha. Both Xi and Phi preserve area and orientation, so this determinant equals r. Since alpha+gamma=2, division gives(2). At either vertical direction q=0, so(3) follows from(2). The signs follow from q'(theta_-)>0 and q'(theta_+)<0. Equation(2) also directly proves that the zeros of q are simple and g does not vanish at either endpoint.

## 3. Absence of a logarithmic singularity at each vertical direction

On an interval where q!=0, divide(2) by alpha q^(k+1) to obtain

    (g/q^k)'=1/(alpha q^(k+1))+(kappa/(alpha beta))q'/q.              (9)

Fix theta0, set s=theta-theta0, and write q=s u(s), where u is smooth, even and nonzero near0. Likewise g is smooth and even. Hadamard's finite Taylor formula gives

    g/u^k = sum_(j=0)^k B_j s^j + s^(k+1)R(s),
    u^(-k-1) = sum_(j=0)^k C_j s^j + s^(k+1)S(s),

with R,S smooth near0. The left side of(9) is the derivative of s^(-k)g/u^k, hence equals sum_(j=0)^k (j-k)B_j s^(j-k-1)+(sR(s))'. The last term is bounded. Its finite Laurent expansion therefore has no s^(-1) term: the only possible j=k coefficient is multiplied by0. This controls the differentiated remainder using smoothness, without analyticity.

The s^(-1) coefficient of the first term on the right side is C_k/alpha=Res(q;theta0)/alpha. Since q'/q=1/s+u'/u, the second term contributes kappa/(alpha beta). The difference of the two sides is a finite sum of negative powers of s plus O(1) and is identically zero on a punctured interval. Multiplying by the most negative power's inverse and taking s to0 successively forces every negative-power coefficient to vanish. In particular the s^(-1) coefficient vanishes, proving(5). Equivalently, integrate(9): any nonzero sum would produce an s^k log|s| term in g, inconsistent with its smoothness. Formula(6) follows by expanding

    q=a s+b s^3+c s^5+O(s^7),
    q^(-5)=a^(-5)s^(-5)
             [1-5(b/a)s^2+(15(b/a)^2-5c/a)s^4+O(s^6)],

and using b=q3/6 and c=q5/120.

Changing eta to eta+c xi^k preserves the normalization, area, parity and kappa, and changes g to g+c q^k. This leaves(2) and(5) unchanged. The argument gives the same coefficient kappa at both ends. It does not prove that this common value vanishes. At kappa=0 it states that the two coefficients(4) are both zero.

## 4. The corrected coordinate and its angular zero

Subtract (kappa/lambda)log|q| from g/q^k in(9), using lambda=alpha beta. Then

    (ghat/q^k)'=1/(alpha q^(k+1)).                                  (10)

On the right semicircle the derivative is positive. Because k is even, q^k is positive and tends to0 at either endpoint; q^k log|q| tends to0, while g tends to the nonzero signed constants in(3). Hence ghat/q^k tends to minus infinity at the lower endpoint and plus infinity at the upper endpoint. It is strictly increasing, so it has exactly one zero. Reflection gives the left-half-plane assertion. Although ghat is smooth within the open semicircles, the logarithmic correction is generally only C^(k-1) across the axis. No smooth linearization is inferred when kappa!=0.

## 5. Large-radius zeros of the uncorrected fast coordinate

Take kappa>0 first and write A=(kappa/beta)log r -> +infinity. By(1), zeros are those of g+Aq^k. On compact subsets of the open right semicircle Aq^k dominates g, and close to the upper endpoint both g and Aq^k are positive. Thus all zeros eventually lie near theta_-.

Set s=theta-theta_->0, a=q'(theta_-)>0, g0=g(theta_-)<0. Parity and smoothness give

    q=a s(1+O(s^2)),   g=g0+O(s^2).

Every root is trapped between positive fixed multiples of A^(-1/k), because g is bounded away from0 there. At these roots and throughout their fixed-multiple interval,

    (g+Aq^k)'=O(s)+Akq^(k-1)q'>0

for A large. There is at least one root by the intermediate value theorem, since the expression is negative at s=0 and positive at a sufficiently large fixed multiple of A^(-1/k). Hence the root is unique. Substitution gives

    s=(-g0/(A a^k))^(1/k)(1+O(A^(-2/k))).

Using -gamma a g0=1 proves(8). For kappa<0 the same argument at theta_+, with s=theta_+-theta, q=(-q'(theta_+))s(1+O(s^2)) and g0>0, proves the other case. Reflection supplies the left root. The circles here are scattering-coordinate circles, as expressly stated; the argument has not replaced them by physical circles.

## 6. Scope and verification

Dependencies are the full B2 class reduction and G structure, packets48,61,65,66. The results allow every even source resonance permitted by those proofs. They supply identities and a tail-matching diagnostic, with no sign assumption on vorticity and no extra reflection in y. There is no full PDE candidate, no exclusion of G, and no early-stop authorization.

The exact formulas and signs were derived independently from the triangular flow and the two-dimensional Jacobian. A separate symbolic check and actual model audit are recorded in verification as they finish. No Lean/Lake formalization or numerical existence claim is made.
