# A precise global triangular realization of pure transport

## Statement and spaces

This is a conditional pure-transport theorem. It does not include the nonlocal velocity coupling. It supplies the jet lift, its transport error, the remainder domain and the index for the uncoupled endpoint of a possible homotopy.

Fix ell>1, k=1/ell, D=4ell-1, a=17/4 and eta=5/4. Let V be a globally Lipschitz C1 real vector field on R2, with div V=2ell and the IPM reflection parities: V1 odd in x and even in y, V2 even in x and odd in y. Its flow is denoted by Phi_s. Assume V1/x and V2/y, extended to the axes, are bounded. Put

 q(X)=V(X).X/r^2,
 v1=V1/x, v2=V2/y,
 d(t)=V2(0,e^t)/e^t,
 b(t)=D-d(t)-2d'(t).

Assume the positive-axis-rate and exponential endpoint hypotheses (1) of V041, with nu_->1/4. For the coefficient estimates below assume there exist finite constants M_P,M_Q such that, at every off-axis point,

 |q(r,theta)-d(log r)| <= M_Q cos(theta)^2,
 |2v1+v2-1-b(log r)| <= M_P min(r^2,1) cos(theta)^2.          (1)

These are explicit hypotheses on the entire prescribed field. They encode angular regularity and the normalized linear part at0.

Define

 w=|cos(theta)|^(-2a) exp(mu(log r)),
 mu(t)=-2a t for t<0, mu(t)=-eta t for t>=0,
 R=L2_P(w dX),
 G=L2(e^(-t/2)dt on t<0; e^(27t/4)dt on t>=0).

The subscript P means even in x and odd in y. Let Gamma and B be the Hilbert spaces of V041 for sigma=1/4 and kappa=3/8+k. Gamma is equivalent to G, with the equivalence constants fixed by the prescribed d. Write

 A beta=d beta'+b beta,
 E beta=x^2y beta(log r).

Assume additionally that the transport weight satisfies, almost everywhere away from x=0,

 kappa_w=1+ell+(mu'/2)q+a tan(theta) V.grad(theta) >= kappa_*>0,          (2)

and |kappa_w| is bounded. The values at the radial weight knot are immaterial.

Let T_R be the maximal distributional realization of V.grad-1 on R, with domain

 D(T_R)={h in R:(V.grad-1)h belongs to R as a distribution},
 ||h||_D=||h||_R+||T_R h||_R.

Define the direct sums

 X={E beta+h: beta in B, h in D(T_R)},
 Y={E gamma+f: gamma in Gamma, f in R},
 ||E beta+h||_X=||beta||_B+||h||_D,
 ||E gamma+f||_Y=||gamma||_Gamma+||f||_R.

Both decompositions are unique. Pure transport T=V.grad-1 is a bounded isomorphism X->Y. In these coordinates it has the exact triangular form

 T = [ A   0 ; B_V   T_R ],
 B_V beta=x^2y{[2v1+v2-1-b]beta+[q-d]beta'}.               (3)

If ||A^(-1)||<=C_A and ||B_V||_(B->R)<=C_B, then solving T(E beta+h)=E gamma+f gives

 beta=A^(-1)gamma,
 h=T_R^(-1)(f-B_V A^(-1)gamma),
 ||h||_R <=kappa_*^(-1)(||f||_R+C_B C_A||gamma||_Gamma),
 ||T_R h||_R <=||f||_R+C_B C_A||gamma||_Gamma.              (4)

The cubic coefficient J=lim_(t->-infinity) beta(t) is continuous on X. Restricting J=0 leaves a closed codimension-one range whose condition is exactly the scalar compatibility integral in V041. Without that restriction the pure-transport index is0.

## The radial lift and its bounded error

For locally H1 beta, the distributional product and chain rules give

 (V.grad-1)(x^2y beta(log r))
 =x^2y[(2v1+v2-1)beta+q beta'].

On x=0, div V=2ell gives partial_x V1=2ell-d-d'. Hence the axis coefficient is d beta'+(D-d-2d')beta=A beta. This proves (3) on a dense smooth core and then distributionally.

The angular factors in (1) imply

 ||B_V beta||_R
 <=sqrt(C_ang)[M_P||m beta||_G+M_Q||beta'||_G],
 C_ang=integral_0^(2pi)|cos(theta)|^(8-2a)sin(theta)^2 dtheta<infinity,
 m(t)=min(exp(2t),1).                                      (5)

Indeed x^2y cos(theta)^2=r^3 cos(theta)^4 sin(theta), and the radial squared density measure is exp((8-2a)t)dt at0 and exp((8-eta)t)dt at infinity, exactly the weight of G. The angular exponent is8-2a=-1/2.

To prove the two scalar quantities in (5) are bounded by ||beta||_B, write beta=Hz as in V041. At negative infinity H and its reciprocal are bounded, H'=O(exp(nu_- t)), and z=J+(z-J). The B norm controls z-J and z' with weight exp(-t/2). The extra factor m controls the constant J, since4-1/2>0. The term H'J is also integrable since2nu_- -1/2>0. At positive infinity H is comparable to exp(-(3-k)t), H'/H is bounded, and

 H^2 exp(27t/4) is comparable to exp(2(3/8+k)t).

The B norm controls z and z' with this last weight. On compact t intervals all these coefficient factors are bounded. Thus there are finite constants C_m,C_der determined by d such that

 ||m beta||_G<=C_m||beta||_B,
 ||beta'||_G<=C_der||beta||_B,
 C_B<=sqrt(C_ang)(M_P C_m+M_Q C_der).                        (6)

No smallness or compactness of B_V is asserted. In fact its Q term has a nonzero limiting coefficient at the normalized saddle. The triangular inverse does not require it to be compact.

## Maximal remainder transport

The bounded functions V1/x and V2/y show that each open quadrant is preserved by the global flow. For example x(s)=x(0) exp(integral_0^s (V1/x)(Phi_u)du), so a nonzero x cannot reach the vertical axis in finite time. The reflection subspace is invariant.

On smooth functions supported away from the axes, define

 S_s h=e^(-s) h(Phi_s), s real.

Change of variables under the C1 flow shows that its weighted norm has logarithmic derivative given by -2kappa_w along the inverse flow. Boundedness of kappa_w gives a bounded group on each finite time interval. In particular (2) gives

 ||S_s||_(R->R)<=exp(-kappa_* s), s>=0.                      (7)

The weight is locally positive and finite away from the axes, and these smooth functions are dense in R. The ordinary local convergence of the flow therefore proves strong continuity on a dense set; the local group bound extends it to all R. Its generator is the maximal distributional transport operator T_R.

Here is a direct justification of the last domain identification. Suppose h,f belong to R and V.grad h-h=f distributionally. Pair S_s h against a smooth test function phi compactly supported away from the axes and change variables Z=Phi_s X. The pairing becomes the integral of h(Z) against e^(-s) phi(Phi_(-s) Z) times the Jacobian of Phi_(-s). Differentiation in s and the weak equation show that its derivative is the pairing of S_s f against phi. This use of a C1 transported test is justified by approximating it in C1 on its compact support by smooth tests: h and f are locally integrable there, and V is C1. All supports stay a positive distance from the axes on bounded time intervals. Integration in s gives

 S_s h-h=integral_0^s S_u f du

first distributionally and then in R, by the local group bound. Strong continuity of S_u implies that the difference quotient tends to f in R. Conversely a generator derivative gives the weak transport equation by the same test pairing. This identifies the generator with the maximal domain and works unchanged at stationary points of V; no nonvanishing-flow coordinate is assumed.

The Bochner integral

 T_R^(-1)f=-integral_0^infinity S_s f ds

converges by (7), satisfies the distributional equation and has norm at most1/kappa_*. If T_R h=0, the variation identity gives S_s h=h, and (7) forces h=0. Hence T_R is an isomorphism from its graph domain to R and is closed. This argument uses no Riesz-transform or edge estimate.

## Direct sums, inverse and normalization

If E beta belongs to R, then for almost every r its angular squared integrand contains |cos(theta)|^(4-2a)sin(theta)^2 times |beta(log r)|^2. Since4-2a=-9/2, this is integrable only when beta(log r)=0. Thus B and R have trivial intersection under E. The same reasoning proves uniqueness on the target. Completeness follows from the Hilbert completeness of the factors and the graph closedness of T_R. The displayed sum norms are equivalent to Hilbert product norms.

V041 gives A:B->Gamma invertible and a continuous trace J. The boundedness (6), the remainder inverse, and the triangular formula prove (4), surjectivity and injectivity. If J is fixed to0, V041 identifies the scalar range as the kernel of the nonzero bounded functional gamma -> integral_R gamma/(dH); the remainder f stays arbitrary because T_R is onto. This is a closed codimension-one range and the restricted operator remains injective.

## Application status

The exact modal field has the relevant local and far formal expansions for (1), and the required C1 regularity is already verified. A complete application still needs checked global bounds in (1), the positive axis rate, and the positive transport margin (2). These conditions are weaker than a full nonlocal edge theorem, but they have not all been certified here. The theorem supplies a rigorous conditional uncoupled endpoint. It does not prove that the coupled homotopy stays Fredholm, that the coupling maps X into Y, or that the normalized nonlinear equation has a solution.
