# Nonlinear derivative loss persists in the joint cofactor Holder graph

## Exact statement and hypotheses

Use the exactly joined, scalar-normalized trial rho0 and the canonical velocity U and strain c. Fix

 0<alpha<1, 2k-1<beta<k, gamma>4k,
 k=1615536043799051/9007199254740992.

Let Z3, D3, T, C0, Cren, A0=T+C0 and Lren=T+Cren be exactly those of proof 236. Thus h=x^2 g with g continuous, even in x, odd in y, and

 ||h||Z3=||chi g||C^alpha
   +sup_(R=1,2,4,...) R^(2-beta)(||g||_(infinity;A_R)+R^alpha[g]_(alpha;A_R))
   +||h||L2((1+r^2)^(-gamma/2)), A_R={R<=r<=4R}.

Use the physical transport T=V.grad-1, V=ell X+U[rho0], ell=1/k, and its exact distributional maximal domain. Proof 236 supplies boundedness of both complete couplings on Z3. No global inverse is assumed. The graph norm for L=T, A0 or Lren is ||h||Z3+||Lh||Z3.

On smooth compact physical-parity inputs define

 N(h)=(U[h]+(c[h]/3)X).grad h.

There are a fixed compact set K separated from both coordinate axes and smooth real h_n supported in K such that

 J(h_n)=c[h_n]=0,
 sup_n (||h_n||Z3+||Th_n||Z3+||A0h_n||Z3+||Lrenh_n||Z3)<infinity,
 ||N(h_n)||Z3>=b n                                                   (1)

for all sufficiently large integers n and some b>0. Each input and image appearing here belongs to the stated space. Consequently N has no continuous extension at zero from any of these graph topologies that agrees with N on the smooth core.

There is a stronger conditional range statement. For L=T, A0 or Lren, every v in its maximal domain satisfying Lv=N(h_n) obeys

 ||v||Z3>=b_L n.                                                      (2)

This statement does not assert that any such v exists. If a right inverse is defined on all these nonlinear images, its composition with N cannot be continuous at zero in the graph topology. No nonlinear nonexistence theorem or failure of an estimate in a stronger norm follows.

## Compact supports and equivalence of local norms

If a smooth f is supported in a fixed compact K with dist(K,{x=0})>0, multiplication by a fixed smooth function equal to 1/x^2 near K gives

 ||f||Z3<=C_K||f||C^alpha(R2).                                         (3)

Only finitely many dyadic annuli meet K, the weights are bounded there, and the weighted L2 norm is bounded by the supremum times a fixed finite volume. The global cofactor f/x^2 is extended by zero near the axis. The same estimate applies to a finite union of reflected boxes.

Conversely, on a fixed compact neighborhood K' of these boxes,

 ||f||C^alpha(K')<=C_K'||f||Z3                                        (4)

for arbitrary f in Z3. This follows from the local and annular controls of its cofactor, multiplication by x^2 and finitely many overlapping annuli. These comparisons do not assert that the nonlocal linear image of a compact input has compact support. Its global membership will use the separately proved coupling bound.

## A regular analytic flow box and an exact transverse velocity

Choose a point Q in the first quadrant, away from the origin and inside an innermost analytic radial cell. It can be taken near enough to zero that V1(Q) is nonzero: the exact expansion V1=-A x+O(r^3), A=2ell-1>0, ensures this on a small cone with x comparable to r. Choose a sufficiently small box around Q, separated from both axes and radial joins. All coefficients are smooth there by the actual finite inner formulas. Its three reflected boxes can be made disjoint.

The flow map (s,z) -> Phi_s(Q+z nu), where nu is transverse to V(Q), has nonsingular derivative. Smooth flow coordinates therefore exist with

 V.grad s=1, V.grad z=0.                                             (5)

Choose a fixed vector w with w.grad z>0 at Q and shrink an inner tube so that w.grad z>=b_*>0 throughout it. Choose a compact smooth potential P0 supported in the larger box and equal on a neighborhood of that tube to

 (w2/2)(x-Qx)^2-w1(x-Qx)(y-Qy).

Reflect P0 evenly in x and oddly in y to get P, and put d=-Delta P. The canonical multiplier of U is (xi eta/(xi^2+eta^2),-xi^2/(xi^2+eta^2)), so direct Fourier multiplication gives exactly

 U[d]=(-P_xy,P_xx).                                                   (6)

The compact potential fixes the canonical full-plane velocity; no harmonic or constant velocity is added. On the inner tube U[d]=w and d=-w2, hence grad d=0. Both d and U[d] vanish near zero. The canonical strain identity then gives c[d]=0, and J(d)=0. This is an exact construction of a transverse velocity.

## Graph-bounded characteristic strips with exact zero strain

Fix a smooth eta(s), supported strictly inside the flow coordinate interval and equal one on a neighborhood of [0,tau], with tau>0 fixed and small. Choose a smooth compact Psi on the real line equal z^2 on neighborhoods of both 0 and 1. In the first flow box put

 k_n^0=n^(-alpha)Psi(nz)eta(s),

and extend with the physical density parities to the other boxes. For large n the supports remain within the fixed boxes. Their amplitude is O(n^(-alpha)), area O(n^(-1)), and Lipschitz norm O(n^(1-alpha)). The global C^alpha norm is uniformly bounded: split every difference at distance 1/n and use respectively the Lipschitz and supremum bounds. Equation(5) also gives

 V.grad k_n^0=n^(-alpha)Psi(nz)eta'(s),

so the same estimates bound its C^alpha norm uniformly. All coordinate cutoffs vanish near the patch boundaries, and the zero extension is smooth.

The strain kernel is smooth on these boxes. Therefore |c[k_n^0]|<=C n^(-alpha-1). Choose a fixed compact smooth physical-parity zeta, supported in the outer boxes and vanishing on neighborhoods of the inner flow tubes, with c[zeta]=1. Such a zeta is obtained by placing a bump where the strain kernel is nonzero, projecting to the density parities, and dividing by its nonzero strain integral. Its zero set has no open subset in a quadrant. Put

 k_n=k_n^0-c[k_n^0]zeta, h_n=d+k_n.                                  (7)

Then c[h_n]=J(h_n)=0 exactly. The correction has C^alpha and transport C^alpha norms O(n^(-alpha-1)). Equations(3),(5) imply

 ||h_n||Z3+||Th_n||Z3<=C.                                            (8)

Every h_n is smooth and compact, so (8) gives its membership in the exact transport domain without a density assumption. Boundedness of C0 and Cren on Z3 proves the uniform bounds for both full linear images in(1), including all their distant and near-axis values.

## The nonlinear image is admissible and large

For each fixed n, h_n is smooth and compact; its canonical Riesz velocity is smooth on every compact set. N(h_n) is therefore smooth and supported where grad h_n is supported, within K. Thus N(h_n) belongs to Z3 by(3). It is not being tested in a target from which it is excluded.

We need the velocity of the thin strip to tend to zero in supremum. Its density has amplitude O(n^(-alpha)) and bounded C^alpha seminorm. In a kernel ball of radius 1/n, Holder cancellation gives O(n^(-alpha)). Between radii 1/n and a fixed support scale, the amplitude bound gives O(n^(-alpha)log n). Outside that scale the compact-source kernel is absolutely integrable; the local multiplier part of U has the same amplitude bound. The small fixed correction in(7) is harmless. Consequently

 ||U[k_n]||infinity<=C n^(-alpha)(1+log n) ->0.                        (9)

On the inner flow tube eta=1, grad d=0 and the compensator and its derivatives vanish. Since c[h_n]=0, equations(6)-(7) give

 N(h_n)=n^(1-alpha)Psi'(nz)(w+U[k_n]).grad z.                          (10)

Along z=0 the value is exactly zero because Psi'(0)=0. Along z=1/n it is at least b_* n^(1-alpha) for large n because Psi'(1)=2 and(9) tends to zero. This lower bound is uniform over 0<=s<=tau. The two trajectories are at distance at most C/n. Their two-point quotient is therefore at least c n in C^alpha. Equation(4) proves the nonlinear lower bound in(1).

Multiplying h_n by n^(-1/2) produces a sequence converging to zero in each graph norm. The nonlinearity is exactly homogeneous of degree two, so its Z3 norm remains bounded below by b. This proves discontinuity at zero, already on smooth inputs with c=J=0. For these inputs the quadratic term is simply U[h].grad h, so no variation of the scalar normalization creates the effect.

## Any preimage must retain the transverse growth

Let L=T+C where C=0,C0 or Cren, and suppose v is a maximal-domain solution of Lv=N(h_n). On the two fixed flow tubes, v and Cv have C^alpha norms bounded by C||v||Z3, by(4) and boundedness of C. In a smooth flow box the distributional equation has the exact orbit form

 exp(-tau)v(Phi_tau X)-v(X)
  =integral_0^tau exp(-s)(N(h_n)-Cv)(Phi_s X)ds.                       (11)

To justify(11), pull the continuous distributional equation into the flow coordinates. The one-dimensional distributional fundamental theorem holds for almost every transverse coordinate, and continuity in both coordinates extends the identity to every coordinate. No transverse derivative of v is assumed.

Subtract(11) at initial transverse coordinates 0 and 1/n. Equation(10) makes the difference of the nonlinear integrals positive and at least b_*(1-exp(-tau)) n^(1-alpha). The endpoint differences and the integral of Cv differences are each bounded by C||v||Z3 n^(-alpha), since the trajectories stay at distance at most C/n. This proves(2).

For the rescaled inputs n^(-1/2)h_n, every preimage of their nonlinear image has norm at least b_L by linearity. Hence any selection of preimages, if it exists for all these images, fails continuity at zero. This conclusion does not require injectivity, a bounded global inverse or a prescribed choice of preimage. If some nonlinear image is outside the range, the corresponding assertion of existence remains false or open; the lower bound(2) is only a statement about preimages that exist.

## Dependencies and limits

Proof 207 supplies the same exact compact-potential and characteristic-strip mechanism in E2. It is fully restated above, with the additional full-cofactor norm comparison and actual full-domain checks. Proof 236 supplies the exact Z3 realization and bounded complete coupling; proof 234 is its divided-velocity input. The regular analytic box follows from the original finite inner trial formulas and exact origin expansion.

The conclusion refutes continuity of this semilinear graph-to-target map and of any inverse composition on these images. It does not rule out stronger domains, derivative-bearing norms, a quasilinear formulation, different iteration variables or profile existence. It gives no certified constant for a contraction argument and no global linear inverse. Independent independent review is requested before adopting the new Z3 statement.
