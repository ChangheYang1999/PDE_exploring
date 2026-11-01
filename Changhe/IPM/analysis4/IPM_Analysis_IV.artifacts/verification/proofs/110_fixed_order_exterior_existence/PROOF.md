# Exterior solutions behind any finite canonical truncation

Status: PROVED. Independent audit of the theory part's corrected Theorem S, recorded in V204. This statement concerns existence behind a fixed finite truncation. It does not assert convergence or summability of the infinite canonical series.

## Statement

Fix c>1, delta=1-1/c, p_n=1-n delta and P_n=2-n delta. Let f_1 be a real smooth angular function that is even under x reflection and odd under y reflection. Construct a finite collection F_n(t,theta), G_n(t,theta), 1<=n<=N, by the canonical stationary recurrence, allowing arbitrary fixed constants in resonant stream modes. For irrational delta these are independent of t; for rational delta they are polynomials in t. Write

    rho_N=sum_(n<=N) exp(p_n t) F_n(t,theta),
    psi_N=sum_(n<=N) exp(P_n t) G_n(t,theta),   t=log r.

For any integer k>=4 and any beta strictly between p_(N+1) and p_N, excluding beta=-3,-5,-7,..., there is R<infinity and an exterior pair rho in C^(k-2), psi in C^(k-1) such that

    -Delta psi=partial_x rho,
    (c X+u).grad rho=rho,   u=(-psi_y,psi_x),

on r>R. The density has the stated reflection symmetries, and psi is odd separately in x and y. For Cartesian derivatives of total order m,

    |D^m(rho-rho_N)| <= C r^(beta-m),       m<=k-2,
    |D^m(psi-psi_N)| <= C r^(beta+1-m),     m<=k-1.

There is a single-valued pressure p on this exterior with u+(0,rho)=-grad p, and div u=0. The construction is unique in the fixed auxiliary class specified below. Neither exterior uniqueness nor identification of solutions obtained from different truncations or weights is asserted. The radius may depend on c, f_1, N, beta, k and the finitely many chosen resonant constants.

## Finite recurrence and residual

Put D=partial_t and lambda_n=(n-1)(c-1). The finite recurrence is

    (lambda_n-cD)F_n=sum_(i+j=n) [(P_i+D)G_i partial_theta F_j
                                   -partial_theta G_i (p_j+D)F_j],

with the polynomial Poisson inverse and the chosen resonant constants. These identities, including their signs, were independently derived in earlier topics. For fixed n the angular inverse has only finitely many small or zero denominators; at large Fourier frequency its denominators grow. Differentiation, multiplication and each finite polynomial inverse preserve rapid Fourier decay. Thus every F_n and G_n in this finite collection has smooth angular coefficients. This argument requires no uniform estimate as n tends to infinity.

Let {a,b}=a_t b_theta-a_theta b_t. Then

    -Delta psi_N=partial_x rho_N,
    Res_N=c partial_t rho_N-rho_N+exp(-2t){psi_N,rho_N}
         =sum_(i,j<=N, i+j>=N+1) exp(p_(i+j)t) q_ij,

where q_ij is the bracket in the recurrence. If K bounds all polynomial degrees in this finite collection, then for every fixed derivative order on t>=1,

    partial^alpha Res_N=O(exp(p_(N+1)t)t^(2K)),
    partial^alpha(exp(-2t) grad psi_N)=O(exp(-delta t)t^K),
    partial^alpha(exp(-t) grad rho_N)=O(exp(-delta t)t^K).

Here grad and partial in the cylinder calculations mean (partial_t,partial_theta), not Cartesian derivatives. Since beta>p_(N+1), the weighted residual tends to zero in every fixed cylinder Sobolev norm as the left endpoint tends to infinity.

## A weighted exterior Poisson operator

Let Z=R times S^1 and Z_T=(T,infinity) times S^1. Define ||w||_(j,beta)=||exp(-beta t)w||_(H^j(Z_T)). Fix a smooth cutoff chi_T(t)=chi_0(t-T), with chi_0 zero for t<=1 and one for t>=2. For an S1 density w, put v=exp(-beta t)w and extend chi_T v by zero from Z_T to Z. Set mu=beta+1<2 and

    h=cos(theta)(partial_t+beta)(chi_T v)
                         -sin(theta)partial_theta(chi_T v).

Equivalently h=(partial_t+mu)(cos(theta)chi_T v)-partial_theta(sin(theta)chi_T v). The parity of h is odd in both x and y, so only sin(2j theta), j>=1, occur. Define phi=exp(mu t) phi_hat through the cylinder Fourier multiplier

    phi_hat_j(xi)=h_j(xi)/[4j^2-(i xi+mu)^2].

The squared denominator equals

    ((2j-mu)^2+xi^2)((2j+mu)^2+xi^2).

The excluded beta values and mu<2 ensure that

    vartheta=inf_(j>=1) min((2j-mu)^2,(2j+mu)^2)/(4j^2)>0.

Consequently the inverse gains two cylinder derivatives, uniformly over angular modes. Since h contains one derivative of chi_T v, for every integer j>=0,

    ||phi_hat||_(H^(j+1)(Z)) <= C_j ||v||_(H^j(Z_T)).                 (1)

At j=0 the derivative is interpreted in H^(-1), which gives the same bound by Plancherel. All constants are independent of T. Multiplication by the translated cutoff and zero extension are bounded because the cutoff vanishes on a strip at the boundary.

The resulting linear operator phi=Phi_beta[w] satisfies

    -Delta phi=partial_x(chi_T w),

hence -Delta phi=partial_x w for t>T+2. It preserves reality and maps S1 density parity to the stated stream parity. It is the unique solution with exp(-mu t)phi in H^1(Z) in this parity class: a difference has modes proportional to exp((2j-mu)t) and exp((-2j-mu)t), and no nonzero such combination belongs to L2 on the whole real line.

## Correction equation and small coefficients

Set rho=rho_N+exp(beta t)v, psi=psi_N+Phi_beta[exp(beta t)v]. Define

    a=(a^t,a^theta)=exp(-2t)(psi_t,psi_theta),  kappa=1-c beta>0.

On the whole auxiliary cylinder Z_T solve

    L_a v=(c-a^theta)v_t+a^t v_theta-(kappa+beta a^theta)v=G(v),
    G(v)=-exp(-beta t)Res_N-exp(-(beta+2)t){phi,rho_N}.              (2)

The equation is imposed even in the cutoff strip. Only outside t>T+2 does it imply the physical Poisson equation together with transport.

Let eps_R=||exp(-beta t)Res_N||_(H^k(Z_T)). Let eps_N be the sum of L2 and Linfinity norms, through derivative order k+1, of exp(-2t)grad psi_N and exp(-t)grad rho_N on Z_(T-1). Both eps_R and eps_N tend to zero as T tends to infinity. Write a=a_N+a_phi. The multiplier bound (1), multiplication by exp((beta-1)t), and two-dimensional Sobolev multiplication give

    ||a_phi(v)||_(W^(1,infinity)(Z_(T-1)))
       +||grad a_phi(v)||_(H^(k-1)(Z_(T-1)))
          <= C_1 exp((beta-1)T)||v||_(H^k(Z_T)),
    ||a_phi(v)-a_phi(v')||_(L2(Z_T))
          <= C_1 exp((beta-1)T)||v-v'||_(L2(Z_T)),                 (3)
    ||G(v)||_(H^k) <= eps_R+C_2 eps_N||v||_(H^k),
    ||G(v)-G(v')||_(L2) <= C_2 eps_N||v-v'||_(L2).                 (4)

For (4), the factors in the nonlinear-looking term are first derivatives of phi_hat, bounded linearly in H^k by (1), multiplied by exp(-t)grad rho_N. Thus G is affine linear in v. The coefficient bound (3) also holds with k=3. This will be used only for the uniqueness energy estimate, not for the H^(k-1) to C1 limit argument.

## Linear transport lemma

For a C1 coefficient vector field on Z_(T-1), put

    A(a)=||a||_(W^(1,infinity))+||grad a||_(H^(k-1)).

For k>=4 and sufficiently small A(a), each G in H^k(Z_T) has a unique H^1 solution of L_a v=G, and

    ||v||_(L2)<=2||G||_(L2)/kappa,
    ||v||_(H^k)<=4||G||_(H^k)/kappa.                              (5)

Here is a proof with all boundary and approximation choices specified. For V=(c-a^theta,a^t), integration by parts on the cylinder gives

    integral f V.grad f
      =-1/2 integral_(t=T)(c-a^theta)f^2
       -1/2 integral_(Z_T)(div V)f^2.

If ||a||_infinity<=c/2 and |beta|||a||_infinity+||grad a||_infinity is small enough, then

    -integral f L_a f >= (kappa/2)||f||_2^2                       (6)

for every H1 function f. The boundary term has the helpful sign, so there is no prescribed boundary value at t=T. Density proves the identity for H1 functions from smooth functions compactly supported in the t direction. Equation (6) gives uniqueness and the first estimate in (5).

For smooth v apply (6) to every partial^alpha v, |alpha|<=k. The commutator consists of products with at least one derivative on a. Integer Sobolev multiplication on the two-dimensional cylinder yields

    ||[partial^alpha,L_a]v||_2 <= C_(k,beta) A(a)||v||_(H^k).

One can obtain this estimate without a fractional commutator theorem: put r=k-1>1, regard a differentiated coefficient as a derivative of grad a, and use the bound for products with total differentiation order at most r on H^r times H^r. On Z this follows by Fourier convolution, the inequality |eta|^b|zeta|^(r-b)<=C(<eta>^r+<zeta>^r), and the embedding of H^r Fourier transforms into L1 for r>1. A fixed half-cylinder extension gives the same estimate on Z_T. It also handles the zeroth-order beta a term. Summing (6) and absorbing C A(a)||v||_(H^k) proves the second estimate in (5).

For smooth a and smooth G supported below some T', let Phi_s denote the forward flow of V and q=kappa+beta a^theta. The coefficient bounds make the flow global forward and ensure t(Phi_s x)>=t(x)+cs/2 and q>=kappa/2. Then

    v(x)=-integral_0^infinity exp(-integral_0^s q(Phi_tau x)d tau)
                                      G(Phi_s x) ds

is smooth, zero when t>=T', and satisfies L_a v=G by differentiation along the flow. The integral is finite because G vanishes along the flow for sufficiently large s. Approximating general G in H^k proves existence for smooth a by (5).

Finally mollify a using its extension to Z_(T-1), with kernels of radius less than1. The mollified coefficients are uniformly small on Z_T and converge uniformly. Their solutions are bounded in H^k. The difference equation and (6) give an L2 Cauchy estimate, because

    ||(L_a-L_b)v||_2 <= C(1+|beta|)||a-b||_infinity ||v||_(H1).

Interpolation gives convergence in H^(k-1), hence in C1 since k>=4 in dimension2. Weak H^k compactness and this strong convergence establish the equation and the bounds. This proves the lemma. Only (6), not the higher-order part of the lemma, is needed when the comparison coefficient arises from an H3 correction.

## Fixed point, symmetry and uniqueness class

Set v^0=0. Given v^m, solve L_(a(v^m))v^(m+1)=G(v^m) by the lemma. Work within the closed S1 density subspace. This is preserved at each step, not merely after taking a limit: both reflected equations have the same coefficient and forcing transformation laws, the approximate pair has the required parity, and uniqueness in the linear lemma forces v^(m+1) to have S1 parity. Thus Phi_beta is defined on every iterate.

Put M=8 eps_R/kappa. Increase T until M<=1, the coefficient smallness hypothesis holds whenever ||v||_(H^k)<=1, 4 C_2 eps_N/kappa<=1/2, and

    (2/kappa)(C_2 eps_N+C_3 C_1 exp((beta-1)T))<=1/2,

where C_3 is chosen so ||grad v||_infinity+|beta|||v||_infinity<=C_3||v||_(H3). Equations (4) and (5) show inductively ||v^m||_(H^k)<=M. For d^(m+1)=v^(m+1)-v^m, the difference equation gives

    ||d^(m+1)||_2
       <=(2/kappa)(C_2 eps_N+C_3 C_1 exp((beta-1)T)M)||d^m||_2
       <=(1/2)||d^m||_2.

The coefficient difference is measured in L2 in this step and is multiplied by the Linfinity norm of the differentiated v^m; no infinite-volume Linfinity-to-L2 estimate is used. The iterates converge in L2, are bounded in H^k, and therefore converge in H^(k-1) and C1. Bound (1) gives convergence of the stream corrections in H^k and C2. Passing to the limit proves (2).

For uniqueness, fix N, beta, T, the cutoff and all resonant constants. If another S1 correction v' in H3(Z_T), of norm at most1, solves (2) on the ENTIRE Z_T, compare it with v using the operator L_(a(v')). Apply only (6). The right side is bounded by

    (C_2 eps_N+C_3 C_1 exp((beta-1)T))||v-v'||_2
       <=(kappa/4)||v-v'||_2.

The left side has coercivity kappa/2, so v=v'. This is auxiliary-class uniqueness. Agreement with the physical PDE only outside t>T+2 is insufficient for this comparison.

## Exterior estimates and pressure

For t>T+2 the cutoff equals1, so the Poisson and transport equations hold classically. On unit cylinder cells the embedding H^k into C^(k-2), together with the chain rule converting Cartesian derivatives into exp(-t) times cylinder derivatives, gives

    |D^m(exp(beta t)v)|<=C exp((beta-m)t),  m<=k-2.

Use (1) at level k to obtain the analogous stream estimate through m=k-1. These are uniform over all cells, since the full half-cylinder norms bound every cell norm. Thus the stated exterior remainder bounds and regularity follow.

The field u is divergence free. The one-form associated with u+(0,rho) is closed because its curl is Delta psi+partial_x rho=0. Its circulation around a circle is zero: x reflection preserves the field as a vector field and reverses the circle's orientation. The exterior annulus has one homology generator represented by such a circle, so all periods vanish and the one-form is exact. Choosing the negative primitive gives the pressure.

## Scope and dependencies

The proof depends on the already verified finite canonical recurrence, Fourier Plancherel, integer Sobolev multiplication and extension, integration by parts, smooth ordinary differential equations, and weak compactness. It is independent of all high-order numerical checkpoints and of any arithmetic small-divisor bound.

For a solution constructed at N' with a chosen beta', any strictly smaller truncation N<N' satisfies the estimate for every admissible beta at N: p_(N+1)>=p_(N')>beta', and the finite truncation difference is O(r^(p_(N+1))(log r)^K). At N=N' the argument only preserves the chosen beta' and weaker beta>=beta'. It does not improve that weight arbitrarily. The reviewed source's Remark2 still needed this restriction when this proof was recorded.

A common potential can additionally be constructed on a slightly smaller exterior by topic109, if that separate proposition is accepted. The present theorem alone does not assert potential-series convergence, one fixed-radius C-infinity solution, one solution asymptotic to every truncation, or a whole-plane canonical stationary extension.


## Noncritical construction for a critical target weight

The restriction beta not in {-3,-5,...} is a restriction on the selected inverse, rather than on the physical remainder conclusion. If a desired beta lies in (p_(N+1),p_N), including an excluded value, choose beta_tilde in (p_(N+1),beta) outside the discrete excluded set. Apply the proved theorem at beta_tilde. Increase R to exceed1 if necessary. Then r^(beta_tilde-m)<=r^(beta-m), and the same inequality with one additional power holds for the stream. Thus the physical conclusions hold at the requested beta, with a possibly larger radius. The auxiliary construction and its uniqueness are still stated at beta_tilde, not at the excluded weight beta.

At mu=-2j the conjugated mode symbol is xi(xi+4ij). For a smooth compactly supported forcing h_j with nonzero integral, its Fourier transform is continuous and nonzero at xi0. Division by this symbol behaves as a nonzero multiple of1/xi near0 and cannot be in L2. This supplies a concrete obstruction to the excluded multiplier. An arbitrary L2 or H^(-1) Fourier transform has no intrinsic point value at0; the nonzero-mean formulation must include the stated regularity or continuity assumption.
