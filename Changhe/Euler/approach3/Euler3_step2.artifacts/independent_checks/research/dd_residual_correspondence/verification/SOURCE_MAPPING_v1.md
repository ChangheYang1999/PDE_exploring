# Frozen v8 source map

Scope: artifacts/dd_same_S01_snapshot_v1/code, dd_chain.py SHA256 4e3eaff8be4b52c2af1a7ab28cb588d0be7f25093217b58209d074a98b5ce097. Both named S01 and S05 copies use the same mathematical helpers. Read with ../PROOF.md and the V270/V273 same-function checks, V276/V279 named reproductions and elementary qualification, which is still pending when this map is written.

| Copied operation | Production definition | Review finding |
| --- | --- | --- |
| dd_tables.matrices_dd, dd_chain.tables_dd | radial.RadialBasis.matrices; fields.Model.radial_derivs | Same envelopes, Chebyshev map, damping and derivative factorials. Fixed inputs imported as binary64 values. E table omits lmask=[0,1]; named stencils have exact zero low-degree E coefficients. |
| dd_tables.twist_tables_dd, dd_chain.twist_dd | RadialBasis.twist_tables; Model._twist | Same beta, derivative Leibniz factors, partner indices and signs. E added after twist. |
| dd_tables.expand_dd | TailConstraints.expand/_solve_pair/_solve_single/_solve_k2 | Same homogeneous zero-viscosity systems, reduced order A,C,B,D,E, scatter/gather and unchanged E. k4 uses extended 8/3. |
| dd_chain.radial_derivs_dd_tables | Model.radial_derivs and fields_dd.radial_derivs_dd | Same contraction/channel order. Cross products are rounded and low-low products omitted. |
| dd_chain.velocity_dd | Model._assemble and fields_dd.scalar_sets_dd/scalar_grid_dd | Same U and G_mi formulas. Source is trace(GG); convection contracts U_m G_mi. |
| dd_tables.linear_radial_dd, dd_chain.linear_velocity_dd | linear_stable.linear_velocity | Same transformed envelope, damping derivative, channel delta and rotation terms. E ell<2 is explicitly zero here. |
| dd_pressure.build_tables_dd | PressureSolver.build_tables | Same quadrature geometry, logarithmic kernels, below/above masks, angular twist, source scale, Green prefactor, volume and l=1 moments. Exterior monopole excluded. Clamp-inactive check observes high words; recorded values are far below 700. Pair cross terms approximate products. |
| dd_chain._make_solve_dd_pairs | PressureSolver._solve_dd_core | Exactly three guarded substitutions retain P, pressure gradient, harmonic values and radial derivatives as pairs, plus function rename. Docstring saying two lines is stale. |
| dd_pressure.solve_dd_pairs_tables | PressureSolver._solve_dd_core | Same analysis, untwist, scaling, Green sums, radial derivative, synthesis and component order, with paired table operands. |
| dd_chain.scale_mom_dd, momentum_rows_dd | Problem.residual_vector | Same weighted component-major momentum rows. Fixed quadrature weights remain float64 inputs. |
| dd_chain.residual_dd and reference_fn | residual_vector_rebuild, residual_vector_rebuild_wd, objective_at | Jf holds weights/target, Jcw recomputes weights with point-specific pressure tables and holds target, Jc recomputes both. Closure/gauge and these selected quantities use production float64. |
| dd_chain.ladder_dd | Registered centered and five-point differences | Pairs retained through the numerator and division, then rounded once; active records include base and all twenty offsets. Independent arrays checked in V276/V279. |

The named Case constructor selects formulation mom, stable_linear=True, nu=0, radial_lambda_w=0, gauge F and sigmaZ=None. Appended far-anchor nodes set far_model=None; there is no fine pressure solver. Thus the omitted optional row branches are inactive. pressure_tables_dd's assertion ending in `or True` is a tautology and proves no restriction; this review instead checks the actual constructor and saved case configuration. This scope must not be generalized to a case with extra rows or a fine-grid gauge.

The scope manifest c3d7ca88ab146b3a6f239c22d2a45a384402c61c1fd2c117ae0e17ecf6ae9489 determines which ingredients change arithmetic. Neither this map nor finite agreement upgrades the mixed-arithmetic copy to a certified uniformly accurate evaluator. A source diff against earlier verifier snapshots is saved by the audit script; validation scaffolding changes are separated from mathematical helper changes by function hashes.
