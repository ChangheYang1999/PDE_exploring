# A regularized weighted L2 commutator and conditional low inverse

## 1. Statement

Let0<a<2,0<d<2-a,R>0 and w_R(X)=(1+|X|²/R²)^(-a/2). All inputs below are real centrally odd functions. The velocity U=(-R1R2,R1²) uses the canonical Fourier realization and its extension to L²(w_R²). Define

M_d=(d/2)((2-d)/d)^(1-d/2),
C(a,d)=a M_d/sqrt(2) * sqrt((2-a-d)^(-2)+(2+d)^(-2)).

Then for every real centrally odd phi in L²,

||r^(-d)(w_R U[w_R^(-1)phi]-U[phi])||_(L²;R²)
 <=C(a,d)R^(-d)||phi||_2.                                (1)

The expression is initially defined on compact smooth functions away from the origin and extends continuously by(1). It agrees with the difference of the two canonical weighted transforms. Real parity is essential to the displayed constant; we do not assert it for arbitrary complex inputs.

As a consequence, let rho be a smooth S1 reference with canonical smooth divergence-free u=U[rho], V=cX+u globally Lipschitz and at most linear, and c>0. Suppose D rho is bounded and

Re<(V.grad-1+U[.].D rho)f,f>_2 <=-beta0||f||_2²           (2)

on the compact smooth S1 core. Suppose also

sup r^d |D rho|<=C_rho,   sup r^(d-1)|u|<=C_u.            (3)

Here norms of D rho and u are Euclidean, taken pointwise before the supremum. Put

beta_R=beta0-ca-[C_rho C(a,d)+a C_u M_d]R^(-d).           (4)

If beta_R>0, the maximal distributional realization of L=V.grad-1+U[.].D rho on L²(w_R²) has a consistent bijective inverse of norm at most1/beta_R. It generates a strongly continuous semigroup of norm at most exp(-beta_R t). The same conclusion for L+W.grad has decay beta_R-a D whenever W is a globally Lipschitz, centrally odd, divergence-free vector field with ||DW||_infinity<=D and beta_R>a D.

This is only a low weighted inverse theorem. No corresponding rough high inverse or complete nonlinear existence theorem is established here.

## 2. Canonical angular blocks

Write D_+=partial_x+i partial_y, D_-=partial_x-i partial_y and B=D_-/D_+, whose Fourier symbol is exp(-2i arg xi). On real inputs U2+iU1=-(I+B)/2. Thus the velocity commutator is minus one half the Beurling commutator, with equality between the complex scalar norm and the real vector norm.

For a compact smooth angular input f_m(r)exp(im theta), put n=m-1 and g=D_-Delta^(-1)f. Its only mode is n, and D_+g=f. The radial equation g'-n g/r=f gives the canonical solution

g(r)=-r^n integral_r^infinity s^(-n)f_m(s)ds,   n>0,
g(r)= r^n integral_0^r s^(-n)f_m(s)ds,          n<0.

For n=0, D_-g=D_+g=f_m, so B maps mode m=1 to mode-1 by the identity radial map. This block has zero commutator with every radial weight. The endpoint choices for n!=0 follow from the canonical inverse's regularity at zero and its exterior expansion for compact centrally odd sources. They can also be checked by substituting the displayed integrals into the radial equation.

Set t=log r and F_m(t)=r f_m(r). This is an isometry of the radial L²(r dr) space onto L²(dt). For n>0 the radial action of B becomes

F_m(t)-2n integral_0^infinity exp(-n v)F_m(t+v)dv.

For n<0 it becomes

F_m(t)+2n integral_0^infinity exp(n v)F_m(t-v)dv.

The angular output is always m-2. Central oddness means m is odd. The nonzero positive n therefore have n>=2, and negative n have |n|>=2.

## 3. Kernel bounds

Let ell(t)=log w_R(exp t). Its derivative satisfies

0<=-ell'(t)=a (r/R)²/[1+(r/R)²]<=a M_d(r/R)^d.

The last inequality follows by maximizing x^(2-d)/(1+x²), whose unique positive maximum occurs at x²=(2-d)/d. Also -ell'<=a.

For v>=0 the forward weight ratio obeys

w(t)/w(t+v)-1
 =integral_0^v [-ell'(t+s)] w(t)/w(t+s)ds
 <=a M_d(r/R)^d (exp((a+d)v)-1)/(a+d).                   (5)

The backward ratio obeys

1-w(t)/w(t-v)
 =integral_0^v [-ell'(t-s)] w(t)/w(t-s)ds
 <=a M_d(r/R)^d (1-exp(-dv))/d.                          (6)

Insert these inequalities into the angular Volterra formulas and multiply by r^(-d). The remaining positive convolution kernels have L¹ norms

P_n=2a M_d/(n-a-d) R^(-d),       n>=2,
D_n=2a M_d/(|n|+d) R^(-d),       n<=-2.

The first formula uses n>a+d. Young's inequality on the t line, obtained directly by Minkowski and translation invariance of the L² norm, bounds each block by these constants.

## 4. Real pairing and the velocity constant

For a real input the coefficients at m and -m are conjugates and have equal radial L² norms. The outputs of distinct input modes are orthogonal because m maps injectively to m-2. For m=1 the positive block is zero and the negative block is bounded by D_(-2). For m>=3 the positive block is bounded by P_2 and the negative block by D_(-2). Consequently the squared norm of the full Beurling commutator is at most

(P_2²+D_(-2)²)/2 * ||phi||_2².

The factor1/2 accounts for the equal energy in each real pair. Dividing the resulting norm by2 for U yields exactly(1). This estimate is not asserted sharp.

The proof first applies to finite angular sums supported on compact annuli. They are dense in the real centrally odd L² space. The uniform bound gives the extension of r^(-d) times the commutator. The radial weighted Riesz theorem of Analysis II P7.2 supplies the individual canonical transforms for |a|<2, and local distributional convergence identifies their difference with this extension. The singular output factor at zero is controlled by(1), not discarded.

## 5. Weighted energy and generator

Conjugate by the isometry phi=w_R h. Direct differentiation gives

w_R L w_R^(-1)phi
 =V.grad phi-phi+U[phi].D rho
  -V.grad(log w_R)phi
  +(w_R U[w_R^(-1)phi]-U[phi]).D rho.

The last term has L² norm at most C_rho C(a,d)R^(-d)||phi|| by(1),(3). Furthermore

-cX.grad log w_R=ca r²/(R²+r²)<=ca,
|u.grad log w_R|<=a C_u r^(2-d)/(R²+r²)
 <=a C_u M_d R^(-d).

Combining these with(2) proves the decay rate(4). The complete Lipschitz flow of V gives a strongly continuous transport group on L² after conjugation; the added scalar transport term is bounded. The weighted Riesz bound and bounded D rho make the coupling a bounded L² perturbation. Thus its generator has the maximal distributional transport domain, preserved under this bounded perturbation. The compact smooth core is a graph core by mollification and radial cutoff. The energy estimate extends to the generator domain. If beta_R>0, minus the time integral of the semigroup converges in operator norm and is an inverse into that domain. Injectivity follows because a kernel vector would have a constant orbit subject to strict decay.

For an additional W, unweighted W.grad is skew in L² because div W=0. Central oddness gives W(0)=0 and hence |W(X)|<=D r. Its conjugated scalar contribution satisfies |W.grad log w_R|<=a D. The same generator construction and energy proof give the stated perturbed decay. No derivative of the input is estimated by its low norm.

## 6. Forcing powers and nonlinear product scope

A smooth nonzero exterior power r^q times a finite angular profile belongs to L²(w_R²) at infinity exactly when q<a-1. The archived residual has q=2/c-1, so the low membership condition is a>2/c. For pure subleading powers, a<1+1/c implies q<a-1<1/c. Membership alone does not establish a pointwise asymptotic for an arbitrary element of the weighted space.

If an independent high norm guarantees ||Dg||_infinity<=D, the weighted Riesz theorem gives

||w_R U[z].Dg||_2<=C_2(-a)D ||w_R z||_2.

Together with the perturbed low inverse this would give a contraction factor at most C_2(-a)D/(beta_R-aD). This observation is conditional on a complete high inverse, the normalized trace, and a closed high ball in the low metric. None is supplied by this low-space theorem.

## 7. A checked low-space parameter example

For state131, use a=221/200, d=4/9, R=2^29, C_rho=186 and C_u=22. The last two coefficients are the existing Analysis II P21.1 bounds. With the independently reproduced gradient-HS input, beta0>2.04956566. The adjacent Arb256 certificate proves C(a,d)<1.038258 and beta_R>0.02181481>1/50. The exponent satisfies a>2/c and a<1+1/c, so the original residual is admitted at infinity in this low norm. For an illustrative gradient bound D=1/250, the perturbed low rate is>0.01739481 and the conditional low contraction factor is<0.528646.

These values do not establish high solvability, residual smallness, or an exact IPM profile. The very large radius and exponent close to the membership endpoint may produce a large forcing norm. The example is a checked realization of the low inverse, not an improvement claim for a completed a posteriori threshold. Team acceptance of the reused new background seminorms is subject to the coordinator's independent-review convention.

## Dependencies and status

The proof uses exact first-order polar identities, the independently proved Analysis II radial weighted Riesz extension, and the explicitly stated low coercivity hypothesis(2). One source of beta0 is the signed-principal plus gradient-HS bound c+1-theta-kappa established elsewhere in this lane. Numerical coefficient bounds must be certified for the particular reference. The theorem is new T4 work and remains CLAIMED until independent Opus review.
