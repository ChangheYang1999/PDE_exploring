# Remainder continuation, the unshifted jet block, and the exact jet index change

## 1. Conditional block theorem

Let R be a Banach space continuously embedded in distributions on an open set. Let T be a distributionally closed transport expression with maximal realization

 D_R={u in R:Tu in R}, ||u||_(D_R)=||u||_R+||Tu||_R.

Distributionally closed means that u_n->u and Tu_n->f in distributions imply Tu=f. This holds for V.grad-1 with the prescribed C1 field. Let C_R:R->R be bounded, and suppose S_1=T+C_R:D_R->R is Fredholm of index0.

Let B and Gamma be Banach spaces with an isomorphism A:B->Gamma. Let the low domain and target be the coordinate direct sums Z=B direct-sum D_R and Y=Gamma direct-sum R, using the sum norms or their fixed Hilbert equivalents. Suppose the actual low operator has the exact decomposition

 L=M+K+c[.] zeta,
 M(beta,u)=(A beta, X beta+S_1 u),
 K(beta,u)=(Gamma_C(beta,u),0),                            (1)

where X:B->R, Gamma_C:Z->Gamma and c:Z->R are bounded. Suppose also L:Z->Y is Fredholm of index0. In the IPM application these are the already proved low realization and its exact jet/remainder decomposition, not a new frozen approximation.

Let X_H and Y_H be Banach spaces with continuous inclusions X_H->Y_H->R. Set

 D_H={u in X_H:Tu in Y_H}, ||u||_(D_H)=||u||_(X_H)+||Tu||_(Y_H).

Assume C_R:X_H->Y_H is bounded, with norm c_H. Assume the following quantitative hypotheses.

(H2) There are omega>=0 and M_0>=1 such that, for every lambda>omega, T-lambda:D_H->Y_H is bijective and its inverse has norm at most M_0/(lambda-omega) from Y_H to X_H.

(H3) Put lambda_*=omega+1+2M_0 c_H. There are C_1<infinity, a Banach space W, and a compact map K_H:X_H->W such that

 ||u||_(X_H)<=C_1||(S_1-lambda)u||_(Y_H)+||K_Hu||_W

for every u in D_H and every lambda in[0,lambda_*].

Let Gamma_H be a Banach space continuously embedded in Gamma, and define

 B_H={beta in B:A beta in Gamma_H},
 ||beta||_(B_H)=||beta||_B+||A beta||_(Gamma_H).

Assume additionally

(J1) X:B_H->Y_H is bounded;
(J2) Gamma_C:B_H direct-sum D_H->Gamma_H is compact;
(J3) zeta belongs to Gamma_H direct-sum Y_H.

Then L:B_H direct-sum D_H->Gamma_H direct-sum Y_H is Fredholm of index0. Its kernel embeds into the kernel of the same low operator on Z. If the low operator is injective, both low and high operators are bijective, and the high inverse is the restriction of the low inverse.

If in addition an independently proved high estimate has the form

 ||h||_(B_H direct-sum D_H)
 <=C_1'||Lh||_(Gamma_H direct-sum Y_H)+C_2'||h||_Z,         (2)

and the low inverse norm is at most K_L, then the high inverse norm is at most C_1'+C_2' K_L iota_Y, where iota_Y is the norm of the high-to-low target inclusion. Compactness alone supplies neither the constants in(2) nor their uniformity under perturbation.

## 2. Proof of the block theorem

A Cauchy sequence in D_H has limits u in X_H and f in Y_H for its T images. The continuous embeddings imply distributional convergence, hence Tu=f. This proves completeness. The same embeddings give a bounded inclusion D_H->D_R. The boundedness of T from its graph domain and C_R:X_H->Y_H makes the family S_1-lambda a continuous path of bounded operators D_H->Y_H.

At lambda_*, the resolvent identity gives

 S_1-lambda_*=[I+C_R(T-lambda_*)^(-1)](T-lambda_*),
 ||C_R(T-lambda_*)^(-1)||<=M_0c_H/(1+2M_0c_H)<1/2.

The inverse is bounded into D_H because Tu=f+lambda_*u. Hence the endpoint is an isomorphism. For each other lambda, (H3) and

 ||Tu||_(Y_H)<=||(S_1-lambda)u||_(Y_H)
                  +(c_H+lambda iota')||u||_(X_H)

give a graph-norm estimate modulo the compact map K_H, where iota'=||X_H->Y_H||. The kernel is finite dimensional and the range closed by the compactness argument in proof 104. The extended semi-Fredholm index is locally constant; the connected path from the invertible endpoint therefore has index0 throughout. This proves S_1:D_H->Y_H Fredholm of index0. Proof 104 contains both the full compactness argument and, for Hilbert spaces, an elementary finite-block proof of index stability.

B_H is complete by the same graph argument, now using the bounded map A:B->Gamma. The map A:B_H->Gamma_H is an isomorphism. Surjectivity follows by applying the low inverse A^(-1) to any gamma in Gamma_H. Its B_H norm is bounded by (1+||A^(-1)|| ||Gamma_H->Gamma||)||gamma||_(Gamma_H). Injectivity is inherited from the low map.

On the high direct sums, (J1) gives the bounded triangular factorization

 M=[[I,0],[X A^(-1),I]] diag(A,S_1).

The left factor has bounded inverse [[I,0],[-X A^(-1),I]]. Thus M is Fredholm of index0. By(J2), K is compact. The functional c is bounded on the high domain by its continuous inclusion into Z; by(J3), c[.] zeta is a bounded rank-one operator into the high target and hence compact. Formula(1) and compact perturbation invariance prove the asserted index.

All embeddings preserve the same distributional functions and the exact low block decomposition. Thus a high null vector is a low null vector. Under low injectivity, the high Fredholm operator is injective and therefore onto. The low Fredholm operator is also bijective, and uniqueness identifies the two inverses. Applying(2) to the high solution and then the low inverse bound proves the last estimate.

No identity shift is applied to the free jet in this proof. In particular it does not require B_H to embed into Gamma_H. The hypotheses about the high remainder and high coupling are still substantive analytic obligations.

## 3. Exact index of the shifted zero-jet row

Use the scalar data of proof 38. Thus ell>1, D=4ell-1, and d is positive C1 with positive upper and lower bounds and exponentially convergent limits D at negative infinity and ell at positive infinity. Let H be its integrating factor. Fix sigma,kappa>0 and

 omega_B(t)=exp(-2sigma t) for t<0, exp(2kappa t) for t>=0.

The scalar target is Gamma={gamma:gamma/(dH) in L2(omega_B dt)}. The domain B consists of beta=Hz with z' in L2(omega_B), z(+infinity)=0, and its full norm is the one in proof 38. Put B_0={beta in B:z(-infinity)=0}. Let

 A beta=d beta'+(D-d-2d')beta.

For every real lambda>=0, A-lambda:B_0->Gamma is bounded and injective. Its exact classification is

 0<=lambda<sigma D: Fredholm of index-1;
 lambda>sigma D: a bounded isomorphism;
 lambda=sigma D: dense, nonclosed range, hence not Fredholm.       (3)

For the first case, its range is the kernel of the nonzero continuous functional

 gamma -> integral_R exp(-lambda Phi(t)) gamma(t)/(d(t)H(t)) dt,
 Phi(t)=integral_0^t 1/d(s) ds.                             (4)

The same formula for the future-selected solution holds whenever that solution belongs to B_0:

 z(t)=-integral_t^infinity exp(-lambda[Phi(s)-Phi(t)])
                               gamma(s)/(d(s)H(s)) ds.     (5)

At lambda=0 the homogeneous z is constant and is excluded by z(+infinity)=0. At lambda>0 it grows at positive infinity. These are distinct reasons for injectivity at the endpoint and in the open positive half-line.

For the actual parameter sigma=1/4, the exceptional value is

 lambda_crit=D/4=1/k-1/4,
 k=1615536043799051/9007199254740992.

Its exact rational value and outward decimal enclosure are in evidence/check.json. No actual full-operator injectivity assertion follows from(3).

## 4. Proof of the index classification

The Hardy bounds of proof 38 imply that beta in B_0 is equivalent to z,z' in L2(omega_B). Conversely these two weighted conditions force both endpoint traces to vanish: z' is integrable because omega_B^(-1) is integrable, so both limits exist, and a nonzero endpoint limit would make the weighted z norm infinite. Thus B_0 is precisely this weighted H1 space, with equivalent norms.

Put u=omega_B^(1/2)z. The continuous piecewise exponential multiplier gives an isomorphism from B_0, in z coordinates, to H1(R). Write r(t)=-sigma for t<0 and r(t)=kappa for t>0. Multiplication of the output by omega_B^(1/2)/(dH) reduces A-lambda to

 Q_lambda u=u'-a_lambda(t)u,
 a_lambda(t)=r(t)+lambda/d(t),
 a_-=-sigma+lambda/D, a_+=kappa+lambda/ell.                (6)

The coefficient is bounded; its jump at0 causes no additional distribution because the multiplier omega_B^(1/2) is continuous. Let a_step equal a_- on the negative half-line and a_+ on the positive half-line. Exponential convergence of d makes a_lambda-a_step integrable and bounded. Consequently

 E(t)=exp(integral_0^t[a_lambda(s)-a_step(s)]ds)

and its reciprocal are bounded W1,infinity multipliers. The exact identity

 Q_lambda(Ev)=E[v'-a_step v]                               (7)

gives isomorphic domain and target realizations. It therefore suffices to analyze the step operator on H1(R)->L2(R).

When a_-<0<a_+, its unique square-integrable half-line solutions are

 v_-(t)=integral_-infinity^t exp(a_-(t-s))f(s)ds, t<0,
 v_+(t)=-integral_t^infinity exp(a_+(t-s))f(s)ds, t>0.

Their L2 bounds are 1/|a_-| and1/a_+ by the one-sided convolution inequality; the equation bounds their derivatives as well. They form an H1 function on the whole line exactly when their traces at0 agree. That equality is one nonzero bounded scalar compatibility condition. The kernel is zero, so the range is closed of codimension one. Conjugating the compatibility back through(6)-(7) gives exactly(4). Its boundedness can also be checked directly: at negative infinity the squared dual integrand decays like exp(2(sigma-lambda/D)t), and at positive infinity it decays like exp(-2(kappa+lambda/ell)t).

When a_->0, both step values are positive. The future formula

 v(t)=-integral_t^infinity exp(-integral_t^s a_step(q)dq) f(s)ds

has L2 norm at most 1/min(a_-,a_+) times ||f||_2. Its derivative is bounded by the equation, so it lies in H1 and solves the equation. The homogeneous solution grows at positive infinity and cannot lie in L2. This proves bijectivity with bounded inverse. Conjugating back proves(5) and the second case of(3).

At a_-=0, the step operator is the ordinary derivative on the negative half-line and d/dt-a_+ on the positive half-line. Choose a nonzero smooth chi supported in(-1,1), with ||chi||_2=1, and set

 v_n(t)=n^(-1/2)chi((t+n^2)/n).

For n>=2 the support is strictly negative. Its L2 norm is1, its derivative norm is ||chi'||_2/n, and its step-operator image is exactly v_n'. It converges weakly to0 in H1 while its H1 norm tends to1. The kernel is zero because a positive-half-line homogeneous solution in L2 must vanish there, hence everywhere by uniqueness. If the range were closed, this injective bounded operator on H1 would be bounded below, contradicting v_n. Thus its range is not closed. The formal adjoint has homogeneous solution exp(-integral_0^t a_step), which is constant on the negative half-line, hence not in L2 unless zero. The adjoint kernel is zero; the range is dense. The bounded conjugations preserve all these statements and prove the third case of(3).

## 5. Audit of the revised theory author statement

The revised remainder lemma and triangular corollary in the theory author snapshot are CONFIRMED under their displayed high-space hypotheses. The zero-jet index classification is also CONFIRMED, with the proof above supplying domain membership, the compatibility functional and a singular sequence at the exceptional parameter.

Two wording corrections are needed. First, beta=JH with constant nonzero J does not belong to B, because z(+infinity)=0 is imposed in B. The correct free-jet example is beta=H chi(t), with a smooth chi equal to1 at negative infinity and0 at positive infinity, or the physical cutoff cubic used in proof 104. It belongs to B and fails to belong to Gamma because of the negative-end weight. Second, a negative transport energy margin alone does not prove that the full transport realization is not semi-Fredholm. Such a statement needs its own spectrum or singular-sequence argument. The present scalar singular sequence proves precisely the critical statement in(3), not that different full-operator assertion.

The remainder resolvent, the high compact estimate, the high off-diagonal map and high compact jet map have not been proved for the actual variable-order realization. Membership of zeta in the verified base target is established separately; its inclusion in a newly chosen target must be checked through the actual embedding. The proposed spectral continuation is therefore a valid alternative conditional route, not a completed high inverse or nonlinear existence theorem.
