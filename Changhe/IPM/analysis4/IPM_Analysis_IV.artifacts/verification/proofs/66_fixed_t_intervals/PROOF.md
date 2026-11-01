# Fixed real-log evaluations of the canonical rational coefficients

Status: CONFIRMED for the130 retained finite interval evaluations. The canonical delta2/3 logarithmic series is not known to converge from these finite evaluations.

## Exact claim and notation

For f_1=sin(theta), delta2/3 and zero resonant stream constants, let A_n(t,theta) denote either F_n or G_n. Write its physical sine amplitudes as polynomials a_m(t)=sum_q a_(m,q)t^q. At each retained integer t and order n, calculate enclosures of

    N_n(t)=sum_m |a_m(t)|,
    M_n(t)=sum_(m,q) |a_(m,q)| |t|^q.

The first is the angular Wiener norm after summing in the logarithmic variable. The second bounds it without cancellation and also bounds the Wiener norm uniformly for every complex t with |t| no greater than the tested magnitude. Where N_n(t)>0, log10(M_n(t)/N_n(t)) measures cancellation in decimal orders of magnitude. These statements concern coefficients at fixed n, not the infinite sum in n.

## Interval method

Read the independently retained exact dyadic coefficient balls in topic64. Reconstruct each midpoint and radius exactly at640-bit working precision. For each angular mode use Horner evaluation with the exact integer t. Outward-rounded additions and multiplications enclose its true polynomial value, so summing absolute-value intervals encloses N_n(t). Horner evaluation of the sums of the absolute coefficient balls at |t| encloses M_n(t). Their quotient and logarithm are valid only when the denominator interval is strictly positive.

The root N_n(t)^(1/n), the coefficient in the physical weighted density term exp(-(n-1)delta*t)N_n(t), and the cancellation measure can then be bounded by outward-rounded elementary operations. A finite root table cannot decide its limiting root or establish a convergence radius.

The theory part's separate long-double calculation uses initial amplitude5 and divides norms by5^n. Homogeneity in the fixed canonical gauge, proved in topic50, makes this the same coefficient problem. Its table is compared numerically with the interval norms; agreement is recorded with a stated finite tolerance rather than treating decimal floating output as an exact interval certificate.

Dependencies: exact logarithmic recurrence in topic10, amplitude homogeneity in topic50, and retained coefficient enclosure audits in topics64 and65. The source and exact comparison conditions are saved beside this proof.


## Completed comparison

The130 evaluations cover n=180,190,200,209,210, both density and stream, and t=-40,-20,-10,-5,-2,-1,0,1,2,5,10,20,40. Every evaluated norm has relative interval radius below2.233e-58. The largest difference from the theory part's long-double log10 norms is1.968e-10, at stream order209 and t=40. This agreement is a finite numerical comparison; the intervals themselves are retained in verification/checks.json.

At n=210 and t=40, density has log10 norm -143.83163916305161439650640042372 and cancellation8.1419571596334231072294451703640 decimal orders. Stream has log10 norm -145.90515324161956584379690580147 and cancellation7.5336983029322925894059536914748 decimal orders. At t=0 the corresponding roots are approximately0.1923366250375371 and0.1870556719819061. Full outward-rounded strings are in the artifact, which should be used for any certified decimal quotation. Actual audit time1.525245782919228 seconds.

## Update 2026-10-31T05:38:07Z: orders220 through260

The same interval method now certifies50 more evaluations: n=220,240,250,255,260, both fields, and t=-40,-20,0,20,40. All norms are positive with relative interval radius below1.035e-35. At n260,t40, log10 density norm is -177.54590009892964403419867348028 +/-1.10e-31 and log10 stream norm is -179.73389119836703490188580390011 +/-1.10e-30. Their cancellation measures are10.284189972743542776313423684137 +/-3.87e-31 and9.5621554069504149584586188374937 +/-3.63e-32 decades.

The largest difference from the theory part's long-double log10 table is1.1766200287866013e-5 at stream n260,t40. Thus the much smaller discrepancy in the first table through210 does not apply to the extension. The interval values themselves remain certified. The actual calculation took1.5831639217212796 seconds; source snapshots and exact comparison conditions are in verification/update_20261031T053639Z/.
