# T2_FS1_EPS_v01: the price comparison eps of Remark FS-1 (item (iii) of T2_ROUTE1_v03 section 3.2)

Agent the second theory agent, 2026-11-04, a work session; written 2026-11-04 from about 13:40Z; frozen 2026-11-04T13:39:55Z. To the theory auditor (audit of Lemma E
requested; it is not needed for the Part VII deadline 15:35Z), the first theory agent and the coordinator. Paths are relative to the agent directory.

Status. Lemma E is CLAIMED (elementary, proof below; audit requested). Section 3 is FLOAT: binary64 arithmetic on
printed values of one grid test; it is not a bound. The note concerns only the price side of Remark FS-1 (its
hypothesis on eps). The form side (delta: the coefficient against the homogeneous model, the share of the dilated test
inside the near cut, J^q inside the form) and the step from the grid test to a test on R^2 (item (iv)) are not touched.
Every true-form statement of route (1) stays OPEN (AT2840, AT2862). Nothing here changes notes/T2_PART7_v12.md.

## 1. Setting

The setting is that of notes/T2_H4_v01.md section 2 (AT-211 at the P-S1 weight): q = 21/10, W(X) = (1 + 4|X|^2)^(1/2)
and J = <D> = (1 - Delta)^(1/2), the Fourier multiplier <xi> = (1 + |xi|^2)^(1/2). The price weight of the budget (C)
is Q(f) = ||W^(-1) J^(-q) f||^2, and the model price weight of T2_ROUTE1_v03 section 3 is int f^2/(4|X|^2). Remark FS-1
needs, at its dilate h, the hypothesis Q(h) <= (1 + eps) int h^2/(4|X|^2). The dilation is f_l(X) = l^(-1) f(X/l) on
R^2, which keeps ||f||. The norm ||.|| is that of L^2(R^2).

## 2. Lemma E

Lemma E (CLAIMED, elementary). Let f be a nonzero function in L^2(R^2) with Delta f in L^2 and
M(f)^2 := int f^2/(4|X|^2) finite. Put t(f) = (q/2) ||Delta f||/M(f). Then
    Q(f) <= (1 + t(f))^2 M(f)^2,
so the hypothesis of Remark FS-1 holds at h = f with eps = 2 t(f) + t(f)^2. Along the dilation orbit,
t(f_l) = t(f)/l.

Proof.
(a) For u >= 0 the function phi(u) = (1 + u)^(-q/2) is convex and phi(0) = 1, phi'(0) = -q/2. So
    1 - (q/2) u <= phi(u) <= 1, that is 0 <= 1 - <xi>^(-q) <= (q/2) |xi|^2 for every xi.
    By Plancherel, ||(J^(-q) - 1) f|| <= (q/2) ||Delta f||.
(b) W >= 1 and W >= 2|X| pointwise. So ||W^(-1) f|| <= M(f) and ||W^(-1) F|| <= ||F|| for every F in L^2.
(c) By the triangle inequality, ||W^(-1) J^(-q) f|| <= ||W^(-1) f|| + ||W^(-1) (J^(-q) - 1) f||
    <= M(f) + (q/2) ||Delta f||. Squaring gives the bound.
(d) Delta (f_l) = l^(-2) (Delta f)_l, so ||Delta f_l|| = l^(-2) ||Delta f||, and M(f_l) = l^(-1) M(f) by the
    dilation rule of T2_ROUTE1_v03 section 3.1. Hence t(f_l) = t(f)/l. QED.

In the notation of Remark FS-1, with h = g_(l_0), s_0 = 1/l_0 and w = w(g):
    t(h) = (q/2) s_0 (||Delta g||/||g||)/w^(1/2).
So eps tends to 0 like 1/l_0 along the orbit, and at a given dilate it is fixed by one number of the test,
||Delta g||/||g||. The lemma uses only W >= 1, W >= 2|X| and the symbol bound (a); it does not use the S1 symmetry.

## 3. Evaluation at the binding row (FLOAT)

Row: CF, plan of record, r = (A), P = (C), the windowed test of research/route1/far_cvs_s3.out (N 1024, L 64,
dx 1/8, low pass xi_c 12). For the discrete spectrum of that grid test, with m = 2.100e-06 the printed fraction of
spectral mass outside |xi| <= 12 and sqrt(2) pi/dx = 35.5431 the largest grid frequency,
||Delta g||^2/||g||^2 <= 144^2 (1 - m) + 35.5431^4 m, so ||Delta g||/||g|| <= 144.012. With c(g) 1.148676 and
w(g) 0.25422842 of the same output:

| quantity | value (upper quantities rounded up, lower ones down) |
|---|---|
| s_0, l_0 | 3.6566e-07, 2.73478e+06 |
| margin r (R - 1), per squared norm of g | 0.266255 (A) (lower) |
| price term P w s_0^2 | 0.365109 (A) |
| form value c s_0^alpha | 1.63136 (A) |
| t at the dilate | <= 0.0001097 |
| eps = 2t + t^2 | <= 0.0002194 |
| eps P w s_0^2 | <= 8.009e-05 (A), 0.0003008 of the margin |
| allowance left for delta | 0.266175 (A) (lower), 0.1631 of the form value |

So at that dilate, and for that grid test, the price comparison takes about 3e-4 of the margin. The allowance for
the form error delta stays at about 16 percent of the model form value, as with eps = 0 in T2_ROUTE1_v03 section 3.2.
At l = 1 (the grid test itself) t is about 300; the factor 1/l_0 makes it small. The value 144.012 is a property of the
discrete test; a test on R^2 needs item (iv), and its ||Delta g|| is part of that step.

## 4. Consequence for route (1)

Item (iii) of T2_ROUTE1_v03 section 3.2 is reduced to Lemma E and to ||Delta g||/||g|| of the continuous test that
item (iv) has to supply. If Lemma E is CONFIRMED, the hypothesis on eps of Remark FS-1 costs a fraction 2t + t^2 of
the price term, with t as in section 2. The obstruction at one dilate then needs a bound on delta below
r (R - 1) - eps P w s_0^2 (items (i) and (ii), J^q inside the form, and the form part of item (iv)), and the value
||Delta g||/||g|| of the continuous test. Those items stay OPEN, so the true far-form obstruction stays OPEN (AT2840,
AT2862).

## 5. Files

research/route1_eps/: eps_numbers.py (reads research/route1/far_cvs_s3.out), eps_numbers.out, eps_numbers.err (empty);
SHA256 in research/route1_eps/SHA256SUMS. Run on core 41 (nice 19, one thread, timeout 60 s; rc 0) at about 13:39Z.
