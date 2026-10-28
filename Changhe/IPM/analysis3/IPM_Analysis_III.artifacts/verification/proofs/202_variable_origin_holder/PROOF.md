# A Holder inverse for the localized variable origin operator

## Statement and domain

Fix 0<alpha<1, A0>0 and D0=2A0+1. Let V be C3 on a disk B_(delta0), with V1 odd in x and even in y, and V2 even in x and odd in y. Assume

 DV(0)=diag(-A0,D0).

Division by the axes defines C2 functions A,D, even in both variables, by

 V1=-x A(x,y), V2=y D(x,y), A(0)=A0, D(0)=D0.

Let rho be C4 on that disk, even in x and odd in y, with rho(0,y)=0 and rho=x^2y+O(r^4). Choose a fixed smooth cutoff chi, invariant under both reflections, equal1 on B_(1/2) and supported in B1. For sufficiently small delta>0 set

 A_delta=A0+chi(X/delta)(A-A0),
 D_delta=D0+chi(X/delta)(D-D0),
 V_delta=(-x A_delta,y D_delta).

These are defined by their constant values outside B_delta. Use the Banach space E_p of bounded continuous functions, even in x and odd in y, with h(0,y)=0 and norm

 ||h||_(E_p)=||h||_infinity+[h]_x+[h]_(y,p),
 [h]_x=sup |h(x,y)-h(x',y)|/|x-x'|^alpha,
 [h]_(y,p)=sup |h(x,y)-h(x,y')|/(|x|^p |y-y'|^alpha).

Take 1<=p<2 with

 1+p A0-alpha D0>0.                                  (1)

The canonical full-plane velocity U and the raw strain c are those of topics199-201. Define

 L_delta h=V_delta.grad h-h
              +chi(X/delta)(U[h]+c[h]X/3).grad rho.  (2)

Its domain is the maximal distributional domain

 D_delta={h in E_p:V_delta.grad h-h belongs to E_p}.

There is delta_*>0, depending only on alpha,p,A0,D0, the stated local norms of V,rho, and chi, such that every 0<delta<delta_* makes L_delta:D_delta->E_p a closed bijection with bounded inverse. The inverse norms in E_p are bounded uniformly as delta tends to0. For every alpha<1 there is p in[1,2) satisfying(1).

On B_(delta/2) this operator equals the actual variable transport V.grad-1 plus the full normalized coupling. Outside B_delta the transport is replaced by its origin linearization and the coupling is zero. The velocity inside the coupling is still the canonical velocity of the whole-plane input h. This is a theorem for this explicitly defined whole-plane extension, with no boundary condition on a disk. It is not an inverse for the original full-plane operator, does not close the cubic normalization, and proves no nonlinear existence assertion. No usable numerical value of delta_* or inverse constant is certified here.

## Axis division and the time parameter

The identities

 A(x,y)=-integral_0^1 partial_x V1(sx,y)ds,
 D(x,y)= integral_0^1 partial_y V2(x,sy)ds

prove C2 regularity and both even parities. Their first derivatives vanish at0. On a fixed smaller disk Taylor's theorem therefore gives

 |A-A0|+|D-D0|<=C r^2,
 |grad A|+|grad D|<=C r.

After the cutoff extension, the deviations have supremum O(delta^2) and first derivatives O(delta), with constants independent of delta. Shrink delta so that A_delta>=A0/2 and D_delta>=D0/2. Put

 q0=1/A0, beta0=D0/A0,
 q_delta=1/A_delta=q0+m_delta,
 beta_delta=D_delta/A_delta,
 v_delta(x,y)=beta_delta(x,y)y,
 W_delta=-x partial_x+v_delta partial_y,
 S_delta=W_delta-q0.

Both m_delta and beta_delta-beta0 are supported in B_delta, are even in both variables, have supremum O(delta^2), and have first derivatives O(delta). In particular

 L=sup_(R^2) partial_y v_delta <= beta0+C delta^2,
 Lx=sup_(R^2)|partial_x v_delta|<=C delta^2.           (3)

We may take L>0. The key feature is that the flow of W_delta has x coordinate e^(-t)x independent of the initial y. This is a change of time along trajectories, not a change of spatial coordinates or a norm-transfer assertion.

## A direct characteristic estimate

We prove a more general estimate using only q0>0, p>0, L>0, Lx<infinity, and the fact that v_delta-beta0 y is supported in B_delta. Suppose

 kappa=q0+p-alpha L>0.                               (4)

The vector field W_delta is globally C1 and Lipschitz, with at most linear growth, so its flow is complete. Write

 Phi_t(x,y)=(e^(-t)x,Y_t(x,y)),
 R_delta f=-integral_0^infinity e^(-q0 t)f(Phi_t(x,y))dt. (5)

The integral converges uniformly for bounded f. Reflection symmetry preserves the parities, and f(0,y)=0 gives R_delta f(0,y)=0. Its supremum is at most ||f||_infinity/q0.

Since partial_y Y_t=exp(integral_0^t partial_y v_delta(Phi_s)ds), the y flow is Lipschitz with constant e^(Lt). At fixed x, the weighted y difference of the integrand is thus bounded by

 [f]_(y,p)|x|^p exp((-p+alpha L)t)|y-y'|^alpha.

Consequently

 [R_delta f]_(y,p)<=[f]_(y,p)/kappa.                  (6)

To control the x difference, first consider two nonnegative initial x values a,b with a>=b>=a/2 and d=a-b>0. Put

 t0=max(0,log(a/(2delta))).

For every initial lambda between b and a, the trajectory x_s=e^(-s)lambda remains outside |x|<delta when 0<=s<t0. On that interval v_delta=beta0 y and partial_x v_delta=0. Differentiation of the y equation in lambda gives

 d_t(partial_lambda Y_t)
   =(partial_y v_delta)(Phi_t) partial_lambda Y_t
      +(partial_x v_delta)(Phi_t)e^(-t),
 partial_lambda Y_0=0.

It follows that the derivative is zero for t<t0 and, for t>=t0,

 |partial_lambda Y_t|
 <=Lx integral_(t0)^t e^(L(t-s))e^(-s)ds
 <=[Lx/(L+1)]e^(Lt)e^(-(L+1)t0).                     (7)

Integrating this bound in lambda controls |Y_t(a,y)-Y_t(b,y)| by d times its right side. Split the forcing difference as an x difference at fixed y, followed by a y difference at fixed x. The former contributes at most

 [f]_x d^alpha/(q0+alpha)

to(5). For the latter, use (b e^(-t))^p<=a^p e^(-pt), the y seminorm of f and(7). Dividing by d^alpha and integrating from t0 gives at most

 [f]_(y,p) [Lx/(L+1)]^alpha
       a^p exp(-(q0+p+alpha)t0)/kappa.

The cancellation of L in the final exponent is exact: alpha(L+1)+kappa=q0+p+alpha. Moreover

 a^p exp(-(q0+p+alpha)t0)<=(2delta)^p.                (8)

For a<=2delta this is immediate. For a>2delta it follows by substituting t0=log(a/(2delta)); the remaining power of a is -q0-alpha<0. Thus this bound is uniform even for initial x far outside the cutoff.

For noncomparable nonnegative a,b, say a>2b, d=a-b>=a/2. The axis condition and the x seminorm give |f(x,y)|<=[f]_x |x|^alpha, hence

 |R_delta f(x,y)|<=[f]_x |x|^alpha/(q0+alpha).

The sum of the endpoint bounds divided by d^alpha is at most 3[f]_x/(q0+alpha), because a<=2d, b<d, and 2^alpha+1<3. Evenness in x reduces opposite-sign pairs to their absolute values and cannot increase this difference quotient. Combining the cases yields

 [R_delta f]_x<=3[f]_x/(q0+alpha)
       +[f]_(y,p) [Lx/(L+1)]^alpha(2delta)^p/kappa.   (9)

The estimates also show continuity. For the sum norm they imply

 ||R_delta||_(E_p->E_p)<=C_R,
 C_R=max(1/q0, 3/(q0+alpha),
             (1+[Lx/(L+1)]^alpha(2delta)^p)/kappa).  (10)

No derivative of f is used in(6) or(9).

## Maximal-domain inversion

Let D(S_delta)={h in E_p:S_delta h in E_p distributionally}. Formula(5) solves S_delta R_delta f=f: this follows by differentiating the integral along a characteristic, or first testing the integral against a compactly supported smooth function and changing variables by the C1 flow. The exponential decay and boundedness justify the limit at infinite time.

Conversely, any bounded continuous distributional solution of S_delta h=0 satisfies h(Phi_t X)=e^(q0 t)h(X). To justify the characteristic identity for distributional solutions, use a local C1 flow box away from stationary points and the one-dimensional distributional fundamental theorem along its time coordinate. The identity extends to all nonstationary points by continuity. At a stationary point S_delta h=0 imposes -q0 h=0 by the continuous inhomogeneous characteristic identity, equivalently by taking nearby nonstationary points and a fixed time. Thus boundedness as t tends to infinity gives h=0 everywhere. The same argument proves the inhomogeneous characteristic identity. This shows bijectivity on exactly D(S_delta).

The graph is closed: convergence in E_p implies local uniform convergence, and application of the C1 differential expression is continuous into distributions. If both h_n and S_delta h_n converge in E_p, their limits satisfy the same distributional equation. These facts and(10) prove the claimed closed inverse. No strong continuity of the flow in the large Holder norm is assumed.

## Multiplication by the varying coefficient

We record why the variation of q can be treated in the same space. Suppose m is supported in B_delta, ||m||_infinity<=C0 delta^2 and ||Dm||_infinity<=C1 delta. Interpolating its supremum and Lipschitz bounds directly by splitting differences at delta gives [m]_alpha<=C delta^(2-alpha). Thus

 ||mh||_infinity<=C delta^2||h||_infinity,
 [mh]_x<=C delta^2[h]_x+C delta^(2-alpha)||h||_infinity.

For a y difference, the term in which h is differenced is bounded by C delta^2[h]_(y,p)|x|^p|y-y'|^alpha. In the other term, choose the product-difference identity so that the undifferenced h is evaluated at a point where m is supported. At that point |y|<=delta, so oddness gives |h(x,y)|<=[h]_(y,p)|x|^p delta^alpha. The alpha difference bound for m then gives the same upper bound. Consequently

 ||mh||_(E_p)<=C_M delta^(2-alpha)||h||_(E_p).         (11)

This proves the multiplier bound for m_delta. In particular multiplication by q_delta has norm at most q0+C_M delta^(2-alpha), uniformly bounded as delta tends to0. Multiplication by A_delta and its reciprocal also preserves E_p; apply the same argument to their constant parts and deviations.

The transport T_delta=V_delta.grad-1 satisfies

 T_delta=A_delta(S_delta-m_delta).                    (12)

By the multiplier statements, its maximal E_p domain equals D(S_delta). The point is algebraic and distributional: S_delta h=q_delta T_delta h+m_delta h, and the converse identity is(12). There is no assertion that V_delta-V(0)'X is a bounded first-order perturbation in E_p.

## Adding the full normalized coupling

Write B_delta h=chi(X/delta)(U[h]+c[h]X/3).grad rho. Topics199-201 prove, on exactly E_p,

 ||B_delta||<=C_B delta^(2-p)+C_c C_H delta^(3-p-alpha),
 C_c=(4/pi)max(1,1/(p+alpha-1)).                      (13)

The first term uses the directional y Holder estimate of U1/x; the second is the strain column. Their derivations need only the stated C4 background. The canonical strain identity and the zero cubic leading coefficient remain valid for these Holder inputs by proof 201.

Combining(12)-(13) gives, on D(S_delta),

 L_delta=A_delta[S_delta+E_delta],
 E_delta=-m_delta+q_delta B_delta.

This perturbation is bounded on E_p, and

 ||E_delta||<=C_M delta^(2-alpha)
   +(q0+C_M delta^(2-alpha))
        [C_B delta^(2-p)+C_c C_H delta^(3-p-alpha)].   (14)

If C_R times the right side of(14) is less than1, the norm-convergent Neumann series gives

 L_delta^(-1)
    =R_delta(I+E_delta R_delta)^(-1)q_delta,
 ||L_delta^(-1)||<=C_R||q_delta||/(1-C_R||E_delta||).

This proves injectivity, surjectivity into the maximal domain and closedness. Adding B_delta does not change that domain, because B_delta is bounded E_p->E_p.

Condition(1) means kappa0=q0+p-alpha beta0>0. Equations(3)-(4) give kappa>=kappa0/2 for small delta. Hence C_R is uniformly bounded. All powers on the right side of(14) are positive: 2-alpha>0, 2-p>0, and 3-p-alpha=(2-p)+(1-alpha)>0. Shrinking delta therefore makes the Neumann condition hold. Finally (D0 alpha-1)/A0<2 for alpha<1, so some p in[1,2) satisfies(1).

## Applicability to the exact modal trial and limits

The exactly joined normalized modal density of proof 04 is C4,1 near0 by proof 33. Its canonical velocity is C3 there. This last fact follows without a global regularity assumption: cut off the density on a fixed small disk; its compact C4,1 part has third derivatives in C^alpha for every alpha<1, and the mean-zero order-zero kernels give local C^alpha estimates after commuting those derivatives. The separated remainder of the velocity is smooth near0, since its differentiated kernels are integrable against the sublinear modal tail. Thus U, and hence V=ell X+U, are C3 locally. Axis parity and the exact scalar normalization give DV(0)=diag(-(2ell-1),4ell-1), with ell>1/2 independently certified in proof 04. The hypotheses above therefore apply to that precise trial.

The theorem replaces the unproved conjugacy transfer with a direct estimate in the original E_p coordinates. Its scope is still local in the operator coefficients: outside B_delta the source point and actual far transport have been removed by definition. A solution of L_delta h=f is an input to a possible localization argument, not a solution of the original full-plane linearized problem. Compatibility between these local inverses and the other regions, a closed cubic trace, control of the moving tail, and nonlinear closure remain separate obligations. In particular the actual low injectivity(I) and nonlinear smallness(S) remain OPEN.

Dependencies: proof 01 for normalized signs and the origin matrix; topics04 and33 for the precise modal trial; topics199-201 for the bounded normalized coupling and strain. The variable characteristic estimate and all domain and multiplier steps are proved here. An independent cross-audit is requested.
