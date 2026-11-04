# Scalar pressure-vorticity criteria for derivative decay

Status: CONFIRMED in A504 at the exact hypotheses below. Criterion (II) needs only a finite bound, by the already confirmed A492.

## 1. Exact statement

Let U in C2(R3;R3) be bounded, P in C1(R3), 0<c<1 and omega any finite real number. Suppose

    div U=0,
    (1-c)U+(DU)((cI-omega J)y+U)+omega JU+grad P=0.

Put G=DU, W=curl U, S=(G+G^T)/2, and t_+=max(t,0). The following separate hypotheses each imply DU->0 uniformly at infinity:

    (I) limsup_(|y|->infinity)(|W|^2/2-Delta P)<3/2;
    (II) limsup_(|y|->infinity)[sqrt((-Delta P)_+/2)+|W|^2/4]<infinity.

In particular the original criterion with the expression in (II) strictly below one holds. Unlike that original normal-form proof, (II) here imposes no numerical smallness. Constants in downstream decay bounds may depend on the fixed profile and on c,omega. No velocity decay, pressure normalization, symmetry or helicity assumption is needed beyond bounded U.

## 2. Exact algebra and regularity

The actual equation expresses grad P as a C1 function, hence P is C2. Taking divergence, the two skew rotation terms cancel and gives -Delta P=tr(G^2). Write G=S+K with K skew. Since div U=0, tr S=0. The curl convention implies |K|_F^2=|W|^2/2, and tr(SK)=0. Therefore

    |S|_F^2=|W|^2/2-Delta P,
    |G|_F^2=|W|^2-Delta P.                                 (1)

These are pointwise identities for the actual pressure.

## 3. Proof under (I)

Let mu=lambda_max(S). Trace zero implies mu>=0. The other two eigenvalues sum to -mu, so their squared sum is at least mu^2/2. Hence

    mu^2 <= (2/3)|S|_F^2.

Under (I), choose q<3/2 which bounds |S|_F^2 outside a sufficiently large ball. Then limsup mu<=sqrt(2q/3)<1. The confirmed A476 applies directly to bounded U and gives DU->0. No preliminary bound on full G is required for that theorem.

The constant 3/2 is sharp for this algebraic eigenvalue inequality: S=diag(1,-1/2,-1/2) has mu=1 and |S|_F^2=3/2. This is not a claim of sharpness among global Euler profiles and does not produce a nonzero borderline profile.

## 4. Proof under (II)

Choose any finite K which bounds the nonnegative expression in (II) outside a large ball. Then

    |W|^2 <= 4K, (-Delta P)_+ <= 2K^2.

The second identity in (1) therefore gives

    |G|_F^2 <= |W|^2+(-Delta P)_+ <= 4K+2K^2.

Continuity of G bounds the remaining compact ball. Thus both U and DU are bounded, and the confirmed A492 gives DU->0. This proof bypasses the original auxiliary normal form entirely. The stronger finite-bound conclusion is a direct corollary of A492, whose focused configured-model review has already been read and checked.

Conversely DU->0 makes W->0 and Delta P=-tr(G^2)->0, so the expression in (II) tends to zero. Thus, at the stated exact-profile scope, finiteness of its tail limsup is equivalent to bounded DU and to derivative decay. The original strict threshold one is not a sharp threshold for this PDE implication. Its source's claimed sharpness is only for a particular matrix inequality and should remain explicitly so.

## 5. Consequences and limits

Under either criterion the confirmed A476/A492 give Dini derivative decay and DU=O(1/r). If additionally U(R .)->0 distributionally and 1/3<c<1, A477 gives DU=O(r^-1/c). These are downstream conclusions, not hypotheses used in proving boundedness.

The original source's two special cases, W->0 with liminf Delta P>-2, or Delta P->0 with limsup |W|<2, satisfy (II). Its enlarged form even permits any finite corresponding bounds that keep |W| and (-Delta P)_+ bounded. Neither criterion follows from U->0 alone in this proof.

The full source and complete configured-model coordinator check were read. The originating model's own model consultation failed; it is not counted as a successful review. No computation or formalization is used. The unrelated approximate profile in the same source has its own audit and is not an exact solution.
