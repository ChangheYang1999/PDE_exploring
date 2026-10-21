## 2026-10-20T20:01:38Z (lead): o51 APPLIED (AV84); applied-bytes request; L16 text repaired (AV81), waiting for your L16 paragraph; axis-residual review; AV85 to numerics

Verifier:
- o51 applied 19:59Z: fresh run of tmp/s78/o51_apply.py on 67c33e7b, cmp SAME with the confirmed preview 64e9f65b,
  then the timeline entry (text tmp/s78/app_o51.txt, 6c875c6f) and the two stamps (19:59Z). FINAL_REPORT.md md5
  5b97aebbd3e748fabbbd65d93eb182b3 (4732 lines, 60 long lines, 0 em-dashes). Backup tmp/FINAL_REPORT.bak_o51pre (=
  67c33e7b). Please check the applied bytes.
- o47 part 2: AV81 taken: "remains at the same order of magnitude", and "the smallest measured Ritz values change"
  (tmp/s78/q1_L16.txt now). I will not apply it until your own L16 paragraph arrives; then I will rewrite the R_c = 16
  sentence in the style of the R_c = 4 one (your reconstruction, 58-point maximum, x*, defect, the two near-source
  values, centre tests; collocation residual, c_l and Ritz values attributed to the numerical researcher) and send a
  fresh dry run. If your paragraph is not ready by about 21:15Z, I will send the repaired attributed version instead.
- axis-residual/PROOF.md (sha256 506c9172...): reviewed in full by hand; correct. Checked: m'/m = A/w and H'/H =
  (3w' - 3A - 2)/w (beta A = 2); Z' = (F + r_G)/(wH); parities (a odd, F even, r_G even, wH = x^(7+beta) times even), so
  the primitives have exponents 2n - 6 - beta and Z has exponents 2n - p, none zero; Z -> 0 at L since H ~ (L -
  x)^(-beta); (3); at A = 4, L = 1: S_4 = 312/31, B_3 = -(281/31) C_4, and C_A > 0 since Gamma(-2 - 1/A) < 0 <
  Gamma(-2 + 1/A), Gamma(2/A); G_* bounded and analytic at L (indicial A n + 2); with the primitive of zero finite part,
  int_x^L = -B_3 - Phi(x), so G_* = B_3 H + H Phi and H Phi is even analytic; (8) since H is homogeneous; the C^j bound
  eps^(6+beta-j); the exact weighted integral -B_3 (chi(2) - chi(1)) = B_3. No gap found. I propose a short report
  sentence (end of "Conditioning", o52, text tmp/s78/o52_text.txt); external audit fred66 launched 20:01Z.
- AV85 read; I steer the numerical researcher below.

Numerical researcher:
- The verifier's AV85 (on your section 0 draft of 19:46Z) lists items that must not enter your final section: the
  B_3 => C^(2,0.803) at P implication and "no global spectral discretization reaches 1e-6" (both refuted, see my
  19:30:32Z note); "equal floors" or "depends on the spectral grid only" (the R_c = 4 and 8 floors differ by a factor
  5.25); "true actions at most 3e-6" (no error bound; say "unresolved at this measurement floor"); finite vector
  overlaps or a 92 percent projection read as convergence or span containment; and the 70 to 95 percent range of
  resolved near-P action fractions (it omits 0.33 for the third L = 16 Ritz direction and 0.522 in the operator-channel
  audit). Please fix these before your final the numerical findings section 0.
- For the (72,30) result (chain K): same list as in my 19:30:32Z note, with the state file name and md5.

