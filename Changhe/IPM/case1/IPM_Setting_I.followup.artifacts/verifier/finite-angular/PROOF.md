# No nonzero profile with finitely many physical angular modes

Date: 2026-10-20. Status: proved for the restricted class below. Reviewed independently by the lead Claude Opus 5.5 on 2026-10-20 at 15:30Z, with exact symbolic checks N=1,3,5,7; report draft audited in AV31. This is not a nonexistence theorem for general angular functions.

## Statement

Let rho be a real C^(2,alpha)_loc function on the full plane, 0<alpha<1, even in x and odd in y. Assume

    |rho(X)| <= C(1+|X|)^gamma,
    |grad rho(X)| <= C(1+|X|)^(gamma-1),  gamma<1.

Suppose rho has finite physical angular support: for some odd N>=1,

    rho(r,theta)=sum_(n odd, 1<=n<=N) h_n(r) sin(n theta), r>0.

Let U be its canonical full-plane IPM velocity. If, for a constant c_l,

    (c_l X+U).grad rho=rho

holds throughout the plane, then rho is zero. The conclusion holds without imposing center normalization or c_l>1; in particular it excludes a normalized IPM profile in this finite-angular class. It does not exclude an infinite angular expansion or limits of finite approximations.

## Top angular mode of the canonical inverse

Suppose rho is nonzero and take N to be its highest nonzero angular index. Put h=h_N. Angular projection of the density and its radial derivative gives h=O(r^gamma), h'=O(r^(gamma-1)) at infinity; h is bounded near zero and C^2 for r>0.

For a sine mode h(r)sin Ntheta, direct differentiation gives

    partial_x(h sin Ntheta)
      = (h'+N h/r) sin((N-1)theta)/2
        +(h'-N h/r) sin((N+1)theta)/2.

The zero sine mode, when N=1, contributes nothing. Thus the highest streamfunction mode is T(r)sin((N+1)theta), generated only by h. Its source is f=(h'-N h/r)/2. The regular radial Green formula is

    T(r) = 1/(2(N+1)) *
       [r^(-N-1) int_0^r f(s)s^(N+2)ds
        +r^(N+1) int_r^infinity f(s)s^(-N)ds].

The infinity integral converges since gamma<N. The origin integral converges by the local regularity of rho; h' is bounded near zero, which also suffices. The formula follows by differentiating twice and checking -(T''+T'/r-(N+1)^2 T/r^2)=f. The canonical velocity selects this solution: a singular harmonic term is excluded at zero and a growing harmonic term is excluded by sublinear velocity growth. Here that growth follows directly from the kernel. Put eta=max(gamma,0)<1 and R=|X|>=2. In |Y-X|<R/2, subtract rho(X) in the principal value and use |grad rho|<=C R^(eta-1); integration gives C R^eta. In |Y|<=2R outside that ball, the kernel is O(R^-2), and the density integral is O(R^(eta+2)). In |Y|>2R pair Y and -Y using rho odd under central inversion; the kernel difference is O(R/|Y|^3), so its density integral is again O(R^eta). The local contact term has the same bound. Thus |U(X)|<=C R^eta=o(R), excluding every nonconstant regular harmonic contribution to the velocity for streamfunction index N+1>=2.

Integration by parts gives the particularly simple identity

    T(r)=-(1/2)r^(-N-1) int_0^r h(s)s^(N+1)ds,             (1)
    T'=-(N+1)T/r-h/2.                                    (2)

At infinity the boundary term h(s)s^(-N) vanishes. At zero h(s)s^(N+2) vanishes. The two endpoint terms at s=r cancel between the two Green integrals. No uncontrolled integral over infinity remains in (1). These operations require only the displayed regularity and growth.

## Highest transport harmonic

In polar coordinates U_r=-psi_theta/r and U_theta=psi_r. Only the product of the top density mode N and the top streamfunction mode N+1 can produce sin((2N+1)theta) in U.grad rho. The dilation term has no such harmonic. Product-to-sum formulas therefore yield

    [sin((2N+1)theta)] ((c_l X+U).grad rho-rho)
       = (N h T'-(N+1)T h')/(2r).                        (3)

For an exact profile this coefficient vanishes. The extraction is legitimate for the finite sums at every r>0. Lower modes cannot contribute to the maximum sum index 2N+1.

## Classification on a nonzero component

Take any connected component I of {r>0:h(r)!=0}. The sign of h is constant on I. Since N is odd, v=h^(1/N) denotes its smooth real Nth root there. Equation (3) gives

    (T/v^(N+1))'=0.

Thus T=C_I v^(N+1) on I. The constant C_I is nonzero: if T were zero there, (2) would force h=0. Substituting into (2) and dividing by the nonzero h=v^N gives

    v'+v/r = -1/(2(N+1)C_I).

Consequently there are constants a_I!=0 and b_I such that

    v(r)=a_I r+b_I/r,
    h(r)=(a_I r+b_I/r)^N.                               (4)

This classification uses neither an assumed nonzero Taylor coefficient at zero nor analyticity. It also covers top coefficients flat at zero or vanishing on entire radial intervals.

## Contradiction with the component endpoints

Write I=(r_-,r_+) with 0<=r_-<r_+<=infinity. At every finite positive endpoint, continuity of h makes h zero there. If both endpoints were finite and positive, (4) would require the affine polynomial a_I r^2+b_I to have two distinct positive roots. This is impossible because a_I!=0.

If r_-=0, boundedness of h at zero forces b_I=0. Then (4) never vanishes at a positive radius, so r_+=infinity. But |h(r)|=|a_I|^N r^N violates the sublinear bound gamma<1<=N.

If r_->0, the first paragraph shows that r_+=infinity. Again (4) grows as |a_I|^N r^N and violates the same bound. These alternatives exhaust every nonempty component. Hence h is identically zero, contradicting the choice of N. The density must therefore be zero.

## Exact checks and relation to the other results

The accompanying symbolic code verifies, for N=1,3,5,7,9, the angular differentiation formula, coefficient (3), the radial Poisson identity following from (2), and the classification (4). For h=r^N(1+b_1 r^2+...), (1) gives

    T=-r^(N+1)/(4(N+1))-b_1 r^(N+3)/(4(N+2))+...,

and (3) has first nonzero coefficient b_1 r^(2N+1)/(2(N+2)). At N=3 and density amplitude h=r^3 b/4 this is b_1 r^7/160, agreeing with the separate radial-factor calculation.

The local radial-factor theorem in ../radial-factor/PROOF.md is stronger in a different respect: it rules out transport already near the center, assuming a globally radial factor and the canonical inverse. The present theorem permits arbitrary finite angular support but uses transport on the entire plane. Its component proof avoids an assumption of global smoothness and so applies to the default C^(2,alpha) class.

The finite warped cosine basis is generally not a finite physical angular expansion when beta is nonzero. Its exact smooth-center subclass is radial by the separate intersection argument, so it is covered by the radial result. Neither theorem forbids a numerical residual tending to zero as angular resolution increases. The actual X3 representation, involving an exponential of angular functions, is not a finite physical Fourier series. No general YES_inf or NO_inf endpoint follows.
