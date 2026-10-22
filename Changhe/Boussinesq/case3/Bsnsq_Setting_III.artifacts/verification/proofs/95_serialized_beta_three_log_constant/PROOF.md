# Stable logarithmic constant of a serialized beta-three source

Written 2026-10-21T00:31:02.624654+00:00. Full informal proof precedes numerical checks. This is a source-inverse statement. It imposes neither transport PDE and does not construct or exclude a B2 profile.

## 1. Exact statement and notation

Let L>0, r=|X|, theta=arg X, z=(1+r²/L²)^(-1/6), t=1-z. Let C_n(t), 0<=n<K, be real piecewise polynomials on a fixed finite partition of[0,1], globally C³, and polynomial on a neighborhood of1. Put rho_n=1 for n even and rho_n=r/sqrt(L²+r²) for n odd, and set

    Omega(r,theta)=r cos(theta) z^4 sum_n C_n(t) T_n(-sin(theta)) rho_n(r),
    S(t)=C_0(t)-C_2(t)/2,                              (1)

where missing modes are zero. T_n is the usual Chebyshev polynomial. Define Omega(0)=0. The source is continuous at0, locally bounded, x-odd, and smooth in angle away from0. No unwarranted full Cartesian smoothness at0 is assumed for arbitrary angular coefficients.

Use the prompt kernel K(Z)=(Z2,-Z1)/(2pi|Z|²) and the canonical relative inverse

    V(X)=integral [K(X-Y)+K(Y)] Omega(Y)dY,
    -Delta Psi=Omega, V=(-Psi_y,Psi_x).                 (2)

In particular curl V=-Omega. At infinity the relative kernel is O(|Y|^-2), and Omega=O(|Y|^-1/3), so the area integral is convergent; its finite-point singularities are locally integrable. The integral converges absolutely. Let omega0,omega1,omega2 be the first three homogeneous source tails, of degrees -1/3,-2/3,-1. Set

    B0=L^(4/3)S(1), B1=-L^(5/3)S'(1),
    alpha=L² S''(1)/2.                                (3)

These are their respective first-cosine coefficients. Let u0,u1 be the homogeneous canonical inverses of omega0,omega1. Write omega2=r^-1 A2(theta), let g solve

    -(g''+g)=A2-alpha cos(theta),
    integral g cos=integral g sin=0,

and set

    B(theta)=-g' e_r+g e_theta
                +(alpha/2)(cos(theta)sin(theta),-cos(theta)^2).

There is a unique real constant C such that, uniformly in angle,

    V(r e)=u0+u1-(alpha/2)log(r)e2+B(theta)+C e2+O(r^-1/3). (4)

Its stable formula is

    C=(3L²/4)[S(0)-S'(0)-integral_0^1 log(1-t) S'''(t)dt]
                       +alpha[(log L)/2-2].           (5)

The integral is ordinary and absolutely convergent. Formula(5) fixes the logarithm as log r; replacing its argument without transforming C would change the normalization.

## 2. The first angular mode and canonical inverse

The exact first-cosine coefficient of(1) is

    q(r)=(1/pi) integral Omega(r,theta)cos(theta)dtheta
         =r z^4 S(1-z).                               (6)

To see this, put phi=theta+pi/2. Then -sin(theta)=cos(phi), cos²(theta)=sin²(phi), and T_n(-sin(theta))=cos(n phi). Orthogonality against sin²(phi) gives1 for n=0, -1/2 for n=2 and0 otherwise. In particular the odd-n factor rho_n has no effect on q. The Taylor expansion at z=0 gives(3), since r z^(4+j)=L^(4/3+j/3)r^(-(1+j)/3)(1+O(r^-2)). All rho_n equal1+O(r^-2) at infinity, so their corrections occur later than the displayed three source tails. The next source remainder is O(r^-4/3), uniformly in angle and with the finite differentiated bounds needed below.

For a first-mode source q(r)cos(theta), the centered stream coefficient is

    p(r)=1/2[r^-1 integral_0^r rho²q(rho)drho
                             -r integral_0^r q(rho)drho].     (7)

It satisfies -(p''+p'/r-p/r²)=q. Its velocity is centered and of sublinear growth. Equation(2), restricted to this mode, has the same distributional div-curl equations, centering and growth; the difference is an entire harmonic field of sublinear growth, hence a constant, and is zero by centering. Local boundedness of q near0 suffices for these statements and the removable origin. Direct angular averaging gives the exact identity

    mean_theta V2(r,theta)=(p/r+p')/2
                           =-1/2 integral_0^r q(rho)drho.     (8)

All other modes have zero vertical angular mean. No free harmonic strain has entered.

For completeness the full expansion(4) follows by subtracting omega0,omega1 and a smooth radial cutoff times r^-1 A2. The remaining source is O(r^-2/3) at0 and O(r^-4/3) at infinity. Its ordinary inverse is absolutely convergent at every point. Splitting the integral at |Y|=r/2 and2r gives an O(r^-1/3) ordinary velocity. The cutoff first mode has stream -(alpha/2)r log r cos(theta) plus a linear term and O(r^-1); the other angular modes have streams r g(theta) plus decaying terms. Oddness eliminates the sin(theta) resonance and the horizontal constant. This proves(4) with a constant fixed by the centered inverse. This argument is the same explicit mode and three-region estimate proved in packet91; here no logarithm occurs in the source remainder. Full Cartesian smoothness of the source at0 is not required. The value estimate uses only local boundedness there.

The mean of -g'e_r+g e_theta is zero because g is orthogonal to the first modes. The mean of the alpha angular term in B is -(alpha/4)e2. Since a source Br^-k cos(theta), k=1/3 or2/3, has mean vertical homogeneous inverse -Br^(1-k)/(2(1-k)), equations(4) and(8) imply

    J=lim_(R->infinity)[integral_0^R q
             -(3/2)B0 R^(2/3)-3B1 R^(1/3)-alpha log R],
    C=alpha/4-J/2.                                    (9)

The alpha/4 term is essential; C is the vector expansion constant, not merely the constant of its angular mean.

## 3. Stable finite-part calculation

Let f(z)=S(1-z), f0=f(0), f1=f'(0), f2=f''(0)/2. Then alpha=L² f2. Because r dr=-3L² z^-7 dz,

    integral_0^R q(r)dr=3L² integral_(z_R)^1 z^-3 f(z)dz.

The ordinary, convergent quantity

    Jf=integral_0^1 z^-3[f(z)-f0-f1 z-f2 z²]dz-f0/2-f1   (10)

exists since f is C³. The explicit first three integrals and

    z_R^-2=(R/L)^(2/3)+o(1),
    z_R^-1=(R/L)^(1/3)+o(1),
    log(1/z_R)=(log R-log L)/3+o(1)

give

    J=3L² Jf-alpha log L.                             (11)

There is no arbitrary finite-part prescription here: J is the explicit limit(9), and(10) is a convergent way to evaluate it.

Two integrations by parts on[epsilon,1] give

    integral_epsilon^1 z^-3 f
      =-f(1)/2+f(epsilon)/(2epsilon²)
       -f'(1)/2+f'(epsilon)/(2epsilon)
       +(1/2)integral_epsilon^1 f''(z)/z dz.

Subtract f0/(2epsilon²)+f1/epsilon-f2 log epsilon. The boundary expansions contribute3f2/2 in addition to -(f(1)+f'(1))/2. For the remaining integral,

    integral_0^1 [f''(z)-2f2]/z dz
       =-integral_0^1 log(z) f'''(z)dz
       =integral_0^1 log(1-t) S'''(t)dt.

The boundary term log(z)[f''(z)-2f2] tends to0 at0 because f is C³, and vanishes at1. Piecewise-polynomial internal boundary terms cancel because f and its first two derivatives are continuous. It follows that

    Jf=-(S(0)-S'(0))/2+3f2/2
                    +(1/2)integral_0^1 log(1-t)S'''(t)dt.    (12)

Combining(9),(11),(12) proves exactly(5). The endpoint integral is absolutely convergent because S''' is bounded and log(1-t) is integrable.

## 4. Exact test family and scope

For S(t)=(1-t)^j and integer j>=0, alpha is zero except j=2, where alpha=L². Direct integration of r z^(4+j) gives

    j=0: C=3L²/4,
    j=1: C=3L²/2,
    j=2: C=L²[1/4+(log L)/2],
    j>=3: C=-3L²/[2(j-2)].                            (13)

For j=2, q=r/(1+r²/L²) and integral_0^R q=(L²/2)log(1+R²/L²), verifying both the logarithmic scale and alpha/4 term independently. For j=0,1 subtract the growing power explicitly; for j>=3 the ordinary q integral converges and equals3L²/(j-2), so(8) yields(13). These sources are positive first modes but have zero center strain; they are not B2 profiles.

Equation(5) can be evaluated on any stored source with basis exponent3 even when its dynamical beta differs. In that case it is still a source-inverse diagnostic, not an assertion about a beta3 solution of the coupled equations. For a hypothetical exact beta3 profile in this finite representation, packet91 additionally requires alpha=0. This conditional necessary constraint neither validates a state when alpha=0 nor rules out the full admissible class. Floating-point evaluation is not interval certification.

## 5. Exact endpoint witnesses in a stored B-spline source

For a degree-p B-spline with knots t_i and control values c_i, its derivative control values are

    d_i=p(c_(i+1)-c_i)/(t_(i+p+1)-t_(i+1)),

with knot vector trimmed at both ends and degree reduced by one. This identity follows by differentiating the Cox-de Boor recursion and collecting neighboring degree-(p-1) basis functions. Applying it twice and taking the last control value evaluates S''(1) exactly at a clamped right endpoint. Applying it to exact binary rational input coefficients and knots, using rational source weights, makes alpha=L²S''(1)/2 an exact rational quantity. This avoids interpreting a rounded floating-point subtraction as an exact source combination. In particular alpha!=0 is an exact necessary-condition failure for a stored beta=b=3 state if it were an exact B2 profile, by packet91. This additional witness is only about the individual finite representation, not the existence of nearby solutions or the full admissible class.

## 6. Dependencies and evidence

First-mode orthogonality, canonical inversion and all finite-part algebra are proved here. The cutoff-mode argument and three-region ordinary bound are also given here, and can be compared to the complete packet91 proof. Formal proof-assistant files are absent; see formal/README.md. Numerical tests and an actual Opus5.5 written audit will be recorded separately when completed. No endpoint is claimed.
