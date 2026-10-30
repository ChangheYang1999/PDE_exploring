# Exact source acceptance of the two N3 scaled calibration repairs

## Statement and scope

This argument precedes the checker. It concerns the frozen repaired sources
legqs_tests.py and legqs_quadcheck.py. It asserts only two finite source
properties. The corrected test A uses admissible exponents in every one
of its 810 small and three large Euler moments. The corrected quadrature
list is a disjoint partition of the entire compact radial interval [0,1]
with 58 positive-length panels. Successful source checks do not establish
that either repaired numerical calibration has run or passed.

## Admissible integral parameters

Let delta=1824676646553933/4076476460239181, so 0<delta<1. For positive
scale a and nonnegative integer i, the calibration moment is

    J(b,i,a)=integral_0^1 v^b/(1+a v)^i dv.

The denominator is positive and continuous at both endpoints. Therefore
b>-1 is sufficient for absolute integrability, because the integrand
is bounded by a constant times v^b near zero and is bounded near one.
The three corrected base exponents are -37/100, 0 and delta/2-1.
Each is strictly greater than -1. Adding any tested m in
{0,7,14,21,28,35} preserves that inequality. There are three positive
scales 624,99,2499 and fifteen powers i=0,...,14, giving 810 admissible
small test instances. The three additional instances have base -37/100,
m=600,1800,2400, scale624 and i=23, so are also admissible.

The old third base was delta-3/2<-1, since the exact campaign delta
is below1/2. At m=0 this created 45 divergent examples. Their removal
corrects the source domain error. It does not turn their old comparison
against analytic continuation into an integral certificate. The original
N4-300 finding and the separate actual production integrator retain their
previous scopes.

## Exact radial partition

The repaired list, in increasing order, is

    [0,2^-12];
    [2^(-(k+1)),2^-k], k=11,10,...,1;
    [1-2^-k,1-2^(-(k+1))], k=1,...,45;
    [1-2^-46,1].

Within each indexed list, consecutive intervals share exactly one
endpoint. The first list joins the initial cell to1/2 and the second
joins1/2 to1-2^-46; the final cell joins this to1. Every length is
positive. Thus all58 panels have disjoint interiors and cover[0,1].
Adding their lengths telescopes to1. Independently checking all
58*57/2=1653 pairs confirms disjoint interiors. Any finite point
r>=0 maps into this domain by t=r^2/(1+r^2); the final cell accounts
for arbitrarily large r. Gauss nodes remain inside each panel, so the
infinite endpoint is not itself an evaluation point.

For the old list, the total constant mass was
3/2-2^-12-2^-46, with a duplicated[2^-12,1/2] and an omitted final
interval[1-2^-46,1]. The corrected list removes the former and includes
the latter. Its exact constant mass is one. Neither exact partition
nor exact trigonometric integration bounds the radial Gaussian or
floating arithmetic error for the actual residual. Those numerical
errors remain separate from this finite geometric statement.

## Verification method and limits

Freeze old and new source bytes and their complete textual differences.
Parse only the relevant constant expressions and panel-list syntax with
an own restricted AST reader: integer constants, rational construction,
arithmetic, tuples, lists, the indicated finite ranges and panel append.
Do not import or execute any foreign source. Compare the actual extracted
source exponents and panels to the formulas above and check every exact
inequality. Bind the prior N4-300 and N4-301 evidence. Record actual
execution time, hashes, all813 exponent cases and all58 panels.

This accepts repairs to the calibration definitions. Actual repaired
calibration output, candidate norm components, quadrature error bounds,
operator inverses and existence claims are outside its conclusion.
