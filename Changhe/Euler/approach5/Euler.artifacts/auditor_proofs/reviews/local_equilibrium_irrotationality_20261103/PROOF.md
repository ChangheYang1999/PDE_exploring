# An expanding carrier equilibrium has an irrotational neighborhood

Status: CONFIRMED at the exact scope below by A473, 2026-11-03T04:42:53.296940+00:00. The proof was independently reconstructed and fully postread. No global nonexistence conclusion follows.

## 1. Exact local statement

Let V be an open neighborhood of p in R^n, let B in C1(V;R^n) satisfy B(p)=0, and let W in C0(V;R^n). Fix kappa>0. Suppose that, for every backward trajectory segment contained in V, the C1 local flow Psi of -B satisfies the Cauchy law

    W(Psi_t x)=exp(kappa t) D Psi_t(x) W(x).            (1)

If every eigenvalue of N=DB(p), counted over C, has real part strictly between0 and kappa, then W vanishes on a neighborhood of p. The neighborhood may depend on N, B and kappa. No completeness assumption is imposed on the surrounding flow; it will be proved for the trapped trajectories used in the argument.

For the Euler corollary, let U in C2(V;R3), P in C1(V) solve the full rotating incompressible profile equation

    div U=0, (1-c)U+(B.grad)U+omega JU+grad P=0,
    B(y)=(cI-omega J)y+U(y), W=curl U,
    0<c<1/2, omega in R.

At any carrier equilibrium p, if every eigenvalue of DB(p) has positive real part, W vanishes near p. Consequently every carrier equilibrium p in the relative closure in V of {W!=0} satisfies

    min Re spec DB(p)<=0.                              (2)

This includes irrotational equilibria with DW(p)=0 and does not require p=0. It gives no positive lower bound for the backward top exponent and no upper bound for it.

## 2. An adapted inner product, with both bounds at once

Let m=min Re spec N and M=max Re spec N, so0<m<=M<kappa. There is a real inner product <.,.>_* and constants0<beta<gamma<kappa such that

    beta |v|_*^2<=<v,Nv>_*<=gamma |v|_*^2             (3)

for every real v. Here is a finite-dimensional construction, including nonnormal and complex blocks. Put N in real Jordan form. A real eigenvalue contributes scalar diagonal blocks; a conjugate pair contributes two-by-two blocks alpha I+theta J_2, whose symmetric part is alpha I. Scale successive elements of each Jordan chain by1,epsilon,epsilon^2,..., using the same scale for both coordinates of a complex block. After conjugation the nilpotent off-diagonal part has norm tending to zero with epsilon. The block-diagonal symmetric part has eigenvalues equal to the real parts of the original eigenvalues. Choose epsilon so the nilpotent symmetric perturbation has norm less than

    delta=min(m/2,(kappa-M)/2).

Pull back the Euclidean inner product by this real change of basis. This gives(3) with beta=m/2 and gamma=(M+kappa)/2, after taking a smaller perturbation if necessary. No diagonalizability or common Euclidean numerical-range bound is assumed. The chosen inner product is fixed in space.

By continuity of DB, choose a closed *_ball Q={|y-p|_*<=r} contained in V, and numbers beta'>0,gamma'<kappa, so that every y in Q satisfies

    beta' |v|_*^2<=<v,DB(y)v>_*<=gamma' |v|_*^2.     (4)

For example choose beta'=beta/2 and gamma'=(gamma+kappa)/2 and then decrease r. Norm equivalence makes continuity of DB equally valid in the adapted norm.

## 3. Trapping, completeness and the lower singular-value estimate

Write z=y-p. Since B(p)=0 and the line segment from p to y lies in Q,

    B(p+z)=integral_0^1 DB(p+s z)z ds,
    <z,B(p+z)>_*>=beta' |z|_*^2.                     (5)

Hence a backward trajectory starting in Q satisfies

    d|Psi_t x-p|_*^2/dt<=-2beta' |Psi_t x-p|_*^2.

The field -B points strictly into Q at its boundary. Local uniqueness and the inequality show positive invariance. Since Q is compactly contained in the open C1 domain V, a trajectory in Q cannot cease to exist at a finite positive time: boundedness of B makes it Cauchy at such an endpoint, and local existence at the limiting point extends it. Thus every such backward trajectory exists for all t>=0 and stays in Q.

For v(t)=D Psi_t(x)v0, the local variational equation and(4) give

    d|v(t)|_*^2/dt=-2<v(t),DB(Psi_t x)v(t)>_*
                  >=-2gamma' |v(t)|_*^2.

Integration yields the lower bound

    |D Psi_t(x)v0|_*>=exp(-gamma't)|v0|_*.            (6)

This is a lower singular-value bound, not an upper operator-norm bound. It holds for every vector, so no invariant-eigenline choice for W is needed.

Equation(1) and(6) imply

    |W(Psi_t x)|_*>=exp((kappa-gamma')t)|W(x)|_*.

The left side is bounded on the compact set Q, since W is continuous. The exponent is strictly positive. Letting t increase proves W(x)=0 for each x in Q, and in particular on its interior. All infinite-time uses follow the completeness argument.

## 4. Euler trace reduction and scope

For a C2 rotating Euler profile, the usual curl equation gives(1) on every local trajectory segment, with kappa=1+c. Also

    tr DB(p)=3c,

because div U=0 and J is skew. If all three eigenvalue real parts are positive, their sum is3c, so each is strictly less than3c. Since0<c<1/2,

    3c<1+c=kappa.

Thus the spectral-strip hypothesis of Section1 follows solely from positivity of the real parts. Its conclusion proves the Euler corollary. Taking the contrapositive proves(2) at points in the relative vortical closure.

The argument is local, has no boundary integral and uses no pressure normalization. Arbitrary omega is allowed; the adapted norm and ball may depend on it. Neither global sublinearity nor global zero helicity nor a compact invariant probability is required. At a boundary eigenvalue0 or kappa the general lemma makes no assertion. The trace corollary rules out a forward hyperbolic source in the vortical closure, but permits saddles and nonhyperbolic equilibria. It does not exclude the large backward exponents remaining in A471.

## 5. Dependencies and evidence

The general lemma is optional O1 in the pinned configured-model coordinator review. Sections2-3 supply its omitted adapted-norm and completeness details. Section4 is the additional elementary trace consequence. This is independent of A413 and A472; A472's special DU(0)=0 argument is one direct Euclidean instance.

No computation is needed or used. The actual-model evidence for the existing collaboration is configuration, the primary model, not independent provider attestation. No new model client is used.
