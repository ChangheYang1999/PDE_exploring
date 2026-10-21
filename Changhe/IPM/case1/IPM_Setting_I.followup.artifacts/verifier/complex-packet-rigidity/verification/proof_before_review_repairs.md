# All complex compact packets have a nonsmooth first trace

Date: 2026-10-21. Status: proof under independent review. The origin in this statement is the singular point of a frozen packet in local coordinates (s,y), not the self-similar center of the original profile.

## Statement

Let A>1, g>0, q=2(A-1), b=g/q, eta=q/A and c_F=(2pi)^(-2). Let Phi be a smooth complex function supported in delta<=|t|<=D, where 0<delta<D<infinity. Assume

    Phi(-t)=-conjugate(Phi(t)),    integral_R Phi(t)dt=0.

On t>0 write Phi(t)=u(t)+i v(t), with u and v real. Thus integral v=0. Define the real frozen packet by the convergent grouped integral

    V(s,y)=2i c_F integral_0^infinity sin(yr)r^(-2)
              integral_R Phi(t) exp(i s t r^A)(1+t^2 r^q)^(-b)dt dr.

This is the same packet convention as ../packet-dyadic-audit/PROOF.md. Its first trace G(s)=partial_y V(s,0) is smooth near zero if and only if Phi=0. In particular, no nonzero packet in this class is smooth in a two-dimensional neighborhood of its singular point.

More precisely, for f=u or f=v set

    M_n[f]=integral_delta^D f(t)t^(-2(b+n)/A)dt,
    a_n=(-1)^n(b)_n/n!,    mu_n=(g+nq)/A.

If f is nonzero, let N be its first nonzero moment and mu=mu_N. The v contribution has the even singularities proved in ../packet-axis-rigidity/PROOF.md. The u contribution is odd and has, after its justified lower Taylor terms:

- a nonzero multiple of sign(s)|s|^mu plus o(|s|^mu) if mu is not an integer;
- a nonzero multiple of sign(s)|s|^m plus o(|s|^m) if mu=m is a positive even integer;
- a nonzero s^m log(1/|s|) term with an O(|s|^m) remainder if mu=m is a positive odd integer.

The corresponding trace fails C^ceil(mu) in the noninteger case and C^m in the integer cases. For every finite integer K>=0 there is nevertheless a nonzero admissible Phi for which G is C^K. No uniform bound on the first failing derivative is asserted.

## Trace identification and separation of parity

Pair t with -t. The full inner integral is

    2i integral_delta^D [u(t)sin(s t r^A)+v(t)cos(s t r^A)]
                         (1+t^2 r^q)^(-b)dt.

The factor 2i in the packet formula therefore produces the real coefficient -4c_F. Differentiation once in y is justified as follows. At r=0 the zero integral of v and the sine factor for u make the paired inner integral O(r^q+|s|r^A), uniformly on compact s intervals. After differentiating sin(yr)r^(-2), the bound is O(r^(q-1)+r^(A-1)), which is integrable because A,q>0. At infinity it is O(r^(-1-g)). Dominated differentiation gives

    G(s)=-4c_F integral_0^infinity dr/r
        integral_delta^D [u(t)sin(s t r^A)+v(t)cos(s t r^A)]
                              (1+t^2 r^q)^(-b)dt.          (1)

The u contribution G_u is odd in s, and G_v is even. Thus G_u=(G(s)-G(-s))/2 and G_v=(G(s)+G(-s))/2. They cannot cancel one another's lack of smoothness. The even part, with integral v=0, is exactly the trace proved in topic82. The rest of this proof treats u without imposing integral u=0.

## Exact sine representation and moment rigidity

For each fixed s the u integrand in (1) is absolutely integrable in (r,t): use |sin(s t r^A)|<=|s|D r^A near zero and O(r^(-g)) for the angular factor at infinity. Set k=t r^A and use dr/r=dk/(A k). Fubini gives

    G_u(s)=-4c_F/A integral_0^infinity sin(sk) h_u(k)dk,
    h_u(k)=k^(-1) integral_delta^D u(t)(1+k^eta t^(2/A))^(-b)dt.  (2)

Here h_u(k)=O(1/k) at zero. It need not be integrable there; the sine in (2) must be retained. Its contribution on 0<k<K_0 is C^infinity in s. For derivative order j>=1 the bound k^j |h_u(k)|=O(k^(j-1)) is integrable, and continuity at order zero follows from the original sine bound. This establishes the smoothness assertion without dropping a divergent constant.

If all moments M_n[u] vanish, then u=0. Indeed x=t^(-2/A) maps [delta,D] one-to-one onto a compact positive interval. For every polynomial p,

    integral u(t)t^(-2b/A) p(t^(-2/A))dt=0.

Uniform polynomial approximation of the continuous function x -> u(x^(-A/2)) implies integral u(t)^2 t^(-2b/A)dt=0, hence u=0. A complete elementary Bernstein approximation argument is given in topic82 and applies without a zero-mean hypothesis. Consequently a nonzero u has a finite first nonzero moment N.

For k large, factor out k^(-b eta)t^(-2b/A) and expand (1+z)^(-b) with z=k^(-eta)t^(-2/A). Its Taylor remainder is uniform on the fixed t interval once |z|<=1/2. For that first N,

    h_u(k)=c k^(-1-mu)+O(k^(-1-mu-eta)),
    c=a_N M_N[u] != 0,    mu=mu_N>0.                     (3)

Every weighted absolute moment of the high-frequency part of order j<mu is finite. This justifies the Taylor coefficients through floor(mu) when mu is noninteger, and through m-1 when mu=m is integer. In the following discussion the lower-frequency contribution is smooth.

## Noninteger exponents and even integer cusps

First let mu be noninteger and m=floor(mu). Subtract the sine Taylor polynomial containing all odd powers <=m. If 0<mu<1 this polynomial is empty. Rescale z=|s|k in the leading tail of (3). Its Taylor remainder divided by sign(s)|s|^mu tends to

    J_mu=integral_0^infinity z^(-1-mu)[sin z-T_m(z)]dz,    (4)

where T_m is that polynomial. The integral is absolutely convergent: the next unused odd power is greater than mu, while every subtracted power is less than mu. The removed interval 0<z<|s|K_0 tends to zero by this same integrability.

Its value is nonzero. For 0<mu<1, pair successive half-periods. Absolute integrability permits regrouping, and the nth pair equals

    integral_0^pi sin z [(z+2n pi)^(-1-mu)
                         -(z+(2n+1)pi)^(-1-mu)]dz > 0.

The first pair is integrable at zero because mu<1. Every pair is positive, so J_mu>0. For mu>1 write T_m=sum_(j=0)^n (-1)^j z^(2j+1)/(2j+1)!, so 2n+1<mu<2n+3. Set S_n=sin z-T_m(z). The base S_0=sin z-z is negative for z>0. For n>=1, S_n''=-S_(n-1) and S_n(0)=S_n'(0)=0. Two integrations give the constant sign (-1)^(n+1), strict on an interval. Thus J_mu has that nonzero sign.

The remainder in (3) cannot remove this term. Choose mu<alpha<min(mu+eta,m+1). The sine Taylor remainder through m is bounded by C|z|^alpha globally, since its local order is at least m+1 and its large-z growth is at most C(1+|z|^m). Integrating against the remainder yields an O(|s|^alpha)=o(|s|^mu) Taylor remainder. The leading coefficient in G_u is therefore -4c_F c J_mu/A, which is nonzero. C^(m+1) regularity would instead give a Taylor remainder O(|s|^(m+1)), a contradiction.

If mu=m is a positive even integer, use the odd Taylor polynomial through m-1 in (4). It has degree 2n+1=m-1, and m lies strictly between 2n+1 and 2n+3. The same constant-sign proof gives J_m != 0 and the leading sign(s)|s|^m term. The remainder in (3) has an integrable m-th moment and hence is C^m; it is odd, so its degree-m Taylor coefficient is zero. A C^m odd function has remainder o(|s|^m) after its lower Taylor polynomial. This contradicts the nonzero term and proves the even-integer obstruction.

## Odd integer logarithms

Let mu=m=2n+1. Subtract the sine Taylor polynomial through m-2. In K_0<=k<=1/|s| the next sine term contributes

    (-1)^n s^m/m! integral_(K_0)^(1/|s|) dk/k
      =(-1)^n s^m log(1/|s|)/m! + O(|s|^m).

The subsequent Taylor remainder integrates to O(|s|^m), since its next power is m+2. For k>=1/|s| the sine and subtracted lower polynomial terms each integrate to O(|s|^m). The error in (3) is C^m because eta>0, so it has no logarithmic term. Thus G_u has logarithmic coefficient

    -4c_F c (-1)^n/(A m!) != 0.

A C^m function has a finite degree-m Taylor coefficient and cannot have this logarithmic remainder. This also covers m=1, where the subtracted lower polynomial is empty.

## Smoothness rigidity and finite cancellation

If G is smooth, its even and odd projections are smooth. Topic82 forces v=0; the preceding argument forces u=0. Conversely Phi=0 gives V=G=0. If V were smooth on a two-dimensional neighborhood, its derivative restricted to y=0 would be smooth, proving the stated two-dimensional consequence.

For any finite K choose N with mu_N>K. In the real vector space spanned by N+1 nonzero smooth bumps with disjoint supports inside (delta,D), the N homogeneous conditions M_n[u]=0 for 0<=n<N have a nonzero solution. Its odd real extension Phi automatically satisfies both reality and zero-integral conditions. Expansion (3), with all coefficients below N absent, implies h_u(k)=O(k^(-1-mu_N)) at infinity. The high-frequency K-th moment is finite; the low-frequency part was shown smooth. Thus G is C^K. Some later moment is nonzero by rigidity, so it eventually fails a higher finite regularity class.

## Dependencies, evidence and limits

Dependencies are the explicit packet convention and convergent trace calculation in topic73, and the full even-sector proof and polynomial approximation argument in topic82. The odd-sector tail proof above is complete and separate. The accompanying exact algebra checks and scalar quadrature examples test formulas but are not substitutes for this argument.

This result covers all complex compact annular Phi satisfying the specified reality and zero-integral conditions in this explicit packet construction. It does not characterize every frozen solution, arbitrary Fourier distributions, variable-coefficient kernels or nonlinear families. Its singular point is a frozen source point; no implication that the strong-setting profile must be smooth there is added. It gives no exclusion theorem for the coupled profile class and changes neither task endpoint. It does not duplicate the separate team's Holder inverse estimates.
