# Inactive coefficient directions and relative-step stopping

## Statement and hypotheses

Let X=R^n and Y=R^m with Euclidean norms. Let N be a nonzero linear subspace of X, and suppose a residual map R:X->Y satisfies R(x+h)=R(x) for every x in X and h in N. No linearity of R is assumed. Fix x,d in X, h in N with h nonzero, and a tolerance tau>0. Whenever the denominator is nonzero, define s(t)=||d||/||x+t h||. Then s(t) tends to zero as |t| tends to infinity, while the residuals at the two endpoints x+t h and x+d+t h are independent of t. Thus this relative-step quantity alone is not a stopping criterion on the quotient X/N: the same residual change can pass an arbitrary positive tolerance after adding a sufficiently large inactive component.

Separately, let B be a real m by n matrix with column j exactly zero. Let D be a positive diagonal matrix with D_jj=delta>0 and write B_s=B D^(-1). If a computed scaled coefficient y has component y_j=epsilon, the unscaled coefficient x=D^(-1)y has x_j=epsilon/delta, which contributes zero to Bx. In exact arithmetic every minimum-Euclidean-norm least-squares solution of B_s y=b has y_j=0. A nonzero computed component in that direction can therefore be an arithmetic artifact even when the residual is small. The algebra does not assert that a particular solver must return such an artifact or bound its size.

## Proof

The reverse triangle inequality gives ||x+t h|| >= |t| ||h||-||x||, which tends to infinity. The numerator is fixed, so s(t) tends to zero. Residual invariance gives R(x+t h)=R(x) and R(x+d+t h)=R(x+d). For the second statement, multiplication by D^(-1) gives the component formula, and the zero column annihilates this component. If a least-squares solution has y_j nonzero, setting just that coordinate to zero leaves the residual unchanged and strictly decreases its Euclidean norm. Hence a minimum-norm solution has y_j=0.

## Campaign application and scope

The E channel in the saved representation masks angular degrees l=0,1. For each carried E coefficient of degree l=1 the represented velocity is identically zero. All spatial derivatives, pressure source, and residual quantities defined only from the represented field are unchanged when such a coefficient changes. The gauge based on the leading A,C tail is unchanged too. This conclusion uses the channel mask itself; a numerically zero sampled column by itself would not establish it. Tail elimination leaves E entries unchanged. In the even-m layouts inspected here l=1 carries m=0, so phase rotation also leaves these entries unchanged.

The producer field fit floors a zero column norm at 10^(-300) and unscales the computed least-squares coefficients by that floor. A computed scaled component of size 10^(-11) would become size 10^289 while remaining invisible to velocity-fit norms. The producer's relative-step test uses the full reduced coefficient norm, including these directions. Floating-point overflow in that norm can worsen the problem, but overflow of a particular operation must be checked on the actual platform and saved vector.

These statements do not make the active coefficient fit well-conditioned. Setting inactive coefficients to zero removes this failure mode, but does not bound active coefficients, gradients, the Euler residual, or the error after any normalization. Bounds on coefficient sizes depend on the chosen basis and are empirical safeguards. A weighted least-squares improvement does not imply improvement on every separately measured shell or of the nonlinear Euler objective.

Dependencies: the elementary Euclidean triangle inequality, least-squares definitions, and the explicit campaign E-channel mask. Source captures and platform checks are listed in verification/plan_v1.md. No formal theorem-prover artifact or floating-point enclosure is claimed.
