# Local endpoint profiles and global pairs exact on a ball

Date: 2026-10-20. Independent audit of lead referee/scap3 Sections 2 and 3. Verdict: CONFIRMED analytically. Supporting exact checks are separate. Neither result gives a global admissible exact profile.

## Statement and notation

Let ell>1, D=ell-1, A=2ell-1, and U=(-psi_y,psi_x). Write R=(ell X+U).grad rho-rho and S=(DU+DU^T)/2. We verify two statements.

1. For every k>0 an analytic pair solves the elliptic and transport equations everywhere and satisfies ||S||<=D on a neighborhood of zero. Its slope is a=2A and its first nonlinear density jet is cubic. It fails the required growth and the global cap.
2. Given a>4D and any finite R0>0, a smooth canonical pair of slope a has sublinear growth with exponent p=1/ell, satisfies the global cap, and has zero transport residual on B_R0. Transport fails somewhere outside that ball.

The second statement uses the already independently proved flat-defect exclusion under the global strain cap, research/strain_cap_flat_exclusion/PROOF.md. The inverse uniqueness and dilation used below are proved explicitly. No sign condition on the constructed density is asserted.

## Exact local endpoint

Set

    rho=A y(1+cos(kx)),  psi=y(ell x-A sin(kx)/k).

Then U=(A sin(kx)/k-ell x, (ell-A cos(kx))y) and
W=ell X+U=(A sin(kx)/k, (2ell-A cos(kx))y). Direct differentiation gives -Delta psi=-A k y sin(kx)=rho_x. Dividing transport by Ay and using continuity when y=0, its left side is

    -A sin(kx)^2+(2ell-A cos(kx))(1+cos(kx))=1+cos(kx),

because 2ell=A+1. Hence R=0 globally. The center strain is psi_xy(0)=ell-A=-D, and rho_y(0)=2A. Moreover

    rho-2Ay=-(A k^2/2)x^2y+O(r^5),
    psi+Dxy=(A k^2/6)x^3y+O(r^6).

Thus the first nonlinear density degree is n=3 and a=(n-1)A. The strain has entries S11=A cos(kx)-ell, S22=-S11, S12=(A k y/2)sin(kx). With w=1-cos(kx)>=0,

    ||S||^2-D^2=A w[-2D+A w+(A k^2 y^2/4)(1+cos(kx))].

The bracket is at most -2D+(A k^2/2)r^2. Consequently the cap holds on r<=2 sqrt(D/A)/k. On x=0 the density is 2Ay, so it has linear growth; at x with sin(kx)!=0 the shear grows linearly in y. This establishes the asserted limitations and shows that local equations and a local cap do not exclude the endpoint, even with all Taylor orders available.

For completeness the degree-five compatibility also has no forced contradiction. Write h3=-3t x^2y, phi4=t x^3y, with t>0, h5=d x^4y+e x^2y^3+f y^5 and phi6=u x^5y+v x^3y^3+w xy^5. The degree-five equations are

    (A x d_x+y d_y-1)h5+2A(phi6)_x-3t^2x^4y=0,
    -Delta phi6=(h5)_x.

Coefficient comparison gives d=-5(A+1)w+3t^2/(2A), e=10Aw, f=-Aw/2, u=2(A+1)w-3t^2/(10A), v=-10(A+1)w/3, with w free. On the vertical axis the next strain term is -5w y^4, so local capping requires w>=0 if this is the first nonzero term there. The trigonometric pair realizes w=0 and t=A k^2/6.

## A radial background with an exactly affine core

Put alpha=1-1/ell in (0,1). Let eta be the smooth nonnegative function proportional to exp[-1/(s(1-s))] on (0,1), zero elsewhere, with integral one. Define

    H0(t)=1 for t<=0,
    H0(t)=(exp(-alpha t)-alpha exp(-t))/(1-alpha) for t>0,
    H(t)=int_0^1 eta(s) H0(t-s) ds,
    f(r)=H(log r)+H'(log r)/4.

Set H=1 at r=0, psi0=-DxyH(log r), rho0=4Dy f(r). The functions are constant in the radial factor for r<=1, hence smooth at zero. H0 is C1, so its distributional second derivative has no point mass; convolution gives smooth H. The identity

    d_r(r^4 H(log r))=4r^3 f(r)

shows that H_f=int_0^1 u^3 f(ur)du=H/4. Direct Cartesian differentiation of psi=-a xy H_f yields -Delta psi=rho_x for rho=ayf. It also yields

    max_theta ||S||=|a|(|K|+|L|)/8,
    K=2f+r f', L=r f'-6f+24H_f.

This can be checked without maximizing a matrix numerically: S11=a(K-L cos4theta)/8, S12=-aL sin4theta/8. For the present pair the maximum equals

    D max(|H+H'|, |H+H'/2+H''/4|).

For H0, the first expression equals 1 on t<0 and exp(-alpha t) on t>0. The second equals 1 on t<0 and on t>0 equals

    G(t)=[(1-alpha/2+alpha^2/4)e^(-alpha t)-(3alpha/4)e^(-t)]/(1-alpha).

Here G(0+)=1-alpha/4, G>0 and G'<0. Positivity follows from the positive coefficient difference at zero and slower decay of the positive term. For the derivative, 1-alpha/2+alpha^2/4>3/4 and e^-t<=e^-alpha t. Thus both expressions are in [0,1] before convolution and remain so afterwards. This proves the cap globally.

For r>=e, convolution costs at most e^alpha<3 and both expressions are at most 3ell r^-alpha. Hence ||S0||<=D/2 on r>=(6ell)^(1/alpha)=Rstar. At r>e, H is exactly C_alpha r^-alpha-C_1 r^-1, where C_alpha=(int eta(s)e^(alpha s)ds)/(1-alpha)>0 and C_1=alpha(int eta(s)e^s ds)/(1-alpha). Thus rho0 has a nonzero leading term 4D(1-alpha/4) C_alpha r^(1-alpha)sin(theta), and U0 and all differentiated terms have the required sublinear symbol bounds. On B1, rho0=4Dy, psi0=-Dxy, W0=(Ax,y).

## A remote compact stream with a central density slope

Define the odd function fstar(s)=eta(s-1) for s>0 and fstar(-s)=-fstar(s), and Kstar(s)=int_-infinity^s fstar(v)dv. Then Kstar is even, equals -1 on [-1,1], vanishes for |s|>=2, and Kstar'=fstar. Let chi(y)=1-int_-infinity^(|y|-1) eta(s)ds and g(y)=y^3 chi(y)/6. This is a smooth odd function supported in [-2,2], with g''(y)=y on [-1,1].

For b=a-4D>0 and L>=1 set

    psir=(b/L) fstar(x/L)g(y),
    rhor=-(b/L^2) fstar'(x/L)g(y)-b Kstar(x/L)g''(y).

Both functions are smooth and compactly supported. Their definitions give -Delta psir=(rhor)_x. The velocity is Ur=(-(b/L)fstar g', (b/L^2)fstar' g), so Ur vanishes on |x|<L although rhor=bg''(y) there. On B1 it adds exactly b y to the density.

Explicit constants suffice to separate the supports from the cap margin. If Z is the normalization integral of eta, then Z>1/729: on [1/3,2/3], the integrand is at least e^-4.5>3^-5, and the interval has length1/3. The inequality v^j e^-v<=j! gives

    ||fstar||<=729, ||fstar'||<=1458, ||fstar''||<=29160,
    ||g||<=4/3, ||g'||<=974, ||g''||<=4862.

For example differentiating g twice gives g''=y chi+y^2 chi'+y^3 chi''/6, bounded by 2+4*729+(8/6)*1458=4862. The strain entries and the triangle inequality give

    ||Sr||<= (b/L)[1458*974/L+(29160*(4/3)/L^2+729*4862)/2]
           <=3211731 b/L <4000000 b/L.

It is supported on L<=|x|<=2L, |y|<=2. Choose L>=max(2,Rstar,16000000 b/D). On this support ||S0+Sr||<=D/2+D/4<D; elsewhere Sr=0. At zero S=diag(D,-D), so the global supremum is exactly D.

## Canonical law, transport and scaling

The total pair has the required parities, elliptic equation and sublinear velocity. If another sublinear velocity had the same divergence and curl, their difference would be entire harmonic. The interior harmonic gradient estimate on a radius-R ball bounds its derivative at any fixed point by C R^-1 times its supremum there. Sublinearity sends this to zero; the difference is constant, and the parities force that constant to vanish. Thus the constructed velocity is canonical.

On B1 the pair is rho=ay, psi=-Dxy, W=(Ax,y), so transport is exact. The affine defect vanishes on an open ball. If transport held globally, the already proved flat-defect exclusion under the cap would give a contradiction. Thus it fails somewhere outside B1. Applying rho_lambda=lambda rho(X/lambda), psi_lambda=lambda^2 psi(X/lambda), with lambda=R0, gives exact transport on B_R0 and preserves a, ell and the strain cap. The far-field leading coefficient is multiplied by lambda^(1-p) and remains nonzero. Every weighted squared defect norm scales by lambda^(4-2m); the ratio is unchanged. Large exact-transport balls alone therefore do not improve that ratio.

Finally g'' must be negative somewhere on y>0: its integral there is g'(infinity)-g'(0)=0, while g''=y>0 near zero. At such a fixed vertical point the added density b g'' makes the total density negative for sufficiently large b. Global density positivity is not a property of this construction. Both verified examples have non-profile scope only, with global growth absent for the first and global transport absent for the second.
