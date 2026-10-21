# Actual Claude Opus 5.5 hand review

2026-10-20T20:23:13Z (lead): reviews of inexact-axis-accounting, source-exception and source-fixed-value: all CONFIRMED; o53 dry run

Verifier (AV91 received, thank you; reviewer of all three below: the lead researcher, Opus 5.5, by hand):
- inexact-axis-accounting/PROOF.md (sha256 cbfade76...): CONFIRMED, no gap. Checked m' = -A/g + r_1/g^2
  (m = -w/g, m' = (w g' - w' g)/g^2 and w g' - w' g = r_1 - A g with r_1 = w g' - (w' - A) g), g'/g = (w' - A)/w + r_1/(w g),
  H'/H = (3w' - 3A - 2)/w + (3 + beta) r_1/(w g), identity (5), both endpoint conventions, the integration by parts
  giving B_F = B_Q - D_1 with D_1 = (beta - 1)/(3 A^beta) FP int (Q - Q(L)) r_1 m^(beta-2)/g^2, and the parity
  arguments that D_1 has no finite-part constant. Not for the report: on trial data the B_3 forms are evaluated with the
  trial's g, and the report already says those values certify nothing; the identity explains the spread but adds no
  statement about P_inf.
- source-exception/PROOF.md (sha256 fce9cbbf...): CONFIRMED. Checked: (3) from (2) (log lambda_t = A t I + O(t^2),
  w_0 bounded away from 0 on supp h); B[w_t] - B[w_0] = O(t) (integrand difference O(|t| delta^(beta-1)) at L, O(|t|)
  x^(-beta) at 0); (7) from the exact eta' (rederived: eta' = [v' w_t - (w_t' - A) v]/(w_t (w_t + v))); the exact Q_new
  and W_new/Wbar identities (rederived from g_new = lambda e^zeta g_t); the leading term of (8) and the prefactor
  (beta - 1) A^(1-beta)/3 times -A^(beta-2)/(2 g^(beta+2)) = (1 - beta)/(6A g^(beta+2)); the integrations by parts
  (2 - beta)(3 - beta) and (3 - beta); int a_T dt = T + 2 int_0^1 chi. Uniformity in T: every error in (8) except the
  lambda -> 1 term is integrable in delta independently of T, and that term is eps^2 delta^(-1) on the support, giving
  eps^2 (T + 2); eta_* = O(eps) uniformly in T since the integrand is O(eps delta^(1-beta)). In particular (6) stays
  valid when eps T is large (here eps_n T_n = n), because the leading term is exactly linear in v. (9), (10):
  K'(g_*) A g_* I = -(1 - beta)(3 - beta) I/(6A g_*^(beta+1)); errors n^(-4)(n^3 + 2) = O(1/n) and n K'' t_n^2 = O(1/n).
  Norm O(1/n) from t_n h; supports disjoint since d_0 < L/4.
- source-fixed-value/PROOF.md (sha256 28a8ef62...): CONFIRMED. Checked (3) (eta(L) = 0 from (1) with v = 0 near L),
  (4), (5) with no lambda term, the vanishing of the leading integral for each v at g_* = 2A - 2 (the integral is
  finite for each compactly supported v, so a zero prefactor gives exactly 0 even though it is not uniformly bounded),
  epsilon(v) <= C ||v||_(C^(2,alpha)) from v'' (L) = 0, and the implicit-function example (partial_a F = -int h_2/w^2 < 0).
- o53 (new, for your text check; I will ask an external referee in parallel when an audit slot frees): in the 6.4 item
  "- Conditioning", the anchor "Both statements concern compatible axis data, not profiles." is replaced by the text
  tmp/s80/o53_text.txt (md5 13722cd7), which states both results and ends with "These statements concern compatible
  axis data, not profiles."; the interior bump is named f_0 (h is taken by 6.3.1 (a)) and the source layer u_n.
  Dry run: python3 tmp/s80/o53_apply.py FINAL_REPORT.md tmp/s80/fr_o53_try.md tmp/s80/o53_text.txt -> md5
  93f5d38683ced33b8acbd9a90ee63cf5 (script md5 53698545; 60 long lines, 0 em-dashes; word-level equal to the report
  with only the anchor replaced). Please CONFIRM or correct (scope, constants, the order of quantifiers in the
  fixed-value statement: d_0 fixed small, then eps_0 and C, then every v).
- The artifacts folder is assembled (150 files, 1.5 MB, sanitize log); I review it next.

