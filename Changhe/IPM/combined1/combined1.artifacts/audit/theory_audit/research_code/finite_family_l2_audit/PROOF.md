# Independent audit of the finite-family L2 floor

## Exact statement and hypotheses

Use the fixed case4 exponent c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma. Let B>=4 and K>=0 be integers. Consider smooth real S1 potentials

chi=sum_(0<=j<B,0<=m<=k<=K) a_(j,m,k) r^(2k)(1+r²)^((3+gamma-j delta)/2-k) cos(2m theta).

Assume their first B principal homogeneous potential profiles are prescribed to be the stationary profiles generated from the full state131 leading profile. If these profiles do not fit the angular index set, there is no such potential. Define rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy) and F=(cX+u).D rho-rho. Let e_B(theta) be the fixed residual angular coefficient at q=1-(B+1)delta and let E_B be its full-circle L2 norm.

Set a0=(B+1)delta/2-3/2 and let A consist of

ell delta/2+k-3/2, 1<=ell<=2B, 0<=k<=2K+4, ell delta/2+k>1.

Require these powers to be distinct and require a0 in A. Then a0>-1/2, and with

D=(2a0+1)^(-1/2) product_(a in A,a!=a0) |a-a0|/(a+a0+1),

every such potential satisfies ||F||_2>=E_B D/sqrt(2). If a candidate framework also has X_s(F)>=(1-34s)E(F), E(F)>=512||F||_2 and 0<s<1/34, its necessary lower bound is X_s(F)>=(1-34s)512 E_B D/sqrt(2).

This independently confirms the theorem in source/N4_PROOF.md. Values of E_B and D require their separate exact-input and arithmetic checks. The statement is a necessary condition for a specified finite-dimensional family, not an existence or nonexistence theorem for unrestricted profiles.

## 1. Finite radial power space

Put u=(1+r²)^(-1) and t=1-u. Each potential term has form (1+r²)^p P(t) cos(2m theta), with deg P<=K. Applying r partial_r to a term with an additional factor r^(-d) acts on its polynomial as

P -> (2pt-d)P+2tu P'.

Consequently three Cartesian derivatives give r u^((j+1)delta/2) times angular polynomials with radial polynomial degree at most K+1. One may verify this by first using Delta=r^(-2)((r partial_r)²+partial_theta²) and then one Cartesian derivative; the numerator is divisible by t² because the original generator is smooth. The same degree bound holds for the velocity's third derivatives of the potential. A further Cartesian derivative of rho gives u^((j+1)delta/2) times a polynomial of degree at most K+2. The factor r is removed and the angular modes remain finite.

Thus the linear residual has degree at most K+2, and the nonlinear product has degree at most2K+3. For each positive odd sine mode,

F_n(r)=r H_n(u), H_n(u)=sum_(ell=1)^(2B) u^(ell delta/2) P_(ell,n)(1-u), deg P<=2K+3.

The fixed stationary principal profiles cancel the residual powers p2 through pB. The remaining first principal power is1-(B+1)delta<-1 for B>=4. All descendants have exponent at most gamma-2<-1. Finite differentiated binomial expansions therefore show F belongs to L2. Equivalently, every coefficient with ell delta/2+k<=1 in the displayed finite power sum vanishes: a nonzero smallest such exponent would give a nonintegrable radial leading power, and distinct exponents prevent cancellation. This argument does not assume any bound on the free coefficients.

The coefficient at ell=B+1,k=0 is precisely e_(B,n). No linear branch j=B exists. Products of the prescribed lower branches determine it. Distinctness of the fractional power classes excludes collision with any descendant. Multiplying H_n by1-u does not change that coefficient because its predecessor in the same fractional class would have k=-1. Thus

w_n(u)=(1-u)u^(-3/2)H_n(u)

lies in span{u^a:a in A}, and its u^a0 coefficient is e_(B,n). Multiplication increases the degree bound by one, explaining2K+4.

## 2. Exact radial and angular normalization

The full-circle norm of sin(n theta) is sqrt(pi) for every positive integer n. Since r dr=-du/(2u²) and r²=(1-u)/u,

||F||_2²=(pi/2)sum_n integral_0^1 (1-u)u^(-3)H_n(u)² du
        =(pi/2)sum_n integral_0^1 w_n(u)²/(1-u) du
        >=(pi/2)sum_n ||w_n||_(L2(0,1))².

The discarded factor1/(1-u) is at least one. This step is global in radius and uses neither a guessed far-field onset nor a truncated asymptotic series.

## 3. Distance in a power span

For distinct a>-1/2 the functions u^a are linearly independent in L2(0,1), with positive Gram matrix G_ab=1/(a+b+1). Let q be the orthogonal residual after projecting u^a0 onto the span of the other powers. Its Mellin transform Q(z)=integral_0^1 q(u)u^z du is rational. It has simple poles at -a-1, zeros at every a!=a0, and residue one at -a0-1. These determine

Q(z)=C product_(a!=a0)(z-a)/product_(a in A)(z+a+1).

The residue condition fixes C. Substitution at z=a0 gives

Q(a0)=(2a0+1)^(-1)product_(a!=a0)(a-a0)²/(a+a0+1)².

Orthogonality yields Q(a0)=||q||². In particular this formula does not require a0 to be the smallest exponent. Every w with coefficient e at u^a0 decomposes as e q plus a vector orthogonal to q, so ||w||>=|e|D. Applying this to each sine mode and summing gives ||F||_2²>=(E_B²/2)D², as stated.

## 4. Scope and dependencies

The argument confirms the degree count, integrability implication, prescribed coefficient, Cauchy distance formula and normalization in N4's proposal. Enlarging the realizable residual set to the full power span weakens the lower bound and is safe. Increasing K or B changes the theorem's input and may greatly weaken the floor. Any exclusion against a high-norm threshold also requires the stated comparison inequality and the independent numerical value of the floor. It does not follow just from a nonzero tail coefficient.

Dependencies are the displayed polar derivative identities, elementary finite binomial expansions, angular orthogonality and the finite-dimensional orthogonal projection argument. The exact stationary recursion and arithmetic values are separate evidence in source/stationary_principal.json and subsequent verification files.
