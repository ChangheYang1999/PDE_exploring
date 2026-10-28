# Exact chordal periodic Hilbert seminorm

## Statement and hypotheses

Let 0<alpha<1 and let f be a continuous real-valued 2pi-periodic function. Define

    [f]_(alpha,ch) = sup_(x-y notin 2pi Z)
        |f(x)-f(y)| / |e^(ix)-e^(iy)|^alpha.

For finite seminorm, define the periodic Hilbert transform by the circular principal value

    Hf(x) = (1/(2pi)) pv integral_(-pi)^pi f(y) cot((x-y)/2) dy.

The exact operator seminorm is

    sup_[f]_(alpha,ch)>0 [Hf]_(alpha,ch)/[f]_(alpha,ch)
      = (2^(1-alpha)/pi) B((1-alpha)/2,alpha)
      = Gamma(alpha/2) Gamma((1-alpha)/2) / pi^(3/2).

The same equality holds for complex-valued functions with the absolute value seminorm. This is a statement about the increment seminorm, not the full supremum-plus-seminorm. The principal value is well-defined because the kernel cancellation leaves a local integrand bounded by a constant times |x-y|^(alpha-1).

## Checked source and reduction to one integral

The dependency is V. F. Babenko, Sharp Estimates for Norms of Functions from Conjugate Classes in Metrics C and L, arXiv:1402.0829v1, Theorem1(2) and Remark3. The actual local PDF and its extracted text are in ../sources/conjugate_sharp_2014.pdf and .txt. The theorem states the exact maximal increment of the conjugate function for any concave Dini modulus. Its normalization is the one above. It is an announcement; no claim is made here to supply the theorem's source proof.

Define omega(t)=(2sin(t/2))^alpha for 0<=t<=pi and omega(t)=2^alpha for t>=pi. It is continuous, increasing, concave and Dini. Concavity on [0,pi] follows by composing the concave nonnegative sine function with the increasing concave power. Its left derivative at pi is zero, so the constant extension remains concave. The periodic modulus class H^omega in the source is exactly the unit ball [f]_(alpha,ch)<=1: for t<=pi the maximum chordal distance among angular distances <=t is 2sin(t/2), while for t>=pi the whole circle has diameter2.

For h in (0,pi], put b=tan(h/4), so 0<b<=1. Babenko's exact increment formula uses the reciprocal tangent pairing

    tan(rho(u)/2) tan(u/2) = b^2,
    0<u<h/2<rho(u)<pi.

The matching identity and its branch are established in ../hilbert_periodic/PROOF.md. Substitution s=tan(u/2)/b gives rho(u)=2arctan(b/s), u=2arctan(bs), and F_h(u)du=2ds/(1-s^2). Therefore the exact maximum of the normalized increment at angular distance h is

    I_alpha(b) = (4/pi) integral_0^1 Q_b(s)^alpha ds/(1-s^2),

where

    Q_b(s) = sin(arctan(b/s)-arctan(bs)) / sin(2arctan b)
           = (1+b^2)(1-s^2) /
               [2 sqrt((s^2+b^2)(1+b^2s^2))].

The denominator here is the chordal output distance to the power one. The factor2 in omega and the factor2 in that output distance cancel. This calculation does not replace angular distance by chordal distance inside an already proved estimate; it applies the exact source formula to the correct new modulus.

## Sharp upper bound and limiting equality

For 0<s<1 and 0<b<=1, the exact identity

    (s^2+b^2)(1+b^2s^2)-s^2(1+b^2)^2 = b^2(1-s^2)^2

implies

    0<Q_b(s)<= (1-s^2)/(2s),
    lim_(b downarrow0) Q_b(s) = (1-s^2)/(2s).

Consequently the normalized integral is dominated by

    2^(-alpha) s^(-alpha)(1-s^2)^(alpha-1),

which is integrable at both endpoints precisely for 0<alpha<1. Dominated convergence and the sharp source formula give

    sup_(0<b<=1) I_alpha(b)
       = (2^(2-alpha)/pi) integral_0^1 s^(-alpha)(1-s^2)^(alpha-1) ds
       = (2^(1-alpha)/pi) B((1-alpha)/2,alpha).

Interchanging the suprema over input functions and increments is legitimate because both range independently over the same pairs. The upper bound holds for each b, and the source's equality supplies the lower bound for each b, so a single function attaining all increments is unnecessary. The gamma duplication formula gives the alternative expression in the statement.

For a complex input and any fixed output increment, multiply by a complex unit so that its real part equals its magnitude. The real projection has input seminorm at most the complex input seminorm and commutes with H. The real theorem proves the complex upper bound; the real subclass proves equality.

## Scope and verification status

The chordal and angular-geodesic seminorms are distinct, but their exact Hilbert operator constants are equal. Both suprema are approached by increments of angular length tending to zero. No planar Riesz or Beurling constant is inferred from this auxiliary one-dimensional result. The proof was written before any numerical evaluation. An independent analytic cross-read is pending; no new accepted numerical bound depends on this note.
