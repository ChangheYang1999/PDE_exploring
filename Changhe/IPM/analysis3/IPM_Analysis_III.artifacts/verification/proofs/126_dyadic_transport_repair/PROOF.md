# A dyadic repair of the large-parameter transport inverse

## Exact hypotheses and statement

Use the spaces, weights, cutoffs and parity of proof 123. In particular sigma=25/4, s_0=41/20, b(t)=exp(3t)a(t), and X_s has the bulk variable v=h/b and sector variable w=chi h/(b p). Use the equivalent Littlewood-Paley Hilbert norm

 ||h||_D^2=sum_(j>=0) ||2^{j s(.)} Delta_j v||_2^2
              +sum_(j>=0) 2^{2j sigma}||Delta_j w||_2^2. (1)

The inhomogeneous block j=0 is included. Smooth Fourier cutoffs on R_t x S^1 are fixed. This is an equivalent norm on the exact same closed space X_s; no new functions or trace conditions are introduced.

Let W=(q,vartheta) be the cylindrical transport field, and let

 c_1=2V_1/x+V_2/y+q a'/a-1,
 c_2=q(3+a'/a)-1.

Assume:

1. W,c_1,c_2 belong to W^(7,infinity) on the cylinder, are compatible with the coordinate reflections, and W is tangent to the axes. The displayed divided velocity coefficients extend across the axes with this regularity.
2. The full-plane flow is complete and its transport group e^{-tau}h o Phi_tau on the low space R has the verified maximal generator T_R.
3. The order function has all the properties in proof 123 and W.grad s>=0 everywhere.

Then there is a finite real omega such that

 ||e^{-tau}h o Phi_tau||_D <= exp(omega tau)||h||_D,
 tau>=0.                                                (2)

The restricted semigroup is strongly continuous on X_s. Its generator is precisely T with domain

 D_X={h in X_s:T_R h in X_s},                            (3)

where derivatives are distributional. After increasing omega to exceed the low growth bound, for every lambda>omega,

 (T-lambda)^(-1)f=-integral_0^infinity
                    exp(-lambda tau)e^{-tau} f o Phi_tau d tau,
 ||(T-lambda)^(-1)f||_D <= ||f||_D/(lambda-omega).         (4)

Thus H2 holds with M=1 in the norm(1). In any fixed equivalent left-quantization norm it holds with a finite equivalence factor M. No claim that M remains1 under an arbitrary change of norm is made.

For the actual modal field, hypothesis1 is satisfied: the finite-angle Green formulas express q, vartheta and the divided velocity coefficients through the C6 density and its radial integrals. Each coefficient is C6 with bounded piecewise seventh weak derivative; no atom occurs in the seventh derivative because the sixth derivative is continuous. The normalized origin and infinity expansions give uniform cylinder bounds. This verifies W^(7,infinity), not smoothness of every order. Hypothesis2 is the already verified low transport realization. Hypothesis3 remains an explicit condition on the chosen order function.

## A finite-regularity dyadic estimate

We record the estimate needed to avoid an unjustified smooth-symbol expansion. Let m(x) be a bounded smooth order on the two-dimensional cylinder, with

 2<m_0<=m(x)<=m_1<7,

and uniformly bounded derivatives. Define ||u||_m by the first sum in(1). For a vector field B and scalar c in W^(7,infinity),

 (sum_j ||2^{jm(.)}[Delta_j,B.grad]u||_2^2)^(1/2)
       <=C_B ||u||_m,
 ||cu||_m<=C_c||u||_m.                                  (5)

The constants depend on the fixed Fourier resolution, finitely many bounded derivatives of m, and the indicated coefficient norms. They are uniform on translations of a fixed coordinate patch.

Here is a proof that specifies the finite regularity used. Smoothness and boundedness of m imply the scale-moderateness bound

 2^{j(m(x)-m(y))} <= C(1+2^j dist(x,y))^L                (6)

for some finite C,L independent of j,x,y. It follows by using the Lipschitz bound when the points are close and the bounded oscillation of m otherwise. Since each dyadic kernel is Schwartz at scale2^{-j}, insertion of (6) preserves integrable kernels, with any desired additional decay by choosing the original kernel seminorm of higher order. Neighboring dyadic weights are uniformly comparable.

Here is a direct finite-regularity bound for the high-coefficient terms. Write u_k=Delta_k u and B_k=Delta_k B, with an enlarged dyadic resolution when needed. For k>=1, the cancellation of the annular Fourier kernel and seven bounded weak derivatives give

 ||B_k||_infinity<=C 2^(-7k)||B||_(W^(7,infinity)).         (7a)

In a paraproduct decomposition, the portion in which the coefficient frequency is at least the input frequency minus a fixed number is a finite sum of terms B_k.grad S_(k+C)u. Its output at frequency j is zero unless k>=j-C. Hence, since m<=m_1,

 ||2^(jm(.)) Delta_j sum_k B_k.grad S_(k+C)u||_2
 <=C 2^(jm_1) sum_(k>=j-C) 2^(-7k)||u||_H^1
 <=C 2^(-(7-m_1)j)||u||_H^1.                             (7b)

The j=0 term uses the bounded low-frequency coefficient as well. The square sum of (7b) converges because m_1<7, and ||u||_H^1<=C||u||_m since m>=m_0>2. Thus no coefficient norm on the whole infinite cylinder is assumed to be integrable.

The remaining low-B/high-u terms can be written, up to finitely many neighboring blocks, as

 [Delta_j,S_(k-C)B].grad u_k
       +(S_(k-C)B-B).grad Delta_j u_k,  |j-k|<=C.        (7c)

For the first term the kernel contains the difference B(x)-B(y), bounded by ||grad B||_infinity |x-y|. The factor |x-y| at kernel scale2^(-j) cancels the derivative at frequency2^k. Insert (6) and use weighted Young's inequality to obtain C||grad B||_infinity ||2^(km(.))u_k||_2. For the second term use ||S_(k-C)B-B||_infinity<=C2^(-k)||grad B||_infinity and the weighted Bernstein bound ||2^(jm(.))grad Delta_j u_k||_2<=C2^j||2^(km(.))u_k||_2. That Bernstein bound follows from (6) applied to an enlarged frequency cutoff. A finite-neighbor square sum proves the first estimate in (5). The paraproduct decomposition used in (7b)-(7c) follows simply by partitioning the pairs of dyadic coefficient and input frequencies; its bounded overlap does not change the constants.

For the product estimate replace grad S_(k+C)u by S_(k+C)u in (7b), and use boundedness of the low-frequency coefficient and (6) for the low/high part. This uses ||u||_2 instead of ||u||_H^1. These arguments apply to vector components separately, and prove (5) using only the stated global W^(7,infinity) bounds.
These estimates apply first to compactly supported functions of regularity above m_1, and extend by completion. They do not use a symbolic expansion requiring infinitely differentiable coefficients. For the scalar coefficient in (5), its full value is included in C_c; it need not have a sign.

## Energy estimate on the bulk chart

Let h_tau=e^{-tau}h_0 o Phi_tau, initially with smooth compactly supported parity-compatible data satisfying the exact zero-axis condition. The bulk variable obeys

 partial_tau v=W.grad v+c_2 v.

Write v_j=Delta_j v and m_j=2^{j s(.)}. Integration by parts gives

 (1/2) partial_tau ||m_j v_j||_2^2
 =-integral [div W/2+j log(2) W.grad s]|m_j v_j|^2
   +Re <m_j[Delta_j,W.grad]v,m_j v_j>
   +Re <m_j Delta_j(c_2 v),m_j v_j>.                     (7)

The logarithmic term is nonpositive by hypothesis3, exactly, without a Garding remainder. The divergence is bounded. Sum(7), apply(5) and Cauchy-Schwarz, and discard the logarithmic term. The result is

 (1/2) partial_tau ||v||_s^2<=C||v||_s^2.                (8)

The coefficient regularity and the initial core ensure enough regularity to justify the integrations and the infinite sums for every finite time. In particular the flow and the chart multipliers are W^(7,infinity) on bounded-time compact sets. Alternatively one may take finite dyadic sums in(7) and pass to the limit using the same summable bounds.

## The cofactor chart and overlap

The uncut cofactor u=h/(b p) satisfies partial_tau u=W.grad u+c_1 u wherever defined. Thus w=chi u satisfies

 partial_tau w=W.grad w+c_1 w-(W.grad chi)u.              (9)

The forcing in (9) is -(W.grad chi)v/p. Its coefficient is supported in a fixed overlap where p is nonzero and s=sigma on a larger neighborhood. Smooth localization in this neighborhood maps H^{s(.)} boundedly into H^sigma. The coefficient belongs to W^(7,infinity), so the product estimate yields

 ||(W.grad chi)u||_H^sigma<=C||v||_s.                    (10)

Apply the constant-order version of(5) to(9), and combine with(8). The result is

 (1/2) partial_tau ||h_tau||_D^2<=omega ||h_tau||_D^2.

Gronwall proves(2) on the core. This treatment includes the complete overlap term and does not identify two nonlocal order reductions merely because their symbols agree on a support.

## Core, trace preservation and strong continuity

The core used above is dense in X_s. One way to verify the only nonstandard point is to smooth the even cofactor in H^sigma and then correct its axis trace with a bounded even right inverse of the trace map H^sigma(R^2)->H^(sigma-1/2)(R). Locally such a right inverse is given in tangential Fourier variables by

 E g hat(xi,z)=ghat(xi) phi(z<xi>),

where phi is even Schwartz with phi(0)=1, followed by a fixed normal cutoff. Scaling in z proves its H^sigma bound. For smooth g it is smooth and even. The trace corrections tend to zero, since the target trace is zero. A radial cutoff then gives compact support while preserving that zero trace. Glue this approximation to the bulk approximation away from the axis in the constant-order overlap. This proves density while retaining both parity and the exact trace condition.

The axis is invariant under the flow. The ratios of its normal and tangential coordinate factors solve ODEs with the divided velocity coefficients from hypothesis1. Therefore the transformed cofactor is a nonzero W^(7,infinity) multiplier times the initial cofactor composed with the flow; a zero axis trace stays zero. No extra pointwise normalization is imposed.

For core data, the flow on every finite time interval and the transformed cofactor are W^(7,infinity) and compactly supported in a bounded t interval, since W is bounded. They lie in H^7, which is above sigma, and they vary continuously in the weaker norm(1). Bound(2) and density extend the semigroup to all X_s and prove strong continuity. The extension agrees with the low semigroup because X_s embeds continuously in R and the two agree on the core.

## Generator and inverse

If h belongs to the X_s semigroup generator domain, its distributional derivative is T_R h, so it belongs to(3). Conversely, if h and T_R h lie in X_s, then h lies in the low maximal domain. The low semigroup identity

 S_tau h-h=integral_0^tau S_v T_R h dv

holds in R. Its right side is also a Bochner integral in X_s by(2) and strong continuity. The continuous embedding identifies the equality in X_s. Divide by tau and let tau tend to zero to obtain the X_s generator derivative. This proves(3), including closedness.

For lambda>omega, the Laplace integral in(4) converges in X_s and is the inverse of T-lambda by the semigroup generator identity. It agrees with the selected low inverse after omega is enlarged to exceed the low growth bound. Injectivity also follows directly from that low inverse. The norm estimate is the integral of exp(-(lambda-omega)tau).

## Scope

This proves H2 under the strengthened, actually available W^(7,infinity) coefficient hypothesis and the explicit monotone smooth-order hypothesis. It repairs the C5 failure in proof 124. It proves neither existence of a monotone order function with the global geometric specifications nor H3, low injectivity, a numerical inverse constant or uniform estimates for rough nonlinear perturbations.
