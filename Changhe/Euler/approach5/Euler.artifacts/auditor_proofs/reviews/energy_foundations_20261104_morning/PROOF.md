# Classical pressure normalization and energy growth, morning recheck

## 1. Exact statement

Fix 0<c<1 and a finite real omega. Let J(x_1,x_2,z)=(-x_2,x_1,0), A=cI-omega J and B=Ay+U. Suppose U in C1(R3;R3) and P in C1(R3) solve

    (1-c)U+(B.grad)U+omega JU+grad P=0,   div U=0.

Assume Hb: U is bounded and U(R.) tends to zero in distributions on compact sets as R tends to infinity. Put M=sup|U|, E(R)=integral_(B_R)|U|^2 and alpha=5-2/c. Then:

1. If 0<c<2/5, U=0 and P is constant.
2. If c=2/5, U belongs to L2 and integral_(|y|>R)|U|^2=O(R^-5).
3. If 2/5<c<1, a finite L>=0 exists with E(R)=L R^alpha+O(R^(alpha-1)). The coefficient L is positive unless U=0. If U also decays uniformly, the error is o(R^(alpha-1)).

Constants in the energy estimates can depend on c, M and E(4), and need not depend on omega. Uniform decay implies Hb. Neither pressure normalization, global derivative bounds, vorticity integrability nor symmetry is a premise. The proof below fixes the actual pressure gradient first and justifies all limits at infinity. It concerns classical profiles only. No characteristic flow is used.

## 2. The canonical gradient and the harmonic remainder

Let T_ij be the multiplier -xi_i xi_j/|xi|^2. Its kernel is the local term -delta_ij delta_0/3 plus the principal-value kernel

    K_ij(x)=(3x_i x_j-delta_ij|x|^2)/(4pi|x|^5).

For a compact smooth phi, T_ij partial_k phi is in L1. On a fixed compact set this follows from its L2 multiplier bound and Cauchy-Schwarz. Outside a ball containing the test support, subtract the leading K_ij(x) integral partial_k phi=0. The derivative bound |grad K_ij(x)|<=C|x|^-4 gives an integrable tail. These estimates also show continuity in the compact-test topology.

Set F_ij=U_iU_j and define the distribution G_k by

    <G_k,phi>=-sum_ij integral F_ij T_ij(partial_k phi).

Boundedness of F makes the definition meaningful. The multiplier identity gives Delta G_k=-partial_k partial_i partial_j F_ij. Divergence of full momentum gives -Delta P=partial_i partial_j F_ij: the contraction from differentiating Ay cancels that from omega JU, and divergence freedom removes the other linear terms. For C1 fields the nonlinear identity is obtained by local smoothing and passage to distributions. Hence H_k=partial_k P-G_k is a harmonic distribution, and is represented by a smooth harmonic function.

Let U_R(z)=U(Rz). Testing the evaluated, original pressure gradient gives

    integral grad P(Rz)phi(z)dz
      =integral U_R[(4c-1)phi+(Az).grad phi]
       -omega integral JU_R phi
       +R^-1 integral U_R[U_R.grad phi].                 (1)

Hb makes the linear terms tend to zero. The last term is O(M^2/R). The same conclusion holds for phi(z-x/R), with x fixed: their supports lie in one fixed compact set, and their required derivatives converge uniformly to those of phi. Boundedness of U_R controls the changing-test error.

The homogeneity of T_ij gives

    <G_k(R.),phi>=-R^-1 sum_ij integral F_ij(Rz) T_ij(partial_k phi)(z)dz.

Its absolute value is at most C_phi M^2/R. The bound is unchanged for translated tests because translation preserves the L1 norm of T_ij partial_k phi. Choose radial phi of integral one. The harmonic mean-value property, integrated in radius against phi, gives

    H_k(x)=integral H_k(x+Rz)phi(z)dz.

Both terms on the right tend to zero by (1) and the bound for G. This identity is valid in distributions as well as for the smooth harmonic representative. Thus H=0 and grad P=G. No polynomial-growth assumption on P and no false L-infinity bound for T_ij was used.

## 3. Annular pressure and the exact radial identity

For R>=2 split F into its restrictions to |z|<R/2, R/2<=|z|<4R and |z|>=4R. Write the corresponding pressures as Pi_inner, Pi_middle and

    Pi_outer(x)=sum_ij integral_(|z|>=4R)
                  [K_ij(x-z)-K_ij(-z)]F_ij(z)dz,  |x|<2R.

The first two are the L2 multiplier applied to compactly supported data. The last integral and its distributional gradient are well defined by the kernel difference estimate. Equality of gradients from Section 2 implies

    P=p_R+Pi_inner+Pi_middle+Pi_outer on B_(2R)

for a constant p_R, with equality almost everywhere sufficient for all following annular integrals. Put epsilon(R)=sup_(|y|>=R)|U(y)| and I(R)=integral_(|z|>=4R)|z|^-4|U(z)|^2. The multiplier norm, separation of supports and the derivative kernel bound give

    ||Pi_middle||2<=epsilon(R/2) E(4R)^(1/2),
    sup_(R<|x|<2R)|Pi_inner(x)|<=C R^-3 E(R/2),
    sup_(|x|<2R)|Pi_outer(x)|<=C R I(R),
    I(R)<=4 integral_(4R)^infinity r^-5 E(r)dr.            (2)

For the last line integrate r^-4 E'(r). The upper boundary vanishes because E(r)<=4pi M^2 r^3/3; the lower boundary has a nonpositive sign and can be dropped.

With q=|U|^2/2, the dot product of momentum with U gives

    (1-5c/2)|U|^2+div(qB+PU)=0.

The field inside the divergence is C1. The divergence theorem and tangency of Jy to spheres give, for every R>0,

    (cR/2)E'(R)+(1-5c/2)E(R)
       =-integral_(|y|=R)(q+P-p)U.n.

The arbitrary constant p disappears because integral_(|y|=R)U.n=0. Consequently, for g(R)=R^-alpha E(R),

    g(R2)-g(R1)=-(2/c) integral_(R1<|y|<R2)
                      |y|^(-1-alpha)(q+P-p)U.(y/|y|).   (3)

The constant can be chosen separately on each annulus. No boundary flux at infinity has been discarded.

## 4. Flux bound and the finite iteration

Let Phi(R)=integral_(R<|y|<2R)|q+P-p_R||U|. By (2) and Cauchy-Schwarz,

    Phi(R)<=epsilon(R)E(2R)/2+epsilon(R/2)E(4R)
          +C R^(3/2) E(2R)^(1/2)[R^-3 E(R/2)+R I(R)].    (4)

If E(r)<=K r^mu for r>=1, with 0<=mu<=3, then (2) gives I(R)<=C K R^(mu-4). The last term in (4) has power (3mu-3)/2<=mu; the first two are bounded using epsilon<=M. Thus Phi(R)<=C R^mu, with a finite constant depending on M,K and universal kernel bounds. Equation (3) implies

    |g(R2)-g(R1)|<=C R^beta,
    beta=mu-1-alpha,  R<=R1<R2<=2R.                      (5)

This controls intermediate radii, not only dyadic endpoints. If beta>0, sum (5) from a fixed inner radius to R to obtain E(R)=O(R^(mu-1)); the initial R^alpha term is smaller. If beta=0, the result is O(R^(mu-1)(1+log R)). If beta<0, sum outward: the geometric tail makes g Cauchy at infinity and gives |g(R)-L|<=C R^beta. These are the only iteration rules used below. Intermediate constants may change with K and mu.

## 5. The three parameter ranges

Start from mu=3. If alpha<0, the positive-beta rule successively gives exponents 2,1,0. Applying (5) at mu=0 gives either E=O(R^-1), E=O(R^-1 log R), or bounded g with E=O(R^alpha), according to the sign of beta. Every alternative tends to zero. Since E is nonnegative and nondecreasing, E vanishes identically.

If 0<alpha<3, apply the positive-beta rule while mu-1>alpha. At equality first use the logarithmic bound and absorb its logarithm in R^(1/4), giving an exponent alpha+1/4. At every stage the exponent remains in [0,3]. In finitely many steps mu-1<alpha, so the negative-beta rule gives a finite limit L of g. In particular E=O(R^alpha). Reapply (5) with mu=alpha to obtain |g-L|<=C/R. Nonnegativity of g gives L>=0.

If L=0, this gives E=O(R^(alpha-1)). If the exponent is nonnegative, apply (5) again at this exponent and sum outward using the same zero limit. Each repetition lowers the energy exponent by one. Once it becomes negative, monotonicity forces E=0. Thus a nonzero profile has L>0.

At alpha=0, the iteration gives 3,2,1, then E=O(log R). Absorb the logarithm into R^(1/4) and use the negative-beta rule. This makes E converge to finite total energy. Reapply (5) with mu=0 to obtain the initial tail bound O(R^-1). Section 6 sharpens it. Each finite iteration starts from boundedness and E on a fixed compact ball, so the final energy constants depend only on c,M and E(4). Rotation entered only in the preliminary normalization limit and the exact cancellations, not these bounds.

## 6. Decay refinement and the endpoint tail

For 0<alpha<3, insert E=O(R^alpha) into the unsimplified (4). Its right side is bounded by

    C epsilon(R/2) R^alpha+C R^((3alpha-3)/2).

Equation (3) and its outward geometric sum give

    |g(R)-L|<=C[epsilon(R/2)/R+R^((alpha-5)/2)].            (6)

Under uniform decay, epsilon tends to zero; since alpha<3 the second power is strictly smaller than -1. This proves the little-o refinement. The same argument at alpha=0 is valid after finite total energy is known.

At alpha=0 write T(R)=integral_(|y|>R)|U|^2. In (4), the cubic and middle-pressure terms are bounded by C T(R/2), the inner pressure contribution by C R^-3/2 T(R)^(1/2), and the outer pressure contribution by C R^-3/2 T(4R)T(R)^(1/2), because I(R)<=(4R)^-4 T(4R). Total energy bounds T(4R), so

    Phi(R)<=C[T(R/2)+R^-3/2 T(R)^(1/2)].

The exact identity (3), summed outward, converges absolutely with these bounds and yields

    T(R)<=C R^-1 T(R/2)+C R^-5/2 T(R)^(1/2).             (7)

A bound T=O(R^-tau) improves by (7) to tau'=min(tau+1,(5+tau)/2). Starting from tau=0 yields successively 1,2,3,4. Then the first term of (7) is O(R^-5). Young's inequality bounds the second by T(R)/2+C R^-5. Absorption proves T=O(R^-5). The result does not exclude nonzero finite-energy profiles at this endpoint.

## 7. Consequences used in the current audits

For bounded full profiles satisfying Hb, the theorem gives E(R)=o(R^2) for 0<c<2/3. Below c=2/5 the field is zero; at equality the energy is bounded; above equality the exponent 5-2/c is strictly less than two. At c=2/3 the argument supplies only O(R^2), so the little-o endpoint must not be silently added.

For 0<c<1/2 it also gives E(R)=o(R). Conversely, bounded U with E(R)=o(R) satisfies Hb, because for each fixed L0>0,

    ||U(R.)||_(L2(B_L0))^2=R^-3 E(L0 R)=o(R^-2).

Thus Hb and E=o(R) are equivalent within the bounded full-profile class in this range. This is not an equivalence for arbitrary bounded vector fields. In the campaign interval 2/5<c<1/2, positive L means infinite total energy with sublinear radial growth, entirely compatible with uniform velocity decay. Nothing here supplies global small vorticity, a helicity sign, source symmetry, pressure symmetry or convergence of general characteristics.

## 8. Reading scope and limits

The entire 367-line current in the team records source, the complete original pressure-normalization and energy-growth proofs, and all seven sections of the evening foundation reconstruction were reread. The current audit independently reconstructs only the classical normalization and energy statements in Section 1, the displayed endpoint refinement and the two consequences in Section 7. Historical priority claims, claims that a method is optimal, attainment by actual profiles, weak-defect theorems, Lorentz convolution statements, and other corollaries in the source are outside this recheck. No HLS or O'Neil inequality is needed here.

The functional inputs are the explicit double-Riesz multiplier and kernel, its L2 bound from Plancherel, harmonic regularity and the radial mean-value property. The boundary estimates are given in the proof. No mathematical computation, formal build, new model client or external-source retrieval was needed. Existing configured model comparison is requested; actual provider execution is independently unattested.

## 9. Complete A115 comparison and disposition

The full in the team records, dated 2026-11-04T07:09Z and announced as A115, was read. Its direct comparison with in the team records and report2A agrees with every analytic step above. The distributional pressure normalization uses no pressure growth bound; the moving-test error is controlled by boundedness and Hb. The annular pressure pieces have different names in the two texts but identical supports and estimates.

The bound at all intermediate radii is necessary for the last partial dyadic annulus. The zero-leading-coefficient iteration continues only while its exponent is nonnegative, then monotonicity forces zero. The endpoint recurrence passes through powers0,1,2,3,4 and uses Young's inequality for power5. These points were independently checked again. The constants need not depend on finite omega.

The described seventeen-item scratch diagnostic and its first failed run were not read or rerun by this agent and are not certified. This verdict concerns only the classical theorem in Section1, its displayed endpoint and decay refinements, and the explicit consequences in Section7. It does not newly certify historical priority, optimality, attainment, weak-defect statements or Lorentz estimates. The unrestricted target case remains open. Existing comparison is with configured model A, actual provider execution independently unattested.
