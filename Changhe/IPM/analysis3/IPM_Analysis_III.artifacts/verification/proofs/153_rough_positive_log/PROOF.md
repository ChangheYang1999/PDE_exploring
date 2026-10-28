# Positive logarithmic forms with only one Holder derivative

## Statement

Let 0<alpha<=1. Let a(X,xi) be real and nonnegative on the two-dimensional flat cylinder, smooth in xi, with uniformly local C^(1,alpha) regularity in X and symbol estimates

 ||partial_xi^beta a(.,xi)||C^(1,alpha)
                  <=C_beta <xi>^(m-|beta|), 0<=m<=alpha/8.        (1)

Then, with left quantization and a fixed smooth low-frequency convention,

 Re<Op(a)w,w> >= -C ||w||H^(-alpha/64)^2.                        (2)

The result initially holds for smooth compactly supported w. In particular, for every nonnegative coefficient ell in C_b^(1,alpha),

 Re<ell log<D>w,w> >= -C ||w||H^(-alpha/64)^2.                   (3)

The constants use finitely many of the seminorms in (1). They may depend on alpha and need not remain bounded as alpha tends to zero. This is a quantitative-order, qualitative-constant statement. It applies to a total perturbed logarithmic coefficient once its nonnegativity and C^(1,alpha) bound are proved. It does not prove the remaining transport conjugation at that regularity.

## Positive smoothing

Use the nonnegative probability mollifier J of proof 143, with radius e(xi)=<xi>^(-1/2), and write

 a_sharp(X,xi)=integral J(Y)a(X-e(xi)Y,xi)dY.

Exactly as in proof 143, a_sharp>=0 and a_sharp belongs to the smooth class S^m_(1,1/2). All derivatives in X beyond those present in a are transferred to the mollifier. Frequency derivatives of the scale contribute the factor <xi>^(-1) and retain the same estimates.

The ordinary smooth sharp Garding theorem gives

 Re<Op(a_sharp)w,w>
               >=-C||w||H^((m-1/2)/2)^2.                       (4)

For m<=alpha/8 and alpha<=1, its exponent is at most -3/16, much smaller than -alpha/64.

## The remainder in a uniformly local Sobolev symbol class

Set r=a-a_sharp. The elementary Holder mollification estimate, for a function f in C^(1,alpha), is

 ||f-J_e*f||C^(1,alpha/2)<=C e^(alpha/2)||f||C^(1,alpha).         (5)

One proof bounds the first derivative difference in supremum norm by C e^alpha, bounds its alpha-Holder seminorm by C, and uses the interpolation inequality

 [g]_(alpha/2)<=2||g||infinity^(1/2)[g]_alpha^(1/2).

The undifferentiated part has at least the same smallness. Derivatives with respect to the scale obey the corresponding estimates after multiplying by the appropriate power of e. The differentiated kernels have integral zero, so the same proof applies by subtracting the value at X. The chain rule for e(xi) therefore proves, for every beta,

 ||partial_xi^beta r(.,xi)||C^(1,alpha/2)
                  <=C_beta <xi>^(m-alpha/4-|beta|).             (6)

On a bounded patch, C^(1,alpha/2) embeds continuously in H^(1+alpha/4). For clarity, the fractional derivative seminorm of the first derivatives is bounded by integrating |X-Y|^alpha/|X-Y|^(2+alpha/2) near the diagonal; in dimension2 its radial integral is a constant times integral_0^1 r^(alpha/2-1)dr, which is finite. Multiplication by a fixed smooth patch cutoff preserves these estimates.

Thus the localized r belongs to Lannes's symbol class Gamma^l_(s0), with

 l=m-alpha/4<=-alpha/8,
 s0=1+alpha/4,       t0=1+alpha/8>1,
 v=alpha/64.

Theorem1, first estimate, of Lannes, arXiv:math/0508465, printed page20 of the retained primary source, applies since -t0<v<t0 and t0<=s0. It gives

 ||Op(r)w||H^v <= C||w||H^(v+l).

Since v+l<=-7alpha/64<=-v, this implies

 |<Op(r)w,w>|<=C||w||H^(-v)^2.                                 (7)

Combining (4) and (7) proves (2).

## Uniform cylinder globalization

Use a fixed-size, bounded-overlap partition in t and a finite angular atlas, with enlarged cutoffs. All local H^(1+alpha/4) symbol bounds from (6) are uniform. For neighboring patches apply the preceding theorem and sum square norms.

For separated input and output patches, repeated integration by parts in xi gives arbitrary distance decay of the kernel and its first X derivative. It also gives arbitrary Y derivatives, because they multiply the symbol by powers of xi before taking sufficiently many frequency derivatives. The same estimates hold for one X derivative and one Y derivative together. Schur's test bounds these separated operators from H^-1 to H^1: represent an H^-1 input as an L2 function plus the divergence of an L2 vector field and integrate by parts in Y; then differentiate the output once in X. Interpolation gives the required H^-v to H^v estimate, with summable constants over the patches. The smooth part in (4) globalizes by the same uniform smooth calculus as proof 143. This proves (2) on the whole cylinder without integrability of a in t.

For (3), the symbol a(X,xi)=ell(X)log<xi> is nonnegative and satisfies (1) with m=alpha/8. The positive power is allowed because log<xi><=C_alpha<xi>^(alpha/8), with the analogous estimates for every frequency derivative.

## Consequence for maximal-domain arguments

If a conjugated distributional equation has the form

 F=B.grad w-ell log<D>w in L2,

with bounded Lipschitz B and ell>=0 in C^(1,alpha), the Friedrichs commutators of proof 148 remain valid: they require only bounded Lipschitz coefficients. Apply (3) to the regularizations J_n w and discard the logarithmic form before passing to the limit. The resulting lower-order remainder is H^(-alpha/64). Proof 144 then compares it to the variable-order norm lowered by any epsilon<=alpha/64. Thus the maximal-domain limiting step itself does not require C3 or W7 coefficients once the conjugated equation and its other terms have been justified.

The unproved step for a nonlinear perturbation is still the tame variable-order coefficient commutator and the relevant global weighted velocity bounds. This proposition neither assumes nor concludes those statements.
