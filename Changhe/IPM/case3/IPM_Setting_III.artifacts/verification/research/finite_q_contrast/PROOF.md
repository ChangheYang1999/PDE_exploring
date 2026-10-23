# Global angular contrast of a finite Q interpolant

Date: 2026-10-20. Status: CONFIRMED algebraic identity and coefficient bound.
Numerical evaluations of the integral are separate, non-certified evidence.

## Statement

Let a finite smooth Q interpolant be given by
\[
 r=\frac{L\sqrt\sigma}{[2(1-\sigma)]^\kappa},\quad
 \rho(r,\theta)=r\sin\theta(1-\sigma)
       \sum_{k=0}^{M-1}\sigma^k B_k(2\sigma-1)\cos(2k\theta),
\]
where \(L>0\), \(\kappa>1\), \(B_k(t)=\sum_j b_{kj}T_j(t)\)
are real polynomials, and \(a=B_0(-1)\ne0\).
Define \(q=\rho/(ay)\), including its smooth axis values, and the
angular contrast \({\cal A}(q)\) as in result55. Set
\[
 P(\sigma,\theta)=\sum_{k=1}^{M-1}\sigma^kB_k(2\sigma-1)\cos(2k\theta),
 \quad A_k=\sum_j|b_{kj}|,
 \quad I_k=\frac1{2k(k+1)}+\frac\kappa{k+1}.
\]
Then the exact infinite-radius integral is
\[
 {\cal A}(q)=\frac1{|a|}\int_0^1
   \left(\frac1{2\sigma}+\kappa-\frac12\right)
      \operatorname{osc}_{[0,\pi/2]}P(\sigma,\cdot)\,d\sigma, \tag{1}
\]
and the following global upper bound holds:
\[
 {\cal A}(q)\le\frac2{|a|}\sum_{k=1}^{M-1}A_k I_k.             \tag{2}
\]
This bound involves all radii and is independent of the map scale \(L\).

Suppose an equally spaced angular grid includes both endpoints, with mesh
width \(h\), and \(\operatorname{osc}_h\) means its sampled oscillation.
Let \({\cal A}_h\) be (1) with that sampled oscillation but with the
radial integral still exact. Then
\[
 0\le {\cal A}(q)-{\cal A}_h
   \le\frac{2h}{|a|}\sum_{k=1}^{M-1}kA_k I_k.                 \tag{3}
\]
A floating-point radial quadrature does not by itself compute
\({\cal A}_h\) with a rigorous error, so (3) is not automatically an
interval enclosure of that output.

The signed third angular moment can also be computed without a far box:
\[
 J=\int_0^\infty\frac{\rho_3(r)}{r^2}\,dr
  =\int_0^1\left(\frac14+\left(\frac\kappa2-\frac14\right)\sigma\right)
       [B_1(2\sigma-1)-\sigma B_2(2\sigma-1)]\,d\sigma.       \tag{4}
\]
Missing \(B_k\) are zero. Its partial integral up to any radius is the
same polynomial integral with upper endpoint \(\sigma(r)\).

## Proof

The map is strictly increasing from zero to infinity and
\[
 \frac{d\log r}{d\sigma}=\frac1{2\sigma}+\frac\kappa{1-\sigma}.
\]
The term \(B_0\) is independent of angle and does not affect oscillation.
Since \(1-\sigma>0\),
\(\operatorname{osc}q=(1-\sigma)|a|^{-1}\operatorname{osc}P\).
Changing variables gives (1). Its apparent singularity at zero is
integrable since \(P=O(\sigma)\) uniformly in angle. At \(\sigma=1\)
all polynomials and the remaining weight are bounded.

For \(-1\le t\le1\), \(|T_j(t)|\le1\), hence \(|B_k(t)|\le A_k\).
The oscillation of a sum is at most the sum of the oscillations, and
\(\operatorname{osc}\cos(2k\theta)\le2\). Thus
\(\operatorname{osc}P\le2\sum A_k\sigma^k\).
Integrating this bound gives (2), because
\[
 \int_0^1(1/(2\sigma)+\kappa-1/2)\sigma^k\,d\sigma=I_k.
\]
For (3), every point of the angular interval is within \(h/2\) of a
grid point. The derivative bound
\(|P_\theta|\le2\sum kA_k\sigma^k\) therefore bounds the difference
of the two oscillations by \(2h\sum kA_k\sigma^k\). Integration proves
(3). These are deliberately global coefficient bounds; cancellation in
the represented polynomial can make them much larger than the contrast.

Finally \(\sin\theta\cos(2k\theta)
 =[\sin((2k+1)\theta)-\sin((2k-1)\theta)]/2\).
Only \(k=1,2\) contribute to \(\rho_3\), giving
\[
 \rho_3/r=(1-\sigma)(\sigma B_1-\sigma^2B_2)/2.
\]
Multiply by \(d\log r\) and simplify to obtain (4).
The canonical strain identity is \(c=-a/4+J\). For a finite interpolant
with a nonzero center defect it is this actual \(-c/a\), not necessarily
\((\ell-1)/a\), which enters the contrast identity in result55.

## Scope and evidence

These formulas apply to the encoded finite function irrespective of
whether it solves transport. The upper bound (2) can be evaluated from
exact binary coefficients using rational arithmetic. Radial and angular
refinement of (1) gives numerical convergence evidence, not a proof of
its computed digits. Formula (4) is a polynomial integral; Gauss
quadrature of sufficient degree is algebraically exact, with floating
point rounding still separate. None of these observations proves a
candidate limit or an affine-range law for a family of iterates.
