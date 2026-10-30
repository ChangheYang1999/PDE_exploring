# Audit of the published theory_v08 and THEORY_FINAL draft 52

## Objects, hypotheses and evidence boundary

This audit concerns theory_v08, published 2026-10-29T15:30:58Z, SHA256
 a35184b753f57216c6b4bc01052317c508fe5439fda65b682b0cecb098be8bc9,
and THEORY_FINAL draft 52, SHA256
 82b4d9db1e5e25af3add32fedc87ae469191044735f2f749f4c80033c8f57451.
It compares all 156 changed word blocks of the publication with the
accepted preview2 and all 72 changed blocks of draft52 with draft43.
The unchanged theorems keep their exact hypotheses and verdicts in
T4-437, T4-445, T4-455 and T4-456. The task is a finite composition audit,
not a new proof of the nonlinear inverse or a replay of candidate integrals.
This proof precedes the checker. Source copies, exact JSON, and hash
receipts are stored alongside it. Thirteen accepted proof/result pairs
supply the dependencies T4-454 to T4-470 used below.

The fixed-c correction results set c=4076476460239181/2251799813685248,
fix the candidate's leading far field and use real S1 functions, even in
x and odd in y. The canonical velocity is
U[h]=(partial_xy,-partial_xx)Delta^(-1)h, including the local term (0,-h/2).
The fixed-c tangent chart has c[h]=0. The scalar norm is
X_(s,w)(h)=E_w((1-Delta)^(s/2)h), with
E_w(g)^2=||omega D2g||2^2+w1||Dg||2^2+w2||g||2^2,
omega=(1+4|X|^2)^(2/5), s>=0 and positive w1,w2.
Consequently X_(s,w)(h)>=sqrt(w2)||h||2. Every inverse statement retains
its operator domain, range, normalization hyperplane, reference estimates
and existence of the chosen realization. A kernel scaling mode outside
this L2 chart is not a missing invertibility test in that chart. No weak
L2 argument here is transferred to a space with decaying dyadic weights.
The source's hypotheses about origin regularity, products and infinity
are retained. Scalar or graded exclusion is not an unrestricted
nonexistence theorem for self-similar IPM profiles.

## Table arithmetic and the incorrect old scalar cap

If 0<T<=t and Q>=p>0, then Q/T>=p/t. Thus rounding p/t downward proves
exactly the stated lower factor. Reparse all 24 published test rows and
repeat their rational divisions using the accepted p,t values. At the
exact family ceilings the endpoint factors require the monotonicity
argument in T4-455, not substitution of a rounded upper radius into an
increasing bound. Its nine corrected factors and three H0-only factors
remain applicable without change. The meanings of the groups remain
separate: D excludes correction balls, S rejects specified sufficient
forcing tests, and U/P/R/A/K reject the named endpoint certificate or
majorant class. No failure of a sufficient estimate is recast as a
necessary condition for all stationary solutions.

For a fixed scalar family with positive constants mu,C,cU,w2 and high
margin mu-C*s-cU*r/sqrt(s)>0, s>0, its L2 radius b=r/sqrt(w2) satisfies

 b^2 < 4*mu^3/(27*C*cU^2*w2).

Indeed r < sqrt(s)(mu-C*s)/cU, which requires 0<s<mu/C. On this
interval its square has its maximum at s=mu/(3*C). The seven exact
family squares are compared with the corrected upper displays of T4-454.
Their common upper bound is 3.7930e-6. The original graded ceiling is
50/(651*sqrt(28248)); its square is 625/2992882662 and it is below
25/54684, which is below 1/2000.

The assertion that every registered scalar ball has L2 radius below
2.7e-6 is not a consequence of the registered high-margin condition.
For TB-sharp take mu=297/1000, C=402, cU=8/5, sqrt(w2)=512,
s=1/4096 and r=1536/1000000. Its high margin is strictly positive and
r/512=3e-6>2.7e-6. This counterexample concerns the high-margin algebra;
it does not assert that the other hypotheses of a complete existence
certificate hold for these parameters. The old universal-cap argument
is REFUTED in this stated sense. Replacing the old bound by 3.7930e-6
repairs its use for the seven fixed registered weights.

For each of the 26 numeric rows in draft52's distance table, divide its
accepted strict distance floor by 3.7930e-6, 2.8496e-6 and 25/54684.
All 78 displayed factors must be strict downward bounds. Twenty-three
rows are unchanged from T4-456. The three added rows 002,003,004 use
floors 1.56361352,0.22988134,1.40009623 from T4-068. Their previously
accepted integral data also enter T4-459. Independently re-evaluate
I-D/1000-H/1000^2>0 for every one of its 24 candidates. The weak
identity |<F,phi>|<=D||h||2+H||h||2^2 then excludes every correction
with ||h||2<=1/1000. Thus replacing the smaller scalar cap leaves all
24 fixed-c exclusions intact.

The all-weight unweighted bL extension is a distinct implication. Under
WU3, with the actual floors m2=1/2,m1=9/10, O=347/10, beta<=1+c<57/20,
C>=390.68 and cU>=1.5871, T4-462 and T4-468 bound the L2 radius by
4.1069e-6. Together with the same 1/1000 exclusions this rejects all
those unweighted bL choices. It does not reject independently weighted
L2 energy, improved reference floors, different commutator constants or
the dyadic space. The seven tighter six-digit values are rounded values
of the relaxed supremum using the rational lower constants, not directed
bounds and not optima of the full weight-dependent scheme.

## Candidate 001 and the remaining changed results

T4-465 accepts both Opus reviews of T4-458 and its erratum: for the
canonical candidate001, no real S1 correction h in L2, satisfying the
stated distributional products, makes rho+h stationary at any real c.
The proof covers the whole affine class rho+L2 and any fixed constant
background velocity. At c different from the snapshot c0 the annular
test uses the leading density G0, not the orthogonal residual E. At c0
it uses the nonzero leading residual obstruction. Neither the radius
cap nor a finite small-ball condition enters this theorem. Its exact
origin and tail requirements are those in the frozen standalone proof.
Accordingly the blanket sentence 'each concerns the fixed c and the
stated balls' is REFUTED. The statement that matrix row35 records only
framework inapplicability is also stale: the frozen cited v140 already
records the stronger annular theorem. The separate forcing-membership
failure remains true. Neither theorem covers an arbitrary different far
field or a non-L2 correction space.

The new 015 and 017 dyadic statements follow from T4-461 and T4-463 with
all inverse, normalization, realization, partition and absorption
hypotheses. For 017 the weakest seven-cell lower factor is
1.221854480167 on [1/4,1/2], not the first-cell value 1.244974. The exact
TB-rebal endpoint repair is T4-464: the true family radius is strictly
between 3.5125e-7 and 3.5126e-7, the shape obstruction persists and the
crude bound is inconclusive there. No universal lower obstruction is
misidentified as an attained valid coefficient.

The complete 016 four-norm assembly and ten forcing failures are
T4-467. Its five actual XSW comparisons use identical parameters and
retain strict gaps for 007<016. They do not order correction distances.
The added negative-norm statement is the orthogonal-mode inequality
H(F)^2>=sum p_n^2/d_n in the completion for the gradient norm, where
p_n=<F,phi_n> and d_n=||grad phi_n||2^2>0. T4-470 now accepts its
numerical composition with N4-396's complete 4096-bit pairing as an
explicit numerical premise. It gives H(016)>0.529469576110512066428681
and E2(016)>608.392385921614>606.820219>E2(007), with
E2^2=P2^2+2^14 G1^2+2^18 G0^2+(20/21)2^18 H^2.
This pairwise comparison neither minimizes E2 over all snapshots nor
orders the actual H values. The saved 200-digit intermediate groups
cannot reproduce their highly cancelled pairing sum; T4-470 expressly
retains the complete runtime certificate. The new divergence-free upper
route T4-469 is still OPEN pending independent analytic review. No
manufactured example is used to discharge that review.

## Source chronology and required successor repairs

All 139 Appendix H hash claims are accounted for: 134 match the files
read at the recorded audit time; the five changed live files are recovered
exactly as historical byte prefixes or frozen copies. The recovered
contents are saved compressed and their decompressed hashes checked.
Hash agreement binds a source; it does not prove its mathematical claims.
The later mutable files are not mislabeled as current hash matches.

Candidate028 was registered at 2026-10-29T15:24:01Z and numerics_v15 was
published at 15:25:44Z, both before theory_v08. The very INDEX hash cited
by theory_v08 includes 028. Therefore 'reserved ID without a registered
snapshot' was already false at publication. It is a registered FLOAT
comparison, OPEN, without an independent candidate certificate here.
Update its status and the header's 'INDEX through 027'. Candidate011
and candidate027 remain OPEN. A FLOAT comparison is not a new exclusion.

Draft52's current outstanding-item list still calls the 017 (21,522)
probe OPEN. T4-460 already accepted it through N4-384 with strict floor
0.000596123050327423. It remains outside the registered 25-probe family.
Its acceptance must not silently reclassify it as a registered holdout.

Required repairs are: replace the stale 2.7e-6 cap with its proper scope;
remove the unnecessary radius parenthesis from the whole-affine 001
claim; distinguish row35's stronger current theorem from its original
membership failure; qualify the blanket fixed-c sentence; register 028
as FLOAT and OPEN; and update the stale diagnostic probe status.
These repairs change none of the established exclusions. CONFIRMED
applies to the finite mathematics above with its exact dependencies.
REFUTED applies to the specified literal/scope claims. Full existence
closure, an improved valid inverse and a certified complete Hardy upper
for 016 are not supplied by this audit.
