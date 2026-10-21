## 2026-10-20T17:37:07Z (lead): REVIEW of r12-global-sign (md5 e5089a73): CORRECT; independent checks; report plan (o42)

Verifier: I reviewed verifier/r12-global-sign/PROOF.md and checked it with my own code, tmp/s65/r12_check.py and
tmp/s65/fp_check.py (sympy and mpmath, written from the definitions in your Statement, not from your check code):
- G_3 = 10 A u^2/((8A - 1)(1 + u^2)^3) solves w G_3' + (3h - 1) G_3 = F_3 identically in (x, A) (symbolic residual 0);
- F_5 from the hierarchy equals u^2 (c_0 + c_2 u^2 + c_4 u^4)/(15 (4A - 3)(8A - 1)(1 + u^2)^6) with your c_0, c_2, c_4
  (residual 0); H_5'/H_5 = (1 - 5h)/w (residual 0); F_5/(w H_5) dx is exactly the integrand of your (2) (ratio 1);
- (3) equals the sum of the three continued Beta terms of (2) at A = 1.25, 1.5, 3, 5, 10.150725214760579, 40 (all digits);
  identity (4) agrees with mpmath's continued Beta to 1e-38 or better at the same points; the finite part computed
  directly (remainder series on [0, 1/4], quadrature on [1/4, 1]) equals the continued Beta at a + j, j = 0, 1, 2, at
  the computed A to 3e-14 relative (quadrature limited by the (1 - t)^(q - 1) endpoint);
- P(1 + v) = 1248 v^4 + 4444 v^3 + 6141 v^2 + 3764 v + 903; the z -> 1 value of (4) is -1/20;
- B_5 in natural units at A = 10.150725214760579: -7.68940786090505e-5 (your -7.689408135610e-5 is at A = 10.150725;
  the report prints -7.6894e-5).
The sign argument (all gamma arguments positive for 0 < z < 2, (2 - z)(3 - z)(4 - z) > 0, the minus sign from
(z - 1) Gamma(1 - z) = -Gamma(2 - z) together with the product of z - 2, z - 3, z - 4) is right, and the domain check
(a = -4 - 2/A in (-6, -4), integer only at A = 2; a + q = -4 + 2/A in (-4, -2)) is right. Verdict: CORRECT as stated,
with the scope you give (prescribed axis data; l_5 can cancel B_5 for profiles).
Report plan (package o42, after an external audit, which I will send as soon as a slot frees; fred53/fred54 are
running): extend the 6.5 item (now "The same closed form holds for 2 < A < 4 ... B_5 < 0 on (1, 4) without A = 2") to
every A > 1, A != 2, with your representation (4); state the consequence for A >= 4 with the exponent condition of
(h), Higher odd orders (C^(4,alpha) near P with alpha > 1 - 4/A) and the summable alternative (p_5 = 10 + 4/A in
(10, 11], not an even integer); replace "computed B_5 ... numerical evidence" in 6.3.2 (a) and 6.4 (o40 tags a2, 48)
by the exact sign; update status line 57 ("For 1 < c_l < 3/2") accordingly. Please record an AV entry for this proof
if you have not; the report will cite your verification and the audit.
Also read: finite-source-family (md5 c3c14527, review in my next shift) and your 96 fixed-c_l audit (0.00471, 0.00439,
0.00445, 0.00310). Note for the report: Q1 (iv) currently says the fixed-c_l states have |R|/N_f between 0.0025 and
0.0046; your +0.001 value 0.00471 at 96 x 40 is above that range, so when the 96 values enter (with an AV entry) the
sentence will give the two grids separately.

