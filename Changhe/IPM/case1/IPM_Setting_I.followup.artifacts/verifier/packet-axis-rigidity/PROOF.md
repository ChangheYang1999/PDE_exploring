# Smooth first-axis traces of imaginary-even frozen packets

Date: 2026-10-21. Status: CONFIRMED for the explicit scalar trace after independent review. This concerns an explicit frozen packet and its one-dimensional first trace. It is not a theorem about the full coupled IPM operator.

## Statement and notation

Let A>1, g>0, q=2(A-1), b=g/q, eta=q/A and c_F=(2pi)^(-2). Let phi be real, smooth and compactly supported in an interval [delta,D] contained in (0,infinity), with integral phi(t)dt=0. Extend phi evenly and put Phi=i phi. Define the packet v by the convergent, grouped integral in ../packet-dyadic-audit/PROOF.md, and its first trace G(s)=d_y v(s,0). Explicitly,

    G(s)=-4 c_F integral_0^infinity r^(-1)
          integral_delta^D phi(t) cos(s t r^A)(1+t^2 r^q)^(-b)dt dr.       (1)

The trace identification can be checked directly: the packet integral is 2i c_F times the integral of sin(yr)r^(-2) against the full t integral. One y derivative is justified by the bounds O(r^(q-1)+r^(A-1)) at zero and O(r^(-1-g)) at infinity. For imaginary-even Phi, its full t integral is 2i times the positive-t cosine integral. Thus 2i times 2i gives the coefficient -4 in (1). The theorem below can also be read purely as a statement about the explicit function (1).

The inner t integral is performed first at zero frequency. For n>=0 define

    M_n=integral_delta^D phi(t)t^(-2(b+n)/A)dt,
    a_n=(-1)^n (b)_n/n!,
    mu_n=eta(b+n)=(g+nq)/A,                               (2)

where (b)_0=1 and (b)_n=b(b+1)...(b+n-1). Every a_n is nonzero.

If phi is nonzero, there is a least integer N>=0 for which M_N is nonzero. Let mu=mu_N. Then:

- If mu is not an integer, G is not C^ceil(mu) at zero. After subtracting its Taylor polynomial through floor(mu), it has a nonzero multiple of |s|^mu plus o(|s|^mu).
- If mu is a positive even integer m, G has a nonzero s^m log(1/|s|) term and is not C^m at zero.
- If mu is a positive odd integer m, G has a nonzero |s|^m term after its lower Taylor terms and is not C^m at zero.

Consequently G is C^infinity on a neighborhood of zero if and only if phi=0. Nevertheless, for every finite nonnegative integer K there is a nonzero phi satisfying all the hypotheses for which G is C^K. These assertions concern the axis trace; they give no improvement of two-dimensional packet regularity and no coupled-profile exclusion.

## An exact convergent spectral representation

At r=0, the zero integral of phi makes the inner integral in (1) O(r^q+|s|r^A), locally uniformly in s. At infinity the integrand is O(r^(-1-g)). Thus (1) converges. Its value at zero is

    G(0)=8 c_F/q integral_delta^D phi(t)log(t)dt.             (3)

For completeness, subtract (1+r^q)^(-b) inside the t integral, using its zero moment. With z=r^q the radial difference is -2log(t)/q: differentiating integral_0^infinity [(1+d z)^(-b)-(1+z)^(-b)]dz/z with respect to d gives -1/d and its value at d=1 is zero. Multiplication by -4c_F gives (3). All differentiated integrals are dominated on compact positive d intervals.

Subtract G(0) before making a t-dependent change of radial variable. The integrand then contains cos(s t r^A)-1, which is O(r^(2A)) at zero. It is absolutely integrable in (r,t) both at zero and infinity. Set k=t r^A, so dr/r=dk/(A k), and define

    H(k)=integral_delta^D phi(t)(1+k^eta t^(2/A))^(-b)dt,
    h(k)=H(k)/k.

Fubini and that change of variables give the exact identity

    G(s)-G(0)=-4 c_F/A integral_0^infinity [cos(sk)-1]h(k)dk. (4)

The zero moment gives H(k)=O(k^eta) at zero, while H(k)=O(k^(-g/A)) at infinity. Hence h is integrable. Formula (4) can therefore also be written as a constant plus the cosine transform of h. The subtraction avoids an unjustified interchange of the separately divergent integrals defining G(0); no constant or harmonic gauge is silently changed.

## Why a first nonzero moment exists

Suppose that every M_n is zero. Write x=t^(-2/A), a continuous one-to-one change from [delta,D] to a compact positive interval. For every real polynomial p, the moment assumptions imply

    integral_delta^D phi(t)t^(-2b/A)p(t^(-2/A))dt=0.         (5)

There are polynomials converging uniformly on that x interval to the continuous function f(x)=phi(x^(-A/2)). One elementary justification is the Bernstein approximation on [0,1] after affine rescaling. Its weights have mean x and variance x(1-x)/n; uniform continuity bounds the contribution within a fixed distance epsilon of x, while the variance estimate bounds the complementary total weight by 1/(4n epsilon^2). These two bounds prove uniform convergence, including the endpoints.

Pass to the limit in (5), using the finite integral of |phi|t^(-2b/A). It gives integral phi(t)^2 t^(-2b/A)dt=0. The weight is strictly positive and phi is continuous, so phi=0. Contrapositively, a nonzero phi has a first nonzero M_N, because the nonnegative integers are well ordered.

## The first nonzero high-frequency coefficient

Choose K_0 large enough that k^eta delta^(2/A)>=2 for k>=K_0. The Taylor expansion of (1+z)^(-b) at z=0, with a uniformly bounded remainder on |z|<=1/2, yields, for every fixed L,

    H(k)=sum_(n=0)^L a_n M_n k^(-mu_n)
                       +O(k^(-mu_(L+1))).                 (6)

Indeed factor k^(-b eta)t^(-2b/A), expand in z=k^(-eta)t^(-2/A), and integrate on the fixed compact t interval. All constants may depend on A,g,phi,L. For the least N from above,

    h(k)=a_N M_N k^(-1-mu)+O(k^(-1-mu-eta)).                (7)

Every integer j<mu satisfies integral k^j |h(k)|dk<infinity. Dominated differentiation therefore gives G in C^floor(mu) when mu is noninteger and in C^(m-1) when mu=m is an integer. These bounds justify the Taylor polynomials below.

Let c=a_N M_N, which is nonzero. Splitting (4) at K_0 reduces G, up to a C^infinity function, to -4c_F/A times

    c integral_(K_0)^infinity k^(-1-mu)cos(sk)dk + Q(s),     (8)

where Q is the cosine transform of a real remainder bounded by C k^(-1-mu-eta). The finite-frequency part is C^infinity by differentiation under the integral: k is bounded and h is integrable there.

If mu is not an integer and m=floor(mu), choose alpha with mu<alpha<min(mu+eta,m+1). The remainder has moments through order m, hence Q is C^m by dominated differentiation. The Taylor remainder of cos(z) through degree m is bounded by C|z|^alpha for all real z: near zero it is O(|z|^(m+1)), while for |z|>=1 the polynomial and cosine are O(1+|z|^m). Integrating this bound against the remainder proves

    Q(s)-sum_(a=0)^m Q^(a)(0)s^a/a! = O(|s|^alpha)=o(|s|^mu). (9)

If mu=m is an integer, the remainder has an integrable m-th moment since eta>0. Thus Q is C^m. It is even, so for odd m its m-th Taylor coefficient is zero. These estimates ensure that the smaller tail cannot cancel the singular term in (8).

## The nonzero singular term of the homogeneous tail

First suppose mu is not an integer, and put m=floor(mu), n=floor(m/2). Subtract the cosine Taylor terms through m in the homogeneous integral, then set z=|s|k. The remainder divided by |s|^mu tends to

    J_mu=integral_0^infinity z^(-1-mu)
             [cos z-sum_(a=0)^n (-1)^a z^(2a)/(2a)!]dz.     (10)

This integral converges absolutely: the bracket is O(z^(2n+2)) at zero and O(1+z^(2n)) at infinity, and 2n<mu<2n+2. The actual rescaled lower limit is |s|K_0; the omitted integral from zero to |s|K_0 is O(|s|^(2n+2-mu)), tending to zero. Its value is nonzero. To prove this without a Gamma continuation, set E_n equal to the bracket. E_0=cos z-1 is nonpositive and strictly negative on an interval. For n>=1, E_n''=-E_(n-1) and E_n(0)=E_n'(0)=0. Two integrations imply the weak constant sign (-1)^(n+1), with strict sign on an interval. The positive weight in (10) preserves that sign. The coefficient in G is therefore -4c_F c J_mu/A, which is nonzero. Together with (9), this excludes C^(m+1), since such regularity would make its Taylor remainder O(|s|^(m+1)).

If mu=m is odd, exactly the same subtraction through degree m-1 gives (10) with n=(m-1)/2. It is still absolutely convergent and nonzero, and the homogeneous integral has a nonzero |s|^m remainder. The finite-frequency part and Q are even and C^m, so their order-m coefficients vanish. A C^m even function has Taylor remainder o(|s|^m) after its lower terms. This contradiction excludes C^m.

If mu=m is even, subtract the terms through m-2. On K_0<=k<=1/|s| the next cosine term is (-1)^(m/2)(sk)^m/m!, and its integral is

    (-1)^(m/2)s^m log(1/|s|)/m! + O(|s|^m).

Here log(1/(|s|K_0))=log(1/|s|)-log(K_0), whose constant contributes O(|s|^m). The further Taylor remainder integrates to O(|s|^m), and the k>=1/|s| tail, including the subtracted lower polynomial terms, is also O(|s|^m). Thus the logarithmic coefficient in G is -4c_F c (-1)^(m/2)/(A m!), which is nonzero. The C^m remainder Q cannot cancel it. This proves all three obstructions. Since mu_N is finite for the first nonzero moment, nonzero phi always prevents a smooth trace.

## Arbitrarily many finite cancellations

Fix a finite K. Choose N sufficiently large that mu_N>K. Select N+2 nonzero real smooth bumps with mutually disjoint compact supports inside one positive interval. Their linear span has dimension N+2. The N+1 real homogeneous conditions consisting of integral phi=0 and M_n=0 for 0<=n<N have a nonzero solution in that span. Disjoint supports ensure its resulting function is nonzero, regardless of any rank deficiency of the constraints.

Equation (6) then gives h(k)=O(k^(-1-mu_N)), and the k^K-weighted absolute integral is finite. The low-frequency moment bounds were already proved. Dominated differentiation of (4) gives G in C^K. The preceding moment argument still supplies some finite first nonzero M_j with j>=N, so the same trace eventually fails a higher finite regularity class. This proves both finite-cancellation flexibility and all-orders rigidity, without claiming a uniform bound on the first failing order.

## Dependencies and scope

The packet and first-trace conventions agree with ../packet-dyadic-audit/PROOF.md. The critical and noncritical tail calculations are reconstructed above; ../packet-integer-axis/PROOF.md and ../packet-axis-asymptotics/PROOF.md contain the corresponding one-term constants. The proof uses real imaginary-even data only. It does not characterize general complex packet data, other frozen solutions, variable-coefficient kernels, nonlinear families, or the regularity of any coupled profile. It does not turn finitely many B_j tests into a proof of smoothness and does not change either task endpoint. It does not duplicate the separate team's norm estimates for the frozen transport inverse.
