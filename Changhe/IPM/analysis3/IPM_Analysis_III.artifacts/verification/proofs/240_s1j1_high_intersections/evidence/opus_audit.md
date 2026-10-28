# Independent audit of proof 240 (S1J1 high input and graph intersections)

Target: verification/proofs/240_s1j1_high_intersections/PROOF.md

- SHA256 at start (sha256sum): 263f44553ac31002cda4177e4a91a6122293757ef76a43a106baea81f1723af6
- SHA256 at end (sha256sum):   263f44553ac31002cda4177e4a91a6122293757ef76a43a106baea81f1723af6
- date -u at start: Wed Oct 28 16:37:47 UTC 2026
- date -u at end:   Wed Oct 28 16:47:13 UTC 2026

The hash matches the requested value, evidence/check.json, and RESULTS.md. All 13 dependency hashes recorded in
check.json match the current files: 198 code, 04 code, 206 PROOF, 206 AUDIT_CLARIFICATIONS, 206 check.json,
235 PROOF, 235 AUDIT_CLARIFICATIONS, 239 PROOF, 239 check.json, 239 exact_inputs.json, 173, 174 and 126. The
export exact_constraints.json (96f271d7...) and code/check.py (f3b32911...) match their recorded hashes.
evidence/run.log is byte-identical to check.json.

Read for this audit:
- PROOF.md, RESULTS.md, code/check.py (read only, not executed), evidence/check.json, evidence/exact_constraints.json;
- proof 235 PROOF.md and AUDIT_CLARIFICATIONS.md (the template);
- proof 239 PROOF.md and RESULTS.md, and the 239 exact_inputs.json export;
- proof 206 PROOF.md, AUDIT_CLARIFICATIONS.md and the V210 audit inside its evidence;
- proof 173 statement and section 2; the definitions of A0 in proof 174, including line 121 (rho0=x^2 y+O(r^5));
- proof 126 statement (hypothesis 1, W^(7,inf) coefficients); proof 76 lines 80-100 (d(t)>=5.5752 for all real t);
- proof 123 estimate (9) and the following trace argument; the m0 membership in proof 167;
- the theory-theory author audit xaudit_V235.md, for style.

## VERDICT: PASS WITH REMARKS

Summary. I found no gap and no false load-bearing statement. Both equivalences (1) and (2) are correct, and so are
the dimensions 32 and 29. The analytic argument is the proof 206/235 jump criterion, applied at three separated joins.
The angular structure is the same as in 235: h=r^3 p F B with F=1+cos(2 theta)=2cos(theta)^2. This is also the m=1
mode F_1 of proof 206.

The two places where 240 goes beyond 206/235 are both handled correctly:
- the inner exponential extensions reach the origin;
- the inner and outer joins are combined in one span.

Both rely on facts in cited or recorded dependencies (topics126, 76, 123, 167, 174), but some of these are not named
in the text. My own exact rational reconstruction gives exactly the exported matrices, the ranks 6 and 9, and all
nullspace identities. The findings are remarks only.

## Findings

1. REMARK (minor misstatement, argument unaffected). PROOF.md line 48: "On a smaller open vertical sector the
   factor 2 cos(theta)^2 is nonzero." Read literally this is inaccurate. A sector about the vertical axis contains
   theta=pi/2 (and 3pi/2), and there the factor vanishes quadratically. The jump criterion needs only an open
   angular interval where the factor does not vanish identically, inside the region where chi=1. Proof 206 line 40
   and the 235 clarification use exactly this: pairing with an angular test function, on a sector "away from the
   axis". The same applies to "the nonzero angular factor" in line 58. Lines 56 and 62 are fine as written: q itself
   is nonzero on the axis.
   Proposed fix: replace the sentence with "On an open angular interval inside the vertical sector where chi=1,
   but away from the axis itself, the factor 2 cos(theta)^2 is nonzero."

2. REMARK (citation for the transport speed at all three joins). PROOF.md line 56. The question was whether q is
   nonzero at t_minus and t_plus, not only at t_J. It is. Proof 76 line 86 states d(t)>=5.5752 for ALL real t. That
   bound is for the exactly joined, exactly normalized background (proof 100 line 5 identifies the proof 76
   background in these words). By continuity of q (it is W^(7,inf) by proof 126), q is nonzero on a neighborhood of
   the axis at each of t_minus, t_plus and t_J. Proof 206 used the same fact at t_minus and t_plus.
   The proof only says "the previously certified coefficient". Proof 76 is not listed in check.json.
   Proposed fix: write "d(t)>=5.5752 for all real t (proof 76, from proof 68), in particular at t_minus, t_plus and
   t_J", and add proof 76 to the dependency list.

3. REMARK (coefficient regularity and uniform end bounds should cite proof 126). PROOF.md lines 62 and 66, and the
   end of line 44.
   - The local facts are those of the 206 clarification: Q in W^(6,inf), and all other coefficients W^(7,inf).
     Proof 126's verification of its hypothesis 1 gives q, vartheta and the divided coefficients as C6 with bounded
     piecewise seventh derivative. Then Q=integral_0^1 d_t q(t0+tau(t-t0)) dtau is W^(6,inf).
   - Line 66 says "The strict inner and outer powers are unchanged by cylinder transport", and line 44 says "all
     orders needed in the transport image are finite at the inner end". Both need uniform W^(7,inf) cylinder bounds
     on the coefficients as t->-inf and t->+inf. Proof 126 supplies these ("the normalized origin and infinity
     expansions give uniform cylinder bounds").
   - This use is new compared with 206 and 235: there the inputs vanish near the origin. Here columns 0..6 equal
     2r^3 cos^4 sin times exponential sums all the way to r=0.
   - The step is correct. Proof 126 is a recorded dependency in check.json but is not named in PROOF.md.
   Proposed fix: cite proof 126 at lines 62 and 66 for the local W^(7,inf) regularity and for the uniform cylinder
   bounds at both ends.

4. REMARK (no-cancellation step: name the bounded coupling and the property of Y_H used). PROOF.md lines 64 and 66.
   "The bounded high realization proves this" carries the load. The precise sources are:
   - proof 123 estimate (9) and the trace identity after it: for h in X_s, C_ren h is the sum of E Gamma_C and an
     element of X_s;
   - proof 167: m0 is in Y_H.

   Here h in S cap H_full lies in X_s, because its scalar coordinate is zero (line 42 is correct). The step
   "addition of the high-target coupling cannot repair" also uses the following fact. Every element of Y_H has a
   vertical-sector cofactor in H^sigma: for E Gamma_H the cofactor is gamma/a_H, which is in H^sigma, and for X_s
   this holds by definition. So A0h in Y_H would force the transport cofactor into H^sigma on the sector.

   I rechecked the direct end bounds of line 64. They are correct but only supplementary:
   - Near the origin, U[h]=c[h](-x,y)+O(r^3). Parity and zero divergence exclude other linear terms and all
     quadratic terms.
   - With rho0=x^2 y+O(r^5) (proof 174 line 121), U[h].grad rho0=-c[h]x^2 y+O(r^5) and c[h]H0=c[h]x^2 y+O(r^5).
     The sum is O(r^5), which is O(r^(1/5)) after division by b_H.
   - At infinity, 3k-3/2<0 and 2k-1/2<0.
   - "Sublinear" is loose wording: the tails are decaying powers r^a with a<=2k-1. The bound U[h]=O(r^(2k-1)) is
     the kernel estimate for -2<beta<1 (proof 222 (4)).

   Proposed fix: cite proof 123 (9) and proof 167, and add the one-line Y_H cofactor property.

5. REMARK (implicit but correct: trace and distributional derivative). PROOF.md lines 58 and 66.
   - The proof does not state that the transport image has zero vertical cofactor trace. It does: in the cofactor
     formula (proof 206 (3)), F=2cos^2(theta) and F'=-2 sin(2 theta) both vanish at the axis, and (p'/p)vartheta is
     regular by axis tangency.
   - Nor does the proof state that distributional derivatives have no surface terms. This holds because every
     column is at least C3 at every join (proof 239 line 28).

   Neither omission matters, but both are used in "A0h belongs to Y_H distributionally". Proposed fix: add one
   sentence citing 206 (3) and 239.

6. REMARK (wording near the origin). PROOF.md line 44.
   - "h_i is a finite polynomial combination of x^4 y (x^2+y^2)^(j-1), supported by the fixed inner region" is
     loose. The polynomial formula holds on the disk r<exp(t_minus). For i=0..3 the column continues as a spline
     beyond it, and for i>=7 it is zero there.
   - The exponent r^(5-24/5) uses b_H=exp(24t/5), which holds only far left. In the transition region b_H is a
     smooth positive interpolation, so the end exponent is a statement as t->-inf.
   - Both points are harmless. I checked the content: exponents e_j=2j>=2 give physical order 2j+3>=5, J=0 and
     cofactor 2cos^2(theta) times the radial factor, hence zero trace.

   Proposed fix: say "on the disk r<exp(t_minus)" and "as t->-infinity".

7. REMARK (rank argument could be stated more directly). PROOF.md lines 70-74. The triangular-minor argument is
   correct. My reconstruction shows something stronger: the order-4..6 jump rows are supported on pairwise disjoint
   column sets, namely minus {0,...,9}, plus {30,31,32} and outer {33,...,37}. The matrix is therefore
   block-diagonal after a column permutation, and its rank is the sum of the block ranks (2+2+2 and 3+3+3). Each
   block has the stated triangular or Vandermonde minor. Column 29 (b_26) and column 10 (b_7) drop out because they
   vanish to order 7 at the respective endpoints.
   Proposed fix (optional): state the disjoint supports. Then "jointly independent of all minus rows" is immediate.

8. REMARK (stale status sentence). PROOF.md line 80: "Exact ranks and nullspace exports remain pending until the
   attached original-data run passes". This has been superseded by RESULTS.md (run passed, export hash 96f271d7...).
   It is harmless because the proof hash was frozen before the run.
   Proposed fix: on adoption, add a pointer to RESULTS.md in an audit-clarification file. Do not edit the frozen
   proof.

## Items checked and found correct

- C6 at the other joins (lines 10, 42, 48). The degree is 7 and every interior knot of the 42-knot clamped vector is
  simple (checked exactly below), so each spline is C^(7-1)=C^6 there. Topics206 and 239 check all 884 interior
  joins exactly. A C6 piecewise polynomial lies in H^s for s<15/2.
- Jump criterion at the exceptional joins (line 48).
  - All columns are C3 at t_minus, t_plus and t_J (rechecked exactly). Each side is analytic up to the join:
    exponentials on the left of t_minus and right of t_J, polynomials in between, zero outside.
  - So a nonzero 4th or 5th jump makes the cofactor fail H^(9/2) or H^(11/2) respectively, and both are below
    25/4. If both vanish, B_d is C5 with a piecewise smooth 6th derivative, hence in H^s for s<13/2, which
    includes 25/4.
  - The cofactor chi h/(b_H p)=chi 2cos^2(theta) B_d exp(3t)/b_H(t) is a tensor product with a smooth positive
    radial weight. Necessity is detected on an open interval in the chi=1 region, away from the axis (Finding 1).
  - Global H^sigma of h/b_H controls the variable order 41/20<=s<=sigma. Proof 173 defines X_s with exactly these
    two terms and the zero traces.
- Scalar coordinate and J (lines 38, 42). The vertical cofactor of h_i is 2cos^2(theta)B_i/s_i, which vanishes on
  both vertical axes. Hence the E B_H coordinate is beta=0 and J=0, and S cap H_full equals S cap X_s. The
  H^(29/4) scalar order never enters, which is correct.
- Ends (lines 44, 46).
  - Inner end: h/b_H=O(r^(1/5)) with all cylinder derivatives, which is square integrable as t->-inf.
  - Outer end: the largest outer exponent is alpha_1=2k-4, so h=O(r^(2k-1)), and dividing by b_H=r^(-1/2) gives
    exponent 2k-1/2<0. Here k=1615536043799051/2^53, approximately 0.1794, which is below 1/4.
  - Every column other than the outer five vanishes on [t_plus,infinity), and every column other than the inner
    seven vanishes near the origin. So the only constraints are the three finite joins.
- Graph necessity (lines 58-62).
  - By one-sided Leibniz, the 5th-derivative jump of q B_d' at t0 is q(t0,theta)J_(v,6)(d). All other
    contributions vanish because q is C6 and B_d is C5.
  - The Hadamard split is correct. (t-t0)B_d' has its first jump in derivative 6, so it lies in H^s for s<13/2,
    and multiplying by Q in W^(6,inf) keeps it in H^6. The terms B_d times W^(6,inf) coefficients are in H^6. The
    leading tensor term fails H^(11/2) on an open interval near the axis, and 11/2<25/4.
  - The three joins are separated (t_minus<t_plus<t_J=t_plus+1), so each condition is local. Membership holds
    exactly when all of them hold, which is the common nullspace.
- Graph sufficiency (line 66). With zero jumps through order 6 at the three joins, B_d is piecewise C6 everywhere.
  Then B_d' is in H^s for s<13/2, and products with W^(7,inf) coefficients stay in H^sigma. The ends keep their
  strict powers (Finding 3), and the coupling is bounded into Y_H (Finding 4). This gives A0h in Y_H on the maximal
  domain. No smooth-core assumption is needed.
- Angular and radial structure versus 235. This is the identical tensor form, F=1+cos(2 theta) (235 lines 21-24).
  The outer rows are exactly 235's J_4, J_5, J_6. I checked that the outer 4th jumps equal P(alpha_q).
- Pivot columns (lines 70-72). The pivot columns 7,8,9 = sp4,sp5,sp6 and 32,31,30 = sp29,sp28,sp27 match the 239
  labels. The endpoint vanishing orders are exactly i on the left (i<=7) and 33-i on the right (i>=26).

## Independent rank check

Script: theory-working-files/audit/agent_240/rank_audit.py
(SHA256 c66673780f7f896fb9d3acf16ec3a719d2a0f24f9219f02253017d052b74ab59)

Output: theory-working-files/audit/agent_240/rank_audit_output.txt
(SHA256 4175fb8c2677b3791f04a6ad368be7734d59f5990f55bd55038df3fee0f595ff)

It was run with nice -n 19 and python3.12 -B, single thread, and took 0.21 s. It uses only fractions.Fraction and
its own elimination; there is no numpy and no import of any team's code.

- Part A loads the exported matrices and bases. It computes ranks with two pivot orders, checks every nullspace
  identity, checks independence of the basis vectors, checks containment, and verifies rank plus nullity equals 38.
- Part B rebuilds every row from scratch and compares entry by entry with the export. It uses:
  - the 239 coarse knots, k and scales;
  - its own Cox-de Boor polynomials on the two end spans;
  - its own Vandermonde solve for the inner C3 matching;
  - its own Lagrange weights for the inner powers;
  - outer exponents from the 235 pair list and k.

Output (verbatim):

```
PART A: exported matrices and bases
shapes: input 6x38, graph 9x38, input basis 32 x 38, graph basis 29 x 38
row labels input: [['minus', 4], ['minus', 5], ['plus', 4], ['plus', 5], ['outer', 4], ['outer', 5]]
row labels graph: [['minus', 4], ['minus', 5], ['minus', 6], ['plus', 4], ['plus', 5], ['plus', 6], ['outer', 4], ['outer', 5], ['outer', 6]]
rank(input matrix)  natural order = 6, reversed order = 6
rank(graph matrix)  natural order = 9, reversed order = 9
nonzero A6*v over 32 input vectors: 0 (of 192 identities)
nonzero A9*v over 29 graph vectors: 0 (of 261 identities)
nonzero A6*v over 29 graph vectors (containment): 0 (of 174 identities)
rank(input basis) = 32, rank(graph basis) = 29
rank(input basis + graph basis) = 32  (32 means graph span inside input span)
every input row equals the identically labelled graph row: True
rank + nullity: input 6 + 32 = 38, graph 9 + 29 = 38

PART B: independent reconstruction of all jump rows
knots 42, splines 34, degree 7; clamped: True; interior knots simple: True
partition of unity at both ends: True
left vanishing orders b_0..b_7: [0, 1, 2, 3, 4, 5, 6, 7]; b_8..b_33 vanish to order >=8 at t_minus: True
right vanishing orders b_26..b_33: [7, 6, 5, 4, 3, 2, 1, 0]; b_0..b_25 vanish to order >=8 at t_plus: True
own inner coefficients equal 239 export: True
k = 1615536043799051/9007199254740992, 0<k<1/4: True; own outer exponents equal 239 export: True; alpha_1..9 distinct: True
own outer Lagrange rows equal 239 export: True
all 38 columns C3 at t_minus, t_plus, t_J (jumps of order 0..3 vanish): True
scales from 239 equal 240 export and all positive: True
rebuilt 6x38 matrix equals exported high_input matrix entrywise: True
rebuilt 9x38 matrix equals exported high_graph matrix entrywise: True
column supports of order-4..6 rows: {'minus': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'plus': [30, 31, 32], 'outer': [33, 34, 35, 36, 37]}
supports pairwise disjoint: True
minus rows on columns [7, 8, 9] lower triangular with nonzero diagonal: True
plus rows on columns [32, 31, 30] lower triangular with nonzero diagonal: True
outer block ranks: orders 4-5 -> 2, orders 4-6 -> 3
minus block ranks (scaled): orders 4-5 -> 2, orders 4-6 -> 3
plus block ranks (scaled): orders 4-5 -> 2, orders 4-6 -> 3
outer block ranks (scaled): orders 4-5 -> 2, orders 4-6 -> 3
outer fourth jumps equal P(alpha_q) of proof 235: True
rank(rebuilt input) = 6, rank(rebuilt graph) = 9
seconds: 0.207
```

The 192+261+174=627 nullspace identities match the count in check.json. The ranks are 6 and 9, so the dimensions
are 32 and 29.

One input is not independent of the teams: the coarse knot vector and k come from the 239 export, not from the
original NPZ. The 240 check.py asserts that its NPZ reconstruction equals that export (line 51 of check.py), and
proof 239 is confirmed.

## Scope

Statements (1) and (2) are proved for this exact 38-column span. The exported bases are exact bases of the two
intersections in the coordinates of the scaled columns h_i. Nothing here gives a high-norm Gram, a singular value,
an inverse bound, or any statement about the 169-column section. The proof says this correctly (lines 38 and 80).
