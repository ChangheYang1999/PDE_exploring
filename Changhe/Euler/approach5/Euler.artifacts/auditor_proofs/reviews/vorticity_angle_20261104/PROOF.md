# Independent audit of every allowed central vorticity direction

Status: A2758-A2759 CONFIRMED after independent reconstruction and existing coordinator comparison. This is the local LIT326 claim, not decay-only nonexistence.

## 1. Exact statement

Let Jx=e3 cross x and let c,omega be real. On a neighborhood of zero let U be C2 and P be C1, with

    div U=0,
    (1-c)U+DU[(cI-omega J)x+U]+omega JU+grad P=0.

Assume U(0)=0 and W=curl U(0) is nonzero. If the central pressure Hessian is positive semidefinite, then

    omega^2 |JW|^2>2|W|^2.                         (1)

The Hessian exists as a consequence of the equation. A local minimum of P implies the assumed semidefiniteness. Conversely, for every unit vector e satisfying omega^2|Je|^2>2, there is a global affine full profile with nonzero vorticity in direction e and positive definite pressure Hessian, for every real c. Its magnitude is chosen by the construction. No affine example decays.

## 2. Necessity from the full equation

The right side defining grad P is C1, hence P is C2. Write M=DU(0) and H=D2P(0). Differentiation at zero gives

    H=-M-M^2-omega[J,M],  tr M=0.                 (2)

Here the derivative of DU times the carrier vanishes because the carrier is zero at zero. The terms (1-c)M+cM combine into M. Taking curl first and then evaluating at zero gives

    MW=W+omega JW.                                (3)

Apply (2) to W and use (3). The terms omega M JW cancel, giving

    HW=-2W-3omega JW-omega^2 J^2W.                (4)

Since J is skew, W.HW=-2|W|^2+omega^2|JW|^2. Positive semidefiniteness gives the weak inequality in (1). At equality, diagonalizing the symmetric H gives HW=0. Since W is nonzero, equality also gives omega JW nonzero. But (JW).HW=-3omega|JW|^2 is nonzero: JW is orthogonal to W and J^2W. This contradiction proves strictness. The argument uses no sign of c and no global flow.

## 3. Frame and full affine equation

Choose an allowed e. Put z=e.e3, s=|Je|>0, f=Je/s and g=e cross f. Then (e,f,g) is oriented orthonormal and e3=z e+s g. In this basis

    J=[[0,-s,0],[s,0,-z],[0,z,0]].

Set k=omega s, v=omega z, u=k^2>2, a=u-2 and d=u v^2. Define

    K=3u+1+(9u+d)/a,  w=2 sqrt(K-1/4),
    M=[[1,k,0],[k,-1/2,-w/2],[0,w/2,-1/2]],
    H=[[a,-3k,-kv],[-3k,K-3u,0],[-kv,0,K]].       (5)

The radicand is positive since K>3u+1>7. The trace of M is zero; its antisymmetric part is the cross-product matrix of we divided by two. Thus curl(Mx)=we after transforming back to the original coordinates.

For U=Mx the full profile equation reduces, exactly, to

    M+M^2+omega[J,M]+H=0.                         (6)

Multiplying the matrices gives the first row of -M-M^2-omega[J,M] as (a,-3k,-kv), the lower diagonal entries K-3u and K, and the lower off-diagonal entry zero. Thus (6) holds. All c-dependent terms cancel; no higher jet or nonlinear residual remains for an affine field.

## 4. Positive definiteness

The first leading principal minor is a>0. The second is

    a(K-3u)-9u=a+d>0.

Since (kv)^2=d, determinant expansion gives

    det H=K[a(K-3u)-9u]-d(K-3u)
         =aK+3ud>0.

Sylvester's criterion gives H positive definite. Therefore P=x.Hx/2 has its unique global minimum at zero. This is a complete full-profile realization of the permitted direction, not merely a Poisson or first-jet example.

## 5. Exact examples and scope

For horizontal e, z=0, this reduces to the LIT324 family. For omega=2 and z=1/2, one has s=sqrt(3)/2, u=3, a=1, d=3, K=40, w=sqrt(159). The pressure matrix is

    [[1,-3sqrt(3),-sqrt(3)],[-3sqrt(3),31,0],[-sqrt(3),0,40]],

with leading minors 1,4,67. These values follow by substitution in the exact formulas. No numerical computation is needed.

For |omega|<=sqrt(2) there is no allowed direction. For larger |omega|, the condition is exactly sin(angle(e,e3))>sqrt(2)/|omega|. Every M has first diagonal entry 1 in the displayed frame, so M is nonzero. On any ray x with Mx nonzero, |U(tx)|=t|Mx| tends to infinity. None of these profiles is a decaying counterexample. The necessity of a central pressure minimum for arbitrary decaying profiles is not established.

## 6. Dependencies and verification

The proof uses the full equation, differentiation at its zero carrier, elementary cross-product identities, matrix multiplication and Sylvester's criterion. It does not assume LIT324 or any other pending verdict. All six source sections and all six independent sections were read. The supplementary checker has not been run or used as a proof dependency. The existing comparison is completed in Section 7; no new client or agent was invoked.

## 7. Existing comparison and conclusion

The complete coordinator comparison of 2026-11-04T02:10Z and all fifteen lines of its supplementary checks were read, not rerun. Its six mathematical items agree with Sections 1-5 above. The three wording points are valid: the earlier result has since been confirmed, the true identity M^T W=MW is not needed in the substitution deriving HW, and the report must keep the central hypotheses and growing-example scope. The source b33a3b63 was the unchanged submission at that comparison.

The strict angular necessity and every-direction affine realization are confirmed. These do not derive a central pressure minimum from decay and do not exclude a decaying profile at larger rotation. Existing configured model comparison was through files; its provider execution is not independently attested.

## 8. Source revision after confirmation

The complete three-hunk source diff from b33a3b63 to a8df043c8c045d2b1d6e7d8e2d38732e1cc7b8e96473d18799a009d9dd66f70e was read. It updates status and verification text, removes the true unused identity before the unchanged formula for HW, and adds a seventh section recording the existing comparisons. The formula for HW was already derived directly from the two preceding identities in Section 2 above; deleting the unused observation leaves that derivation intact. No hypothesis, conclusion, matrix or example changes. Both source versions and the complete diff are retained in verification.
