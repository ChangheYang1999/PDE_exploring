# Higher angular weak probes for fixed-c L2 corrections

## Statement, hypotheses and notation

Let c>1, let rho be a smooth real S1 background on R2, and let u=U[rho] be its canonical divergence-free velocity. Assume u=O(r^gamma), grad rho=O(r^(gamma-1)) for some gamma<1, and F=(cX+u).grad rho-rho belongs to L2(R2). Suppose h is real, belongs to L2(R2), has canonical velocity U[h] in L2 with norm at most ||h||2, and satisfies in distributions

    F+div((cX+u)h)-(2c+1)h+U[h].grad rho+div(U[h]h)=0.

Fix a positive odd integer n and integer K>=(n-1)/2. Write t=r2/(1+r2), v=1-t, and define

    phi_(n,K)=r v2 t^K sin(n theta).

Let d_K(t)=(2K+1)-(2K+4)t. Define the finite quantities

    I=int F phi,
    A=||(2c+1)phi+cX.grad phi||2,
    B2=int |u|2 v4 t^(2K) [d_K(t)^2+n2] dX,
    C2=int |grad rho|2 r2 v4 t^(2K) dX,
    H=max(2K+1,3) K^K 2^2/(K+2)^(K+2),

where the final fraction is1 when K=0. B and C denote the nonnegative square roots of the displayed quantities. Then, with D=A+B+C and m=||h||2,

    |I|<=D m+H m2,
    m>=2|I|/(D+sqrt(D2+4H|I|)).

A positive rational number strictly below the latter expression is a necessary lower bound for every correction with the stated hypotheses. This is not a sufficient existence criterion and makes no claim about varying c or a different background.

## Smoothness, testing and pointwise bounds

The numerator r^(2K+1) sin(n theta) is the harmonic polynomial r^n sin(n theta) times (x2+y2)^(K-(n-1)/2). Thus phi is globally smooth. At infinity phi=O(r^-3) and grad phi=O(r^-4). Smooth radial cutoffs permit testing the distributional equation: the linear coefficient products belong to L2, and U[h]h belongs to L1. Terms involving cutoff gradients vanish by these decays and the sublinear background growth. Integration by parts therefore gives the same weak identity as in ../pure_l2_probe/PROOF.md.

The polar components of grad phi are

    v2 t^K d_K(t) sin(n theta),
    n v2 t^K cos(n theta).

Their squared length is at most v4 t^(2K)(d_K(t)^2+n2). This gives ||u.grad phi||2<=B. Also |phi|<=r v2 t^K gives ||phi grad rho||2<=C. Since |d_K(t)|<=max(2K+1,3) and n<=2K+1, the exact angular maximum of |grad phi| is at most max(2K+1,3) v2 t^K. Differentiation of t^K(1-t)^2 gives maximum K^K 2^2/(K+2)^(K+2) for K>0, and maximum1 for K=0. Hence H is a global bound. Cauchy-Schwarz, ||U[h]||2<=m and the triangle inequality give the asserted quadratic inequality. Solving it yields the displayed stable positive-root formula.

## Exact full-plane integration for the finite candidate class

For the exact rational candidate let delta=1-1/c and p_j=2-(j+1)delta/2. The N4 Cartesian field construction has the forms

    u_i=r sum_(j,l) v^(2-p_j) U_(i,j,l)(t) trig_l(theta),
    partial_i rho=sum_(j,l) v^(2-p_j) R_(i,j,l)(t) trig_l(theta).

All polynomials are rational. For each pair of matching angular frequencies, combine their polynomial products at v=1-t into W_b(v), with b=5-p_j-p_j'. Include twice each distinct radial-branch pair and twice a constant cosine mode, since its angular integral is2pi instead of pi. Sum Cartesian components separately. This gives velocity polynomials W_b^u and density-gradient polynomials W_b^rho. The factor r dr=dv/(2v2) then gives

    B2=(pi/2) sum_b int_0^1 v^b (1-v)^(2K+1)
        [((2K+4)v-3)^2+n2] W_b^u(v) dv,
    C2=(pi/2) sum_b int_0^1 v^b (1-v)^(2K+1) W_b^rho(v) dv.

These are upper bounds for the desired transport and density terms because only the explicit pointwise angular bounds above were applied. The integration itself is complete. No angular residual component enters I except its exact n-th sine projection. If

    F=r sum_(ell,l) v^(ell delta/2) P_(ell,l)(t) sin(l theta),

orthogonality gives

    I=(pi/2) sum_ell int_0^1 v^(ell delta/2-1)
        (1-v)^(K+1) P_(ell,n)(1-v) dv.

Write L0=3c+1+2cK, L1=2c(K+2), a=2K+2. Then

    A2=(pi/2) [L0^2-2L0 L1 a/(a+2)
               +L1^2 a(a+1)/((a+2)(a+3))]/[a(a+1)].

This follows by integrating t^(2K+1)(1-t)(L0-L1 t)^2. It is independent of n>0 because each sine has squared angular integral pi.

Every radial integral is a finite sum of beta moments B(b+j+1,M+1), with positive arguments. Starting at the gamma-function expression for j=0, successive moments have exact ratio (b+j+1)/(b+j+M+2). Arb evaluates gamma functions and all polynomial operations outward. Exact endpoint zeros are retained before conversion. The code requires integrable exponents and positive, accurate energy enclosures. All residual modes and background cross terms contributing to each target are retained.

## Verification, dependencies and scope

The candidate source, independently assembled complete residual cache and its verification record, code, proof and field helpers are hashed. The n=1 pairings, A and C quantities are compared against previously retained exact first-mode values where their K values coincide. The new B and H are explicit, possibly less sharp bounds and are not claimed equal to older choices. Analytic differentiation of phi is checked using exact Cartesian harmonic polynomials at rational points for selected n,K. Positive beta moments are checked against elementary rational fixtures.

The finite scan is a search for a useful necessary test. It does not establish optimality over all probes or certify an optimizer. A candidate-specific new bound remains OPEN until an independent lane verifies the argument and arithmetic. The purpose is to test angular components absent from the first-sine pairing objective, while retaining a complete-plane certificate for each individual test.
