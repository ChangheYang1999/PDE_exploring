# Result333: selected high-precision angular inverse operands

Written 2026-10-22T09:20:13.173012+00:00 before new numerical code. This finite sensitivity audit is separate from the conditional continuum theorem331. It concerns the saved auxiliary hydrostatic stateB, not the primary elliptic IPM inverse.

## Exact finite definitions

Choose index254, the already observed maximum perturbation and finite divergence-proxy point in327, at each radius3 and30. This is an a posteriori witness selection, not a global verification set. Freeze the same B-rule physical nodes and the binary64 combined weights actually used by327. The inner V2 weights are fl(a_weight*a_node), the outer/tail V2 weights are fl(y*weight), and the V1/tail weights are0 on the inner part and the original outer/tail weights elsewhere. No new quadrature rule is introduced.

At a central binary64 x and node s, epsilon values are0,1e-5,1e-6. Freeze h=fl(epsilon*(1+hypot(x,s))) and xplus=fl(x+h), xminus=fl(x-h), exactly as the327 worker. For epsilon>0 the high-precision comparison quantity is D_epsilon^rounded=[F(xplus,s)-F(xminus,s)]/(2h), with all frozen operands interpreted as exact rationals; F is the x derivative of the same reconstructed density. At epsilon0 use H=g_xx. This tests high-precision differentiation and arithmetic at the actual rounded sample coordinates. The two rounded coordinates need not be exactly symmetric around x. Therefore this is not the exact mathematical D_epsilon in331, and331 does not directly enclose this finite calculation.

An independent scalar density implementation reconstructs the compact radial map through safeguarded high-precision Newton and the angular factor through complex arithmetic. mpmath differentiation at72 and108 decimal digits supplies F,H and local g,g_x,g_y,g_xx. The own double Cartesian chain-rule evaluator is used only for comparison and geometry replay. Producer code is never imported or executed.

For every integral component let B be the stored double velocity, D the exact rational sum of the frozen double weights times double integrands, and M the exact rational sum of those weights times the serialized MP decimal integrands. The identity M-B=(M-D)+(D-B) separates changed integrand operands from floating products and summation. MP decimals themselves are finite rational observations, not certified enclosures. The72/108 change is empirical precision sensitivity.

At a selected target the local and inverse differences are also separated. Let R(j,v)=(2x+v1)j_x+(2y+v2)j_y-j_0. Then

R(jM,vM)-R(jD,vD)=[R(jM,vD)-R(jD,vD)]+[R(jD,vM)-R(jD,vD)]+(vM-vD).(grad jM-grad jD).

Expansion proves this exact finite identity. Nf and Nv are recomputed for each of the four combinations; any fixed-Nf_D normalized difference is labeled separately. Zero denominators remain undefined.

## Prospective verification and execution

Before candidate execution, test the finite weighting and decomposition algebra on exact rational synthetic operands. Test the differentiation and centered-difference records against a Gaussian with independent analytic F,H and against polynomial local identities. Check checkpoint chunk recovery on a small manufactured record. Rebind327 sources and data,331 scope only if cited, and the complete physical geometry against the stored327 point values. Record state SHA, every module origin, precision settings, source hashes, PID, time limit, one thread, nice19 and14GiB cap. One detached heavy job runs only after332 replay has exited.

Each precision is checkpointed in small numbered chunks. A later shift may collect complete chunks; incomplete chunks are not accepted. An independent results checker must recompute exact sums and residual decompositions from the frozen fields. Candidate-specific conclusions remain OPEN until that checker and an actual Opus5.5 review have been resolved. No inverse quadrature error bound, full-grid precision bound, historical cause, auxiliary exact profile or primary endpoint follows.

All writes stay in this lane. No JavaScript/TypeScript/Node, servers/listeners/tunnels, RLScience cluster, Lean/Lake, commits/push/posts or human contact. One heavy single-thread nice19 process below16GiB; each shell command below10minutes.
