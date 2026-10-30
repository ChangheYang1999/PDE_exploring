# What a compact correction cannot repair in the low energy

## 1. Statement

Let L=V.D-1+U[.].D rho be the fixed-c linearized S1 operator, V=cX+U[rho], and let w=(1+r^2/R^2)^(-a/2), with 0<=a<2 and R>0. The value a=0 means the unweighted space. Assume the regularity, decay, canonical velocity, symmetry and compact-remainder hypotheses proved in ../weighted_signed_compact/PROOF.md. Define

    b=-V.D log w,
    M(X)=[[b-rho_y,rho_x/2],[rho_x/2,b]],
    lambda(X)=b+(sqrt(rho_x^2+rho_y^2)-rho_y)/2,
    Lambda=ess sup_X lambda(X).

In particular M is bounded and continuous and has the reflection covariance associated with the S1 space of real functions even in x and odd in y. Write L_w=w L w^-1 on its compact smooth S1 core. Let C be any compact operator on S1 L2. If a real beta satisfies

    Re <(L_w+C)phi,phi> <= -beta ||phi||_2^2                 (1)

on that core, then necessarily

    beta <= c+1-Lambda.                                    (2)

The same conclusion holds if the core in (1) is restricted to c[w^-1 phi]=0, where c[h]=partial_y U2[h](0) is the canonical strain. It also holds after imposing any finite collection of additional homogeneous constraints whose restrictions to compact sets away from the origin are continuous L2 functionals, provided their common kernel has the expected finite codimension there.

Consequently a point with lambda(X0)>c+1 rules out every positive contraction rate of the form (1), even after any finite-rank additive correction. A point with lambda(X0)>c-1 rules out rate beta=2. These are energy obstructions. They do not prove noninvertibility, spectral instability or failure of a semigroup estimate with a multiplicative constant greater than one. They do not exclude a change of principal norm or principal operator.

## 2. Proof of the high-frequency test

The signed decomposition gives, for real phi,

    Re <L_w phi,phi>=-(c+1)||phi||_2^2
       +integral (R1 phi,R2 phi) M(X) (R1 phi,R2 phi)^T dX
       +<K phi,phi>,                                      (3)

where K is compact and self-adjoint. The weighted compact theorem gives K=K_rho+D_R-K_b; for a=0 this reduces to K_rho. The local contact term is included in this identity.

We first establish a test on a small ball B away from the axes. Let chi be a real compact smooth cutoff in B, xi a real unit vector, and f_n=chi cos(n xi.X). Under the convention R_j has multiplier i eta_j/|eta|, Fourier translation and dominated convergence give

    ||R_j f_n+xi_j chi sin(n xi.X)||_2 -> 0.                (4)

Indeed for the positive-frequency packet chi exp(i n xi.X), its translated multiplier converges pointwise to i xi_j and is uniformly bounded. The negative-frequency packet converges to -i xi_j. Add the two packets. Riemann-Lebesgue then gives

    ||f_n||_2^2 -> (1/2) integral chi^2,
    integral (R f_n)^T M (R f_n)
        -> (1/2) integral chi^2 xi^T M xi.                  (5)

The sequence f_n converges weakly to zero.

Reflect this packet into the four disjoint images of B, with plus sign for x reflection and minus sign for y reflection. This produces a real compact smooth S1 function. The reflected frequency vector is the corresponding reflection of xi. The covariance M(SX)=S M(X)S for coordinate reflections S implies that each of the four packets has the same limiting quotient in (5). Formula (4) also shows that cross terms vanish: the leading oscillatory packets have disjoint supports and their L2 errors tend to zero. Normalize the resulting S1 function to unit norm.

Choose X0 off the axes and xi a unit eigenvector for the largest eigenvalue of M(X0). By continuity, choosing B sufficiently small makes the limiting principal quotient at least lambda(X0)-epsilon. Since the normalized packets converge weakly to zero, compactness implies ||K phi_n||_2+||C phi_n||_2 -> 0. Apply (1), use (3)-(5), and let n tend to infinity. This gives

    beta <= c+1-lambda(X0)+epsilon.

Let epsilon tend to zero and take the supremum over points off the axes. Continuity and the density of those points give (2), including when the supremum is only approached at infinity.

## 3. Normalization does not remove the test

All packets above are supported in a fixed compact set away from the origin. On such a set, the contact formula reduces to

    c[h]=(1/pi) integral sin(3 theta) h(X) r^-3 dX,

because h_y(0)=0. Thus c[w^-1 phi] is a continuous L2 functional of these packets. Weak convergence implies that it tends to zero. Choose one fixed compact smooth S1 function g supported away from the origin with c[w^-1 g]=1. Such a function exists because sin(3 theta)r^-3 is not identically zero in the S1 sector; take a nonnegative cutoff times that kernel and symmetrize.

Replace phi_n by phi_n-c[w^-1 phi_n]g and renormalize. The difference tends to zero in L2, and the strain constraint now holds exactly. The symmetric form on the right of (3) is bounded on L2. Its value therefore changes by o(1), irrespective of the large antisymmetric transport derivative of the packet. The compact correction changes by o(1) as well. This proves the normalized assertion without needing a high-norm bound on the correction.

For finitely many continuous local constraints, choose a finite-dimensional right inverse on their independent range and perform the same subtraction. Redundant constraints may be removed first. The correction is o(1) in L2, so the argument is unchanged. Compact support away from the origin already makes all local origin jets vanish.

## 4. Applications and limitations

For a=0, lambda is theta_X=(|D rho|-rho_y)/2. Thus the three independently confirmed witnesses in T4-046 show that the target rate2 cannot be recovered for candidates002,003,004 merely by replacing the Hilbert-Schmidt norm of the compact remainder by a sharper finite-rank calculation. Candidate002 and003 in fact have theta_X>c+1 and hence obstruct every positive unweighted L2 contraction rate of this form. Candidate004 only obstructs rates greater than c+1-0.879940161..., approximately1.93037905; it does not obstruct all positive rates.

For weighted state131, selected rational points will be evaluated using the independent polar field construction. A positive certified value lambda(X0)-(c+1) proves the corresponding energy obstruction, conditional only on the stated decomposition assumptions. No finite grid is used as an upper bound. A grid with positive sampled margins would give no success certificate.

The principal obstruction persists for compact additive changes to L_w. A finite-rank change of inner product requires separate control of the transport commutators and is not automatically covered unless its resulting symmetric correction is bounded and compact. General nonlocal symmetrizers, noncompact changes to the principal energy, and invertibility certificates that allow transient growth remain outside the theorem.

## 5. Verification and review status

This is a complete informal proof. It depends on the weighted signed compact decomposition, Fourier translation, dominated convergence, compactness and elementary finite-dimensional eigenvectors. No numerical result is needed for (2). Selected point computations will be placed in verification/. This new T4 result remains CLAIMED pending independent Opus review. No Lean or other proof assistant is run.
