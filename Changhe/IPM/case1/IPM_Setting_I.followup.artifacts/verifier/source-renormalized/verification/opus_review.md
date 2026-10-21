# Hand review of the verifier's source-renormalized proof (PROOF.md sha256 161f766e...)

Reviewer: lead researcher, 2026-10-20T20:52:29Z. Verdict: CONFIRMED, no gap found.

Checked step by step:
- (4): from w g' = (w' - A) g, log g = log|w| - A int 1/w + const; the constants agree at 0 because v = 0 near 0, so
  eta = log(1 + v/w) - A int_0^x (1/(w+v) - 1/w). The reciprocal difference is -v/(w(w+v)) = O(e delta^(1-beta)).
  Hence |log lambda| <= C e, (5) for zeta by subtraction at L, and (6) from the exact derivative identity with
  A - w' = O(delta), w + v = -A delta (1 + O(delta) + O(e delta^(2-beta))). No v''' used; constants independent of
  the support structure.
- (7): with g_v = lambda e^zeta g, g_v' = g_v (g'/g + eta'), so Q_v = lambda^(-2) e^(-2 zeta) (G + eta'/(2 g^2))
  + lambda^(-3) e^(-3 zeta) (V - v''/(2 g^3)); and m_v = -(w+v)/g_v, so W_v/Wbar = (1 + v/w)^(beta-2) e^(-(beta-1) zeta).
  Q_v(L) = Qbar(L) since zeta = 0 and v = 0 near L.
- Leading coefficients, recomputed: v'' term -lambda^(-3) v''/(2 g_*^3) * lambda^(1-beta) A^(beta-2) g_*^(1-beta)
  delta^(beta-2) = -A^(beta-2)/(2 s^(beta+2)) v'' delta^(beta-2); eta' term with eta' ~ -v'/(A delta):
  -A^(beta-2) lambda^(-1-beta) g_*^(-1-beta) v'/(2 A delta) delta^(beta-2) = -A^(beta-2)/(2 s^(beta+2)) (s/A) v'/delta
  delta^(beta-2). Both as in (9), with s = lambda g_*. Prefactor (beta-1)A^(1-beta)/3 times -A^(beta-2)/(2 s^(beta+2)) =
  (1-beta)/(6 A s^(beta+2)), as in (10).
- Error ledger (9): leading terms are O(e/delta) in size; relative O(delta) replacements give O(e); W_v/Wbar - 1 =
  O(e delta^(2-beta)) times O(e/delta) gives O(e^2 delta^(1-beta)); zeta in the leading terms likewise; eta' errors give
  O(e) and O(e^2 delta^(1-beta)); (8) is O(delta) * O(e delta^(beta-2)) + O(e delta) * O(delta^(beta-2)) =
  O(e delta^(beta-1)). Since lambda is kept, there is no lambda - 1 times O(e/delta) term, i.e. no e^2/delta error.
  All integrable, integral O(e + e^2) independent of the support of v.
- Outside the source segment only Q(L) changes, by O(e), against W = O(x^(-beta)) at 0: integrable; the difference of
  finite parts is an ordinary integral, no constant lost.
- (11): int f'' delta^(beta-2) = (2-beta)(3-beta) J, int f' delta^(beta-3) = (3-beta) J (boundary terms vanish: v = 0
  near delta = 0, flat at d_0), so the bracket gives (3-beta)(2-beta-s/A) J and B[w+v] - B[w] = K(s) J + O(e).
- (13): int a_T dt = T + 2 int_0^1 chi. (14): log lambda = A int v/w^2 + O(int v^2/|w|^3) with v^2/|w|^3 =
  O(eps^2 delta^(3-2beta)), uniform in T; I_T - I_infinity is supported in delta <= d_0 e^(-(T+1)) where the integrand
  is O(delta^(1-beta)): O(e^(-(2-beta)T)). (16): 2 - beta - (2A-2)/A = 0, K'(g_*) = -(1-beta)(3-beta)/(6A^2
  g_*^(beta+2)). (17): eps = 1/n, T = n^2, J = n + c/n, K(s_n) = K'(g_*) A g_* I_infinity/n + O(n^(-2)); limit
  -(1-beta)(3-beta) I_infinity/(6A g_*^(beta+1)) < 0; eps = a/n gives a^2 times it.
- Norm: |d^i v| <= C |eps| delta^(3-beta-i), i <= 3, gives the C^(2,1-beta) bound C|eps| uniformly in T (amplitude
  when e - d >= d/2, mean value otherwise).
Relation to the report: the fixed-value statement of o53 follows (K(g_*) = 0 and e(v) <= C ||v||_(C^(2,1-beta)) for v
vanishing near x*, fred69's estimate). Proposed report text o55 (after the fixed-value statement), external audit fred70.
