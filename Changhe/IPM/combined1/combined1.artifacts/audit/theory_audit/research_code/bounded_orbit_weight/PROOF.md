# Necessary orbit budgets and a compact Lipschitz weight

Theorem A audits Proposition L3 of the frozen T2 note and is CONFIRMED, with the smooth-test approximation made explicit. Section B refutes the claim that the same necessity applies to an arbitrary auxiliary majorant. Theorem C repairs the compact-support construction under a quantitative exterior hypothesis and is OPEN pending independent Opus review.

## A. The necessary budget uses the actual principal coefficient

Work on the real S1 subspace of L2(R2), consisting of functions even in x and odd in y. Let

    A h = V.grad h - h + grad rho.U[h],
    U[h]=(-R1 R2 h,R1^2 h), Rj=partial_j(-Delta)^(-1/2).

Assume V is a globally Lipschitz reflection-equivariant vector field with div V=2c. Assume rho is C1, belongs to S1, and has bounded uniformly continuous gradient. Let

    theta=(|grad rho|-rho_y)/2.

Let psi be bounded, locally Lipschitz and even in both variables, and let g=V.grad psi belong to L infinity. Set w=exp(psi). Suppose every compact smooth S1 test satisfies

    <Ah,w^2 h> <= -beta ||wh||_2^2.

Then

    g >= theta-lambda almost everywhere, lambda=1+c-beta.       (A1)

Consequently for every X and T>=0,

    psi(Phi_T X)-psi(X)
      >= integral_0^T [theta(Phi_t X)-lambda]dt,                 (A2)

where Phi is the complete flow of V. In particular

    osc psi >= sup_(X,T>=0) integral_0^T [theta(Phi_t X)-lambda]dt. (A3)

### Proof

Fix a Lebesgue point X0 of g away from the axes. Choose a unit vector xi maximizing the quadratic principal symbol at X0. With a=rho_x and b=rho_y, its matrix is

    M=[[-b,a/2],[a/2,0]], lambda_max(M)=theta.

For a smooth amplitude phi supported near X0 use phi cos(n xi.X) and its four reflected copies with S1 signs. For every L2 amplitude q and every bounded degree-zero multiplier m continuous at plus and minus xi, its action on q exp(plus or minus i n xi.X) differs in L2 from multiplication by m(plus or minus xi) by a quantity tending to zero. This is dominated convergence after translating the Fourier variable. It applies to the Riesz products defining U, with amplitudes phi and w phi.

The weighted transport identity contributes exactly -integral(1+c+g)w^2 h^2. The even multiplier of U has the same value at xi and -xi. The coupling contribution therefore tends to its local quadratic-symbol integral. Reflection equivariance makes all four contributions identical after change of variables. The oscillating double-frequency terms vanish by the Riemann-Lebesgue lemma. Dividing by the norm gives the necessary inequality

    integral w^2 phi^2 [xi^T M xi-g] / integral w^2 phi^2 <= lambda.

To shrink the support, choose a fixed nonzero smooth bump and rescale it about X0. Lebesgue differentiation for g and continuity of w,M give theta(X0)-g(X0)<=lambda. This keeps every original test smooth; the indicator used in the T2 sketch is unnecessary. Almost every point is such a Lebesgue point, proving (A1). This argument also explains why the conjugation commutator has zero packet limit without being Hilbert-Schmidt.

The locally Lipschitz chain rule and preservation of null sets by the Lipschitz flow imply (A2) for almost every starting X and each fixed T. Both sides of (A2) are continuous in X: psi and the flow are continuous, and theta is continuous. Hence the inequality extends to every X. One can first use rational T and then continuity in T to obtain all T simultaneously. Taking the supremum proves (A3). This does not extend the integral identity involving an arbitrary measurable representative of g to exceptional orbits.

## B. An auxiliary majorant has no universal necessary budget

The assumption theta<=theta_c+theta_1 is useful for a sufficient estimate. It does not identify theta_1 with the actual principal coefficient in Theorem A. The last paragraph following Lemma L4 in the frozen T2 note applies L3 with theta_1 substituted for theta and claims that this orbit cost cannot be avoided by any multiplier weight. That inference is false without a further hypothesis.

For an explicit example take rho=0 and V=cX with c>0. Then theta=0, and psi=0 gives the exact rate beta=1+c. Choose any nonnegative smooth radial bump theta_1 supported in an annulus, with value greater than a fixed lambda>0 on an open subannulus. The decomposition 0<=0+theta_1 holds. A radial orbit spends a positive interval in that subannulus, so its theta_1-lambda budget is strictly positive. Nevertheless the zero weight already gives a better rate than 1+c-lambda, at zero oscillation cost.

More generally, for any fixed background one can enlarge theta_1 without changing the actual operator or its unweighted energy rate. Thus a necessity statement cannot grow arbitrarily with the chosen majorant. The corrected statement is: the theta_1 budget is the minimum oscillation among weights satisfying the chosen stronger barrier V.grad psi>=theta_1-lambda. It is not a necessary cost for all weights realizing a prescribed operator rate.

## C. Quantitative repair of the compact-support construction

Let V be globally Lipschitz with Lipschitz constant L, V(0)=0, reflection equivariance, and

    V(X).X >= m |X|^2 for every X, m>0.

Let theta_1 be bounded, globally Lipschitz, nonnegative and even in both variables. Fix 0<r1<r2, lambda>0 and delta>0 such that

    theta_1(X) <= lambda-delta whenever |X|<=r1 or |X|>=r2.     (C1)

Set

    f=theta_1-lambda,
    H=max(0,sup f), T_ann=log(r2/r1)/m,
    C=H T_ann, R=r2 exp(L C/delta), T_*=log(R/r1)/m.

Define

    psi(X)=sup_(tau>=0) integral_(-tau)^0 f(Phi_t X)dt.          (C2)

Then psi is finite, even and globally Lipschitz, vanishes for |X|<=r1 and |X|>=R, and

    0<=psi<=C,
    Lip(psi)<=Lip(theta_1)(exp(L T_*)-1)/L.                    (C3)

Its oscillation equals the orbit budget

    osc psi = sup_(X,T>=0) integral_0^T f(Phi_t X)dt.           (C4)

Along every orbit W(t)=psi(Phi_t X) is locally Lipschitz and obeys, almost everywhere in t,

    W'=f(Phi_t X) when W>0,
    W'=max(0,f(Phi_t X)) when W=0.                            (C5)

Thus g=V.grad psi is bounded and g>=theta_1-lambda almost everywhere in X. The same construction supplies the finite inputs required by the symmetric coupling proposal T4-163:

    ||psi||_2 <= C sqrt(pi(R^2-r1^2)),
    ||grad psi||_2 <= Lip(psi) sqrt(pi(R^2-r1^2)).              (C6)

These constants can be very conservative. No candidate bound follows without verifying every hypothesis and evaluating the resulting costs.

### Proof

Global Lipschitzness gives a complete flow and |V(X)|<=L|X|. Every nonzero orbit has

    m <= d/dt log|Phi_t X| <= L.

It crosses the annulus at most once, spending at most T_ann there. All positive values of f occur in that annulus. The integral over any orbit segment is therefore at most C, proving finiteness and the first bound in (C3). For |X|<=r1 the entire past orbit is in the inner region where f<=-delta, so the supremum is zero.

Once an orbit exits at radius r2, its accumulated positive workload is at most C. Further motion has f<=-delta, so after time C/delta all integrals ending there are nonpositive, and the workload is zero. The radial upper growth bound shows that |X|>=R implies at least that much time has passed since the exit. Hence psi vanishes outside radius R.

For r1<=|X|<=R, any maximizing segment may start no earlier than the first crossing of radius r1: deleting the preceding portion with f<=-delta only increases its integral. The time since that crossing is at most T_*. For points outside this compact annulus the workload is zero and every segment integral is nonpositive. Therefore on the whole plane the supremum in (C2) equals the maximum over the common finite window 0<=tau<=T_*.

For two starting points X,Y, backward flow Lipschitzness gives |Phi_(-s)X-Phi_(-s)Y|<=exp(Ls)|X-Y|. Each integral over that fixed window consequently has Lipschitz constant at most Lip(theta_1) integral_0^T_* exp(Ls)ds. A supremum of functions with this common constant has the same constant, proving (C3). Reflection symmetry of V and theta_1 proves evenness.

Every forward segment can be viewed as a past segment ending at its terminal point, and conversely. Thus sup psi equals the right side of (C4). Since psi is zero on the inner ball, its infimum is zero and (C4) follows.

For h>=0, splitting a past segment at time zero gives the exact dynamic identity

    W(h)=max(W(0)+integral_0^h f(Phi_t X)dt,
             sup_(0<=s<=h) integral_s^h f(Phi_t X)dt).

Because f along the orbit is continuous, this is the usual reflected integral at zero. On an open interval where W>0 its derivative is f; at almost every point where W=0 the derivative is max(0,f). Equivalently one can take difference quotients in the displayed identity at points where W is differentiable. This proves (C5). The locally Lipschitz chain rule identifies this orbit derivative with V.grad psi at almost every spatial point and yields |g|<=||f||_infinity. Finally the support and the pointwise bounds imply (C6).

Dependencies are the complete Lipschitz flow, elementary Fourier packet localization for Theorem A, the Sobolev chain rule, Lebesgue differentiation, and elementary maximum-of-integrals identities. No numerical computation is involved. The strict uniform exterior margin in (C1), absent from the original compact-support assertion, is essential to the finite support argument.
