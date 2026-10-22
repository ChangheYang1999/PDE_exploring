# A direct radial ODE certificate for the canonical velocity modes

## Statement and scope

Let -Delta psi=partial_x rho, U=(-psi_y,psi_x), and let f_n(r) be a radial forcing coefficient multiplying sin(l theta), l=2n>0. Assume the canonical Green moments converge and are regular at zero. Set t=log r and

 A(t)=r^{-l} integral_0^r s^{l+1} f_n(s)ds,
 B(t)=r^l integral_r^infinity s^{1-l} f_n(s)ds,
 P(t)=l psi_n(r)/r^2, R(t)=psi_n'(r)/r.

On any cell t=t_a+u, 0<=u<=h, suppose the forcing f(u)=f_n(exp(t_a+u)) is a specified finite sum of real exponential polynomials. Then P and R satisfy

 P'=-2P+lR, R'=lP-2R-f.                              (1)

The independent scalar variables q_+=P+R and q_-=P-R satisfy

 q_+'=(l-2)q_+-f, q_-'=-(l+2)q_-+f.                 (2)

These equations, with coherent initial data from the canonical moments, give a complete local certificate. A rigorous residual bound for any proposed polynomial approximation is given below. This is an analytic criterion and an arithmetic implementation test, not an acceptance of the current finite-annulus flow certificate. Actual forcing coefficients, initial anchors, candidate polynomials, all-mode/all-cell arithmetic, angular summation and field inequalities remain to be checked.

## Derivation from the canonical Green formula

The canonical radial formula is psi_n=(A+B)/(2l). Differentiation in t gives A'=-lA+r^2 f_n(r), B'=lB-r^2 f_n(r). Hence psi_n'(r)=(B-A)/(2r). Consequently

 P=(A+B)/(2r^2), R=(B-A)/(2r^2),
 q_+=B/r^2, q_-=A/r^2.

The product rule yields (1) and (2), including both forcing signs. The n=1 plus equation has zero growth coefficient. The minus equation has coefficient -(2n+2), whose magnitude can exceed2N even when the original certificate assumes2Nh<=1. No such small-step assumption is required by the criterion here; exponentials are enclosed directly.

In the trial representation rho=x^2y sum a_m(r)cos(2m theta), an input term a_m=e^{alpha u}T_m(u) produces

 f(u)=exp(2t_a) exp((alpha+2)u) F_n(u),

where F is the finite angular derivative map. The plus2 exponent, not plus4, is the forcing exponent in (2). The plus4 exponent belongs to r^2 f in the original A/B equations. Confusing these changes the ODE. Verification of the finite angular map is a separate dependency; no modal truncation is silently added here.

## A scalar defect theorem

Let q'=lambda q+g on [0,h], with real constant lambda and continuous g. Let p be any continuously differentiable approximate solution and |q(0)-p(0)|<=epsilon_0. Define the signed defect d=g+lambda p-p'. Suppose

 |d(u)|<=sum_{j=0}^J D_j u^j, D_j>=0.                (3)

For j>=0 define the positive moment

 J_j(lambda,t)=integral_0^t exp(lambda(t-u))u^j du.

Variation of constants, proved by multiplying q-p by exp(-lambda t) and integrating, gives the pointwise bound

 |q(t)-p(t)|<=epsilon_0 exp(lambda t)
                  +sum_j D_j J_j(lambda,t).           (4)

Each J_j is increasing in t. To see this, substitute v=t-u: for j=0 its derivative is exp(lambda t)>0; for j>=1 differentiate integral_0^t exp(lambda v)(t-v)^j dv to obtain j J_{j-1}>0. Therefore a uniform bound on the cell is

 E=epsilon_0 exp(max(lambda,0)h)+sum_j D_j J_j(lambda,h). (5)

No sign restriction on lambda is used. Initial uncertainty must not be discarded even for a stable minus equation. If g is known only within a forcing enclosure, (3) must include its full radius and truncation error.

Apply this theorem separately to (2), using g=-f and g=+f. If their polynomial approximations are p_+,p_- with errors E_+,E_-, then (p_++p_-)/2 and (p_+-p_-)/2 approximate P and R with uniform errors at most(E_++E_-)/2. Correlation between the two errors is not required for this upper bound.

## Exact construction of a defect majorant

For one forcing term exp(gamma u) C(u), C=sum_{k=0}^d c_k u^k, and integer Q>=d, its Taylor coefficient through degree Q is

 f_j=sum_{k=0}^{min(j,d)} c_k gamma^{j-k}/(j-k)!.

Taylor's integral remainder for the exponential, or j-fold integration of its derivative, gives on[0,h]

 |exp(gamma u)C(u)-sum_{j=0}^Q f_j u^j|
 <=u^{Q+1} exp(max(gamma,0)h)
       sum_{k=0}^d |c_k| |gamma|^{Q+1-k}/(Q+1-k)!.     (6)

This holds for either sign of gamma. Sum over the finite forcing terms, including any multiplicative exp(2t_a), to obtain T_Q u^{Q+1}. Interval coefficient uncertainty is enclosed term by term before taking absolute values.

For an exact rational candidate p=sum_{j=0}^Q p_j u^j, set p_{Q+1}=0. The defect polynomial coefficients are f_j+lambda p_j-(j+1)p_{j+1}. Their absolute interval upper bounds supply D_j, j<=Q; D_{Q+1}=T_Q. Formula(4) then gives a complete enclosure without assuming p was computed by a correct recurrence. In particular it can independently check a candidate produced by the A/B algorithm.

If a candidate Taylor model is p(u)+[-sum rho_j u^j-rho_*,sum rho_j u^j+rho_*], all rho_j,rho_*>=0, it contains the true scalar solution whenever the right side of(4) is<=sum rho_j u^j+rho_* for everyu in[0,h]. A sufficient, conservative test is E<=rho_0+rho_*. Alternatively the pointwise comparison can be certified on subintervals. Mere agreement at sample points or overlap of coefficient intervals is insufficient.

## Two independent moment evaluations

For lambda=0, J_j(0,h)=h^{j+1}/(j+1). For lambda!=0, integration by parts gives

 J_0=(exp(lambda h)-1)/lambda,
 J_j=(j J_{j-1}-h^j)/lambda, j>=1.                    (7)

This recurrence can involve cancellation, so all operations must carry interval radii. Independent expansion of the exponential inside the integral, justified by uniform absolute convergence on the compact interval, gives

 J_j(lambda,h)=h^{j+1} j! sum_{k=0}^infinity (lambda h)^k/(j+k+1)!. (8)

For a truncation after K, let z=|lambda h|, assume z/(j+K+3)<1, and bound the absolute remainder by

 h^{j+1} j! z^{K+1}/(j+K+2)! / (1-z/(j+K+3)).          (9)

Indeed this is the first omitted absolute term times a geometric ratio bound for every later term. For negative lambda the partial sum is signed but the absolute remainder remains valid. If lambda,h are rational, (8)-(9) produce exact rational endpoints. For z=0 use the exact zero-lambda result, avoiding0^0. Positivity of J follows directly from the integral, and the general upper bound is

 0<J_j(lambda,h)<=exp(max(lambda,0)h) h^{j+1}/(j+1).

## Verification obligations and scope

The checker will use n in{1,2,20,100,261}, both scalar branches, h in{1/1044,1/522}, j in{0,1,2,12,13}. These are 100 exact rational illustrative cases testing signs, the zero mode, stable and unstable growth, and high Taylor orders. Primary Arb512 and mpmath.iv180 use (7). A separate exact rational series program uses (8)-(9) through K=300, imports neither the primary checker nor the producer, and checks full containment inside the primary enclosures. This is not an all-cell audit. The primary identity checks reconstruct the moment equations and canonical signs symbolically.

Dependencies: only the proved canonical Green formula and finite forcing representation stated here. Source implementation inspected: research/flow_certificate/evidence/source/cert_flow.py and cert_resid.py. The actual finite-annulus comparison remains OPEN until exact data and complete coverage are supplied. This proof precedes the new checker.
