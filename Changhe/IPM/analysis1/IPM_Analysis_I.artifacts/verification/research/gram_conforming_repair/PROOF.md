# A continuous repair of the selected saved spline columns

## Statement fixed before computation

Let a compactly supported radial coefficient B(t) have consecutive
polynomial pieces P_i(t-a_i) on [a_i,a_{i+1}), i=0,...,s-1, where all
endpoints and coefficients are exact rationals. The two external support
traces are compared with zero. Put

    beta_0=beta_s=0,
    beta_i=(P_{i-1}(a_i-a_{i-1})+P_i(0))/2, 0<i<s.

On the i-th interval choose the unique affine polynomial d_i such that

    d_i(0)=beta_i-P_i(0),
    d_i(w_i)=beta_{i+1}-P_i(w_i), w_i=a_{i+1}-a_i.

Define Bhat=P_i+d_i on that interval and zero off the support. Then Bhat
is exactly continuous at every interval and support endpoint. For any
integer m>=0, hhat=x^2 y Bhat(log r) cos(2m theta) belongs to the diagnostic
weak-gradient space X, since its support is a compact annulus and its
piecewise first derivatives are bounded. Only C0, not C1, is asserted.

The original h may be outside X. In the following bound a subscript b
means the integral using piecewise classical derivatives. It is a broken
energy, not the norm of a distributional weak gradient.

Fix positive L and k<3/2 and set

    W(t)=exp(2t)(1+exp(2t)/L^2)^(3/2-k).

Let

    U=sum_i W(a_{i+1}) integral_0^wi [d_i^2+(3d_i+d_i')^2] ds,
    V=sum_i W(a_i) integral_0^wi P_i^2 ds.

For a nonzero B, V>0 and

    ||hhat-h||_{X,b} / ||h||_{X,b} <= sqrt(U/V),

uniformly for every single angular mode m. The left expression is explicitly
broken energy, not an X distance from an element h outside X. The finite
data calculation will certify a numerical upper bound only after both
independent arithmetic methods pass.

If a selected family has distinct increasing support starts and its
first-piece polynomial has degree at least2 with nonzero top coefficient,
then the repaired radial functions are linearly independent. They remain
so after replication in any finite set of angular modes. This does not
place them inside the original encoded span.

## Proof

The definition makes the left and right traces at a_i both equal beta_i.
At both support boundaries that value is zero. Distributional integration
by parts therefore has no circle measure. Compact annular support bounds
all positive weights and their inverses, proving X membership.

For Phi_m(theta)=cos^2(theta)sin(theta)cos(2m theta), write
A0=integral Phi_m^2>0 and A1=integral (Phi_m')^2>=0. Polar differentiation
and dxdy=exp(2t)dtdtheta give exactly

    ||x^2 y B(log r) cos(2m theta)||_{X,b}^2
      = L^6 integral W(t) [(A0+A1)B^2+A0(3B+B')^2] dt.

Because k<3/2, W is strictly increasing. Applying its endpoint extrema
on each interval gives the numerator at most L^6(A0+A1)U, since
A0<=A0+A1. The denominator is at least L^6(A0+A1)V, by discarding its
nonnegative radial-derivative contribution. Their ratio proves the bound.
All integrations defining U and V are exact polynomial integrations;
only the positive endpoint weights require interval enclosures.

For independence, choose the least support start among the radial
functions having a nonzero coefficient in a purported linear relation.
On a short interval before the next support start, it is the only such
function. Adding an affine correction cannot erase its nonzero coefficient
of degree>=2, so that function is not identically zero there. Its coefficient
must vanish, a contradiction. The angular independence follows by the
same nonzero-arc trigonometric argument as topic131.

## Finite verification plan and scope

Use every selected mode-zero interior spline in the two unique topic131
metadata sets. Verify consecutive pieces, endpoint ordering, distinct
support starts, and nonzero degree>=2 first-piece coefficients. Form all
beta_i and d_i exactly. Check every repaired endpoint trace and integrate
the polynomial squares exactly. Method1 uses rational Horner evaluation,
coefficient convolutions and Arb512 endpoint weights. Method2 independently
decodes binary64 bits, evaluates direct power sums, computes polynomial
integrals by monomial double sums, and encloses weights with mpmath.iv.
Compare the resulting rigorous per-column ratio bounds.

The numerical constants are the exact dyadics
L=8614738245908811/1125899906842624 and
k=1615536043799051/9007199254740992, linked to the already checked trial.
No statement transfers the raw matrix to this repaired space. The velocity
and operator action, matrix entries, Gram whitening, condition numbers,
actual singular values, full inverse and nonlinear PDE remain unverified
for the repair. It is a constructive finite conformity result only.
