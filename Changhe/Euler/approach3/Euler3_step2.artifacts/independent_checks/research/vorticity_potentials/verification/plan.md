# Tensor-grid vorticity qualification plan

Registered 2026-10-29T00:47:53.308272+00:00, after writing the informal proof and before implementing or running the tensor-grid evaluator.

Preserve the qualified field and spatial implementations. Write a separate wrapper using the existing extended angular matrices and the new vorticity potential identity. It must not evaluate negative powers at r=0; use the Cartesian spatial evaluator there. Check U,DU,Omega,DOmega and stable curl(LU) against the independently differentiated Cartesian evaluator on both the manufactured field and S01, at r/R0 in{1e-6,0.2,0.7,2,256,65536} and six directions including both axes and nonsymmetric points. For U,DU,Omega,DOmega require relative norm difference<=2e-13. For nonzero ordinary curl(LU) use the same relative tolerance, and for r>=256R0 use2e-6 times |U|^2/r^2, as already registered for the spatial evaluator. These tests depend on the spatial v2 qualification passing. Record source hashes and failures.

Once qualified, use fresh volume quadrature for partial vorticity diagnostics. Report actual volume domains, both five-term and single-term ratios, and truncation of global integrals. No full Tier verdict follows from this evaluator qualification or a partial diagnostic.

Extension registered 2026-10-29T00:49:48.400926+00:00, before qualification: also implement the same potential identity for scattered Cartesian points using second-order angular polynomials and the existing first-derivative assembly. Check it against the full Hessian route on the same72 nonzero points and on the origin for each field. All thresholds are unchanged; exact zero references must match exactly. This avoids requiring third angular derivatives at every centered-ball quadrature point.
