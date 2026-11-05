# An explicit first-commutator bound for the campaign weight

Status: proved analytic operator bounds. No transport-remainder or existence
claim follows without the additional integer divergence-form estimates.

Let D0=|D|, J=(1-Delta)^1/2, W(x)=sqrt(1+4|x|²), and let R denote the
joint vector Riesz transform, whose L2 norm is one. Then
\[
\boxed{\|[J,W]\|_{2\to2}\le4,\quad
\|[R,W]|D|\|_{2\to2}\le6,\quad
\|[\nabla J^{-1},W]J\|_{2\to2}\le6.}
\tag{1}
\]
These are bounds for this precise weight, without an unspecified Calderon
commutator constant. The proof works on the full scalar L2 space and does
not use S1.

## The homogeneous radial model

First take a(x)=|x|. In two dimensions the |D| commutator has kernel
\[
[|D|,a](x,y)=\frac1{2\pi}\frac{|x|-|y|}{|x-y|³}.
\]
Subtract its first linear approximation at x. The linear term has norm at
most one: it is the scalar product of x/|x| with the joint vector Riesz
transform, with an immaterial sign. The remaining kernel is negative,
with absolute value
\[
H(x,y)=\frac1{2\pi}\frac{|y|(1-\cos\theta)}{|x-y|³},
\]
where theta is the angle between x and y. This follows exactly from
\(|x|-|y|-\widehat x\cdot(x-y)=-|y|(1-\cos\theta)\).
There is no singular-integral remainder: near x=y its numerator is
quadratic in transverse displacement, so it is locally integrable.

Use the Schur weight w(x)=1/|x|, which is positive and finite almost
everywhere. Homogeneity and the substitution rho->1/rho make both Schur
ratios equal to
\[
\frac1{2\pi}\int_0^{2\pi}\int_0^\infty
\frac{1-\cos\theta}{(1+\rho²-2\rho\cos\theta)^{3/2}}\,d\rho\,d\theta=1.
\]
Indeed, for almost every angle,
\[
\int_0^\infty(1+\rho²-2\rho c)^{-3/2}d\rho=\frac1{1-c},\quad c=\cos\theta.
\]
One obtains this by integrating (rho-c)/[(1-c²)sqrt(1+rho²-2rho c)].
The endpoint angles follow by limits and have zero angular measure.
Positive Tonelli and Schur's test therefore give ||H||<=1. Adding the
linear Riesz term proves
\[
\|[|D|,|x|]\|\le2.
\tag{2}
\]
All identities may first be tested on smooth functions away from the origin.
The bounded extensions agree with the distributional commutator, by density.

## The regularized distance is a positive average of translations

For a>0 put
\[
P_a(y)=\frac{3a³}{2\pi(a²+|y|²)^{5/2}}.
\]
This is a probability density, with finite first moment. Its ordinary
Fourier transform is (1+a|xi|)exp(-a|xi|). For example, obtain it from the
two-dimensional Poisson density a/[2pi(a²+r²)^(3/2)] by applying
1-a partial_a; this differentiates exp(-a|xi|) to the displayed multiplier.
Consequently
\[
\sqrt{a²+|x|²}=\int|x-y|P_a(y)dy.
\tag{3}
\]
One direct verification takes transforms away from zero:
F(|x|)=-2pi|xi|^-3 and
F(sqrt(a²+r²))=-2pi(1+a|xi|)exp(-a|xi|)|xi|^-3 there. These formulas
follow by differentiating in a the elementary Gaussian-integral transform
F((a²+r²)^(-1/2))=2pi exp(-a|xi|)/|xi|. Any polynomial ambiguity is
constant, since both sides of (3) are radial and have the same at-most-linear
growth. Their values at zero are both a:
3a³ integral_0^infty r²(a²+r²)^(-5/2)dr=a. Thus (3) is an identity of
actual functions, not merely of transforms away from zero.

In particular W=2 integral |x-y|P_(1/2)(y)dy. Translation conjugation
preserves (2), and integration against this probability density gives
\[
\|[|D|,W]\|\le4.
\tag{4}
\]
This averaging is justified first in matrix elements of compactly supported
smooth tests, then by the uniform bound (2) and density.

Apply (3) in frequency space as well:
\(J=\int P_1(k)|D-k|dk\).
Frequency modulation conjugates |D| and commutes with W. Averaging (4)
therefore proves ||[J,W]||<=4. Although J itself is unbounded, its
commutator average is uniformly bounded; the identity is first valid on
Schwartz matrix elements and extends uniquely to L2.

## Vector Riesz and Bessel-gradient consequences

Since R|D|=grad up to the fixed harmless sign convention,
\[
[R,W]|D|=R[W,|D|]+[\nabla,W].
\]
The joint Riesz norm is one, and ||grad W||infty<=2. Equations(4) and this
identity give the second bound in (1). Similarly, with B=grad J^-1,
\[
[W,B]J=[W,\nabla]-B[W,J].
\]
Since ||B||<=1, its norm is at most2+4=6, proving the third bound. Signs
do not affect the stated norms. The proof supplies only these first
commutators; a second weight commutator cannot be inferred by squaring6.

The left-preconditioned bound is also at most6, since
J[W,B]=[J,W]B+[W,grad]. By adjoints the same constants apply to row
B* commutators on either side. For W_a=sqrt(1+a²r²), the averaging proof
scales to ||[J,W_a]||<=2a, and each B commutator with one J on either
side has norm at most3a. These auxiliary estimates hold for every a>0.
