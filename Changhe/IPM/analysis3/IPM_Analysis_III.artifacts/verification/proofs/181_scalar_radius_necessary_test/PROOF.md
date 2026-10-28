# A necessary smallness test from the scalar chart radius

## Setting and statement

Use exactly the moving-tail chart, high correction Hilbert space H, high target Y_H, maximal high realization of A_0, and hypotheses (I), (S) of proof 174. Let chi be its fixed radial cutoff: 0<=chi<=1, chi=0 for r<=1, and chi=1 eventually. The exact normalized trial has parameter ell_0=1/k, where k=1615536043799051/9007199254740992. Write

 rho_ell=rho_0+chi(r)(r^(1/ell)-r^k)Theta(theta),
 n(ell)=3ell-1-c[rho_ell], S=(1/pi) integral sin(3theta)Theta(theta)dtheta.

Here S>0 is the actual angular moment certified in proof 31. The allowed parameter interval I in proof 174 satisfies 1/ell<q_*<1/4 for every ell in I. In particular I is contained in (4,infinity). Put N_4=-n(4). This scalar is well-defined even though ell=4 need not be allowed in the high residual family.

Let C_c=||c||_(H*) and eta_H=||f_0||Y_H. If a closed H ball of radius r_* is contained in the scalar chart ell(h) in I and (S) holds on a ball of radius r<=r_*, then

 K_H eta_H C_c <= N_4.                                      (1)

Consequently, for every nonzero d in the maximal high domain of A_0,

 eta_H |c[d]| <= N_4 ||A_0 d||Y_H.                          (2)

The domain condition in (2) means both d in H and A_0 d in Y_H, with the precise closed realization of proof 171. It cannot be replaced by arbitrary membership in H. For the actual trial, independently of the choice of the cutoff,

 0 < N_4 <= 3ell_0-12+S(4/3-1/(1-k)) < 9.06.               (3)

The numerical rational bound in (3) is verified below. It uses the same normalized modal object as proof 31 and no floating input substitution.

## Proof of the chart restriction

For ell>1, the canonical strain moment converges absolutely on the cutoff tail and gives

 c[rho_ell]=3ell_0-1+S integral_1^infinity chi(r)(r^(1/ell)-r^k)r^(-2)dr.

It is smooth on every compact subinterval of (1,infinity), by differentiation under the integral with an integrable power and logarithmic majorant. Differentiating gives

 n'(ell)=3+ell^(-2) S integral_1^infinity chi(r)r^(1/ell-2)log(r)dr >=3.

Thus n is strictly increasing, n(ell_0)=0, and n(4)<0 because ell_0>4. The scalar identity n(ell(h))=c[h] then implies c[h]>n(4) for every h whose scalar parameter belongs to I. Taking the infimum of c[h] on the closed H ball of radius r_* gives -r_* C_c>=n(4). This infimum identity follows from the definition of the dual norm and the symmetry of the ball; no attainment argument is required. Hence r_* C_c<=N_4. The ball condition K_H eta_H<=r<=r_* proves (1).

The same conclusion holds with any lambda satisfying 1<lambda<inf I and lambda<ell_0, replacing N_4 by -n(lambda). We use4 because it is valid for every interval allowed in proof 174.

## Proof using a test direction

The compatible high inverse bound in proof 174 applied to A_0 d gives

 ||d||H <= K_H ||A_0 d||Y_H.

Injectivity makes the denominator positive for nonzero d. Also |c[d]|<=C_c||d||H. Combining these two inequalities with (1) proves (2). This argument uses the actual high inverse estimate only as a hypothesis whose necessary consequences are being tested. It does not construct or assume a numerical value for the inverse.

At ell=4, the strain formula yields

 N_4=3ell_0-12+S integral_1^infinity chi(r)(r^(1/4)-r^k)r^(-2)dr.

Because k<1/4, the integrand is nonnegative. Replace chi by1 and integrate the two powers to obtain (3) before its final numerical inequality. Positivity already follows from n'>=3. Proof 31 bounds S between37.63077494715565 and37.63077494715567; insertion of the upper rational endpoint and the exact rational k gives the asserted cutoff-independent bound by rational arithmetic.

## Scope

A rigorously certified violation of (2), using the actual high norm on both f_0 and A_0 d, would refute (S) for this chart. The upper bound in (3) permits a weaker cutoff-independent test. Rescaling the high target norm by a positive scalar changes both sides of (2) by that scalar. There is therefore no inference based solely on an arbitrary normalization of eta_H.

No test direction is evaluated here. In particular the high residual lower bound in proof 179 alone does not violate (2). A finite-section vector or a pointwise upper estimate of A_0 d cannot supply its full high target norm. Failure of (S), if later established, would concern this sufficient iteration criterion and would not prove nonexistence of an exact IPM profile or exclude a different trial or chart.

Dependencies: proof 31 for S and the exact trial; proof 35 for the canonical strain formula, independently derived above; topics171,173,174 for the high realization, scalar chart and conditional inverse bounds.
