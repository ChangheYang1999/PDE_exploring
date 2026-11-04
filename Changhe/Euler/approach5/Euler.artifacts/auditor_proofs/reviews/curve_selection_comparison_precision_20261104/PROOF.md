# Parameter selection: sufficient bound versus equivalence

Date: 2026-11-04T13:02:08.372759+00:00.

## 1. Exact claim and hypotheses

Let m>0, 0<z<z'<m, Delta=z'-z, and let p be a positive integer with p(m-z)>2. Define

    theta=(p Delta-3)/(p(m-z)-2),    theta0=Delta/(2m).

The Theory Agent C  comparison dated13:01:06Z, item4, says that theta>=theta0 if and only if p Delta>=6. This equivalence is false. The report2C Lemma11 uses only the sufficient bound p Delta>=6, which is correct. Here m=log Mf, z=zeta and z'=zeta'. No Euler or regularity hypothesis enters this scalar check.

## 2. Complete argument

Both denominators are positive. Cross multiplication gives

    theta>=theta0
      iff 2m(p Delta-3)>=Delta(p(m-z)-2)
      iff p Delta(m+z)>=6m-2Delta
      iff p Delta>=(6m-2Delta)/(m+z).

The last threshold is strictly below6, because z>0 and Delta>0. Hence p Delta>=6 is sufficient but need not be necessary. For an exact example take m=1, z=1/4, z'=3/4 and p=10. Then p Delta=5<6, theta=4/11>1/4=theta0, and the denominator is11/2>0. Also h=pz+2=9/2, alpha=pz'-1=13/2 and L=pm=10 satisfy 1<h<alpha<L. This example refutes the stated equivalence, without claiming to satisfy every later complexity constraint on the final selected p.

## 3. Disposition and dependencies

Verdict: REFUTED only for the word "iff" in this comparison. Replace it by "whenever", as the source's "as soon as" already states. The report selects p large enough to satisfy the sufficient condition together with its other bounds, so neither the source lemma nor A3243 needs a mathematical repair. The Theory Agent A  comparison109lines and all seven C items plus its closing scope paragraph have been read. Their remaining analytical steps agree with the independently reread report2C Lemmas6-20. The A comparison cites the initial follow-up e649ade2; C explicitly checks the corrected92113e4b and its two-hunk precision delta. No symbolic diagnostic in either comparison is adopted.

Dependencies are the exact scalar definitions in report2C Lemma11 and the captured comparison text. The source proof remains at4466ea1ade736a92d76f1f77f811905b6fff2dd0f62d0952664f9a7f8fe91b32. This is an ancillary comparison correction, not a new research direction, report-assembly verdict, or objection to the main core theorem. The arbitrary-omega conjecture remains OPEN.
