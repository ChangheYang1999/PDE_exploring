# A finite-family lower bound for the L2 residual

## Statement and exact family

Let c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma. Fix integers B>=4 and K>=0. Consider real, smooth S1 potentials

chi=sum_(0<=j<B, 0<=m<=k<=K) a_(j,m,k) r^(2k)(1+r²)^((3+gamma-j delta)/2-k) cos(2m theta).

Their leading homogeneous potential coefficients are prescribed to equal the first B stationary principal profiles obtained from the full state131 leading angular profile. Those exact rational profiles and their recursion are in ../sector_audit/PROOF.md and verification/stationary_principal.json. If the prescribed angular profiles do not fit this index set, the family is empty. No descendant cancellation or bound on the remaining coefficients is assumed.

Set rho=-partial_y Delta chi, U=(-chi_xyy,chi_xxy), F=(cX+U).D rho-rho. Let e_B(theta) be the fixed residual forcing from the first B principal profiles at exponent p_B=gamma-B delta=1-(B+1)delta. Write E_B=||e_B||_(L2 full circle). Assume the powers in the finite set below are distinct, a condition checked exactly for every reported B,K. Put

a_*=(B+1)delta/2-3/2,
A={ell delta/2+k-3/2: 1<=ell<=2B, 0<=k<=2K+4, ell delta/2+k>1},
D=(2a_*+1)^(-1/2) product_(a in A, a!=a_*) |a-a_*|/(a+a_*+1).

Assume a_* belongs to A. Then every potential in the family satisfies

||F||_2 >= E_B D/sqrt(2).

For any framework whose energy is E_*(F)²=P2²+2^14 G1²+2^18 G0² and whose comparison is X_s(F)>=(1-34s)E_*(F), 0<s<1/34, it follows that

X_s(F)>=(1-34s)512 E_B D/sqrt(2).

This is a lower bound for this specified finite-dimensional family, not for arbitrary smooth references. A numerical evaluation of this formula requires an independent audit before it is treated as a certified team conclusion.

## Radial representation and prescribed coefficient

Put u=(1+r²)^(-1), t=1-u. Repeated Cartesian differentiation of one potential generator, or the explicit recurrence in ../radial_fourier/PROOF.md, gives

F_n(r)=r H_n(u), H_n(u)=sum_(ell=1)^(2B) u^(ell delta/2) P_(ell,n)(1-u),

where each polynomial has degree at most 2K+3. One third derivative has polynomial degree at most K+1, one fourth derivative at most K+2, and their product has degree at most 2K+3. The linear contribution has smaller degree. Apparent negative powers at the origin cancel by smoothness of each generator with k>=m. The angular sum is finite and consists of odd sine modes.

All sectors with h<B and q=0 vanish by the imposed stationary leading profiles. Because B>=4, these include every nonautomatic sector with exponent at least -1. Descendants q>=1 have exponent at most gamma-2<-1. Consequently F is in L2. In the displayed finite power representation every coefficient with ell delta/2+k<=1 vanishes. This also follows by the triangular relation between the exterior expansion and powers of u, or directly from L2 integrability and distinct powers.

The coefficient of u^((B+1)delta/2) is e_(B,n), the nth sine coefficient of e_B. The absent branch j=B contributes no linear term. The coefficient is therefore the quadratic forcing of prescribed lower principal profiles. Descendants cannot change it when the displayed exponents are distinct. Multiplication by 1-u does not change this coefficient: within this fractional class it is the first nonzero power. Thus

w_n(u)=(1-u)u^(-3/2)H_n(u)

belongs to the power space spanned by u^a, a in A, has coefficient e_(B,n) at u^a_*, and every exponent in that space is greater than -1/2.

## The L2 inequality

Since r dr=-du/(2u²), full angular orthogonality gives

||F||_2²=(pi/2)sum_n integral_0^1 (1-u)u^-3 H_n(u)² du
         =(pi/2)sum_n integral_0^1 w_n(u)²/(1-u) du
         >=(pi/2)sum_n ||w_n||_(L2(0,1))².

No tail onset radius or asymptotic truncation is used in this inequality.

For distinct exponents a>-1/2, the Gram matrix of u^a is the positive Cauchy matrix G_ab=1/(a+b+1). The squared distance of u^a_* from the span of the other powers is

D²=(2a_*+1)^-1 product_(a!=a_*) (a-a_*)²/(a+a_*+1)².

For completeness, let q be the orthogonal residual of u^a_*. Its Mellin transform Q(z)=integral q(u)u^z du has poles at -a-1, zeros at each other exponent a, and residue1 at -a_*-1. These conditions determine its numerator and constant uniquely. Substitution at z=a_* gives Q(a_*)=||q||² equal to the displayed positive product. This derivation does not require a_* to be the smallest exponent. Orthogonality then gives ||w_n||_2>=|e_(B,n)|D. Summing the squared inequalities and using E_B²=pi sum_n e_(B,n)² proves the claim.

## Scope and verification

The bound allows every vector in a larger linear power space, whether or not it comes from a nonlinear residual. Enlarging the space can only weaken the lower bound. Coefficient size and ill-conditioning cannot evade it inside the specified family. Adding branches, increasing K, changing c or changing the leading profile changes the bound. A failure of this lower bound to exceed a closure threshold gives no evidence that a candidate exists. The framework's background bounds and actual residual upper bound are separate requirements.
