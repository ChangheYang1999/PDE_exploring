# Inner log-cell residual bounds without a small Green denominator

Date: 2026-10-20. This is a general enclosure theorem written before implementation. The application is OPEN until exact coefficients, canonical moments, all cells, remainders and output aggregation have passed independent audits. No numerical conclusion follows from this note alone.

## Statement and data

Use the exact normalized modal density and the canonical inverse in ../inner_majorant/PROOF.md. Their accepted verdict, exact coefficient JSON and canonical upper moments are dependencies, with hashes required in the application. Put R=exp(t_a), tau=log(r/R)<=0, k=1615536043799051/9007199254740992, c_l=1/k and c=3/k-1. Write

rho=r^3 sum_(j=0)^260 H_j(tau) sin((2j+1)theta),
H_j(tau)=C_j+sum_(l=0)^6 D_(j,l)exp((2l+2)tau)+exp(b_i tau)E_j(tau),

where b_i>=49, E_j has degree at most6 and all coefficients are exact rationals. C_0=C_1=1/4 and the other C_j vanish. Extend H by H_261=0 on the entire modal extension, including the exterior. The exact coefficient audit, not a rounded or sampled comparison, must establish this representation. The canonical normalization theorem gives c=psi_xy(0) exactly for this same density.

Let rho_0=x^2y and eta=rho-rho_0. For a finite list of exact rational cells covering -T<=tau<=0, the Taylor constructions below and complete angular convolution give rigorous upper bounds for the true stationary residual

epsilon=(c_l X+U[rho]) dot grad rho-rho.

The existing complete inner-majorant theorem supplies the remaining disk tau<=-T when evaluated at that exact T. The maximum of the valid cell and tail bounds then covers the whole inner disk. A partial list of cells does not imply this conclusion.

## Canonical moment identities

For m=2n, n=1,...,261, define

i_n(tau)=integral_(-infinity)^tau exp(-(m+4)(tau-s))H_(n-1)(s)ds,
j_n(tau)=integral_tau^infinity exp((4-m)(s-tau))H_n(s)ds.

Outside tau<=0 these definitions use the actual complete modal extension, not the inner formula. The integrals converge for the accepted modal trial. They solve

i_n'=-(m+4)i_n+H_(n-1), j_n'=(m-4)j_n-H_n.

The forcing and physical Green moments are

F_n=(H_(n-1)'+H_n'+(4-m)H_(n-1)+(4+m)H_n)/2,
f_n(r)=r^2 F_n(tau),
A_n=r^4[(H_(n-1)+H_n)/2-m i_n],
B_n=r^4[m j_n-(H_(n-1)+H_n)/2].

Here A_n=r^(-m)integral_0^r s^(m+1)f_n(s)ds and B_n=r^m integral_r^infinity s^(1-m)f_n(s)ds. To verify the formulas, insert f_n and integrate the H derivatives by parts. The lower boundary is zero because H is bounded near tau=-infinity. The upper boundary is zero by the already checked exterior decay. Direct differentiation also gives A_n'=-m A_n+r^4F_n and B_n'=mB_n-r^4F_n.

Every lower moment can be evaluated without small denominators. For a polynomial P and lambda=m+4+alpha>0, the polynomial q determined by q'+lambda q=P is

q_d=P_d/lambda, q_l=[P_l-(l+1)q_(l+1)]/lambda.

Its contribution to i_n is exp(alpha tau)q(tau). All such lower lambdas are at least6. For the upper moment, let j_n(0) be the pinned canonical boundary value. If tau=-s, s>=0, then

j_n(-s)=exp((4-m)s)j_n(0)
 +sum_alpha exp(-alpha s) integral_0^s exp((4-m+alpha)v)P_alpha(v-s)dv.

This is the exact split at0. Polynomial shifts P_alpha(v-s) are expanded by the finite binomial formula, with exact or outward-enclosed coefficients. It never requires division by 4-m+alpha. In particular the n=27, alpha=b_i term is evaluated as a finite integral even though b_i is nearly50.

For a polynomial P(v)=sum_l p_l v^l on [0,s], the integral is

integral_0^s exp(lambda v)P(v)dv=sum_l p_l s^(l+1)Phi_l(lambda s),
Phi_l(z)=integral_0^1 x^l exp(zx)dx.

At z=0, Phi_l=1/(l+1). For small z use the entire series sum_(q>=0) z^q/[q!(q+l+1)]. If terms through q=K are retained and |z|/(K+2)<1, the absolute tail is at most

|z|^(K+1)/[(K+1)!(K+l+2)] / [1-|z|/(K+2)].

Indeed the ratio of successive absolute terms is at most |z|/(K+2) after the first omitted term. For larger nonzero z, finite integration by parts gives Phi_0=expm1(z)/z and Phi_l=[exp(z)-l Phi_(l-1)]/z. Rounding and cancellation are enclosed; loss of accuracy is a failed useful enclosure, not a license to take midpoints. An independent method can instead integrate the polynomial antiderivative exp(lambda v)Q(v) at both endpoints, using the same entire series near zero.

## Remove the exact affine strain before modeling

The n=1 upper moment has the exact decomposition

B_1=2cr^2+Bhat_1,
Bhat_1=-r^2 integral_0^r f_1(s)/s ds.

The canonical strain formula c=(1/2)integral_0^infinity f_1(s)/s ds proves it. Thus Bhat_1 can be computed entirely from the inner density with denominators alpha+2>=2, and it obeys Bhat_1'=2Bhat_1-r^4F_1. For n>=2 put Bhat_n=B_n. Define

p_n=-(A_n+Bhat_n)/(2r^2), s_n=(Bhat_n-A_n)/(2r^2).

These are the coefficients of U_rem,r/r and U_rem,theta/r, where U_rem=U-(-cx,cy). There is no arbitrarily chosen strain in this definition. All higher B moments remain the canonical ones.

The exact identity (3c_l-c-1)rho_0=0 gives

epsilon=(c_l partial_tau-1)eta
 -c cos(2theta)partial_tau eta+c sin(2theta)partial_theta eta
 +(sum_n p_n cos(2n theta))partial_tau rho
 +(sum_n s_n sin(2n theta))partial_theta rho.

This identity removes the cubic residual before intervals or absolute values are introduced. It follows by writing the affine velocity in polar coordinates and subtracting the exact equation for rho_0. Each term retains all angular modes. The first three terms have frequencies at most523; the products at most1043. In particular merely overlapping an interval strain with 3/k-1 is insufficient: the exact normalization theorem is essential.

## Taylor models and the ODE remainder

Fix a cell a<=tau<=b<=0 with midpoint t_c=(a+b)/2, halfwidth h=(b-a)/2 and v=(tau-t_c)/h. A model (P,r) means f=P(v)+e, |e|<=r on |v|<=1, with interval coefficients containing the exact coefficients. The exponential-polynomial construction and product theorem in ../outer_cells/PROOF.md apply without a sign restriction on t_c or the exponent. Their proof only uses exp(lambda t_c)>0 and |lambda h|. Thus every H, rho, derivative and r^4F has an explicitly bounded Taylor model, including degree-six corrections.

For the primary construction, model A and Bhat by their physical Green ODEs. Its center B_n, n>=2, may be obtained directly from the canonical B_n(0) by

B_n(t_c)=R^4{exp(m t_c)[B_n(0)/R^4]
 +sum_alpha exp((4+alpha)t_c)integral_0^(-t_c)exp((4+alpha-m)v)F_(n,alpha)(v+t_c)dv}.

This follows by splitting the defining upper forcing integral at0. It uses the same finite Phi integral and encloses its polynomial shift. The lower A center is R^4 sum_alpha exp((4+alpha)t_c)q_(n,alpha)(t_c), where q solves q'+(m+4+alpha)q=F_(n,alpha). The n=1 Bhat center uses the negative polynomial solution with denominator alpha+2. These are equivalent to the density-moment formulas but use different integrands.

For the ODE construction, more generally suppose y'=lambda y+sigma G, with an enclosing center value y_0 and G represented by sum_(q=0)^Q g_q v^q+e, |e|<=r_G. Define ell=lambda h and

p_0=y_0, p_(q+1)=[ell p_q+sigma h g_q]/(q+1), q=0,...,Q-1.

Assume |sigma|<=1, as holds here. Then a valid degree-Q remainder is

r_y=exp(|ell|)[|ell p_Q+sigma h g_Q|/(Q+1)+h r_G].

For exact center and coefficient values, subtract the polynomial from the ODE in v. The error has zero initial value and forcing

[ell p_Q+sigma h g_Q]v^Q+sigma h e(v).

Variation of constants from0 to v, in either direction, bounds the kernel by exp(|ell|), the integral of |u|^Q by1/(Q+1), and the interval length by1. Interval coefficient choices enlarge the resulting bound. If y_0 is an interval, the exact center is one permitted coefficient p_0; no extra center uncertainty term is omitted. Multiplication by exp(-2(t_a+tau)) then gives p_n,s_n, with the complete product remainder retained. The largest physical ODE rate is522, not the density-moment rate526.

An independent construction can instead model i,j from their density ODEs and recover A,B algebraically using the displayed moment identities. Its largest ODE rate is526. For n=1 it must compute Bhat directly from its positive-denominator inner integral, or enforce the exact strain subtraction symbolically. The two ODE representations have the same exact solution by the proven identities, but different recurrences and intermediate rounding. A recorded rate must match the actual chosen representation.

## Complete angular convolution and publication

Apply the elementary identities cos(a)sin(b)=[sin(b+a)+sin(b-a)]/2 and sin(a)cos(b)=[sin(a+b)+sin(a-b)]/2, including negative-frequency signs. A primary full-frequency Laurent convolution and an independent compressed-index exact integer interval convolution are both described and proved in ../outer_cells/PROOF.md. No angular coefficient may be discarded. The coefficient-sum model norm bounds the product error because each product-to-sum identity has absolute coefficient sum at most1.

After adding the exact affine-strain linear terms, retain radial degrees0,...,Q and bound all higher degrees through2Q by their absolute coefficient sums. Any multiplication used to form p_n,s_n has already contributed its own truncation and product remainder. Transform retained polynomials to Bernstein form on [-1,1]; the maximum absolute Bernstein coefficient bounds the polynomial throughout the cell. The sum over all522 real sine modes, plus every discarded and nonpolynomial remainder, is a bound B_W for W=sum|epsilon_j| on the full cell.

Let u=r/L and m=u^3(1+u^2)^((k-3)/2). Since d log(m)/d log(r)=(3+ku^2)/(1+u^2)>0,

W/m<=B_W/m(R exp(a)),
(1+u)^delta W/m<=(1+R exp(b)/L)^delta B_W/m(R exp(a)), delta>=0.

The orthogonal-sine L2 annulus bound in ../outer_cells/PROOF.md also applies. It uses exactly dX/(1+u^2), and the integral of r/(1+(r/L)^2) is L^2 log(1+u^2)/2. Different radial cells have disjoint interiors, so squared bounds add. For a complete inner L2 conclusion, the missing disk must also have a separately proved bound; a supremum row alone does not automatically provide an integrated certificate.

A final numerical statement requires the exact adjacent partition, all endpoint and source hashes, finite arithmetic, complete remainder accounting, independent coefficient consistency checks and separate output aggregation. Both methods must individually have valid enclosures. An overlap is a consistency check, not a theorem proving either implementation correct. Publication uses a rational upper bound at least as large as both independent upper endpoints. No derivative norm, global inverse, distance to X3 or decisive endpoint is asserted here.

## Dependency contracts and the disk L2 join

The primary finite integral function `certify_inner.integ(P,offset,h,rate)` integrates exp(rate v)P(v+offset) from0 to h by the binomial shift and Phi recurrence. The independent `audit_inner_iv.integrate(p,offset,h,rate)` uses the same argument convention and a polynomial antiderivative at the endpoints, or an integrated exponential Taylor series with its absolute remainder. Thus the calls offset=t_c and h=-t_c have the required shift. At rate0, P=x^2, offset=-2 and h=3, both must enclose the exact value3. This test alone does not prove the contract; the displayed source formulas and their earlier audit establish it.

In the accepted T=0 inner-majorant evidence, upper_Green contains exactly260 rows n=2,...,261. Each j_boundary is j_n(0), and B_over_R4 is m j_n(0)-(H_(n-1)(0)+H_n(0))/2. This follows directly from the definitions used to construct the evidence, and the existing independent inner audit recomputed both quantities for every row. The present implementations check row indices and lengths before using them.

For a sine series epsilon=sum epsilon_j sin((2j+1)theta), orthogonality gives integral_0^(2pi)|epsilon|^2dtheta=pi sum epsilon_j^2<=pi W^2. Hence the annulus squared norm is bounded by pi M^2 L^2[log(1+u_b^2)-log(1+u_a^2)]/2 if W/m<=M there. If an accepted tail majorant proves W/m<=M_T on the complete disk0<r<=Rexp(-T), its squared norm is at most pi M_T^2 L^2 log(1+(Rexp(-T)/L)^2)/2. This follows by integrating the constant upper bound, and does not require taking a supremum over an unbounded log interval numerically. The origin has measure zero. Both interval engines must evaluate this scalar disk integral independently; its value must be added to the finite-cell squared bounds before the final square root.

For the planned application T=7, reuse the accepted B_5 from the old cutoff T_0=5/2. That theorem gives W<=B_5 r^5 on the entire larger disk, so it still holds on the smaller disk. The derivative of log(r^5/m) is at least2, hence its supremum on the smaller disk is B_5 exp(5(t_a-7))/m(exp(t_a-7)). This restriction does not assume that recomputing B_5 at a new radius preserves its numerical value. The same old constant is used throughout, and both engines take the larger accepted B_5 upper endpoint. The exact planned partition comprises25 cells of width1/5 from-7 to-2,19 cells of width1/10 from-2 to-1/10, and10 cells of width1/100 from-1/10 to0, for54 cells. Full computation and aggregation remain required.
