# A rank-one perturbation can preserve the low inverse and destroy high regularity

## Exact abstract assertion

Let Z and Y be Banach spaces, let L0:Z->Y be a bounded isomorphism, and let c be a nonzero continuous linear functional on Z. Let H be a linear subspace of Z and let YH be a dense linear subspace of Y. Suppose u belongs to Z, c[u]=0, and u does not belong to H. Set N=L0u and

 Lepsilon h=L0h+epsilon c[h]N.

For every scalar epsilon, Lepsilon:Z->Y is a bounded isomorphism, with

 Lepsilon^(-1)f=L0^(-1)f-epsilon c[L0^(-1)f]u.            (1)

If L0^(-1) maps YH into H, then for every nonzero epsilon the inverse of Lepsilon fails to map YH into H. Thus a low inverse and unchanged local frozen principal operators do not imply a high inverse when the rank-one profile is only assumed smooth and in Y.

This is an insufficiency statement about hypotheses. It is not a theorem that every possible high inverse requires the profile separately to belong to YH. Such necessity would require additional mapping hypotheses on the other terms. It is also not a counterexample for the actual IPM bordering profile zeta, whose high-target membership is proved in proof 83.

## Proof of the abstract assertion

Lepsilon=L0(I+epsilon u c), where (u c)^2=u c[u] c=0. Hence I-epsilon u c is its exact bounded inverse, giving (1). The functional c L0^(-1) is continuous and nonzero on Y. Density gives f in YH on which it is nonzero. If L0^(-1)f belongs to H and Lepsilon^(-1)f also belonged to H, their difference would put the nonzero multiple epsilon c[L0^(-1)f]u in H, a contradiction.

## A concrete low-domain function for the actual modal background

Use the strong spaces Z and Y of proof 76, and their remainder weight

 w_a(X)=|x|^(-17/2) max(1,r)^(29/4).

In a fixed closed angular cone away from both axes and at r>1, this weight is comparable to r^(-5/4). The remainder domain requires u and V.grad u in L2(w_a). Functions vanishing in neighborhoods of the axes have zero axis jet, and compactly supported potentials below produce no velocity outside those neighborhoods.

Choose nonzero smooth real cutoffs a supported in (1,2), b supported strictly inside (0,pi/2), and a fixed R0 larger than the outermost spline radius and all finite critical points. Put Rj=R0 4^j and let nj be integers with nj asymptotic to exp(j^2). In the positive quadrant define

 vj(r,theta)=Rj^2 nj^(-4) a(r/Rj)b(theta)cos(nj theta).

Extend vj evenly in x and oddly in y, and put v=sum_j vj and u=-Delta v. The supports are disjoint annuli and vanish in a fixed angular neighborhood of the axes. The sum is locally finite, hence smooth everywhere. Polar differentiation gives

 u_j=nj^(-2) a(r/Rj)b(theta)(Rj/r)^2 cos(nj theta)
       + O(nj^(-3)),                                    (2)

uniformly on each scaled annulus. Its radial derivatives of fixed order have the corresponding powers of Rj^(-1), and one angular derivative has size O(nj^(-1)).

Since the area of the annulus is O(Rj^2),

 ||u_j||_L2(w_a) <= C Rj^(3/8) nj^(-2).

For the actual background, U[rho]=O(r^k), grad rho=O(r^(k-1)), and V=ell X+U[rho], with k<1. Thus

 ||V.grad u_j||_L2(w_a)
 <= C Rj^(3/8)(nj^(-2)+Rj^(k-1)nj^(-1)).               (3)

All sums of these bounds converge. Therefore u belongs to the actual low remainder graph domain and hence Z, with J[u]=0.

## Exact nonlocal localization and strain

The canonical stream of u is psi=partial_x v, because -Delta(partial_x v)=partial_x u, this stream has the required parity and decay, and the canonical convention excludes extra harmonic terms. Consequently

 U[u]=(-partial_xy v,partial_xx v).                    (4)

Both components have the same annular supports and size O(nj^(-2)). In particular they vanish near the axes and all critical points. The kernel K(X)=pi^(-1)r^(-3)sin(3theta) is harmonic off zero. Integration by parts separately on each compact annulus gives integral K(-Delta vj)=0. Absolute convergence follows from the bound C Rj^(-1)nj^(-2). Hence c[u]=0. This also follows by differentiating the stream, which vanishes near zero.

It follows from (3), (4) and the bound on grad rho that N=Lred u belongs to Y, has zero axis jet and is smooth. Its support lies in the same annuli. It vanishes near zero and the source points. Its smoothness here is literal local C-infinity: every support lies beyond the finite spline joins, where the modal background is analytic. No uniform bounds on arbitrarily high derivatives of N are asserted.

## Failure of the high condition

For any fixed far exponent gamma and any cylinder order s>2, the high norm of r^(-gamma)u_j has lower bound

 c Rj^(-gamma) nj^(s-2)

for sufficiently large j. To verify this, project the angular Fourier series to frequencies of size nj. The leading nonzero cutoff coefficient in (2) retains a fixed fraction of its L2 norm in that band; smooth cutoff tails tend to zero faster than any inverse power of nj. The O(nj^(-3)) terms have smaller band norm. The radial support has fixed length in t=log r, so its L2 factor stays bounded above and below after scaling. Multiplication by the Sobolev multiplier contributes a factor comparable to nj^s. The displayed lower bound tends to infinity because nj grows like exp(j^2), while Rj grows geometrically. Thus u is excluded by every such far high space, including the proposed order25/4 and weight gamma=-1/2.

If the actual Lred low inverse exists, it may serve as L0 in the abstract assertion. Changing its rank-one profile by epsilon N leaves V, the order-zero Riesz coupling symbol, and the frozen operators near the critical points unchanged, while destroying the proposed high inverse whenever the unperturbed inverse has it. This proves the advertised non-implication. The modified rank-one profile need not arise from a stationary density, and no such physical realization is claimed.

## Dependencies and scope

The actual background far growth, exact low space and boundedness of c are the verified results in topics26,76 and83. The construction itself uses only polar differentiation, integration by parts and a Fourier band lower bound. It independently verifies the relevant counterexample of the theory author's TH_varorder consultation and corrects any reading of that example as a failure theorem for the actual zeta.
