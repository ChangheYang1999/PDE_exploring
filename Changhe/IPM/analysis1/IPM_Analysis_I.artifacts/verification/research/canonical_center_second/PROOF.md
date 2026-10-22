# Independent canonical center-moment validation

Written 2026-10-21T22:06:11.456329+00:00, before new code. Status OPEN until complete execution, independent audit, actual Opus5.5 review and later own adjudication.

## Exact statement and the distinct dependency

The inputs for143,144and145 are the thirteen center records in research/residual_samples/evidence/sample_result.json, SHA0608fe74dbeef4eaf21e26aedffe61453f558e25e0e902dd72fda6b3084f630c. They are not the endpoint archive original_knots.jsonl.gz. The original28 calculation used Arb320 exponential-moment integration on1571 intervals obtained by adding thirteen centers to the1558 original spans. Its independent Laurent audit shares those I/J inputs, so it is not a second integration. Topics156and173 validate and apply a different endpoint archive. They alone do not establish membership in the narrower center targets. This is a dependency distinction, not a claim that28's primary calculation is invalid.

Use the exactly normalized finite trial in research/modal_repair/PROOF.md, source JSON SHA57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6, at its distinguished exact normalizer z_star in certificate Z SHA0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a. The exact rational log-midpoints t_c correspond to cell indices0,5,100,500,1500,2761,3925,4102,4125,4211,5622,7038,7808 in the partition SHA56ce08f1b8d0ee7cf2508f23de5c29fff326167332021bdfd21fb5db005612f2. Each entire cell must lie in one original span and its stated center must equal the exact midpoint.

Write rho=r^3 sum_(j=0)^261 H_j(log r)sin((2j+1)theta), H_261=0. Define m=2n,1<=n<=261,

 I_n(t)=integral_-infinity^t exp(-(m+4)(t-s))H_(n-1)(s)ds,
 J_n(t)=integral_t^infinity exp(-(m-4)(s-t))H_n(s)ds.

The intended finite conclusion is that all13*261*2=6786 defining moment values belong to their unchanged exact serialized center balls, and all13*262*8=27248 exact local density coefficients belong to their unchanged serialized polynomial balls. There are262 density slots j=0,...,261 and261 stream modes n=1,...,261; no additional mode is claimed. Computation counts use those precise ranges.

## Exact source and infinite anchors

The independent source construction of156, research/canonical_archive_second/code/engine.py, is already accepted and pinned. It reconstructs the degree7 spline in normalized original-span coordinates by exact rational Cox recurrence and multiplies the full original control matrix by two independently matched angular conversion maps. It computes the complete analytic I anchor at the first knot and the affine J anchor U_n+V_n z at the last knot, with exact dependent six-jet corrections. This new calculation may reuse that accepted engine but no endpoint archive value as a propagation input.

For completeness, at the inner knot a_0 with s<=0 the exact branch is C_j+sum_l D_jl exp((2l+2)s)+exp(b_i s)sum_l e_jl s^l. Its integral equals

 I_n(a_0)=C_(n-1)/(m+4)+sum_l D_(n-1,l)/(m+6+2l)+sum_l e_(n-1,l)(-1)^l l!/(m+4+b_i)^(l+1).

The outer branch at a_S and u>=0 is sum_l A_jl exp(alpha_l u)+exp(-b_o u)sum_l e^o_jl u^l, plus C_j z[exp(alpha_0u)-exp(-b_ou)sum_(l=0)^6(alpha_0+b_o)^l u^l/l!]. Its integral gives

 U_n=sum_l A_nl/(m-4-alpha_l)+sum_l e^o_nl l!/(m-4+b_o)^(l+1),
 V_n=C_n(alpha_0+b_o)^7/[(m-4-alpha_0)(m-4+b_o)^7].

Here alpha_l=k-3-j_l(1-k)-2l_l with the exact source indices. All denominator positivity conditions are checked. The inner/outer e coefficients solve the exact seven triangular jet equations, and both the finite-geometric and factored formulas for V agree. Absolute convergence follows from these positive decay rates and finite sums. These formulas include the entire infinite tails, without numerical truncation. They preserve one common z, forming J_constant+J_z Z only at a comparison.

## Independent integration at centers

On original span[a,b], h=b-a>0, let P_j(u)=H_j(a+hu),0<=u<=1, an exact rational polynomial of degree<=7. Suppose y'=lambda y+P(t) in the physical log coordinate. In a normalized interval of width d, the equation becomes y_u=zeta y+d Q(u), zeta=lambda d. If zeta!=0, set q_8=0 and recursively q_k=((k+1)q_(k+1)-d Q_k)/zeta for k=7,...,0. Then q'-zeta q=d Q exactly by coefficient comparison, so

 y(1)=q(1)+exp(zeta)(y(0)-q(0)).

If zeta=0, use y(1)=y(0)+d sum_k Q_k/(k+1). This is an exact primitive, never a division by zero. The formula uses a finite exact particular polynomial and outward mpmath.iv exponential, a different integration method from28's truncated exponential-moment series.

Propagate I from its exact anchor across all original spans with lambda=-(m+4),Q=P_(n-1). For a center t_c=a+xi h,0<xi<1, evaluate its value directly from the current I(a), using d=xi h and Q_k=P_(n-1,k)xi^k. This leaves the main propagation unchanged. For J, start its constant/normalization parts at a_S and propagate backwards with lambda=4-m and Q(u)=P_n(1-u). From J(b), evaluate the center using d=(1-xi)h and Q(u)=P_n(1-(1-xi)u). Its coefficient of u^q is (-(1-xi))^q sum_(k>=q)binom(k,q)P_n,k. Propagate J_z by exp(lambda d) only, then form the target interval J_constant+J_z Z. All centers in one span are evaluated independently from its same endpoint values; they are not chained as propagation inputs.

Induction from the exact analytic anchors proves that every generated interval contains the defining canonical value. The exact local density coefficient of (t-t_c)^q is h^(-q)sum_(k>=q)binom(k,q)P_jk xi^(k-q), by the binomial theorem. Check each against its unchanged target. All H_261 coefficients and J_261 values are exactly zero; their zero-width targets must be met exactly. For n=2 the J propagation rate is zero and the exact primitive is used. Use iv200 at fixed precision throughout, unless a failure is preserved and a separately reviewed new version changes that choice.

## Directed target tests and independent output audit

Decode every original midpoint/radius target exactly as rationals. A new interval[l,u] validates it only if target_lower<=l<=u<=target_upper. Mere overlap is insufficient. A failed sufficient containment is OPEN; it refutes membership only if a separately justified disjoint enclosure excludes the true value. Never enlarge a target or replace a target record by a regenerated one.

Retain all6786 new interval endpoint pairs with cell,center,mode and family, not a sparse witness selection. Retain full propagation step counts, exact anchors, normalized source-coordinate checks, source/code/target hashes, completed footer and elapsed time. Independently re-read every saved pair with Python Fraction, re-decode every original target, check directed containment, mode completeness and exact point identity. Independently check the density-coefficient targets from the exact source, using the already accepted143 entire polynomial-binding result and current pins; if a new different construction is used, state its exact extent. An audit of saved intervals alone does not re-prove the global propagation; the full executed, reviewed integration and its mathematical soundness remain a premise of the certificate. Record that limit explicitly.

After actual full completion, the final result may explicitly discharge the center-box membership premise of143,144and145 by matching their exact shared input SHA, coordinate definitions, normalization, mandatory supplements and final accepted verdicts.143then retains its thirteen-point scope and all273 Wiener intervals;144and145retain exactly their three cells4102,4125,4211 and all other hypotheses, actual63bounds/cap comparisons and tail certificates. No numerical value changes. The final composition is a separate precisely checked application; successful integration alone does not automatically rewrite old verdicts. All analytic/arithmetic hypotheses and trusted-library limits remain. Preparation accepts no future execution.

## Acceptance and scope

Read and check this proof before implementing it. Obtain actual Claude Opus5.5 collaboration before computation and again for actual output; authenticate the actual model/end condition, complete request/response bytes, scoped verdict and full code/evidence bundle. Independently read its full response, resolve substantive objections, then create a separately later own adjudication. Pin all accepted dependencies and unchanged targets; no fake or partial record can count as complete. Every result requires full actual output, not a time budget or apparent numerical agreement.

No global derivative cover, physical maximum location, full forcing norm, global inverse, X3 distance, nonlinear closure or IPM endpoint follows. No original endpoint archive or historical producer array identity is inferred from these centers.

Restrictions: write only in ipmA-ver; no JavaScript/TypeScript or Node, no servers/listeners/tunnels, no RLScience cluster, no Lean/Lake builds, no outside writes, no people contact. The full calculation must wait for the lane's existing heavy radial job to finish, run single-threaded at nice19, and stay below16GB RAM. One heavy job only.
