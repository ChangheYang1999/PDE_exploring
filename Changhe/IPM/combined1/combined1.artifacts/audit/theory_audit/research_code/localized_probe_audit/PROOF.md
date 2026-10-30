# Localized weak tests from independently reconstructed polar fields

Written 2026-10-28 before executing the numerical certificate. The N4 statements and their numerical outputs are frozen in source/. This audit uses a different field reconstruction and never reads the N4 residual cache.

## Statement and hypotheses

Let rho and u=U[rho] be smooth real S1 fields on the plane. Here S1 means rho is even in x and odd in y; u is the canonical divergence-free velocity with Fourier vector multiplier of Euclidean modulus at most one. Suppose u=O(r^gamma), D rho=O(r^(gamma-1)) for some gamma<1. Fix real c, set V=cX+u and F=V.D rho-rho, and assume F belongs to L2. A correction h is any real L2 function satisfying

    F + div(V h) -(2c+1)h + U[h].D rho + div(h U[h]) = 0

in distributions, with all the displayed products interpreted locally. In particular h U[h] is locally integrable. There is no gradient bound on h. Let k be a nonnegative integer, W=(1+r^2)^(-1), T=1-W, and

    phi_k = y T^k W^2,
    L_k = 3c+1+2ck W-4c T,
    G_k = 1+2k W+4T,
    I_k = |integral F phi_k|,
    A_k = ||phi_k L_k||_2,
    B_k = ||T^k W^2 G_k u||_2,
    C_k = ||r T^k W^2 D rho||_2,
    D_k = A_k+B_k+C_k.

For a>=0, b>0 put S(a,b)=a^a b^b/(a+b)^(a+b), with S(0,b)=1. Set H_0=1 and H_k=S(k,2)+2k S(k,3)+4 S(k+1,2) for k>=1. Then every such correction has m=||h||_2 satisfying

    I_k <= D_k m+H_k m^2.                                      (1)

When I_k>0, this implies

    m >= 2 I_k/(D_k+sqrt(D_k^2+4H_k I_k)).                     (2)

These are necessary fixed-c distances, not an existence theorem or a bound uniform over changing c. A maximum over the finitely many evaluated k remains a necessary bound.

## Proof of the inequality

Testing the equation first against compactly supported smooth phi and integrating the divergence terms gives

    <F,phi> = <h,V.Dphi+(2c+1)phi>
              -<U[h],phi D rho>+<h U[h],Dphi>.

The velocity multiplier bound and Cauchy-Schwarz give

    |<F,phi>| <= m(||V.Dphi+(2c+1)phi||_2+||phi D rho||_2)
                   +m^2 ||Dphi||_infinity.                    (3)

For phi=phi_k, all linear coefficients in (3) belong to L2, by the stated sublinear growth and phi_k=O(r^-3), Dphi_k=O(r^-4). Replace phi_k by chi(X/R)phi_k, with a fixed smooth compact radial cutoff chi=1 near zero. The added linear coefficient phi_k V.Dchi(X/R)/R tends to zero in L2. The added nonlinear coefficient phi_k Dchi(X/R)/R tends to zero uniformly. The original nonlinear pairing converges by h U[h] in L1, and the residual pairing by F in L2. Thus (3) holds for phi_k.

Direct differentiation gives

    Dphi_k = T^k W^2[e_y+2yX W(kW/T-2)],
    cX.Dphi_k+(2c+1)phi_k = phi_k L_k.

At T=0 the apparent pole cancels when k>=1; the k=0 term with that coefficient is zero. Since |yX|<=r^2 and r^2 W=T,

    |Dphi_k| <= T^k W^2(1+2kW+4T).

The maximum of T^a(1-T)^b on [0,1] is S(a,b), by a one-variable derivative and the endpoints. This proves ||Dphi_k||_infinity<=H_k for k>=1. For k=0, D[X W^2] has radial eigenvalue W^2(1-4T) and tangential eigenvalue W^2. Their absolute values are at most one: the negative radial maximum is max_(0<=T<=1) (4T-1)(1-T)^2=1/4. Hence the y component phi_0 has gradient norm at most one. Finally |phi_k|<=r T^k W^2 and the triangle inequality bound the linear coefficient in (3) by D_k. This proves (1). Solving its positive quadratic root proves (2).

## Independent polar evaluation

The rational potential coefficients determine finite expansions, already derived independently in T4-018 and T4-031,

    rho = r sum_(j,n) W^a_j R_(j,n)(T) sin(n theta),
    psi = r^2 sum_(j,m) W^a_j S_(j,m)(T) sin(m theta),
    a_j=(j+1)(1-1/c)/2,
    u_r=-partial_theta psi/r, u_theta=partial_r psi.

The code reconstructs these polynomials from the potential and checks all divisions by T^2 exactly. Define D_(a,l)P=(l-2aT)P+2T(1-T)P'. Then

    u_r=-r sum W^a_j m S_(j,m) cos(m theta),
    u_theta=r sum W^a_j D_(a_j,2)S_(j,m) sin(m theta),
    partial_r rho=sum W^a_j D_(a_j,1)R_(j,n) sin(n theta),
    partial_theta rho/r=sum W^a_j n R_(j,n) cos(n theta).

Angular orthogonality, r^3 dr=T W^-3 dT/2, and summing unordered branch pairs with multiplicity two give B_k^2 as pi/2 times the sum of

    integral_0^1 T^(2k+1) W^(1+a_i+a_j) G_k^2
       [m^2 S_i S_j+D_(a_i,2)S_i D_(a_j,2)S_j] dT.             (4)

C_k^2 uses the same formula without G_k^2 and with S replaced by R, m by n and radial order2 by1.

The pairing is obtained directly by integration by parts in the background equation, independently of a residual expansion. Its linear part is

    -(pi/2) sum_j integral_0^1 T^(k+1) W^(a_j-1) R_(j,1) L_k dT. (5)

The nonlinear part is pi/4 times the sum, over |n-m|=1 and sigma=sign(n-m), of

    integral_0^1 T^(k+1) W^(a_j+a_i-1) R_(i,n)
       [sigma m S_(j,m)(1+2kW-4T)-D_(a_j,2)S_(j,m)] dT.       (6)

The angular identities are integral sin(n theta)cos(m theta)sin(theta)=sigma pi/2 and integral sin(n theta)sin(m theta)cos(theta)=pi/2. All other pairs vanish. The background boundary terms vanish because gamma<1: at infinity their orders are r^(gamma-1) and r^(2gamma-2), and smoothness handles zero. This establishes (5)-(6) with their signs.

Finally A_k^2=(pi/2) integral_0^1 T^(2k+1) W L_k^2 dT. This can be integrated by the same method as the other components, without N4's closed rational A_k formula.

## Gamma-free beta arithmetic

For each rational b>-1 and integer M>=0 define

    beta(b,M)=integral_0^1 W^b(1-W)^M dW
             = 1/(b+1) product_(m=1)^M m/(b+m+1).            (7)

Integration by parts or induction proves (7). If P(1-W)=sum_l p_l W^l, integrate W^b(1-W)^M P(1-W) by summing p_l beta(b+l,M). The successive moments obey

    beta(b+l+1,M)=beta(b+l,M)(b+l+1)/(b+l+M+2).

All coefficients and exponent shifts are exact rationals. Arb evaluates positive products, sums and square roots outward; no gamma implementation is used. Every endpoint condition b>-1 is checked. The largest polynomial degree is independent of k. Thus this construction independently tests both N4's Cartesian field sums and its gamma-based beta integrals.

## Verification and scope

The script must record positive squared norm enclosures, all constituent values, input hashes, and overlap with the frozen N4 output. The numerical results remain pending until that execution completes. This proof audits N4's necessary inequality; it does not validate an asymptotic extrapolation of its finite list. No formal code or build is claimed.
