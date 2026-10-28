# Binding sign clarification

Recorded 2026-10-28T17:02:34.067756+00:00, during the verifier's second read before the independent audit was recorded.

In the statement of PROOF.md, replace `c[h]=partial_x U1[h](0)` by

    c[h] = -partial_x U1[h](0) = partial_y U2[h](0)
         = psi_xy[h](0).

This is the established strain convention of topics01 and213. If v=(-Delta)^(-1)h, it also equals partial_xxy v(0). The positive kernel Kc in the strain-correction section of PROOF.md already has exactly this established convention. Consequently the exact c=0 correction there, the compact positive c=1 function, all displayed velocity kernels, every upper and lower estimate, and the conclusion are unchanged. The first-line derivative sign was a transcription error, not a changed definition of the operator. No assertion uses the erroneous sign.

This sidecar is part of the theorem statement and must accompany any adoption or quotation of the proof. The original proof is preserved unchanged so the submitted audit hash remains reproducible. The theorem is still awaiting independent audit.
