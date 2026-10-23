# Canonical compactness, closed strain caps, and a failure of strong strain convergence

Date: 2026-10-20. Status: independent proof complete; supporting checks are recorded separately. These are statements about convergence of canonical pairs. Only the final conditional compactness corollary uses the exact profile equation. No compactness or global strain upper bound is asserted for the numerical iterates.

## 1. Definitions and statements

Write ell>1, D=ell-1, A=2ell-1. The canonical inverse of a smooth even-x/odd-y density is the unique sublinear velocity U with div U=0 and curl U=-rho_x, with U1 odd in x/even in y and U2 even in x/odd in y. Its stream has both odd parities. Let S=(DU+DU^T)/2 and R=(ell X+U).grad rho-rho. All supremum norms of matrices below use their Euclidean operator norm.

Suppose rho_n and rho are smooth densities with these parities, rho_n->rho in C1 on every compact set, and there are COMMON constants C and 0<gamma<1 such that

    |rho_n(X)|+(1+r)|grad rho_n(X)| <= C(1+r)^gamma.       (1)

The same bound then holds for rho. Let U_n,U be their canonical inverses.

(i) U_n->U uniformly on each compact set. If, on every compact set, the gradients also have a common Dini modulus, then DU_n->DU uniformly on compact sets. A common Dini modulus means a nondecreasing function omega_K with omega_K(s)->0 and integral_0^1 omega_K(s)ds/s<infinity which bounds every |grad rho_n(X)-grad rho_n(Y)| for X,Y in the compact set K with |X-Y|<=s.

(ii) Even without the Dini assumption, a global cap is closed: if ell_n->ell and eps_n->0 with

    sup_X ||S_n(X)|| <= ell_n-1+eps_n,                   (2)

then sup_X||S(X)||<=ell-1. No uniform convergence of DU_n is needed for this implication. If additionally R_n->0 locally uniformly, then rho,U solve exact transport. Also a_n=rho_(n),y(0)->a=rho_y(0).

(iii) Neither C1 convergence, common growth, fixed nonzero a, nor the exact primary center identity alone guarantees strong strain convergence. For every fixed ell>1 there are smooth canonical nonprofiles rho_n converging to a smooth rho_0 in GLOBAL C1, all satisfying (1),

    a_n=a=4D, psi_(n),xy(0)=-D,

but ||S_n(P)||->infinity at the fixed point P=(3,3). These pairs have the same density Taylor series at zero and Gaussian density tails. They are not counterexamples to (ii), because their global strain suprema are unbounded.

## 2. Continuity of the canonical velocity

The independently proved inverse formula is

    U(X)=-rho(X)e2/2 + PV int K(X-Y)rho(Y)dY,
    K(Z)=(-z1*z2/pi, (z1^2-z2^2)/(2pi))/|Z|^4.            (3)

Its exterior integral uses centered circular truncation. K has zero angular mean. Near X, subtract rho(X); the local integrand is bounded by C_K/|X-Y|. For X in a fixed compact set and |Y|>2|X|, central oddness permits replacement of K(X-Y) by K(X-Y)-K(-Y). This difference is at most C|X||Y|^-3. Therefore (1) bounds the exterior tail beyond radius T uniformly by C_K T^(gamma-1).

On a fixed bounded region, C1 convergence controls the contact term, the locally subtracted singular integral, and the remaining nonsingular integral uniformly for X in the chosen compact set. Given any error tolerance, first choose T so the common tail is small and then use C1 convergence on a ball containing that region. This proves local uniform convergence of U_n. It uses a common sublinear growth bound, not just individual membership in the admissible class.

For derivatives, distributional differentiation and integration by parts give

    partial_j U=-partial_j rho*e2/2 + PV int K(X-Y)partial_j rho(Y)dY.   (4)

The exterior boundary term tends to zero: its size is O(T^(gamma-1)). The tail in (4) is absolutely bounded by C integral_T^infinity s^(gamma-2)ds. At the local singularity subtract partial_j rho(X). A common Dini modulus bounds the inner contribution within distance delta by C integral_0^delta omega_K(s)ds/s, uniformly in n. The finite annulus converges by C1 convergence. Taking the inner and outer cutoffs first, then n, proves the derivative assertion. This also justifies the classical formula at the smooth limit. A common local C1,alpha bound for any alpha>0 is a sufficient special case of this Dini condition.

## 3. Passing a global cap by weak convergence

By (i), U_n->U locally uniformly, so S_n->S in distributions. Let v be any fixed unit vector and let phi>=0 be a smooth compactly supported test function. Assumption (2) gives both inequalities

    -(ell_n-1+eps_n) int phi <= int phi v^T S_n v
                              <= (ell_n-1+eps_n) int phi.

The middle integral equals an integral against U_n after one integration by parts, so it converges. Passing to the limit and using continuity of the smooth matrix S gives

    |v^T S(X)v|<=ell-1 for every X.

One may first use a countable dense collection of unit vectors and then continuity in v. The spectral characterization of a symmetric operator norm proves the cap. This argument is local in the test function but uses a genuine global upper bound for every S_n. Finite samples, even on larger and denser grids, do not supply (2) without a separate bound on the unexamined points.

The transport limit follows directly from ell_n->ell, local uniform U_n convergence and C1 density convergence. In particular local residual convergence cannot be inferred from a normalized residual without controlling its denominators. If a!=0, differentiation of the exact limiting equation gives ell+psi_xy(0)=1. The proof of the cap does not require first passing numerical center strains through a singular integral.

## 4. A smooth log-annulus with exact strain

Choose a fixed nonnegative even C-infinity function eta supported in [-b,b], b=1/4, with integral eta=1. For example normalize exp[-1/(1-(s/b)^2)] on |s|<b and set it to zero elsewhere. For L>=1 define

    f_L(t)=int_(-L)^0 eta(t-s)ds,
    q_L(r,theta)=r sin(3theta) f_L(log(r/R0)), R0=1/8,

with q_L=0 at the origin. The support satisfies

    R0 exp(-L-b) <= r <= R0 exp(b).

Thus q_L is smooth, vanishes on a neighborhood of zero, and is supported in a fixed small disc. Its parities are even in x and odd in y. The convolution definition gives 0<=f_L<=1 and |f_L'|<=2||eta||_infinity, independent of L. In polar coordinates,

    partial_r q_L=sin(3theta)(f_L+f_L'),
    r^-1 partial_theta q_L=3cos(3theta)f_L.

Consequently the global C1 norm of q_L and its L1 norm are bounded independently of L.

Since its center slope is zero, the canonical angular strain formula gives

    c[q_L]=int_0^infinity b3(r)r^-2 dr
          =int_R f_L(t)dt=L, b3(r)=r f_L(log(r/R0)).      (5)

Tonelli proves the last equality exactly. An independent derivation from c=(1/pi)int xy*r^-4*q_x dX gives

    (1/pi)int_0^(2pi) cos(theta)sin(theta)q_x dtheta
           =f_L+f_L'/4,

and the integral of f_L' is zero. No conditionally convergent integral is used: each q_L vanishes near both radial endpoints.

## 5. Reflection, center correction, and failure of strain convergence

Let epsilon_n=1/n, L_n=n^2, and define

    F_n(x,y)=epsilon_n sum_(sigma,tau in {+1,-1})
                          tau q_(L_n)(sigma x-3,tau y-3).

Its four supports are disjoint fixed small discs away from zero. Reflection proves the required global parities. The uniform estimates from Section4 give ||F_n||_C1<=C epsilon_n. Since the support stays away from zero, the center-strain kernel and its derivatives there are nonsingular, so

    d_n=c[F_n]=O(epsilon_n).                             (6)

Choose the fixed smooth annular density

    J(r,theta)=r sin(3theta) eta(log r).

It vanishes near zero, has the required parities, and c[J]=int eta=1 exactly. Its support is disjoint from the four patch discs. Put

    rho_0=4D y exp(-r^2),
    rho_n=rho_0+F_n-d_n J.                              (7)

The correction preserves global C1 convergence and makes the center strain exactly c[rho_n]=c[rho_0]=-D. The radial sine-one Gaussian has c[rho_0]=-rho_(0),y(0)/4=-D. Both perturbations vanish on a fixed neighborhood of zero, so every density Taylor coefficient agrees with rho_0, including a=4D. The common support of the perturbations and the Gaussian base give (1) for every fixed gamma in (0,1), with a uniform C.

At P=(3,3), the matching patch contributes epsilon_n L_n=n to partial_y U2[F_n](P), by translation invariance and (5). Every other patch is separated from P by a fixed distance. The derivative kernel is smooth there and their L1 norms are O(epsilon_n), so their contributions are O(epsilon_n). The correction d_n J has the same O(epsilon_n) contribution at P. Hence

    partial_y U2[rho_n](P)=partial_y U2[rho_0](P)+n+O(1/n).   (8)

Since this derivative is a diagonal entry of S_n, (8) implies its operator norm diverges. In contrast U_n->U_0 locally uniformly by Section2, and in fact globally uniformly here: the compactly supported perturbations have C1 norm O(epsilon_n), so the local subtraction in (3), the nonsingular bounded region and the exterior decay each give O(epsilon_n) uniformly in X.

These fields are explicitly nonprofiles. Their common cubic density coefficients are b_cub=e_cub=-4D. Exact primary transport and the Poisson equation would require

    6e_cub=(a-2A)b_cub.

Here a-2A=-2, so the defect is 8b_cub=-32D!=0. This contradiction is independent of the higher harmonic Taylor coefficients generated by the distant patches. The example concerns topology of the inverse, not a solution family.

## 6. A conditional compactness gap for near-capped residual sequences

Fix gamma,C as in (1), constants ell_min>1, ell_max<infinity, a_min>0 and eta0>0, and uniform bounds M_(k,j) on every C^k norm of rho on the closed ball B_j, for all integers k,j>=1. Consider smooth canonical pairs with ell in [ell_min,ell_max], |rho_y(0)|>=a_min, and

    rho_y(0) <= 2(2ell-1)-eta0.                          (9)

No separate sign of rho_y(0) is assumed. Define the bounded local residual metric

    d_R=sum_(j=1)^infinity 2^-j min(1,||R||_(C0(B_j))),

and the excess E_S=max(0,sup_X||S||-(ell-1)), allowing infinity. There exists a positive number delta_* depending on this class of bounds such that every such pair has

    d_R+E_S>=delta_*.                                   (10)

This is a qualitative compactness assertion and supplies no computable numerical value for delta_*.

Proof. If (10) failed, choose a sequence with both terms tending to zero. Local derivative bounds and diagonal Arzela-Ascoli extraction give C-infinity convergence on every compact set to a smooth rho. Extract also a convergent ell. Bounds (1), (9) and |a|>=a_min pass to the limit. The metric d_R forces R_n->0 locally uniformly, since each of its fixed nonnegative summands tends to zero. Sections2-3 give the canonical exact limiting profile and its global cap. The independently proved theorem in ../strain_cap_flat_exclusion/PROOF.md, using ../all_degree_strain_cap/PROOF.md, then forces a>=2(2ell-1). This contradicts (9). The contradiction proves (10).

The local derivative bounds are substantive hypotheses. They can fail through origin layers, angular oscillations or loss of regularity, even when a few fitted coefficients look stable. Numerical samples of S are lower estimates of its supremum and do not give E_S. Residuals restricted to finite boxes do not directly give d_R. To apply the argument modulo the genuine spatial dilation one needs representatives satisfying the stated common bounds; no arbitrary normalization of a or ell is allowed. Therefore (10) does not exclude the current archived iterates from approximating some uncapped profile, and it gives no principal YES or NO endpoint.

## Dependencies and verification

The canonical kernel and strain identity are proved independently in ../inverse/PROOF.md and ../origin/PROOF.md. The cap exclusion used only in Section6 is result68. The new arguments here are the convergence/topology statements, weak closure of a global cap, the exact-center-preserving counterexample, and the explicit compactness corollary. Supporting checker outputs belong in verification/; finite quadrature does not prove the unbounded sequence or compactness theorem.
