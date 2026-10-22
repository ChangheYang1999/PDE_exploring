# Independent audit of proposed report item 4.39

## Exact statements and status

This packet audits the literal entry work/enter_439/text_v1.md, its complete report preview, and its references to P228 and P226. The two mathematical results are confirmed. Two repairs are required before entry approval: explicitly qualify the beta2 neighbourhood exclusion by the smooth B2 assumptions, and correct the P228 symbolic-control time from23:47 to23:45. The v1 full insertion controls passed51 checks at00:20:34 UTC. The v2 full preview passed13 follow-up checks at00:22:44 UTC; both repairs are adopted, and that preview is CONFIRMED. Actual insertion remains OPEN. These representation exclusions do not settle general B2.

The shared hypotheses are W of class C1 on R2, div W=2beta, W=betaX+o(r) uniformly at infinity, Theta of class C1, and W.gradTheta=(beta-2)Theta. Part(a), for beta>0, assumes one fixed finite horizontal polynomial degree and C1 vertical coefficients. Part(b), for beta>2, adds W(0)=0 and a global representation Theta=H(x/rho(y)), with rho positive C2 and H of class C2, H(0)=H'(0)=0 and H''(0)!=0. These match the standalone P228 and P226 theorems.

## Proof of part(a)

If a positive-degree coefficient is nonzero, choose the greatest such degree N and write f=f_N. On a component J of {f!=0}, set K=(N-1)beta+2>0. At each fixed y, W1/x tends beta and W2/x tends0 as x tends positive infinity. If f'(y)=0, then Theta_y has degree at most N-1 at that height. Dividing transport by x^N would give Kf=0, which is impossible. Thus f' never vanishes on J.

Solving transport for W2 gives W2(x,y)->g(y)=-Kf/f', since Theta_y/x^N tends f'(y)!=0. Integrate divergence over [R,2R] times [y1,y2], for arbitrary y1<y2 in J, and divide by R. Uniform convergence of W1/x on the compact height interval makes the vertical-face flux tend beta(y2-y1). The average of W2 on each horizontal face tends g(yi) from its ordinary finite limit. The divergence integral is 2beta(y2-y1). Hence g(y2)-g(y1)=beta(y2-y1), so g(y)=beta y+d. No derivative of a velocity limit is taken.

Since g never vanishes, f'/f=-K/(beta y+d), and integration gives f=c|beta y+d|^(-K/beta), c!=0, on J. At a finite endpoint of J, continuity and maximality would require f=0; the expression instead tends a nonzero finite value or diverges. Therefore J has no finite endpoint and equals R. But beta y+d has a real zero in J, a contradiction. Every positive-degree coefficient vanishes, and the axis condition Theta(0,y)=0 then kills f0. This includes N=1 and beta=2 and uses no coefficient bound at vertical infinity.

## Proof of part(b)

Write lambda=beta-2>0, k=x/rho(y), A=int_0^y rho, V(k,y)=W2(k rho(y),y), Q=W1-k rho'V. Chain differentiation gives W.gradTheta=H'Q/rho and Q_k+(rho V)_y=2beta rho. Where H'!=0, Q=rho q with q=lambda H/H', so rho V=(2beta-q')A+C(k), where C(k)=rho(0)W2(k rho(0),0).

The quadratic jet gives q/k->lambda/2 and q'->lambda/2. Thus q extends C1 across0. Taking k->0 and using C(0)=0 yields phi(y)=W2(0,y)=d0 A/rho, d0=1+3beta/2. Sublinearity gives phi(y)/y->beta at both ends. Integrating A'/A=d0/phi separately on the positive end and after y=-t on the negative end gives rho between positive multiples of |y|^(gamma-eps) and |y|^(gamma+eps), gamma=1/2+1/beta in(1/2,1), for any sufficiently small eps. No asymptotic identity is differentiated. Hence rho tends infinity at both ends, rho=o(|y|), and |y|rho tends infinity.

On the positive component (0,L) where H'!=0, fix an arbitrary finite k. Since k rho(y)=o(y), uniform sublinearity gives V(k,y)/y->beta as y tends positive infinity. The integrated identity gives the same limit as (2beta-q'(k))beta/d0; its C term vanishes because y rho tends infinity. Consequently q'=alpha=(beta-2)/2, and the center limit fixes q=alpha k. Thus kH'=2H and H=H''(0)k²/2 throughout (0,L). If L were finite, continuity would give H'(L)=H''(0)L!=0, contrary to maximality. Hence L=infinity. The two-end growth of rho gives a global minimum y_m with rho'(y_m)=0. At that height W1(x,y_m)=alpha x for every positive x, contradicting W1(x,y_m)/x->beta>alpha. Each limit fixes k before taking y to infinity.

## Applicability and counterexamples

For a smooth temperature in part(a), evaluation at N+1 distinct x values followed by inversion of a fixed Vandermonde matrix proves coefficient smoothness. For part(b), the y=0 slice gives H(k)=Theta(k rho(0),0), smooth with H''(0)=2a0rho(0)²!=0. Differentiating only in x at each fixed y gives Theta_xx(0,y)=H''(0)/rho(y)², proving rho smooth through the positive square-root formula. Subtracting the constant U(0) preserves uniform sublinearity. No inverse or observer gauge is changed.

The field W=(alpha x,d0 y), Theta=x² satisfies temperature transport, divergence and W(0)=0 but fails isotropic sublinearity. On y>0, W=betaX and Theta=x^N y^(-K/beta) satisfy temperature transport and divergence but do not extend with continuous coefficients across the entire axis. These verify the two scope examples.

The beta2 result 4.7(xxiv) needs full smooth B2 with the nonzero quadratic temperature jet. Adding only the vorticity equation to the broader opening hypotheses does not exclude constant representations: W=2X, Theta=Omega=0, H=0 and rho=1 satisfy transport, divergence, curl, vorticity, W(0)=0 and the velocity asymptotic. They fail the nonzero B2 jet. The Scope sentence must therefore say 'at beta = 2, in the smooth B2 setting, the form ...'. The Q1 bullet already says smooth B2 and is correctly scoped.

## Timing, dependencies and insertion checks

P226's proof-before-code record is23:31:43.371579, its final34 controls ran23:33:14.843227--23:33:15.335062, and publication was23:35:20.187110. P228's proof-before-controls record is23:44:47.917956, its49 controls ran23:45:26.628737--23:45:27.700944, and publication was23:47:48.391625. All these are UTC on2026-10-21. The candidate timeline incorrectly assigns P228's controls to23:47. The corrected timeline must distinguish controls23:45 from confirmation23:47.

The frozen entry, complete preview, preceding report, old and new timeline entries, and static application script are in verification/. No lead script is run. Own controls compare the complete preview against six approved changes with whitespace normalized, check preservation of every old timeline entry plus the one intended entry, and verify factual timestamps and scope. P226/P228 and their exact evidence are the mathematical dependencies; the complete arguments needed to assess this entry appear above. The scope does not include arbitrary polynomial growth, variable horizontal degree, or a beta>2 neighbourhood-only representation.

## Final preview adjudication

The lead's v2 uses the more specific qualification "in the full smooth B2 setting of 4.7(iii)" and distinguishes controls23:45 from confirmation23:47. Independent comparison of the entire normalized preview verifies that these are exactly the two changes requested after v1. All135 preceding timeline entries are preserved and exactlyone intended entry is added. The lead application script was read as data and never executed. Preview834489f2d05bf35c8c16620f018df3b702fbad8565f68058b5c0bda6a14fdddd is CONFIRMED; actual insertion requires a fresh read.
