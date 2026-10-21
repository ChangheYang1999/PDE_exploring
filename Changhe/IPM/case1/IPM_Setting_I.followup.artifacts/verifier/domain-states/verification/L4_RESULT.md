# Independent audit of the completed L=4 trial

Date: 2026-10-20. All evaluations use this lane's field reconstruction, full-plane inverse and differentiation. No numerics-lane evaluator is imported.

The frozen input dnB_n96m40SL4.npz has md5 c103a60bbbf2279e7c21f4f5a2b580be, N=96, M=40, L=4, beta=0.9 and c_l=5.574689635078895. The snapshot came from the completed trial in the numerics lane's runs directory. L is a compactification scale, not a finite physical boundary. The nodal reconstruction error is below4e-13. The first radial row equals1 exactly; density parity and cubic normalization hold. These do not imply a smooth factor at the center.

The independent angular moment gives c=15.724068046101149 and 3c_l-1-c=8.59135536e-7. The 4096-angle canonical velocity has U(0)=0 and a positive-axis zero x*=8.577249196807788. Refinement from2048angles changes x* by -1.1208812e-11. The corresponding source g is29.5476798225233. At the smaller differentiation step the transverse source eigenvalue has h(P)-1=-2.03711422e-6. Density and velocity parity defects in the prescribed check are zero to stored floating precision. Adding a harmonic strain to repair any identity is not part of this audit or the canonical law.

On the common58point sample, 4096angles, radial Gauss order28, panel width at most0.08 and outer radius10^30 give

    max |R|/N_f = 0.00382566619497
    at (x,y) = (2.898862035813389, 7.456312687737810).

Here N_f=|rho|+sum_i|W_i partial_i rho|. With N_v=|rho|+|X.grad rho|+|U.grad rho| the sampled maximum is0.00760406550198 at(0.362357754476674,0.932039085967226). The finest Cartesian density step is1/32000 times max(1,|x|,|y|). The maximum signed R/N_f effect from the two coarser steps is1.59811e-10; comparison with the independent polynomial chain rule gives1.12289e-10. Thus the transport failures are resolved by these derivative checks.

At the independently located source, the physical residuals are

| Point | |R|/N_f | |E|/|rho_x|, smaller step |
| --- | --- | --- |
| (x*,0.1) | 4.84937842e-7 | 1.34815174e-7 |
| (x*,1) | 2.41928903e-4 | 5.82378302e-8 |

The elliptic defect is E=-partial_x U_2+partial_y U_1-partial_x rho. The preceding elliptic values use Cartesian eighth-order velocity differentiation. Halving its step from0.005 to0.0025 changes the first ratio from1.34902412e-7 and the second from5.82225025e-8. Elliptic success at those points does not remove the transport defect.

For the six fixed main-audit points shared by the coarse and fine inverse rules, the maximum signed velocity-induced change in R divided by the fixed fine N_f is3.936633e-9. The two near-source points move slightly with the independently found root and are not silently treated as identical observation points. This comparison changes both angular and radial inverse rules; it is an observed difference, not a certified quadrature bound.

An exact exterior density constant is C=1484032 in |rho|<=C r^(1/5) for r>=1. The exact exterior-velocity bound at the sample points is at most3.710451008e-14; its contribution to R/N_f using the numerical gradient is at most1.66973e-15. The exact omitted strain bound is5797/1562500000000000000000. These enclose the infinite exterior only, not the interior quadrature or floating arithmetic.

The independent256-bit interval evaluation for the ideal-node binary interpolant excludes zero from both the forbidden fifth-degree sine7 coefficient (-0.00690881001998926445) and the center transport determinant (-0.00021286680845915617348). The first refutes smoothness of its factor, and the second refutes exact transport of that fixed represented field. They do not exclude a smooth limit of other fields.

Verdict: CONFIRMED for the finite physical checks, canonical gauge, cubic normalization and parity; REFUTED for smoothness and exact transport of this fixed interpolant. Its sampled transport residual does not meet the1e-6 standard. Comparison with L=8 concerns different stationary trials and gives no domain-convergence theorem. In particular the numerics lane's statement that the L=4 collocation residual is larger does not imply that this physical sampled maximum is larger: our L=8 same-grid snapshot has0.00548170121946 on the identical58points. Neither endpoint is reached.

Evidence: dnB_n96m40SL4_summary.json records all input hashes and extracts; the strain, balls, reconstruction, physical and broad4096 JSON files retain the raw independent results. Code/summarize.py reproduces this extraction from the completed files.
