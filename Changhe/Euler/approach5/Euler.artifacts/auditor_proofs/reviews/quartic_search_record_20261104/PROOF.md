# Audit of the bounded quadratic-pressure search record

Status: numerical-record and static implementation review. No numerical candidate is promoted to an exact certificate, and no global optimum is inferred.

## 1. Claim and evidence boundary

The retained search asks whether a real solenoidal homogeneous quadratic vector field Q in three variables has an admissible quartic Poisson pressure ratio larger than the previously established equivariant value g_star. The prewritten plan uses the exact scalar cone criterion but evaluates it in floating arithmetic. Its success condition is a candidate above g_star+1e-7 or 1/6, with a positive computed cone margin after lowering gamma by 5e-7. Such a success would require subsequent exact verification.

The claim audited here is limited: the executed source snapshot implements the stated finite-dimensional polynomial quantities, the archived summaries agree with the retained records, and none of the completed records passes the literal numerical success condition. The audit does not attest all runtime scheduling or hardware settings and does not rerun the search.

## 2. Static polynomial and gradient check

Write Q_i(x)=x^T A_i x with each A_i real symmetric. Then

    div Q=2 sum_j (sum_i (A_i)_{ij}) x_j.

The three independent linear constraints sum_i(A_i)_{ij}=0 eliminate exactly the three entries (A_j)_{jj}. The other fifteen entries are free. The source's three assignments are precisely these eliminations, so its parameterization covers the full fifteen-dimensional solenoidal space.

For the normalized mean over the unit sphere, denoted by angle brackets, the coordinate x_1 is uniform on [-1,1], so <x_1^4>=1/5. Expanding (x_1^2+x_2^2+x_3^2)^2=1 and using symmetry gives <x_1^2 x_2^2>=1/15; odd moments vanish by reflection. Expanding each quadratic square therefore gives

    <|Q|^2>=[2 sum_i |A_i|_F^2+sum_i (tr A_i)^2]/15.

This is a positive definite quadratic form in the fifteen free coefficients. Also

    tr((DQ(x))^2)=4 sum_{i,j,k,l}(A_i)_{jk}(A_j)_{il} x_k x_l,
    Delta |Q|^2=x^T [8 sum_i A_i^2+4 sum_i (tr A_i) A_i]x.

These identities match the source's tensor contractions and its explicit symmetrization of the first coefficient matrix. Polarization correctly constructs the bilinear coefficient tensors from basis vectors and their pairwise sums.

Let D={B real symmetric positive definite: tr B=1, tr(B^-1)<=49}. For nonscalar C, the exact minimum m(C)=min_{B in D}tr(BC) has the unique minimizing B established in the scalar audit. Its derivative in a matrix direction H is tr(BH): compactness gives convergent subsequences of minimizers for C+tH, uniqueness identifies their limit, and the two variational inequalities squeeze the difference quotient. The chain rule therefore gives the implemented coefficient gradient and the gamma derivative -tr(B D_E), where Delta |Q|^2=x^T D_E x. At scalar C the minimizing B is not unique; the program chooses I/3 and does not claim differentiability there. Moreover its small-spread shortcut replaces nearly scalar inputs by their mean. Both this shortcut and floating root solving prevent the computed margin from being an exact cone certificate.

The run searches gamma in [0,0.251], uses finitely many local starts, and permits iteration-limit exits. None of these choices supports an upper bound for the unrestricted optimum. The exact polynomial identities are consistent with the independently compared cone and synthesis results; no property of the optimizer is a proof dependency.

## 3. Record reconciliation and success criterion

The source and executed-source snapshot are byte-identical, and their SHA256 matches the compact summary. All724 completed records were parsed and aggregated, not each individually read. Their identifiers are exactly0 through723. The flag counts are318 successful terminations and406 iteration-limit exits, agreeing with the summary. The five implementation-check entries all report passing their explicitly recorded floating tolerances. The same best record and all six checked top-level counters and timestamps occur in the full and compact results.

There are609 records passing the program's retention filter. Their largest retained gamma is0.11964126855951063, below the recorded g_star=0.1196412685595196. Its original computed margin is negative at tolerance scale, so the record is not an exact feasible example. No completed record, even before imposing the normalization-error filter, has both a gamma above either stated target and a positive margin after the planned reduction.

There is a minor implementation difference: the program's above_gstar and above_one_sixth flags compare the reduced gamma with the targets, whereas the literal plan compares the unreduced gamma and separately requests a positive reduced margin. The implemented flags are therefore stricter. The independent aggregation tested the literal plan itself and found zero candidates, so this difference does not change the reported outcome.

The archived timestamps are start2026-11-04T02:35:26.806832+00:00 and end2026-11-04T02:38:26.823019+00:00. The recorded total duration is180.0161870890297 seconds, with180.00015177484602 seconds of optimization and407140 evaluations. These are reconciled record values, not independently observed execution times.

## 4. Scope and dependencies

The plan, complete source, five implementation checks, compact summary and numerical explanation were read in full. All completed records were aggregated to test the claims in Section3. The search was not rerun. The files and exact hashes are archived under verification, including in the team records.

The existing configured model coordinator's comparisons of LIT332-LIT334 support the mathematical cone and synthesis formulas used by this search; no separate model review of this execution record is claimed. Actual provider execution of the existing model agents is not independently attested. This audit ran only local file bookkeeping. It supplies no exact new Q or pressure, no value of Gamma_2, no decaying Euler profile and no global nonexistence theorem.
