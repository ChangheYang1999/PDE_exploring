# Common physical sample across five resolutions

2026-10-21T00:28:50.425492+00:00. Finite arithmetic completed, review followup pending.

|N,M|c_l|max R/N_f|RMS R/N_f|max R/N_f120|RMS R/N_f120|
|---|---:|---:|---:|---:|---:|
|72,30|5.56297828849|0.00590303704436|0.00142155859168|0.00613909025092|0.00143411434011|
|84,35|5.60015699621|0.00678329917656|0.0014147118419|0.00680254992193|0.00142019600582|
|96,40|5.57623817044|0.00548170121831|0.00129301162919|0.00554443234812|0.00129665484328|
|108,44|5.5751891918|0.00252613493977|0.000816564106749|0.00252996509633|0.000816927985018|
|120,48|5.57469254218|0.0026269804156|0.000648851220536|0.0026269804156|0.000648851220536|

All numbers come from this lane's own saved physical components on the same58 ordered points. The aggregation uses exact rational arithmetic on their parsed binary values. A second arithmetic implementation using110-digit Decimal checks R,N_f,N_v and both ratios, 1450 quantities across 290 rows; maximum absolute discrepancy 1E-106. This checks arithmetic on identical inputs and is not another physical inverse evaluation.

Both own and fixed-denominator maxima increase at72to84 and108to120. Both RMS sequences decrease at every step. All are finite-sample statements. Different radial quadratures were disclosed in the original protocol and are now asserted in code:4096angles, order28/panel0.08 for72/84/108, order32/panel0.075 for96/120, cutoff10^30. No rigorous interior quadrature bound is available. These finite sequences neither establish nor preclude eventual convergence.

All gradients use the same eighth-order Cartesian stencil and final relative step1/32000. The source programs and state identities were manually checked and pinned, including the120 filename dnSB_n120m48.npz. N_f is the principal triangle normalizer; N_v is an earlier secondary diagnostic without c_l in its drift term. No triangle-bound interpretation of N_v is used.

The fifth-state median is0.00012924880367383957; RMS0.0008165641067487909. Manual report audit in ../report-audits/verification/num_0017_audit.json identifies the numerical report by MD5 and checks its new paragraph against AV150. That report's1.5e-4 median is wrong;1.3e-4 is the correct rounding. Its other stated fifth summary values agree at their reported precision. The aggregation computes the statistics; comparison against prose is a separate manual audit, not a hidden code assertion.

No continuum inverse error, kernel, family, isolation, B_j vanishing or task endpoint follows. Source identities, post-original-computation registration timing, code and results are pinned under verification/.
