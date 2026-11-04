# Harmonic-polynomial horseshoe and its precise Euler scope

Date: 2026-11-02T22:17:24Z. A225 CONFIRMS the constructive content of coordinator CO18 with the addition sign in formula (14) interpreted as in answer formula (6). A226 CONFIRMS the ancillary obstruction, exponent and extension statements below. A227 leaves the broader claimed exclusion of every local approach to branch (I) OPEN.

## Statement and source correction

Let J(x,y,z)=(-y,x,0). There exist a real harmonic polynomial phi, c=9/20 and a finite positive omega such that B=(cI-omega J)y+grad phi has a compact, nonsingular, uniformly hyperbolic invariant set K with a Poincare return map conjugate to the full two-sided two-symbol shift. Thus both time orientations have positive entropy. The example has a positive-entropy ergodic flow measure, with backward Lyapunov spectrum (chi,0,-3c-chi), chi>0. No attractor, positive-volume basin, or SRB property is established.

The finite formula in the team records specifies the polynomial, using n=2^(2^1000), m=2^(n^2), R=2^(n^4) and omega=R. Formula (14) in that file OMITS the addition sign between the even and odd sums. They must be added, as correctly done in the team records formula (6). Their product would not give this harmonic construction. This correction is mandatory whenever the formula is reproduced.

## Independent construction check

Start with H(u,v)=(v,v^2-100-u) on Q=[-13,13]^2. If max component and first-partial errors of F-H are below 0.001, a full orbit with sign code sigma_i is the fixed point of

    u_i=v_(i-1)+e_1(u_(i-1),v_(i-1)),
    v_i=sigma_i sqrt(100+v_(i+1)+u_i-e_2(u_i,v_i)).

On |u_i|<=13 and 8<=sigma_i v_i<=12 this maps into the interior: the radicand lies in [74.999,125.001]. In the norm max(sup |u_i|/5,sup |v_i|), the two Lipschitz bounds are 0.2012 and 6.006/(2 sqrt(74.999))<0.35. The contraction theorem gives one orbit for each code. Compactness and uniqueness imply continuous coding, and invertibility of F gives injectivity. At these points DF has rows (a,1+b),(-1+d,2v+e), with each error below 0.001 and 8<|v|<12. Its determinant lies in (0.973,1.027). The unstable cone |du|<=|dv|/5 maps strictly inside itself, its dominant component expanding by at least 15.7988. The inverse stable cone has dominant expansion at least 15.7988/1.027>15. This proves uniform hyperbolicity and a full shift, without a numerical orbit calculation.

The harmonic polynomials a=(u^2-v^2)/2, b=uv, d=u^2 v-v^3/3 and the linear map D=diag(2,1/2) synthesize three shears. Take

    (p_1,q_1)=(-16b/15,4b/15),
    (p_2,q_2)=(-b/15,4b/15),
    (p_3,q_3)=(16(d-b)/15-100v,-8d/15+4b/15).

Direct differentiation gives grad p_j+D_*grad q_j equal respectively (0,-u), (v,0), and (0,u^2-u-100). Their three time-one maps compose to H. The third identity follows from D_*grad d=(4uv,u^2/8-2v^2); cancellation gives its claimed vertical component. D itself is the time-log(2) flow of grad a. Thus each repeated block

    D composed Phi_(grad q_j)^(1/n) composed D^-1 composed Phi_(grad p_j)^(1/n)

is a product of harmonic-gradient flows. Three groups of n blocks give a 2 pi-periodic piecewise constant harmonic potential, with four equal time intervals per block. The constituent potentials are p_j/(nh), -log(2)a/h, q_j/(nh), log(2)a/h, h=2 pi/(12n).

Here are checks on all three error stages. On S=[-1000,1000]^2 the six shear fields and their first two derivatives are bounded componentwise by 10^8. The ideal paths stay in [-150,150]^2. Integration of the ODE and its first variational equation gives a one-step Lie-product C1 error bounded by 100 L^3 t^2 exp(10Lt), L=10^8, for t<=1/L. Telescoping and composing three stages gives at most 10^12 L^12 exp(1000L)/n. This is below C exp(C)/n with C=10^60. Stopping at a first exit, the short flow displacement is at most 2L/n and D or D^-1 expands max norm by at most two. The same bound thus proves existence of the whole construction and keeps its paths within [-400,400]^2.

Let q(s,u,v) be the order-m Fejer mean of this time potential. The potential coefficients, and the gradient's first two spatial derivatives, are O(n). There are 12n jumps, so their coefficient total variation is O(n^2). For a periodic bounded-variation coefficient f, convolution with the Fejer kernel and the elementary inequality ||f(.-t)-f||_1<=Var(f)|t| give error at most 100 Var(f)(1+log(m+1))/(m+1). Since there are only finitely many monomials of degree at most three, this also bounds the L1-in-time C1-in-space gradient error on S, after a fixed factor. Gronwall for position and the variational equation gives at most

    exp(Cn) C n^2 (1+log(m+1))/(m+1).

The fixed monomial factor and polynomial-in-n factors are absorbed by the ample C and exponent margin. This addresses the distinction between a pointwise-in-space L1 estimate and the L1 C1 norm actually used by continuous dependence. Stopped estimates keep the smoothed paths in [-401,401]^2.

Write q=sum_(|k|<=m) b_k(u,v) exp(iks), w=(X^2+Y^2-R^2)/(2R), and E_k=((X+iY)/R)^k for k>=0, with the conjugate expression for k<0. Let F=sum E_k b_-k(w,0) and G=sum E_k partial_v b_-k(w,0). The correct polynomial is

    P_R=sum_(j=0)^3 (-1)^j Z^(2j) Delta_2^j F/(2j)!
        +sum_(j=0)^2 (-1)^j Z^(2j+1) Delta_2^j G/(2j+1)!.

The exact identity

    Delta_2(E_k f(w))=E_k[(1+2w/R)f''+2(|k|+1)f'/R]

lowers the radial polynomial degree by at least one. Hence Delta_2^4F=Delta_2^3G=0 and applying Delta_2+partial_Z^2 to the two sums telescopes. The polynomial is real and harmonic, of degree at most m+6.

For |u|,|v|<=1000 and r=R+u, w=u+u^2/(2R) and E_k=(1+u/R)^|k| exp(ik theta). The radial operator on degree-three polynomials has coefficient l1 norm at most 7 and differs from partial_w^2 by at most 18(|k|+1)/R. At most three applications occur. Using coefficient bounds 10^4 n, |w|<=1001, and the first three derivatives of (1+u/R)^|k|, summation over 2m+1 modes gives

    ||P_R-q(-theta,u,v)||_(C3 in u,v) <= 10^40 n(m+1)^8/R,
    ||partial_theta P_R||_(C2 in u,v) <= 10^40 n(m+1)^3.

These large constants dominate the finite coefficient counts and the at-most-six polynomial degrees in u,v. No expansion in m is necessary. Now phi=-c(X^2+Y^2)/2+cZ^2+R P_R gives

    B=-R Jy+3cZ e_3+R grad P_R.

With s=-theta, the transverse equation is (grad_(u,v) P_R+(0,3cv/R))/(1-partial_theta P_R/(R+u)^2). The denominator is between 1/2 and 3/2. Its C1 discrepancy from grad q is at most C n^3(m+1)^12/R; its second spatial derivatives are controlled as needed for the variational comparison. One more stopped Gronwall estimate gives return-map error at most exp(Cn) C n^3(m+1)^12/R and paths inside [-402,402]^2.

The combined error is therefore at most

    C exp(C)/n
    +exp(Cn) C n^2 (1+log(m+1))/(m+1)
    +exp(Cn) C n^3 (m+1)^12/R.

Each term is below 10^-4 for the stated exact parameters. For the first, log n>10^300 while C=10^60; for the second log m=n^2 log 2 dominates Cn and all logarithmic factors; for the third log R=n^4 log 2 dominates 12 log(m+1)+Cn and those factors. These comparisons also establish all intermediate smallness and no-exit conditions. Thus the return map meets the explicit horseshoe criterion.

The angular speed is bounded away from zero, so suspension produces a compact nonsingular hyperbolic flow set. The return times are at most 4 pi/R. The suspension of the fair Bernoulli shift measure has entropy at least R log 2/(4 pi)>0. For the backward flow, div(-B)=-3c and the nonvanishing flow vector has exponent zero, so uniform transverse hyperbolicity gives spectrum (chi,0,-3c-chi). This measure has not been shown to be SRB.

## Euler coupling and extension

For ANY harmonic phi on an open set, put U=grad phi and

    P=-(1-2c)phi-((cI-omega J)y).grad phi-|grad phi|^2/2.

Differentiating uses A^T=cI+omega J and gives exactly (1-c)U+(Ay+U).grad U+omega JU+grad P=0; div U=0. Consequently this polynomial example actually supplies a global polynomial Euler profile, which does not decay. Its polynomial gradient cannot be bounded unless constant; the horseshoe excludes that constant case. Hence it is not a counterexample in the task's class.

To preserve the same local dynamics with a smooth decaying divergence-free field, define a vector potential Acal=-y cross integral_0^1 t U(ty)dt, and replace U by curl(eta Acal), where eta is a compactly supported smooth cutoff equal to one near K. The homogeneous identity curl(y cross U_l)=-(l+2)U_l proves curl Acal=U term by term. The resulting field is compactly supported and agrees near K, but no global Euler equation for that cutoff field is asserted.

More generally a smooth divergence-free germ near compact K has such an extension if and only if its flux two-form is exact on SOME neighborhood of K. Necessity follows by restricting a global primitive in contractible R3. Sufficiency is the same cutoff construction on a local primitive. De Rham's integration pairing gives the equivalent vanishing of all two-cycle flux periods. The existential neighborhood quantifier is essential.

The source's obstructed local torus example is also valid: prescribe analytic Cauchy data phi=-c|y|^2/2 and partial_n phi=-c y.n on an analytic torus away from the axis. The noncharacteristic analytic Cauchy theorem gives a harmonic germ on a collar, with gradient -cy on the torus. Thus B=-omega Jy is tangent and nonsingular there, but U-flux is -3c Vol(interior), precluding a global divergence-free extension. A disjoint union with the polynomial horseshoe preserves positive entropy. This last example is for arbitrary harmonic germs, not an asserted finite-source representation or connected domain.

## Other checked statements

For an axisymmetric phi, g=c|y|^2/2+phi satisfies B.grad g=|grad g|^2. Every invariant probability lies on {grad g=0}, where the flow is rigid rotation. Averaging a time-one invariant measure over one unit of flow preserves its entropy, so the variational principle gives zero topological entropy on a compact invariant set. Recurrence itself is NOT excluded: phi=-c(X^2+Y^2)/2+cZ^2 gives periodic circles at Z=0.

For any potential g, integrating |B|^2 along a nonconstant periodic orbit yields -2 omega times signed projected area. Cauchy-Schwarz and the periodic mean-zero Wirtinger inequality bound its absolute area by T/(4 pi) times that same energy, hence T>=2 pi/|omega|. The rotation-removing forward substitution is y=exp(-omega tJ)Y. A uniformly positive symmetric derivative cI+D2phi>=eta I on a convex neighborhood forces distinct forward trajectories apart at least exp(eta t), so a compact invariant set there is a singleton. Spatial scaling phi_epsilon(y)=epsilon^2 phi(y/epsilon) conjugates the dynamics at unchanged time, c and omega, excluding an absolute domain-size lower bound without further derivative data.

## Scope verdict

The construction refutes a universal local zero-entropy assertion for harmonic-gradient-plus-rotation fields, and shows that the entropy-zero premise used elsewhere is not a consequence of local irrotationality alone. It does NOT refute a possible local obstruction to an irrotational SRB measure or attractor. Therefore the coordinator's stronger sentence that every proof of branch (I) or case (gamma) needs global information is not justified by this saddle example. In particular, a local exclusion specific to physical measures remains logically possible. The construction is at one enormous omega and does not cover every prescribed omega. No numerical evidence or remote model was needed for this audit. The independent model coordinator check was read and its algebra verified; its unverified constants were checked here through the explicit coefficient and variational bounds above.
