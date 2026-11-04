# Independent audit of distributional critical inverse-radius continuation

This is the audit of LIT350, submitted source SHA256 cc8b5e090eee9062bcd1a6f9ac1bffea0df6f7ab7155ab6fa10773b103c542ee. All seven source sections and49 manual checks were read. The independent argument below keeps the distributional premise, the order of the regularity steps and the closed spectral constant explicit. Existing configured model comparison is pending at initial writing.

## 1. Exact theorem

Let O be an open connected planar domain containing0, and let u,g belong to L1_loc(O;C^N), with N a finite positive integer. Use the Euclidean vector norm and dbar=(partial_x+i partial_y)/2 componentwise. Suppose

    dbar u=g in distributions on O,
    |g(z)|<=C |u(z)|/|z| almost everywhere,
    integral_(|z|<r)|u(z)|=o(r^m) for every real m>0.

Here C is a fixed finite nonnegative constant. Then u belongs locally to W1,q for every finite q>=1 and has infinite L2 integral order at0. If C<=1/4, then u=0 almost everywhere on O. If a continuous representative is chosen, it is identically zero.

There is also a punctured version: retain u in L1_loc(O) and integral flatness, but initially assume g in L1_loc(O\{0}) and the distributional equation only there. The same coefficient bound implies g in L1_loc(O) and removal of the distributional singularity, so the same conclusions follow. A pointwise derivative formula for an arbitrary rough function is not the distributional premise.

## 2. The Cauchy potential and its weak endpoint bound

Let E(z)=1/(pi z), so dbar E=delta0 in distributions, as follows by integration by parts outside a circle and passage to its boundary limit. For a compactly supported vector h in L1(C), set H=||h||1 and Th=E*h. Local integrability and almost-everywhere absolute convergence follow from Tonelli: the integral of |z-w|^(-1) over a bounded z set is uniformly bounded for w in the fixed compact support. Fubini then proves dbar Th=h in distributions.

For H>0 and t>0 split E into the regions |z|<R and |z|>=R, where R=2H/(pi t). The near kernel has L1 norm2R. The far kernel has L-infinity norm1/(pi R). Therefore the far convolution has norm at most t/2 everywhere, and Markov's inequality on the near convolution gives

    area{|Th|>t}<=4RH/t=8H^2/(pi t^2).

If H=0 the conclusion is immediate. Consequently

    K2(Th):=sup_(t>0)t sqrt(area{|Th|>t})<=sqrt(8/pi)||h||1.

This is a vector estimate obtained from absolute values; its constant is independent of N.

## 3. Initial integrability without assuming Sobolev regularity

Choose a smooth compactly supported chi in O equal to1 near a given relatively compact disc. Extend v=chi u by0 to C. The product rule for distributions gives

    dbar v=h=chi g+(dbar chi)u,

with compactly supported L1 right side. The difference v-Th is an entire distribution killed by dbar. The distributional Weyl lemma makes it an entire holomorphic function. Outside a disc containing the support of v and h, v=0 and Th=O(1/|z|), by direct kernel estimation. Thus the holomorphic function tends to0 at infinity. Liouville's theorem makes it zero. We obtain v=Th almost everywhere, hence local weak-L2 membership of u.

On a finite-area set, split layer cake at t=1. For1<=p<2 the high part is at most p K2(u)^2 integral_1^infinity t^(p-3)dt<infinity, while the low part is finite by the area bound. In particular u is locally L^(3/2). No classical derivative of u has been assumed to reach this step.

## 4. Flatness, weighted interpolation and bootstrap

For M,m>0 and epsilon>0, flatness supplies r0 such that integral_(B_s)|u|<=epsilon s^(m+M) for0<s<r0. For0<r<r0, summing the annuli r2^(-j-1)<|z|<=r2^(-j) gives

    integral_(B_r)|u(z)| |z|^(-M)
       <=epsilon 2^M r^m sum_(j>=0)2^(-jm)
       =epsilon 2^M r^m/(1-2^(-m)).

Thus u/|z|^M is integrable and L1 flat for every fixed M. For p>q>1 let epsilon=(p-q)/(p-1). Then0<epsilon<1 and q=epsilon+p(1-epsilon). Holder's inequality on a sufficiently small disc yields

    integral (|u|/|z|)^q
       <=(integral |u|/|z|^(q/epsilon))^epsilon
          (integral |u|^p)^(1-epsilon).

If u is Lp the right side is finite, and g is Lq. The local elliptic implication used here is: a distribution f with dbar f in Lq_loc,1<q<infinity, belongs to W1,q_loc. To justify it, cut off the right side near the compact set of interest and apply T. Its dbar derivative is the cutoff right side, its partial derivative is the Beurling singular integral, and the latter is bounded on Lq by the Calderon-Zygmund theorem. Its function value is locally Lq by convolution with the locally L1 kernel and its compact support. The remainder is holomorphic by Weyl. This proves the local statement for finite vectors; no bound for its constant is used below.

Starting with p=3/2, choose q=4/3. Then epsilon=1/3 and the weighted L1 exponent is4. We obtain W1,4/3 and, by planar Sobolev embedding, L4 locally near0. With p=4,q=3 the same epsilon is1/3 and the weighted exponent is9. We obtain W1,3 and a bounded Holder representative. Every finite Lp exponent is now available on smaller discs; the same interpolation proves W1,q for each finite q>1, and W1,1 follows on compact sets.

Away from0 the coefficient is bounded. Starting with L^(3/2), the equation gives W1,3/2, then L6, W1,3 and boundedness; repeating gives all finite q there as well. All embeddings and cutoffs are local on nested relatively compact discs. Finally, a local bound |u|<=M0 implies integral_(B_r)|u|^2<=M0 integral_(B_r)|u|. This proves infinite L2 integral order. It also gives integrability of |u|^2 times every inverse power, using the weighted L1 result. These conclusions require only finite C, not C<=1/4.

## 5. The full angular equation

Fix B(0,R) compactly contained in O, T=-log R, and set r=exp(-t). Write

    U(t,theta)=u(r exp(i theta)),
    H=L2(S1;C^N), D=-i partial_theta,
    G(t,theta)=-2r exp(-i theta)g(r exp(i theta)).

The domain of the self-adjoint D is periodic H1. Its spectrum comprises every integer k, with all N components included. The polar identity

    dbar=exp(i theta)(-partial_t+i partial_theta)/(2r)

gives U_t+D U=G. On compact t intervals, the established H1 regularity gives U in H1_t(H) and L2_t(domain(D)). Thus U has a common locally absolutely continuous H-valued representative. For almost every t,

    ||G(t)||H<=2C||U(t)||H<=||U(t)||H/2

when C<=1/4. For each lambda>0, weighted L2 integrability gives

    integral_T^infinity exp(2lambda t)||U(t)||H^2 dt
       =integral_(|z|<R)|z|^(-2lambda-2)|u(z)|^2 dA<infinity.

The outer annulus causes no difficulty. This estimate does not claim pointwise decay on every circle.

## 6. Signed energy at the closed threshold

For any integer m>=0 put lambda=m+1/2 and S=sign(D-lambda). This is a bounded self-adjoint involution, positive on k>=m+1 and negative on k<=m. Let W=exp(lambda t)U and Q=<SW,W>H. The form Q is real and locally absolutely continuous. At almost every t,

    Q'=-2<|D-lambda|W,W>H+2 Re<SW,exp(lambda t)G>H
       <=-||W||H^2+2||W||H exp(lambda t)||G||H<=0.

The first inequality uses |k-lambda|>=1/2 for all integers k. Its quadratic form is absolutely convergent because W lies in domain(D) at the times in question, with sum |k-lambda||W_k|^2 finite by Cauchy-Schwarz. Only the bounded S form is differentiated. No derivative of the unbounded D energy is taken.

For each fixed lambda, W belongs to L2 in t, so there is a sequence t_j->infinity with ||W(t_j)||H->0. The locally continuous representative can be used at these points. Therefore Q(t_j)->0. Nonincrease gives Q(t)>=0 for every t>T. Cancel the positive exponential factor to obtain

    ||P_(k<=m)U(t)||H^2<=||P_(k>=m+1)U(t)||H^2.

Now fix t and let m increase through all nonnegative integers. Square summability of the complete angular expansion makes the left side approach ||U(t)||H^2 and the right side approach0. Thus U(t)=0, proving local vanishing of u. Equality C=1/4 is allowed: no strict absorption was used. The two limits are distinct, a time sequence at each fixed spectral split followed by the spectral split tending to infinity.

## 7. Propagation on O

Let Z be the set of points with an almost-everywhere zero neighborhood. It is open and nonempty. If x is in its relative closure and x!=0, choose B(x,2d) compactly contained in O avoiding0. The coefficient there is bounded by K. Choose0<rho<d sufficiently small that K rho<=1/4, and then choose a in Z with |a-x|<rho/2. The disc B(a,rho) remains in B(x,2d). On it,

    |g|<=K|u|<=|u|/(4|z-a|).

The equation is distributional on this entire disc, and u has infinite integral order at a because a has a zero neighborhood. Sections2-6, translated to a, give vanishing on B(a,rho). This contains a neighborhood of x. The case K=0 permits any sufficiently small rho, and0 was already in Z. Hence Z is relatively closed. Connectedness implies Z=O. No flatness at a previously unknown boundary point was assumed.

## 8. Removing a punctured distributional singularity

In the punctured version, Section4's dyadic proof is available before any use of the equation. With M=1 it yields u/|z| in L1 near0 and hence g in L1 there. Choose a smooth cutoff eta_epsilon, zero for |z|<=epsilon and one for |z|>=2epsilon, with |dbar eta_epsilon|<=A/epsilon. Test the punctured equation against eta_epsilon phi, where phi is smooth with compact support in O. The error term is bounded by

    A epsilon^(-1)||phi||infinity integral_(|z|<2epsilon)|u|=o(1),

using flatness, for example exponent2. Dominated convergence handles the two remaining integrals because u,g are now L1 locally. The full distributional equation follows. Thus no distribution supported at0 survives. Sections2-7 then apply without alteration.

## 9. Dependencies and scope

The source's complete seven-section argument and49 manual checks have been read and are retained in `verification`. The only qualitative classical analytic inputs are distributional Weyl, Liouville, Beurling Lq boundedness for1<q<infinity, and planar Sobolev/Morrey embeddings at the specified exponents. Their constants do not enter the spectral threshold1/4. The dyadic and interpolation strategy is already present in the inspected Pan-Zhang sequel; its printed vector theorem has strict C<1/4 and initially assumes W1,1. The present proof does not attribute the initial L1 or closed-endpoint strengthening to that source. No novelty claim is made.

The inverse-radius premise is still essential. This is not a theorem for arbitrary weak-L2 coefficients, and it does not provide a reduced Euler coefficient bound or a rough real-carrier trace theorem. It provides no Euler counterexample. Existing configured model comparison is requested through files, with actual provider execution independently unattested. No mathematical computation, formalization or new model client was used.

## 10. Existing model comparison and diagnostic scope

The entire existing Theory Agent C note dated2026-11-04T04:46:17Z was read. Items5-11 agree with the Cauchy distribution estimate, compact distributional inversion, weighted interpolation, two bootstrap stages, all-mode signed energy, propagation and singular-point extension. Integer exponents in the source definition of infinite order and every positive real exponent in this theorem are equivalent: for any real exponent choose a larger integer, and use0<r<1. The qualitative elliptic dependencies remain explicit and do not enter the critical numerical constant.

The entire13-condition script and log were read, not rerun. Their counts are3EXACT,5SYM,2EX,1QUAD,2SAMPLE, with nonzero exit on a failed predicate. The unit-disc Cauchy transform has value conjugate(z) inside and1/z outside; for0<s<1 its superlevel set is s<|z|<1/s, giving squared weak norm pi. That exact formula checks the independent illustrative norm calculation. The three-point quadrature is evidence only. The sampled flat-function check takes a maximum at200 radii rather than the supremum over all radii, so it is not a proof of the dyadic hypothesis; Section4 above supplies the dyadic proof. The polynomial -1+4C has its exact zero at1/4 and positive slope, which proves its sign for every larger C independently of the script's one positive sample.

LIT350 includes the positive result A2930: its punctured H1 and L2-flat hypotheses imply local L1 flatness by Cauchy-Schwarz, and the punctured distributional equation has the derivative as g. The extension argument above then applies. It does not subsume the separate variable-width counterexample. Existing configured model collaboration is through files; actual provider execution is independently unattested. No new mathematical computation or model client was used.


## 11. Confirmed-source status revision

The exact current source has SHA256 73cc6bc1ee1b5af13e81895446e5fe15f793dc9be9ba9ec43231ac13e8302ea2. The full difference from the retained submission has been read: one opening status line changes, and one final comparison section is added. The opening and added final section accurately cite A2939-A2940 for the regularity and continuation steps. They keep the qualitative analytic inputs, distributional premise, puncture removal and A2941 limits. The source agent does not claim to have read the shared diagnostic. No displayed equation, mathematical hypothesis or proof argument changes. The old pending sentences belong to the dated original submission and are superseded by the new status section. The capture and complete difference are retained in verification.
