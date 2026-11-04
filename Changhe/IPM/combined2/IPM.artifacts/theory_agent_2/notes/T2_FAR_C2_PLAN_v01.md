# T2_FAR_C2_PLAN_v01: priced plan for row C2 (a certified A_low^+(8 pi) <= Gbar - S^+), for X7 (the coordinator 20:11Z item 4)

Agent the second theory agent. Written from 2026-11-03T20:21Z; file created 2026-11-03T20:29Z. Status labels: Lemma QID and Proposition ZO are
CLAIMED here (short proofs below, for the theory auditor); every cost is HEURISTIC; every band value is FLOAT (the second numerics agent) and is not a bound.

## 0. Answer

No route that the team can complete before the stop (2026-11-04T17:05:30Z) gives a certified A_low^+(8 pi) <=
Gbar - S^+. The blocker is the size of the certified eigenproblem, not the room: the tail beyond the window radius
Rw must be paid separately (certified OMF(a_t) <= 0.11404 at Rw 200, Ww 200), so the matrix must represent the band
form on a support of radius at least Rw, which needs order 1.6e6 or more in the parity class (Landau-Pollak, as in
the second numerics agent results/N2_BAND_PRICE_013_v02.md section 3.2), against a capacity of about 5e4 for a dense certificate in
32 GB on one core. Proposition ZO (section 2) shows that no general lemma can charge a slowly varying part of the
coefficient through its derivatives alone: its band constant is of zeroth order. The only route whose dimension fits
the capacity is a phase-space split (section 3, route P), and it needs two analytic estimates that nobody has
written; priced, it does not fit in the remaining time (about 20.5 h at 20:35Z). Recommendation (section 4):
record C2 as OPEN with this obstruction, keep Proposition F conditional on C2, and do not start code for C2.
Nothing in this note changes Theorem CS-B or the comparison SC^+ + S^+ <= Gbar.

## 1. Target and budget

- Proposition F (F3), second half, with the CS-B value S^+ = 0.059699233948103884 (CLAIMED, under the theory auditor review):
  A_low^+(8 pi) <= Gbar - S^+ = 426560137443922093/720575940379279360 > 0.591971.
- FLOAT band value of the far piece at erflog 8, rho 1, K' = 8 pi: 0.3848 (the second numerics agent; box and window move it by about
  2e-4). Room above it: 0.2072 (it was 0.244 with the FLOAT S_h^B 0.0227 used in the second numerics agent's pricing).
- Window split. A_low(K'; a) is the supremum of a form linear in a, so for a_f = a_W + a_t,
  A_low(K'; a_f) <= A_low(K'; a_W) + A_low(K'; a_t), and A_low(K'; a_t) <= A_*(a_t) <= OMF(a_t) (the step used in
  route F-a). With the certified OMF(a_t) <= 0.11404 at Rw 200, Ww 200 (AT1336 to AT1342) it suffices that the matrix part
  gives A_low^+(8 pi; a_W) <= 0.477931 (a lower rounding of Gbar - S^+ - 0.11404), at most 24 percent above the FLOAT
  value 0.3848, for a_W supported in |x| <= Rw + Ww = 400. No smaller certified tail charge exists; the FLOAT absolute
  charges are 0.29 at Rw 50 and about 0.21 at Rw 100 (the second numerics agent v02 section 3.1); at Rw 100 the charge alone already exceeds
  the room 0.2072, so a window beyond Rw 100 is forced, and Rw 200 is the first with a certified charge.

## 2. Two facts about the band form

Write S for the double integral normalized by Parseval, S[a^(xi - eta)](u) = int a u^2 dx, so that
S[k](u) = (2 pi)^-4 int int k(xi, eta) u^(eta) conj(u^(xi)) d xi d eta. With u = J^-1 f, A_low(K') is the supremum of
S[-(1/2) a^ Ktil](u)/||u||^2 over real nonzero u in L^2 of the test parity with u^ supported in |xi| <= K'
(T2_FAR_v02 section 2.3). Lambda^s is the multiplier <xi>^s and R_j the Riesz transform with symbol -i xi_j/|xi|.

Lemma QID (CLAIMED). Let a be real and bounded with a^ in L^1, and let u be real in L^2 with u^ supported in a
bounded set. Then
    S[-(1/2) a^ Ktil](u) = int a rho_u dx,  rho_u = sum_(j=1,2) (Lambda R_j u)^2 - (Lambda^(1+q) u)(Lambda^(1-q) u),
and int rho_u dx = 0.
Proof. All functions Lambda^s u and Lambda R_j u are real (even real symbols, odd imaginary symbols) and band-limited,
so they lie in L^2 with integrable Fourier transforms, and the Parseval form of int a g h dx with a^ in L^1 converges
absolutely. For multipliers p, p' the form int a (P u)(P' u) dx has kernel a^(xi - eta) p(eta) conj(p'(xi)). Hence the
right side has kernel a^(xi - eta) [<xi><eta> w.w' - (1/2)(<xi>^(1+q) <eta>^(1-q) + <xi>^(1-q) <eta>^(1+q))], with
w = xi/|xi|, w' = eta/|eta| (the two orders of the factors of the cross term give the same form, so its kernel may
be averaged). Expanding
    Ktil = <xi><eta> |w - w'|^2 + (<xi>^q - <eta>^q)^2 (<xi><eta>)^(1-q)
         = 2 <xi><eta> - 2 <xi><eta> w.w' + <xi>^(1+q) <eta>^(1-q) + <xi>^(1-q) <eta>^(1+q) - 2 <xi><eta>
shows that -(1/2) Ktil equals the bracket. Finally int rho_u = sum_j ||Lambda R_j u||^2 - ||Lambda u||^2 = 0, since
sum_j xi_j^2/|xi|^2 = 1 and <xi>^(1+q) <xi>^(1-q) = <xi>^2. QED.
FLOAT check (not a proof): research/h4/far009/code/c1/qid_check.py compares both sides on the torus for random
real a and u with modes |k| <= 6 (64^2 grid): relative difference 1.2e-15 (runs/qid_check_2032.log).
So the band form is int (a - c) rho_u for every constant c, and its value on a test concentrated at frequencies
|xi| << 1 is close to int a rho^0_u with rho^0_u = sum_j (R_j u)^2 - u^2 (zeroth order, scale invariant).

Proposition ZO (CLAIMED). Let K' > 0. For every real Schwartz function b and every real nonzero u of the test parity
with u^ supported in |xi| <= 1,
    liminf_(eps -> 0+) A_low(K'; b(eps .)) >= Z(b, u) := int b rho^0_u dy/||u||^2,
and there are such b (radial, b >= 0) and u (even in x_1, odd in x_2) with Z(b, u) > 0. Meanwhile
SC(b(eps .)) = eps^2 SC(b) and D_s(b(eps .)) = int |(b(eps .))^| |zeta|^s d zeta = eps^s D_s(b) tend to 0 for every
s > 0. For every real bounded b and every u, int b rho^0_u <= osc(b) ||u||^2.
Proof. (i) Take w radial with w^ >= 0 smooth, nonzero, supported in |xi| <= 1, and u = d_2 w (even in x_1, odd in x_2,
the parity class of the second numerics agent v02 section 3.2; band-limited to the unit disk; for another parity class, any u with
rho^0_u not identically 0 works, since int rho^0_u = 0 gives a point where rho^0_u > 0 and b can be centred there).
Then u(0) = 0, R_1 u(0) = 0 by symmetry, and R_2 u(0) = (2 pi)^-2 int w^(xi) xi_2^2/|xi| d xi > 0, so
rho^0_u(0) > 0, hence rho^0_u > 0 on a disk |y| < delta (continuity). For
b(y) = exp(-|y|^2/sigma^2) with sigma small, int b rho^0_u > 0 (it is pi sigma^2 (rho^0_u(0) + o(1))).
(ii) For 0 < eps <= K' put u_eps(x) = u(eps x); its Fourier support lies in |xi| <= eps <= K' and it has the same
parity. Dilation commutes with R_j, and Lambda^s u_eps = (M_eps^s u)(eps .) with M_eps^s the multiplier <eps zeta>^s.
By Lemma QID and the substitution y = eps x, the quotient for b(eps .) at u_eps is
int b [sum_j (M_eps R_j u)^2 - (M_eps^(1+q) u)(M_eps^(1-q) u)] dy/||u||^2. On |zeta| <= 1, |<eps zeta>^s - 1| <= C_s eps^2,
so each M_eps factor converges to the identity in L^2 on the band, the products converge in L^1, and b is bounded:
the quotient tends to Z(b, u). (iii) a^ of b(eps .) is eps^-2 b^(zeta/eps), which gives the scaling of D_s; SC scales by
the second derivatives. (iv) int b rho^0_u <= sup b sum_j ||R_j u||^2 - inf b ||u||^2 = osc(b) ||u||^2. QED.
Consequence. No bound of the band constant by SC and the moments D_s (s > 0) alone, vanishing with them, can hold:
a slowly varying part of the coefficient is charged at zeroth order, between Z-type constants and osc. This is the
precise form of the obstacle noted by the second numerics agent (v02 sections 2 and 3.1) for a lemma that would charge the tail a_t only
through its derivatives. It does not exclude a sign-aware treatment of the tail jointly with the window region.
Relation to earlier results: the theory auditor showed (AT459 to AT465, exchange v165 and v166) that the form without a frequency
restriction is invariant under a common dilation, so positive-order moment and derivative budgets cannot lower the
unrestricted constant. Proposition ZO is the corresponding statement for the low band |xi| <= K', where the form is
not dilation invariant (the weights <xi>^s) and only its zeroth-order limit survives.

## 3. Routes and prices

Capacity (HEURISTIC): a dense certified test U I - M >= 0 by a floating-point Cholesky with an a priori shift for the
rounding error (the criterion of S. M. Rump, BIT 46 (2006)) costs n^3/3 flops and 8 n^2 bytes: n = 5e4 needs 20 GB and
about 1 h at 1e10 flop/s on one core; n = 6.5e4 reaches the 32 GB limit. In arb, about 1e4 (the second numerics agent). Matrix-vector
methods alone give no certified upper (the second numerics agent v02 section 3.3). Parity-class counts n = K'^2 Rs^2/16 (support radius
Rs, disk band of radius K'): at K' = 8 pi, 1.6e6 (Rs 200) and 6.3e6 (Rs 400); at K' = 4 pi, 3.9e5 and 1.6e6.

| route | what is certified | order n | theory to write | code | core time | review | fits before the stop |
|---|---|---|---|---|---|---|---|
| W (window + OMF, lattice) | A_low(a_W) <= 0.477931 by a dense certificate plus a lattice projection error | 6.3e6 (Rs 400) | projection error with constant cells (AT-753 type) | 8 to 12 h (the second numerics agent) | dense: about 3e2 TB, about 1e5 days | The theory auditor: projection lemma; the numerical auditor: entries | no (memory and time) |
| W' (smaller window) | as W, Rw 100 | 3.9e5 to 1.6e6 | as W, and a tail charge <= 0.207 - error at Rw 100 (FLOAT 0.21: none) | as W | about 20 to 2e3 days | as W | no (no tail charge fits) |
| K (lower K' to 4 pi) | as W at K' = 4 pi | 1.6e6 (Rs 400) | new CS-B run at (pi, 4 pi): S^+ grows (FLOAT trend 0.416 to 0.844 at log 8, the second numerics agent v02 3.5) | 1 h (the second theory agent) | 1 to 2 h for CS-B; dense as W | The theory auditor: CS-B rerun | no (n) |
| B (block certificate on a computed subspace) | PMP <= alpha, QMQ <= beta, norm QMP <= delta | subspace small | an upper beta for the complement below the budget: only absolute-kernel bounds exist, all above it (the second numerics agent v02 section 2); subtracting a signed principal part first is unexplored | - | - | - | no (beta missing) |
| P (phase-space split) | a_t by OMF as in W; for a_W, an eigenproblem on low frequencies over its whole support plus all band frequencies over a core disk, and the rest (frequencies in [k0, K'] outside the core) by derivative bounds of the outer part a_o of a_W | about 1e4 + 3.6e4 (|xi| <= 1 over Rs 400; K' = 8 pi over Rs 30) | (P1) a bound of the form of a_o on tests with frequencies in [k0, K'] by derivative norms of a_o; (P2) coupling bounds for the phase-space cutoffs with explicit constants | 10 to 16 h (new basis and entries) | 5 to 10 h | The theory auditor: P1, P2 and the basis lemma; the numerical auditor: entries and Cholesky | no (theory 12 to 24 h + review 6 to 12 h + code, against about 20.5 h) |

Notes on route P (the only one with a fitting order). (i) Proposition ZO does not exclude P1: P1 concerns a fixed
k0 > 0 with k0 R_core >> 1 (R_core the core radius), while the dilation argument of ZO uses frequencies tending to
0. An angular mode of order m of a_f has local frequency about m/r at radius r, so R_core must also be large
compared with the highest mode order of a_f divided by k0 (HEURISTIC). An estimate of the type
|Ktil - P| <= (A2 |zeta|^2 + A4 |zeta|^4)/|xi|^2 on |zeta| <= |xi|/2, proved in Lemma KT region R1 for |xi| >= 64
with explicit A2, A4 (code/c1/k_tail.py; other constants are needed at smaller |xi|), suggests a charge of order
SC(a_o) + D_2(a_o)/k0^2 (HEURISTIC). (ii) P2 is the open difficulty: the phase-space cutoffs
(a spatial cutoff at the core radius composed with a frequency ramp at k0) do not commute with the form, and their
commutators must be bounded with explicit constants; where the coupling passes through a_f near the core, Ktil - P is
not small relative to P at |xi| of order k0 (it grows like |zeta|^2/|xi|^2 as |xi| decreases; T2_FAR_v02 section 2.3
Remark 1 and the origin rows of route (a) in section 2.5), so an absolute bound there is not expected to fit the room
(HEURISTIC, not computed).
(iii) Before any code, route P would need a FLOAT test of its premise: the FLOAT band value of a_W on the complement
space (frequencies in [k0, 8 pi], support outside the core disk) must be far below the room. The second numerics agent's band code could give it
in 1 to 3 h on one core (FLOAT, not a bound).

## 4. Recommendation for X7

1. Record C2 as OPEN with the obstruction "certified tail charge 0.11404 at Rw 200 forces a band eigenproblem of
   parity order at least 1.6e6 (6.3e6 with the window width), against a dense certificate capacity of about 5e4;
   Proposition ZO excludes a derivative-only tail charge". Proposition F stays conditional on C2.
2. No C2 code before the stop. If X7 wants one informative step, the FLOAT test of route P item (iii) (the second numerics agent, 1 to
   3 h, one core) is the cheapest; it cannot produce a certificate before the stop.
3. The second theory agent keeps CS-B under review (the rounding correction of notes 20:19Z; the theory auditor's open questions) and can write
   Lemma QID and Proposition ZO into a theory note for the first theory agent if the theory auditor confirms them.

## 5. Files

- research/h4/far009/code/c1/qid_check.py (SHA256 53d1c030f1086eb3cd738c17d63ac32c2281c7575fb2955a490ff9954051112f),
  runs/qid_check_2032.log (b296624df78ff1aea37beb2dc87f70e072c9732b13079bf267b0ef05394a7439); run 20:32:04Z on one
  core, holding the req48 row 3 job as in T2_FAR_CS_v02 item 6.
- Inputs quoted: notes/T2_FAR_CS_v02.md (S^+), RESTART.md section 5 (OMF(a_t) at Rw 200, Ww 200), the second numerics agent
  results/N2_BAND_PRICE_013_v02.md (FLOAT band values, tail charges, Landau-Pollak counts, certification routes).
