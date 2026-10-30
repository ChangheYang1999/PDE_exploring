# A certified improvement of the angular Hardy upper bound

Written UTC 2026-10-29T15:26:31.980131+00:00 before the checker. This is an independent alternative for the negative Sobolev upper bound. It does not infer completeness of a trial basis from stable lower bounds, and it supplies no stationary inverse or existence theorem.

## Statement, spaces and hypotheses

Use Lebesgue measure dx on R2 and the real homogeneous norm

 H(F)=sup{|integral F phi dx| : phi in C_c^infty(R2), ||grad phi||2<=1}.

This is the norm of F as a continuous functional on the gradient completion of C_c^infty, with constants identified. Let F be a real locally integrable function with finitely many positive angular sine modes F(r,theta)=sum_n f_n(r) sin(n theta), n>=1, and suppose integral_0^infty r^3 f_n(r)^2 dr<infinity for every mode. S1 means that only positive odd n occur. The result also holds without oddness. Set

 A_F(r,theta)=-e_theta r sum_n f_n(r) cos(n theta)/n,
 M2=||A_F||2^2=pi sum_n n^-2 integral r^3 f_n^2 dr.       (1)

Take a real smooth function psi with finitely many positive sine modes, grad psi in L2, belonging to the same gradient completion, and r Delta psi in L2. In particular the exact rational trial functions stated below meet these hypotheses. Define A_(Delta psi) by the same angular formula and put

 Z_psi=A_(Delta psi)-grad psi,
 a=||Z_psi||2^2,
 b=<A_F,Z_psi>,
 p=integral F psi dx, d=||grad psi||2^2.                 (2)

The pairing is the ordinary absolutely convergent integral for the trial functions below. For every real t,

 H(F)^2 <= M2+2t b+t^2 a.                              (3)

If a>0, this gives the sharper certified upper bound

 H(F)^2 <= M2-b^2/a.                                   (4)

For several trial functions psi_i and arbitrary real coefficients t_i, the bound is M2+2 sum_i t_i b_i+sum_ij t_i t_j <Z_i,Z_j>. Its Gram matrix is positive semidefinite. If the psi_i have different individual angular frequencies n_i, the Z_i are orthogonal and

 H(F)^2 <= M2-sum_i b_i^2/a_i                           (5)

whenever all a_i>0. The M2 in every formula contains ALL modes of F, including any mode absent from the chosen tests. These statements do not require a Galerkin solve, optimal coefficients or an estimate of an omitted projection.

## Proof of the norm upper bound and admissibility

For any compact smooth phi, integration in theta gives

 -integral A_F dot grad phi dx=integral F phi dx.

The tangential field has no radial boundary term on any annulus. Since A_F is in L2 and F is locally integrable, shrinking the inner radius and increasing the outer radius proves div A_F=F in distributions. Cauchy-Schwarz proves H(F)<=||A_F||2 and extends the pairing continuously to the gradient completion.

Exactly the same argument gives div A_(Delta psi)=Delta psi. Therefore div Z_psi=0 and div(A_F+t Z_psi)=F. Testing this latter field and applying Cauchy-Schwarz proves (3). Expanding the square proves its stated coefficients. If a>0, completing the square yields M2-b^2/a+a(t+b/a)^2, so t=-b/a proves (4). A vector of coefficients proves the Gram variant. Different angular frequencies are orthogonal in both the radial and tangential components, proving (5). For an untested mode, its full contribution to (1) is retained.

For the stated smooth tests, angular Hardy gives ||psi/r||2<=||grad psi||2 because each n>=1. Thus integral |F psi|<=||rF||2 ||psi/r||2<infinity. The angular integration identity therefore yields <A_F,grad psi>=-p without a missing boundary term. The same argument and approximation in the gradient completion give <A_(Delta psi),grad psi>=-integral Delta psi psi=d. Hence

 a=||A_(Delta psi)||2^2-d,
 b=<A_F,A_(Delta psi)>+p.                              (6)

No contact term is introduced at the origin: psi is smooth there, and the distributional angular right inverse has no radial flux.

## Positive one-mode formulas without subtracting large energies

Let psi=u(r) sin(n theta) and put y=log r, v(y)=u(exp y). Suppose v,v',v'' decay at both ends and belong to L2(dy). All trial functions below satisfy these conditions. Polar differentiation gives

 d=pi integral [v'^2+n^2 v^2] dy,
 ||A_(Delta psi)||2^2=(pi/n^2) integral (v''-n^2 v)^2 dy.

Integration by parts, using v v' tending to zero, yields

 a=(pi/n^2) integral v''^2 dy+pi integral v'^2 dy.       (7)

Thus a>0 for every nonzero such trial function. A zero a would force v'=0, hence a constant v, whose L2 membership forces v=0. In (6) the angular term cancels p exactly, giving

 b=(pi/n^2) integral_0^infty r f_n(r) [r^2 u''(r)+r u'(r)] dr.
                                                               (8)

This cancellation is analytic before any ball arithmetic. Formula (7) is positive and does not estimate a by subtracting two nearly equal enclosures. Formula (8) uses only the n-th mode of F; its integral is absolutely convergent by Cauchy-Schwarz applied in the y variable.

## Exact rational representation used by the current trial family

Write t=r^2/(1+r^2), w=1-t. A single-mode trial is

 u(r)=sum_(beta,k) x_(beta,k) r^3(1+r^2)^(-beta) t^k,

with finitely many exact rational x,beta, integer k>=-1, beta>3/2, and 3+2k>=n with 3+2k-n even. These conditions make each term smooth at the origin: r^(3+2k) sin(n theta) is a polynomial in x,y times a nonnegative integral power of r^2. At infinity u and its logarithmic derivatives have magnitude O(r^(3-2 beta_min)); this is square integrable in dy. The radial cutoffs from T4-466 have squared gradient error O(R^(6-4 beta_min)), tending to zero. The same decay gives r Delta psi in L2. Thus all hypotheses above hold.

Group b=beta-1>1/2 and write P_b(t)=sum_k x_(beta,k) t^(k+1). Then u=r sum_b w^b P_b. To avoid confusion with the scalar b in (2), call the differential polynomial operator

 D_b P=(1-2 b t)P+2t(1-t)P'.                           (9)

Direct differentiation proves u_y=r sum_b w^b D_b P_b and u_yy=r sum_b w^b D_b(D_b P_b). Since dy=dt/[2t(1-t)], (7) becomes

 a/pi=(1/2) sum_(b,c) integral_0^1 w^(b+c-2)
       [ D_b^2 P_b D_c^2 P_c/n^2 + D_b P_b D_c P_c ] dt. (10)

Here D_b^2 means composition of the operator, not pointwise squaring. Every exponent b+c-2>-1 and all coefficients are rational. The integrals of each monomial are exactly rational: for q>-1,
 integral_0^1 t^j(1-t)^q dt=j! / product_(i=1)^(j+1)(q+i).
Consequently a/pi is an exact positive rational for every nonzero exact trial vector.

If the source mode is serialized as f_n=r sum_ell w^(ell delta/2) A_(ell,n)(t), where delta and polynomial coefficients are exact rationals, then (8) is

 b=(pi/(2n^2)) sum_(ell,b) integral_0^1
     w^(ell delta/2+b-3) t A_(ell,n)(t) D_b^2 P_b(t) dt. (11)

Before termwise integration, group equal exponents and whole polynomials and certify every endpoint cancellation. If q is the exact order of vanishing at t=1 of its whole polynomial, require ell delta/2+b-3+q>-1. Expand in w only after cancellation. Such a certificate gives a rational value of b/pi when all exponents are rational. If approximate floating serialized exponents are involved, they must first be bound to the exact input, as with all previous moment certificates. Formula (11) is a proposed additional numerical integral, not an assertion that current N4 pairings have evaluated it.

## Directed use and a check with a known solution

For a nonzero one-mode test, if a rigorous M2 upper U, an a upper A>0 and a lower |b|>=B>=0 are available, then (4) yields H(F)^2<=U-B^2/A. For distinct modes these corrections add. Alternatively, choose any exact rational t and enclose the quadratic (3) directly. A numerical choice of t or a numerical trial vector is a proposal only; once its coefficients are frozen as exact rationals, every test is admissible. No numerical optimality is required.

The identity has an exact test independent of an optimization. For F=-Delta psi, its Riesz representative is psi, so H(F)^2=d: Cauchy-Schwarz gives the upper bound, and compact cutoff approximations to psi/sqrt(d) give the lower bound. Then A_F=-A_(Delta psi), M2=||A_(Delta psi)||2^2=d+a and b=-a, so t=1 in (3) gives equality d. This also verifies the sign of b and the factors pi and n^2.

Two manufactured modes will be checked from exact rational JSON. First u_1=r/(1+r^2)^(3/2) has d/pi=3/8, M2/pi=3/4 and a/pi=3/8. Second u_3=r^3/(1+r^2)^3 has d/pi=6/35, M2/pi=64/315 and a/pi=2/63. For F=-Delta(psi_1+psi_3), the two independent corrections recover H(F)^2/pi=153/280 exactly. Keeping only the first test gives the valid upper1457/2520*pi, whose gap above the exact norm is2/63*pi. The omitted mode is covered explicitly, even though it is absent from the chosen correction space. These values will be checked using separate direct polar Laplacian identities and exact beta moments.

## Dependencies and scope

The analytic input is elementary polar differentiation, distributional integration, Cauchy-Schwarz and the gradient-completion definition of H. The existing T4-466 proof supplies the exact trial family's cutoff convention and the current source serialization. N4-394 explains why finite basis stability alone is insufficient; it is not needed for the proof. The present correction replaces a particular angular right inverse by another right inverse with smaller L2 norm. It can sharpen the Hardy upper bound, while preserving full-plane and omitted-mode coverage.

No candidate016 upper value, actual E2 ordering, completeness of a trial basis, canonical strain/contact term, S1 linear inverse or a posteriori existence result is claimed. Independent Opus review is requested through the existing T1/T2 lanes. Their configured model is us.anthropic.claude-opus-5-5; the actual provider identity is not observable here. All numerical candidate use stays OPEN until its full exact inputs and integrals are independently checked.
