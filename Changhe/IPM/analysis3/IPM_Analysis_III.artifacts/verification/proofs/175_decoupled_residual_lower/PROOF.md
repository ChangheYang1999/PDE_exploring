# A positive residual lower bound in the decoupled low target

## Exact statement and target

Let rho be the exact normalized modal trial reconstructed from the original NPZ with SHA-256 a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874. Its parameter is k=1615536043799051/9007199254740992 and ell=1/k. Let F=(ell X+U[rho]).grad rho-rho use the canonical full-plane velocity. Set t=log r and p=x^2 y. The exact vertical-axis decomposition is

 F=p gamma(t)+p cos(theta)^2 Q(t,theta),

where Q is a finite cosine polynomial in 2 theta. Every residual sine mode through index522 is retained when making this decomposition.

For 18/5<=a<=4 define

 N_a(t)^2=gamma(t)^2+integral_0^(2pi)|cos(theta)|^(8-2a) sin(theta)^2 Q(t,theta)^2 dtheta,
 g(t)=exp(-t/2) for t<0, g(t)=exp(123t/20) for t>=0,
 ||F||Y_a^2=integral_R g(t)N_a(t)^2 dt.

The completed directed computation and audit described below establish

 3.270 < ||F||Y_a < 485.632 for every 18/5<=a<=4.        (1)

Only the lower bound is new here; the upper bound is V174/proof 170. These are bounds in a low target, not in the high target of the nonlinear existence theorem. Neither bound alone tests nonlinear smallness or an inverse inequality.

## General angular Gram formula

Set alpha=(9-2a)/2 and beta=3/2. On a quadrant put z=cos(2 theta). The angular measure, after summing four quadrants, has mass

 M_a=2 Gamma(alpha)Gamma(beta)/Gamma(alpha+beta).

Its normalized z-distribution is the beta distribution transported by z=2u-1, with u in[0,1]. If m_n is the expectation of T_n(z)=cos(2n theta), then integration by parts, or the Chebyshev differential identities, gives

 m_0=1, m_1=(alpha-beta)/(alpha+beta),
 (n+alpha+beta)m_(n+1)=2(alpha-beta)m_n+(n-alpha-beta)m_(n-1). (2)

All endpoint integrations are legitimate because alpha,beta>0; one may first integrate on truncated intervals and use the vanishing factor (1-z^2) in the boundary term. For Q=sum_j q_j cos(2j theta), the exact normalized square is

 sum_(i,j) q_i q_j [m_(i+j)+m_|i-j|]/2.                (3)

The checker uses exact rational moments and outward Arb arithmetic for the coefficients and mass. For a=18/5, alpha=9/10, so (2) is

 (5n+12)m_(n+1)=-6m_n+(5n-12)m_(n-1), m_1=-1/4.

For a=4, M_a=pi, m_1=-1/2 and m_n=0 for all n>=2. Thus (3) also equals

 q_0^2 + sum_(j>=1)q_j^2/2 - q_0 q_1 - sum_(j>=1)q_j q_(j+1)/2. (4)

The independently evaluated form (4) is checked at every selected center. The first25 moments are independently derived by expanding Chebyshev polynomials in u and using the beta moments E[u^j]=(alpha)_j/(alpha+beta)_j.

## Interval lower enclosures

The original-data Green formulas, exact residual convolution and angular divisions are those verified in topics98,105 and134. Eight pairwise disjoint radial windows are selected from the already verified V164 partition. Selection uses floating scores only to choose which valid windows to inspect; it does not enter any enclosure.

On a selected window t=m+h z, |z|<=1, write the exact residual angular vector as sum_(j=0)^N f_j z^j plus a remainder e(z). The Green-ODE Taylor proof in proof 134 applies with the new positive angular Gram form. It gives

 ||e(z)||_a <= sqrt(1+M_a) C_522 E_raw,
 C_522=4(522)^4(1045),
 V_a=sum_(j>=1)||f_j||_a+sqrt(1+M_a) C_522 E_raw.

Here E_raw is the outward coefficient l1 product-error bound from all density and velocity modes. The two polynomial divisions and axis functional have the same coefficient majorant C_522 irrespective of the positive angular weight; only its total mass changes. Therefore

 N_a(t)>=max(0,N_a(m)-V_a)                             (5)

on the entire window, by the triangle inequality. The degree of the product polynomial may exceed N; every coefficient produced by that product is included in the sum defining V_a. The saved fresh-window energy computed internally with the old radial weight is ignored. Only its center and variation bounds are used with the new radial weight.

At each center an independent scalar identity also checks the axis extraction. Put A=-sum_j (-1)^j(2j+1)^2 H_j/2, where H_j are the density coefficients of rho/r^3, and put d=ell-sum_n (-1)^n P_n. Then

 gamma=d A'+(4ell-1-d-2d')A.

This agrees with the axis value of the complete angular residual. The old angular center norm is recomputed and checked against the accepted V164 journal, providing a further link to the original trial.

The new radial integral of each window [l,r] is enclosed directly as

 W(l,r)=exp(b l) expm1(b(r-l))/b,
 b=-1/2 or123/20 according to its side of zero.

Multiplying W by the square of the nonnegative rational lower endpoint in (5), then summing the eight disjoint contributions, gives a lower bound for the full squared norm. The contribution of every omitted interval and both infinite ends is nonnegative, so no tail subtraction or completeness assumption is needed for this lower bound.

Finally, |cos(theta)|^(8-2a) increases with a on[18/5,4]. Hence N_a>=N_(18/5) pointwise. The lower certificate calculated at a=18/5 applies to every member of the family.

## Computation, audit and limitations

The producer validates the original source, Green cache and previously accepted partition hashes. It recomputes all selected centers and their variation bounds from the original data at384 bits and degree28. An independent replay uses640 bits and degree32. The audit checks the exact window identities, disjointness, all moment formulas, all provenance hashes, positive window lower endpoints and the strict rational comparison with (327/100)^2. The resulting exact endpoints are retained in JSON rather than transcribed as long decimal tables.

The first attempt reused the much larger variation envelopes in the old angular norm. It produced only zero lower endpoints and is retained as an inconclusive attempt. This says nothing about whether the exact residual vanishes. The fresh angular computation in (5) is what supplies the positive lower bound.

The lower bound is deliberately partial and need not be close to the exact norm. Increasing its size is not a route to existence by itself. The high residual norm, base injectivity and quantitative inverse and nonlinear constants remain separate tasks.
