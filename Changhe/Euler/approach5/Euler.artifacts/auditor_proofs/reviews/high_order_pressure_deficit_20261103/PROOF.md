# Sharp pressure deficits and a flat positive-pressure steady model

Status: complete independent audit of all eight LIT216 sections and C48(c). The full-ball hypothesis is essential. The models satisfy the local steady Euler and pressure systems; they are not actual decaying similarity profiles or actual tails.

## 1. Exact local statement and notation

Let B_R in R3 be centered at0. Suppose v in C1(B_R;R3), pi in C1(B_R), div v=0 and

    -Delta pi=partial_i partial_j(v_i v_j)

in distributions. Put s=pi-|v|^2/2. For real m>1 suppose |v(x)|<=C|x|^m. If on a full neighborhood of0

    s(x)-s(0)>=-epsilon|v(x)|^2,
    0<=epsilon<(m-1)/(2m),

then v=0 on a neighborhood. The strict threshold is sharp. If |v|=O(|x|^M) for every M, with radius and constant allowed to depend on M, every fixed epsilon<1/2 gives the same conclusion. Equivalently pi-pi(0)>=delta|v|^2 on a full neighborhood is sufficient for every delta>0 in the infinitely flat case. The endpoint delta=0 is insufficient.

There is also a C1 statement without a size-order assumption: if v(0)=curl v(0)=0 and s has a local minimum at0, then v vanishes near0. This strengthens the regularity scope of the older A1006 minimum argument.

## 2. Spherical identity at C1 regularity

Let the bar mean normalized unit-sphere average with arguments rn. Set

    E(r)=bar|v(rn)|^2, F(r)=bar(v(rn).n)^2,
    Y(r)=bar(pi(rn)-pi(0))+F(r).

These functions are C1 for r>0. Since div v=0, the distributional source equals div((v.grad)v). The flux identity obtained by radial testing is

    bar pi'(r)=-bar((v.grad)v).n.

One can first obtain this for almost every radius. Continuity of both sides extends it to every r>0. The possible integration constant in r^2 times the flux is zero at0 because pi is C1 and (v.grad)v is continuous. Thus no unproved boundary term at the center remains.

Write v=v_r n+v_T. Then

    ((v.grad)v).n=v_r partial_r v_r+r^(-1)v_T.grad_S v_r-r^(-1)|v_T|^2,
    div_S v_T=-r partial_r v_r-2v_r.

Integrating by parts on the sphere gives bar((v.grad)v).n=F'+(3F-E)/r, hence exactly

    Y'=(E-3F)/r.                                          (2.1)

For divergence-free C1 v the product-source equation equals -Delta pi=tr((Dv)^2) distributionally: mollify v locally, use the smooth identity and pass using C1 convergence. Thus C48's C^(1,beta) version is covered and LIT216's weaker C1 formulation is valid.

## 3. The graded threshold and infinite-order corollary

Since v=O(r^m), E,F=O(r^(2m)) and Y(0)=0. Integrating(2.1) gives Y=O(r^(2m)). The pointwise scalar inequality, after averaging, gives

    Y>=(1/2-epsilon)E+F>=0.

Let beta=(1/2-epsilon)^(-1). Equation(2.1) yields Y'<=beta Y/r. Thus r^(-beta)Y is nonnegative and nonincreasing. The strict threshold is exactly beta<2m, so this function tends to0 as r decreases to0. It must vanish identically. The lower bound forces E=0 on each small sphere, so continuity makes v=0 on a ball.

For size-flat v, choose m>1/(1-2epsilon). For delta in(0,1/2], use epsilon=1/2-delta. Larger delta implies the inequality with delta=1/2. Thus every positive delta is covered. No inference at delta=0 follows from this limit.

## 4. Local scalar minima and constant scalar regions

Suppose v(0)=curl v(0)=0 and s has a local minimum. Put M=Dv(0). Divergence and curl make M symmetric and trace free. The C1 expansion v(rn)=rMn+o(r), uniformly in n, gives

    E(r)=|M|_F^2 r^2/3+o(r^2),
    F(r)=2|M|_F^2 r^2/15+o(r^2).

The second equality follows from the fourth spherical moment formula, or integrating the coordinate monomials n_i n_j n_k n_l. Integrating(2.1) therefore gives

    Y(r)=-|M|_F^2 r^2/30+o(r^2).

But the minimum assumption gives Y>=E/2+F>=0. Hence M=0. Now E,F=o(r^2), and integration gives Y=o(r^2). The same lower bound gives Y'<=2Y/r. The nonnegative nonincreasing function r^(-2)Y tends to0 at0, so Y=E=0 near0. Only C1 regularity is needed.

If s is constant on a connected open region G, either v=0 throughout G or v and curl v have no simultaneous zero anywhere in G. To see this, let K be the relative support of v. At any relative boundary point, v=Dv=0 by continuity from the open complement, so the local result would create a neighborhood disjoint from K, contradicting support. Thus K has empty relative boundary. Connectedness makes K empty or G. In the latter case any simultaneous zero would again create an open zero neighborhood, impossible for full support. This argument neither assumes isolated zeros nor encloses them in an index contour.

## 5. Finite-order saturation for every real m>1

Let rho=(x1^2+x2^2)^(1/2), Jx=(-x2,x1,0), and define

    v=rho^(m-1)Jx, pi=rho^(2m)/(2m).

Set both to0 on the axis. The first derivatives of v off the axis are O(rho^(m-1)), so v is C1 with derivative0 on the axis. It is C^(1,beta) for some beta>0 whenever m>1, using any beta<min(m-1,1); the pressure is C2. Direct calculation gives

    div v=0, (v.grad)v=-rho^(2m-2)(x1,x2,0),
    grad pi=rho^(2m-2)(x1,x2,0).

Thus this is an exact local steady Euler pair and solves the pressure equation. Since |v|^2=rho^(2m),

    s=-(m-1)/(2m)|v|^2.

It is nonzero off the axis, with a supported simultaneous velocity and vorticity zero on the axis. The threshold is therefore sharp in the stated C1 class and in C48's class with some positive Holder exponent. This is not a claim of sharpness for each separately prescribed exponent exceeding the regularity of the example.

## 6. Smooth infinite-order model and the endpoint ratio

Put t=x1^2+x2^2, g(t)=exp(-1/t) for t>0 and g(0)=0. Define

    v=g(t)Jx, pi=(1/2)integral_0^t exp(-2/u)du.

All derivatives of g and the integrand extend as0 at0. Thus v and pi are smooth and flat at every point of the axis. The same direct steady Euler calculation gives

    div v=0, (v.grad)v=-g(t)^2(x1,x2,0),
    grad pi=g(t)^2(x1,x2,0),
    curl v=(0,0,2g(t)(1+1/t)) off the axis.

Vorticity is nonzero arbitrarily close to each axis point. Pressure is positive off the axis and zero on it. Let I(t)=integral_0^t exp(-2/u)du. Integration by parts gives

    I(t)=(t^2/2)exp(-2/t)-integral_0^t u exp(-2/u)du.

The final integral lies strictly between0 and tI(t). Dividing the resulting bounds by2t exp(-2/t) gives

    t/[4(1+t)]<=pi/|v|^2<t/4, t>0.

The ratio approaches0 from above, while s/|v|^2 approaches-1/2 from above. This verifies the sharp infinite-order endpoint and shows that arbitrarily large strict scalar deficits do not imply a negative pressure value. The ratios are only used off the zero axis, where their denominators are nonzero.

## 7. Complete similarity residual and actual-tail interpretation

For any c>0 and finite omega, put A=cI-omega J and use the same pi. The complete rotating-profile residual is

    R=(1-c)v+Dv(Ax+v)+omega Jv+grad pi.

The nonlinear steady terms cancel. Equivariance gives Dv(Jx)=Jv, so the rotation terms cancel too. Since x.grad g=2t g', the remainder is

    R=g(t)(1+2c/t)Jx, t>0,
    (curl R)_3=2g(t)[1+1/t+2c/t^2]>0.

All other curl components vanish. This follows directly from curl(h(t)Jx)_3=2h+2th'. Therefore no alternative C1 pressure can repair this velocity into a similarity profile, since every distributional gradient has zero curl. The field is also independent of x3 and grows linearly at large rho. No decay, twisted tail homogeneity or actual-profile realization is asserted.

For an actual tail in the exact class of the smooth-quasianalytic review, take x0 in T0 and assume V is size-flat there. Since x0 is in supp W, V cannot vanish on a full neighborhood. The contrapositive of Section3 gives, for every delta>0 and every neighborhood O,

    some x in O satisfies P2(x)<delta|V(x)|^2.

For only V=O(distance^m), the corresponding conclusion holds for every delta>1/(2m). More generally a supported order-m velocity zero has S(x)-S(x0)<-epsilon|V(x)|^2 arbitrarily nearby for every nonnegative epsilon<(m-1)/(2m). These are continuous-function inequalities. A witness is not assumed vortical or nonzero in velocity, and pressure negativity is not asserted. For delta>=1/2 in the infinitely flat statement, choose a smaller positive delta first rather than substituting a negative epsilon into the theorem.

## 8. Verification and remaining scope

All eight LIT216 sections and the whole C48(c) proof were read and independently reconstructed, including the C1 central flux, the scalar-minimum endpoint, real noninteger m and the complete nonzero residual. No numerical computation is needed. The sources are pinned after the full post-read.

The unrestricted Euler conjecture, the exclusion of infinitely flat supported actual T0 points, and any sign theorem for actual tail pressure remain open. No one-sided region inequality is substituted for the full-ball premise. C48 supplies a continuing configured model comparison, runtime unattested; a focused comparison of the extra C1 minimum statement remains requested through existing agents. No new model client, agent or formal build is used.
