# Binding the parameter audit to frozen source

Mandatory supplement to PROOF.md and ADDENDUM.md. The local Bernstein routine is in cert_resid.py, not cert_resid_deriv.py. The latter passes the scalar h_up; the former implements the four subintervals. The exact frozen lines below show the default K=4, the derivative caller explicitly selecting K=4, hk=succ(h_up/K), a=kk*hk, and MR(a,succ(U*a)). The independent auditor reproduces these scalar expressions exactly, including all nested RN and successor operations. It does not certify the rest of the Bernstein matrix multiplication or the derivative models.

All source hashes agree with the first checker before this extraction. The quoted line numbers are part of this source snapshot. The original PROOF.md description of checking JSON rounding cells means exact round-to-nearest-even conversion of the decimal tokens; the auditor performs that conversion, with no independent interval endpoint test of its rounding cells. This suffices because the theorem defines ahat,h as binary64 values.

Frozen research/derivative_intended_partition/sources/cert_resid.py, SHA256 1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053.

```python
356: def bernstein_sup_sub(self, tot, hpow, h_up, K=4):
357:     """sup over [0,h] of sum_N |p_N| (Wiener sum) and per-N sups, from the TM 'tot' (coefficients (S, Q+1), remainders),
358:     using K equal sub-intervals: on each, re-centre the polynomial (exact binomial shift in mid-rad arithmetic), Bernstein
359:     bound with length h/K; W_bound = max over sub-intervals of sum_N sup_sub|p_N| (+ remainders); supN = max over sub-intervals."""
360:     from math import comb as _comb
361:     Q = self.Q; S = tot.c.m.shape[0]; hk = succ(h_up / K)          # sub-interval length (upper bound: the Bernstein bound on a longer interval is valid)
362:     hkP = self.mr_powers(hk, Q)                                      # MR enclosures of hk^i for the signed transformation
363:     supN_all = np.zeros(S); W_best = 0.0; W1_best = 0.0; W2_best = 0.0
364:     twoN1 = 2.0 * np.arange(S) + 1.0
365:     for kk in range(K):
366:         a = kk * hk                                     # sub-interval start (exact multiple of hk up to rounding, covered by using hk upper bound)
367:         # re-centre: q_j = sum_{i>=j} C(i,j) c_i a^{i-j}
368:         cm = np.zeros_like(tot.c.m); cr = np.zeros_like(tot.c.r)
369:         apow = [MR.exact(1.0)]
370:         for i in range(1, Q + 1): apow.append(apow[-1] * MR(a, succ(U * a)))
371:         for j in range(Q + 1):
372:             acc = MR(np.zeros(S), np.zeros(S))
373:             for i in range(j, Q + 1):
374:                 acc = acc + tot.c[..., i] * MR.exact(float(_comb(i, j))) * apow[i - j]
375:             cm[:, j] = acc.m; cr[:, j] = acc.r
376:         ah = MR(cm, cr) * MR(hkP.m[None, :], hkP.r[None, :])
377:         b = mr_matmul(ah, MR(self.Bern.m.T, self.Bern.r.T))
378:         supN = succ(mag(b).max(-1) + tot.r)
379:         supN_all = np.maximum(supN_all, supN)
```

```python
479:     supNs = []
480:     for i in range(nder + 1):
481:         tot = eps[i]
482:         supN, Wb0, Wb1, Wb2 = self.bernstein_sup_sub(tot, hpow, h_up, K=4); supNs.append(supN)
483:         Wb = [Wb0, Wb1, Wb2]
484:         for j in range(nder + 1 - i):
```

```python
507: 
508: def cell_deriv(self, ci, nder=2):
509:     h = self.tb[ci + 1] - self.tb[ci]; h_up = h.mag()
510:     res = self.cell_core_deriv(h_up, self.e_ta[ci], [(0.0, self.T[ci])], self.A[ci], self.B[ci], self.m_ta[ci], self.wfar_ta[ci], nder)
511:     res.update(ci=ci, t_a=float(self.tb.m[ci]), h=float(h_up))
512:     return res
```

Frozen research/derivative_intended_partition/sources/cert_resid_deriv.py, SHA256 38e45bcd4400d119fb0a887794c4866bcc1d61eed1c3d69f58616eb7c95d5ac8.

```python
35:     alphas = d["alphas"]; base_m = d["base_mid"]; base_r = d["base_rad"]; nc = len(d["tau"]) - 1
36:     base_t = float(d["t0"]) if region == "outer" else float(d["tmin"]); base_r_ = float(d["t0_rad"]) if region == "outer" else float(d["tmin_rad"])
37:     ctx.prec = 128; k = arb(C.k); L = arb(C.L); rows = []; t0 = time.time()
38:     for ci in range(nc):
39:         h = tau[ci + 1] - tau[ci]; h_up = h.mag()
40:         tau_a = arb(float(d["tau"][ci]), float(d["tau_rad"][ci])); ta = arb(base_t, base_r_) + tau_a
41:         e = ta.exp(); u = e / L
42:         m_ta = MR.from_arb([u ** 3 * (1 + u * u) ** ((k - 3) / 2)])[0]; wf = MR.from_arb([(1 + u).sqrt()])[0]; e_ta = MR.from_arb([e])[0]
43:         a_terms = recentre_terms(alphas, base_m, base_r, tau_a, d["alphas_rad"] if "alphas_rad" in d.files else None)
44:         r = C.cell_core_deriv(h_up, e_ta, a_terms, A[ci], B[ci], m_ta, wf, 2)
45:         r.update(ci=ci, region=region, t_a=float(ta.mid()), r_a=float(e.mid()), h=float(h_up), nder=2); rows.append(r)
```
