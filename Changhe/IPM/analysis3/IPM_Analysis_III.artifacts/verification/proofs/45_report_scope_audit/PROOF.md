# Scope audit of the theory report and two explicit counterexamples

## Object, method and scope

The audited object is the exact snapshot in evidence/report_snapshot.md, version labelled 2026-10-28T03:26Z. Its SHA-256 is in evidence/check.json. This audit compares the report with the standalone proofs supporting its numbered verdicts. Statements requiring the unresolved edge estimates, a global margin or a nonlinear inverse remain conditional. This result is not an existence or nonexistence theorem for an IPM profile.

Most of the report preserves the distinction between conditional theorems, observations and open steps. The following corrections are necessary for its precise mathematical claims.

## 1. Uniqueness of the certified source is local

Sections1.3 and6.3 call the source unique without restricting the assertion to the displayed interval. V017 proves existence and uniqueness in

 I=(4841405518533377,4841405518533711)/2^49.

Its proof encloses V1 at the two endpoints and proves partial_x V1>10 throughout I. It does not enclose V1 on the complement of I, count all equilibria, or prove the proposed global phase portrait. Hence uniqueness on I is CONFIRMED and uniqueness on the whole positive axis is OPEN. The report should say 'a source, unique in the certified interval'. Its reflected source is of course also present by parity; this observation is separate from positive-axis uniqueness.

## 2. The strain cancellation is only the linear contribution

Section4.2 currently says

 (U[h]+(c[h]/3)X).grad(x^2y)=0 exactly.

This identity is false for the full velocity. The correct exact algebraic identity is

 [c[h](-x,y)+(c[h]/3)(x,y)].grad(x^2y)=0.                 (1)

The velocity remainder survives. A concrete local counterexample is any smooth compact density h=x^2y chi(r), with radial chi equal1 near0. Its canonical stream is smooth near0 and solves -Delta psi=2xy there. The parity of psi is odd in both x and y. Its degree-four Taylor polynomial therefore has the form

 psi4=-(x^3y+xy^3)/6+H(x^3y-xy^3),                     (2)

for some real H: the first term is a particular solution and the second is the general parity-compatible harmonic polynomial of that degree. The degree-two term is c[h]xy. The velocity of this quadratic term cancels in (1). Applying (-partial_y,partial_x) to (2), then pairing with grad(x^2y), gives the degree-five polynomial

 x^2y[(-1/6+H)x^2+(5/6+5H)y^2].                       (3)

Its two coefficients cannot both vanish: the first requires H=1/6 and the second H=-1/6. Higher stream terms have degree at least6 and cannot cancel (3). This is a compact, parity-compatible density for which the displayed full-velocity identity fails. The surviving term has order r^5. The leading cancellation used in the linearized theory remains valid.

The symbolic code verifies -Delta psi4=2xy, formula(3), and inconsistency of the two coefficient equations. No numerical observation is used to infer the counterexample.

## 3. Numerical constants in Theorem O must retain their parameters

Section2.1(a) starts with arbitrary5/2<a<9/2,0<=b<3/2,a+b>4 but later gives the two local-strain constants

 0.069735617396310252 and0.045183183318774124

without repeating that they are for a=7/2,b=6/5. They are not uniform on the stated parameter range. In V022 the exact jet coefficient is

 C_v(sigma)=1/[8 sqrt(sigma(sigma+1)(sigma+2))], sigma=a+b-4.

For a=17/4,b=0, sigma=1/4 and C_v=0.14907119849998597976..., more than twice the first displayed value.

This is an actual sharp obstruction for the jet term, not merely a larger sufficient constant. Put

 v(s)=(1-exp(2s))exp(2sigma s) for s<0, and v(s)=0 for s>=0,
 beta(t)=integral_-infinity^t v(s)ds,
 h=x^2y beta(log r), J=0.

Then v belongs to G=L2(exp(-2sigma s)ds), h belongs to the domain of Theorem O, and its local strain is

 c_<[h]=(1/8)integral_-infinity^0(1-exp(2s))v(s)ds.

Equality holds in the weighted Cauchy-Schwarz inequality. The ratio |c_<[h]|/||v||_G is exactly C_v. Thus the parameter-free reading of the report's smaller constant is REFUTED. The report should append 'at a=7/2,b=6/5' to that inequality, or display the parameter-dependent formulas. The two fixed-parameter constants in the report are individually valid upward bounds at those parameters.

## 4. Nonlinear obstruction: preserve the input and solution hypotheses

Section3.4 and the last row of the exponent table use phrases such as 'every space controlling the local C^alpha norms' and 'any C^alpha-type norm'. V030 proves the following precise statement instead. On a fixed compact set K, assume a solution norm X controls

 ||g||_(C^alpha(K))+||U[g]||_(C^alpha(K))+|c[g]|.

There are specified smooth compact input sequences h_n, with zero strain and cubic coordinate, whose C^alpha norms are bounded, and every solution of Lg=N(h_n) has X norm tending to infinity. The second sequence is bounded in the stated C^alpha graph norm as well. A failure of a map bounded on X-balls follows if that input sequence is also bounded in X. A stronger norm can make those same inputs unbounded; V030 explicitly allows that possibility. Thus the universal wording should be replaced by the stated low norms and hypothesis(H) of V030. The solution lower bounds and the particular Holder/graph-norm counterexamples are CONFIRMED.

This restriction matters because the report itself proposes a stronger quasilinear norm. The obstruction does not refute that proposal merely because the stronger norm controls C^alpha.

## 5. Transport-uniformity statement retains domain and margin hypotheses

Section5.4's formula for p_i is correct under V040's explicit assumptions: each psi_i belongs to the common adjoint domain; the weighted derivative r grad psi_i is square integrable; the perturbed operator has the same compact error K and an appropriate positive margin m_W. To get a quantitative inverse one additionally needs

 delta+epsilon+(sum_i p_i^2)^(1/2)<m_W

and Fredholm index0. The phrase 'one set of psi_i serves the whole correction ball' should carry these conditions. The displayed plain-L2 adjoint formula does not automatically apply to the jet-plus-remainder realization, which has extra jet rows. The report later notes those rows; the immediate uniformity claim should retain that restriction too.

## 6. Conormal derivatives and classical normalization

Section3.4 says only conormal derivatives are needed across the axes. Tangency of W to the axes explains the algebraic rewriting

 W.grad h=(W1/x)(x partial_x h)+(W2/y)(y partial_y h),

when the quotients are controlled. It does not, by itself, prove a product estimate in the proposed global high space, a Lipschitz bound for W, or continuity of h/(x^2y). Those high-space estimates remain OPEN and should be described as a proposed route.

Likewise J is a continuous coordinate on Z, not automatically the classical Taylor coefficient of every measurable remainder. A nonlinear application to the prompt must verify a continuous factor at0 in its high space. If it solves with a free cubic coordinate, it must either impose J=0 or explicitly recover the required normalization by a proved rescaling after showing1+J>0 and the classical leading expansion. None of these observations changes the verified conditional linear theorem.

## 7. Current-status and accepted upgrades

The archived report says S0 'is assembled'. At the audit time its numerical run log still ends with 'assembly:1569 cells over2 workers'; there is no completed matrix certificate. The safe status is 'assembly in progress' unless a newer completion record is available. This is a status correction, not a mathematical refutation.

The revised Theorem C' has since been CONFIRMED conditionally as V047, including the core, homotopy and bounded strain. It can be upgraded from DERIVED to CONDITIONAL THEOREM with the explicit hypotheses retained. V044 should be added when discussing why Lfix and its local normalization term cannot separately take values in the strong target. V043 certifies the two S0 scalar tail strains and their shifted-log denominator, but no matrix singular value. V045 proves the separated outside-to-inside part of the edge estimate only for a fixed bounded output strip.

The following checked quantitative claims in the snapshot agree with the existing certificates: k and the exact modal normalization; the raw-X3 defect; the displayed source interval and coefficient box at its local scope; the frozen source inverse500/1687; the positive tail denominator for the specified unshifted nonnegative-log cutoff; C_cap and C_c0 at their stated parameter pairs; K_A<0.032162163072022018; and the local-strip C_a=1759/6 at a=7/2. The global margin, finite singular values, complete edge estimates, quantitative inverse and nonlinear existence remain unverified in this snapshot.

## Dependencies and verdict

Dependencies: V002,V005,V011,V016,V017,V018,V022,V026,V028,V030,V034,V038,V040,V042-V047 and their standalone proofs. The snapshot comparison is recorded in code/evidence. The two counterexamples above are independent exact mathematical checks.

Verdict: REFUTED for the literal full-velocity cancellation and parameter-free local-strain bound; OPEN for global source uniqueness and the unrestricted high-space statements; CONFIRMED for their precisely stated replacements and for the listed certificate comparisons. The overall report correctly states that nonlinear existence is not established.
