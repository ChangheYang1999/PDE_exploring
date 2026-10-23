# A nonzero profile has nonzero angular far-field amplitude

Status: CONFIRMED after independent derivation and checked Opus 5.5 review 06. Date: 2026-10-20.

## Statement

Let c_l>1 and let rho be any nonzero smooth full-plane profile with the parities and canonical inverse of PROMPT.md, satisfying its density and gradient growth bound for some 0<gamma<1. Do not assume rho_y(0) is nonzero, or that rho(0,y) is nonzero. Put p=1/c_l. Then the angular far-field limit Theta_0 is nonzero and p<=gamma. In particular, every nonzero profile in this class is unbounded in absolute value at infinity along at least one direction.

The continuous angular-limit proof in ../far_field/PROOF.md and the Holder upgrade in ../far_field_holder/PROOF.md apply without a center condition. In using them here, the nonzero amplitude and p<=gamma needed in the Holder upgrade are supplied by the following argument in place of the primary y-axis argument.

## Proof

The canonical inverse gives U=O((1+r)^gamma). Thus W=c_l X+U has at most linear growth and its smooth flow is complete for every finite positive or negative time. There is R0>0 such that V=W.e_r>=c_l r/2 on r>=R0. The defining equation W.grad rho=rho therefore gives, along every trajectory,

    rho(Phi_t X)=e^t rho(X).

Choose X with rho(X) nonzero. This trajectory eventually leaves every compact set, since otherwise the unbounded right side would contradict boundedness of rho on that compact set. More precisely, for each radius R, the finite maximum of |rho| on the closed disk shows that |Phi_t X|>R for all sufficiently large t.

There is a point Y on r=R0 with rho(Y) nonzero. If X lies inside that circle, the forward escape just proved gives such a crossing. If X lies outside, follow its trajectory backward while r>=R0. The inequality dr/dt>=c_l r/2 forces a crossing within time at most (2/c_l)log(|X|/R0). Nonzero density is preserved at every finite trajectory time. Starting on the circle is already sufficient.

For every angle beta on the circle, the radial scattering construction gives a limiting angular map theta_infinity(beta), a continuous function H_infinity(beta), and

    Theta_0(theta_infinity(beta))
       =R0^(-p) exp(H_infinity(beta)) rho(R0,beta).

The limiting map is a diffeomorphism of the circle and the exponential factor is strictly positive and finite. At the nonzero point Y the right side is nonzero. Hence Theta_0 is nonzero. Uniform convergence of r^(-p)rho(r,theta) and the assumed O(r^gamma) growth force p<=gamma. At an angle where Theta_0 is nonzero, rho(r,theta) grows as a nonzero constant times r^p, proving the final assertion.

## A reporting scale without a center condition

Use the explicitly normalized angular norm

    S=( (1/(2pi)) integral_0^(2pi) |Theta_0(theta)|^2 dtheta )^(1/2)>0.

Under the genuine scaling rho_lambda(X)=lambda rho(X/lambda), with lambda>0, the parameter p is invariant, Theta_{0,lambda}=lambda^(1-p)Theta_0 and S_lambda=lambda^(1-p)S. Therefore

    L_angular=S^(1/(1-p))

transforms as a length. Every nonzero profile in this class has exactly one representative with L_angular=1, obtained using lambda=1/L_angular. This condition neither changes nor fixes c_l or any invariant center slope. No exceptional profile with S=0 has been discarded, since the theorem excludes it for exact nonzero profiles.

The primary reporting scale (K/a0)^(1/(1-p)) in ../scaling/PROOF.md remains valid and may be more useful for those profiles. These two conventions select different representatives of the same scaling orbit. The angular norm condition also covers the secondary branch and profiles with an identically zero y-axis trace. It is a scale convention, not an existence result or a classification of solution families.
