# Complete transport, maximal graph domains, and compact-error estimates

Status: independently proved. Date: 2026-10-20. This is an abstract domain lemma; application of its bounded-conjugation and compact-error hypotheses to the full IPM operator is a separate step.

## Exact statement

Let M be a smooth manifold without boundary with a smooth positive density dm. Let V be a real smooth complete vector field, with smooth flow Phi_t defined for all real t. On H=L2(M,dm), define the distributional transport operator

    T=V.grad+(div_m V)/2,
    D(T)={v in H: Tv in H distributionally}.

Then T is skew-adjoint, and C_c^infinity(M) is a core for T. These assertions also hold on a closed symmetry sector invariant under the flow and admitting dense smooth compactly supported tests, with projections commuting with T.

Let C be any bounded operator H->H, possibly nonlocal, and put B=T+C on D(T). Then B is closed and

    B*=-T+C*, D(B*)=D(B)=D(T).                 (1)

In particular these are the maximal distributional graph domains whenever C is also specified as that bounded operator on distributions in H.

Suppose a compact operator K:H->H0 into a Hilbert space H0 and constants epsilon>0, C0>=0 satisfy

    Re <Bv,v> >= epsilon ||v||^2-C0||Kv||^2     (2)

for all smooth compactly supported tests in the chosen sector. Then (2) extends to D(T), holds with B* as well, and

    ||v||^2 <= epsilon^(-2)||Bv||^2
                   +2C0/epsilon ||Kv||^2,     (3)

with the same assertion for B*. Consequently B, from its graph space to H, is Fredholm. For any norm-continuous bounded family C_tau with (2) at each parameter, the graph domain remains fixed and the index is locally constant. Uniform constants are not needed for local constancy, though uniform estimates can give quantitative bounds.

This lemma supplies a precise replacement for saying that strict symbol margins absorb unspecified graph-regularization errors. It does not establish inequality (2) from a pointwise principal symbol.

## Unitary flow and the maximal domain

Let J_t be the positive density Jacobian, characterized by Phi_t^*dm=J_t dm, and define

    Q_t f(X)=J_t(X)^(1/2) f(Phi_t X).

The change of variables Y=Phi_t X proves ||Q_t f||=||f||. The chain rule for Jacobians gives the group law. On a smooth compactly supported function Q_t f depends continuously on t in H; its support for t in a compact interval stays in a compact set, and differentiation gives

    d/dt Q_t f = Q_t Tf = T Q_t f.

Density and unitarity imply strong continuity of Q_t on all H.

Let G be its strong generator. Testing the derivative at t=0 against smooth compactly supported functions gives Gv=Tv distributionally for every v in D(G). Conversely, let v,Tv both be in H. Differentiation against compactly supported tests and integration in t yield the weak identity

    Q_t v-v=integral_0^t Q_s Tv ds.             (4)

All pairings are legitimate because a fixed finite segment of a test's flow stays compact and smooth. The right side is a strong H integral by strong continuity. Dividing (4) by t and taking t to zero proves v in D(G) and Gv=Tv. Thus D(G)=D(T), and the maximal domain has been identified without an unproved spatial mollifier commutator.

The generator is closed: if v_n->v and Tv_n->w in H, pass to the limit in (4), then differentiate at zero to obtain v in D(T), Tv=w. Integration by parts first on tests, and then (4) or the unitary group on D(T), gives skew symmetry.

For completeness, maximal skew-adjointness can be seen from the resolvents. For lambda>0, the norm-convergent integrals

    R_+ f=integral_0^infinity exp(-lambda t) Q_t f dt,
    R_- f=integral_0^infinity exp(-lambda t) Q_(-t) f dt

have norm at most ||f||/lambda. Difference quotients, followed by one integration by parts in t, show

    (lambda-T)R_+f=f, (lambda+T)R_-f=f.

A densely defined closed skew-symmetric operator for which both lambda-T and lambda+T are onto is skew-adjoint. One direct proof is to take z in D(T*), solve (lambda+T)u=(lambda-T*)z, and use the adjoint relation to see z-u is orthogonal to ran(lambda-T), hence zero. This gives T*z=-Tz. The reverse inclusion is skew symmetry.

## Smooth compact core

Choose a real compactly supported smooth approximate identity phi_epsilon on the time line. For v in D(T), set v_epsilon=integral phi_epsilon(t)Q_t v dt. Strong continuity applied to both v and Tv gives convergence in the graph norm as epsilon tends to zero. For fixed epsilon, approximate v in H by f_n in C_c^infinity(M). Define

    f_(epsilon,n)=integral phi_epsilon(t)Q_t f_n dt.

Each such function is smooth and compactly supported: the union of its supports is the image of one compact set under a compact interval of the smooth flow. Moreover

    T f_(epsilon,n)=-integral phi_epsilon'(t)Q_t f_n dt.

Thus f_(epsilon,n)->v_epsilon and T f_(epsilon,n)->T v_epsilon in H as n tends to infinity, using only L2 convergence of f_n. A diagonal sequence proves the core assertion. If a finite symmetry projection commutes with Q_t, project the approximants; this gives the same result in the parity sector. No spatial derivative bound on the approximating f_n is needed.

## Bounded perturbations, adjoints, and the estimate

Boundedness of C proves that B has domain D(T), is closed, and has graph norm equivalent to that of T. The bounded perturbation adjoint identity gives (1). It can be verified directly from the definition of an adjoint: bounded C contributes no domain restriction, leaving the skew-adjoint domain of T.

For v in D(T), Re<Tv,v>=0. Hence the real quadratic forms of B and B* both equal Re<Cv,v>. Approximate by the established smooth compact core. The graph convergence and boundedness of K pass (2) to D(T), with the same K for B and B*. Apply Cauchy-Schwarz and

    ||Bv||||v|| <= (epsilon/2)||v||^2
                         +(1/(2epsilon))||Bv||^2

to get (3).

Estimate (3) and compactness imply finite-dimensional kernel: any orthonormal sequence in the kernel would have a subsequence whose K images converge, and applying (3) to differences would force convergence in H. The same argument applies to B*.

For closed range, if no bound ||v||<=C||Bv|| held on D(B) intersect ker(B)^perp, there would be v_n in that space with ||v_n||=1 and Bv_n->0. Pass to a subsequence for which Kv_n converges and use (3) on differences to obtain a strong H limit v. Closedness gives Bv=0; orthogonality gives v=0, contradicting norm one. The resulting estimate and closedness prove the range is closed. Its orthogonal complement is ker B*, already finite-dimensional. Thus B is Fredholm.

For the family assertion, take X=D(T) with its graph norm. C_tau varies continuously as a bounded X->H operator. Fredholm maps remain Fredholm under sufficiently small norm perturbations and keep their index: split source and target into kernel, range and finite-dimensional complements at a fixed parameter, invert the infinite-dimensional diagonal block by a Neumann series, and use the remaining finite-dimensional Schur complement. Its index is the fixed difference of the finite source and target dimensions. This proves local constancy.

## What remains to apply this to IPM

For the lead's extra global-source and full derivative-decay hypotheses, a useful realization uses a smooth complete metric that is Euclidean near zero and cylindrical in t=log r at infinity. Its volume density is dX inside and dr/r dtheta outside. The vector W is complete; its skew transport is exactly T=W.grad+(div_m W)/2. Choose a Sobolev isomorphism A_s and a radial growth weight, and conjugate the full linearization to H. The required checks are:

1. The conjugated operator is T+C with C bounded on H, including the canonical inverse and its nonlocal tails.
2. The real quadratic form satisfies (2), with an actual compact remainder. Interior order-minus-one remainders are compact after cutoff; exterior remainders must have small operator norm in both relevant directions, not merely small pointwise coefficients.
3. The chosen Sobolev and growth conjugation identifies the proposed maximal graph norm with the domain of T+C.

The dyadic bounds and local symbols have been independently checked elsewhere. The abstract domain/adjoint step above is now proved. Establishing all pseudodifferential conjugation and compactness assertions in these exact hybrid spaces remains a separate audit. In particular, neither the prompt's basic growth assumption nor a pointwise local indicial calculation implies those assertions. The original class also does not imply the lead's extra full derivative asymptotics or global-source-basin hypothesis.

The elementary density factors give a useful sign check: for W=(Ax,y), dm=dX, Q_t f=exp((A+1)t/2)f(exp(At)x,exp(t)y). For W=ell r partial_r and dm=dr/r dtheta, Q_t f=f(exp(ell t)r,theta), with no volume factor. These are precisely the interior/end density distinctions in the frozen Sobolev calculation.
