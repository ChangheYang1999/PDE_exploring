# Sharp bounds for the frozen Mellin compatibility map

This proof is written before its new computations. Its real creation time and hash are in evidence/proof_first.json. Status OPEN until actual-model review and own adjudication. This result corrects the ancillary sentence “No raw unweighted L2_xi bound follows or is claimed” in ../logarithmic_frozen_range_inverse/REVIEW_RESPONSE.md. That negative assertion is false. The parent's closed-range theorem and inverse estimate do not use it and remain unchanged. Old reviewed bytes are preserved for audit.

## Statement and notation

Fix A>0, D=2A+1, finite real a and s>=0. Put c=-A(a-1/2)-1, u=D/2-c and v=sD-u. Assume u>0 and v>0, so in fact s>0. On x>0 set F(z,y)=exp((1/2-a)z)f(exp z,y) and ||f||Y=||F||Hs(R²), with the unitary Fourier convention. Write H(xi,eta)=Fhat(xi,eta), B=1+xi², t=u/D, w=v/D, so t,w>0 and t+w=s. The Fourier description of Y is the full complex Hilbert space with squared norm integral_R² (B+eta²)^s |H|² dxi deta. The parity-restricted real subspace is treated below.

For sigma in{+1,-1}, define for almost everyxi

 J_sigma(xi)=integral_0^infinity eta^(-c/D+iAxi/D) H(xi,sigma eta) deta.

Define the positive finite constant

 N=(1/2)integral_0^infinity q^(t-1)(1+q)^(-s)dq
  =(1/2)integral_0^1 z^(t-1)(1-z)^(w-1)dz
  =Gamma(t)Gamma(w)/(2Gamma(s)).                                 (1)

Then each integral defining J is absolutely convergent almost everywhere, the map is bounded and surjective from Y onto the two-copy space L2(R,B^w dxi), and

 sum_sigma integral_R B^w |J_sigma|² dxi <= N ||f||Y².             (2)

The operator norm in (2) is exactly sqrt(N) and is attained by nonzero inputs. Its kernel is the closed compatible forcing subspace in the parent range theorem. It follows that

 sum_sigma integral_R |J_sigma|² dxi <= N ||f||Y²,                 (3)

and this unweighted operator norm is also exactly sqrt(N), though it is not attained by any nonzero input. These norm statements hold also on the real odd-in-y subspace, with the corresponding symmetries imposed on the target. No full IPM inverse or decisive PDE endpoint is claimed.

## Direct fibre calculation

In a fixed sign copy let

 b_xi(eta)=eta^(-(c+iAxi)/D)(B+eta²)^(-s), eta>0.

The weighted pairing integral H conjugate(b_xi)(B+eta²)^s deta is exactly J_sigma; the sign of the imaginary exponent is therefore positive in J. Its representing vector has squared norm

 n_xi=integral_0^infinity eta^(-2c/D)(B+eta²)^(-s)deta.

Set q=eta²/B. The eta-power gives B^(-c/D)q^(-c/D), the weight gives B^(-s)(1+q)^(-s), and the Jacobian is sqrt(B)q^(-1/2)/2. Thus the power of B is -c/D-s+1/2=t-s=-w, while the power of q is -c/D-1/2=t-1. Hence

 n_xi=B^(-w)N.                                                   (4)

The q-integral converges at0 because t>0 and at infinity because t-s=-w<0. Weighted Cauchy-Schwarz proves absolute existence and |J_sigma(xi)|²<=n_xi integral_0^infinity(B+eta²)^s|H(xi,sigma eta)|²deta. Fubini, multiplication by B^w and summation give (2). As B>=1 and w>0, (3) follows immediately. This last implication is the correction to the earlier false negative sentence.

For completeness, q=z/(1-z) gives the second integral in (1), including its exponents and Jacobian. The gamma identity follows directly from the positive double integral defining Gamma(t)Gamma(w): set r1+r2=r and r1/(r1+r2)=z, whose Jacobian is r. It separates into Gamma(t+w) times the beta integral. Thus no analytic continuation is involved.

## Surjectivity, sharpness and a right inverse

Given any target pair j_sigma in L2(B^w dxi), set

 H(xi,sigma eta)=j_sigma(xi)b_xi(eta)/n_xi.                         (5)

Its squared Y norm, by (4), is sum_sigma integral |j_sigma|²/n_xi dxi=N^(-1)sum_sigma integral B^w|j_sigma|²dxi. It is measurable and belongs to the Fourier Hilbert space; its inverse Fourier transform defines an element of Y. The moment equals j_sigma pointwise almost everywhere. This proves surjectivity and a right inverse of norm1/sqrt(N). It also gives equality in (2) for every nonzero target and proves the sharp constant sqrt(N).

To see sharpness for the unweighted target, take H(xi,sigma eta)=C_sigma(xi)b_xi(eta), with C nonzero, bounded and supported in |xi|<delta. Then J_sigma=C_sigma n_xi. The ratio of the squared unweighted output norm to squared input norm is

 N [sum_sigma integral |C_sigma|² B^(-2w)dxi]
   /[sum_sigma integral |C_sigma|² B^(-w)dxi].                    (6)

It lies between N(1+delta²)^(-w) and N. Let delta decrease to0 and normalize the input. The ratios tend to N, proving sharpness of (3). For a nonzero input with nonzero J, the inequality integral|J|²<integral B^w|J|² is strict, because B^w>1 except on the null set xi=0. If J=0, the norm ratio is zero and cannot attain the positive constant. Consequently there is no nonzero extremizer for (3).

Real fields odd in y satisfy H(xi,-eta)=-H(xi,eta) and H(-xi,eta)=-conjugate(H(xi,eta)). Since b_(-xi)=conjugate(b_xi), their moments obey j_-=-j_+ and j_+(-xi)=-conjugate(j_+(xi)). Formula (5) preserves precisely these relations, so surjectivity onto the restricted target and the norm upper bound persist. For the lower bound choose C_+=i chi with chi real, even, nonzero and smooth compact in |xi|<delta, and C_-=-C_+. This produces the required real odd inputs for (6). The same choice at fixed delta gives equality in (2). Even extension in the physical x variable is compatible with the original half-plane logarithmic definition; no regularity across x=0 is asserted or needed here.

## Two numerical methods for the actual constant

For the actual dyadic k=1615536043799051/9007199254740992, take A=2/k-1, a=0 and s=153/50. Then u=1+1/k and t=u/D, w=s-t. In this case 0<t<1 and 2<w<3. The primary checker must decode the literal NPZ using Fraction, verify these strict rational conditions, and enclose (1) by Arb gamma functions and square root. It must bind the unchanged parent records. A displayed interval is to be accepted only when its endpoints are strictly outward.

The independent calculation decodes the hexadecimal dyadic independently using integer arithmetic and fmpq. It does not use gamma functions. Split the z-integral at1/2 and exchange z with1-z on the second half. For p,q>0 define

 S(p,q)=integral_0^(1/2) z^(p-1)(1-z)^(q-1)dz
       =sum_(n=0)^infinity (1-q)_n/n! * 2^(-p-n)/(p+n).           (7)

The generalized binomial coefficients follow from the recurrence of the analytic solution of (1-z)g'=(1-q)g with g(0)=1. The series converges uniformly on[0,1/2], and multiplication by the integrable z^(p-1) permits termwise integration. Therefore N=[S(t,w)+S(w,t)]/2.

For n>=2 in both actual parameter choices, (n+1-q)>0 and <n+1, because q is either t in(0,1) or w in(2,3). The ratio of successive absolute terms in (7) is

 (n+1-q)/(n+1) * (1/2) * (p+n)/(p+n+1) <1/2.                    (8)

In each series all terms of index n>=2 are positive: when q=w, the first two factors of (1-q)_2 are negative and all later factors are positive; when q=t, every factor is positive. For Nterms>=3, the tail from index Nterms is thus positive and at most twice that first omitted term. Exact rational Pochhammer coefficients and mpmath.iv powers2^(-p) give a directed finite-sum enclosure and this rigorous tail. No numerical quadrature or truncation without a tail is used. Interval square root then encloses sqrt(N) independently. All numerical endpoints must be compared to the primary strict window using exact rationals.

The two methods share the proved beta identity but use different algorithms and arithmetic libraries. They do not constitute two independent analytic proofs. The functional-analytic statements require reconstruction of the full argument by the verifier and actual Opus5.5. No smoothness, center normalization, or nonlinear IPM property is inferred from arbitrary elements of this Fourier Hilbert space.
