# A far-field obstruction for every bounded coupling with small output tails

## Statement and exact spaces

Fix 0<alpha<1 and gamma>4k, where k=1615536043799051/9007199254740992 and ell=1/k. Let rho0 be the exact joined normalized trial. Let Y consist of bounded continuous physical-parity functions, even in x and odd in y, vanishing on x=0, with norm

 ||h||Y=||h||infinity+[h]_(x,alpha)+[h]_(y,2,alpha)+||h||L2(w_gamma),
 [h]_(y,2,alpha)=sup |h(x,y)-h(x,y')|/(x^2 |y-y'|^alpha),
 w_gamma(X)=(1+|X|^2)^(-gamma/2).

Use V=ell X+U[rho0], T=V.grad-1, and the maximal domain

 D_Y={h in Y:V.grad h belongs to Y distributionally}.

Fix a smooth radial cutoff chi, equal to1 on B1 and0 outside B2, and put beta_R=1-chi(X/R). Suppose B:Y->Y is a bounded LINEAR map and

 epsilon(R)=||beta_R B||_(Y->Y) tends to0 as R tends to infinity.       (1)

Then A=T+B:D_Y->Y is not surjective. In particular it is not bijective and has no right inverse onto Y. This applies to Lren and the full moving-tail A0 in topics214/217 when 4k<gamma<2. The abstract theorem allows every gamma>4k for which (1) and boundedness of B are supplied.

This theorem is separate from proof 220's infinite algebraic cokernel for the actual coupling. It uses no special kernel estimate for B beyond (1). It proves no failure for the particular forcing F0, no assertion on other Sobolev spaces, and no profile nonexistence.

## Completeness, closedness and what surjectivity would imply

The target is Banach: a Cauchy sequence converges uniformly, its parity and weighted difference bounds pass to the limit, and its weighted L2 limit agrees locally with the uniform limit. Local uniform convergence also implies distributional convergence. Hence if h_n and T h_n converge in Y, their limits satisfy the transport equation distributionally, so T is closed on D_Y. The graph norm ||h||Y+||T h||Y makes D_Y Banach. Boundedness of B makes A closed on the same domain with an equivalent graph norm, whether or not the domain is dense in Y.

If A were onto, the open mapping theorem for the bounded map A:D_Y->Y would give a constant K and, for each f in Y, at least one solution u with

 Au=f, ||u||Y<=K||f||Y.                            (2)

No injectivity, bounded linear selection, or complemented kernel is needed. Indeed the quotient D_Y/ker A is Banach; choose a representative whose graph norm is at most twice the quotient norm. We will contradict (2) with uniformly bounded smooth compact forcings.

## Actual far characteristics

The exact finite outer Green formulas imply

 |U[rho0](X)|<=C r^k, |D U[rho0](X)|<=C r^(k-1)     (3)

for large r. The finite angular modes and decaying harmonic terms justify this at the axes as well. In the sector x>=R1, 0<=y<=x write

 V1=x(ell+a), V2=y(ell+b).

Here |a|<=Cx^(k-1). Since U2 is odd in y,

 b(x,y)=integral_0^1 partial_y U2(x,sy) ds,

and every point on that vertical segment has radius at least x. Thus |b|<=Cx^(k-1), without using a derivative estimate near the physical origin.

Choose a number d>0 with 2d<log(3/2)/2, and then choose R1 so large that C R1^(k-1)<ell/2 and

 4 C R1^(k-1)/(ell(1-k))<d.                       (4)

For a forward orbit beginning at (R1,y*), 0<y*<=R1/4, the sector is invariant by a bootstrap. As long as it remains in the sector, x_t>=R1 exp(ell t/2), and therefore

 integral_0^infinity (|a|+|b|)dt
 <=4 C R1^(k-1)/(ell(1-k))<d.

The ratio y_t/x_t changes by a factor between exp(-2d) and exp(2d); choose d also with exp(2d)<2. It cannot reach1 from an initial ratio at most1/4. The lower x bound prevents exit across x=R1. At most linear growth of V gives global existence. Consequently

 x_t=R1 exp(ell t+A_t), y_t=y* exp(ell t+B_t),
 |A_t|,|B_t|<=d                                             (5)

for every t>=0. The exact exponent ell is retained. The factor 1/(1-k) in (4) corrects a harmless missing factor in the submitted theory author draft's explicit choice of d.

## Uniformly bounded forcing packets

Take smooth functions phi,theta,sigma with the following properties. The function phi on the positive half-line is nonnegative, supported in [1,4], and equal1 on [2,3]. The function theta is even, nonnegative, equal1 on [-1,1], and0 outside [-2,2]. The function sigma is odd, nondecreasing, and equal1 on [1,infinity). All are bounded by1 in absolute value. For X0 tending to infinity define

 f_(X0)(x,y)=phi(|x|/X0) theta(X0 y) sigma(|x|^(2/alpha)y).      (6)

It is smooth on the plane because it vanishes near x=0, has the required parities, and is nonnegative on y>=0. Its support has |x| comparable to X0 and |y|<=2/X0. Its supremum is at most1.

The horizontal derivative is O(1/X0): in the differentiated sigma factor its argument lies in [-1,1], so |x|^(2/alpha-1)|y|<=C/X0. A bounded function with this derivative has horizontal alpha seminorm bounded uniformly for X0>=1. For the vertical difference, use min(2,Ls)<=C_alpha L^alpha s^alpha for a bounded function with Lipschitz constant L. The sigma contribution gives L^alpha<=C x^2, and the theta contribution gives C X0^alpha<=C x^2 on the support. Taking the product difference with x fixed proves a uniform divided vertical seminorm, including pairs outside the support. Finally the support area is bounded and its weighted L2 norm squared is O(X0^(-gamma)). Thus

 ||f_(X0)||Y<=C0                                           (7)

uniformly in X0. Each forcing is compact and smooth, so it also belongs to D_Y. No uniform transport-graph norm of the forcings is asserted or needed.

Set

 y*=exp(2d) R1 (2X0)^(-1-2/alpha).                         (8)

When x_t runs through [2X0,3X0], equations (5) give x_t^(2/alpha)y_t>=1 and y_t<=C X0^(-2/alpha)<=1/X0 for large X0. Thus f_(X0)(x_t,y_t)=1 throughout this interval. Its duration is at least (log(3/2)-2d)/ell>0. The entry time t0 satisfies exp(-t0)>=c(R1/X0)^k, since ell k=1. The forcing is nonnegative on the entire orbit. Therefore

 I_f:=integral_0^infinity exp(-t) f_(X0)(x_t,y_t)dt
       >=c1(R1/X0)^k.                                   (9)

All constants may depend on fixed R1,alpha,gamma and the chosen cutoffs, but not X0.

## The full time integral of a small-tail coupling

Write H=ell(2+alpha)>1 and

 L=R1^2(y*)^alpha=C_* R1^(2+alpha) X0^(-2-alpha).

For every h in Y, oddness in y and the seminorm give |h(x,y)|<=||h||Y min(1,x^2|y|^alpha). From (5), x_t^2 y_t^alpha<=C L exp(Ht). Let R=X0^(1/2), and let t_R be the unique exit time from the disk of radius2R. Along the sector orbit both coordinates strictly increase. Equation (5) implies exp(ell t_R) is comparable to R/R1.

Before t_R, the bound for B gives

 integral_0^(t_R) exp(-t)|Bu(x_t,y_t)|dt
 <=C||B|| ||u||Y L exp((H-1)t_R)
 <=C||B|| ||u||Y (R1/X0)^k (R/X0)^(2+alpha-k).     (10)

After t_R, beta_R equals1 along the orbit. Its output seminorm and supremum therefore give

 |Bu(x_t,y_t)|<=epsilon(R)||u||Y min(1,C L exp(Ht)).

The exact elementary integral satisfies, for 0<L<1,

 integral_0^infinity exp(-t) min(1,C L exp(Ht))dt
 <=C_H L^(1/H).                                   (11)

To verify (11), split at log(1/(CL))/H; the two integrals are bounded respectively by (CL)^(1/H)/(H-1) and (CL)^(1/H). If CL>=1 the asserted estimate follows by increasing the same constant. Since L^(1/H)=C(R1/X0)^k, (10)-(11) give

 |I_B|:=|integral_0^infinity exp(-t) Bu(x_t,y_t)dt|
 <=C||u||Y (R1/X0)^k
       (||B|| X0^(-(2+alpha-k)/2)+epsilon(X0^(1/2))).       (12)

This controls the entire forward trajectory. There is no assumption about a rate for epsilon, compactness of B, or cancellation of the coupling.

## Contradiction

Suppose surjectivity and choose solutions u_(X0) from (2), with ||u_(X0)||Y<=KC0. Their transport images are f_(X0)-Bu_(X0) in Y. Continuity and a smooth flow-box change of variables turn the distributional transport equation into the characteristic integral identity on every finite time interval. The identity initially valid on almost every transverse coordinate extends by continuity to every coordinate. Boundedness of u lets the terminal exp(-t)u(Phi_t X) vanish as t tends to infinity. Hence

 u_(X0)(R1,y*)=-I_f+I_B.

The bracket in (12) tends to0, so (9) implies |u_(X0)(R1,y*)|>=c1(R1/X0)^k/2 for large X0. But oddness and the defining vertical seminorm give

 |u_(X0)(R1,y*)|<=KC0 R1^2(y*)^alpha
                      =C KC0 R1^(2+alpha)X0^(-2-alpha).

This is impossible because 2+alpha>k. Equivalently, the normalized vertical difference between (R1,y*) and (R1,-y*) diverges at least as a positive constant times X0^(2+alpha-k), contradicting the uniform bound. Surjectivity fails.

## Applications and limits of the conclusion

Proof 214 proves (1) for Cren when 4k<gamma<2, with epsilon(R)<=C R^(k-1)(1+logR). Proof 217 proves it for the full C0 with epsilon(R)<=C R^(2k-gamma/2)(1+logR), whose exponent is strictly negative. Thus both actual closed realizations fail surjectivity. Proof 220 gives the stronger infinite-cokernel result for these particular operators using a different forcing family and an additional exact kernel bound.

The proof shows that a global inverse onto the present Y is impossible. It does not prove that one specified replacement norm, or the suggested far window beta<k, is necessary among all possible spaces. Such a statement needs its own hypotheses and scaling theorem. It does not show that the actual residual has no preimage, or that a parametrix onto a smaller compatible range cannot be built. The local extension inverses remain valid.

Dependencies: topics35/117 for the exact outer Green growth; topics213/214/217 for the common space and actual bounded coupling applications; proof 220 for the separately stated stronger actual result. The abstract proof, forcing bounds, complete time integrals and surjectivity argument have been independently derived here from the theory author's submitted draft.
