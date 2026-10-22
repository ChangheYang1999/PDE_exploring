# Flatness rates require more than the local identities alone

Status: CONFIRMED for the two precisely separated packages of weaker hypotheses; full local equations together with outgoing endpoint geometry remain OPEN. Complete independent informal proof written before controls. The two examples below separate hypotheses. Neither is a profile in the prompt's full class, and neither settles regularity under both the full local equations and an outgoing endpoint.

Throughout, curlW means partial_u W_v-partial_v W_u in an oriented Cartesian chart; Omega=-curlW.

## 1. A smooth flat function with no finite Gevrey order

For |u| sufficiently small, define

    h(u)=exp[-log(1/u)^2] for u>0,
    h(u)=0 for u<=0.

Put L=log(1/u) on u>0. For each integer n>=0 there is a polynomial P_n such that

    h^(n)(u)=u^(-n) exp(-L^2) P_n(L),
    P_0=1,
    P_(n+1)=(2L-n)P_n-P_n'.                         (1)

This follows by differentiating the displayed expression, using dL/du=-1/u. Every fixed derivative tends to0 faster than any power of u: after multiplication by u^(-k), its absolute value is exp[-L^2+(n+k)L]|P_n(L)|, which tends0 as L tends infinity. Extending all derivatives by0 to u<=0 makes h C-infinity and flat at0. An induction using the derivative limits proves differentiability across0 at every order. The function is strictly positive for u>0.

Here a finite Gevrey-s bound near0 means, for some constants C,R>0 and finite s>=1,

    sup_(|u|<epsilon) |h^(n)(u)| <= C R^n (n!)^s
    for every integer n>=0.                         (2)

This is the usual local derivative convention; a primary-source definition is archived in verification/source_record.json. No theorem from that source is used below.

Taylor's integral remainder at the flat point would give

    |h(u)| <= C (R u)^n (n!)^(s-1)                  (3)

for all positive u sufficiently small and every n. If s=1, choose Ru<1 and send n to infinity; then h(u)=0, a contradiction. If s>1, put q=1/(s-1) and choose

    n=floor[(2 R u)^(-q)].

For small u this n is at least half of (2Ru)^(-q), and Ru n^(s-1)<=1/2. Since n!<=n^n, (3) implies

    h(u) <= C 2^(-n) <= C exp[-c u^(-q)]             (4)

with c=(log2)(2R)^(-q)/2>0. But for any c,q>0,

    log[h(u) exp(c u^(-q))] = -L^2+c exp(qL) -> infinity.

This contradicts(4). Therefore h has no finite Gevrey order on any neighborhood of0. It also fails every nonzero stretched-exponential upper bound C exp(-c/u^q), despite being smooth and flat.

The first derivatives needed below are

    h'=2L h/u,
    h''=(4L^2-2L-2)h/u^2.                           (5)

In particular h''>0 for0<u<e^(-1). If h' had a bound of the form(2), then for n>=1, h^(n)=(h')^(n-1) would have the same bound with R enlarged to at least1; the n=0 bound follows by integrating h' from0. Thus h would satisfy(2), a contradiction. Therefore h' has no finite Gevrey order either.

## 2. Both local equations without an endpoint

Use physical Cartesian coordinates (x,y) near p=(0,M/4), for any real M, and set

    F(x)=M+h(x),
    Theta=F(x),
    W=(0,4y-F(x)),
    Omega=F'(x).

Then divW=4 and -curlW=F'=Omega. Both beta2 equations hold exactly:

    W.gradTheta=0,
    W.gradOmega+Omega=F'=Theta_x.

At p, Theta-M and Omega are flat, and DW(p)=diag(0,4). Nonetheless Theta-M and Omega have no finite Gevrey order near p, by section1 and restriction to a horizontal line. These facts show that the two local equations and flat jets with the stated derivative, considered without the endpoint geometry, do not give an automatic finite Gevrey estimate.

The exact reason this is not a counterexample to the outgoing-endpoint question is that the equilibrium set is the complete local graph y=F(x)/4 on both sides of x=0. It has no endpoint at p. This is a local Cartesian comparison field; x-reflection, the marked a0 jet, full-plane sublinear canonical velocity, and other global profile conditions are not imposed or inferred.

## 3. An outgoing endpoint with exact thermal transport

Now use physical coordinates (u,v) about p=(0,0), where v=y-M/4 is a constant translation of y and u=x. Define

    f(u)=h(u),
    F(u)=M-h(-u),
    W=(f(u),(4-f'(u))v+M-F(u)),
    Theta=F(u),
    Omega=f''(u)v+F'(u).                            (6)

All fields are smooth across u=0. Direct differentiation gives divW=4, -curlW=Omega and the exact thermal equation W.gradTheta=f F'=0. Indeed f and all its derivatives vanish on u<=0, while F-M and all its derivatives vanish on u>=0. At p, DW=diag(0,4), and Theta-M and Omega are flat. On u<0, Theta-M=-h(-u), so the temperature is not Gevrey of any finite order on any full neighborhood of p and is nonconstant on every terminal subarc.

For small |u|, 4-f'(u)>0. The normal nullcline is

    v=k(u)=(F(u)-M)/(4-f'(u)).

For u<=0, f'=0 and k(u)=-h(-u)/4, and every point (u,k(u)) is an equilibrium. For u>0, f(u)>0, so there is no equilibrium. The reduced tangential field is exactly f and is strictly outward. Thus p is a smooth outgoing endpoint of the local equilibrium arc. This checks the geometry rather than merely matching its derivative at p.

The vorticity equation has the exact residual

    R_Omega = W.gradOmega+Omega-Theta_u
            = [f f'''+(5-f')f'']v.                 (7)

Terms f F'' and (M-F)f'' vanish because of their disjoint one-sided supports. On u<=0 this residual is zero, so both equations hold on the interior side of the equilibrium arc and to every order at p. For u>0, (1) and(5) give

    [f f'''+(5-f')f'']/f''
       = 5-f'+(h/u) P_3(L)/P_2(L) -> 5
       as u tends0 from above.                     (8)

The limit uses only exponential domination of a fixed polynomial and P_2(L)>0 for L>1. Therefore the coefficient in(7) is strictly positive for small u>0. The vorticity equation fails at every such point with v!=0. In particular it fails in every full neighborhood of p and on the local outgoing side. This is consistent with164, which excludes this affine-transverse ansatz from full local B2 profiles.

Thus exact thermal transport, smooth outgoing geometry, nonconstant flat terminal temperature, correct local curl/divergence, and both equations on the interior side still do not force a finite Gevrey rate. The missing hypothesis in this example is precisely the vorticity equation on the outgoing side. No gluing, inverse or existence claim is hidden in(6).

## 4. What remains open

For a genuine smooth outgoing B2 endpoint, the two local equations force Theta=Theta(p) and Omega=0 on an open outgoing region, so all their derivatives vanish on its boundary. This is the consequence established in162 and164. It gives, at p, a bound of the form C_N |X-p|^N for each fixed N, with no estimate yet on the growth of C_N as N increases.

Sections2 and3 do not resolve whether adding all the missing hypotheses produces such growth control. Specifically, whether the full local equations together with a smooth outgoing endpoint force a finite Gevrey estimate, some specified quantitative derivative sequence, or a stronger continuation principle is OPEN. They refute only attempts to infer the estimate from the displayed weaker packages of hypotheses. They are not counterexamples to the full local endpoint problem or to the prompt's global B2 class.

Dependencies: elementary differentiation, Taylor's integral remainder and exact Cartesian residual calculation suffice for sections1-3. Sections162 and164 are used only to state the already checked outgoing-side consequence and the scope of the remaining question. No numerical computation or external regularity theorem is a premise.

Written UTC 2026-10-21T12:22:55.182970+00:00, before control implementation.

Wording clarification UTC 2026-10-21T12:29:59.962295+00:00: the log variable is always L=log(1/u), not1/u, and h is always exp(-L^2). The residual includes both +Omega and -Theta_u, so their F-prime terms cancel exactly. The full-equations/outgoing-endpoint combination remains open.
