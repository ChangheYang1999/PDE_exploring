# Independent review of the auxiliary Q nonlinear estimate

Reviewed by the root during the combined3 campaign. Reviewed source: `finite_rank/QNORM_NONLINEAR_BOUND.md` and its Arb calculator. This review does not certify a linear background estimate or a stationary solution.

Verdict: the stated outside-ball implication is correct under the identified inherited unweighted principal/core inequalities.

The exact identity for xjJq(a·grad g) follows from xj(a·grad g)=a·grad(xjg)−ajg and [xj,Jq]=q partial_j J^(q−2). The two direct advection pairings vanish because div a=0. The remaining commutator pairs are correctly split using Jq(xjg)=xjJqg−[xj,Jq]g. The inherited angular Hilbert–Schmidt core proof explicitly uses no test-function parity (combined2 T2_CEPS_v02, Lemma CORE remark(i)), so xjg is an admissible test even though it may leave S1.

The separate commutator operator bound follows by the mean value theorem and
\(\langle r+tp\rangle^{q-1}\le2^{q-2}(\langle r\rangle^{q-1}+|p|^{q-1})\). Young's inequality then gives the stated coefficient. The gradient Wiener constant S1 is exactly the Fourier Cauchy–Schwarz constant, with the vector norm and unitary normalization included.

All interpolation steps are in the correct direction: Q dominates the unweighted inhomogeneous Hq norm; the coefficient's homogeneous norm is at most M; Z/G is at most q(R/M)^(1/q) when G≥M. The product exponents use 1/q+theta=1−1/q. The two products produce the stated P and T after using G≥M, and the four weighted position pairings give the final factor2(qv+P+T). The factor (1+2z)² follows by a vector triangle inequality on (f,2Y), not a componentwise overcount.

The essential scope restriction must be kept: this is a bound for ||g||2≤R and Q(g)≥M, with frozen coefficient ||k||2≤R and Q(k)≤M. It is not asserted as the same homogeneous bound on every test function, and therefore does not by itself construct a uniformly stable high-space semigroup. A complete use must first establish qualitative high solvability for the actual frozen inverse (for example by verified positive frozen principal matrices and the existing lifting proof), then apply the outside-ball barrier, and finally pass from smooth coefficients to the complete Sobolev ball.

Subsequent bridge correction: the assertion that the stationary high inverse must be established first was unnecessarily restrictive. The independently reviewed Q_FORCED_EVOLUTION_BRIDGE_v02 proves finite-time Q evolution and applies this same exterior estimate to its forced trajectory. The trajectory stays in the ball and its L2 limit gives high regularity of the actual stationary inverse afterward. No old high-matrix or Garding lifting premise is needed. The scope of the nonlinear inequality itself is unchanged. Its delicate inherited core scalar constant also now has a fresh whole-half-line Arb verification in operator_theory/verify_nonlinear_core_scalar.py and nonlinear_core_scalar_result.json (see that directory for the exact output name).
