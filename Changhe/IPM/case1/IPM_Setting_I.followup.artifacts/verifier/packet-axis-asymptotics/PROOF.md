# Exact axis Taylor coefficients and noninteger packet asymptotics

Date: 2026-10-20. This proof concerns the specified frozen Fourier packet, including its first axis trace. It makes no claim about a coupled profile or the regularity of a nearby exact solution.

## Statement and definitions

Let A>1, g>0, q=2(A-1), b=g/q and c_F=(2pi)^-2. Let Phi be smooth, compactly supported away from zero, satisfy integral Phi=0 and Phi(-t)=-conjugate(Phi(t)). Let v be the continuous packet of ../packet-dyadic-audit/PROOF.md. Fix an odd integer j>=1 with g>j-1. Put

    G_j(s)=d_y^j v(s,0)/j!,
    mu=(1+g-j)/A>0.

If mu is not an integer and m=floor(mu), then G_j is C^m near zero as a one-dimensional axis function, and

    G_j(s)=sum_(a=0)^m tau_(j,a) s^a
                      +C_(j,sign(s)) |s|^mu+o(|s|^mu).         (1)

For0<=a<=m, apart from(j,a)=(1,0), set p=j-1+Aa>0. Then

    tau_(j,a)=2 i^(j+a)c_F/[j!a!q]
          B(p/q,(g-p)/q) integral t^a Phi(t)|t|^(-2p/q)dt.      (2)

Here B(u,w)=integral_0^infinity z^(u-1)(1+z)^(-u-w)dz for u,w>0, so the beta integral used here is defined explicitly and converges. The exceptional coefficient is

    tau_(1,0)=-4i c_F/q integral Phi(t)log|t|dt.                (3)

Define the absolutely convergent complex integral

    J_mu(epsilon)=integral_0^infinity z^(-1-mu)
                [e^(i epsilon z)-sum_(a=0)^m(i epsilon z)^a/a!]dz,
                         epsilon in{-1,1}.                    (4)

Then the two one-sided leading coefficients are

    C_(j,epsilon)=2 i^j c_F/[j! A]
             integral Phi(t)|t|^(mu-2b) J_mu(epsilon sign(t))dt. (5)

These formulas specify the signs and constants without requiring an analytic continuation formula for Gamma. In particular, taking a=0 in(2) for j>=3 gives the beta formula quoted in the lead's axis-trace statement. Formula(3) supplies the first trace, for which substituting p=0 into that beta formula is invalid.

There exist imaginary even Phi of integral zero for which C_(j,+)=C_(j,-) is nonzero, for every allowed A,g,j with noninteger mu. Thus the singular axis coefficient can be nonzero even when all normalized higher traces vanish. Lower Taylor terms in(1) must not be dropped. Integer mu, possible logarithms and the general finite-order two-dimensional expansion are handled separately in ../packet-expansion-audit/PROOF.md; no integer asymptotic is asserted here.

## Axis differentiation and Taylor coefficients

Differentiating the sine j times at y=0 gives

    G_j(s)=2 i^j c_F/j! integral_0^infinity r^(j-2)
              integral Phi(t)e^(i s t r^A)(1+t^2r^q)^(-b)dt dr. (6)

For j>=3 the low-r absolute bound is C r^(j-2), integrable. For j=1, subtract the zero moment inside the t integral: for bounded s, it is O(r^A+r^q), and the r^-1 factor still gives an integrable bound. At infinity the bound is C r^(j-2-g), which is integrable precisely under the stated g>j-1. The same bounds hold locally uniformly in s. To justify the actual y derivative, the y-derivative of order c<=j has kernel r^(c-2) times sin(yr) or cos(yr), with high-r bound C r^(c-2-g), and the low-r case of the first y derivative uses the same moment cancellation uniformly on compact(s,y) sets. Lower y derivatives have better high-r powers; at order zero and one use the density proof's moment cancellation. Dominated differentiation therefore gives the actual derivative in(6), not just a formal trace.

An s derivative of order a>=1 inserts(i t r^A)^a. Its low-r power is r^(j-2+Aa), integrable for every a>=1. At high r it is r^(j-2+Aa-g), integrable if a<mu. For j>=3 the same statement also holds for a=0. The exceptional j=1,a=0 was treated above. The high-r bounds are independent of s. For j=1,a=0, continuity uses e^(i s t r^A)-1=O(|s|r^A) locally uniformly in s together with the amplitude cancellation. These locally uniform bounds justify differentiation and continuity through order m on a neighbourhood of zero, so G_j is C^m as asserted.

For p=j-1+Aa>0, evaluation at s=0 and division by a! gives the radial integral

    integral_0^infinity r^(p-1)(1+t^2r^q)^(-b)dr
        =|t|^(-2p/q)/q B(p/q,(g-p)/q),

by z=t^2r^q. Both beta arguments are positive because0<p<g. The t support is compact and separated from zero, so Fubini applies. This proves(2).

For j=1,a=0, subtract the reference amplitude(1+r^q)^(-b), whose t integral vanishes by integral Phi=0. With z=r^q and a positive scalar d=t^2, define

    H(d)=integral_0^infinity [(1+d z)^(-b)-(1+z)^(-b)] dz/z.

This difference is integrable at zero and infinity, uniformly when d ranges in a compact subset of(0,infinity). Differentiating with respect to d gives

    H'(d)=-b integral_0^infinity (1+d z)^(-b-1)dz=-1/d,

where the differentiation is dominated on such compact d intervals. Since H(1)=0, H(d)=-log d. Consequently the original radial difference is -2 log|t|/q. Multiplying by2i c_F proves(3). This also shows why the answer is independent of b despite the singular separate beta expressions at p=0.

## Remainder rescaling and absolute domination

Let E_m(z)=e^(i z)-sum_(a=0)^m(i z)^a/a!. Subtracting the Taylor terms proved above from(6) gives exactly

    G_j(s)-sum_(a=0)^m tau_(j,a)s^a
       =2 i^j c_F/j! integral_0^infinity r^(j-2)
          integral Phi(t)E_m(s t r^A)(1+t^2r^q)^(-b)dt dr.       (7)

At j=1,a=0 this equality follows by subtracting the two convergent grouped integrals first. In every case the new integrand is absolutely integrable before t integration: near r=0, E_m(s t r^A)=O(r^(A(m+1))); at infinity it is bounded by C(1+r^(Am)), and m<mu. Thus the manipulations in(7) are justified independently of cancellation in(6).

For s!=0 write epsilon=sign(s) and set r=|s|^(-1/A)u. Factoring |s|^(g/A) out of the amplitude and using mu=(1+g-j)/A turns(7) divided by |s|^mu into

    2 i^j c_F/j! integral_0^infinity u^(j-2)
        integral Phi(t)E_m(epsilon t u^A)
                        (|s|^(q/A)+t^2u^q)^(-b)dt du.          (8)

Because b>0, the amplitude in(8) is at most |t|^(-2b)u^-g. The fixed t support has positive lower and finite upper bounds. Hence its absolute integrand is dominated for u<=1 by C u^(-1-A mu+A(m+1)), whose exponent is greater than -1, and for u>=1 by C u^(-1-A mu+Am), whose exponent is less than -1. Dominated convergence proves the finite limit obtained by replacing the amplitude in(8) by |t|^(-2b)u^-g.

In this limit set z=|t|u^A. Then

    u^(-1-A mu)du=|t|^mu z^(-1-mu)dz/A.

Fubini is justified by the absolute majorants just given. This yields exactly(4) and(5), and proves the little-o remainder in(1) for each sign separately. Near zero, the integrand in(4) is O(z^(m-mu)); at infinity it is O(z^(m-1-mu)); these powers also directly prove its absolute convergence. This is a direct one-dimensional estimate and does not rely on the two-dimensional quasi-homogeneous expansion.

## A nonzero leading coefficient without a Gamma formula

Put n=floor(m/2), so the real part of E_m(z) is

    F_n(z)=cos z-sum_(k=0)^n(-1)^k z^(2k)/(2k)!.

For z>=0, F_0(z)=cos z-1 is nonpositive and not identically zero. For n>=1,

    F_n''(z)=-F_(n-1)(z),  F_n(0)=F_n'(0)=0.

Twice integrating this identity proves that F_n has constant weak sign(-1)^(n+1), and is nonzero on a nonempty interval. Since the integral in(4) is absolutely convergent, its real part is integral z^(-1-mu)F_n(z)dz, which has that sign and is nonzero. Also J_mu(-1)=conjugate(J_mu(1)).

Take Phi=i phi, with phi real and even. Combining t and -t in(5) gives the same coefficient on either s side, explicitly

    C_(j,+)=C_(j,-)=4 c_F i^(j+1)/[j! A]
           times Re J_mu(1) integral_0^infinity phi(t)t^(mu-2b)dt.
 Since j is odd, i^(j+1) is real and nonzero. Moreover

    mu-2b = [(1-j)(A-1)-g]/[A(A-1)] <0.

Choose phi on the positive half-line as the difference of two nonnegative smooth bumps of equal integral, with the entire support of the first strictly to the left of the second, both away from zero. Extend evenly to the negative half-line. The full integral of phi is zero, while the displayed weighted positive-half-line integral is strictly positive because t^(mu-2b) is strictly decreasing. Thus C_(j,+)=C_(j,-) is nonzero. This proves existence of data with the singular trace, without silently assuming a moment does not vanish.

## Scope and verification record

This theorem supplies an axis C^m statement and a one-dimensional asymptotic for a specified packet. It does not promote the density to ordinary two-dimensional C^j or to a coupled solution. The all-order normalized trace vanishing follows from the separate direct estimate in the packet dyadic proof, including orders with g<=j-1 that are not covered here. The first-trace coefficient may be relevant to bending calculations, but no coordinate correction or profile family is constructed. Mathematical review, exact algebra checks and any numerical illustrations belong in verification/. The actual Claude Opus 5.5 follow-up completed at 2026-10-20T23:09:21Z and confirmed the mathematics subject to three wording repairs, all applied above. Its two external-dependency questions were checked by this verifier against the confirmed dyadic proof AV131 and the lead's displayed beta formula. The earlier truncated review is not counted as a completed confirmation. Status CONFIRMED after these checks; see verification/review_resolution.json.
