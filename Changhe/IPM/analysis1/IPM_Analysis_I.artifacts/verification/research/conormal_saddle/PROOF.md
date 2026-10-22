# The weighted saddle inverse and a sufficient exit-trace condition

Date: 2026-10-20. Status: local model statements CONFIRMED by independent reconstruction, exact rational arithmetic with interval cross-check, and actual Claude Opus5.5 focused follow-ups. Global realization remains OPEN. This addresses only the local model statements in the pinned lead `conormal_framework.md` revision2. It does not construct the proposed global edge/corner space.

## Weighted maximal-domain inverse

Fix A>0, D=2A+1, b_0=(A+3)/2, real a,b, and a nonnegative integer m. On Q={(x,y):x>0,y>0}, define H_b^m(a,b) as the completion of C_c^infinity(Q) under

||h||^2=sum_(i+j<=m) integral_Q x^(-2a)y^(-2b)|(x partial_x)^i(y partial_y)^j h|^2 dx dy.

Put T=-Ax partial_x+Dy partial_y-1 and delta=bD-aA-b_0. Its maximal distributional domain is D(T)={h in H_b^m(a,b):Th in H_b^m(a,b)}. If delta!=0, T is bijective from D(T) to H_b^m(a,b), and

sup_(f!=0) ||T^(-1)f||_(H_b^m)/||f||_(H_b^m)=1/|delta|.

This is the inverse norm measured in the base space. With the sum graph norm ||h||_D=||h||+||Th||, the inverse norm into D(T) is exactly1+1/|delta|. With the Hilbert graph norm it is sqrt(1+|delta|^(-2)); these two graph norms are equivalent, but not identical. Thus a bare assertion of the sharp inverse norm must specify the output norm.

For delta<0 the inverse is

T^(-1)f(X)=-integral_0^infinity exp(-t) f(exp(-At)x,exp(Dt)y)dt.

For delta>0 it is

T^(-1)f(X)=integral_(-infinity)^0 exp(-t) f(exp(-At)x,exp(Dt)y)dt.

Both are Bochner integrals converging in the base Hilbert space. If delta=0, T is injective with dense nonclosed range and has no bounded inverse.

To prove these statements put u=log x,v=log y and

F(u,v)=exp((1/2-a)u+(1/2-b)v)h(exp u,exp v).

This is a unitary map for the weighted L^2 term. The two b derivatives become partial_u+a-1/2 and partial_v+b-1/2. Consequently, with unitary Fourier transform in (u,v), the full norm becomes

integral_R2 P_m(xi,eta)|F_hat(xi,eta)|^2 dxi deta,
P_m=sum_(i+j<=m)(xi^2+(a-1/2)^2)^i(eta^2+(b-1/2)^2)^j.

P_m is positive, bounded below by1, and comparable to(1+xi^2+eta^2)^m. The conjugated T is -A partial_u+D partial_v+delta, with symbol delta+i(D eta-A xi). Distributional differentiation identifies its maximal domain with the functions for which this symbol times F_hat belongs to L^2(P_m dxi deta). When delta!=0, division by the symbol defines an everywhere bounded inverse into the base space and lies in the maximal domain. Its exact norm is the essential supremum of the reciprocal modulus, namely1/|delta|. Fourier functions supported in increasingly narrow strips about D eta=A xi give sharpness. The graph-norm constants follow by adding ||T T^(-1)f||=||f||, or adding its square.

When delta=0, the zero set of the symbol is a line of measure zero, so the kernel is zero. The range is dense: truncate the Fourier transform of any target to the sets |D eta-A xi|>=epsilon, then divide by the symbol; these targets converge in the base norm. Its range is not closed because unit vectors supported in shrinking strips have ||Th|| tending to0. If the range were closed, it would be a Banach space in the base norm. The inverse of this injective closed operator would then be bounded from its range into the base space by the closed graph theorem, contradicting these vectors. Equivalently one may choose a target whose square-integrable Fourier transform does not remain square-integrable after division near the line.

The semigroup S(t)h=exp(-t)h(exp(-At)x,exp(Dt)y) has norm exp(delta t), either by change of variables or its Fourier multiplier. Its generator is T, and it is strongly continuous. The two integrals have the asserted norms and solve T R f=f by integration of partial_t S(t)f, first for smooth compact Fourier data and then by closure. They agree with the unique Fourier inverse. A graph core can be obtained by truncation and smoothing in log coordinates: T has constant coefficients, smoothing commutes with it, and derivatives of expanding cutoffs tend to zero in the commutator. This also verifies the distributional realization independently of the integral formula.

This inverse gives no full additional b derivative. Indeed high-frequency packets can remain near D eta=A xi while their transverse frequency tends to infinity. Their inverse multiplier stays of size1/|delta|, with no transverse decay.

## Exit trace and regularity at a finite saddle box

Retain A>0, D=2A+1, T=-Ax partial_x+Dy partial_y-1, and weighted measure x^(-2a)y^(-2b)dxdy from above. Let 0<nu<=1, 0<alpha<1, and H be even and C^(4,nu) on a neighborhood of[-1,1]. On0<y<=1, the homogeneous solution determined by H on y=1 is

h_hom(x,y)=y^(1/D) H(x y^(A/D)).

Differentiating this expression proves T h_hom=0; its value at y=1 is H(x). Extend evenly in x and oddly in y. Write

H(z)=H_0+H_2 z^2+H_4 z^4+R_H(z),
H_2=H''(0)/2, H_4=H''''(0)/24.

Taylor's theorem with a Holder fourth derivative gives

|R_H^(j)(z)|<=C|z|^(4+nu-j), j=0,...,4.

Therefore

h_hom=H_0 sgn(y)|y|^(1/D)+H_2 x^2 y
 +H_4 x^4 sgn(y)|y|^(beta_2)+R(x,y),
beta_2=(4A+1)/D=2-1/D,
q_nu=(1+(4+nu)A)/D.

On each quadrant, chain-rule differentiation gives for i+j<=3

|partial_x^i partial_y^j R(x,y)|<=C|x|^(4+nu-i)|y|^(q_nu-j).

For y!=0, the C^4 regularity of R_H already gives C^3 regularity across x=0; the displayed vanishing powers agree with those derivatives there. If q_nu>=2+alpha, derivatives through order2 extend across y=0 and are Holder with exponent alpha. Here are the details for the last assertion. Every second derivative is bounded by C|y|^alpha, and its first derivatives off y=0 are bounded by C|y|^(alpha-1) on a bounded box. Given two points at distance d, if either point has |y|<=2d then both have |y|<=3d and the second-derivative difference is bounded by Cd^alpha. Otherwise the segment between them stays at distance at least d from y=0, and the third-derivative estimate bounds the difference by Cd times d^(alpha-1). The same argument handles opposite sides of the axis. The lower derivatives extend by their vanishing bounds. Hence R is C^(2,alpha), including at equality q_nu=2+alpha.

The sufficient condition is exactly

nu>=2alpha+(1+alpha)/A.

It is not a necessary condition on an individual H, which may have a smoother or zero remainder. If a particular inhomogeneous solution is already C^(2,alpha), H_0=0, and the preceding trace hypotheses including q_nu>=2+alpha hold, then H_4 is the sole remaining obstruction among these displayed homogeneous terms: beta_2 lies strictly between1 and2, so x^4 sgn(y)|y|^(beta_2) is not C^2 at y=0 for any fixed x!=0 unless its coefficient vanishes. H_2 x^2 y is smooth. This conclusion is conditional on the regularity of the particular solution and the trace; it is not a Fredholm index calculation.

The need to control the particular solution is real. Direct differentiation gives

T(x^2 y log|y|)=D x^2 y.

Thus vanishing of a forcing on the y-axis alone does not ensure a C^2 particular solution. A separate exact resonance cancellation and a solved inhomogeneous problem are needed.

## The weight/trace arithmetic correspondence

With b=5/2+alpha and a=9/2+nu, direct substitution gives

delta=A(2alpha-nu)+1+alpha.

Hence delta<0 is equivalent to the strict inequality nu>2alpha+(1+alpha)/A. This numerical correspondence does not identify the two spaces: a monomial x^p y^q belongs locally to the weighted L^2 space near both faces exactly when p>a-1/2 and q>b-1/2. The equalities give logarithmic divergence. This can fail for every nu in the preceding correspondence, not just on delta=0. For example H(z)=|z|^(4+nu), with a harmless cutoff equal to1 near0, is even and C^(4,nu). Its homogeneous remainder is |x|^(4+nu)sgn(y)|y|^(q_nu). For a=9/2+nu the x exponent is exactly a-1/2; integrating its weighted square in x diverges logarithmically on every fixed interval0<y_1<y<y_2. Thus even delta<0 and the sufficient C^(2,alpha) trace condition do not embed the generic C^(4,nu) trace remainder into this weighted space. A positive x margin, extra vanishing, or a separate trace component is required.

The lead's example alpha=2/5, s=1701/500, b=3403/1000, a=1299/200 is only an algebraic feasibility point. Its inequalities and delta are checked separately against the exact normalized modal k, with A=2/k-1. No embedding theorem or global operator estimate follows from passing these rational inequalities. This is a separate general-weight point, not an example of a=9/2+nu,b=5/2+alpha from the preceding C^(4,nu) trace comparison: here a-9/2=399/200>1 and b!=5/2+alpha. The C^(4,nu) argument above is therefore not applied to this point. The independently executed evidence/feasibility_audit.json gives delta=-6254978666120071/403884010949762750, between -0.015487067 and -0.015487066; all six displayed feasibility margins are strictly positive.

## Axis equations and their hypotheses

Suppose a sufficiently differentiable reflection-equivariant field has expansions near the x-axis V_1=w(x)+O(y^2), V_2=mu(x)y+O(y^3). Then

(V dot grad-1)(y c(x))=y[w c'+(mu-1)c]+O(y^3).

Near the y-axis write V_1=x lambda(y)+x^3 lambda_3(y)+O(x^5), V_2=v(y)+x^2 v_2(y)+O(x^4), and h=x^2 e_2(y)+x^4 e_4(y)+O(x^6). Multiplication gives the two coefficients

x^2: v e_2'+(2lambda-1)e_2,
x^4: v e_4'+(4lambda-1)e_4+v_2 e_2'+2lambda_3 e_2.

Thus the jet system is triangular, not diagonal. If rho=x^2 y a with sufficient derivatives and W is a velocity with the same parity, direct product differentiation gives

partial_y(W dot grad rho)(x,0)=W_1(x,0)rho_xy(x,0)+partial_y W_2(x,0)rho_y(x,0),
(1/2)partial_x^2(W dot grad rho)(0,y)=2partial_x W_1(0,y)y a(0,y)+W_2(0,y)(y a)_y(0,y).

These are exact identities when the traces exist, not estimates that they are bounded in a proposed space.

For the exactly linear frozen center retain D=2A+1 and beta_2=(4A+1)/D. Here w=-Ax, mu=D, v=Dy, lambda=-A and v_2=lambda_3=0, so the homogeneous transport solutions are c(x)=x^2, e_2(y)=y and e_4(y)=y^(beta_2). At a source with w(P)=0,w'(P)!=0, the pure-transport exponent is (1-mu(P))/w'(P), equal to0 only when mu(P)=1. For an exact C^2 stationary background rho odd in y and reflection-equivariant C^2 field V satisfying V dot grad rho=rho, differentiation at y=0 gives w g'+(mu-1)g=0 with g=rho_y(x,0). At w(P)=0 and g(P)!=0 this proves mu(P)=1. The normalized numerical trial instead has a small nonzero mu(P)-1, so its transport exponent is not exactly0. The coupled source problem does not inherit a resonance pole from this scalar equation, as proved separately in ../source_pole/PROOF.md.

If at infinity w(x)/x and mu(x) tend to c_l=1/k, the leading transport exponent for c is k-1; if v(y)/y and lambda(y) tend to c_l, that for e_2 is k-2. Limits alone give logarithmic asymptotic growth x^(k-1+o(1)) or y^(k-2+o(1)), not a nonzero asymptotic coefficient without a rate of convergence. These statements are about the uncoupled scalar transport parts.

Finally, if on the whole positive y-axis the coupling vanishes, the forcing vanishes, v(y)>0, and v(y)/y tends to c_l>0, a nonzero homogeneous axis solution obeys h'=h/v. Integration gives h(y)=y^(k+o(1)) times a nonzero constant in logarithmic asymptotics. A bound |h(y)|<=C y^gamma with gamma<k therefore forces it to be zero. The positivity and limit hypotheses for the actual profile must still be proved, and are not supplied by sampled axis diagnostics.

## Resolved symbol observation and limits

On the x-face, an ordinary tangential covector xi dx and normal b covector sigma dy/y give the multiplier

m=y^2 xi^2/(y^2 xi^2+sigma^2).

At y=0,sigma=0,xi!=0, limits with different sigma/y disagree, so this face symbol has no continuous extension there. This does not exclude every resolved formulation. Blowing up a source point via x-x_*=r cos(theta),y=r sin(theta), a covector tau dr/r+omega dtheta has ordinary components r^(-1)(tau cos(theta)-omega sin(theta),tau sin(theta)+omega cos(theta)). Hence

m=(tau cos(theta)-omega sin(theta))^2/(tau^2+omega^2),

smooth down to r=0 away from the zero covector. Likewise

A(x-x_*)partial_x+y partial_y
 =(A cos^2(theta)+sin^2(theta))r partial_r+(1-A)sin(theta)cos(theta)partial_theta,
r^2 Delta=(r partial_r)^2+partial_theta^2.

These direct identities describe resolved symbols only. They prove no boundedness of the nonlocal operator on a weighted blow-up space, no normal-family inverse, and no matching with the proposed source disc.

## Scope

Confirmed model statements may be used only with their domains and hypotheses. Open items include global axis sign/zero counts, coefficient regularity for an unknown exact P_2 solution, trace and extension bounds, corner coupling, weighted compactness, adjoint estimates, index, nonlinear closure, and the decisive endpoint. The ordinary Sobolev disc at the source remains a design choice. No model calculation here proves a full IPM inverse or rejects an exact profile.
