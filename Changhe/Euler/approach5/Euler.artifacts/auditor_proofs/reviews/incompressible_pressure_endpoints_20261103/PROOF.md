# Incompressible positive-pressure endpoint examples

## 1. Exact finite-order statement

For every real m>0 put rho=sqrt(x1²+x2²), e_theta=(-x2,x1,0)/rho away from the axis and

    v=rho^m e_theta, P=rho^(2m)/(2m).

Set both fields equal to zero on the axis. They are continuous on R3, satisfy div v=0 and div(v tensor v+P I)=0 in distributions, have exact value order m at the origin, and obey P=|v|²/(2m). Thus the strict finite-order threshold delta>1/(2m) in A1638 cannot be replaced by equality in the continuous-stress class, even after adding incompressibility and stationary Euler momentum.

To check all claims, more generally let v=a(rho)e_theta and P(rho)=integral_0^rho a(t)²/t dt. Off the axis, direct cylindrical differentiation gives

    div v=0, (v.grad)v=-a² e_rho/rho,
    grad P=a² e_rho/rho,
    curl v=(a'+a/rho)e3.

For a=rho^m the pressure integral converges since m>0. The stress is O(rho^(2m)). For a compact vector test, excising a tube of radius epsilon leaves a boundary integral O(epsilon^(2m+1)), which tends to zero. Velocity flux through the tube is identically zero. These facts remove the axis in both distributional equations. The value bound |v|=rho^m<=|x|^m is saturated on x3=0. For m=2k+1 with integer k>=0, the fields are the smooth polynomials

    v=(x1²+x2²)^k(-x2,x1,0),
    P=(x1²+x2²)^(2k+1)/(4k+2).

No smoothness is asserted for every noninteger m. In particular, the continuous theorem's sharpness for all m and the smooth examples at odd integers are different claims.

## 2. The infinitely flat stationary example

Now take a(rho)=exp(-1/rho²) for rho>0, extended by zero, E=a² and

    v=a(rho)e_theta, P=I(rho)=integral_0^rho E(t)/t dt.

All derivatives of a/rho and E/rho tend to zero faster than every power at the axis. Since v=(a/rho)(-x2,x1,0) and I'=E/rho, both fields are smooth and flat there. They are independent of x3 and nonzero in every neighborhood of the origin. Section 1 proves stationary Euler and incompressibility; their classical smooth extensions satisfy both equations everywhere. The helicity v.curl v is zero. P is zero on the axis and strictly positive off it.

This is a counterexample to replacing delta>0 by delta=0 in the infinite-flatness positive-pressure criterion, even in the stronger smooth incompressible stationary class. It strengthens the scope of the elementary positive endpoint test without asserting similarity homogeneity.

## 3. The ratio endpoint with the full zero-set convention

Because E'=4E/rho³,

    0<I(rho)=integral_0^rho (t²/4)E'(t)dt<rho² E(rho)/4.

For 0<rho<1 define H=E/2-P. The preceding estimate gives

    E/4<H<E/2, 2<R=E/H<4, I/E->0, R->2 as rho->0.

On the axis H=v=0. Thus H>=0 and v=0 on {H=0} throughout the tube. The example lies in precisely the zero-set convention of the local ratio statements. It has pointwise R>2 on {H>0} but no uniform lower margin above 2 in any neighborhood of the origin. Consequently the pointwise inequality alone cannot replace the uniform margin. It agrees with the necessary liminf R<=2, attaining equality. Flatness along a line is permitted; no isolated-zero premise is used.

## 4. Failure of every target similarity equation

Let 0<c<1, omega any real number and Jx=(-x2,x1,0). Equivariance of a(rho)e_theta gives (Jx.grad)v=Jv. Hence the rotation terms in the similarity equation cancel. With the displayed stationary pressure the exact residual is

    F=[(1-c)a+c rho a']e_theta.

For a=rho^m it is (1-c+cm)a e_theta, whose scalar coefficient is positive. For a=exp(-1/rho²) it is [(1-c)+2c/rho²]a e_theta, again positive off the axis. On a complete circle the circulation is

    integral F.dx=2pi rho[(1-c)a+c rho a']>0.

The circulation of any single-valued pressure gradient is zero. Therefore another pressure cannot repair either field on a full tubular neighborhood. For completeness even on a simply connected small angular patch these particular residuals have nonzero curl somewhere in every punctured neighborhood: the axial curl is rho^(-1)(rho F_theta)', which is not identically zero for either displayed a. The circle argument alone suffices for the source's stated full-tube claim.

The fields also fail spatial decay: at a fixed rho>0 their speeds stay nonzero as |x3| tends to infinity. The power example grows in rho, and the flat example tends to unit speed. Thus neither is a target profile for any omega or for 2/5<c<1/2.

## 5. Dependencies and limits

All five sections of LIT252 and this independent proof have been read. The argument needs only exact differentiation, a convergent integral, and the stated vanishing tube flux. There is no numerical computation or external existence theorem. These examples complement A1618-A1620, which concern negative pressure and lack divergence freedom, and A1640, whose spherical flat pair has positive pressure but negative H on its axis.

The incompressible negative-pressure endpoint remains OPEN. So do the common-flat tail system, the missing similarity homogeneity and rank relations for these examples, and the main nonexistence conjecture. No endpoint optimality for actual rotating profiles follows from these stationary tests.
