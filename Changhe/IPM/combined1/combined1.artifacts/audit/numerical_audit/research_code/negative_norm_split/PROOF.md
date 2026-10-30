# Exact radial splitting of the homogeneous negative norm

## Statement and assumptions

Let F be a finite real sum of odd sine modes on R2,

F(r,theta)=sum_n f_n(r)sin(n theta),
f_n(r)=r t^m sum_i u^(b_i) Q_i(u),
m=(n-1)/2, u=(1+r²)^-1, t=1-u,

where n>=1 is odd, Q_i are rational polynomials and b_i>3/2 are rational. The sum over i may differ between modes. The endpoint factors of each term have already been absorbed into b_i. These hypotheses imply regularity of the angular mode at zero and membership in dotH^-1, by the absolute-convergence proof in exact_negative_norm/PROOF.md.

Fix R>0 and U=(1+R²)^-1. Write F_in=F 1_(r<R) and F_out=F 1_(r>=R). Both belong to dotH^-1. Define

A_i(u)=(1-u)^n Q_i(u)=sum_k a_ik u^k,
D_j(u)=sum_l q_jl u^l/(b_j+m-1+l).

For a mode n, let P_ij=A_i D_j, with coefficient p_ijk of u^k. Its full and exterior squared norm contributions are

E_n = (pi/(4n)) sum_(i,j,k) p_ijk/(b_i+b_j-3+k),
O_n(R) = (pi/(4n)) sum_(i,j,k)
             p_ijk U^(b_i+b_j-3+k)/(b_i+b_j-3+k).        (1)

Define alpha_ik=b_i-m-2+k and X_jl=b_j+m-1+l, and set

I_n(R)=(1/2) sum_(i,k) a_ik L(alpha_ik,U),
L(alpha,U)=(1-U^alpha)/alpha if alpha!=0, and -log U otherwise,
J_n(R)=(1/2) sum_(j,l) q_jl U^X_jl/X_jl.

Then the cross contribution to the squared full norm is

C_n(R)=(pi/n) I_n(R)J_n(R),                             (2)

and the interior squared norm contribution is E_n-O_n-C_n. The totals are obtained by summing over n. A cross contribution need not be positive for a signed radial source; the full, interior and exterior squared norms are nonnegative.

## Proof

Use the Green kernel (min(r,s)/max(r,s))^n/(2n), with full-circle factor pi. The two triangular halves agree by interchange of r and s, so the exterior squared norm is

(pi/n) integral_R^infinity r^(1-n)f_n(r)
                     integral_R^r s^(n+1)f_n(s) ds dr.

For inner branch i the second integral becomes

(1/2) integral_u^U v^(b_i-m-3) A_i(v) dv.

For outer branch j the first measure becomes

(1/2) u^(b_j+m-2)Q_j(u)du.

For X>0 and X+alpha>0, absolute convergence and interchange of integration give

integral_0^U u^(X-1) integral_u^U v^(alpha-1)dv du
 = U^(X+alpha)/[X(X+alpha)].

The identity also holds at alpha=0; it follows directly from the double integral and introduces no division by alpha. Here X=X_jl>0 and X+alpha=b_i+b_j-3+k+l>0. Finite expansion proves the exterior formula in (1). Setting U=1 gives the full norm.

For disjoint radial supports r<R<s, the kernel separates as r^n s^-n/(2n). Both orders of the two supports contribute, giving pi/n times the product

integral_0^R r^(n+1)f_n(r)dr
and integral_R^infinity s^(1-n)f_n(s)ds.

The same coordinate change gives precisely I_n and J_n, proving (2). Bilinearity gives the interior expression. Mode orthogonality proves the total formulas. The possible jump of F_in or F_out at the circle creates no source measure; these are ordinary measurable functions, not derivatives of their indicator functions.

## Independent normalization check

Take n=1 and f(r)=r/(1+r²)^2, so b=2 and Q=1. Direct differentiation gives the full potential p(r)=log(1+r²)/(4r), with its regular continuation at zero. Direct integration yields the full norm pi/8.

At R=1, the exterior potential for r>=1 is

p_out(r)=[log(1+r²)-log 2+1/2]/(4r).

For r<=1 it is r/8. The values and first derivatives agree at one, and the radial equation has source f outside and zero inside. Integrating f p_out over r>=1 gives 3pi/32. The cross term is pi(log 2-1/2)/8, leaving interior norm pi(3-4log 2)/32. The implementation checks all four expressions before a campaign calculation.

## Numerical evaluation and scope

All source coefficients and exponents start as exact rational values. Powers of the positive rational endpoint, logarithms, polynomial products and sums are evaluated with outward Arb arithmetic. For small alpha the expression L is evaluated through expm1(alpha log U) to avoid subtracting nearly equal numbers. No quadrature or asymptotic truncation is used.

The optional binary64 radius parser converts the exact binary value of N1's supplied radius to a rational. This ensures that comparison with its diagnostic uses the same circle, not merely the same printed decimal. The input and prior full-norm hashes, all mode contributions, precision and actual runtime are recorded. Agreement of a floating diagnostic is not a rigorous certificate for its quadrature; the exact split provides a separate reference against which its errors can be measured.
