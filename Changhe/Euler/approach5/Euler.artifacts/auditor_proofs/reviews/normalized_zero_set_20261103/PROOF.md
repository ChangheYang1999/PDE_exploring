# Removal of arbitrary zero sets for a normalized velocity

## 1. Statements and exact regularity

Let 0<c<1/2, omega be any finite real number, Jx=e3 cross x, X=(cI-omega J)x, eta=(1-2c)/(2-2c), gamma=c/(1-c), and m=1/c. Let G be open in R3 minus{0}. Suppose V is smooth, divergence free and satisfies

    X.grad V=-(1-c)V-omega JV.

Set E=|V|² and W=curl V. Assume the additional identity

    E W=eta grad E cross V                       (1)

at every point of {V!=0}. If V is infinitely flat at an interior point x0, then V vanishes on a neighbourhood of x0. Flatness here may be read as the value estimates |V(x)|<=C_N|x-x0|^N for every positive integer N, with a possibly different neighbourhood for each N.

In fact smoothness can be replaced by V in C_loc^(k,theta), where k is a positive integer, theta in(0,1], and k+theta=1/gamma, retaining the stated value flatness. If 1/gamma is an integer N, choose k=N-1 and theta=1. All derivatives in the hypotheses then exist classically because k>=1. In the campaign interval the sufficient regularity is C_loc^(1,1/c-2), whose Holder exponent lies in(0,1/2). Alternatively C2 suffices for every c>1/3 by an elementary estimate below. Neither conclusion assumes a pressure, a scalar S, or k0:=X.V=0.

## 2. Scalar roots and the finite-regularity input

The external input is Ghisi and Gobbino, arXiv:1107.2694v2, Theorem2.3. For a continuous real f with |f|^(k+theta)=|g| and g in C^(k,theta), its weak gradient is locally weak L^p, where 1/p+1/(k+theta)=1. It follows that f is locally W1,s for every 1<=s<p. Apply this only on compact boxes, where the required Holder norms are finite. There is no assumption on the zero set.

For each real component v_i of a C^(k,theta) vector field v, take f_i=sign(v_i)|v_i|^gamma. Off {v_i=0},

    Df_i=gamma |v_i|^(gamma-1)Dv_i.

Both the classical derivative of v_i and the weak derivative of f_i vanish almost everywhere on their zero level set. Thus h_i=|v_i|^(gamma-1)|Dv_i| off that set, extended by zero, is in L_loc^s for every s<1/(1-gamma).

The actual primary text was inspected at Theorem2.3 and its complete slicing proof on printed pages15-16, as well as its stated one-dimensional input. The last displayed inequality on printed page16 retains p/(k+theta) on the gradient norm after taking a p-th root. That exponent must be 1/(k+theta), by the preceding(3.24); the theorem statement already has the correct exponent. The erroneous display is not used. A saved primary text identifies the version. This audit does not claim a new complete proof of the cited root theorem.

## 3. Vector regularization and removal

Define T_epsilon(v)=(|v|²+epsilon²)^((gamma-1)/2)v. The derivative of the radial map has tangential eigenvalue a_e=(|v|²+epsilon²)^((gamma-1)/2) and radial eigenvalue a_e[1+(gamma-1)|v|²/(|v|²+epsilon²)], between gamma a_e and a_e. Consequently

    |DT_epsilon(v)|_F
       <=a_e |Dv|_F
       <=sum_i (v_i²+epsilon²)^((gamma-1)/2)|Dv_i|
       <=sum_i h_i                                      (2)

almost everywhere. The last step also holds on each component zero set because Dv_i=0 almost everywhere there. The bound is independent of epsilon. Moreover T_epsilon(v) converges locally uniformly to T_gamma(v)=|v|^(gamma-1)v, extended by zero; the error is at most a constant depending on gamma times epsilon^gamma, by splitting |v|<=epsilon and its complement.

For any 1<s<1/(1-gamma), weak compactness in W1,s and distributional testing identify the derivative of this uniform limit. It follows that T_gamma(v) is W_loc^(1,s), and hence W_loc^(1,1). On {v=0} its weak derivative vanishes almost everywhere, componentwise by the Sobolev level-set property. Off that set it has its classical derivative. Therefore a classical zero exterior derivative off {v=0} is a zero exterior derivative in distributions everywhere. No boundary size or geometry enters.

For alpha=T_gamma(V), its classical curl where E>0 is

    curl alpha=E^(-eta-1)(E W-eta grad E cross V).

Thus (1) gives a continuous distributionally closed form on all G. This proves the zero-set step at the finite regularity of Section1.

## 4. Independent C2 proof in the target range

For gamma>1/2 and a real C2 function f put Psi_epsilon(t)=t(t²+epsilon²)^(gamma-1). Then

    |Psi_epsilon(t)|<=|t|^(2gamma-1),
    Psi_epsilon'(t)>=(2gamma-1)(t²+epsilon²)^(gamma-1).

With a compactly supported smooth cutoff chi, integration by parts gives

    integral chi² Psi_epsilon'(f)|Df|²
       =-integral Psi_epsilon(f)(chi² Delta f+2chi Dchi.Df).

The right side is uniformly bounded using the compact C2 norms. Applying this componentwise and using

    |DT_epsilon(v)|²
      <=sum_i(v_i²+epsilon²)^(gamma-1)|Dv_i|²

gives uniform local W1,2 bounds. Uniform convergence then proves alpha in W1,2 and the same distributional removal. The strict inequality gamma>1/2 is exactly c>1/3. This proof makes no claim at gamma=1/2 and uses no primary root theorem.

## 5. A potential and the derived zero-contraction identity

On a small ball about x0, a continuous distributionally closed form alpha has a C1 potential psi: mollify on a larger ball, use radial integrals for the smooth closed forms, and pass uniformly to their potentials and gradients after fixing the value at x0.

Let Q_t=exp(-omega tJ), F_t x=exp(ct)Q_t x. The homogeneity equation gives

    V(F_t x)=exp(-(1-c)t)Q_t V(x),
    alpha(F_t x)=exp(-ct)Q_t alpha(x), F_t^*alpha=alpha.

These equalities include zeros. On a smaller connected ball and for all sufficiently small t, D(psi composed with F_t-psi)=0, so the difference is spatially constant. Homogeneity keeps V(F_t x0)=0. The derivative of psi along this zero orbit is alpha.X=0, and evaluation there shows that the spatial constant is zero. Thus X.psi=0 locally. It follows that X.V=0 there, including velocity zeros. This conclusion is derived from a single zero, not assumed.

The value flatness of V gives |alpha(x)|=|V(x)|^gamma flat to every order. Line integration gives the same property for psi-psi(x0). No smoothness of all divided derivatives is asserted.

## 6. Exact transverse scalar equation

Because gamma(m-1)=1, inversion yields

    V=|Dpsi|^(m-2)Dpsi.

Divergence freedom therefore makes psi weakly m-harmonic. Use a smooth local flowbox x=exp(t(cI-omega J))n(y), y in R2, at x0. The metric is exp(2ct)g(y). Since X.psi=0, write psi=u(y). Put mu=sqrt(det g), B^ij=g^ij for i,j=1,2, z^j=g^0j. The contravariant m-flux has factor exp(-mct)=exp(-t), and volume has factor exp(3ct). Integrating the weak equation against product tests in t,y gives exactly

    partial_i(mu |Du|_B^(m-2) B^ij u_j)
      +(3c-1)mu |Du|_B^(m-2) z^j u_j=0.              (3)

This is a full-disk weak equation; there is no deleted zero set. In smooth isothermal coordinates for the positive metric B^(-1), B=lambda^(-2)I. Define w0=mu lambda^(-m) and d=(3c-1)lambda²z. Equation(3), after division by w0, becomes

    Delta_m u+beta.(|Du|^(m-2)Du)=0,
    beta=grad log w0+d.

Here beta is smooth, u is C1 and hence W_loc^(1,m), and u-u(0) has every value vanishing order. All coefficients arise from the smooth linear flow, not from dividing by V or a pressure scalar.

## 7. Continuation and its precise external scope

Guo and Kar, arXiv:1512.00673v2, Theorem1.2, gives strong unique continuation for the preceding planar scalar equation for every 1<m<infinity with locally Lipschitz drift and W_loc^(1,m) solutions, using value flatness relative to the value at the point. Its actual statement on printed page4 and the short deduction from Theorem3.5 on printed page15 were reread; the factorization argument and regularity scope were checked in the retained A1437-A1443 audit. Here m>2 and beta is smooth, so this is a literal application. It makes u constant locally. Therefore V=0 on a smaller flowbox.

The ten-section A1467 dependency was previously read in full and is pinned beside this proof. The new points are removal for arbitrary velocity zero sets, derivation of X.V=0 from one zero, and the finite-regularity version. The planar reduction is repeated here to expose every hypothesis.

## 8. Consequences for existing tails and the remaining premise

If an actual tail is C_loc^(1,alpha) for every alpha<1, then it meets the Section1 regularity threshold for every target c. To apply the theorem one must still prove its value flatness at the proposed point and (1) at every nearby nonzero-velocity point. Regularity alone proves neither.

On a patch with X.V=0, H=|S|>0 and the already established identity grad H cross V=(H/eta)W, put R=E/H. Direct differentiation gives

    curl(E^(-eta)V)=-eta E^(-eta)(grad log R cross V).

Hence grad R cross V=0 is sufficient there. If S vanishes where V does not, classical closedness must also hold at those points, or follow by density and continuity within {V!=0}. A condition stated only on selected S-components cannot be extended by assertion. No bounded-ratio or generic helicity identity is substituted for (1).

## 9. Verdict and evidence

The complete seven-section LIT244 source and all sections of this independent reconstruction were read. The root and elementary removal, local invariant potential, and planar continuation are confirmed with their exact extra hypothesis. The finite-regularity refinement is independently proved above and offered for comparison through the existing configured model agents. Their provider runtime remains unattested. All finite omega are admitted, with no division by omega. No computation, formal build, new model client, or outside-agent write was used. The unrestricted profile conjecture remains open.
