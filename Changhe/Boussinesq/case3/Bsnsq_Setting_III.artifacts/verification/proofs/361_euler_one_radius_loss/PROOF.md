# The Euler inverse loses one analytic radius factor after two derivatives

Prepared 2026-10-22T12:09:26.948946+00:00, before finite controls. This refines the nonsharp radius-loss estimate of P355. It concerns arbitrary scalar forcing, not convergence of the B2 formal hierarchy.

## Statement

Let rho>0, 0<r<rho, m a nonnegative integer, and A_rho the power series f(z)=sum f_j z^j with norm sum |f_j|rho^j. Define D=d/dz and S_m f=sum_(j!=m) f_j z^j/(j-m), removing the resonant coefficient. Then the coefficientwise operator S_m D^2 extends from polynomials to a bounded operator A_rho to A_r, with

    ||S_m D^2 f||_r <= [1/(rho(rho-r)) + (m+2)^2/rho^2] ||f||_rho.

For each fixed m, the order (rho-r)^(-1) as r increases to rho cannot be replaced by o((rho-r)^(-1)) uniformly over the unit ball, even restricting to polynomial f whose D^2 f has zero coefficient at resonance m. Specifically, for any integer j>=max(2,m+3), set r_j=rho(1-1/j), f^(j)=rho^(-j)z^j. Then

    ||S_m D^2 f^(j)||_(r_j) >= (j-1)/(3rho^2)
      = (1-1/j)/(3rho(rho-r_j)).

Both statements concern scalar sequences, not the nonlinear B2 forcing. The first constant is an upper bound, not the exact norm.

## Proof

Put q=r/rho. A monomial of degree j>=2, except j=m+2 which is removed, has output/input norm ratio

    rho^(-2) j(j-1) q^(j-2) / |j-m-2|.

For 2<=j<=m+1, this is at most rho^(-2)m(m+1), hence at most the claimed bound. For j>=m+3, divide the quadratic exactly:

    j(j-1)/(j-m-2) = j+m+1+(m+1)(m+2)/(j-m-2)
                    <= j+(m+1)(m+3).

Writing n=j-2>=1, the n-th binomial distribution term gives n(1-q)q^(n-1)<=1. Therefore n q^n<=q/(1-q) and

    j q^(j-2) <= 2+q/(1-q) = 1+1/(1-q).

Since q^(j-2)<=1, the normalized ratio is at most

    rho^(-2)[1/(1-q)+1+(m+1)(m+3)]
      = rho^(-2)[1/(1-q)+(m+2)^2].

The constant and linear monomials have zero output. Summing the coefficient bounds against |f_j|rho^j proves the inequality; absolute convergence also defines the extension and proves its agreement with the coefficientwise series.

For the lower bound, j-m-2 is positive and at most j, so the rational factor is at least j-1. Moreover

    log(1-1/j) = -integral_0^(1/j) dt/(1-t) >= -1/(j-1).

Consequently (1-1/j)^(j-2)>=exp(-(j-2)/(j-1))>exp(-1)>1/3. The last inequality follows from e=sum 1/k!<3, for example k!>=2^(k-1) for k>=1 with strict inequality for k>=3. This gives the stated lower bound. The input norm is exactly1, and the resonance coefficient of D^2 f^(j) vanishes because j-2>m. As j tends to infinity, r_j tends to rho and the displayed lower bound disproves any uniform smaller-order radius singularity.

## Scope and dependencies

P355 supplies the B2 axis-operator conjugation, whose fixed analytic coordinate and nonvanishing multiplier require their own domain and multiplier norms. This proof needs only its scalar definitions. It shows that the scalar inverse reduces the naive two-derivative radius loss to one. It gives neither bounds on the hierarchy's resonant homogeneous constants nor a majorant estimate in the transverse index. It therefore proves no convergence, divergence, local actual solution, full-plane inverse, attachment to the marked center, or B2 endpoint. General B2 remains OPEN.

Finite exact rational checks below are controls of the inequalities and resonant projection, not the infinite-index proof. All writes are inside verification. No JavaScript/TypeScript or Node, servers/listeners/tunnels, RLScience cluster, Lean/Lake builds, commits/pushes, posting or human contact. One low-priority single-thread heavy CPU process at a time.
