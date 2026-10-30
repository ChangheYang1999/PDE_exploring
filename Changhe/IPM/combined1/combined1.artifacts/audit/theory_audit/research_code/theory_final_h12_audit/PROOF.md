# Audit of the H12 theory draft and numerical publication

## Scope, sources and dependencies

The frozen theory target is source/THEORY_FINAL_draft12.md, SHA256
5e4f4b003ed15fbed67ba4e6e32bafe2c4dd23b8b48bf4a3b42cddcb8d23daa6.
The numerical target is source/numerics_v09.md, the immutable publication
at 2026-10-29T07:11:15Z. This audit reads the complete changes from the
previously audited theory draft and checks the new deductions against the
standalone proofs cited below. Unchanged results retain their earlier audit
hypotheses. This is not a new existence theorem.

## 1. The global sector convention requires relabelling

The theory draft now defines a sector (l,q) by

    e(l,q)=1-l delta-2q,  delta=1-1/c,
    c=4076476460239181/2251799813685248, l>=1, q>=0.

The leading transport cancellation is (1,0), since e(1,0)=gamma=1/c
and c gamma-1=0. A nonzero homogeneous residual r^e A(theta), with
A continuous and not identically zero, belongs to L2 at infinity exactly
when e<-1: its squared norm contains the divergent or convergent integral
integral_1^infinity r^(2e+1) dr. Therefore all sectors with e>=-1 must
vanish. Exact rational enumeration gives (1,0),(2,0),(3,0),(4,0). After the
automatic leading cancellation, the three nonautomatic conditions are

    (2,0), (3,0), (4,0).

The analogous weighted first moment integral is integral r^(2e+3) dr.
Its threshold e<-2 gives eight sectors before removing the leading one:
(1,0) through (6,0), and (1,1),(2,1). Hence the three-versus-seven count
is correct, but the three labels in draft lines77,134,189,583,841 are
not consistent with its definition. Line104 and any other occurrence of
the old three-label list need the same update. The old convention was
(h,k) with e=gamma-h delta-2k; the exact conversion is l=h+1,q=k.

This is a real specification error: the old list includes an automatic
condition and omits the nonautomatic (4,0) condition. The candidate
conclusions are unaffected because the audited eleven exact cancellations
include all the required sectors. The adjacent code exhausts the possible
indices using the exact positive delta, rather than a floating exponent.

## 2. The second forced tail is relative to a changed reference

The theorem in ../dipole_forced_tail/PROOF.md has the following domain.
Fix c>1, gamma=1/c and gamma-4<q<-3. The reference R is C1 and S1, its
specified canonical velocity satisfies |U[R]|<=V r^gamma, and
|grad R|<=G r^(gamma-1) for r>=R0>=2. Its residual has the uniform form
F(R)=r^q A+O(r^(q-epsilon)), epsilon>0. The correction k is centrally
odd C1 with

    H_q(k)=max(sup (1+r)^(-q)|k|,
                 sup (1+r)^(1-q)|grad k|)<infinity.

If R+k is exact at the same c with velocity U[R]+U[k], the theorem
implies k=r^q A/(1-cq)+o(r^q). Its proof includes the local velocity
term, a dipole estimate, and radial integration with a zero boundary value
at infinity. It does not derive H_q(k) from an L2 hypothesis.

For the application, start with one of 007,013,014, denote it by R, and
let eta be the global repair of T4-295. Define R_tilde=R+eta. Apply the
theorem to R_tilde and a NEW correction k with H_q2(k)<infinity, where
q2=1-9delta. The correct conclusion is

    k=r^q2 F_(9,0)/(1-cq2)+o(r^q2),
    h_total=eta+k,
    R+h_total=R_tilde+k.

Draft line542 switches between these two meanings of h. Explicitly name
k and its H_q2 hypothesis. In particular, the earlier H_q1 assumption
on h_total, q1=-1-4delta, does not itself state H_q2(h_total-eta).
An O(r^q2) value remainder alone does not establish the needed derivative
bound. The earlier -3<q<0 forced-tail statement also needs the reference
growth hypotheses |U[R]|<=V r^gamma and |grad R|<=G r^(gamma-1), as
stated in ../forced_integrable_tail/PROOF.md. They hold for the present
algebraic references but should be explicit in a standalone theorem.

These are domain and notation repairs. The cited underlying theorems and
their explicitly conditional applications remain CONFIRMED.

## 3. Small-norm cutoff radii and weighted costs

For the particular leading-tail cutoff family of T4-314,

    ||h_L||_2=C00 L^(q1+1), C00>0, q1+1<0.

For epsilon>0 this norm is less than epsilon if and only if

    L>(C00/epsilon)^(1/(-q1-1)).

That is an exact symbolic threshold. R1-035 computed C00 by mpmath
quadrature, not a directed enclosure, and obtained approximately215936.94,
with a threshold approximately45174.312 at epsilon=10^-3. Therefore draft
lines64 and379 should state this as a FLOAT estimate for this particular
cutoff family, not an exact numerical threshold or a necessary radius
for every repair. No certified result uses these approximate radii.

R1-035 remark(b) is now independently CONFIRMED by T4-326. If a<=q1+1,
the E_a residual of this family diverges as L tends to infinity: the rate
is at least a positive multiple of L^(q1+1-a), or sqrt(log L) at equality.
The explicit finite-radius and remainder hypotheses are given in
../tail_cutoff_weighted_cost/PROOF.md. The result is not a lower bound
for every repair and does not apply to a=0. T4-314 is AUDITED in T4-325;
its two-tail extension T4-324 remains OPEN independent review.

## 4. Arithmetic and report status

The checker evaluates every displayed distance ratio in the fourteen
numeric rows, including the arithmetic of the still-labelled-OPEN017 row.
Each displayed factor is below the ratio obtained using the displayed
distance floor and the safe ceilings3.7930e-6,2.8496e-6,25/54684. Checking
the arithmetic of an OPEN row does not accept its input certificate.

Since draft12, T4-319,320,323 independently confirm017's local fields,
the n23,K2400 weak radius greater than0.001068502321536437, and its full
sixteen-sector prefix. Thus017 is excluded from every registered scalar
ball and graded box, including statL and bL. The stronger n19,K1800
number remains OPEN in this audit until independently reproduced.
The dyadic result T4-303 for010 is already accepted, so section2.6's
'Not tested at010 to014' and section9.3 item5's request to test010 are
stale. Update them without implying that all later dyadic pairs have
been tested. A blanket 'every registered candidate/framework pair is
excluded' is too broad: the localized route still lacks a high inverse,
and not every dyadic pair has a completed candidate check. T4's own
handoffs136,137 and status file used that overbroad shorthand; the correct
H12 sentence names the scalar and graded frameworks explicitly.011
remains a controlled FLOAT comparison.

No existence closure has been established. Finite-dimensional rank does
not give an inverse, and necessary distance lower bounds do not order
actual distances between candidates.

## 5. Numerical-publication interpretation

The mathematical counterexamples in ../theory_v05_audit/PROOF.md refute
numerics_v09 section1's assertion that the held-out rows decide whether
a previous plateau was a span limit. A finite set of smaller probe
values, including higher angular modes, supplies no upper bound on the
unmeasured residual or on the actual correction distance. Thus section0's
inference that residual mass lies in a specified finite mode band, or
that a sweep ending at31 is sufficient, is not established by the listed
probe lower bounds. The reported trials remain useful FLOAT observations.

The exact support of the new densities includes17, not just19 through31
(T4-321, independent reproduction of N4-248). Numerical rank and exact
rank must also remain separate in the SVD discussion: a badly conditioned
mesh Gram matrix is evidence about the sampled and scaled matrix, not
by itself a proved physical inverse condition number. When reporting
step residuals, specify whether the displayed quantity is F+Lh or
F(R+h), since they differ by U[h].grad h.

N4-250's previously recorded corrections remain necessary in section4:
label the positive listed sector values as magnitudes, not signed
pairings; label the maximum over tested k as a sampled maximum; and
keep a truncated31-sector model distinct from the complete residual.
The header's merged text and stale consultation time need editorial
repair. Those issues do not invalidate the independent complete Arb
certificates in the ledger. Publication versions remain immutable;
repairs belong in the next version or final report.
