# Direct curl-ratio asymptotics for the flat rotating carrier

Status: LIT304 and the exact stated generalization CONFIRMED A2508-A2511, after the complete eight-item existing coordinator comparison. Broader conclusions OPEN A2512. No full Euler or pressure conclusion is asserted.

## 1. Exact theorem and dependencies

Fix 0<c<1/2, omega in R, Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J and a=1-2c. Let sigma be a smooth section on a planar disc centred at zero, with sigma(0)!=0 and det(sigma_1,sigma_2,X(sigma)) nonzero. All assertions are local after shrinking this disc and a finite flowbox about it.

Let g:(0,R)->(0,infinity) be smooth and nondecreasing, with g^(k)(r)=O(r^N) as r tends to zero for every pair of nonnegative integers k,N. Suppose

    ell(r)=r g'(r)/g(r) -> infinity.                         (1)

Define the exact Volterra carrier in Section2. Then its zero set is the central X orbit, it is smooth and flat there, and there are constants 0<K1<=K2<infinity and r1>0 such that both section ratios

    Q1(y)=|(W.X)(sigma(y))|/|V(sigma(y))|,
    Q2(y)=|W(sigma(y))|/|V(sigma(y))|, W=curl V,

satisfy

    K1 ell(|y|)/|y| <= Qj(y) <= K2 ell(|y|)/|y|              (2)

for 0<|y|<r1, j=1,2. Constants may depend on the fixed geometry and on the chosen radial factor. There is no assertion of uniform constants over unbounded omega.

In particular neither ratio can be bounded by B2+C0/|y| on any centre disc for B2 nonnegative in L2 and finite C0>=0. This conclusion follows directly from (2), independently of any continuation theorem. For g(r)=exp(-t log t), t=log(1/r), formula (2) is precisely LIT304, with ell=log t+1. Each ratio is then in every Lp, 0<p<2, but no L2.

The more general g from the arbitrary-envelope proof has ell=Lambda(t)->infinity. Once its independently checked construction is confirmed, (2) gives its actual lower ratio too, without relying on the endpoint criterion for non-L2. No equation for S or P is a premise or conclusion here.

Dependencies are smooth differentiation, the inverse function theorem, elementary integration and the exact local carrier construction already established in A2482-A2483. The needed construction identities and the full leading-term calculation are supplied below.

## 2. Complete carrier construction and elementary derivative bounds

On a relatively compact disc put

    m=|X(sigma)|, beta_i=X(sigma).sigma_i/m^2,
    T_i=sigma_i-beta_i X(sigma), G_ij=T_i.T_j,
    j=|det(sigma_1,sigma_2,X(sigma))|=m sqrt(det G),
    M=G/j, b=(3c-1)beta.

The capital G in this proof is the two-dimensional metric matrix. Transversality makes G and M positive definite and m,j positive. Their coefficients and fixed-order derivatives are bounded, and the relevant least eigenvalues and positive functions have positive lower bounds on the closed smaller disc.

Write y=r e_r, e_r=(cos theta,sin theta), e_theta=(-sin theta,cos theta), and b_r=b.e_r, b_theta=b.e_theta. Define

    q(r,theta)=r^-1 integral_0^r s b_theta(s,theta)g(s)
                      exp(integral_s^r b_r(u,theta) du) ds,
    w=g e_theta+q e_r.                                     (3)

Monotonicity of g and bounded coefficients give, with fixed constants,

    |q|<=C r g, |q_theta|<=C r g,
    q_r=b_r q+b_theta g-q/r, |q_r|<=C g.                    (4)

Every angular derivative of q is O(rg), since derivatives of the exponential kernel are bounded combinations of integrals of bounded coefficient derivatives. Repeated radial differentiation of the displayed differential equation proves that every fixed mixed derivative of q tends to zero faster than every power: the induction uses the assumed derivative flatness of g and only fixed powers of 1/r. Cartesian derivatives introduce further fixed powers of 1/r and bounded angular factors. Thus w extends smoothly and flatly at zero. Difference quotients verify the derivatives of the extension, as in A2482. Its tangential component g is positive off zero, so w has no other zero. Also

    g<=|w|<=C g, |D(q e_r)|<=C g,
    |Dw|<=C(g'+g/r+g), div w=b.w.                           (5)

The last identity is (r q)'/r=b_r q+b_theta g.

Set v=w/j, h=-beta.v. On a sufficiently small product flowbox define

    Phi(y,s)=exp(sA)sigma(y),
    V(Phi(y,s))=exp(-s)D Phi(y,s)(v(y),h(y)).                (6)

Its coordinate components are exp(-s)(v,h), so [X,V]=-V and DV X=(A-I)V=-LV. Conformality of exp(sA) transports the zero scalar X.V from the section, where it is m^2(beta.v+h)=0. The coordinate volume density is exp(3cs)j, so

    div V=exp(-s)j^-1[div(jv)+(3c-1)jh]
         =exp(-s)j^-1[div w-b.w]=0.

This verifies all three carrier equations. Formula (6) and the invertible coordinate changes preserve smooth flatness and the exact central-orbit zero set. On the section V=T_i v_i, giving

    c1 g<=|V(sigma)|<=c2 g,
    |W(sigma)|<=C(|Dw|+|w|).                               (7)

The second estimate follows by differentiating (6) once: derivatives in s contribute bounded matrices multiplying v,h; derivatives in y contribute at most Dw and w.

## 3. Positive leading term in the pulled-back curl

Let u_i=V(sigma).sigma_i and regard u_i dy_i as a one-form. Since V is orthogonal to X, u=Gv=Mw. By (5), D(q e_r)=O(g). In contrast,

    D(g e_theta)=g' e_theta tensor e_r+g D e_theta,
    |D e_theta|<=C/r.

Differentiating M supplies O(g), while the second term supplies O(g/r). Consequently, uniformly in theta,

    partial_1 u_2-partial_2 u_1
      =g'[e_r1(M e_theta)_2-e_r2(M e_theta)_1]+O(g/r)
      =g' e_theta^T M e_theta+O(g/r).                       (8)

The last equality uses e_theta=(-e_r2,e_r1). Because M is symmetric positive definite, its coefficient is bounded below by a fixed mu0>0. Writing g'=ell g/r, choose r1 so that ell is large enough to absorb the absolute error constant in (8). Then

    c3 ell g/r<=partial_1 u_2-partial_2 u_1<=c4 ell g/r      (9)

on 0<r<r1. The lower bound is positive, not a sign-indefinite estimate. In particular an O(g/r) remainder cannot cancel the leading term once ell tends to infinity. The radial correction is only O(g) after one derivative, so it creates no competing g' term.

## 4. Exact conversion to the actual three-dimensional curl

Differentiate X.V=0 to get DV^T X=-A^T V. The component identity

    X cross W=DV^T X-DV X

therefore gives X cross W=(L-A^T)V=aV. Solving for W yields

    W=(W.X)X/m^2+a(V cross X)/m^2                           (10)

on the section. The sign is fixed by X cross (V cross X)=m^2 V, since X.V=0.

The exterior derivative of the pulled-back velocity form is the pulled-back curl two-form. Thus, if epsilon is the fixed determinant orientation,

    partial_1 u_2-partial_2 u_1
      =W.(sigma_1 cross sigma_2)
      =epsilon j(W.X)/m^2
           +a(V cross X).(sigma_1 cross sigma_2)/m^2.        (11)

The final term is O(|V|)=O(g), with a geometry-dependent constant. The multiplier m^2/j is bounded above and below by positive numbers. Equations (9)-(11), shrinking once more if necessary, imply

    |(W.X)(sigma)|>=c5 ell g/r.

Dividing by the upper inequality in (7) gives the Q1 lower bound. For the upper bound use (5), (7), ell>=1 and r<1 to obtain Q2<=C ell/r, then Q1<=m Q2. Finally Q2>=Q1/m and bounded m give the Q2 lower bound. This proves (2) for every real omega.

## 5. Direct integrability conclusions and exact scope

For the logarithmic factor ell=log log(1/r)+1, the upper bound in (2) has pth-power radial integral bounded by a constant times

    integral_log(1/r1)^infinity exp(-(2-p)t)(log t+1)^p dt.

It is finite for every 0<p<2. The lower bound for p=2 instead gives a positive multiple of integral (log t+1)^2 dt, which diverges. This establishes the actual non-L2 property without using an upper bound backwards.

For general ell in (1), suppose Qj<=B2+C0/r on a centre disc. Choose a smaller disc so K1 ell(r)>=2C0 and ell(r)>=1 there. Formula (2) forces

    B2>=(K1/2)ell(r)/r.

The square integral diverges, already because integral_0^delta dr/r diverges. This contradicts B2 in L2 and proves the stated mixed-majorant failure. For C0=0 the same proof applies. For the arbitrary-envelope construction, Lambda(t)<=C(1+t) also implies every subcritical Lp membership by the same exponential integral.

All seven original LIT304 sections were read. Their construction, symmetric positive coefficient, O(g/r) remainder, exact three-dimensional identity, integration and missing-pressure qualification agree with the argument above. The independent generalization replaces the one explicit radial factor by exactly the derivative-flat monotone factors satisfying (1); it does not assert that value flatness alone implies (1).

These are fields satisfying C only. They supply no scalar S, pressure P, pressure-Poisson relation, full common-flat solution, global smooth extension or decay at spatial infinity. The local construction is not a counterexample to the original Euler conjecture. A bound uniform in omega, arbitrary weak-L2 continuation and completion to F are not established. Existing configured model theory-agent comparison is requested through files only; actual provider execution is independently unattested.

All five independent sections, all seven LIT304 source sections and the complete eight-item coordinator comparison were read. The comparison specifically recomputes the exact sign, O(g/r) remainder, all-omega transport and direct integrability conclusion. Its scope statement that no full-system solution exists in the submission is understood as no completion supplied; actual non-completability is a separate claim awaiting LIT305 review.
