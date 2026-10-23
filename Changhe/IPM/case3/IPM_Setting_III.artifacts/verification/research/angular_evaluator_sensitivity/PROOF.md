# Result327: controlled sensitivity of an auxiliary vertical evaluator

Written 2026-10-22T08:30:58.890374+00:00 before new numerical code. This is a finite diagnostic of the auxiliary hydrostatic problem at c=2. It is not the elliptic full-plane IPM inverse and supplies no primary existence evidence. Its motivation is the unresolved radius3 sign-count difference on exactly the same255 angular points in completed result320.

## Exact statement, hypotheses and notation

Let g be smooth, even in x and odd in y. On y>=0 assume the improper integrals below converge and permit differentiation in x on compact sets. These convergence and differentiation conditions are proved below for the saved finite representation and separately for the Gaussian manufacture; they remain explicit hypotheses for other g. For the saved state, fixed-x F and H have integrable O(s^(p-2)) tails, while the unrestricted gradient is O(r^(p-1)). Let F(x,s)=g_x(x,s), H(x,s)=g_xx(x,s). For eps>0 put h(x,s)=eps(1+sqrt(x^2+s^2)) and

D_eps F(x,s)=[F(x+h(x,s),s)-F(x-h(x,s),s)]/[2h(x,s)].

The h in this definition is fixed at the central evaluation point when the difference is taken. It is not a difference of F evaluated with recursively altered h. Set D_0 F=H. Define

V1(x,y)=-integral_y^infinity F(x,s) ds,
V2_eps(x,y)=integral_0^y s D_eps F(x,s) ds+y integral_y^infinity D_eps F(x,s) ds.

Define V_eps=(V1,V2_eps) and V_0=(V1,V2_0). V0 is the canonical auxiliary vertical velocity under the previously proved vertical gauge. For eps>0, Veps is a deliberately perturbed evaluator and generally is not divergence free. It must not be called the exact canonical inverse.

Claim1. Wherever the stated differentiations are justified,

div Veps(x,y)=integral_y^infinity [D_eps F(x,s)-H(x,s)] ds.

Claim2. At any fixed point with the same exact local values g,g_x,g_y, the signed residual R_eps=(2x+V1)g_x+(2y+V2_eps)g_y-g satisfies

R_eps-R_0=(V2_eps-V2_0)g_y.

These equalities also hold for exact rational arithmetic on any stored finite operands when the residual is formed without intermediate rounding. They are identities, not integral error bounds. Nf_eps=abs((2x+V1)g_x)+abs((2y+V2_eps)g_y)+abs(g), and Nv_eps=abs(g)+abs(xg_x+yg_y)+abs(V1g_x+V2_eps g_y). Each ratio uses its own denominator; a zero denominator is undefined. DeltaR/Nf_0 is a separately named fixed-denominator comparison.

Claim3. The Gaussian manufacture g(x,y)=y exp(-x^2-y^2) has

cH_eps=lim_(y->0) V2_eps(0,y)/y
= -exp(-eps^2)/a + (b/a)exp(-eps^2) J,
a=1+eps^2, b=2eps^2,
J=sqrt(pi)/(2sqrt(a)) exp(b^2/(4a)) erfc(b/(2sqrt(a))).

At eps=0 this is -1. Polynomial manufactures test only the local derivative operation: for g=y x^2, D_eps F=2y; for g=y x^4, D_eps F=12x^2 y+4h^2 y. Their nondecaying integrals are not evaluated.

## Complete arguments

Differentiating V1 gives -integral_y^infinity H. In V2_eps the two moving endpoint terms are y D_eps F and -y D_eps F and cancel, leaving integral_y^infinity D_eps F. Their sum proves Claim1. Because g is even in x and odd in y, F is odd in each variable and h is even in each. Thus D_eps F is even in x and odd in s. For negative y define V1(x,-y)=V1(x,y) and V2_eps(x,-y)=-V2_eps(x,y). V1 is odd in x and V2_eps even in x. This preserves the velocity parities but does not restore zero divergence. The divergence identity differentiates V1 in x and V2_eps only in y; no x derivative of h in V2_eps is needed. Because h uses a radial absolute value, no smoothness of the deliberately modified Veps at the origin is claimed.

Subtract the two transport expressions with identical local jets and V1. All terms except (V2_eps-V2_0)g_y cancel, proving Claim2. The triangle inequality Nf_eps>=abs(R_eps) holds for this residual definition. No Rv<=1 bound follows because Nv lacks the coefficient2 on X.grad g. The triangle inequality does give abs(R)<=2Nv, hence0<=Rv<=2 whenever Nv>0.

For the Gaussian, F(0+h,s)=-2hs exp(-h^2-s^2) and F(0-h,s)=2hs exp(-h^2-s^2), so D_eps F(0,s)=-2s exp(-s^2-eps^2(1+s)^2). Dominated convergence near y=0 makes cH_eps its integral over s>=0. Completing the square gives J=integral_0^infinity exp(-as^2-bs) ds as stated. Integrating the derivative of exp(-as^2-bs) gives 2a integral_0^infinity s exp(-as^2-bs) ds+bJ=1. Multiplication by -2exp(-eps^2) yields Claim3. Direct expansion of (x+h)-(x-h) and (x+h)^3-(x-h)^3 proves both local polynomial formulas.

Here is the tail argument for the saved finite representation, including the distinction between fixed x and an angular sector. Write sigma=(1+t)/2,w=(1-t)/2, r=L sqrt(sigma)/(2w)^P, p=1-1/P in(0,1), and g=y w B(t,theta), where B is a finite polynomial sum in t,sigma and cos(2k theta). The map is strictly increasing because d(log r)/dt=1/(4sigma)+P/(2w)>0; its endpoint limits are0 and infinity. Squaring the map makes sigma a smooth analytic function of r^2 near0 by the implicit function theorem. Then sigma^k cos(2k theta) is smooth at the origin, as shown in the completed Cartesian evaluator proof. All t/angular derivatives of B are bounded at t=1. The radial map gives w=O(r^(-1/P)), r d_r t=O(w), and repeated scaled radial derivatives of w remain O(w). Cartesian differentiation, expressed through radial/angular derivatives, therefore gives uniformly in angle |grad g|<=C r^(p-1) and |H|<=C r^(p-2) for large r. The constants depend on this fixed state, not on the sample point.

Evenness in x gives F(0,s)=0. For every fixed compact x interval, F(x,s)=integral_0^x H(u,s)du=O(|x|s^(p-2)) uniformly there. This stronger fixed-x bound proves absolute convergence of V1 and justifies its x derivative by the uniform integrable bound on H. It is not the weaker global gradient bound O(r^(p-1)). Thus the first model objection is resolved by a parity cancellation already available in the representation, without an added sign or decay hypothesis.

For a fixed eps>0, (x+-h(x,s),s) stays in a compact angular sector near the vertical as s grows. The global angular-uniform gradient bound above gives F(x+-h,s)=O(s^(p-1)) there. Since h is comparable to eps*s, D_eps F=O(s^(p-2)), proving its absolute tail convergence. For eps=0, H has that integrable order. These are separate bounds for each eps. No uniform eps error estimate or eps->0 interchange over the unbounded tail is inferred or used.


## Finite execution plan and independence

Freeze the producer's new default radius3 and radius30 arrays and the immutable state B coefficients from result320. Do not import or execute producer code. Reconstruct the255 angles and Cartesian points independently and check exact equality. Our density jets use Cartesian analytic chain rules, a Chebyshev recurrence and a complex angular recurrence. Our full half-line integral uses physical panels and a separate mapped tail. Reuse own bound B rule (finite order64, tail192, split128, inner.125); compare selected points using own A and C rules. The producer uses log-coordinate panels and a finite difference for g_xx.

Run the analytic baseline and eps=1e-4,1e-5,1e-6 on the same255 points at each of the two radii. The eps list is fixed before seeing results. Store the local jets, Veps and the difference-integrand tail integral at all points. Check the finite signed residual, both normalizations, sign counts, and nonconstant least-squares cosine coefficients independently using exact rational residual arithmetic in a separate checker. Dominant means largest absolute coefficient over k>=1 in the fit cos(2k theta),0<=k<3M, with M=32. Report the singular-value condition number of this actual cosine matrix. Sign changes count strict adjacent products<0 and do not skip zeros. Neither statistic is a continuous root count or an adequate summary of the full shape.

Own full baseline at every point is compared with completed320 only after recomputation. Producer stored velocities and jets are compared pointwise but do not become own inverse evaluations. Split producer-versus-own residual differences into exact fixed-jet velocity and fixed-velocity jet contributions. Treat all values as finite diagnostics without a rigorous integral enclosure. A repeated count, changed fit or closer residual does not establish the historical cause of the earlier producer values.

Manufactures precede candidate execution: local quadratic/quartic differences including h dependence; Gaussian center formula at eps0,.1,.3 against the independent physical quadrature at multiple rules; an off-axis Gaussian point compared with independent high-precision tanh-sinh quadrature (including its nonconstant h); zero-aware ratio and sign-count cases; exact residual decompositions. Record in advance that truncation and floating-point cancellation can both contribute at small eps, so no universal optimal step is asserted for this residual. Higher-precision local gx checks at any severe cancellation witnesses may be added if the results require them, in a documented extension before their execution.

## Dependencies, scope and unresolved steps

Dependencies are the completed Cartesian evaluator and physical quadrature derivations in research/independent_hydrostatic_evaluator, research/node_export_inverse_audit and completed result320. Exact residual identities are proved here. Before publication, bind all actual sources, saved arrays, outputs, manufacture evidence and actual Opus5.5 reviews. The finite experiment itself is OPEN until executed and independently checked. No derivative approximation at eps>0 is advertised as satisfying the defining PDE, no finite rule difference is an error bound, and no primary or auxiliary existence conclusion follows.

All operations write only in the verifier lane. No JavaScript/TypeScript/Node, servers/listeners/tunnels, RLScience cluster, Lean/Lake, commits/push/posts or human contact. One heavy CPU process, one thread, nice19, below16GB. Every shell command completes within10minutes; longer jobs use one detached timeout wrapper and recorded PID. The actual48-hour run deadline remains12:44:21Z on2026-10-22.
