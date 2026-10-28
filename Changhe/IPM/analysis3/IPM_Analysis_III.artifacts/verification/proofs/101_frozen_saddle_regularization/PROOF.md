# Regularization of the selected frozen saddle inverse

## A weighted cylinder realization

Let A>0, D=2A+1, Sigma=A+D, and beta>0. On the cylinder R_t x R_z define

 P_beta=-A partial_t+Sigma z partial_z-c,
 c=1+A beta.

For a real number lambda put H_lambda=L2(exp(lambda t)dt dz), and give P_beta its maximal distributional domain. Suppose

 kappa_lambda=c+Sigma/2-A lambda/2>0.                    (1)

Then P_beta is bijective on H_lambda, with

 P_beta^(-1)F=-integral_0^infinity S_tau F d tau,
 S_tau F(t,z)=exp(-c tau)F(t-A tau,exp(Sigma tau)z),       (2)
 ||P_beta^(-1)||_(H_lambda->H_lambda)<=1/kappa_lambda.

Let s>=0 and suppose

 kappa_s=c+Sigma/2-s Sigma>0.                            (3)

If u belongs to H_lambda and P_beta u=F in distributions, with F in H_lambda intersect H^s(R^2), then u belongs to H^s(R^2), without any prior high-regularity assumption, and

 ||u||_H^s<=||F||_H^s/kappa_s.                           (4)

Here H^s is the ordinary inhomogeneous Bessel-potential space with Fourier weight (1+xi^2+zeta^2)^s and Lebesgue measure dt dz. The norm in (4) has exactly this convention; a change to polar-cylinder charts has a separate equivalence constant.

## Proof of the realization and selection

Changing variables t'=t-A tau, z'=exp(Sigma tau)z gives exactly

 ||S_tau F||_H_lambda=exp(-kappa_lambda tau)||F||_H_lambda.

The same formula for negative tau defines a strongly continuous group. To verify strong continuity, first use smooth compactly supported functions, then their density and the locally uniform group bound. Conjugation by exp(lambda t/2) reduces the generator to a constant t-translation plus the z-dilation generator and a constant. On either half-plane z>0 or z<0, the further change z=+/-exp(v) and unitary multiplication by exp(v/2) gives the constant-coefficient operator

 -A partial_t+Sigma partial_v-kappa_lambda.

Its maximal domain is its group-generator domain: Fourier transformation in (t,v) identifies both with the set on which multiplication by -i A xi+i Sigma eta-kappa_lambda is square integrable. The set z=0 has measure zero. No distribution supported there can be a nonzero H_lambda function. Testing across z=0 gives the same maximal domain, since z partial_z has zero normal coefficient there. One may justify the last statement directly with cutoffs in log|z|: their commutators with z partial_z are uniformly bounded and tend to zero strongly, while the cutoffs converge strongly to the identity. Thus the quadrant realizations glue without an additional trace condition.

The convergent Bochner integral in (2) is in the generator domain because

 S_h u-u=integral_0^h S_tau F d tau.

After division by h this converges to F. If P_beta u=0, the group satisfies S_tau u=u, and the strictly decaying norm forces u=0. This proves existence, uniqueness and the stated low bound.

## Proof of high regularization

Fourier transformation of the translated and dilated function in (2), followed by zeta'=exp(-Sigma tau)zeta, gives

 ||S_tau F||_H^s^2
 =exp(-(2c+Sigma)tau) integral
   (1+xi^2+exp(2 Sigma tau)zeta'^2)^s |Fhat(xi,zeta')|^2 dxi dzeta'.

For tau>=0 the weight is at most exp(2s Sigma tau)(1+xi^2+zeta'^2)^s. Hence the integral in (2) converges in H^s under (3), with the bound (4). Its truncated integrals also converge in H_lambda to the unique low solution. Both convergences imply convergence in distributions on compact sets, so the two limits are the same distribution. This identifies the high solution with the prescribed low solution. It does not assume that the latter was already in H^s.

## Application to the frozen x-axis corner

Let L00=-A x partial_x+D y partial_y-1 and work in x>0. Set

 t=log x, z=y/x, h(x,y)=x^beta u(t,z).

The Jacobian is dx dy=x^2 dt dz, and direct differentiation gives

 x^(-beta)L00 h=P_beta u.

For the near-origin remainder weight |x|^(-2a), the norm of h becomes exactly the H_lambda norm of u, where

 lambda=2(beta+1-a).

For a=17/4, beta=3+delta, condition (1) becomes

 kappa_lambda=1+(D-A)/2+aA>0.

Condition (3) is precisely

 s<3/2+delta A/Sigma,                                   (5)

using D=2A+1. Thus the sharp upper threshold previously exhibited by the counterexample in proof 77 also gives a genuine regularization theorem for the selected frozen inverse in this cylinder chart.

For the actual rational rates k=1615536043799051/9007199254740992, A=2/k-1, D=4/k-1, take delta=9/5 and s=41/20. Then beta=24/5, lambda=31/10, and

 kappa_s=1+24A/5-31 Sigma/20 > 0.97260878319.

The exact rational value is in the verification evidence. This bounds the inverse in this chart by 1/kappa_s. The limiting value s=3/2+delta A/Sigma is not included.

For a local statement, choose a bounded cutoff chi smooth on the punctured polar blow-up, supported in a bounded x-axis cone |z|<=z0 and in r<1, with bounded V00.grad chi. If h is a low R solution and

 F_chi=x^(-beta)[chi L00 h+(V00.grad chi)h]

belongs to H^s(dt dz), then u_chi=x^(-beta)chi h belongs to H^s with (4). Its membership in H_lambda and that of F_chi follow from the low graph domain and bounded cutoff commutator. This proves local regularization from a regular localized right side. It does not supply high regularity of the transition term (V00.grad chi)h; a global proof must propagate that regularity from adjacent regions.

On a bounded z interval, the change to the usual polar coordinates is theta=arctan z and log r=t+(1/2)log(1+z^2). Multiplication by x^beta/r^beta=(1+z^2)^(-beta/2) is smooth with bounded derivatives of each fixed order. These maps identify the local H^s class with that of r^(-beta)chi h. Their operator norm is not asserted to be one. Parity extension gives the corresponding statement near the negative x-axis.

## Scope

This is a low-to-high regularization theorem for the frozen scalar saddle, not merely an a priori estimate on smooth solutions. It supplies the correctly directed x-axis step of the proposed high inverse. It does not prove regularization for the full variable IPM operator, does not handle the factored vertical-axis jet, and does not propagate the cutoff transition regularity. The threshold counterexample in proof 77 and the present sufficient estimate are compatible and use the same cylinder origin weight.
