# A cubic spectral majorant for the source013 fractional norm

## Statement

Let g belong to H^3(R^2), use the unitary Fourier transform, and let

    T_j=integral |xi|^(2j)|g_hat(xi)|^2 dxi,  j=0,1,2,3.

Suppose 0<=L_j<=T_j<=U_j are certified rational bounds. Fix q=21/10 and rational nodes 0<=a<b. Set t=b-a, f(s)=(1+s)^q and

    c=[3(f(b)-f(a))-t(f'(b)+2f'(a))]/t^2,
    d=[t(f'(b)+f'(a))-2(f(b)-f(a))]/t^3.

The cubic P(s)=f(a)+f'(a)(s-a)+c(s-a)^2+d(s-a)^3 satisfies

    (1+s)^q <= P(s),  s>=0.

Write P(s)=sum_(j=0)^3 p_j s^j and suppose [p_j^-,p_j^+] contains each coefficient. Define

    M_j=max(p_j^- L_j,p_j^- U_j,p_j^+ L_j,p_j^+ U_j).

Then ||g||_(H^q)^2<=sum_j M_j. Coefficients are allowed to be negative: in that case the lower moment endpoint is essential. All T_j use the complete ordered Cartesian derivative tensor.

The source013 application fixes c_l=4076476460239181/2251799813685248, the accepted exact residual F013, W(X)=sqrt(1+4|X|^2), g=WF013 and the certified moment intervals of AT1418-1419, independently adopted by AN307. It uses a=1 and b=13000. This is a particular majorant, with no claim of optimality over nodes or polynomials.

## Complete argument

Direct substitution gives P(a)=f(a), P'(a)=f'(a), P(b)=f(b) and P'(b)=f'(b). For s distinct from a and b, subtract from f-P a multiple K(u-a)^2(u-b)^2 chosen to make the result zero at u=s. Repeated Rolle's theorem, counting the double zeros at a and b with multiplicity, gives a point xi between the smallest and largest of a,b,s where the fourth derivative of this difference vanishes. Since P is cubic,

    f(s)-P(s)=f''''(xi)(s-a)^2(s-b)^2/24.

Here f''''(xi)=q(q-1)(q-2)(q-3)(1+xi)^(q-4)<0. This proves f<=P on the entire nonnegative half-line, including both interpolation nodes by equality. The proof also covers s outside the node interval, since all points involved remain nonnegative and f has four continuous derivatives there.

Multiply the pointwise inequality by |g_hat|^2 and integrate. The left side is the squared Bessel norm; the right side is sum_j p_j T_j by the full-tensor Plancherel identities. A bilinear product on a rectangle attains its maximum at a vertex, so p_j T_j<=M_j for the supplied intervals. This proves the norm bound with every coefficient sign accounted for. All integrals are finite because g belongs to H^3 and q<3. No integration by parts on finite radial panels and no spectral concentration assumption is used.

For the exact arithmetic, let z_a=(1+a)^(1/10) and z_b=(1+b)^(1/10). The values f(a),f'(a),f(b),f'(b) are rational multiples of z_a,z_b. Hence every p_j is an exact rational linear combination of these two roots. Rational root enclosures satisfying z_-^10<=1+a<=z_+^10, and similarly at b, give containing coefficient intervals by signed interval linear arithmetic. Exact vertex products then give a rational squared-norm upper, and an exact square comparison proves the displayed norm upper.

## Dependencies and scope

The source013 moment intervals and H^3 membership are imported from the already audited full-plane source certificate and its moment refinement. This is a new consequence of those containing intervals, not new quadrature. It changes no candidate, parameter or weight. The previous fractional lower bound is retained when the new upper improves the previous one. The result supplies no P-S2, strong Holder, global background, near/far form, full inverse, invariant-ball or existence assertion. Independent AN and Opus review are requested through the published agent notes after the arithmetic check.
