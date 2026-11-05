# Independent local-coefficient producer review

Reviewed `../certify_local_energy_coefficients.py`. Mathematical method and
constant assembly pass this review. Its live all-panel computation and
endpoint completion remain separate from this method audit.

The producer evaluates actual corrected density derivatives through order3
and velocity derivatives through order2 using the frozen exact-source Arb
evaluator. Its ordered tensor seminorm uses binomial(d,i) for partial
derivatives of total order d; these are exactly the multiplicities in the
Frobenius derivative tensor. Angular absolute sums give uniform upper
bounds at all angles without an angular grid for these envelopes. The
separate strain bound uses the genuine traceless2-by-2 operator norm,
quarter-plane reflection symmetry, and containing trigonometric intervals.

Each radial harmonic is enclosed by its actual Taylor polynomial plus the
source Cauchy remainder. The adaptive degree/refinement changes efficiency
and tightness, not validity. It never replaces a failed strain panel by a
claim of success. Assembly checks full metadata/hash equality, unique base
indices and complete prefix-free adaptive binary leaves. The stored512-bit
series-degree assertion is enforced by the frozen field routine itself.

The pointwise quantities are exactly
B0=|grad rho|, H1=W2|D²rho|F, H2=W2²|D³rho|F, and
Hu=r|D²u|F, where W2=sqrt(1+4r²). All displayed records are containing
Arb values. A positive norm/sum is squared only after its sign is fixed;
the signed-ball exponentiation pitfall does not affect this path.

The origin endpoint bounds are uniform because all origin expansion powers
are nonnegative and the weights/radius factors increase. At infinity,
W2(r)/r decreases; the asserted strictly negative shifted powers make
H1,H2,Hu uniformly bounded by their endpoint values. The expansion degree16
gives N17, sufficient for every physical derivative order used. The strain
origin/far bound is the safe entrywise traceless operator upper
|S11|+|S12|. Hence its3/2 target, if all panels and endpoints pass, suffices
to prove cX+u has nonnegative radial component and dmin=c+1.

Let omega4, a2, s3/2 and Minf=1+(2-q)c>0. The K1 formula in assembly
is a valid conservative Frobenius triangle bound for the exact E1 in
`LOCAL_Q_BACKGROUND_IDENTITY_v01.md`; it discards the favorable -2betaomega.
Its terms bound, respectively: the constant/strain part of half the trace
Hessian, the X·D²u part, rho_y times the identity, the cross gradient of
rho_y, the product X tensor Delta u in Dv, and the two third-density
derivative contributions. The coefficient(1+q)/2 on H2 is valid because
Delta u=(rho_xy,-rho_xx), and |Sym D Delta u|F<=|D³rho|F.

The scalar K0 formula follows from the exact identity
\[
E0=\omega[(8-2q)c+4-4\beta+\rho_y
+(2-q/2)(x\rho_{xy}-y\rho_{xx})].
\]
Using r|Db|<=H1/2 and discarding -4betaomega gives exactly its stored
upper. This checks its density/velocity sign convention independently.

Two optional consumer improvements need no producer modification. First,
the traceless matrix
\(\tfrac12(X\cdot\Delta u)I-\operatorname{Sym}(X\otimes\Delta u)\)
has operator norm r|Delta u|/2 exactly. Its qH1 contribution can therefore
be reduced from qomega(1+1/sqrt2)H1/a to qomega H1/(2a).
Second, for any auxiliary a<=2, W_a<=W2 and the recorded envelopes remain
valid; use the smaller omega=a² in the algebra and retain the safe
r|Db|<=H1/2 rather than weakening it to H1/a.

The fractional local transport term needs Wu2=sup W_a|D²u|F. A leaf's Hu
record bounds r|D²u| throughout that leaf, so multiplication by
W_a(left)/left is a safe upper. At the origin use directly the monotone
origin derivative bound times W_a(rmin), equivalently its endpointHu times
W_a(rmin)/rmin. At infinity both Hu and W_a/r have valid decreasing bounds.
This reconstructs Wu2 from the existing producer records without a new
field evaluation.

`certify_actual_matrix.py` is imported for its interval trigonometric
arithmetic and is included in every binding hash. It must stay frozen until
this run is assembled; an auxiliary-weight matrix producer should use a
new filename rather than changing that dependency mid-run.
