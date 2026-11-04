# Negative pressure at a continuous flat stress zero

## 1. Exact theorem

Let v and P be continuous on a ball B_R(0) in R3 and assume div div(v tensor v+P I)=0 in distributions. Put pi=P-P(0). Suppose |v(x)|<=C|x|^m near0 for constants C<infinity and m>0. If pi<=-beta|v|^2 on a full neighborhood of0 for one beta>1+1/m, then v=0 and P=P(0) on a neighborhood of0.

If v vanishes to infinite value order, every fixed beta>1 suffices. The pressure need not have derivatives or a separately imposed vanishing order. A C1 divergence-free v satisfying -Delta P=tr((Dv)^2) distributionally is a special case, by local mollification. The statement itself does not impose divergence freedom, momentum, self-similarity, helicity, c or omega.

## 2. Radial identity without differentiating a continuous stress

Use normalized unit-sphere averages, and for r>0 put

    E(r)=average |v(rn)|^2,
    A(r)=average (v(rn).n)^2,
    q(r)=average pi(rn), Y=q+A.

These functions are continuous, 0<=A<=E=O(r^(2m)), and Y(0)=0. For a smooth radial test psi supported away from0, the Hessian formula gives

    0=integral [r^2Y psi''+r(E-3A+2Y)psi']dr.

Distributional integration by parts shows that -r^2Y'+r(E-3A) is constant, say K, on(0,R). Therefore

    Y'=(E-3A)/r-K/r^2.

The first right-side term is integrable at0. Any primitive of the second contains K/r, whereas Y is bounded at0. Thus K=0. Using Y(0)=0 gives the exact identity

    Y(r)=integral_0^r (E(t)-3A(t))/t dt,
    rY'(r)=E(r)-3A(r), Y=O(r^(2m)).                    (1)

In particular Y is C1 away from0. No trace of a differentiated distribution, origin flux or unproved pressure estimate is used.

## 3. The finite-order inequality

Set Z=-Y and theta=2/(beta-1)>0. Averaging the pressure inequality gives

    Z=-q-A>=beta E-A>=(beta-1)E>=0.

Equation(1) yields rZ'=3A-E. Since 0<=A<=E,

    theta(beta E-A)-(3A-E)
       =[(3beta-1)/(beta-1)](E-A)>=0.

Thus rZ'<=theta Z and r^(-theta)Z is nonnegative and nonincreasing. The strict hypothesis on beta is exactly theta<2m. By(1), r^(-theta)Z tends to0 at0, so this function must vanish identically. Therefore E=0 on every sufficiently small sphere, and v=0 by continuity. Now A=Y=q=0, while pi<=0 pointwise. Its zero average on each sphere implies pi=0 there by continuity. This proves the full conclusion, including the pressure constant.

For infinite value flatness and fixed beta>1, choose m>1/(beta-1) and apply the finite-order argument. No uniform choice of the flatness constants as m varies is needed.

## 4. Ratio consequences with zero sets retained

Suppose additionally P(0)=0. Define H=|v|^2/2-P and assume H>=0 on a neighborhood and v=0 wherever H=0. If on {H>0},

    |v|^2/H<=Rstar<2/3,

the undivided inequality extends to the whole neighborhood. For Rstar>0 it implies

    P<=-(1/Rstar-1/2)|v|^2,

whose coefficient beta is greater than1. An infinitely value-flat velocity therefore gives a zero germ. Rstar=0 directly gives v=0; the distributional identity then makes P harmonic, and its nonpositive sign and P(0)=0 imply zero. Equivalently, the mean identity and sign already give zero without invoking harmonic regularity.

For a finite order m, the sufficient strict ratio bound is Rstar<2m/(3m+2), exactly equivalent to beta>1+1/m. Neither the pointwise nor the uniform ratio premise follows from flatness alone.

For a supported nonzero flat germ, meaning that v is nonzero in every neighborhood, the resulting necessary condition is

    limsup_(x->0,H(x)>0) |v(x)|^2/H(x)>=2/3.

The positive-pressure theorem LIT216, at its independently audited C1 velocity/pressure scope, supplies the opposite necessary condition liminf<=2. The two limits do not imply that every nearby ratio is in[2/3,2] or that the ratio converges. The common zero orbit is permitted because the undivided inequalities extend across it.

## 5. Exact finite-order endpoint test in the stress-only class

For any m>0, put r=|x| and

    v(x)=r^(m-1)x for x!=0, v(0)=0,
    P(x)=-(1+1/m)r^(2m).

These fields are continuous, v has exactly order m, and P(0)=0. For a radial tensor v tensor v+P I, its divergence away from0 is

    [(r^(2m))'+2r^(2m)/r+P']n=0.

This identity also holds distributionally across0: the boundary flux of the tensor against a fixed smooth test vector is O(r^(2m+2)), which tends to0. Hence div div(v tensor v+P I)=0. The pair is nonzero and satisfies the pressure bound with beta=1+1/m exactly. The strict finite-order constant cannot be weakened to equality in the theorem's stated continuous stress class. When m=1 the fields are the polynomials v=x and P=-2|x|^2.

These are not divergence-free examples: div v=(m+2)r^(m-1) away from0. They do not establish sharpness for incompressible Euler or contradict the target conjecture.

## 6. Exact infinitely flat endpoint test

Set a(r)=exp(-1/r^2) for r>0 and a(0)=0, E(r)=a(r)^2, and

    I(r)=integral_0^r E(t)/t dt,
    v(x)=a(r)x/r for x!=0, v(0)=0,
    P(x)=-E(r)-2I(r), P(0)=0.

The fields extend smoothly and vanish to infinite order at0. Indeed a/r and all its derivatives are flat; I'=E/r is flat with all derivatives, and the integral from0 supplies a flat primitive. For a radial scalar, these estimates also prove smoothness after composition with |x|.

The radial stress divergence is zero away from0 because P'=-E'-2E/r. Smoothness gives the same equality everywhere. Thus this is a nonzero smooth solution of the stress equation with

    P<=-|v|^2,

showing that the infinite-flatness theorem cannot replace beta>1 by beta=1 in the stress-only class.

Here H=3E/2+2I and R=E/H<2/3 at every nonzero point. Nevertheless R approaches2/3 as r approaches0, so there is no uniform Rstar<2/3. To see the limit without asymptotics, E'=4E/r^3 and

    I(r)=integral_0^r (t^2/4)E'(t)dt<=r^2E(r)/4.

Thus I/E tends to0 and R tends to2/3. This also refutes replacing the uniform strict ratio bound by the pointwise inequality R<2/3 in the stress-only class. Its negative stress has radial eigenvalue2I and transverse eigenvalues E+2I; their ratio is unbounded near0, so it does not violate A1610.

Again div v=a'+2a/r>0 off0. The example is not an incompressible pressure pair, a similarity tail or a full Euler profile. It tests only the exact scope of the continuous-stress theorem.

## 7. Verification and remaining questions

All six source sections of LIT250 were read. The radial distribution argument, pressure normalization, finite-order inequality, zero-set extension and supported ratio conclusions pass. Sections5-6 are independent exact countertests supplied for comparison through the existing configured model agents; actual provider runtime is unattested. They require no numerical computation.

The theorem strengthens the C1 tensor proof A1611 by using only continuous stress and velocity flatness, with an explicit finite-order threshold. No endpoint counterexample has been supplied in the divergence-free class. The remaining local ratio ranges, finite logarithmic energy and the main bare-decay conjecture stay open.
