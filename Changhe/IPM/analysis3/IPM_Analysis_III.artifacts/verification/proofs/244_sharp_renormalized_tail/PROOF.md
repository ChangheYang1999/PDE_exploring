# Sharp renormalized coupling tails, including exact zero strain

## Statement and spaces

Fix the actual normalized and exactly joined modal trial rho0. Its exponent is k=1615536043799051/9007199254740992, with0<k<1/2. For0<alpha<1 let E2 be the space of bounded continuous real functions h on the plane, even in x and odd in y, with h(0,y)=0 and finite norm

 ||h||E2=||h||infinity+[h]_x+[h]_(y,2),
 [h]_x=sup_(x!=x',y) |h(x,y)-h(x',y)|/|x-x'|^alpha,
 [h]_(y,2)=sup_(x!=0,y!=y') |h(x,y)-h(x,y')|/(x^2|y-y'|^alpha).

For each fixed gamma>4k use

 Y_gamma=E2 intersect L2(w_gamma dX),
 w_gamma=(1+|X|^2)^(-gamma/2),
 ||h||Y_gamma=||h||E2+||h||L2(w_gamma).

Let U be the canonical IPM velocity, c[h]=partial_x U1[h](0),

 Cren h=U[h].grad rho0+c[h]H0,
 C0 h=U[h].grad rho0+c[h]M0,

where H0 is the compact normalization column and M0 the full moving-tail column. These are bounded on the displayed targets by proof 226. Define B0=ker(c:B->R), with the norm inherited from B, for B=E2 or Y_gamma. The functional c is bounded there, so B0 is a closed subspace. Let chi_* be a fixed smooth radial cutoff, one on B1 and zero outside B2, and beta_R(X)=1-chi_*(X/R).

There are positive finite constants b_B,C_B,R_B depending only on the displayed fixed parameters, trial and cutoff such that, for R>=R_B,

 b_B R^(k-1)logR <= ||beta_R Cren||_(B0->B)
                  <= ||beta_R Cren||_(B->B)
                  <= C_B R^(k-1)logR.                    (1)

Moreover beta_R C0 and beta_R Cren agree on B0. Hence(1) gives the same sharp rate for beta_R C0:B0->B. The lower bound is witnessed by smooth compactly supported physical-parity inputs with c=J=0 that belong individually to the actual maximal transport and full operator domains. Their graph norms are not claimed uniformly bounded. Constants are qualitative. The logarithm cannot be removed in these bounded-operator estimates.

The result concerns the coupling alone. It gives no global inverse, complement inverse, Fredholm conclusion or profile existence statement.

## A direct weighted velocity estimate for gamma<2

For completeness, the weighted step used below follows without extending a weight theorem to an endpoint. For -2<gamma<2, the IPM velocity satisfies

 ||U[h]||L2(w_gamma)<=C_gamma ||h||L2(w_gamma).             (2)

First take compactly supported L2 input. Plancherel gives the unweighted bound with constant1: the vector multiplier has Euclidean norm |xi_x|/|xi|<=1. Partition the plane into A0={r<2} and Aj={2^j<=r<2^(j+1)},j>=1, using their indicator projections Pj. On Aj, w_gamma is comparable, with constants depending only on gamma, to2^(-gamma j).

If |i-j|<=2, ||Pi U Pj||_(L2->L2)<=1. If |i-j|>2, the local delta term is absent and the velocity kernel is bounded by C2^(-2 max(i,j)) on Ai times Aj. Its Hilbert-Schmidt norm is at most C2^(-|i-j|), because the two areas are bounded by constants times2^(2i) and2^(2j). In weighted block coordinates this gives

 2^(-gamma i/2)||Pi U Pj h||2
 <= C a_(i-j) 2^(-gamma j/2)||Pj h||2,

where a_d is bounded for |d|<=2, is at most2^(-(1+gamma/2)d) for d>2, and at most2^(-(1-gamma/2)|d|) for d<-2. This sequence is summable exactly in the stated open range. The elementary convolution bound on l2, obtained by the triangle inequality for each shifted sequence followed by summation of a_d, proves(2). Truncation and L2(w_gamma) convergence extend the bound.

For the physical-parity E2 input used here, this weighted realization is the canonical velocity. The integral at infinity converges absolutely by Cauchy-Schwarz, since the squared order-minus-two kernel divided by w_gamma is integrable there for gamma<2. The subtraction constant of the canonical formula vanishes on each centered annulus by parity. Local principal values exist by local Holder regularity. Thus no different velocity normalization has entered(2).

## Upper bound for every displayed target

Take R larger than the fixed support radius of H0. The E2 tail estimate of proof 226, equation(5), is

 ||beta_R U[h].grad rho0||E2
                 <= C_alpha R^(k-1)(1+logR)||h||E2.       (3)

It includes the divided vertical seminorm and cutoff-crossing pairs. This proves the E2 upper bound.

When4k<gamma<2, the actual density gradient is bounded by C R^(k-1) for r>=R. Equation(2) therefore gives

 ||beta_R U[h].grad rho0||L2(w_gamma)
                 <= C_gamma R^(k-1)||h||L2(w_gamma).      (4)

When gamma>=2, use the canonical pointwise bound |U[h](X)|<=C_alpha||h||E2(1+log(2+r)) from proof 226. Direct polar integration gives

 ||beta_R U[h].grad rho0||L2(w_gamma)
             <= C_(alpha,gamma) R^(k-gamma/2)(1+logR)||h||E2
             <= C_(alpha,gamma) R^(k-1)(1+logR)||h||E2.    (5)

Here gamma>2k makes the radial integral finite, including gamma=2; no equivalence between E2 and Y_2 is asserted. Combining(3)-(5) and1+logR<=2logR for R>=e proves the upper bound in(1) for all gamma>4k. This sharpens the convenient four-term upper envelope of proof 226 only for Cren. It does not discard the full M0 column on unrestricted inputs.

## A nonzero far gradient and the exact velocity kernel

The exact finite outer expansion supplies

 rho0(r,theta)=r^k Theta(theta)+O(r^(2k-1)),
 grad rho0=r^(k-1)(k Theta e_r+Theta' e_theta)+O(r^(2k-2)), (6)

uniformly in theta. The leading trigonometric polynomial Theta is nonzero. Its highest sine coefficient is a521=exp((3-k)t_plus)Aout[259,0]/8, where the exact nonzero original dyadic coefficient is

 Aout[259,0]=-8059128652303703/10384593717069655257060992658440192.

The mode-zero normalization repair does not affect it. Since k>0, the leading gradient vector in(6) is nonzero at some angle theta_* strictly between0 andpi/2, away from both axes. Fix this angle. For X_R=3R(cos theta_*,sin theta_*), sufficiently large R satisfy

 |grad rho0(X_R)|>=b R^(k-1).                            (7)

Put n_R=grad rho0(X_R)/|grad rho0(X_R)|. It is a unit vector. We allow it to vary with R; every bound below is uniform over unit vectors.

For a smooth input, away from the input point the velocity kernel, in polar coordinates Z=(s cos phi,s sin phi), is

 K1(Z)=-sin(2phi)/(2pi s^2),
 K2(Z)= cos(2phi)/(2pi s^2).                             (8)

The second component also has the local term -h/2. These signs follow from U=(-partial_xy v,partial_xx v), v=(-Delta)^(-1)h, whose fundamental solution is-log|Z|/(2pi). All inputs constructed below vanish at X_R, so the local term is zero there.

## Uniformly bounded packets whose velocity grows logarithmically

For B=Y_gamma choose delta=min(1/2,gamma/4). For B=E2 choose delta=1/2. In each case0<delta<1; in the weighted case2delta<gamma. Set S=R^delta. Choose fixed smooth radial cutoffs chi_in,chi_out with

 chi_in(s)=0 for s<=1, chi_in(s)=1 for s>=2,
 chi_out(s)=1 for s<=1/2, chi_out(s)=0 for s>=1,
 0<=chi_in,chi_out<=1.

Write X-X_R=(s cos phi,s sin phi) and set

 a_R(X)=chi_in(s)chi_out(s/S)
                  (-n_R,1 sin(2phi)+n_R,2 cos(2phi)),   (9)

extended by zero at the center. For large R its support lies in the first quadrant and has positive distance of order R from both axes. Form the exact physical-parity extension

 q_R(x,y)=a_R(x,y)+a_R(-x,y)-a_R(x,-y)-a_R(-x,-y).

The four supports are disjoint. They have radius S=o(R), so their mutual distances are bounded below by a positive multiple of R.

The supremum and all first Cartesian derivatives of q_R are bounded independently of R. The apparent angular derivatives in(9) cost1/s, but s>=1 wherever they occur. The outer cutoff costs1/S<=1. Therefore its ordinary global alpha-Holder seminorms are bounded uniformly. For a fixed x, either q_R(x,.) is identically zero or |x|>=cR. This proves the divided vertical bound, including pairs with one endpoint outside the support. Consequently

 ||q_R||E2<=C_alpha,
 ||q_R||L2(w_gamma)^2<=C_gamma R^(-gamma)S^2<=C_gamma    (10)

in the weighted case. Every q_R is smooth and compactly supported, with J(q_R)=0.

At the central point X_R, the primary packet in(9) and kernel(8) give exactly

 n_R.U[a_R](X_R)
 = (1/(2pi)) integral_0^(2pi)(-n_R,1 sin2phi+n_R,2 cos2phi)^2 dphi
                      integral_0^infinity chi_in(s)chi_out(s/S)ds/s
 = (1/2) integral_0^infinity chi_in(s)chi_out(s/S)ds/s
 >= (1/2)log S-log2.                                  (11)

The sign is unchanged when X_R-X replaces X-X_R because both kernels have even total parity. Each of the other three packets contributes at most CS^2/R^2 in absolute value at X_R, by its area and separation. Thus

 n_R.U[q_R](X_R)>=(delta/2)logR-C-CS^2/R^2.              (12)

## Exact strain correction and maximal-domain membership

The strain kernel is Kc(X)=y(3x^2-y^2)/(pi|X|^6), of homogeneity-3. Every point in the four packets has radius comparable to R. Hence

 |c[q_R]|<=C S^2 R^(-3).                               (13)

Fix once and for all a smooth compact physical-parity function phi with c[phi]=1 and support away from the axes and origin. It exists by choosing a nonnegative bump near radius1,angle pi/6, adding even-x and odd-y reflections, then dividing by its positive kernel integral. Set

 h_R=q_R-c[q_R]phi.

Then c[h_R]=0 exactly and J(h_R)=0. By(10)-(13), ||h_R||B<=C_B. Its canonical velocity contribution from phi is O(r^-3), since its integral is zero by oddness and the order-zero velocity kernel admits a first multipole expansion outside fixed compact support. In particular the correction to(12) is O(S^2 R^-6), and

 n_R.U[h_R](X_R)>=(delta/2)logR-C-CS^2/R^2-CS^2R^-6.    (14)

Each h_R is smooth, compactly supported away from x=0 and the origin. The actual vector field V is C1 on its support, including at any radial joins. Thus T h_R=(V.grad-1)h_R is C1, compactly supported in the same axis-separated sets, and belongs to E2 and Y_gamma. By the bounded coupling theorem, h_R is in the actual full maximal domains of A0 and Lren as well. These are membership statements for each R, not uniform graph estimates.

## Lower bound and exact scope

For large R, beta_R(X_R)=1, and H0 vanishes there. Since c[h_R]=0,

 (beta_R Cren h_R)(X_R)=(beta_R C0 h_R)(X_R)
                        =grad rho0(X_R).U[h_R](X_R).

Equations(7),(14), S/R->0 and delta>0 show that its absolute value is at least b_B R^(k-1)logR. The supremum term is part of either output norm. Dividing by the uniform upper bound for ||h_R||B proves the first inequality in(1), with witnesses in B0 and in the specified maximal domains. The middle inequality is restriction to a subspace. This completes the proof.

In particular no uniform bound CR^(k-1) without logR can hold on B0 or B. The full C0 on unrestricted inputs may have the slower nonzero moving-column rate described separately in proof 243; no use of that pending sharp lower-bound theorem is needed here. This result removes only the strain direction when asserting the faster full-C0 rate. It gives no information about a global inverse, and no numerical constant or output quadrature is certified.

Dependencies: proof 213 for the exact spaces and strain convention; proof 214 and proof 226 with binding clarifications for the E2 product and cutoff bounds and canonical velocity; proof 217 for the columns; proof 222 with binding clarifications for the exact nonzero leading far coefficient. This entire informal proof precedes any computation. No computation is needed. An actual independent review is requested before adoption as a theorem.
