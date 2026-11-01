# Explicit tail bounds from a certified prefix box

Status: PROVED. Independent theory-part review of every analytic step was received at 13:48 UTC and checked as V359. V354 confirms the exact numerical examples.

## Exact hypotheses and notation

Let 0<delta=2h/Q<1, let N be a positive multiple of Q, and suppose a certified prefix majorant172 or175 with bandwidth B has a supersolution at w0>0. Write its components as (V1,...,V(Q-1),E,X1,...,XQ), and denote the retained upper bounds for E and Xr by e and b_r. The previously proved scalar domination is

    n ||f_n||_1 <= x_n,    n |H_n| <= eta_n,
    ||g_n||_1 <= L ||f_n||_1 + |H_n|.

Here H_n=0 away from resonances, all relevant angular frequencies are at most Bn, and

    sum_{k>=0} x_(N+r+kQ) w0^k <= b_r    (1<=r<=Q),
    sum_{k>=0} eta_(N+kQ) w0^k <= e.

Take any integer J>=N, any z>0 with t=z^Q/w0<1, and set

    K_r=max(0,ceil((J+1-N-r)/Q)),   m_r=N+r,
    K_E=max(0,ceil((J+1-N)/Q)),    m_E=N.

For integers d>=0 define the positive rational functions

    A_0(m,K,t)=t^K / ((m+QK)(1-t)),
    A_d(m,K,t)=(m+Q t d/dt)^(d-1) [t^K/(1-t)]   (d>=1).

Set

    D_d(z,J)=sum_{r=1}^Q b_r z^(N+r) A_d(m_r,K_r,t),
    E_d(z,J)=e z^N A_d(m_E,K_E,t).

All these quantities are finite and nonnegative. They are rational when z,w0 and the box are rational.

## Tail theorem

Write rho_tail(r,theta)=sum_{n>J} r^(1-n delta) f_n(theta) and psi_tail(r,theta)=sum_{n>J} r^(2-n delta) g_n(theta), with z=r^(-delta). For nonnegative integers a,b with d=a+b,

    r^(-1) ||(r d/dr)^a d_theta^b rho_tail||_infinity
      <= max(delta,1-delta)^a B^b D_d(z,J),

    r^(-2) ||(r d/dr)^a d_theta^b psi_tail||_infinity
      <= (2-delta)^a B^b [L D_d(z,J)+E_d(z,J)].

These inequalities also hold with the angular Wiener norm in place of the uniform norm. For every R with R^(-delta Q)<w0, their right sides evaluated at z=R^(-delta) bound the indicated weighted norms uniformly for r>=R. They apply to the already identified tuned series and do not assert convergence for an arbitrary numerical continuation.

## Complete proof

Nonnegativity of the majorant coefficients and the certified evaluations at w0 imply x_(N+r+kQ)<=b_r w0^(-k) and eta_(N+kQ)<=e w0^(-k), separately for each k. For d>=1,

    sum_{k>=K} (m+Qk)^(d-1) t^k
      = (m+Q t d/dt)^(d-1) [t^K/(1-t)].

The identity follows by differentiating a convergent geometric series finitely many times; every term is nonnegative. For d=0, 1/(m+Qk)<=1/(m+QK) for k>=K, giving A_0 as an upper bound for the corresponding negative-power sum. Multiply these estimates by b_r z^(N+r) or e z^N and sum the residue classes. This gives

    sum_{n>J} n^d ||f_n||_1 z^n <= D_d(z,J),
    sum_{n>J} n^d |H_n| z^n <= E_d(z,J).

The Poisson norm estimate gives the analogous stream bound L D_d+E_d. The exact identities (r d/dr)^a r^(1-n delta)=(1-n delta)^a r^(1-n delta) and its stream analogue supply the radial multipliers. For n>=1,

    |1-n delta| <= n max(delta,1-delta),
    |2-n delta| <= n (2-delta).

The angular support bound gives ||d_theta^b f_n||_1<=(Bn)^b ||f_n||_1, and likewise for g_n. Triangle inequalities now prove both displayed bounds. Absolute convergence of their dominating series justifies the termwise derivatives. Monotonicity in z>0 proves the uniform exterior bounds. This is the complete argument.

## Scope of the planned exact evaluations

For a box w0=2^(-q), choose z=2^(-ell) with ell=ceil(q/Q)+1. Then t=2^(q-Q ell)<1 and the physical radius is R=2^(ell Q/(2h)). Record exact rational bounds for J=N,N+Q,N+2Q and d=0,1,2,3. Independent checks of A_d against explicit polynomial numerator identities for d<=3 verify the evaluator. No fitted asymptotic constant is used. For leading amplitude epsilon, homogeneity replaces z by |epsilon|r^(-delta); thus multiply the stated physical radius by |epsilon|^(1/delta).

## Completed exact evaluations

At 2026-10-31T13:48:13+00:00, V354 confirms the arithmetic: For 22 retained profile-prefix certificates, all 264 pairs (D_d,E_d) and all 660 density/stream derivative-bound pairs replay as exact rational equalities, at J=N,N+Q,N+2Q and total derivative orders zero through three. All source and archive hashes match. Three symbolic geometric-series identities pass. Original evaluation took 6.276836392935365 seconds; independent rational replay took 0.3331221528351307 seconds. The independent analytic review remains pending; numerical agreement alone does not discharge it.

## Independent review closure

At 2026-10-31T13:52:45+00:00, V359 confirms the theory part's 13:48 UTC line-by-line review, including the support bound, residue indexing, all moment formulas, radial multipliers and amplitude scaling. The historical V354 review-pending qualification is now discharged.
