# Common physical sample across five resolutions

2026-10-21T00:21:05.922904+00:00. Finite arithmetic completed, independent audit pending.

|N,M|c_l|max R/N_f|RMS R/N_f|max R/N_f120|
|---|---:|---:|---:|---:|
|72,30|5.56297828849|0.00590303704436|0.00142155859168|0.00613909025092|
|84,35|5.60015699621|0.00678329917656|0.0014147118419|0.00680254992193|
|96,40|5.57623817044|0.00548170121831|0.00129301162919|0.00554443234812|
|108,44|5.5751891918|0.00252613493977|0.000816564106749|0.00252996509633|
|120,48|5.57469254218|0.0026269804156|0.000648851220536|0.0026269804156|

All numbers are computed from this lane's own saved physical components on the same58ordered points. Exact binary-rational residual/normalizer arithmetic was cross-checked against290 independent Decimal evaluations at110digits. Maximum discrepancy4.8457e-107. Different radial quadratures are disclosed in PROOF.md. The maximum is not monotone:108to120 increases, while RMS decreases. This does not exclude eventual convergence or establish it. Changing to the shared120denominator does not remove either observed increase of the maximum. The raw state and code hashes are in verification/comparison.json.

The fifth-state median is0.00012924880367383957; RMS0.0008165641067487909. The numerical report's1.5e-4 median is a transcription/arithmetic discrepancy;1.3e-4 is the correct rounding. Other audited fifth summary statistics agree.

No continuum inverse error, kernel, family, isolation, B_j vanishing or task endpoint follows.
