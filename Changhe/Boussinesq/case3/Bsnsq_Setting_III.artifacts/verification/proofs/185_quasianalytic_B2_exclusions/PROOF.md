# Quasianalytic exclusions for the beta-two B2 problem

Status: CONFIRMED from the explicit hypotheses, after an independent complete proof, exact controls and a written general-theorem review from actual Claude Opus5.5. The B2 applications were checked independently against the listed prior geometric proofs; further requested B2 model reviews returned no written audit. These are restricted regularity exclusions. The full smooth B2 problem remains OPEN.

## Statement, notation and dependencies

A positive sequence m=(m_k) has m_0=1 and satisfies

    m_k^2 <= m_{k-1}m_{k+1},
    D_m=sup_{k>=1}(m_{k+1}/m_k)^(1/k)<infinity,
    sum_{k>=1}m_{k-1}/m_k=infinity.                         (1)

For an open G in R^d, define C{m}(G) by f smooth and, for every compact K contained in G, constants A,B>0 with

    sup_K |partial^alpha f| <= A B^|alpha| m_|alpha|.       (2)

Vector membership means membership of each component. Constants may depend on K. We use the weight on actual derivatives; there is no additional factorial in (2).

The general assertions proved here are: C{m} is closed under linear combinations and partial derivatives; a function in C{m} flat at one point of a connected open set is identically zero there. Here flat includes the zeroth derivative. For m_k=k!, this is precisely the real analytic class.

Apply these assertions to beta=2, with smooth fields on the full physical plane satisfying

    W=2X+U-U(0), div U=0, Omega=-curl U,
    W.grad Theta=0, W.grad Omega+Omega=Theta_x,
    U=o(|X|), Theta(-x,y)=Theta(x,y), Theta(0,y)=0,
    Theta=a0 x^2+O(|X|^3), a0!=0,
    W_1 odd in x, W_2 even in x.                         (3)

These hypotheses include the canonical B2 velocity requirement when this is used to obtain the global fields. No extra harmonic velocity or fixed-center restriction is introduced here. The following are necessary:

(A) Theta does not belong to C{m}(R^2). This also holds under the weaker temperature-only assumptions of lead4.7(ii): smooth divergence-free U, U=o(r), DW(0)=diag(0,4), the temperature parity, axis condition, center jet and thermal equation. The vorticity equation is unnecessary for (A).

(B) Let gamma be the connected component of {W=0} through0. At each endpoint p of gamma, neither Omega nor U belongs to C{m} on any open neighborhood of p. Theta does not belong to C{m}(G) for any connected open G containing gamma.

(C) At an outgoing endpoint p, or at an incoming endpoint p when all zeros off gamma are isolated, let Cstar be p and the two complete orbits continuing its strong unstable curve. None of Theta, Omega, U belongs to C{m} on a neighborhood of any point of Cstar.

The geometric and transport inputs are the previously proved results08 (temperature flat point),45 (compact central arc and endpoint flatness),177 (incoming side with isolated off-arc zeros), and179 (strong-orbit flatness and absence of a full constant-temperature or irrotational neighborhood). Their exact used content is restated below. This packet does not remove their hypotheses, especially the incoming isolation premise. The weights (1) form a strict extension of analytic regularity, demonstrated below, but do not cover every smooth or every Gevrey function. None of (A)-(C) excludes the entire prompt class.

## A finite-interval uniqueness proof

Let f be smooth on a neighborhood of a compact real interval J, flat at q in J, and suppose |f^(j)|<=A B^j m_j throughout J. Divide by A and replace m_j by M_j=B^j m_j. The positive ratios mu_j=M_j/M_{j-1} are nondecreasing by logarithmic convexity; the sum of their reciprocals diverges. M_0=1. Translating q to0 and reflecting the variable if necessary, it suffices to prove f(t)=0 for an arbitrary fixed t>0 with [0,t] contained in J.

For n sufficiently large set

    S_n=sum_{j=1}^n 1/mu_j, a=t/S_n<1/4,
    t_k=a sum_{j=k}^n 1/mu_j (1<=k<=n), t_{n+1}=0,
    I_k=[t_{k+1},t_k], I_{n+1}={0}.

Write F_{s,k}=sup_{I_k}|f^(s)|. All F_{s,n+1} are zero, by flatness. For k descending from n to1 and s descending from k to0 we claim

    F_{s,k} <= (2a)^(k-s) M_s, 0<=s<=k.                (4)

The case s=k follows from the assumed derivative bound. For s<k, the fundamental theorem of calculus from t_{k+1}, and then the induction hypotheses, give

    F_{s,k} <= F_{s,k+1}+(a/mu_k)F_{s+1,k}
       <= (2a)^(k-s) M_s [2a+mu_{s+1}/(2mu_k)]
       <= (2a)^(k-s) M_s.

At k=n the first term is zero, which is even stronger than its displayed bound. The last inequality uses s+1<=k, the nondecreasing ratios, and a<1/4. Since t=t_1, (4) gives |f(t)|<=2a M_0=2t/S_n, which tends to0. This proves the claim on all of J, including the case q is an endpoint. This sufficiency argument requires neither a separate root-growth assumption on m nor m_1>=1. The B factor multiplies every ratio by B and preserves reciprocal-sum divergence.

For provenance, the interval subdivision argument agrees with Lemma3.2 and the sufficiency direction of Theorem3.6 in Rainer's survey cited below. It is included in full so no unmentioned normalization of the literature's weight sequence is needed.

## Several variables, derivative closure and analytic regularity

For a unit direction e, the line restriction g(t)=f(q+te) satisfies

    |g^(k)(t)| <= A [B sum_i |e_i|]^k m_k
               <= A (sqrt(d) B)^k m_k                 (5)

on each compact segment, by the multinomial formula and (2). If every ambient derivative of f vanishes at q, every derivative of g at0 vanishes. The interval result therefore gives f=0 on a sufficiently small open ball about q contained in G: apply it separately to the segment from q to each point in that ball. The set of flat points is relatively closed in G by continuity of each derivative and open by this ball argument. On connected G it is all of G if nonempty. This uses only compact subsets of G, not bounds on its whole closure.

Let D=max(1,D_m). For k>=1, m_{k+1}<=D^k m_k; for k=0 use m_1. Thus

    |partial^alpha partial_j f|
       <= A B max(1,m_1) (B D)^k m_k, k=|alpha|.        (6)

Linear combinations satisfy (2) after enlarging A,B, and constants satisfy it trivially. In particular subtracting the value at the flat point is permitted.

For m_k=k!, a real analytic function has the stated derivative bounds on compacts, by a finite cover of neighborhoods of convergent analytic power series (or their complex extensions and Cauchy bounds). Conversely the Taylor remainder on a line segment is bounded by A B^n n! |h|^n/n! in dimension1, and by A(B sum_i|h_i|)^n after the multinomial expansion in dimension d. It tends to zero for small h. The resulting power series converges absolutely there, so (2) is equivalent to local real analyticity.

## B2 consequences, with the exact geometric inputs

For (A), the temperature-only input from08 is a point p at which all derivatives of Theta of positive order vanish. Here is the relevant reasoning. The nonzero quadratic jet and DW(0)=diag(0,4) force a local zero arc: on the smooth graph W_2=0, Theta_x=2a0 x+O(x^2) is nonzero for small x!=0, so thermal transport gives W_1=0. Sublinearity makes Z={W=0} compact. Its accumulation set Z' is nonempty and compact. At each p in Z', DW(p) is singular with trace4, hence has eigenvalues0,4 and is diagonalizable. In fixed linear coordinates (s,z), the first nonconstant homogeneous temperature polynomial, if any, must solve4z partial_z P=0, so it is c s^m, c!=0. On the regular normal nullcline z=k(s)=O(s^2), its s derivative is nonzero for small s!=0. Thermal transport then forces the entire nullcline to be a zero arc. If there were such a nonflat temperature jet at every point of Z', then Z' would locally be a regular curve without boundary. A compact component would be a simple closed curve C. Since W=0 on C, the divergence theorem would give4 area(interior C)=0, impossible. Thus some p has all positive temperature derivatives zero. Apply the proved quasianalytic uniqueness to Theta-Theta(p) on R^2. A constant Theta contradicts its nonzero quadratic jet.

For (B),45 proves that the central zero component gamma is a compact embedded arc with paired endpoints and that Theta-L and Omega are flat at each endpoint p, with L=Theta(p), and DW(p)=4n tensor n. These statements use (3); they do not assume an arc is a graph over x. The flatness argument is also local: a first nonconstant temperature Taylor polynomial would extend the normal nullcline into a full zero arc beyond an endpoint, as in the preceding paragraph. The vorticity equation then gives Omega(p)=0, and any first nonzero vorticity Taylor polynomial Q would solve (4z partial_z+1)Q=0. Every monomial eigenvalue4j+1 is positive, so no such Q exists. Omega(p)=0 makes DW(p) symmetric and yields its normal projection form.

If Omega belongs to C{m} on a neighborhood of p, apply uniqueness on a connected disk to get Omega=0 there. Then U is both divergence free and curl free, so

    Delta U_1=partial_x div U-partial_y curl U=0,
    Delta U_2=partial_y div U+partial_x curl U=0.

Smooth harmonic functions are real analytic. Thus W is real analytic on that disk. The normal component W.n has nonzero normal derivative4 at p, so its zero set is a real analytic graph. The tangential component W.tau restricted to this graph is analytic and zero on the side occupied by gamma, hence zero on the other side too. The central zero component would extend beyond its endpoint, impossible. This argument works even when zeros outside gamma accumulate at p. If U belongs to C{m}, derivative closure makes Omega=-curl U belong too and gives the same contradiction. If Theta belongs to C{m} on a connected open G containing gamma, endpoint flatness gives Theta=L on G; because0 belongs to G, the center jet is contradicted.

For (C),179 gives the following exact inputs under its outgoing or conditional incoming hypotheses: at every X in Cstar, every ambient derivative of Theta-L and of Omega vanishes; nevertheless no neighborhood of X has Theta identically L, and no neighborhood has Omega identically zero. The flatness comes from a smooth open irrotational, constant-temperature side adjacent to the strong orbit, followed by smooth finite-time transport. The nonconstancy uses arc-side backward projection onto an entire terminal interval of gamma, rather than just convergence to the endpoint. An isothermal full neighborhood would force a terminal plateau on gamma and then a forbidden irrotational neighborhood of p. The vorticity assertion also uses the coupled system; it does not follow from flatness alone. These statements were proved in179 with the incoming basin condition established in177. Apply uniqueness on a disk to Theta-L or Omega and use these contradictions. For U use (6). This proves (C) without asserting additional regularity of an artificial simultaneous coordinate chart or analyticity of a strong curve.

## A strict extension of the analytic class

Let L(t)=log(t+e) and m_k=k! L(k)^k, with m_0=1. The function g(t)=t log L(t) on t>=0 satisfies

    g''(t)=[2L(t)-t/(t+e)(L(t)+1)]/[(t+e)L(t)^2]>0.     (7)

Indeed L>=1, t/(t+e)<1, and the numerator is strictly larger than L-1. The logarithm of k! is discretely convex, so (7) proves logarithmic convexity of m. For r_k=m_k/m_{k-1},

    r_k=k L(k) [L(k)/L(k-1)]^(k-1),
    k L(k)<=r_k<=e k L(k).                              (8)

The upper bound follows by integrating the decreasing positive derivative1/((t+e)L(t)) of log L: the logarithm of the bracket to power k-1 is at most (k-1)/((k-1+e)L(k-1))<=1. Consequently sum1/r_k diverges by comparison with sum1/(k log(k+e)), and r_{k+1}^{1/k} is bounded (and tends to1), so (1) holds. Also m_k>=k!, so every analytic function is in this class.

For x>1 and integer j>=1 we prove the exact bound asserted in the lead draft:

    x^j exp(-x/log x) <= 8^j j! [log(j+e)]^j=8^j m_j.  (9)

Put L=log(j+e). If log x<=8L, the exponential series gives x^j<= (8L)^j j! exp(x/(8L)); multiplying by exp(-x/log x) proves (9). If t=log x>8L, then t>2 and exp(t)/t^2 is increasing. Since L<=j+e,

    exp(t)/t^2 > (j+e)^8/(64L^2)
                    >=(j+e)^6/64 > j.

For the last inequality, j+e>3 and j+e>j, so (j+e)^5>3^5>64. Hence j t-exp(t)/t<0 and the left side of (9) is less than1, which is at most its right side. This proves (9) for all indices and all x>1 without a finite numerical scan.

Define

    f(x,y)=sum_{n=2}^infinity exp(-n/log n) cos(nx).       (10)

A bound on one summand alone does not justify summation. Apply (9) with index j+2, divide by n^2 and sum. Since sum_{n>=2}1/n^2<=1,

    sum_{n>=2} n^j exp(-n/log n) <= 8^(j+2)m_{j+2}.       (11)

For j>=1, derivative closure twice gives m_{j+2}<=D^(2j+1)m_j, D=max(1,D_m). At j=0 use m_2 separately. Thus the right side of (11) is bounded by A B^j m_j for

    A=64 max(D,m_2,1), B=8D^2.

Every derivative series converges uniformly by the summable n^-2 bound. Termwise differentiation is therefore valid at every order, giving a smooth function in C{m}(R^2), independent of y.

With fhat(n)=(2pi)^(-1) integral_0^(2pi) f(x,0) exp(-inx) dx, its positive-frequency Fourier coefficient is exp(-n/log n)/2. If this periodic function were real analytic everywhere on R, compact analytic bounds on one period would give sup|f^(j)|<=A B^j j!. Integrating by parts j times gives |fhat(n)|<=A B^j j!/n^j<=A(Bj/n)^j. Choosing j=floor(n/(2B)) for sufficiently large n bounds this by A exp(-c n) with c>0. This contradicts the displayed coefficients, since1/log n tends to0. Hence (10) is not real analytic everywhere, and the class inclusion is strict.

## Why general smooth and higher Gevrey profiles remain open

For s>1 put a=1/(s-1), h(t)=exp(-t^-a) for t>0 and0 for t<=0. All derivatives tend to0 as t decreases to0, by their finite combinations of powers times this exponential, so h is smooth and flat but nonzero on every right neighborhood. It belongs to Gevrey order s. To see the quantitative bound, choose a constant delta>0 small enough that in |z-x|<=delta x, x>0, one has Re(z^-a)>=c x^-a with c>0, using a holomorphic branch near the positive axis. Cauchy's estimate gives

    |h^(j)(x)| <= j! (delta x)^(-j) exp(-c x^-a).

Maximizing x^-j exp(-c x^-a) gives c^(-j/a)(j/(ae))^(j/a). The elementary factorial bound j!>=(j/e)^j therefore yields |h^(j)|<=C^j(j!)^(1+1/a)=C^j(j!)^s. The zeroth bound is1. On the negative side every derivative is zero. No class satisfying (1) can contain h on a neighborhood of0, by uniqueness. This example illustrates the logical gap between quasianalytic regularity and unrestricted smoothness; it is not a B2 solution.

Likewise any nonzero smooth correction which is flat at an endpoint, such as the flat holomorphic correction from exp(-z^-1/2) in168 and its stated smooth extensions, cannot lie in C{m} on a full neighborhood of that endpoint. Analyticity on the open punctured side is compatible with this failure. The nonprofile constructions168/161 do not become solutions of both B2 equations by this observation.

## Verification scope and source

The proof above precedes computation. Controls check algebra and deliberate invalid extrapolations; they are not a finite proof of a statement for every k. No formal source or theorem-prover build is claimed.

Primary reference: Armin Rainer, *Ultradifferentiable extension theorems: a survey*, arXiv:2107.01061v2, 30 December2021; sections2.1 and2.5, Example2.8 (Gevrey weights and flat functions), Lemma3.2 and Theorem3.6. Downloaded2026-10-21 from https://mat.univie.ac.at/~armin/publ/survey-UET.pdf to verification/literature/Rainer_2107.01061v2.pdf. Rainer's capital M is our derivative weight m; his auxiliary lower-case sequence is divided by k!. Local source hashes are recorded separately. All B2 statements additionally depend on the explicitly named lane proofs and the hypotheses restated here.

## Audit evidence

Published UTC 2026-10-21T16:57:03.223205+00:00. The standalone argument was written16:46:17 before the controls. Independent exact controls1284 and seven negative controls passed in1.470903042s, from2026-10-21T16:50:29.409128+00:00 to2026-10-21T16:50:30.880008+00:00. The tests check the log-weight second derivative, finite rational instances of the double induction with three ratio families and three subdivision factors, multinomial restrictions, endpoint jet eigenvalues, the two derivative-closure factors, a telescoping summable majorant, and a coupled polynomial control. These are algebra checks; none is a finite proof of the universal inequalities in the preceding argument.

The polynomial control Theta=x^2,Omega=2x,Psi=2xy-x^3/3,U=(-2x,2y-x^2),W=(0,4y-x^2) satisfies both beta-two transport equations and Omega=-DeltaPsi. It violates U=o(r), so is not an admissible profile. Negative controls record that dropping sublinearity, connectedness, the zeroth derivative in flatness, the reciprocal-sum premise, or the summable-majorant step would invalidate the respective inference. They also detect the reversed streamfunction convention and an induction subdivision factor outside the sufficient bound. The flat-function derivative samples check an explicit counterexample already justified for all orders in the written proof.

The actual requested model was us.anthropic.claude-opus-5-5 and every API return was claude-opus-5-5. Review334 supplied a full written confirmation of the interval theorem, several-variable step, derivative closure, weight example, universal constant8, infinite series bound, nonanalyticity and Gevrey example in63.430220704s. Its advice was independently checked; the Fourier normalization was made explicit. The source citation was checked against the locally downloaded primary PDF: section2.1 uses the weight on actual derivatives, section2.5 gives the derivative-closure condition, Example2.8 is the Gevrey example, Lemma3.2 gives the interval subdivision, and Theorem3.6 the divergent reciprocal-ratio criterion. Our proof avoids depending on additional normalizations in the survey's definition of a weight sequence. The log-factorial example and its Fourier estimate are proved here; they are not attributed to Example2.8.

The other calls do not count as mathematical evidence. Review333 exhausted16000 tokens with no written answer (145.975829321s). Reviews335,336 and337 returned no written audit, with API stop_reason refusal, in8.823301710,10.653964301 and6.267361044s. No reason is inferred from private response content. The independently proved B2 applications above retain the exact hypotheses of08,45,177 and179; the confirmed prior packets remain their dependencies. Review334 explicitly did not inspect those applications or the primary PDF. Full API provenance, frozen prompts, written answers and the limitations are retained in the review adjudication. No model was silently substituted. Every request explicitly preserved the standing machine and lane restrictions. No theorem-prover formalization or build is claimed.
