# Quantitative angular variation under a one-sided affine defect

Date: 2026-10-20. Independent verifier reconstruction of QLE1(a)-(e). Status: analytic CONFIRMED; separate exact and high precision supporting checks are recorded in verification. The results below are conditional exclusions and examples of nonprofiles. They do not exclude the full primary admissible class.

## Statement, hypotheses and dependencies

Write ell>1, D=ell-1, A=2ell-1, r=|(x,y)|. A primary profile is a smooth real density rho, even in x and odd in y, with nonzero a=rho_y(0), solving

    W.grad rho=rho, W=ell X+U, U=(-psi_y,psi_x), -Delta psi=rho_x,

on the whole plane. The stream is odd in both coordinates. The velocity is canonical, U=o(r). For some 0<gamma<1, assume

    |rho|+(1+r)|grad rho| <= C(1+r)^gamma.

The origin equation gives c=psi_xy(0)=-D. Define the smooth, even quotient q=rho/(a y), extended to y=0 by integrating rho_y on vertical segments. Let H=y-rho/a. Our extra sign hypothesis is q<=1 everywhere, equivalently yH>=0. It is not known for the unrestricted class.

Results70 and74, ../one_sided_flat_exclusion/PROOF.md and ../one_sided_jet_thresholds/PROOF.md, prove the following facts used here: H is not flat under this extra sign; if its first nonlinear degree is odd n>=3, its leading polynomial H_n satisfies the recurrence given below; for 1<ell<=5 one has a>=2A, with equality only at n=3 and H_3=c_3 x^2y, c_3>0. More generally, a>=(n-1)A whenever A<=n, and for all first degrees if ell<=3. These are proved without a global strain cap. No theorem below assumes analyticity.

Set w(theta)=cos(theta)sin(theta)^3 on [0,pi/2] and define

    P = int_0^infinity int_0^(pi/2) w (q_theta)_+ dtheta dr/r,
    N = int_0^infinity int_0^(pi/2) w (-q_theta)_+ dtheta dr/r,
    C(q) = int_0^infinity osc_[0,pi/2] q(r,.) dr/r.

The use of C here avoids confusing the angular contrast with A=2ell-1. The conclusions are:

1. P,N,C(q) are finite, and D/a=1/4+(4/pi)(P-N).
2. If q<=1 and 1<ell<=5, then N>pi/(16A) and C(q)>pi/(3 sqrt(3) A).
3. If q<=1 and the first-degree threshold a>=(n-1)A holds, then N>pi*((n-3)A+2)/(16*(n-1)*A).
4. Independently of the extra sign, a>0 and N<pi/16 imply a<=4D/(1-16N/pi). This inequality is sharp among smooth canonical nonprofiles with the correct center relation.

Sections below also verify the two proposed families and the cubic and quintic counterjets. All inequalities and functionals are invariant under the genuine spatial dilation q_lambda(X)=q(X/lambda), since dr/r is invariant.

## Convergence and the canonical angular identity

Near zero smoothness and parity give q=1+O(r^2), q_theta=O(r^2), uniformly in angle. At infinity q=O(r^(gamma-1)) uniformly. To see the latter statement near the horizontal axis, when |y|<r/2 one has |x|>sqrt(3)r/2. Integration of rho_y(x,s) for 0<=|s|<=|y| gives |rho(x,y)|<=C|y|r^(gamma-1). Away from this strip division of the growth bound by |a y| suffices. Thus C(q) is finite at both endpoints.

Direct differentiation gives

    q_theta=(-sin(theta)rho_x+cos(theta)rho_y)/(a sin(theta))
            -rho cos(theta)/(a r sin(theta)^2).

Multiplication by w bounds the absolute value by C(|grad rho|+|rho|/r), uniformly in angle for r>=1. This is O(r^(gamma-1)), so P and N are finite. The apparent axis singularity is removable for each finite r. Similar multiplication by cos(theta)^2 sin(theta)^2 controls q_r and justifies the radial integration below.

The canonical center strain has the absolutely convergent source-derivative form

    c = (1/pi) int_R2 x y r^(-4) rho_x dX.

Indeed rho_x=O(r^2) at zero and O(r^(gamma-1)) at infinity, so both endpoint radial integrals converge. The identity follows by differentiating the cross derivative of the logarithmic Green potential for -Delta psi=rho_x. A radial cutoff of rho_x and central pairing of the far velocity kernel give the canonical sublinear velocity, as proved in the canonical inverse results. No unrenormalized density integral is being declared absolutely integrable: the equivalent formula with rho itself requires angular cancellation at zero. These arguments also apply without transport when c is prescribed separately.

Substituting rho=a y q, using the four quadrants, and changing to polar coordinates yields

    c/a=(4/pi) int_0^(pi/2) int_0^infinity
         [cos(theta)^2 sin(theta)^2 q_r - w q_theta/r] dr dtheta.

The radial boundary values are q(0,theta)=1 and q(infinity,theta)=0. As the angular integral of cos(theta)^2 sin(theta)^2 is pi/16, this proves c/a=-1/4-(4/pi)(P-N). The primary center relation c=-D proves conclusion1.

Equivalently let k=-w'=sin(theta)^2(4sin(theta)^2-3). Integration by parts in theta gives int w q_theta=int kq, with no endpoint term since w vanishes at both axes. The k integral must be taken before the radial integral at zero because its mean vanishes.

## Strictness at the slope threshold

For q<=1 and ell<=5, the imported theorem gives a>=2A>0. Therefore

    N-P=(pi/4)(1/4-D/a) >= pi/(16A),

using A-2D=1. If a>2A this is already strict. If a=2A, the same theorem gives H_3=c_3 x^2y with c_3>0 and

    q=1-c_3 r^2 cos(theta)^2+O(r^4),
    q_theta=2c_3 r^2 sin(theta)cos(theta)+O(r^4).

The differentiated remainder is uniform on the full angular interval, since q is smooth in Cartesian coordinates and its Taylor remainder has derivative O(r^3). Fix a closed sector, for example theta in [pi/6,pi/3]. On this sector sin(theta)cos(theta) and w have positive minima. There is delta>0 such that q_theta>=c_3 r^2 min_sector(sin theta cos theta)>0 for every 0<r<delta. Its weighted integral against dr/r is strictly positive and finite. Thus P>0, and N>pi/(16A) also at equality.

For completeness, the leading recurrence is obtained by writing H_n=sum_(j=0)^K c_j x^(2j)y^(n-2j), n=2K+1, and e_j=n-1+2j(A-1):

    (n-2j)(n-2j-1)e_j c_j
      +(2j+2)(2j+1)(e_(j+1)-a)c_(j+1)=0, 0<=j<K.

If a=(n-1)A=e_K, backward substitution first gives c_(K-1)=0, then every lower coefficient zero. Nontriviality and yH_n>=0 force c_K>0. Hence H_n=c_K x^(n-1)y, and

    q_theta=(n-1)c_K r^(n-1) cos(theta)^(n-2)sin(theta)+O(r^(n+1)).

The same sector argument proves P>0. Replacing 2A by (n-1)A in the preceding algebra gives conclusion3, including its strict equality boundary. No extra resonant case has been omitted.

## Contrast estimate and the conditional upper bound

The kernel k is negative on (0,pi/3), positive on (pi/3,pi/2), and has zero integral. Its positive and negative masses equal max w=3sqrt(3)/16, denoted M. For any continuous nonconstant f on the angular interval,

    |int k f| < M osc f.

The weak inequality follows by subtracting min f and bounding separately on the two sign intervals. Equality would force f to equal one extremum throughout one open sign interval and the other extremum throughout the adjacent interval. Continuity at pi/3 would then force the two extrema to coincide. This proves strictness.

For an exact profile satisfying the current hypotheses q cannot be radial: the center identity would give a=4D<2A. Thus q is nonconstant in angle at some radius and, by continuity, on an interval of radii. Integration of the strict angular estimate on this interval and the weak estimate elsewhere gives

    |P-N| < M C(q).

Together with N-P>=pi/(16A), this yields C(q)>pi/(3sqrt(3)A). It is not legitimate to bound N itself by M times oscillation, since repeated angular oscillations can have arbitrarily large negative variation. Our proof only bounds the signed integral.

Finally, for a>0 the center identity gives D/a>=1/4-4N/pi. If N<pi/16 the right side is positive. Rearranging proves conclusion4.

## A small negative-variation family with correct canonical center

Fix ell>1 and set eps=1/(2A). Define

    q_eps=exp(-r^2)*(1-eps*y^2/(1+r^2)).

Since 0<eps<1/2 and 0<=y^2/(1+r^2)<1, it is smooth, even in both variables, and 0<q_eps<=1. At fixed r,

    (q_eps)_theta=-2eps exp(-r^2) r^2 sin(theta)cos(theta)/(1+r^2)<0

in the open quadrant. Hence P=0 and

    N=(eps*pi/16)*int_0^infinity r exp(-r^2)/(1+r^2) dr
      <eps*pi/32=pi/(64A),

where the angular integral of cos(theta)^2 sin(theta)^4 is pi/32. Define s_eps=1/4-4N/pi and a_eps=D/s_eps. The bound above implies s_eps>1/4-1/(16A)>D/(2A), hence 0<a_eps<2A. The smooth rapidly decreasing density rho_eps=a_eps y q_eps has canonical c=-D by the density-only strain identity. Its velocity is sublinear and its parities are correct.

It is not a profile. Its first affine defect is H_3=x^2y+(1+eps)y^3. For any exact primary cubic the recurrence requires 6(1+eps)=a_eps-2A; the left side is positive while the right side is negative. This is a concrete violation of transport compatibility, despite all the stated shape and canonical normalization conditions.

## Gaussian sharpness and a global gradient check

Let beta>=1, B=sqrt(beta), and set

    a_beta=D(1+B)^2, rho_beta=a_beta y exp(-x^2-beta*y^2).

The canonical source-derivative integral in polar coordinates gives

    c=-4a_beta/pi * int_0^(pi/2)
         cos(theta)^2 sin(theta)^2/(cos(theta)^2+B^2 sin(theta)^2) dtheta
      =-a_beta/(1+B)^2=-D.

For a direct integral evaluation substitute t=tan(theta). The resulting integrand t^2/[(1+t^2)^2(1+B^2 t^2)] equals

    1/[(B^2-1)^2(1+t^2)]
    +1/[(B^2-1)(1+t^2)^2]
    -B^2/[(B^2-1)^2(1+B^2 t^2)]

when B!=1; integration of the three elementary terms gives pi/[4(1+B)^2]. At B=1 continuity gives pi/16. This verifies the canonical normalization without inserting a harmonic term.

The quotient is positive and at most1. Its angular derivative is -2(beta-1)r^2 sin(theta)cos(theta)q, so P=0. Consequently

    N=(pi/4)*(1/4-1/(1+B)^2)<pi/16,

and a_beta exactly saturates conclusion4. Thus no stronger bound can follow from the canonical identity and the same variation data alone.

To verify the global gradient bound put s=beta*y^2, t=x^2+s. Since beta>=1,

    |grad rho_beta|^2/a_beta^2
      =exp(-2t)*[(1-2s)^2+4x^2*s/beta]
      <=exp(-2t)*[1+4s(t-1)].

When 0<=t<=1 this is at most1. For t>=1, s<=t bounds it by exp(-2t)(2t-1)^2. On [1,infinity) its maximum occurs at t=3/2 and equals4exp(-3)<1. The bound holds everywhere, with equality at the origin. Nevertheless at x=0,y=1/sqrt(2beta) the density is positive and its entire gradient is zero, so W.grad rho-rho=-rho!=0 for every smooth velocity. These are nonprofiles even though a_beta is unbounded as beta tends to infinity.

## Independent checks of the two finite counterjets

For ell=2, A=3, a=13, set

    H_3=x^2y+(7/6)y^3,
    V_3=6x^2y+(7/3)y^3,
    phi_4=2x^3y+(7/3)xy^3.

Differentiation gives V_3=(3x*d_x+y*d_y-1)H_3=(phi_4)_x and Delta phi_4=13(H_3)_x. Thus the leading coupled equations hold. The quotient 1-H_3/y has q_theta=-(1/3)r^2 sin(theta)cos(theta), while H_3/y>0 off the origin. This refutes the proposed local implication from one-sided defect and the leading coupled equations to nonnegative angular derivative. It does not give an exact transport solution.

For the exact cubic polynomial density rho=13(y-H_3), the more explicit gradient bound requested by the lead at23:12Z is also valid. Namely

    (H_3)_y=x^2+(7/2)y^2 >= r^2,
    |grad H_3|^2=x^4+11x^2y^2+(49/4)y^4,
    (49/4)r^4-|grad H_3|^2=(45/4)x^4+(27/2)x^2y^2 >= 0.

It follows that |grad rho|^2/169 <= 1-2r^2+(49/4)r^4<1 whenever 0<r<2sqrt(2)/7. This explicit radius applies to the polynomial just specified. For a smooth density with the same cubic jet and unspecified higher terms, only some sufficiently small radius follows without bounds on those terms. This remains a local polynomial example, not a global canonical profile.

For ell=19, D=18, A=37, a=2, set

    H_5=x^4y-(73/19)x^2y^3+(2701/380)y^5,
    V_5=148x^4y-292x^2y^3+(2701/95)y^5,
    phi_6=(148/5)x^5y-(292/3)x^3y^3+(2701/95)xy^5.

Then V_5=(37x*d_x+y*d_y-1)H_5=(phi_6)_x and Delta phi_6=2(H_5)_x. The derivative

    (H_5)_y=x^4-(219/19)x^2y^2+(2701/76)y^4

is positive away from zero: as a polynomial in x^2/y^2 its discriminant is -3358/361<0 and its leading coefficient is1; on y=0 it is x^4. Integrating in y proves yH_5>=0. Compactness of the unit circle gives (H_5)_y>=c r^4 for some c>0. Since |grad H_5|^2=O(r^8), the density rho=2(y-H_5) obeys

    |grad rho|^2/4=1-2(H_5)_y+|grad H_5|^2<1

on a sufficiently small punctured ball. But (V_5)_y(t,t)=-(11131/19)t^4<0. For psi=-18xy+phi_6 the symmetric strain therefore has S_22(t,t)<-18, and its operator norm exceeds D arbitrarily close to zero.

For either polynomial pair rho=a(y-H_n), psi=-Dxy+phi_(n+1), Poisson is exact, whereas the full transport residual is -a v.grad H_n, v=(-phi_y,phi_x). It has degree2n-1 and is nonzero. The fields also fail the growth and canonical sublinearity conditions. The second example refutes a local deduction of the strain cap from a positive slope, a local gradient maximum, the one-sided defect and leading coupled equations. It does not refute such an implication for global admissible exact profiles.

## Verification scope

The exact computations independently verify the recurrence boundary, angular constants, partial fraction identity, cubic and quintic equations, and nonzero full polynomial residuals. High precision quadrature checks the Gaussian center and the small-variation integral. They support the preceding proof and do not certify any numerical candidate. No producer code or lead checking code was used. The lead's actual model is Claude Opus5.5; its QLE1 requests were treated as claims to audit, not as evidence.
