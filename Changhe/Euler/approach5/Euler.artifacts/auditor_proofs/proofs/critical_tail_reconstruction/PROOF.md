# Critical-tail reconstruction of a smooth independent bracket field

## Statement and hypotheses

Fix 2/5<c<1/2 and finite real omega, set gamma=1/c in (2,5/2), p=3/gamma and alpha=5-2gamma. Let U0,W be the smooth real fields of A121, with U0 compactly supported, div U0=div W=0, W nonzero and

    [Ay+U0,W]=-(1+c)W,   A=cI-omega J.

Choose R0 beyond the support of U0 and with w(theta)=W(R0 theta) nonzero. The exterior transport law is

    W(R0 exp(ct) exp(-omega Jt)theta)=exp(-t)exp(-omega Jt)w(theta).

Under these hypotheses all four numbered conclusions of LIT36 hold. The reconstructed velocity is not thereby an Euler profile. This statement has no regular-attractor existence conclusion.

## Recurrence and the exact endpoint norm

Exterior differentiation gives |D^k W(y)|<=C_k(1+|y|)^(-gamma-k). Constants may depend on omega. The bounded smooth field has complete flow in both directions. Along every trajectory,

    |d_t(1+|y|)^(gamma+1)|<=C.

The images of a bounded set up to integer time N therefore lie in a ball of volume O(N^(3/(gamma+1))). The exponent is less than one. Since div W=0, these maps preserve volume. If E is a bounded set of points which never return to a given bounded measurable set containing E, its positive integer iterates are disjoint, giving

    (N+1)|E|<=C(1+N)^(3/(gamma+1)).

Thus E has measure zero. Taking the last return handles finitely many returns, and a countable basis of bounded balls proves almost-everywhere topological recurrence. The same proof applies in negative time. A fixed point is recurrent as usual.

Rotating polar coordinates have volume c R0^3 exp(3ct) dt dtheta. Hence the exterior L^s integral is a positive constant times integral_0^infinity exp((3c-s)t)dt. It is finite exactly when s>3c=p. The compact core creates no additional restriction for finite positive s.

For R>=R0 the distribution function is exactly

    lambda^p |{y: |y|>R, |W(y)|>lambda}|
      =R0^3/3 integral_S2 (|w|^p-lambda^p(R/R0)^3)_+ dtheta.

It increases to C0=R0^3/3 integral |w|^p>0 as lambda decreases to zero. Thus every exterior weak-L^p quasi-norm to the power p equals C0. Boundedness on the compact core gives global weak-L^p membership. The positive limiting distribution coefficient implies W*(t)>=C t^(-1/p) for large t, excluding every finite-index Lorentz class. This is the precise critical case left outside A165-A166.

## Inversion, cancellation and energy

Extend the exterior formula to all positive radii and call the result Wh. It is smooth off zero, homogeneous under dilation combined with Q_lambda=exp(-(omega/c)J log lambda), and locally integrable because gamma<3. Its divergence vanishes away from zero. Flux through spheres is constant in radius and is also multiplied by lambda^(2-gamma), so it is zero. Subtracting the test-function value at zero in the remaining boundary term gives O(r^(3-gamma)); hence div Wh=0 distributionally on all of R3.

D=W-Wh is compactly supported, integrable, distributionally divergence free and has finite first absolute moment. Testing div D against a cutoff equal to y_i on its support gives integral D_i=0. No unverified surface term at the singular origin is used.

The Newton potentials A0=N*W and Ah=N*Wh, N=1/(4pi |y|), converge absolutely, with Ah evaluated away from zero. Their outer integrals are bounded by integral r^(1-gamma)dr. Local singularities are integrable. They define locally integrable distributions on all of R3 and satisfy -Delta A0=W, -Delta Ah=Wh and div A0=div Ah=0. The last assertion follows by distributional integration by parts; the outer boundary is O(r^(1-gamma)). Set V=curl A0 and Vh=curl Ah. Local elliptic regularity gives smoothness on the indicated domains, and

    div V=0, curl V=W,   div Vh=0, curl Vh=Wh.

In particular Vh is nonzero. Kernel covariance gives

    Vh(lambda Q_lambda y)=lambda^(1-gamma)Q_lambda Vh(y).

The difference is the Biot-Savart convolution K*D. For |y|>2R0, subtracting D^kK(y) inside its integral is legitimate because integral D=0. The mean-value estimate and finite first moment yield

    |D^k(V-Vh)(y)|<=C_k |y|^(-3-k).

This proves all derivative tail estimates and strong rotating blow-down convergence. The rescaled error is O(lambda^(gamma-4)), including every fixed number of derivatives on a punctured annulus.

By rotation invariance of sphere area,

    integral_(|y|<R)|Vh|^2=C_h R^alpha,
    C_h=alpha^(-1) integral_S2 |Vh(theta)|^2>0.

Near zero Vh is L2 because alpha>0. At infinity the cross term in |V|^2-|Vh|^2 is O(r^(-2-gamma)) and the squared remainder O(r^-6). Thus this signed difference is absolutely integrable on R3, and its omitted outer integral is O(R^(1-gamma)). Consequently

    integral_(|y|<R)|V|^2=C_h R^alpha+C_defect+O(R^(1-gamma)).

## The unresolved equation and an additional necessary tail test

The reconstructed field has the actual curl W, but its carrier is Ay+V. Its exact vorticity residual is

    [Ay+V,W]+(1+c)W=[V-U0,W].

Outside the compact support of U0 it equals [V,W]=O(r^(-2gamma)). If this residual vanished everywhere, the full smooth momentum vector would be curl free on the simply connected space R3, giving a global pressure and an exact profile. No such vanishing has been proved.

There is a useful necessary test. On the exterior W=Wh and V=Vh+H, where D^kH=O(r^(-3-k)). Therefore

    [V,W]=[Vh,Wh]+O(r^(-gamma-4)).

The first term has exact rotating homogeneity of degree -2gamma. Since gamma<4, exact vanishing of the residual forces [Vh,Wh]=0 by scaling any punctured point to infinity. Equivalently the leading velocity must itself solve the steady Euler curl equation on the punctured space. This implication supplies a test, not an exclusion: no claim that it fails for every A121 construction is established.

## Dependencies and scope

The only existence input is A121. The recurrence, distribution-function, inversion and residual arguments above are direct. No pressure is imported from U0. The old bracket identity is not silently transferred to V. No numerical calculation is used, and no bound uniform as |omega| tends to infinity is asserted.
