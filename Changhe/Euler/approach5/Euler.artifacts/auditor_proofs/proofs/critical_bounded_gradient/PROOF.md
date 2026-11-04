# Critical exponent with a bounded gradient

## Exact statement

Let c=2/5 and omega be any finite real number. Let U in C1(R3;R3) and P in C1(R3) satisfy div U=0 and

    (1-c)U + ((cI-omega J)y+U).grad U + omega J U + grad P = 0,

where J(x,y,z)=(-y,x,0). Assume U is bounded, U(R.) tends to zero in distributions as R tends to infinity, and sup|DU| is finite. Then U=0. In particular this applies when U tends to zero at spatial infinity. The distributional dilation condition is the hypothesis Hb used in the earlier energy and pressure audits.

This uses the full Euler equation and canonical pressure. It does not follow for an independent bracket eigenfield.

## Dependencies and source check

A031 identifies the pressure gradient with the canonical Calderon-Zygmund pressure gradient under Hb. A054 gives U in L2 at c=2/5, with squared L2 tail O(R^-5). We also use the pure point concentration theorem of D. Chae and J. Wolf, *Energy concentrations and Type I blow-up for the 3D Euler equations*, arXiv:1706.02020v2, 21 May 2018, Theorem 3.1, or equivalently its consequence Corollary 1.2. The published article is in Communications in Mathematical Physics 376 (2020), 1627-1669.

The needed source statement is: a whole-space Euler solution v in L-infinity_t L2_x and L-infinity_loc([-1,0);W^{1,infinity}_x), with sup_{-1<t<0}(-t)||grad v(t)||_infinity finite, cannot have limiting energy measure E delta_0 unless v=0. No smallness of the Type I constant is assumed.

The actual v2 PDF, not its abstract, was inspected at pages 3-4 and 12-27. The pure point proof proceeds through weighted moments, an exterior pressure projection, arbitrarily fast decay of the exterior solenoidal part, a backward integral inequality, and conservation of the volume of the nonzero-vorticity set. It does not assume a particle map exists at t=0. The broader argument removing a single atom from a general limiting measure is unnecessary here.

Source URL: https://arxiv.org/pdf/1706.02020v2 . Read-only evidence: in the team records; SHA256 `6fb036499add1639bc4e03d31246d7a206529fae320cfa2eab829c9a1f5b14f0`. Source inspection date: 2026-11-02T19:35:29Z.

## Proof

For -1<t<0 put tau=-t, s=-log tau and Q_s=exp(omega s J). Define

    y=tau^{-c} Q_s^T x,
    u(x,t)=tau^{c-1} Q_s U(y),
    p(x,t)=tau^{2c-2} P(y).

Since ds/dt=tau^{-1}, differentiation gives

    partial_t u=tau^{c-2} Q_s[(1-c)U+omega J U+(cy-omega Jy).grad U],
    (u.grad)u=tau^{c-2} Q_s[(U.grad)U],
    grad_x p=tau^{c-2} Q_s grad_y P.

Thus (u,p) solves Euler and div_x u=0. Dilation and orthogonal covariance of the canonical pressure show that p is the canonical pressure of u up to a function of time.

Change of variables and differentiation give

    ||u(t)||_2^2=tau^{5c-2}||U||_2^2=||U||_2^2,
    D_xu=tau^{-1}Q_s DU(y)Q_s^T.

Consequently u belongs to the spaces in the source theorem, including on every closed time interval ending before zero, and its Type I bound is exactly ||DU||_infinity. For each continuous compactly supported test function phi,

    integral |u(x,t)|^2 phi(x) dx
      = integral |U(y)|^2 phi(tau^c Q_s y) dy
      -> ||U||_2^2 phi(0).

The convergence is dominated convergence: tau^c|Q_s y| tends to zero for every y, even if Q_s does not converge. Hence the limiting measure is ||U||_2^2 delta_0. The pure point concentration theorem forces U=0.

## Scope

This proves Theory Agent A C14 with its stated bounded-gradient hypothesis, for every omega. It does not settle the endpoint with only U tending to zero and no derivative bound. It gives no exclusion for 2/5<c<1/2: the nonzero profiles in that interval would have infinite L2 energy, and the Type I finite-energy theorem cannot be applied.

For omega nonzero the same construction is discretely self-similar with spatial factor exp(4 pi/(5|omega|)); that reformulation is not needed for the proof.

## Subsequent source-display check

At 2026-11-02T19:42:31Z, the printed page-25 gradient-pressure formula was independently corrected as documented in the team records. The correct expression is still a pure gradient, which disappears in the exterior projected energy estimate. This local display error does not alter the pure-point theorem's application above.
