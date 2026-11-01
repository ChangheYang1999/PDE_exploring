# A shifted negative cycle can have a positive-real singularity

Status: complete counterexample. This refutes an inference from a shifted coefficient cycle; it makes no assertion about the actual IPM coefficients.

## Statement, hypotheses and notation

Let a>0. Write n=3k+s uniquely with k>=0 and s in {1,2,3}, and set

    F_n(theta)=(-a)^k sin((2k+1)theta).

Let x_n be its vector of positive odd sine coefficients, with zero padding. Let T shift this vector one position to the right, so that T sends the coefficient of sin((2j+1)theta) to that of sin((2j+3)theta). Then, for every n>=4,

    x_n=-a T x_(n-3).

Thus the least-squares multiplier against the shifted preceding vector is exactly -a and the relative residual is exactly zero. Nevertheless the scalar generating series U(z,theta)=sum_(n>=1)F_n(theta)z^n has a positive-real pole at z=a^(-1/3) when theta=pi/2. In particular, a negative multiplier after a Fourier-mode shift does not imply that all nearest singularities have arguments60,180,300 degrees or avoid the positive real axis. One may take a=229/10000 to match the reported approximate multiplier magnitude.

## Complete proof

For n=3k+s with k>=1, shifting x_(n-3) raises its only frequency from2k-1 to2k+1 and leaves its amplitude(-a)^(k-1) unchanged. Multiplication by -a gives x_n. The Euclidean projection multiplier is therefore exactly-a, and the projection residual is zero. All vectors are nonzero, so both normalized diagnostics are defined. Every F_n is a finite real odd-sine polynomial, with frequency bounded linearly in n. A logarithmic-column representation may place every coefficient in column0.

For |az^3|<1, the geometric series converges absolutely and

    U(z,theta)=(z+z^2+z^3) sum_(k>=0)(-az^3)^k sin((2k+1)theta)
              =(z+z^2+z^3)(1-az^3)sin(theta)
                /[1+2az^3 cos(2theta)+a^2z^6].

The identity follows by writing sine as the difference of its two complex exponentials and summing each geometric series. At theta=pi/2, sin((2k+1)theta)=(-1)^k. Hence directly, without any cancellation ambiguity,

    U(z,pi/2)=(z+z^2+z^3)/(1-az^3).

The numerator is strictly positive at z=a^(-1/3)>0 and the denominator has a simple zero there. This is a genuine positive-real pole and is on the circle of convergence.

More generally the complex exponential branches have denominators1+az^3 exp(2i theta) and1+az^3 exp(-2i theta). Their possible poles depend on theta. Dropping the phase from the Fourier shift changes these equations and does not preserve the pole locations. This proves the assertion.

## Scope and dependencies

This example need not solve the IPM recurrence. Its purpose is to test the logical implication proposed from a numerical diagnostic. It satisfies that diagnostic exactly for every order, more strongly than the finite approximate data, while violating the proposed conclusion. Additional information from the IPM equations would be needed to locate actual singularities. Finite residuals near a shifted cycle also do not prove its persistence, a limiting multiplier, or the existence of any limiting singularity. No external theorem beyond the geometric series is used.
