# Full weighted Laplacian of the exact candidate 007

## Statement, reference and scope

Let c=4076476460239181/2251799813685248, delta=1-1/c and A=1+1/c.
The exact candidate is C1-N1-007-d2w-j7-e2bal. Its canonical potential
has SHA-256 153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316.
Set rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), and
F=(cX+u).grad rho-rho on R². The full-circle angular measure is dtheta.
For a>=0, define

    N(a) = ||(1+r²)^((2-a)/2) Delta F||_(L²(R²)).

The computation encloses this full norm, including every angular mode
of the exact residual, at a=0,1/5,2/5,3/5,4/5. Additional quarter points
and A are used for comparison with the previously verified selected-mode
calculation and for continuous cell tests. The exact input, code,
precision, all modes and all outward enclosures are recorded in JSON.
No numerical result is asserted in advance by this proof.

The conditional dyadic application uses exactly FW-T-DYADIC-Y-v1,
including its smooth radial cutoff plateaus, unitary Fourier convention,
positive low rate, high inverse and contraction-radius hypotheses. Let
Y be the space in ../projected_laplacian_audit/PROOF.md. The independently
reviewed plateau argument and inverse-floor/radius argument give

    Y(F) >= 5^((a-2)/2) N(a),
    closure requires Y(F) < B(a),
    B(a) = sqrt(8 pi) (1+c-ca)²/(1+a),    0<a<A.             (1)

Thus failure of the necessary scalar test excludes only this registered
scheme and reference. Passing the scalar test is not a closure result,
because its left side is only a lower bound for Y(F).

## Exact finite angular and radial construction

The independently assembled full residual has the finite representation

    F = r sum_(ell,n) v^(ell delta/2) P_(ell,n)(t) sin(n theta),
    t=r²/(1+r²), v=1-t.

Its coefficients are exact rational polynomials. The assembly retains
all linear terms and all potential-product terms; the packed convolution
is an exact rational polynomial multiplication, as proved and separately
checked in ../whole_plane_norms/PROOF.md. The cache is accepted only with
the matching exact source hash and assembly record. Its finite support
supplies the complete angular mode list. The nonlinear product can have
more modes than the input potential; no cutoff at the input degree is used.

For each complete sine mode, differentiate this representation in Cartesian
coordinates twice, verify equality of both mixed derivatives, and add
F_xx+F_yy. Independently check the identity

    Delta [r v^d P(t) sin(n theta)]
       = r v^(d+1) L(t) sin(n theta),
    t L = T_d(T_d P)-n²P,
    T_d P = (1-2dt)P + 2t(1-t)P',   d=ell delta/2.           (2)

Indeed r partial_r of r v^d P is r v^d T_d P, and the polar
Laplacian is r^-2((r partial_r)²+partial_theta²). Since
r^-2=v/t, (2) follows. Exact equality with the Cartesian trace verifies
both the normalization and cancellation of every unwanted frequency.
The necessary division by t is checked as a polynomial identity, not
performed as a numerical division near the origin.

Full-circle sine orthogonality and r dr=dt/(2v²), r²=t/v give

    N(a)² = (pi/2) sum_n sum_(ell,k)
      integral_0^1 v^(a+(ell+k)delta/2-3)(1-v)
        L_(ell,n)(1-v) L_(k,n)(1-v) dv.                    (3)

Every radial cross term at fixed n is retained. Distinct n have zero
angular cross integral. If q is the exact vanishing order of
L_(ell,n)(1-v) at v=0, its diagonal is integrable precisely when

    a+ell delta+2q-2 > 0.                                (4)

Checking (4) at a=0 suffices for all tested a>=0. Cross terms are then
integrable by Cauchy-Schwarz. The code also checks each grouped monomial
exponent is greater than -1 before integration. The origin is regular
because the exact polynomials in (2) came from smooth Cartesian fields.

Form each polynomial product in (3) exactly, with multiplicity two for
ell<k, then group identical real powers of v. For a remaining monomial
coefficient z and exponent e>-1, its integral is z/(e+1). Rational
coefficients and exponents are converted with outward ball arithmetic;
all sums, divisions, multiplication by pi/2 and square roots are outward.
Cancellation is allowed but a positive lower bound on each nonzero mode
energy is required. This proves enclosure of the full nonnegative mode
energy without quadrature, finite-radius truncation or angular sampling.

## Checkpoints and completeness

A completed mode record includes the common input/proof/code hashes,
its full branch and moment counts, exact Cartesian/polar identity checks,
and the outward energy at every requested a. The final sum is accepted
only after one matching record exists for every mode in the full residual
cache, with no repeated or missing mode. Summing these energy enclosures
and taking their square root gives both a lower and an upper bound for
N(a). At an intermediate checkpoint, the sum over completed modes is a
lower bound only; no full upper bound is claimed from a partial sum.
Selected-mode values for n=1,3 at quarter points are compared against
the independently confirmed N4-113 record.

## Continuous parameter cells

N(a) is nonincreasing, since its squared integrand decreases pointwise
in a. The factor 5^((a-2)/2) increases. B(a) strictly decreases on [0,A),
because its positive numerator decreases and its denominator increases.
For l<=a<=h<A, outward bounds therefore give

    5^((l-2)/2) N(h) <= 5^((a-2)/2) N(a)
                         <= 5^((h-2)/2) N(l),
    B(h) <= B(a) <= B(l).

A positive lower enclosure of 5^((l-2)/2)N(h)-B(l) proves failure of
(1) throughout the cell. A negative upper enclosure of
5^((h-2)/2)N(l)-B(h) proves that this necessary scalar test passes
throughout the cell, but does not prove any bound on the remaining parts
of Y(F), an inverse estimate or a nonlinear solution. All other cells
are explicitly unresolved by this coarse comparison. The endpoint A
can bound a failure cell by continuity but never belongs to the positive
rate parameter range itself.

## Dependencies and independent review

Dependencies are the exact Cartesian residual and derivative engines,
finite Fourier orthogonality, the elementary power integral, outward
Arb arithmetic, and the already reviewed framework-specific facts in (1).
Their hashes are registered by the computation. A new full candidate
norm remains N4-origin and OPEN pending independent peer reproduction,
even when its selected-mode anchors match earlier confirmed results.
