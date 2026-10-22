# The normalized scaling field and the frozen Fminus exterior span

Written 2026-10-21T23:04:21.307017+00:00, before this topic's checker. Status: analytic argument awaiting its finite input checks and actual second-model review.

## Exact statement and dependencies

Let t=log r, t0 be the last exact knot of data_exact/modal_v2.json, and s=t-t0. Let Phi_m(theta)=cos(theta)^2 sin(theta) cos(2m theta). Pad all vectors below to dimension261, with indices0,...,260. The canonical, exactly joined normalized trial of ../modal_repair/PROOF.md has exterior density

 rho_star=r^3 sum_m a_m(t) Phi_m(theta),
 a(t)=C exp(lambda s)+sum_q p_q(s) exp(lambda_q s),
 C=A+z_star e0, lambda=k-3, lambda_q<lambda,

where the sum is finite and its vector-valued p_q are polynomials. Here k=1615536043799051/9007199254740992, A is the first Aout column of the exact JSON (last padded entry0), and z_star is the unique exact real scalar defined by the central-strain equation in modal_repair. Its certified interval Z is the A00_correction interval in that topic's independent_gauss_iv.json, bound to accepted156. It is not replaced by an interval midpoint. All nine other exact outer rates and the rate -bo are strictly below lambda. Recomputing the exact outer jet correction changes only the degree6 polynomial at rate-bo. Adding z_star changes precisely the leading coefficient of mode0 by z_star. These facts follow directly from the exact join and normalization definitions.

Let A and B be the exact dyadic A0 and Bm vectors in the frozen saved-vector NPZ of accepted172 (SHA4fd4ff818efd62aa03cb4392d8d56dcaf8f948188962fc1133c38c561099ba2e). The full A0-to-Aout identity must be rechecked. B is the actually stored rounded vector, with B_260=0, not the ideal cosine-product vector. Let nu=fl(k-3), where fl denotes the nearest-even binary64 subtraction in the frozen c2_fminus recipe. The exact normalized trial retains lambda=k-3; nu is a distinct column exponent.

For mu<min(lambda,nu), let G_mu be the set of vector functions that, for all sufficiently large t, are finite sums p(s) exp(eta s), where p is any vector polynomial and eta<=mu. This set includes any function with bounded support in t. Define two exterior classes

 F_lambda={r^3 sum_m [g_m(t)+alpha*t*A_m exp(lambda s)+beta*B_m exp(lambda s)] Phi_m: g in G_mu, alpha,beta real},
 F_nu={r^3 sum_m [g_m(t)+alpha*t*A_m exp(nu s)+beta*B_m exp(nu s)] Phi_m: g in G_mu, alpha,beta real}.

Only the exterior restrictions are specified; no joins, norm, closure or interior conditions are imposed. Thus any actual constrained finite span with these exterior tails is a subset of the corresponding class. Choose mu as the maximum of the exact outer rates with q>0, their independently rounded source rates, and-bo. Exact finite checks must prove

 mu<lambda<nu, 0<k<1, A_0>0, B_1>0,
 D(z)=(A_0+z)B_1-A_1 B_0>0 for every z in Z.

Under these checks, the normalized scaling field K_star=rho_star-partial_t rho_star belongs to neither F_lambda nor F_nu. In particular it does not belong to the explicit frozen non-free Fminus function recipe with Mh=16 and stride16, with either mathematical-rate or literal-rate interpretation. Its constrained subspaces and finite rescalings cannot enlarge that span. This is a comparison with that frozen recipe, not a redefinition of its tail vectors using C. No claim about a free-tail class or any norm closure is included.

## Proof

Differentiation at fixed theta gives

 K_star=r^3 sum_m (-2a_m-a'_m)Phi_m,
 exp(-lambda s)(-2a-a')=(1-k)C+o(1).

To justify the limit, the derivative of exp(eta s)p(s) is exp(eta s)(eta p+p'). For delta>0 and a polynomial of degree d, s^d exp(-delta s) tends to0: exp(delta s)>=(delta s)^(d+1)/(d+1)! for s>0. The same applies to every polynomial derivative. Hence both the canonical lower terms and every g in G_mu, after multiplication by exp(-lambda s), tend componentwise to0. Also C is nonzero, since D(z_star)>0.

The finite functions Phi_m are linearly independent. Divide a vanishing sum on an open angular arc by cos(theta)^2 sin(theta), which is nonzero there. The resulting cosine polynomial is a polynomial in x=cos(2theta). Restricting to an arc where this variable ranges over an interval forces that polynomial to vanish identically. The recurrence T_(m+1)=2xT_m-T_(m-1) gives strictly increasing degrees and nonzero leading coefficients, so every coefficient vanishes. Consequently equality of the physical functions implies equality of the vector coefficients at each large t. The common positive factor r^3 can be cancelled.

If K_star belongs to F_lambda, division by exp(lambda s) yields

 (1-k)C+o(1)=alpha*t*A+beta*B+o(1).

Divide by t and pass to the limit. Since A_0>0, alpha=0. Passing to the limit again gives (1-k)C=beta*B. Taking the determinant of coordinates0,1 gives (1-k)D(z_star)=0, contradicting the checked strict inequalities.

If K_star belongs to F_nu, division by exp(nu s) yields

 o(1)=alpha*t*A+beta*B+o(1),

since lambda<nu and every lower exponent is at most mu<lambda. Division by t first forces alpha=0; the remaining limit and B_1>0 then force beta=0. The original equality is therefore K_star=r^3 sum_m g_m Phi_m. Dividing its coefficient identity by exp(lambda s) gives (1-k)C=0, another contradiction. This proves both claims.

The literal-rate proof requires the explicit gap mu<lambda. Replacing G_mu by the larger class of all g=o(exp(nu s)) would invalidate this conclusion: the coefficient vector of K_star itself is in that larger class because lambda<nu. The tiny exponent difference is kept exactly and cannot be discarded on grounds of numerical size.

## Frozen-column interpretation and finite checks

In the frozen c2_fminus.py, every inner, J and coarse-spline column vanishes for t>t0. The outer q=0 column is skipped; the remaining nine outer rates are bounded by mu. The KP exterior piece has ascending coefficients[t0,1] in s=t-t0, and hence equals t exp(nu s); TAU has coefficient[1] and equals exp(nu s). Their angular vectors are A and the stored B, respectively. The source sums only m<260; B_260=0. The ExpPolyBasis source confirms this convention. These source interpretations are explicit definitions of paired functions. They authenticate no historical matrix assembly, projection or floating operator evaluation.

The checker will rehash accepted172 and156 and their recorded dependencies, manually decode all A0,Bm,k,t0 scalars from ZIP/NPY/IEEE words, and compare NumPy exact ratios. An independent exact hexadecimal parser will read the JSON Aout and knots. It will reconstruct the ten exact and ten rounded rates in Fraction and by an independent integer rounding algorithm, compare the live elementary binary64 operations, and verify the exact positive gap nu-lambda. The stored B recipe and all Aout leading coordinates will be checked.

Since B_1>0, D(z) is increasing, so its exact range over Z is[D(z_lo),D(z_hi)]. Fraction and fmpq will independently compute both endpoints. Arb balls and mpmath.iv will separately enclose the same affine expression with interval z, and exact comparisons will place both enclosures in a stated strictly positive rational decimal window. These are directed enclosures, not agreement-based error estimates. Guard cases will reject nonfinite IEEE and interval endpoints; a manufactured rate case will demonstrate why nu's broad little-o class is excluded. No numerical limit or finite-radius sample is used to prove nonmembership.

Passing these finite checks and actual review will establish only exact algebraic nonmembership in the two stated exterior spans for the distinguished normalized trial. It gives no positive norm distance, failure of an ideal projection, coercivity, physical forcing norm, inverse, X3 error bound, nonlinear closure or decisive IPM endpoint.
