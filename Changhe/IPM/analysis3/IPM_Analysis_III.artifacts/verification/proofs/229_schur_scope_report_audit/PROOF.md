# The finite-block hypotheses in the inverse bound are essential

## Statement and scope

This is a scope audit of the Schur paragraph of S2_BASIS_CERTIFICATION.md section6.1, in the preserved15:14 report snapshot. It does not alter proof 78's verified conditional theorem. That theorem assumes a Hilbert space H, a bounded Fredholm operator F:H->H of index zero, an orthogonal finite-rank projection P, Q=I-P, a bijective complement D=QFQ, and constants d>0, a,b,c>=0 with

 ||D^(-1)||<=1/d, ||PFQ||<=b, ||QFP||<=c,
 ||PFP p||>=a||p|| for every p in PH,
 s=a-bc/d>0.

It gives invertibility and

 ||F^(-1)||<=sqrt(p0^2+((1+c p0)/d)^2),
 p0=sqrt(1+(b/d)^2)/s.

The report paragraph omits finite rank, orthogonality and index zero in its statement. For a general orthogonal projection and a bounded operator, the displayed bounds prove injectivity and a lower bound but do not prove onto. This omission is refuted by the exact counterexample below. The intended conditional theorem is restored by stating proof 78's hypotheses.

## Counterexample

Let H=ell^2(N0) direct-sum R with its Hilbert norm. Let P(u,v)=(u,0), Q(u,v)=(0,v). P is an orthogonal projection of infinite rank. Let S be the unilateral right shift on ell^2(N0),

 S(u0,u1,u2,...)=(0,u0,u1,...),

and put F=S direct-sum I_R. This is a bounded operator of norm one. Its complement D is the identity of R, so d=1. The two cross blocks vanish, so b=c=0. Since S is an isometry, ||PFP p||=||p||, so a=1 and s=1. Thus all the assumptions actually printed in the shortened Schur paragraph hold.

F is injective. Its range is the closed codimension-one subspace of pairs (w,v) with w0=0. Therefore it is not onto and has no inverse H->H. The target vector ((1,0,0,...),0) has no preimage. Its Fredholm index is minus one. This counterexample does not satisfy proof 78's finite-rank or index-zero hypotheses and therefore does not contradict that theorem.

## The exact estimate and existence step

For Fu=f write u=p+q in the orthogonal decomposition PH direct-sum QH. The complement equation gives

 ||q||<=(||Qf||+c||p||)/d.

The first row and the triangle inequality give

 s||p||<=||Pf||+(b/d)||Qf||
          <=sqrt(1+(b/d)^2)||f||.

The second inequality uses orthogonality. These inequalities at f=0 show injectivity, but not existence of a preimage for arbitrary f. Under proof 78's index-zero assumption, injectivity gives surjectivity. Once existence is known, orthogonality of p and q proves the displayed inverse bound.

Alternatively, finite rank of P and invertibility of D already reduce existence to the finite-dimensional Schur operator PFP-PFQ D^(-1)QFP on PH. Its norm lower bound is s, so it is injective and hence bijective. This also proves existence under the finite orthogonal projection hypotheses. No such implication applies to an arbitrary infinite block.

No numerical computation, PDE inverse, complement estimate or necessary finite dimension is claimed. The only dependencies are the elementary Hilbert-space block equations and the accepted statement of proof 78. The saved report snapshot fixes the wording being audited.
