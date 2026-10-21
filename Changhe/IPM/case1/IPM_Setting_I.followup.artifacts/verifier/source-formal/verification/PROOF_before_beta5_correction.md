# Fixed-line obstruction and formal source corrections

Date: 2026-10-20. Independent audit of the lead's fred48 result. These are local results and formal expansions, not a constructed nonlinear source solution or a global profile.

## Equations and hypotheses

Let A>1 and g>0. In coordinates (s,y) centered at the source define D_A=A s partial_s+y partial_y. The local perturbation equations are

    (D_A-1)v+g V_2+V.grad v=0,
    div V=0, curl V=-v_s.                                  (N)

Densities and second velocity components are odd in y; first velocity components are even in y. The previously checked frozen fields are

    V-mode: v=int_0^y (s²+t²)^((A-1)/2)dt,
        A=5/2, g=21/4, d=5/2;
    Q-mode: v=s int_0^y(s²+t²)^((d-2)/2)dt,
        A=7/4,g=27/8,d=5/2, or A=2,g=5,d=3.

Here d is the homogeneous degree and R=sqrt(s²+y²). Their frozen velocities are

    V-mode: V_1=s R^(A-1)/(A+1),
            V_2=-(v+s v_s)/(A+1);
    Q-mode: V_1=R^(d-2)[(d+1)s²+y²]/[d(d+2)],
            V_2=-v+y v_y/(d+2).

The full derivations and regularities are in ../frozen-source/PROOF.md and ../nonlinear-source-line/PROOF.md. They satisfy the linear part of(N), divergence and curl, and are C2 at the singular line. Thus derivatives used below are classical or distributional without interface measures. The V-mode forcing identity is V.grad v=-v v_y/(A+1), obtained by substitution and v_y=R^(A-1).

## 1. No C^(1,1) first correction across the old line for Q

For either Q field, there are no locally C^(1,1) fields (w,B) on a neighborhood of (0,y0), y0!=0, satisfying even the transport part

    (D_A-1)w+g B_2=h0,  h0=-V.grad v.                      (1)

Consequently there is no second-order amplitude expansion solving(N) in C2 on a fixed neighborhood with leading pair(v,V). This does not exclude a family whose singular line moves and whose amplitude derivatives fail to be C2.

Proof. It suffices by reflection to take y0>0. Integrate(1) against a nonnegative smooth eta(y), supported in a small positive interval, with nonzero integral. Integration by parts in y gives

    int h0 eta = A s F'(s)-F(s)-int w(y eta)'dy+g int B_2 eta dy,
    F(s)=int w(s,y)eta(y)dy.

All integrated functions are C^(1,1). Each has an affine Taylor approximation with O(s²) remainder; the same is true of sF'(s), because F' is Lipschitz. Thus so does the left side.

For d=5/2, set c_d=int_0^infinity[(1+t²)^((d-2)/2)-t^(d-2)]dt. This is finite and positive: its integrand is positive, bounded near0 and O(t^(d-4)) at infinity. Substitution and tail expansion give, uniformly for y in the support of eta,

    v=s y^(d-1)/(d-1)+c_d s|s|^(d-1)+O(s³),
    v_s=y^(d-1)/(d-1)+d c_d |s|^(d-1)+O(s²).

The differentiated remainders follow by a convergent power series of the tail for |s|<y. Since V_1(0,y)=y^d/[d(d+2)] and v_y=s R^(d-2),

    h0(s,y)=h0(0,y)-c_d y^d |s|^(d-1)/(d+2)+O(s²).

The integrated |s|^(3/2) coefficient is nonzero, contradicting the required O(s²) affine remainder. For Q_2 the exact formula

    v=s[y R+s² log((y+R)/|s|)]/2

instead gives

    h0(s,y)=-y^5/30+(y³/10)s² log|s|+O(s²).

Its integrated logarithmic coefficient is again nonzero, giving the same contradiction. The argument uses no boundary condition or div-curl inverse, so adding a smooth harmonic velocity cannot evade it.

Substituting an amplitude expansion epsilon(v,V)+epsilon²(w,B)+o(epsilon²) in C2 into(N) yields(1) at order epsilon². Since C2 functions are locally C^(1,1), such an expansion is impossible.

A related precise exclusion holds for a single exact pair v+e,V+E: it cannot satisfy uniform bounds

    |D^k e|+|D^k E|<=C R^(2d-1-k), k=0,1,2,              (2)

throughout a punctured neighborhood, for either Q field. Indeed e_lambda=lambda^(-(2d-1))e(lambda X), and likewise E_lambda, have bounded C2 norms on a fixed rectangle around(0,1). A subsequence converges in C1 on smaller rectangles to C^(1,1) limits. Divide the rescaled exact transport equation by lambda^(2d-1). Its pure quadratic frozen forcing is h0; the mixed terms carry lambda^(d-1), and the remainder-remainder term lambda^(2d-2), so tend uniformly to zero. The limit solves(1), contradiction. Bounds only on a left cone, weaker radial orders, or lack of uniform derivative bounds across the line are not excluded.

## 2. The scalar backward inverse can destroy left-axis smoothness

For h=O(R^M), M>1, the integral

    Ih(s,y)=int_-infinity^0 exp(-t)h(exp(A t)s,exp(t)y)dt

converges and has size O(R^M). Along characteristics differentiation proves (D_A-1)Ih=h. A homogeneous solution of order O(R^M) has exp(-t)w(Phi_t X) tending to zero backwards and is zero, proving uniqueness in that order class. These are function/characteristic claims; high spatial derivative bounds need separate justification.

If |partial_s^i partial_y^j h|<=C R^(M-i-j) and i+j<=M, differentiation under the integral gives the bound C R^(M-i-j)/[M-1+(A-1)i]. This uses R(Phi_t X)<=exp(t)R(X) with a nonnegative exponent. For i+j>M one must use the lower bound R(Phi_t X)>=exp(A t)R(X), giving a denominator AM-1-(A-1)j only if positive. No arbitrary-order preservation follows.

For the explicit A=5/2, h=y(s²+y²)^(3/2), substituting tau=exp(3t) gives

    Ih=2y[(s²+y²)^(5/2)-|y|^5]/(15s²), s!=0.

This is O(R^4) and solves the equation, but at every fixed s<0 its y|y|^5 term is not C6 at y=0. Thus punctured-plane smooth forcing need not give an inverse smooth on the open left axis. This is a limitation of the scalar inverse, not a theorem about all solutions of(N).

## 3. Linear homogeneous inversion on a left cone

Write s=-r<0, z=y/r. On |z|<1, let h(z) be odd and analytic and p>1. Seek a density w=r^p phi(z) and velocity B=r^p(alpha(z),beta(z)). The forced linear part of(N), divergence and curl become

    (Ap-1)phi+(1-A)z phi'+g beta=h,
    beta'=p alpha-z alpha',
    -p beta+z beta'-alpha'=p phi-z phi'.                    (3)

For odd indices j define c_j(p)=Ap-1-(A-1)j. Normalize phi_1=0, beta_1=h_1/g, and alpha_0=beta_1/p. Coefficient comparison yields

    phi_j=(h_j-g beta_j)/c_j(p),
    beta_(j+2)=-(p-j)(p-j-1)(beta_j+phi_j)/[(j+1)(j+2)],
    alpha_(j+1)=(j-p)(beta_j+phi_j)/(j+1).                  (4)

The formulas imply all three equations(3), not just transport. Phi_1 could also be chosen freely, with beta_1 adjusted. At an odd-index resonance p=j-(j-1)/A, a purely homogeneous solution requires h_j=g beta_j; if this holds phi_j is free. If compatibility fails for every allowed phi_1 no purely homogeneous analytic-axis solution exists.

To prove convergence, fix a complex disk radius rho<1 strictly inside the analyticity radius of h. Weighted coefficients h_j rho^j are bounded, c_j is comparable to j for large j, and the beta recurrence multiplier tends to -rho². Hence its modulus is eventually less than a fixed number below1, and the forcing contribution is bounded. Induction bounds the weighted beta and phi coefficients, with at most polynomial factors for alpha. Their series converge on each smaller disk. The argument is uniform when p varies in a compact set away from its finitely relevant resonances.

At a given resonance just one c_j vanishes. The same recurrences define a meromorphic triple near that p, with at most a simple pole, since all later steps are linear and their denominators nonzero. The locally uniform bounds justify this assertion for the analytic angular functions, not only their coefficients. Multiply by r^p and take the Laurent constant term. Physical differential operators are independent of p, so they commute with taking the constant term and produce forcing r^p h at the resonant value. The pole introduces a log r term. For forcing r^p (log r)^k h, differentiate the meromorphic family k times in p before taking that constant term. This gives finite powers of log r and solves all three equations. Thus each power-log coefficient problem on a smaller left cone is solvable. This is not an inverse bounded uniformly in radial degree or on a neighborhood crossing s=0.

## 4. Formal iteration, resonance and its limits

Starting from any of the three frozen modes, define p_n=1+(n+1)(d-1), n>=0. At order n>=1 solve the linear problem with forcing

    -sum_(i+j=n-1) V_i.grad v_j.

Products and derivatives of prior finite power-log sums have degree p_n and analytic angular coefficients on |z|<1. Section3 constructs the next coefficient, preserving parities, divergence and curl. Induction proves an all-orders formal solution. For each finite N its residual is O(r^(p_(N+1))(1+|log r|^K)), and each fixed derivative order lowers the power correspondingly on smaller closed cones. All constants may depend on N and derivative order. No bound in N, convergence, or extension across s=0 is obtained.

The possible resonant odd indices are (5n+7)/2 for V_(5/2), (7n+9)/2 for Q_(7/4), and4n+5 for Q_2. The first correction resonances are n=3 in the first two cases and n=1 for Q_2. For Q_2 at n=1, p=5, expansion of the exact forcing gives

    h=4z/15+z³/15-2z^5/25+11z^7/525-4z^9/315+... .

Regardless of phi_1, the factor p-j-1 at j=3 gives beta_5=0 and the factor p-j at j=5 gives beta_7=0. Thus phi_7=h_7/2, beta_9=-h_7/24, and

    h_9-g beta_9=-1/120.

No purely homogeneous degree5 correction analytic at the axis exists. Since c_9(p)=2(p-5), the phi_1=0 meromorphic construction has coefficient -1/240 of r^5 z^9 log r. These are radial logarithms, smooth at every point of the open left axis, not log|y| singularities. First-correction phi_3,phi_5 with the chosen normalization are (8/63,1/70), (32/405,-11/405), and(1/10,-1/48) for V,Q_(7/4),Q_2 respectively. The exact checks are retained in verification/checks.json.

For Z_j=r^((j-1)/A) partial_y^j f(-r,0)/j!, a correction of radial degree M with axis derivative bounds contributes O(r^(M-j+(j-1)/A)(1+|log r|^K)). The first correction degrees2d-1 give positive fifth-order exponents3/5,9/7,2 respectively. Later ones are larger. Thus each finite formal truncation preserves the frozen leading Z3,Z5 behavior. It is not an exact field solving(N).

For any actual nonlinear source solution with w(s)=W_1(s,0), g1=f_y(s,0), the axis equations give wg1'=(w'-A)g1. Hence a positive homogeneous solution of the j-th axis ODE is C g1^(j+(j-1)/A)|w|^(-(j-1)/A). If w(-r)/r tends to -A and g1(-r) tends to g>0, it is K r^(-(j-1)/A)(1+o(1)), K>0. This justifies interpreting the zero/nonzero/divergent Z_j limits as the corresponding endpoint limits, whenever the axis derivatives exist. It supplies no actual field to which the formal expansion can be applied.

## Audit scope and dependencies

The exact symbolic checks independently implement the frozen cone series, forcing, recurrence, resonance defect, radial log coefficient, and scalar inverse identity. No lead code is imported or executed. The proof above confirms these principal fred48 results and their limitations. Its third-order Fourier construction is not needed for these statements and is not independently re-proved here; extending the formal theorem to it is conditional on an analytic odd angular germ of the stated frozen degree. All global canonical, center, source matching and growth requirements remain separate. Neither endpoint nor nonlinear sharpness of a source threshold follows.
