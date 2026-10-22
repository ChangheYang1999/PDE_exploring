# Topic97: certified dilated auxiliary inverse, V32

Read PROOF.md, ADDENDUM.md and AUDIT_METHOD.md together. The final
verdict is evidence/verdict.json after the complete audit passes.
The exact normalized modal_v2 trial and the explicit C4 cutoff of topic95
are unchanged. Its maximal-domain auxiliary inverse satisfies the strict
bounds below. N_(1/ell)(u)^2=integral(ell^(-2)+|xi|^2)^s |uhat|^2.

| order s | scale ell | norm | inverse bound |
|---|---|---|---|
| 3.05 | 1/500 | N_500 | <608 |
| 3.06 | 1/500 | N_500 | <554 |
| 3.1 | 1/500 | N_500 | <473 |
| every3.05<=s<=3.1 | 1/500 | N_500 at that s | <922 |
| 3.06 | 3/1000 | H^3.06 | <5.743e10 |
| 3.1 | 11/4000 | H^3.1 | <6.968e10 |
| every3.05<=s<=3.1 | 3/1000 | H^s | <1.223e11 |

For the requested scales at s=3.1, ell=delta=33/2000 gives
R^*<679.382 and the N_(1/ell) inverse bound<5.7e6. At ell=7/2000,
R^*<48.225 and the inverse bound is<1874. At ell=1/500,
R^*<29.812 and the inverse bound is<473. These are rigorous upper
bounds for this chosen cutoff, with imported coarse trial derivative
ceilings. They are not the lead's floating values for a different cutoff.

The new calculation takes about one second and requires no new PDE
or canonical Green integration. It uses exact weighted radial integrals
of cutoff derivative tensors, a Leibniz-Minkowski L2 estimate, scaled
H3/H4 bounds and fractional interpolation. Two rational reconstruction
and integration methods compute all15 moments; Arb512 and iv180 check
81 scales at three orders and with a whole-order-interval formula.
A third exact quadrature and higher-precision output audit are required
before final acceptance.

The physical rank-one term, outer matching, saddle and far-field spaces,
residual in the global error norm and nonlinear closure remain open.
An upper bound is not a lower bound on the true inverse norm. This is
not a decisive YES or NO endpoint.
