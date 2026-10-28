# Domain audit of the first S2 specification

This note audits the theory author's CONVENTIONS.md version 1, observed on 2026-10-28. Item labels below refer to that version. Confirmed statements are restricted to the exact hypotheses stated here. A missing hypothesis is not evidence of a nonexistent stationary profile.

## 1. A continuous center factor does not give a pointwise image jet

Let ell>2, A=2ell-1, D=4ell-1 and T_0=-A x partial_x+D y partial_y-1. Suppose the background is the exact modal trial of proof 04, or any background satisfying

    rho_bar=x^2y+R, |D^j R|=O(r^(5-j)), j=0,1,2,
    V=diag(-A,D)X+E, |E|=O(r^3), |DE|=O(r^2).

Let chi be a smooth radial compact cutoff equal to one near zero. Define

    h(X)=chi(r) x^2 y r^(1/10) sin(r^(-2/5)), r>0,
    h(0)=0.                                                        (1)

Then h has the required parity, a continuous even-even factor with J(h)=0, and h=o(r^3). It belongs to C^(2,1/10)(R^2). Its canonical velocity belongs locally to C^(2,1/10). Both h and its full normalized image Lh belong to the diagnostic X of proof 03. Nevertheless Lh/r^3 is unbounded on a fixed non-axis ray. In particular a pointwise cubic coefficient of Lh does not exist.

To prove the regularity, write the oscillatory part as r^(31/10) times a smooth angular factor. A derivative can cost one power from ordinary differentiation and an additional 2/5 power from the phase. Therefore

    |D^j h|<=C r^(31/10-7j/5), j=0,1,2,3, r>0,                    (2)

with smooth cutoff terms harmless away from zero. In particular the Hessian is O(r^(3/10)) and tends to zero at the origin, while the third derivatives are O(r^(-11/10)). These bounds and the corresponding first derivative limits prove C^2 regularity by differentiation along segments.

Here is a direct Holder check for the Hessian. For points with comparable radius r and separation d<r/2, its difference is bounded both by C r^(3/10) and by C r^(-11/10)d. If d<=r^(7/5), the second bound is at most C d^(1/10), since r^(-11/10)d^(9/10)<=r^(4/25). If d>=r^(7/5), the first is at most C d^(3/14), hence at most C d^(1/10) for d<=1. When radii are not comparable, d controls the larger radius and the same conclusion follows from (2). Thus the Hessian is Holder with exponent 1/10. Compact support and smoothness elsewhere give the global claim.

The order-zero velocity multiplier preserves local C^(2,1/10) for compact C^(2,1/10) input, for instance by applying the ordinary Holder singular-integral estimate to each second derivative and treating the remote kernel smoothly. Parity eliminates its constant and quadratic Taylor terms. Hence

    U[h]=c[h](-x,y)+O(r^(21/10)),
    DU[h]=diag(-c[h],c[h])+O(r^(11/10)).                           (3)

The normalized linear velocity c[h](-2x/3,4y/3) annihilates x^2y exactly. Equations (2)-(3) and the background bounds imply

    Lh=T_0h+O(r^(41/10)),                                        (4)

and the gradient of the remainder is O(r^(31/10)). The local transport error E.grad h is O(r^(47/10)); its derivative is O(r^(33/10)). The coupling with R is still smaller. Thus none of the remainders can remove the term below.

On the cutoff plateau, T_0(x^2y)=0 gives

    T_0h=x^2 y (-A cos^2(theta)+D sin^2(theta))
             [(1/10)r^(1/10)sin(r^(-2/5))
                -(2/5)r^(-3/10)cos(r^(-2/5))].                   (5)

At theta=pi/4 the angular transport coefficient is ell>0. Taking r_n=(2pi n)^(-5/2) makes the sine zero and cosine one. Equations (4)-(5) show that Lh/r^3 tends to minus infinity along this sequence. A sequence with cosine minus one gives the opposite sign.

Finally h is in X because its value is O(r^(31/10)) and r|grad h| is O(r^(27/10)). The full image has value O(r^(27/10)) and r|grad Lh|=O(r^(23/10)). The most singular radial squared-norm integrand is r^(46/10)r^(-6)r=r^(-2/5), which is integrable. At infinity the compact perturbation velocity is O(r^-2) with derivative O(r^-3), while X.grad rho_bar has order r^k. Both its nonlocal product and the rank-one term lie in X by the powers already checked in topics 03 and 05. Thus this is an actual graph-domain counterexample, not merely a formal singular function.

Verdict on S4.6: REFUTED as a pointwise image-jet statement for the listed class h=Jx^2y+o(r^3), U[h] locally C^(1,alpha). The counterexample has stronger regularity than required. A distributional cubic blow-up still vanishes; its meaning is different.

A sufficient repair is to impose |D^j(h-Jx^2y)|=o(r^(3-j)) for j=0,1 together with compatible first-order velocity control, or to define the range coefficient solely through a specified distributional blow-up. Every Banach range space must say which interpretation it uses.

Verdict on the final sentence of S4.5: the formula involving derivatives of a_bar is algebraically correct where those derivatives exist. The conclusion that its factor is o(1) needs x partial_x a_bar and y partial_y a_bar to tend to zero. Continuity of a_bar alone does not imply this. The exact modal background has the stronger derivative bounds and therefore satisfies the conclusion. The example a_bar=1+chi(r)r^(1/10)sin(r^(-2/5)) shows why the generic continuity inference fails.

## 2. Axis transport and its regularity limit

Suppose rho is C^1 near the entire y-axis, even in x and odd in y, stationary, and rho=O(r^3) near zero. Write v(y)=V_2(0,y). Suppose v(y)=D y+O(y^3), D>1/3, and v(y) never vanishes for y!=0. Then rho(0,y)=0 for every y.

Indeed parity gives V_1(0,y)=0, so g(y)=rho(0,y) satisfies v g'=g. On each half-axis, a nonzero solution is C exp(integral dy/v). Near zero, 1/v=1/(Dy)+O(y), whence its magnitude is asymptotic to a nonzero constant times |y|^(1/D). Since 1/D<3, this contradicts g=O(|y|^3). The zero solution extends over each entire half-axis by uniqueness of the scalar ODE where v is nonzero. Continuity supplies its value at zero.

Verdict on the vanishing part of S1.4: CONFIRMED with the stated D>1/3, which the S2 parameters satisfy.

The further expansion rho=x^2 G_2(y)+O(x^4) does not follow from C^1 regularity, parity and axis vanishing. Those three regularity properties alone hold for |x|^(3/2)y^3, which has no such expansion at a fixed nonzero y. This example is not asserted stationary. Thus the extra PDE regularity claim remains OPEN unless an independent regularity theorem is supplied. A direct sufficient hypothesis is C^4 in x with locally bounded fourth derivative. Taylor's theorem and parity then give G_2(y)=rho_xx(0,y)/2 and the O(x^4) remainder. C^2 only gives x^2 G_2(y)+o(x^2).

## 3. What the first non-smooth saddle mode means

The homogeneous solutions of T_0 are |x|^p sign(y)|y|^q with -Ap+Dq=1. If q is restricted to positive odd integers, the q=1 solution is x^2y and the next is |x|^(6+2/A)y^3. This proves the stated first fractional x-power within that ansatz.

It is not the first non-smooth solution in the full continuous-factor or C^(2,alpha) class. Take

    q=5/2, p=5+3/(2A).

Then -Ap+Dq=1, p>5, and

    H=|x|^p sign(y)|y|^(5/2)
       =x^2 y |x|^(p-2)|y|^(3/2)

has a continuous even-even factor and belongs locally to C^(2,alpha) for alpha<=1/2. Its degree is 15/2+3/(2A), smaller than 9+2/A, the degree of the q=3 mode. It solves the frozen equation on every quadrant and across the axes in the distributional sense because it is C^1 there. There are further noninteger families.

Verdict on the unqualified first-mode phrase in S6.2: REFUTED for the full continuous-factor class. CONFIRMED after explicitly restricting the y exponent to positive odd integers. The formula for p_3 itself is correct for X3's chosen ansatz.

The integer resonance arithmetic is separate. With k=n/2^53, n=1615536043799051, A=(2^54-n)/n=M/n and gcd(M,n)=1, the equation for integer i,j is i=2j+(j-1)n/M. Hence M divides j-1. For the required odd j and even i, the next possible j after one is actually 1+2M, since M,n are odd. The weaker exclusion j<1+M in S6.2 is valid.

## 4. The full strain kernel, including a nonzero first jet

Assume a smooth compact parity-compatible h, and denote its sine density coefficients by F_l(r). The radial Green formula from proof 01 gives

    c[h]=(1/4)integral_0^infinity
        [F_1'/r-F_1/r^2+F_3'/r+3F_3/r^2]dr.

At the origin F_1/r tends to h_y(0), whereas F_3/r tends to zero. Integrating the first pair as (F_1/r)' and the F_3 derivative by parts proves

    c[h]=integral_0^infinity F_3/r^2 dr-(1/4)h_y(0)
        =(1/pi)PV integral h sin(3theta)/r^3 dX-(1/4)h_y(0).       (6)

The radial PV is meant here. The same identity extends whenever the corresponding endpoint bounds justify the integration by parts. For h=y exp(-r^2), F_3=0 and h_y(0)=1, so c=-1/4. Thus the local term cannot be omitted on a space admitting a nonzero y-jet.

For the class in S3.2, |h|<=C r^(1+epsilon) near zero, the kernel integral is absolutely convergent there, since its radial absolute bound is C r^(epsilon-1). At infinity the assumed beta<1 gives C r^(beta-2), also integrable. If h is locally Holder with a fixed positive exponent on a neighborhood of zero, the canonical velocity is differentiable at zero and (6) has no local term. One way to see the differentiability is to split the velocity integral at radii 2|X| and a fixed small radius. Taylor expansion on the outer part leaves an o(|X|) error by the two convergent kernel moments. On the inner part, the local Holder estimate and the amplitude M=O(|X|^(1+epsilon)) bound the singular integral by C M(1+|log |X||): split its singular ball at radius (M/H)^(1/alpha), where H is the Holder constant. This is o(|X|). The explicit local multiplier term is O(M). Hence the derivative is the absolutely convergent differentiated kernel integral. Its parity and zero divergence give diag(-c,c).

Verdict on S2.2 and S3.2, including its warning: CONFIRMED with the explicit local Holder hypothesis and the stated endpoint bounds. S2.3's size bound alone is not a pointwise singular-integral domain; local regularity or an almost-everywhere formulation must be added. Sublinear growth of U itself also requires more control than the size of h alone and must be checked in any space that uses it.

## 5. Source identities and the rank-one coefficient

Let an exact stationary C^2 background have a source at P=(x_P,0), with g=rho_y(P)!=0. Let w(x)=V_1(x,0), mu(x)=partial_y V_2(x,0), g(x)=rho_y(x,0). Differentiating stationarity gives

    w g'+(mu-1)g=0, w'+mu=2ell.

At P, w=0, so mu(P)=1 and w'(P)=2ell-1. For an approximate background with residual epsilon, the first identity instead reads

    w g'+(mu-1)g=epsilon_y(x,0).                              (7)

Thus a numerical root of w does not by itself certify mu=1.

If the background is C^3 near P, odd-y symmetry and Taylor expansion give

    X.grad rho=(g+x_P rho_xy(P))y+O(|(s,y)|^2), s=x-x_P.       (8)

With more regularity the remainder may be refined to O(|s y|+|y|^3). The spatial constant of this coefficient is zero. Freezing grad rho alone at (0,g) while retaining X gives the coarser coefficient g y. Equations (7)-(8) explain exactly which terms are lost in that operation.

Verdict on S6.3's exact-solution eigenvalue identities: CONFIRMED under the stated regularity and nonzero g. Its displayed G expansion is CONFIRMED for a sufficiently smooth background such as the exact modal trial. The numerical X3/trial values remain OPEN until independently certified. The constant-coefficient operator with only -g M is a separate principal frozen model; its inverse is not yet an inverse of the full localized expression.

## 6. Local weighted energy

On a quadrant domain Omega bounded away from the coordinate axes, let h be smooth and real, 1<p<infinity, and w=|x|^(-a p)|y|^(-b p). Direct integration by parts gives

    integral_Omega (T_0h)|h|^(p-2)h w
       =-kappa integral_Omega |h|^p w
          +(1/p)integral_boundary |h|^p w (-Ax,Dy).n,
    kappa=1+(D-A)/p+A a-D b.                                  (9)

Indeed div(w(-Ax,Dy))/w=D-A+p(Aa-Db). No boundary term may be discarded on a singular axis without proving the trace limit. For radial w=r^(-beta p), the corresponding local coefficient is

    1+(D-A)/p-beta(-A cos^2(theta)+D sin^2(theta)).               (10)

It is negative at the y-axis when beta>(D-A+p)/(pD), and positive at the x-axis for positive beta. The formula confirms the sign obstruction for sufficiently strong isotropic weights. Neither (9) nor (10) bounds the nonlocal term or gives a global inverse.

Verdict on S7.3: CONFIRMED as this integration-by-parts identity with boundary flux retained and integrability/trace hypotheses made explicit.

## Dependencies and remaining scope

Topics 01, 03, 04 and 05 supply the canonical sign, modal background bounds and weighted norms. The new ingredients are the explicit oscillatory counterexample, elementary Taylor and Holder estimates, the axis ODE and integration by parts. Local Holder boundedness of the classical order-zero Riesz multipliers is used with compact C^(2,alpha) input, where its standard hypotheses hold.

The claimed strict far-field L^2 threshold in S0.3 has not been certified here: the upper decay bound gives sufficiency, while the claimed necessity requires a nonzero leading residual angular coefficient. The latest accepted status of the case1 follow-up and every raw-X3 number remain subject to separate input and numerical checks. No theorem about nonlinear existence follows from these local checks.
