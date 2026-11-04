# Carrier flatness under arbitrarily slow supercritical radial envelopes

Status: C71 and C72 are confirmed at the exact scopes below after the complete ten-item coordinator comparison. The construction supplies the carrier system, with no pressure or scalar completion provided.

## 1. Exact theorem and scope

Fix 0<c<1/2 and omega in R, Jx=e3 cross x, A=cI-omega J, L=(1-c)I+omega J and X(x)=Ax. Let sigma:D->R3 minus {0} be a smooth section on a planar disc about zero, with det(sigma_1,sigma_2,X(sigma)) nonzero. There exists a constant Cstar>=1, depending only on c, omega and a fixed relatively compact section disc, with the following property.

For every positive finite-valued function lambda:(0,rho1)->(0,infinity) satisfying lambda(r)->infinity as r decreases to zero, there exist r0>0, t0>0 and a smooth V on the flowbox

    Phi(y,t)=exp(tA)sigma(y), |y|<r0, |t|<t0,

such that

    div V=0, X.V=0, DV X=-LV, W=curl V,                      (C)

V is flat precisely along the central orbit y=0, is nonzero everywhere off that orbit, and on its section

    Q1(y)+Q2(y) <= Cstar+lambda(|y|)/|y|,
    Q1=|W.X|/|V|, Q2=|W|/|V|, 0<|y|<r0.                    (1)

Both Q1 and Q2 belong to every Lp with 0<p<2 and to no L2 on any centre disc. The Lp statements concern these measurable ratios; lambda itself need not be measurable, since the proof uses only its pointwise limit and a smooth lower envelope.

Thus, by the confirmed L2+C0/|y| continuation criterion A2501-A2505, its inverse-radius summand cannot be replaced by lambda(|y|)/|y| for any such diverging lambda. A constant Cstar is itself L2 on the disc, so these fields meet the proposed weakened criterion but do not vanish near the flat point. This is optimality only on the stated scale of pointwise radial envelopes for C. It is not a classification of all non-L2 coefficients or all weak-L2 potentials, and says nothing about existence in the full common-flat system F.

The submitted C71 statement has the parameter restriction omega=0 or c=1/3 and concerns Q1. The independent argument below supplies every omega by the exact radial correction already checked in A2482-A2484. We check the general radial factor rather than assume that a proof for one factor automatically applies to all factors.

## 2. Fixing geometric constants before the envelope

Choose once a relatively compact section disc D_R with R<1 and a finite flowbox time interval on which Phi is a diffeomorphism. On its closure put

    j=|det(sigma_1,sigma_2,X(sigma))|,
    beta_i=X(sigma).sigma_i/|X(sigma)|^2,
    b=(3c-1)beta.

All coefficients and their derivatives of each fixed order are bounded, and j and |X(sigma)| have positive lower bounds. For any positive nondecreasing smooth radial factor g on (0,r0), r0<=R, define the polar correction

    q(r,theta)=r^-1 integral_0^r s b_theta(s,theta)g(s)
                         exp(integral_s^r b_r(u,theta) du) ds,
    w=g(r)e_theta+q(r,theta)e_r.                             (2)

The fixed coefficient bounds and monotonicity of g give, with constants independent of g and r0,

    |q|<=C r g, |q_theta|<=C r g,
    q_r=b_r q+b_theta g-q/r, |q_r|<=C g,
    |w|>=g, |Dw|<=C(g'+g/r+g).                              (3)

These are precisely the elementary estimates from A2482, and depend only on g'>=0, not on a special logarithmic expression. The exact identity div w=b.w follows by differentiating rq.

Set v=w/j, h=-beta.v, and lift

    V(Phi(y,t))=exp(-t)D Phi(y,t)(v(y),h(y)).                 (4)

The same fixed smooth matrices and their inverses give

    Q1+Q2 <= Cstar[1+g'/g+1/r]                              (5)

for some Cstar>=1 independent of g and r0. To verify (5), |V(sigma)|>=c1|w|, while |W(sigma)|<=c2(|Dw|+|w|), and |X(sigma)| is bounded. The t derivatives in (4) are bounded matrix multiples of v,h. Insert (3) and enlarge Cstar. This order of choices is essential: no constant selected after lambda is allowed to consume its prescribed envelope.

Now choose r0<R and r0<rho1 so that lambda(r)>=2Cstar for every 0<r<=r0; shrink further to make r0<1. Let T1=log(1/r0).

## 3. A smooth minorant that grows as slowly as required

For t>=T1 define

    mu(t)=inf_{0<r<=exp(-t)} lambda(r)/Cstar.

It is finite, nondecreasing, at least2 and tends to infinity. Finiteness follows by evaluating lambda at exp(-t); the lower bound and limiting assertion follow from the definition of lambda(r)->infinity. No regularity of lambda is needed.

Choose increasing times T_n, n>=2, so that T_2>=T1+1, T_(n+1)>=T_n+1, and mu(t)>=n+1 for every t>=T_n. Let chi be a fixed smooth nondecreasing function equal to zero on (-infinity,0] and one on [1,infinity). Define

    Lambda(t)=sum_(n>=2) chi(t-T_n), t>=T1.                  (6)

The sum is locally finite. At most one summand is nonconstant at a given t. Thus Lambda is smooth, nonnegative and nondecreasing; every derivative of order j>=1 is bounded by sup|chi^(j)|; and Lambda(t)->infinity. On [T_n,T_(n+1)), Lambda<=n-1, while mu>=n+1. Before T_2, Lambda=0 and mu>=2. Therefore

    Lambda(t)+1<=mu(t),
    Lambda(t)<=M1(t-T1), M1=sup|chi'|.                      (7)

These bounds hold also at the transition endpoints by smoothness and continuity of Lambda; mu is not required to be continuous.

Define

    G(t)=integral_(T1)^t Lambda(s) ds,
    g(r)=exp(-G(log(1/r))), 0<r<r0.                         (8)

Then g is positive, nondecreasing in r, and g'=Lambda(t)g/r. Because Lambda tends to infinity, for every M>0 there is C_M with G(t)>=Mt-C_M for all t>=T1. Consequently g(r)<=exp(C_M)r^M for every M.

All derivatives are flat, not merely the values. Induction gives

    g^(k)(r)=r^-k q_k(t)g(r),
    q_0=1, q_(k+1)=(Lambda-k)q_k-q_k'.                      (9)

The q_k are polynomials in Lambda and finitely many derivatives, with degree at most k in the unbounded variable Lambda. The bounded positive-order derivatives and (7) imply |q_k(t)|<=C_k(1+t)^k, with constants allowed to depend on T1. Choosing M>N+k+1 in the bound from (8) gives |g^(k)(r)|=O(r^N) for every k,N. No numerical evidence is needed for this induction.

## 4. Flat correction and complete carrier verification

Use (2) with this g. Every angular derivative of q is O(rg), by differentiating the Volterra integral: derivatives of the exponential factor are bounded combinations of integrals of bounded coefficient derivatives. Differentiating q_r=b_rq+b_theta g-q/r in r and theta then proves inductively

    |partial_r^k partial_theta^l q|
        <= C_(k,l) r^(1-k)(1+t)^k g(r).                     (10)

At the induction step, derivatives of 1/r multiply previously bounded derivatives of q, giving the required r power; derivatives of g obey (9); and all coefficient derivatives are bounded. As g beats every power, all these mixed derivatives, after multiplication by any fixed negative power of r, tend to zero faster than every prescribed power.

Cartesian derivatives of g e_theta+q e_r are finite sums of these polar derivatives times trigonometric factors and powers of 1/r. Therefore all Cartesian derivatives extend to zero with value zero. Difference quotients of the extended derivatives verify successively that these are the actual derivatives, so w is smooth and flat. It is nonzero on the punctured disc because its tangential component is g>0. The exact divergence identity extends to zero by continuity.

The lift (4) is smooth, flat on the central orbit, and nonzero off it because D Phi is invertible. Its coordinate components are exp(-t)(v,h), so [X,V]=-V and DV X=(A-I)V=-LV. Since exp(tA) is exp(ct) times an orthogonal matrix,

    X(Phi).V(Phi)=exp((2c-1)t)
                  X(sigma).(sigma_i v_i+hX(sigma))=0.

The coordinate volume density is exp(3ct)j, and hence

    div V=exp(-t)j^-1[div(jv)+(3c-1)jh]
         =exp(-t)j^-1[div w-b.w]=0.

This verifies every carrier equation for arbitrary omega. The zero set is exactly the central orbit, and any point off it is not flat because V is nonzero there.

## 5. Envelope, integrability and threshold conclusion

Insert g'/g=Lambda/r into (5). By (7) and the definition of mu,

    Q1+Q2 <= Cstar[1+(Lambda(t)+1)/r]
           <= Cstar+Cstar mu(t)/r
           <= Cstar+lambda(r)/r,

which proves (1) with the geometric constant selected before lambda. On the other hand Lambda(t)<=M1(t-T1), so each ratio is bounded by a constant times 1+(1+log(1/r))/r. For every 0<p<2 its pth-power integral on the disc converges, since the radial change of variables gives an exponentially decaying factor exp(-(2-p)t) times a fixed power of (1+t). This conclusion does not require lambda itself to have any integrability.

There is also a direct lower estimate, independent of continuation: A2509-A2510 apply to this derivative-flat monotone factor with ell(r)=r gprime/g=Lambda(log(1/r)) tending to infinity. They give constants 0<c0<C0prime such that c0 Lambda/r<=Qj<=C0prime Lambda/r for j=1,2 on a smaller punctured disc. Therefore Qj is not L2, and (Qj-C0/r)_+ is not L2 for every fixed C0>=0. Indeed, for small r this positive part is at least c0 Lambda/(2r), whose square integral contains a divergent integral of Lambda(log(1/r))^2 dr/r. Independently, the same conclusions follow from the confirmed carrier continuation A2471 and A2503. None requires integrability of lambda.

For the weakened continuation condition with the prescribed envelope, take B2=Cstar. It is L2 on the bounded section disc and (1) provides the exact inequality. V is smooth and flat at the centre but nonzero in every neighbourhood. This is an explicit counterexample to that weakened carrier criterion for every lambda tending to infinity and every omega. It does not say that every potential above C0/r admits a counterexample, nor that oscillatory or nonradial weak classes are classified.

## 6. Source comparison and limits

All three sections of the original C71 source were read. The smooth step sum, its derivative bounds, the recurrence for radial derivatives, and the order in which Cstar is chosen agree with Sections2-3. In its stated omega=0 or c=1/3 cases, the original proof uses the already checked integrating factor from C69 instead of (2), and is valid. Its corollary that the larger-envelope criterion fails follows directly from the nonzero constructed field; only calling this a sharp threshold also requires the continuation half C70.

The all-omega extension does not assume an integrating factor. It uses the field-dependent correction, whose bounds were checked for this general radial factor in Sections2 and4. No topological exactness claim has been reversed. The positive radial envelope and derivative bounds make the construction valid independently of any numerical residual or remote referee assertion.

The entire three-section C72 source was also read. Its explicit constants agree with Section2: if M0>=1 bounds b_r, b_theta and their angular derivatives on a radius below1, then |q|<=M0 exp(M0) r g/2, |q_theta|<=(M0+M0^2)exp(M0) r g/2, and |q_r|<=C1 g with C1=M0+M0 exp(M0)(M0+1)/2. Consequently |Dw|/|w|<=gprime/g+1/r+C2, where C2=C1+M0(M0+2)exp(M0)/2. A fixed geometric K>=1 with |V|>=|w|/K and |W|<=K(|Dw|+|w|) gives each of Q1,Q2 bounded using Cstar=K^3(1+C2), as in C72. Enlarging once before lambda controls their sum as in (1). Its radial derivative recurrence and all-order flatness use the same bounded positive-order derivatives of Lambda. No numerical residual is used.

No function S, pressure P or pressure-Poisson identity is constructed. Thus no completion to F, counterexample to its continuation consequences, or global Euler profile with decay is provided by this construction. A separate pressure-sign argument, LIT305, is not used here. The strongest unrestricted conjecture remains open. Existing configured model theory and coordinator collaboration proceeds through files; actual provider execution is not independently attested.

The complete ten-item coordinator comparison in the team records was read and checked against all six sections. It independently checks the fixed constants, minorant, derivative recurrence, original stream function, envelope, Volterra estimates, smoothness, all three carrier equations, integrability and exact scope. Its proposed phrase sharp threshold is used here only with the explicit radial-envelope quantifiers of Section 1. The source status-note changes do not alter the proofs.
