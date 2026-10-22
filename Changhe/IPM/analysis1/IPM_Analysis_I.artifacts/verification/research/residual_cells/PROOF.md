# Selected whole-cell residual bounds by polynomial products and exact Bernstein conversion

Date:2026-10-20. Status: CONFIRMED for all thirteen specified full log-radius cells. This certifies only the selected full log-radius cells when its output audits pass. It does not cover untested cells, the center region or the exterior tail.

## Inputs and objective

Use the exactly normalized finite modal trial of ../modal_repair/PROOF.md. At each selected exact log midpoint t_c, ../residual_samples supplies outward balls for every canonical density moment i_n,j_n, n=1,...,261, and every coefficient of the degree-seven density polynomials R_j(t_c+x), j=0,...,260; the slot R_261 is exactly zero. The entire selected closed cell [t_c-h,t_c+h] lies in one original spline span, verified using exact rational endpoints. These point moments and polynomials are inputs to the present enclosure, not samples from which a bound is interpolated.

Set c_l=1/k, as guaranteed by the exact modal normalization. Write m_n=2n, nu_j=2j+1 and r=exp(t). Then rho=r^3 sum R_j(t)sin(nu_j theta). At t_c the exact canonical stream moments are

A_n=exp(4t_c)[(R_{n-1}+R_n)/2-m_n i_n],
B_n=exp(4t_c)[m_n j_n-(R_{n-1}+R_n)/2].

On the whole cell they solve

A_n'=-m_n A_n+G_n,
B_n'=m_n B_n-G_n,
G_n=exp(4t)[R_{n-1}'+R_n'+(4-m_n)R_{n-1}+(4+m_n)R_n]/2.

This identity follows by differentiating the density-moment formulas with i_n'=-(m_n+4)i_n+R_{n-1} and j_n'=(m_n-4)j_n-R_n. The moments initialized at t_c are canonical; solving their exact ODEs on this cell retains that gauge.

The goal is an upper bound for

sup_{t in cell} sum_{N=0}^{521}|E_N(t)|,

where epsilon(t,theta)=sum E_N(t)sin((2N+1)theta) is the exact residual. The angular mode set is finite and complete. If the new upper bound is no greater than a published whole-cell upper bound of the same functional, that particular published inequality is independently confirmed, despite any defects in its original calculation. A larger new upper bound proves no refutation.

## Exponential-polynomial Taylor models

A scalar Taylor model on |x|<=h is (p,r), meaning f(x)=p(x)+e(x), with p=sum_{q=0}^Q p_q x^q and |e(x)|<=r. All coefficient balls enclose the coefficients of the exact polynomial; r is an outward nonnegative upper bound. For P(x)=sum_{l=0}^d c_l x^l and Q>=d, the Taylor coefficients of exp(lambda x)P(x) are

p_q=sum_{l<=min(d,q)} c_l lambda^{q-l}/(q-l)!.

The remainder is at most

exp(|lambda|h) sum_{l=0}^d |c_l| h^l (|lambda|h)^{Q-l+1}/(Q-l+1)!.

Taylor's integral remainder for exp(lambda x), or its absolutely convergent series, proves this termwise bound for both signs of x and lambda. It is multiplied by |exp(lambda t_c)| when the original factor is exp(lambda t).

For the ODE y'=lambda y+sigma G, sigma in{+1,-1}, let G have degree-Q Taylor coefficients g_q and remainder r_G, and define

p_0=y(0), p_{q+1}=(lambda p_q+sigma g_q)/(q+1), q=0,...,Q-1.

Subtract the polynomial equation from the exact ODE. The error e=y-p satisfies e(0)=0 and

e'=lambda e +(lambda p_Q+sigma g_Q)x^Q+sigma(G-G_Q).

Variation of constants, in either integration direction, gives the uniform bound

r_y=exp(|lambda|h)[|lambda p_Q+sigma g_Q| h^{Q+1}/(Q+1)+h r_G].

No derivative beyond the original polynomial coefficients is assumed. Dependence among coefficient balls can only widen the resulting upper bound.

For products (p,r_p)(q,r_q), retain the degree-Q truncation of pq. If P=sum|p_l|h^l and Qb=sum|q_l|h^l, its remainder is bounded by

sum_{l=Q+1}^{2Q}|[x^l]pq|h^l + P r_q+Qb r_p+r_p r_q.

This follows by expansion of (p+e_p)(q+e_q), followed by the triangle inequality. Multiplication by a real scalar ball uses its absolute upper bound in every remainder.

## Residual as two angular products

Construct scalar models for every coefficient of the density rho=exp(3t)sum_j R_j sin(nu_j theta), as well as the four fields

D(t,theta)=rho_t=exp(3t)sum_j(3R_j+R_j')sin(nu_j theta),
H(t,theta)=rho_theta=exp(3t)sum_j nu_j R_j cos(nu_j theta),
P(t,theta)=-exp(-2t)sum_n(A_n+B_n)cos(m_n theta)/2,
Q(t,theta)=exp(-2t)sum_n(B_n-A_n)sin(m_n theta)/2.

Since U_r=-psi_theta/r and U_theta=psi_t/r, and psi_n=(A_n+B_n)/(2m_n), psi_n'=(B_n-A_n)/2, the full residual is exactly

epsilon=c_l D-rho+P D+Q H.

The density model uses the exponential-polynomial formula with lambda=3 and P=R_j. Its remainder is included in the linear term as |c_l| r_D+r_rho. The exp(-2t) factor is a separate degree-Q model with d=0, including its remainder; the scalar product rule combines it with A+B and B-A. Every coefficient and every multiplication, including the encoded polynomial product, uses outward Arb balls. Q>=7 is mandatory.

Here primes on A,B,psi and R denote log-radius derivatives. In the formula U_theta=psi_t/r the t derivative is explicit, avoiding a radial-versus-log derivative ambiguity.

Use imaginary Laurent coefficients for real sine sums and real Laurent coefficients for real cosine sums as in ../residual_samples/PROOF.md. Their Laurent l1 norm equals the real trigonometric Wiener norm. For every angular coefficient keep its degree-Q radial polynomial and a scalar remainder. Let r_F be the sum of its Laurent-coefficient remainder bounds, and P_F=sum over Laurent modes and radial degrees of |c_{nu,q}|h^q. Then a product has nonpolynomial angular l1 remainder at most

P_F r_G+P_G r_F+r_F r_G.

This is the convolution inequality ||ab||_{l1}<=||a||_{l1}||b||_{l1}, proved by summing |sum_k a_k b_{n-k}| over n and interchanging two finite nonnegative sums. The same bound holds uniformly for each x. Sum the bounds for the two advective products and the linear term. Add the absolute h-weighted sum of every discarded radial coefficient of the finite polynomial products.

## Exact encoding of the two-variable polynomial product

Encode a Laurent mode nu shifted by an integer C and radial degree q as a univariate exponent (nu+C)(2Q+1)+q. Each factor has 0<=q<=Q, so a product has 0<=q<=2Q. There is no carry into the angular index because the base is2Q+1. Thus ordinary outward polynomial multiplication computes the exact two-variable convolution, including every angular mode and every radial product degree. The density shift is521 and velocity shift522, so their product is centered at1043. The largest physical frequency is1043. Recovering the sine coefficients uses the difference between the imaginary Laurent coefficients at-nu and+nu. The total discarded radial Laurent l1 bound also bounds the discarded real sine Wiener sum, by that same difference and the triangle inequality.

## Bernstein bound on the real cell

For a degree-Q real polynomial p(x)=sum_l c_l x^l, substitute x=h(2u-1), 0<=u<=1. Its monomial coefficients are

d_i=2^i sum_{l=i}^Q binom(l,i)(-1)^{l-i} c_l h^l.

Its Bernstein coefficients of degree Q are

b_k=sum_{i=0}^k [binom(k,i)/binom(Q,i)] d_i.

Indeed u^i=sum_{k=i}^Q [binom(k,i)/binom(Q,i)] binom(Q,k)u^k(1-u)^{Q-k}; cancellation of binomial factors reduces the right side to u^i times the binomial expansion of(u+1-u)^{Q-i}. Since the degree-Q Bernstein basis is nonnegative and sums to1, |p(x)|<=max_k|b_k|. Every matrix entry is computed as an exact rational and converted outward; no binary64 Bernstein coefficient is treated as exact and no radius is discarded.

Apply this bound separately to every retained real residual sine coefficient, sum their maxima and add the total angular Wiener remainder. This gives the claimed whole-cell W bound. For m(r)=u^3(1+u^2)^((k-3)/2), u=r/L and k>0,

d_t log m=(3+k u^2)/(1+u^2)>0.

The exact functional compared is sup_cell W(t)/m(exp(t)), not mW. The constants k and L are the exact binary64 inputs specified by data_exact/modal_v2.json, hash57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6. Therefore W divided by the outward lower bound for m at the exact left endpoint bounds the whole-cell weighted Wiener norm. No additional far weight is included here.

The implementation may store coefficients in z=x/h, |z|<=1. This is the exact substitution p_q x^q=(p_q h^q)z^q. In this convention the ODE recurrence replaces lambda by lambda*h and G by h*G; its remainder is exp(|lambda|h)[|lambda*h*p_Q+sigma*h*g_Q|/(Q+1)+h*r_G]. All polynomial norms and discarded tails are then sums of absolute coefficients, and the Bernstein conversion uses h=1. This is a change of variables, with no approximation.

## Required verification and limits

Pin input moments, density coefficients, source code and comparison snapshots. Verify Q>=7, h>0 and exact inclusion in one original spline span. Independently check ODE and Laurent sign identities and Bernstein conversion. The execution records every selected cell, degree, bound, total remainder and exact comparison value. Its acceptance requires a source and output audit. It is a finite-cell certificate, not a global residual theorem and not an inverse or closing inequality.

Review: actual Claude Opus5.5 accepted the identities at2026-10-20T16:01:16Z subject to explicit density-model and weight definitions. Both are now supplied above, together with outward arithmetic and exp(-2t) model requirements. Code and output audits remain necessary.

## Completed output audits

The first run completed2026-10-20T16:06:46Z in25.87seconds. The source review by actual Claude Opus5.5 accepted every remainder, sign and conversion, subject to export/provenance checks. An unchanged-source replay completed16:10:48Z, asserting zero radius on all390values passed to the exact dyadic scalar exporter. It reproduced every coefficient and bound exactly. The angular fixture used rho=exp(3t)sin(theta), psi=exp(4t)sin(2theta), whose advective residual is exp(5t)[5sin(theta)-sin(3theta)]. All34retained coefficients matched this exact formula; the full bound enclosed its checks.

The independent mpmath.iv75 output audit finished16:13:20Z in34.40seconds. It reconstructed the Bernstein coefficients by Horner translation and finite differences, then recomputed all thirteen upper comparisons using exact decimal inputs. Every selected W and W/m inequality was confirmed. The two completed run logs, full Cartesian cell selection, unchanged source and fixture hashes, exact endpoints, weight constants and output hashes were checked. See evidence/iv_output_audit.json and evidence/zero_radius_replay.json. The midpoint-overlap test is only a consistency check; the proof rests on the exact identities and outward remainders. The resulting thirteen-cell certificate leaves every other cell untested.
