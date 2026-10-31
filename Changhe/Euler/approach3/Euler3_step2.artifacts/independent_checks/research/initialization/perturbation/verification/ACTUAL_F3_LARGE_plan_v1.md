# Saved F3 size 0.1, seed 2: independent initialization check

This plan applies the already qualified V509 method to the second actual F3 initialization, F3_S01_1e-1_s2.pt. It concerns the raw file and its worker entry, not the optimized endpoint. The producer summary was read before this registration.

Freeze the actual source, generated checkpoint, producer record and implementation sources. Reconstruct NumPy default_rng(2), its non-axisymmetric coefficient mask and the recorded scale. Check the exact unchanged physical parameters, m=0 entries and inactive E entries. Use the independent extended-precision velocity implementation on the original training geometry to check the requested raw size 0.1 and every reported shell size. Use the same relative tolerance 1e-8 and absolute tolerance 1e-12 as V509.

Replay phase alignment and the phase/tail/parameter entry map separately. Check coefficients and arrays agree before every independent field calculation. Evaluate raw and entry fields on physical-volume rules 4/18/40 and 8/32/64 with new azimuthal phases 0.297463 and 0.719583. Recompute the far-field norm and gauge. Retain the V509 gauge comparison rule, relative tolerance 1e-9 and absolute tolerance 1e-10, and the phase-invariance rule 1e-12. Check complete producer O1 only for finite additive consistency; do not call it an independent pressure evaluation.

Report the actual raw and entry distances separately. No endpoint recovery, removal or retention of the perturbation follows from this initialization check. All sampled norms are finite-grid observations. The exact fixed-parameter coefficient-mask proof remains research/initialization/perturbation/PROOF.md.

Execution uses CPU35, one thread, nice10, an empty CUDA_VISIBLE_DEVICES, and a bounded recursive controller pause. No JavaScript/TypeScript, servers, cluster, remote compute, or writes outside this side are used.
