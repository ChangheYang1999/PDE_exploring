# The weighted factor supremum does not control interior velocity

Date: 2026-10-20. Status: CONFIRMED after independent derivation and actual Claude Opus 5.5 review. This restricts the choice of a low norm in a possible iteration. It neither excludes a profile nor refutes stronger norms.

## Statement and notation

Fix L>0, 0<k<1, and W(r)=(1+r^2/L^2)^((k-3)/2). For a smooth correction h, even in x and odd in y and vanishing near the axes, define

||h||_F=sup_{x y !=0} |h(x,y)|/[x^2 |y| W(|(x,y)|)].

The factor extends by zero near the axes. Use the canonical full-plane velocity

U[h](X)=-h(X)e_2/2+PV integral K(X-Y)h(Y)dY,
K(Z)=(-sin(2phi),cos(2phi))/(2 pi r^2), Z=(r cos(phi),r sin(phi)),

and c[h]=psi[h]_xy(0)/3. Let Gamma[h](X)=U[h](X)+c[h]X. Every compactly supported smooth h in this statement has a well-defined canonical velocity. The inverse and strain formulas are proved in ../canonical_inverse/PROOF.md and ../trial_regularities/PROOF.md.

For every X0=(a,b) with a,b>0 and every nonzero vector g, there are corrections h_delta in C_c^infinity, of the required parity and zero near the origin, with ||h_delta||_F<=1 such that

g dot Gamma[h_delta](X0) tends to positive infinity as delta tends to zero.

In particular no constant C satisfies |Gamma[h](X0)|<=C||h||_F for these corrections. The corresponding statement for U is also false. In contrast, the paired-kernel estimate on the symmetry axis in ../axis_control/PROOF.md remains valid.

## Construction

Choose 0<R<min(a,b)/4. The four radius-R disks centered at (plus or minus a, plus or minus b) are disjoint and avoid both axes. Set

c0=min_{|Y-X0|<=R} Y_1^2 Y_2 W(|Y|)>0,
d=2 min(a,b)-R>0,
r0=|X0|-R>0.

Let chi be a smooth nondecreasing function with values in [0,1], zero on (-infinity,1] and one on [2,infinity). For 0<delta<R/4 put

chi_delta(r)=chi(r/delta)chi(R/r),
A(phi)=(-g_1 sin(2phi)+g_2 cos(2phi))/|g|.

For Y in the first disk write X0-Y=(r cos(phi),r sin(phi)) and set

h_delta(Y)=c0 chi_delta(r) A(phi).

Define the value as zero for r=0. Extend by the required even-x, odd-y reflections to the other three disks and set it to zero elsewhere. The cutoff is zero for r<=delta and r>=R, with smooth transitions; hence h_delta is globally smooth. It is compactly supported away from the axes and origin. Since |A|<=1 and the weight x^2|y|W is invariant under these reflections, ||h_delta||_F<=1. Its center factor is identically zero near zero, so it is a correction preserving a background center normalization.

## Velocity lower bound

At X0 the correction is zero in a whole neighborhood, so the local term vanishes and the singular integral is an ordinary convergent integral for each delta. On its own disk,

g dot K(X0-Y) h_delta(Y)
 =c0 |g| chi_delta(r) A(phi)^2/(2 pi r^2).

The polar angular integral of A^2 is pi: the squared sine and cosine each integrate to pi and the cross term integrates to zero. Thus this disk contributes

(c0 |g|/2) integral_0^R chi_delta(r) dr/r
 >=(c0 |g|/2) log(R/(4delta)),

because chi_delta=1 on [2delta,R/2]. On each reflected disk, |X0-Y|>=d and |K(X0-Y)|<=1/(2 pi d^2). The total absolute contribution of those three disks is at most

3 c0 |g| R^2/(2d^2).

Consequently

g dot U[h_delta](X0)
 >=(c0 |g|/2) log(R/(4delta))-3 c0 |g| R^2/(2d^2),

which tends to infinity.

## The normalization functional cannot remove this divergence

For corrections supported away from zero, differentiation of the smooth kernel near the origin gives

sigma[h]=psi[h]_xy(0)
 =integral h(Y) Y_2(3Y_1^2-Y_2^2)/(pi |Y|^6)dY.

Indeed sigma=-partial_x U_1(0); differentiating K_1=-z_1z_2/(pi|Z|^4) and evaluating at -Y yields this sign. Since |Y_2(3Y_1^2-Y_2^2)|/|Y|^3=|sin(3theta)|<=1, the kernel magnitude is at most 1/(pi|Y|^3). All four supports lie in |Y|>=r0 and have total area at most 4pi R^2. Hence

|sigma[h_delta]|<=4c0 R^2/r0^3,
|g dot c[h_delta]X0|<=4c0 R^2 |g| |X0|/(3r0^3).

This uniform bound cannot cancel the preceding logarithmic divergence. It proves the statement for Gamma.

## Consequence for a two-norm scheme

Choose one fixed smooth compactly supported correction u, with the same parity and zero near the origin, such that grad u(X0)=g. It exists: on the first disk use g dot (Y-X0) times a smooth cutoff equal to one near X0, reflect by parity, and set it to zero outside the four disks. For any high space X containing these smooth compactly supported corrections, ||u||_X is fixed and finite.

If the forcing norm Y_L controls the value of a function at X0, then no bilinear estimate

||Gamma[e] dot grad u||_{Y_L}<=C_B ||e||_F ||u||_X

can hold for all such e and u. Substitute e=h_delta. The left side grows without bound, while the right side is fixed. Thus a two-norm argument whose forcing norm includes a pointwise residual bound must use more information than the weighted factor supremum alone for its low correction norm. A Holder norm, a suitable logarithmic modulus, or direct velocity control may supply that information; no bound for those stronger choices is proved or refuted here. The conditional theorem in ../two_norm_scheme/PROOF.md explicitly requires the full low-velocity bilinear estimate and is not contradicted.

## Verification scope

The counterexample uses an exact angular integral and explicit bounds for all reflected patches and for the canonical scalar functional. There is no fitted coefficient input, limiting exchange in the PDE, or numerical enclosure assumption. Each h_delta has the required kinematic correction properties individually. Its high derivatives are allowed to grow as delta tends to zero; the assertion being refuted imposes only the low factor norm on e. No unproved uniform high-norm claim is made.

Actual Claude Opus 5.5 rederived the support, parity, angular integral, reflected-patch bound and scalar-kernel sign and accepted the counterexample. The forcing-space consequence applies to a supremum norm or essential-supremum norm with nonzero local weight, because these coincide on continuous functions. It does not by itself refute any finite-L^p forcing norm or a logarithmic estimate using an additional high norm of e. The latter norm diverges for the constructed sequence.
