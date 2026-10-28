# Independent audit of V256 (proof proof 232, turning_height_obstruction)

Audited directory: verification/proofs/232_turning_height_obstruction/ (read only).
Audit date: Wed Oct 28 16:15 UTC 2026. Auditor: independent team. Only this file and work/audit/V256_run/ were
written. The theory author sketch's audit (xaudit_Z2_turning.md) was not consulted.

## Audited SHA256

- PROOF.md (228 lines): e9cb9c1127881c91f5c4e36beb1de113644db3c7a491da5862a55234952cec5b (rechecked at the end, unchanged)
- code/certify_turn.py: 74f177aeebdafd902b0fa4460ca6f4573c780884c624c4957872c6533873720c
- evidence/turn_certificate.json: 0c0efde05da80d130d6244ed3aad0e31ccd856359a4099f27807cd7e4cc4afd8
- evidence/check.json: ca90606965c400fd89d0d374138784dcb437fd0662af7dbc51dd4311cf31cb33
- evidence/certify.log: 1453a24facb994f333a85fe5525c353adc72bd58361b0e3d8d344f59d3166c46

Every dependency PROOF.md hash in check.json matches (topics 228, 227, 217, 88, 68, 134, 50 and the clarification
files). The code-dependency hashes in the certificate match the files on disk: 134 integrate.py 2dae7a79...,
105 check_points.py 1bce2527..., 68 global_check.py c7008385..., 15 certify.py aa3ac41f....

VERDICT: PASS WITH REMARKS

No gap was found. All three claims are proved under the stated hypotheses: the simple turn (CT3)-(CT4), T not onto
for alpha>1/2, and A0 and Lren not onto for alpha>2/3 for every beta in (2k-1,k) and gamma>4k. Finding 1 is the only
remark that matters for the 2/3 threshold. It cites a bound that proof 217 supports but does not display.

## Findings

1. NEEDS CLARIFICATION. Location: "Whole-trajectory differences", line 117 ("For M0, the divided coefficient has
   order r^(2k-3)(1+log r), with first derivatives of order r^(2k-4)(1+log r)").
   The two-orbit bound C q^2 delta (1+t) exp(ell(2k-1)t) needs the FULL gradient of m0/x^2 in the thin cone,
   including d_x(m0/x^2). Proof 217 display (6) lists only |m0/x^2|, |d_y(m0/x^2)|, |m0| and |d_x m0|.
   The displayed |d_x m0| is not enough. For the horizontal step it gives
   r^(2k-2) * q exp(ell t) delta = q delta exp(ell(2k-1)t), which is order q delta and not q^2 delta. In (16) the
   ratio to q^2 lambda^(-1/2) would then be n^((3 kappa-1)/2). That diverges for kappa>alpha/2>1/3, so the 2/3 claim
   would fail.
   The needed bound does hold. Proof 217 (5) is stated "including fixed cylinder derivatives", lines 83-84 give smooth
   division by cos^2(theta) with uniform angular derivative bounds, and line 90 gives the compact C6 region.
   Fix: write M0(Phi_t) = x_t^2 (M0/x^2)(Phi_t) and split the difference as Delta(x_t^2) M0/x^2 + x_t^2 Delta(M0/x^2).
   State |grad(m0/x^2)| <= C r^(2k-4)(1+log r) in the cone, and cite proof 217 (5) and lines 83-90 rather than (6).

2. CLARIFICATION / COSMETIC. Location: line 117, "The compact H0 obeys the corresponding finite-time bound".
   Fix: say that H0 = chi0 X.grad rho0/3 = chi0 x^2 (a1 + y a2)/3, with a C1 cofactor on supp chi0. The orbit spends
   a bounded time there, so the same split gives C q^2 delta, and the contribution is zero if supp chi0 misses the
   orbits.

3. NEEDS CLARIFICATION. Location: the stationary-phase lemma (7), line 133, and its proof, line 140.
   (a) "No other critical point" does not give uniform constants over a parameter family, because |phi'| could
   degenerate away from s_c. Fix: add the hypothesis |phi'| >= b off a fixed neighborhood of s_c. In the application
   this follows from the uniform C1 convergence (11) of X/q to Lambda and the simple critical point of Lambda in J.
   Say so after (11).
   (b) "u times a bounded piecewise C1 function" should read "u times a C1 function". This is the Hadamard quotient
   (B - B(0)chi)/u of a C2 function.

4. COSMETIC. Location: lines 21, 85 and 133. The regularity wording is inconsistent: "Global C2 punctured
   regularity" (line 21), "punctured C4 field" (line 85), and a C6 phase in (7).
   Fix: say once that V is C4 off the origin (from the C6 density), which is used for (1)-(2), and analytic on the
   span-705 annulus, which is used for (7) and (11)-(13).

5. COSMETIC. Location: line 93, "The same bounds ... hold on the fixed compact annulus ... localized proof of
   proof 228". The initial annulus has r about 9.1, so proof 228 (6), valid for R>=2, already applies directly.
   Fix: cite proof 228 (6) for R>=2.

6. COSMETIC. Location: lines 46 and 60 ("Directed512-bit and640-bit", "directed evaluation", "at both precisions").
   The computation uses arb ball (midpoint-radius) arithmetic, not directed rounding. The 640-bit pass reproduces the
   512-bit balls to all 60 printed digits with identical radii, and only trailing bits of the exact bounds differ.
   This is because Data and the Green cache are fixed inputs. The second precision is therefore a consistency check,
   not independent evidence. The center check uses a separate code path (proof 66 local_series against proof 134
   spline_eps), but it shares Data and the cache.
   Fix: reword to "ball arithmetic" and describe the 640-bit pass and the center check accurately.

7. COSMETIC. Location: certify_turn.py line 57 ('dependencies' covers I, P, G and M only). The run also executes
   proof 66 code/certify.py through G.C (local_series, horner) and proof 98 code/angular.py, which is imported by
   proof 105. Neither file is hashed.
   Fix: add 66_source_zero_exclusion/code/certify.py
   39d1efac6e391a22e837b0ba56cf0e97496f69c5b0fbf8093a8adee068339f91 and 98_exact_angular_norm/code/angular.py
   6be4e82bd1df5633605d6623686ed678240d0022cafbb9ded1a8aea66a45a319 to the record.

8. COSMETIC. Location: lines 23 and 228 (scope). The disclaimers cover degenerate turns, F0, nonexistence, infinite
   cokernel and alpha<=2/3 for the full operators. They do not explicitly cover alpha<=1/2 for T, or targets other
   than Z2 of proof 228 (unscaled E2, Y, Sobolev-type targets).
   Fix: add one sentence saying so.

9. REMARK (no fix required). a<0 is certified only on [exp L, s*), roughly [9.14660, 9.14670), since a(L)<0 and
   a_t>0 on [L,R]. That is enough, because y0<s* close to s* is all the proof needs. The analytic annulus from the
   span-705 knots is y in (9.13064, 9.14798), so s* lies only about 0.0013 below the upper knot and J must be that
   small. Stating these numbers would help a reader place y0, I and J (line 54).

## Checks confirmed (items 1-8 of the request)

- Forcing norm (9): sup C q^2; horizontal C(q^2 eps^-alpha + q^(2-alpha)) by interpolation; vertical [g]_alpha;
  local E2 term zero because J lies near y=9.15, outside B4. The bound holds for q^2 <= eps^alpha. The q_c correction
  (10) keeps the bound and vanishes on the orbits.
- Range and domain: packets are smooth and compact, so they lie in Z2 and D2. Open mapping gives preimages with
  ||h|| <= K||f|| from surjectivity of a closed operator alone; no injectivity is needed.
- (15): the identity is d/dt[e^-t h(Phi_t)] = e^-t (C[h]-f)(Phi_t), and the endpoint satisfies
  e^-t |h(Phi_t)| <= C N exp((ell beta - 1)t), which tends to 0 since beta<k.
- Stationary phase: the phase X/q is smooth, even in q, and analytic on the annulus. Lambda_s(s*)=0 and
  Lambda_ss = Lambda a_y/V2 > 0, so s* is a nondegenerate minimum. g is compactly supported in J, so there are no
  endpoint terms. The exact q-dependent phase is kept (the q^3/eps error is not discarded). The amplitude is positive
  at s_c. The envelope identity gives (12), and (14) follows with separation comparable to 1/lambda (finding 3
  aside).
- (6): from the annular term R^(2+alpha)[h]_(y,2,alpha) <= C R^beta N at R = 4 or 8.
- (4): checked term by term, namely Delta(x_t^2), Delta(a1), Delta(a2), the horizontal and vertical steps for U1/x,
  and U2. The bound is C N (q^(1+alpha)+q^2) delta^alpha exp(ell(beta+k-1)t), with exponent ell(beta-1)<0 after
  e^-t. The column exponent is 1-ell<0, and the (1+t) factor is harmless (finding 1 aside).
- (16)-(17): the arithmetic is exact. (9) needs kappa>=alpha/2. lambda=n^(1-kappa). For T the ratio is
  lambda^(1/2-alpha). For the full operators the extra ratio is n^((1+kappa)/2-alpha), which tends to 0 iff
  kappa<2alpha-1. A nonempty kappa window exists iff alpha>2/3.
- Certificate: (CT1) follows from div V = 2 ell. (CT2) has no truncation: 15 certify.py asserts out[-1]==0, and
  modes n=1..261 are complete. The series remainder |v| h^j e^(|e|h)(|e|h)^(17-j)/(17-j)! is a correct Lagrange
  bound and is exact for e=0. The enclosure covers the whole interval. a_y = a_t/y, and the y ball soundly encloses
  exp([L,R]).

## Rerun (once, single-thread, nice 19, timeout 500)

- Copy: V256_run/code/certify_turn.py. Line 9 is the only change, with TOP set to V256_run and LANE set to verifier
  read only. Wrapper: V256_run/run_audit.py. Log: V256_run/run.log.
- Output: V256_run/evidence/turn_certificate.json. No file in verifier/proofs/232 or in its dependencies was written.
- REPRODUCED. main() ran in 39.2 s, against 39.164 s in the original.
- Identical to the original JSON field by field: t_interval_exact, spline_span 705, knots_exact, every results entry
  (all exact lower and upper bounds, at 512 and 640 bits), bisection, status, the source, cache and scalar SHAs, and
  the dependency SHAs.
- Only date, elapsed_seconds and code_sha256 differ. The patched copy has code_sha256 8ee49ee9....
- Extra checks:
  - All passed:
    - all CT3 and CT4 decimals hold as exact rationals at both precisions;
    - the secant (a(R)-a(L))/(R-L) lies inside the a_t enclosure;
    - the bisection point() signs at L and R agree with the endpoint signs, via the separate local-series path;
    - k = 1615536043799051/2^53 exactly;
    - span 705 lies inside (tm, tp);
    - rho0 on the axis encloses 0 at the center.
  - At the center, the polar formula d + sum 2n(-1)^n Q_n equals 2ell - d - d' = 4.14749548e-5. This is a code
    consistency check only, since it is an identity once Q_n = r^2(4S_n+S_n').
