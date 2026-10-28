# An exact transport reduction near the modal source

## Statement

Let V be a smooth vector field near0 in R2 with V(0)=0 and DV(0)=B=diag(A,mu), where

 10<A<51/5, 99/100<mu<1, 10mu<A<11mu.                (1)

There is a smooth local diffeomorphism Psi with Psi(0)=0 and DPsi(0)=I such that

 DPsi(X)V(X)=B Psi(X).                               (2)

If V1 is even in y and V2 is odd in y, Psi has the corresponding reflection equivariance. For every sufficiently small delta>0, a fixed smooth cutoff defines a global smooth diffeomorphism Phi_delta, equal to Psi on B_(delta/2) and to the identity outside B_delta. It satisfies

 ||Phi_delta-id||infinity<=C delta^2,
 ||DPhi_delta-I||infinity<=C delta,
 [DPhi_delta-I]_alpha<=C_alpha delta^(1-alpha),
 ||D2Phi_delta||infinity<=C,                          (3)

for each fixed 0<alpha<1. The constants depend on V on a fixed neighborhood and on the cutoff. No numerical value of the admissible delta is claimed.

Define the global extension

 V_delta(X)=[DPhi_delta(X)]^(-1) B Phi_delta(X).       (4)

It equals V on B_(delta/2) and B X outside B_delta. On X_alpha=C^alpha_b intersect L2, with the sum norm of proof 208, let C_delta h=h composed Phi_delta^(-1). Both C_delta and its inverse have norm at most 1+C_alpha delta. On maximal distributional domains one has exactly

 C_delta(V_delta.grad-1)C_delta^(-1)=B X.grad-1.      (5)

In particular C_delta identifies the two maximal transport domains as sets with equivalent graph norms. Equation(5) is not a small bounded first-order perturbation assertion. It also does not conjugate the IPM Riesz multipliers to themselves. The latter error is a separate obligation.

For the exact modal source P=(p,0) of proof 15, apply this theorem to X -> V(P+X). The hypotheses hold. The accompanying original-data check confirms that the source lies in an analytic disk of radius1/1000, and that all150 homological denominators of degrees2 through11 have absolute value greater than3/20. The minimum lower endpoint is approximately0.150725468783092. These are source-geometry and spectral-gap certificates, not a numerical conjugacy radius or a coupled inverse bound.

## Removal of the finite Taylor polynomial

For a vector monomial X1^m X2^n e_j of degree d=m+n, the homological map

 P -> DP(X)B X-B P(X)

multiplies its coefficient by mA+nmu-lambda_j, where lambda_1=A and lambda_2=mu. For 2<=d<=11 these denominators never vanish under(1). For j=2 the sum mA+nmu is at least2mu>mu. For j=1 and m>=1, equality with A is impossible except at the excluded degree-one monomial m=1,n=0. For m=0, the only candidate is nmu=A, excluded by10mu<A<11mu. This argument also excludes higher-degree resonances, but only the indicated finite list is needed.

Suppose degrees2 through d-1 have already been removed and N_d is the homogeneous degree-d part of the remaining field. In coordinates Y=X+P_d(X), its degree-d term becomes

 N_d+DP_d B X-B P_d.

Terms involving N_d and DP_d beyond this expression have degree at least d+1. Divide each coefficient of -N_d by its nonzero homological denominator to obtain P_d. The map is a local smooth diffeomorphism because its derivative at0 is I. Compose these coordinate maps for d=2,...,11. The resulting local map Psi_0 is tangent to the identity and transforms V into

 W(Z)=B Z+R(Z),
 D^j R(Z)=O(|Z|^(12-j)) for 0<=j<=12.               (6)

All derivatives of R of fixed higher order are bounded on a smaller neighborhood. Taylor's theorem proves(6); the background is smooth, so taking this finite jet does not require an analytic normal-form theorem. If V has the stated reflection, its Taylor coefficients have that reflection and the diagonal homological map preserves it. Each P_d, and hence Psi_0 and W, is equivariant.

## The convergent backward-flow correction

Choose mu_prime=99/100. Since mu>mu_prime and DW(0)=B, shrink a closed ball about0 so that the symmetric part of DW is bounded below by mu_prime I. If Y_t(Z) is the backward flow of W, it solves

 d_t Y_t=-W(Y_t), Y_0=Z.

The ball is invariant under this backward flow: W(0)=0 and the derivative lower bound imply Z.W(Z)>=mu_prime|Z|^2. Thus

 |Y_t(Z)|<=exp(-mu_prime t)|Z|.                       (7)

The solution exists for every t>=0, since it stays in the ball and tends to0. Differentiating in the initial point gives

 ||DY_t||<=exp(-mu_prime t).

For each k>=2, the equation for D^kY_t has linear part -DW(Y_t)D^kY_t and forcing made from bounded derivatives D^jW, j>=2, times products of at least two lower derivatives of the flow. Induction and variation of constants give

 ||D^kY_t||<=C_k exp(-mu_prime t)                    (8)

on a fixed smaller initial ball. Indeed every forcing product has bound C exp(-2mu_prime t), and its convolution with exp(-mu_prime(t-s)) is at most C exp(-mu_prime t)/mu_prime. This verifies the needed uniform derivative estimates rather than assuming differentiability of a limiting flow map.

Set

 H(Z)=Z-integral_0^infinity exp(Bt)R(Y_t(Z))dt
     =lim_(t->infinity) exp(Bt)Y_t(Z).              (9)

The second identity follows by differentiating exp(Bt)Y_t and integrating. Equations(6)-(8) justify all derivatives in(9). A term in a k-th initial derivative with l derivatives of R has an exponential factor at most exp(-max(12,l)mu_prime t): when l<=12, the vanishing |Y_t|^(12-l) and the l flow derivatives together give exp(-12mu_prime t); when l>12, the l flow derivatives give at least that decay. Multiplication by exp(Bt) costs at most exp(At). The resulting majorant is integrable because

 12mu_prime-A>297/25-51/5=42/25>0.                  (10)

Thus the convergence is uniform with every fixed number of derivatives, and H is smooth. The same estimates with the vanishing powers retained give

 H(Z)-Z=O(|Z|^12), DH(Z)-I=O(|Z|^11), D2H(Z)=O(|Z|^10).

In particular H is a local diffeomorphism tangent to the identity.

For a fixed sufficiently small flow time s, the flow law in the limit in(9) gives

 H(Flow_s^W Z)=exp(Bs)H(Z).

Both initial points may be chosen in the smaller ball, and after sufficiently large backward time the same backward orbit lies there; the limit identity is therefore within the already defined local flow. Differentiating in s at0 yields DH W=B H. Consequently Psi=H composed Psi_0 satisfies(2). Reflection equivariance is preserved by the backward flow and the integral in(9). This proves the local transport reduction directly, without an external linearization theorem.

## Global cutoff and norm transfer

Fix a smooth cutoff chi supported in B1 and equal1 on B_(1/2), and put

 Phi_delta(X)=X+chi(X/delta)(Psi(X)-X).

Since Psi(X)-X=O(|X|^2), DPsi-I=O(|X|) and D2Psi is bounded near0, differentiating this formula proves the first, second and fourth bounds in(3). The third follows by splitting derivative differences at distance delta: a bounded function of supremum O(delta) and Lipschitz constant O(1) has alpha seminorm O(delta^(1-alpha)). Extension by0 across the support boundary is smooth because the cutoff is smooth and compactly supported.

For small delta, ||DPhi_delta-I||infinity<1/2. If Phi_delta=id+w, then Lip(w)<1, so solving X=Y-w(X) by contraction for each Y gives a unique global inverse. Its smoothness follows from the invertible derivative. The singular values of DPhi_delta lie between1-Cdelta and1+Cdelta, and its positive determinant is bounded between their squares. These bounds also control the inverse derivative.

For C_delta h=h composed Phi_delta^(-1), a change of variables gives

 ||C_delta h||2<=(1+Cdelta)||h||2,
 ||C_delta h||infinity=||h||infinity,
 [C_delta h]_alpha<=(1-Cdelta)^(-alpha)[h]_alpha.

The inverse composition has the analogous bounds. These prove the X_alpha statements, with constants enlarged for the fixed alpha. Reflection-equivariant maps preserve the odd-y subspace if it is imposed. No assertion is made about the weighted origin space E_2, for which a different coordinate transfer was previously refuted.

For smooth h the chain rule and definition(4) give(5). The identity extends to distributions by testing and changing variables with the smooth diffeomorphism. Equivalently approximate h in distributions by smooth functions and use continuity of both the differential expressions and distributional pullback; no convergence in the Holder norm is required for this identity. Since C_delta and its inverse are bounded on X_alpha, the identity shows

 {h in X_alpha:V_delta.grad h in X_alpha}
   =C_delta^(-1){u in X_alpha:B X.grad u in X_alpha}.

It also gives both graph-norm comparisons. There is no derivative loss hidden in the domain identification.

## Applicability to the original modal data

Proof 15 supplies the exact modal source and its rigorous bracket [a,b], the transverse rate interval, and the identity A+mu=2/k from div U=0. The original k is the exact dyadic1615536043799051/9007199254740992. The companion code reads it again from the read-only original NPZ and checks its hash. It uses the certified transverse interval as an explicitly named input, not a midpoint approximation to mu.

The source's stored logarithmic span endpoints are checked to be consecutive original knots. At both256 and384 bits, directed exponential arithmetic proves

 a-exp(t_left)>0.0096052856238,
 exp(t_right)-b>0.0068269382814.

In particular every point in the physical disk of radius1/1000 about any P in the bracket has radius strictly within that one knot span. On this annulus the density is a finite sum of logarithmic degree-seven polynomials times smooth radial and angular functions. It is smooth there. The canonical stream's finite radial Green modes solve constant-coefficient equations in log r with these smooth forcings, so the velocity is smooth on the same annulus. The finite global C6 knot regularity is not being substituted for arbitrary local smoothness at a knot.

With A=2/k-mu, every homological denominator is affine in mu. Evaluating its two exact rational endpoints gives its complete enclosure over the certified source interval. All150 denominators of degrees2 through11 have magnitude greater than3/20. This independently verifies(1) and the finite denominators for this precise state. The check takes less than one second on one thread; its true time, original hash, exact endpoints and both precision replays are recorded in evidence/check.json. The claimed inequalities use directed or exact arithmetic. The displayed approximate minimum is only a readable rendering of its exact rational lower endpoint.

## Scope

This theorem constructs a specific source transport extension, equal to the actual transport locally. It does not show that the full IPM nonlocal operator commutes with the diffeomorphism, and it supplies no numerical inverse constant. Closeness of Phi_delta to the identity does not imply operator-norm smallness of C_delta-I on a Holder space; high-frequency translated inputs already preclude that inference. A coupled inverse requires a bound for C_delta M C_delta^(-1)-M itself, together with coefficient variations. That separate estimate is addressed next in the reading-order index. Full central strain on X_alpha, origin and far matching, closed normalization and nonlinear closure remain separate questions. Independent independent cross-audit of the finite-jet and backward-flow proof is requested.
