Written 2026-10-30T01:50:02Z (lead, shift 5). Lead reduced-sensitivity calculation (tools/sensitivity.py v6, sha in tool.sha256) of the F1 m2
end (S05 FREE lineage, iteration 386) from the complete J_c EVAL record in the frozen copy runs_l/jceval_v5_f1_S05_m2_004618
(validation/jc_eval/f1_S05_m2_L6_cl0.4500_om0.3000_free/linearization_00386_eval_complete.npz; hashes in inputs.sha256).
Producer-side calculation (lead tool on the producer record); compared with the verifier's independent V560.

Valid output: f1_S05_m2_L6_cl0.4500_om0.3000_free.json, run with the explicit declaration "optimizer" (the record's
"coordinates" key reads optimizer (z_c, z_w); chain factors 0.024982814507583145, 0.5044761032568639).
INVALID_misinvoked_f1_S05_m2.json: first run at 01:48Z with the jc_eval.json path passed as the second argument, which the
tool reads as the coordinate declaration; an unrecognized declaration was taken as "physical" and the chain conversion was
skipped. Scaled quantities (eta, rank, absorption, scaled Schur eigenvalues, condition, predicted decrease) are unaffected;
every physical-unit quantity in that file is wrong. Kept for the record only. No earlier lead sensitivity output is affected
(all read "optimizer" with chain factors; checked over notes/sens_*).

Agreement with V560 (cutoff 1e-12): rank 1451; absorption 3.4687538357633517e-06 and 9.407966142853863e-05; scaled Schur
eigenvalues 1.156664726736833e-11 and 8.851448300414212e-09; condition 765.2561797562375; physical eigenvalues
3.8192574489187254e-07 and 4.962053824306046e-06; reduced step (0.04897499452826491, 0.13167902031844364); predicted
relative decrease 0.04827970915274477; eta 0.833745940439051 / 0.8318737097527501 / 0.8286649856059534 / 0.7359646300501492.
All agree with V560 to the printed digits (the step's omega component differs by 1.2e-11 absolute).
1 per cent widths about the model minimum (c_l, omega) = (0.49766, 0.63616): soft direction d_c_l 0.0312, d_omega 0.0216;
stiff direction d_omega 0.1077 (optimizer log-omega half-width 0.1077/0.5045 = 0.2135; physical-minimum logs +0.156/-0.186).
Numerics, not a proof. Local linear-model quantities, not parameter uncertainties.
