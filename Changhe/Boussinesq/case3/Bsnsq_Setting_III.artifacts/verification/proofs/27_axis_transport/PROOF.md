# Exact desingularized transport on the invariant axis

Status: an independent one-dimensional quadrature formula, under explicit absence of an additional axis equilibrium on the branch considered. It supplies axis-limit tests for the characteristic method, including the nonzero slow vorticity tail. It does not establish nonlocal self-consistency or exclude profiles with additional equilibria.

## Statement and hypotheses

Fix beta>2 and a0=1. Let W be a smooth vector field with the B2 x parity, div W=2 beta, W(0)=0, and DW(0)=diag(lambda,mu), where lambda=(beta-2)/2 and mu=1+3 beta/2. Put w(y)=W2(0,y). On a positive branch 0<y<Y, suppose w(y)>0. Define f(y)=F(0,y) and g(y)=G(0,y), the smooth axis coefficients of Theta=x^2 F(x^2,y) and Omega=x G(x^2,y), with f(0)=1 and g(0)=4/beta. The two transport equations imply the formulas below. Conversely those formulas are the unique smooth axis solutions through these values on this branch. The analogous negative branch uses s=-y and wbar(s)=-w(-s).

The forcing field need only satisfy the displayed divergence and center identities for this calculation. In a B2 profile these follow from its full-plane velocity. No claim of solving the Poisson equation is made by prescribing w alone.

## 1. Axis equations

Write W1=x A(x^2,y). The divergence equation on the axis gives A(0,y)=2 beta-w'(y). Divide the two transport equations by x^2 and x respectively and take x=0. This gives

    w f'=[2w'-(3 beta+2)]f,
    w g'+[2 beta+1-w']g=2f.                         (1)

These are desingularized equations. The undivided residuals vanish automatically on x=0 and cannot replace them. Since w=mu y+O(y^2) and 3 beta+2=2mu, the center values in (1) are compatible.

## 2. Explicit quadratures and uniqueness

The function

    S(y)=integral_0^y [1/w(z)-1/(mu z)] dz

is well defined and smooth at0. Indeed w(z)=mu z[1+z a(z)] with smooth a, so the difference of reciprocals extends smoothly. Set

    qH=(beta+1)/mu, gamma=(2 beta+1)/mu,
    qH+gamma=2, 0<qH<1.

Direct integration of the first equation gives

    f(y)=[w(y)/(mu y)]^2 exp[-2mu S(y)].             (2)

For the second equation, its integrating factor is

    J(y)=y^gamma exp[(2 beta+1)S(y)]/w(y).

Substituting (2) in (Jg)'=2Jf/w gives

    g(y)=(2/mu^2) w(y)y^(-gamma)exp[-(2 beta+1)S(y)]
             * integral_0^y z^(-qH)exp[-(beta+1)S(z)] dz.   (3)

The lower endpoint is integrable since qH<1. A nonzero homogeneous integration constant would yield g~C y^(1-gamma) at0, with 1-gamma=-(beta/2)/mu<0. Boundedness therefore removes it. Formula (2) tends to1 and (3) tends to2/[mu(1-qH)]=4/beta. Thus these formulas give the required solution and uniqueness. Smoothness through0 also follows from the transformed formula below, since its integrand is smooth in y with uniformly bounded derivatives on compact y intervals.

For numerical use remove the integrable endpoint singularity by z=y u^(1/(1-qH)):

    g(y)=2/[mu^2(1-qH)] * [w(y)/y] exp[-(2 beta+1)S(y)]
          * integral_0^1 exp[-(beta+1)S(y u^(1/(1-qH)))] du. (4)

Equations (2) and (4) require only scalar quadrature and give an independent test of a two-dimensional characteristic solver. The formulas imply f>0 and g>0 throughout a branch with w>0. These signs concern axis coefficients on this branch, not the whole half-plane.

A useful equivalent coordinate is h(y)=y exp[mu S(y)]. It satisfies w h'=mu h and h'(0)=1, and (2) becomes f=1/(h')^2. This shows explicitly how axial expansion determines the transverse temperature coefficient through incompressibility.

## 3. Conditional axis tail

Assume the branch is (0,infinity) and, for some delta>0,

    w(y)=beta y+O(y^(1-delta)) as y tends to infinity.

Reducing delta if necessary does not weaken this condition. Comparing reciprocal denominators yields

    S(y)=(1/beta-1/mu)log y + S_infinity + O(y^(-delta)).

Consequently (2) gives

    f(y)=C_f y^(-1-2/beta)[1+O(y^(-delta))],
    C_f=(beta/mu)^2 exp[-2mu S_infinity]>0.

The integrand in (3) is asymptotic to a positive constant times z^(-1-1/beta). It is integrable at infinity and at0. Its integral tends to I_infinity>0. Therefore

    g(y)=C_g y^(-1-1/beta)[1+O(y^(-delta))+O(y^(-1/beta))],
    C_g=(2 beta/mu^2)exp[-(2 beta+1)S_infinity] I_infinity>0.

This is a nonvanishing slow vorticity coefficient in the axis limit Omega/x. It is not a pointwise statement about Omega on the axis, which is identically zero. The conclusion requires that the chosen axis branch reach infinity without another equilibrium. It does not classify branches separated from the center by an additional zero of w.

## 4. Gaussian forced-flow test domain

For the external Gaussian of research/22, with c=2.5, beta=3, y0=2.85 and s=1,

    w(y)=beta y+Q(y-y0)-Q(-y0),
    Q(z)=A s^4 (1-exp[-z^2/(2s^2)])/z^2.

The amplitude A is positive for these c,y0,s, by its formula in research/22. Q is positive, even, and strictly decreasing with |z|>0, with its removable value at z=0. For y<0, Q(y-y0)<Q(-y0), so w(y)<0. For 0<y<=Q(-y0)/beta, this interval lies below y0, hence Q(y-y0)>Q(-y0) and w(y)>0. For y>=Q(-y0)/beta, beta y-Q(-y0)>=0 and Q>0, so again w>0. The needed inequality Q(-y0)/beta<y0 holds here since Q(-y0)=3.8355593 and beta y0=8.55; these values can also be bounded directly from the explicit exponential formula. Thus both axis branches have no additional zero. The same check must be performed for any other Gaussian parameters; it is not assumed automatically.

Since Q=O(y^-2), w=beta y-Q(-y0)+O(y^-2) on the positive branch and wbar=beta s+Q(-y0)+O(s^-2) on the negative branch. The tail hypotheses hold with delta=1. Both axis coefficients are therefore strictly positive and have the powers in section3. The original Gaussian forcing vorticity is a different function; equality with the transported Omega is not claimed.

Dependencies: the two exact divided transport equations, constant divergence, elementary integrating factors and reciprocal estimates. The formulas are checked before numerical implementation. Numerical evidence will be stored separately and will not substitute for the stated hypotheses.
