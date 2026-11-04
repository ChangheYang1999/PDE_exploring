# Independent audit of the exact central vorticity magnitude threshold

Status: A2760 CONFIRMED after independent reconstruction and existing comparison; a separate comparison-sentence qualification is recorded in Section 7. This is the LIT327 local central-matrix classification; no decaying counterexample is constructed.

## 1. Exact hypotheses and conclusion

Let c,omega be real and Jx=e3 cross x. Let U be C2 and P be C1 on a neighborhood of zero, satisfying

    div U=0,
    (1-c)U+DU[(cI-omega J)x+U]+omega JU+grad P=0.

Suppose U(0)=0 and W=curl U(0) is nonzero. Write w=|W|, e=W/w, s=|Je|, z=e.e3, k=omega s, v=omega z and u=k^2. The equation implies P is C2. We classify which pairs (omega,W) permit a positive semidefinite H=D2P(0), allowing all remaining strain parameters and H to vary.

First u>2 is necessary. For u>2 let a=u-2 and define

    C=[[3u+9u/a,3uv/a],[3uv/a,uv^2/a]],
    tau=tr C=u(3u+3+v^2)/a,
    h=((C11-C22)/2,C12),  R=|h|,
    psi=R-v^2       when R>=2v^2,
    psi=R^2/(4v^2) when R<2v^2,
    K_min=tau/2+psi,
    w_min=sqrt(4K_min-1).

Exactly the magnitudes w>=w_min are possible. Every permitted pair is realized by a full global affine profile for every real c. Positive definite H is possible exactly when w>w_min. A local pressure minimum implies semidefinite H but is not assumed separately in this classification. A strict local minimum need not have positive definite H, so no stronger necessity is inferred from strictness alone.

## 2. All central matrices are included

Set M=DU(0), Omega=curl U and B=(cI-omega J)x+U. As in the direct differentiation and curl calculation, reproduced here in its needed form,

    H=-M-M^2-omega[J,M],  tr M=0,
    MW=W+omega JW,
    HW=-2W-3omega JW-omega^2J^2W.                 (1)

The first identity follows because the carrier is zero at zero; the curl equation is Omega+B.grad Omega+omega JOmega-DU Omega=0. Substitution gives the third identity. It implies W.HW=w^2(u-2). If H is semidefinite, equality would imply HW=0, contradicting (JW).HW=-3omega|JW|^2. Thus u>2 and s>0.

Use the oriented frame (e,f,g), f=Je/s, g=e cross f. The matrix of omega J is [[0,-k,0],[k,0,-v],[0,v,0]]. The first column of M is (1,k,0), by MW=W+omega JW. Its antisymmetric part is the cross-product matrix of we divided by two. Therefore M12=k, M13=M31=0, and M32-M23=w. Trace zero leaves exactly two free real parameters eta,xi:

    M=[[1,k,0],
       [k,-1/2+eta,xi-w/2],
       [0,xi+w/2,-1/2-eta]].                     (2)

No admissible central matrix has been omitted.

## 3. Exact Hessian and Schur complement

Let K=(1+w^2)/4. Multiplication in (1) gives

    H=[[a,-3k,-kv],
       [-3k,K-eta^2-xi^2-3u+2vxi,-2veta],
       [-kv,-2veta,K-eta^2-xi^2-2vxi]].          (3)

For example, (M+M^2)12=k(3/2+eta) and [omega J,M]12=k(3/2-eta), so H12=-3k. In entry 13 the two terms involving xi-w/2 cancel, leaving H13=-kv. The 22 entry of M+M^2 is eta^2+xi^2+u-K; its commutator correction is 2u-2vxi. The 23 entry of M+M^2 is zero and its commutator correction is 2veta. These checks fix the signs of every variable term.

Since a>0, completing the square in the first coordinate shows H is semidefinite exactly when its lower Schur complement is semidefinite. Put y=(xi,-eta). That complement is

    (K-|y|^2)I-C+2v[[y1,y2],[y2,-y1]].           (4)

For a symmetric two-by-two matrix with trace tau and traceless coordinate h, the eigenvalues are tau/2 plus or minus |h|, directly from its characteristic polynomial. Thus (4) is semidefinite exactly when

    K>=|y|^2+tau/2+|h-2vy|.                      (5)

It is positive definite exactly when this inequality is strict.

## 4. Complete minimization

The number R is positive. If v=0, C11>0 and C22=0. If v is nonzero, C12=3uv/a is nonzero. Also tau>3u>6. For v=0, the minimum of |y|^2+|h-2vy| is R at y=0.

For v nonzero, put t=|y|. The reverse triangle inequality gives

    |h-2vy|>=|R-2|v|t|,

with equality when y=sign(v)t h/R. Hence it suffices to minimize t^2+|R-2|v|t| for t>=0. On the first interval 0<=t<=R/(2|v|), this is t^2+R-2|v|t, minimized at the clipped value min(|v|,R/(2|v|)). On the second interval it is t^2+2|v|t-R, which is strictly increasing. The exact minimum is therefore psi from Section 1, realized by

    y=v h/R   if R>=2v^2,
    y=h/(2v) if R<2v^2.                          (6)

The first formula includes v=0. They agree at the branch boundary. The second branch forces v nonzero, so no denominator vanishes. In the first branch psi>=v^2>=0; in the second branch it is positive. Thus K_min>3 and the radicand defining w_min is positive.

Combining (5)-(6) proves necessity and sufficiency of K>=K_min, equivalently w>=w_min. With the minimizing y, strict inequality gives positive definite H. At equality no other y can make (5) strict, so positive definiteness is impossible.

## 5. Full affine realization and exact endpoint examples

Choose y from (6), set eta=-y2 and xi=y1, and use (2)-(3). Let U(x)=Mx and P(x)=x.Hx/2 after transforming back by the oriented frame. Trace M is zero, curl U=we, and the entire profile equation reduces to M+M^2+omega[J,M]+H=0. Equation (3) proves this exactly, for every c. A semidefinite H gives a global quadratic pressure minimum.

For horizontal e, v=0, C=diag(3u+9u/a,0), so

    K_min=3u(u+1)/(u-2),
    w_min^2=12u(u+1)/(u-2)-1.

At omega=2, K_min=30 and w_min=sqrt(119). The Hessian [[2,-6,0],[-6,18,0],[0,0,30]] has eigenvalues 0,20,30. This confirms the semidefinite endpoint explicitly.

For k=2,v=4, one has u=4,a=2,tau=62,h=(-1,24),R=sqrt(577)<32. Formula (6) gives y=(-1/8,3), eta=-3, xi=-1/8. Then K_min=31+577/64=2561/64 and w_min=sqrt(2545)/4. Substitution in (3) gives

    H=[[2,-6,-8],[-6,18,24],[-8,24,32]]
      =2(1,-3,-4)(1,-3,-4)^T.

This is rank one. Increasing w with eta,xi fixed increases K, adding a positive multiple of the identity to the lower Schur complement, and makes H positive definite.

## 6. Scope and verification

Every displayed M has first diagonal entry 1 in the chosen frame. Hence M is nonzero and U grows along a ray, precluding decay. The classification permits strain and Hessian to vary; it does not prescribe all entries of H or higher derivatives. No pressure minimum has been deduced from the original decay-only assumptions. Strict local minima with singular Hessian are not excluded by the positive-definite threshold statement.

All six source sections and all six independent sections were fully read. The proof uses only the full equation, exact matrix algebra, a two-by-two eigenvalue formula and one real-variable minimization. No numerical optimization, checker execution or formal build is a dependency. The existing comparison and its precise wording qualification are recorded in Section 7; no new client or agent was invoked.

## 7. Existing comparison and a singularity wording correction

The complete coordinator comparison of 2026-11-04T02:10Z and all eighteen supplementary checks were read, not rerun. The first four mathematical steps and both endpoint examples agree with Sections 2-5. Random samples in the comparison log are not a proof of the minimum; the exact one-variable minimization in Section 4 is the proof. Source8827e39a was the unchanged submission at that comparison; the later source revision is recorded below.

One sentence at the end of comparison item 4 needs a qualifier. At K=K_min it says that H is singular for every y. The valid statement is that every positive semidefinite admissible H at this threshold is singular; equivalently no choice of y makes H positive definite. Without the semidefinite qualifier the sentence is false.

Indeed, take k=2, v=0, u=4, a=2 and w=sqrt(119), so K=K_min=30. Choose eta=1, xi=0. Formula (3) gives

    H=[[2,-6,0],[-6,17,0],[0,0,29]],
    det H=(34-36)29=-58.

This H is nonsingular and indefinite. It is the Hessian of the full affine profile obtained from (2), but it has no pressure minimum. The literal sentence is therefore refuted outside the pressure-minimum class. The local classification itself already has the required semidefinite hypothesis and is unaffected.

To prove the corrected statement, at K=K_min every y has the smallest Schur eigenvalue at most zero. If H is positive semidefinite, that eigenvalue is also nonnegative and hence zero. The positive pivot a then shows H is singular. This is a complete proof, not an appeal to the supplementary samples. The correction is sent through the existing comparison files; no new client or agent is used.

## 8. Corrected comparison and source revision

The coordinator's revision of 2026-11-04T02:13Z now states exactly that no y gives a positive definite H at the endpoint and that every positive semidefinite endpoint H is singular. The complete two-hunk comparison diff and the full revised comparison were read. Its added paragraph reproduces the determinant -58 counterexample and the corrected Schur argument. This resolves the comparison defect A2761 without changing the confirmed classification A2760.

The complete source diff from 8827e39a to b5d4613d316d8cd5bfe1eedd070e009638b57d0ea1c4782fe1816d2110388bba was also read. It changes the status line and final verification paragraph and adds a seventh section recording the existing comparisons and verdicts. No statement, matrix, hypothesis or proof step changes. The original and revised submissions and both comparison versions are retained in verification.
