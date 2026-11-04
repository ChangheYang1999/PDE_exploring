# Audit of the report assembled at 15:50 UTC

## 1. Exact object and method

The retained in the team records has 6085 lines and SHA256 8207e59676a668dae262db17faa433fc9f3cabd379da50df1b257325536f4fed. Its stated assembly time is 2026-11-03T15:50Z and it records verdicts through A1536. The prior retained report is in the team records. Every one of the 54 word-level changes was read, together with the complete new Theorem 8, its assumptions row, new scope paragraphs and the relevant retained proof dependencies. This is a delta audit on the previous body and appendix audits, not a claim that the new 6085 lines were independently reread in full.

The exact notation below is Jx=e3 cross x, B=(cI-omega J)y+U, W=curl U and S=(DU+DU^T)/2. The equation is

    (1-c)U+B.grad U+omega JU+grad P=0, div U=0.

Hb means bounded U with U(R.) tending to zero in distributions as R tends to infinity. All spaces are on R3 unless a local tail is explicitly specified. Every omega is a finite real number. Matrix norms are Frobenius norms.

## 2. Previously requested repairs

The A1458 repair now states p1>=0 at common flat points, with equality only under the separately proved hypotheses. It no longer infers equality merely from DW=0. The A1459 repairs restore the zero-field alternative, or explicitly require nontriviality, in the fixed-direction and axially invariant local-tail results. The A1460 repair adds the supported zero of W with k=S=0 to the negative-sigma1 rank-one conclusion. These changes match A1414-A1422 and A1452-A1460.

The CO60 row distinguishes a reduced-system example from a full profile and records failure of the Poisson equation. Its corrected annular virial formula matches A1507-A1508. The critical vorticity shells in Theorem 8 are exactly Ak={2^(k-1)<=|y|<2^k}, as in A1526. There is no shell-index or constant mismatch.

## 3. Theorem 8 at its explicit hypotheses

Let U be C2, P C1 and satisfy the equation and Hb. For 0<c<2/3 put kappa=1-3c/2. With bounded W, each of the following implies U=0: (i) sup|W|<sqrt(3)kappa; (ii) sup|W|<=sqrt(3)kappa and limsup at infinity |W|<sqrt(3)kappa; (iii) bounded S and sup|S|<(3sqrt(6)/2)kappa; (iv) bounded S and sup(-lambda_min S)<3kappa. For 2/5<c<1, U and P merely C1 suffice if integral<y>^(2/c-3)|W|^2 is finite. For every c>0, the pointwise strict inequality lambda_max S<1 on the closed ball of radius ||U||infinity/c also implies U=0; this last criterion needs no global W bound.

These are the exact assertions confirmed in A1433-A1435, A1524-A1526 and A1530-A1535. Their proofs give the stated thresholds. In particular the energy theorem supplies the shell bound for c<=2/3. The velocity-weight statement means precisely integral<y>^(-m-2)|U|^2<infinity for m>3-2/c, not an integral with weight <y>^(-m). The strict far-field W condition supplies W,DU in L2 and U in L6, after which

    integral|S|^2=(1/2)integral|W|^2,
    kappa integral|W|^2=integral W.SW,
    integral W.SW=-(4/3)integral tr(S^3)

give the smallness conclusions; the third identity is used only with bounded S. For the strain forms, bounded W and S imply bounded DU before applying A492 to obtain W=O(1/r); hence the far-field condition is redundant. Bounded S alone is not the hypothesis used in that argument. For the weighted criterion A1524 gives U=BS(W) and energy o(R^(5-2/c)), contradicting the positive energy constant of a nonzero profile. Its normalized-shell limsup and C4 match the report.

For the compact-core criterion, continuity gives a slightly larger ball and delta>0 with lambda_max S<=1-delta there. Every backward carrier orbit enters that ball and stays there. On a segment from time s to t inside it,

    |W(Phi_t y)|^2<=exp(-2delta(t-s))|W(Phi_s y)|^2.

Let s tend to minus infinity. W is bounded on this compact ball by continuity, so W vanishes there and then on every orbit. This explains both the direction of the damping argument and why no global vorticity bound is needed in part (c). Bounded harmonic U is constant and Hb makes it zero.

## 4. Scope omissions and wording repairs

The complete statement of Theorem 8(a) retains bounded W and is confirmed. Its Section 3 assumptions row compresses the strain alternative to a strain bound and omits bounded W. That row is not a faithful standalone statement of the audited theorem. Add bounded curl U to the strain alternative, and retain the precise constants or a reference to the complete part (a). The compact-core alternative (c) remains separate.

The phrases that decay alone gives none of the added conditions, or that decay alone does not give them, assert unproved nonimplications inside the profile class. The correct formulation is that it is not known whether bare velocity decay implies the needed smallness or weighted integrability. In particular, proving the main conjecture would make all those conditions true trivially. No counterexample profile establishes their failure. A1564 already corrected an earlier auditor sentence that made this mistake for the velocity shell bound, which actually follows from Hb.

The LIT244 summary says there is no infinitely flat germ. Its literal form excludes the zero germ, which satisfies all its premises. Say instead that an infinitely flat germ is identically zero near the point, or that there is no nonzero infinitely flat germ. The precise source and A1541-A1545 have the latter meaning.

## 5. CO61 additions

In this paragraph only, V is a local homogeneous tail, X=(cI-omega J)y, k=V.X, q=2(1-c)/(1-2c), and S=P2-|V|^2/2 is the tail scalar, not the strain matrix.

The report repeats two scope errors already isolated in A1561-A1562. The nonzero-k representation with S=D|k|^q describes one vortical component, and need not hold on an irrotational k!=0 patch. An exact local counterexample for each target c at omega=0 is h=rho^(1-p)cos((1-p)theta), V=grad h, P=-|V|^2/2, p=(1-c)/c, on a patch with positive cosine. It is divergence free and irrotational and solves the local similarity equation, while S/|k|^q is nonconstant. Section 5 of in the team records gives every substitution.

For transverse covectors the quadratic form is Q(xi)=(qS+|V|^2)|xi|^2-(V.xi)^2. Its eigenvalues are qS+k^2/|X|^2 and qS+|V|^2. Thus the strict interval -|V|^2<qS<-k^2/|X|^2 gives two distinct real characteristic lines. At either equality there is still a null line, or every line if Q vanishes identically. Replace the report's real-characteristics iff strict wording by the two-distinct-lines statement and identify the degenerate equalities. The local coupled system has not been proved to have, or to lack, continuation through a common flat point.

## 6. Verdict boundary and remaining work

The explicit Theorem 8 statement and the old requested repairs pass. The table omission and the CO61 summaries need repair; the zero-germ phrase needs its nonzero qualifier. The bare-decay nonimplications remain open. CO62 is marked submitted and needs its own audit. Whole-report approval is therefore OPEN. This review neither proves the target conjecture nor broadens any conditional theorem to arbitrary helicity or bare decay. No computation, formal build or new external model consultation was used.
