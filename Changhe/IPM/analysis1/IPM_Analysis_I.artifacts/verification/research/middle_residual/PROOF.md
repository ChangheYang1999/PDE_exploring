# Independent middle-region residual certificate

Date:2026-10-20. Status: method and canonical input archive verified; complete computation active and final output audit pending. This topic extends the selected-cell method to every exact middle cell of the normalized finite modal trial. It does not cover the inner region or the exterior tail and does not prove a global inverse.

## Exact statement to be certified

The density, canonical inverse, exact dependent normalization and binary64 input meanings are those of ../modal_repair/PROOF.md and ../modal_green/PROOF.md. Let the distinct exact log knots be t_0<...<t_S. Every parent interval is subdivided into the positive integer count specified by the pinned subdivision artifact. The resulting exact rational closed cells cover [t_0,t_S], including their endpoints. For each cell C let B_C be the output bound. A completed accepted computation proves

sup_{t in C} sum_{n=0}^{521}|epsilon_n(t)|/m(exp(t)) <= B_C,

where epsilon is the true canonical profile residual, c_l=1/k, and m(r)=(r/L)^3(1+(r/L)^2)^((k-3)/2). In particular the maximum of the finite list B_C bounds the entire middle region. To add a far weight (1+r/L)^a, use its right endpoint when a>=0 and its left endpoint when a<0, evaluated outward. No normalized residual denominator N_f or N_v is substituted for this weight.

The certification must record every exact cell once, its code and input hashes, its bound and remainders. Partial output is not a certificate of the full middle region.

## Canonical moments at original knots

Write rho=exp(3t) sum R_j(t)sin((2j+1)theta). On each original open span, R_j is the exact polynomial reconstructed from the original rational spline coefficients by the Cox recurrence. Its polynomial variable is x=t-(a+b)/2. At shared knots, the two polynomial values agree because the spline is continuous; higher smoothness is not needed for integration. The exactly normalized inner and outer extensions determine the canonical endpoint moments. Those definitions and convergence denominators are proved in ../modal_green/PROOF.md.

Store the outward i_n(a) at the left endpoint of each original span and j_n(b) at its right endpoint. Forward and backward recurrences propagate these endpoints over every original span, once in each direction. These are integrations of the density moments, not imports from the numerics lane's velocity arrays.

For a nonzero real z define phi_l(z)=integral_0^1 exp(zv)v^l dv. Integration by parts gives

phi_0(z)=(exp(z)-1)/z,
phi_l(z)=(exp(z)-l phi_{l-1}(z))/z, l>=1.

At z=0, phi_l(0)=1/(l+1). These identities are exact for either sign of z. The implementation encloses the recurrences with outward Arb arithmetic, checking that the denominator ball excludes zero whenever the rational z is nonzero. Cancellation can widen a ball; it cannot make a correctly rounded ball cease to enclose the integral. The implementation checks positivity and a prescribed relative-accuracy threshold before accepting values. A failed check aborts instead of silently replacing the ball by its midpoint. For validation, compare this recurrence at representative exact arguments with the independently proved Taylor-series enclosure of ../exponential_moments/PROOF.md.

For a polynomial P(v)=sum c_l v^l on [0,h], the integral of exp(lambda v)P(v) is exactly h sum c_l h^l phi_l(lambda h). Translation, reversal, and multiplication of the degree-seven polynomial use finite binomial identities with outward coefficients. All radii, including those of the scalar normalization correction, remain in the resulting sums. The m=2 backward propagation is growing and is enclosed without assuming contraction.

## Midpoint recovery and whole-cell enclosure

For each child cell midpoint t_c in an original span [a,b], recover the canonical moments directly from that span's endpoints:

i_n(t_c)=exp(-(2n+4)(t_c-a))i_n(a)
 + integral_0^{t_c-a} exp(-(2n+4)v) R_{n-1}(t_c-v) dv,

j_n(t_c)=exp((4-2n)(b-t_c))j_n(b)
 + integral_0^{b-t_c} exp((4-2n)v)R_n(t_c+v)dv.

These follow by splitting the original defining integrals. The density Taylor coefficients about t_c follow by polynomial translation. Thus every midpoint input to the cell enclosure has its own direct canonical integral definition; midpoint values are not interpolated from a sampled solution. The thirteen existing point certificates provide independent comparisons with the earlier Taylor-series integration, but agreement is a cross-check rather than the proof of enclosure.

The entire child cell lies in its original span by exact rational endpoint checks. Apply the degree-Q scaled Taylor-model, ODE, Laurent-product and exact Bernstein argument of ../residual_cells/PROOF.md. That proof bounds each complete closed cell. Its source arithmetic has been checked separately; a refactored driver must retain every term and pass the same fixtures. Every scalar quantity sent into the driver is an outward ball with exact dyadic serialization. No floating midpoint is treated as a proved bound.

## Completion and scope

An accepted output audit must verify the exact parent partition, every child index and endpoint, positivity of the weight, source/import hashes, absence of unfinished cells, nonnegative tail bounds and the maximum reduction. Resume files may contain only an initial segment; their existence does not certify omitted cells. The final reduction must use exact rational upper bounds, independently from any displayed decimal strings.

This statement concerns an explicitly reconstructed modal trial. A rigorous distance from that modal trial to X3 has not been established merely by sampled fitting errors. Even a successful full middle-region residual enclosure supplies neither the missing center/exterior bounds nor an a posteriori existence theorem.

## Source-review clarifications

The pinned parent-count artifact is ipmA-num/data/cert_green.npz, SHA256c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1. It supplies only a partition definition. The exact density definition and L,k come from modal_v2.json, SHA25657f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6. The driver separately pins all its own source imports. A source audit verifies that modal_setup.setup is byte-for-byte the initialization body of the already confirmed independent point integration; see evidence/setup_provenance.json. It also pins the imported exponential-moment module and library versions omitted from the builder header.

For clarity, the leading cosine-mode-zero outer correction is z[exp(alpha_0 tau)-exp(-bo tau)sum_(l=0)^6 ((alpha_0+bo)tau)^l/l!]. It vanishes with its first six derivatives at tau=0, so changes neither the inner formula nor any join jet through order6. Projection multiplies it by C=P_(j,0), explaining A[0]+=Cz and eo[l]-=C(alpha_0+bo)^l z/l!. The exact projection uses cos^2(theta)sin(theta)=(sin(theta)+sin(3theta))/4 and the sine-cosine product identity, hence the signed1/8weights. The scalar z is the exact canonical-normalization solution already independently enclosed. These facts are proved in the modal repair and modal Green dependency topics.

The scaled density moments already divide I,J by exp(3t); differentiating their definitions gives i_prime=-(2n+4)i+R_(n-1) and j_prime=(2n-4)j-R_n. This explains the two kernel rates without a missing density power. The weight satisfies d_t log m=(3+k u^2)/(1+u^2)>0, so its left endpoint is the required minimum.

The published residual file is used to report comparison labels and to select cross-check points; requiring its presence is a reproducibility choice, not a mathematical input to the bound. Every bound is computed independently of its numerical values. Full completion and an exact-output audit are still mandatory.

## Driver review closure

The output includes both explicitly defined multipliers (1+u)^(1/2) and (1+u)^(1/2-k). These are two distinct finite middle-region norms; neither is silently substituted for a convention in SPEC. The exponent c_l=1/k is the exact prescribed trial exponent, and the dependent outer coefficient is defined by the exact canonical equation sigma=3/k-1. Thus both the held k and the scalar normalization describe the same normalized modal trial.

The field max_Green_remainder is a diagnostic maximum of the remainders in the dimensional A_n and B_n ODE Taylor models. These remainders already enter the velocity Taylor-model multiplication by exp(-2t), then enter the angular product_tail bounds through P[2] and Qf[2]. They are thereby included in nonpolynomial_remainder. Adding the raw maximum to W would mix quantities with different factors and count errors twice. The displayed decomposition W >= retained_Bernstein_sum + discarded_polynomial_remainder + nonpolynomial_remainder is the complete residual bound.

In cell_core.bound_cell, row['residual_coefficients'] appears only in an assertion comparing the newly computed constant coefficients with separately integrated point coefficients. The pub values appear only in index assertions, published value fields and comparison labels after W and W/m have been computed. Neither input can modify any coefficient or bound. The source is pinned; the output audit must retain this distinction.

Checkpoint fault injection covers absent/empty files, incomplete headers and rows, valid JSON without a newline, malformed completed lines, wrong geometry, wrong degree, negative bounds and wrong weights. The driver rechecks the weight lower bound with outward Arb on both new and resumed rows, pins the completed archive audit and its source, and gates the recorded moment accuracy above200bits. Seven-cell smoke output is only a partial run.

## Explicit middle-annulus L2 consequence

The domain here is R^2, with polar measure dX=r dr dtheta and the full angular interval0<=theta<=2pi. The 522 real coefficients epsilon_n multiply the distinct sine frequencies2n+1, n=0,...,521, so the highest frequency is1043. This coefficient convention is established by the Laurent-to-sine identity in the selected-cell proof and its independent Laurent audit. Orthogonality gives

integral_0^(2pi)|epsilon(r,theta)|^2dtheta=pi sum_n|epsilon_n(r)|^2<=pi W(r)^2.

For each cell with the uniform bound W(r)/m(r)<=B_C, its contribution to the squared norm

N_2^2=integral_(middle annulus)|epsilon(X)/m(|X|)|^2 dX/[1+(|X|/L)^2]

is at most pi B_C^2 L^2/2 log{[1+(r_right/L)^2]/[1+(r_left/L)^2]}. The exact finite sum of these quantities, evaluated with outward intervals, bounds N_2^2. This is one explicitly defined middle-annulus norm, with no assertion that it is the unchosen full forcing norm of SPEC. Every interval conversion must reject infinity and NaN before reading the internal finite dyadic tuple.

The parent-count NPZ is already hashed by build_knot_moments.py and again by the pinned archive auditor. The final output audit pins that passed archive audit and the extracted exact partition, including its recorded NPZ hash; it independently checks full coverage against the original exact knots. A new read of the large NPZ is not needed for the final mathematical coverage check. Its velocity arrays are never inputs to the bounds. Library versions for the output audit are pinned to python-flint0.9.0, mpmath1.3.0, and numpy2.5.0, matching the recorded input-preparation environment. These libraries remain trusted arithmetic implementations, not formally verified code.


## Final audit provenance and the two rate ranges

The cell field max_abs_lambda_h_exact means the largest absolute homogeneous rate times the half-width in the dimensional Green ODE models A_n and B_n. Their identities are partial_t A_n=-2n A_n+exp(4t)F_n and partial_t B_n=2n B_n-exp(4t)F_n. Thus n=1,...,261 gives exactly522h. The directly expanded forcing exp(4t), density exp(3t), and velocity factor exp(-2t) have smaller rates. This diagnostic is not a bound on the scaled density-moment integration rates: recovering i_n and j_n uses rates -(2n+4) and 4-2n, whose largest absolute value is526. The separate pinned archive/midpoint integration code and its setup checks cover that range, including the phi checks at526 times the largest original span. No526 bound is replaced by522 in either calculation. The cell source and the full running job remain unchanged.

The completed output audit additionally requires that the archive auditor's partition_sha256 equals the full run header's partition_sha256. Both must hash the exact partition read by the final audit. It also requires the passing non-finite fixture to pin the current output auditor and current fixture source. These checks close source-to-evidence links rather than changing a mathematical bound. Both the driver and the final auditor resolve equal maxima by the first cell, using strict greater-than updates. Partial smoke output is labelled PASS_PARTIAL_TEST and cannot close the full7809-cell claim.
