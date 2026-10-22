# Direct coefficient comparison supplement

Written 2026-10-22T11:42:06.664875+00:00, before executing the supplemental comparison.

The original scaling_norm_lower_bound run.py and replay.py compare returned dictionaries. These contain exact Q values and density polynomial SHA256 digests, not the individual density coefficients. Thus the old field density_coefficient_equalities=6264 overstates that executable comparison. It counts reconstructed coefficients whose digests agree. The old preparation acceptance and its reviews require this correction; they do not alone establish literal coefficient equality. No original frozen source or accepted file is modified.

The additional code/direct_coefficients.py will reconstruct all 261 degree-seven angular density polynomials independently by Cox recurrence and de Boor recurrence on exactly spans 7, 620, 1564. It will compare each of their 8 exact rational coefficients directly, and independently form B and C and compare every coefficient of both. It will compare exact square integrals against the saved rows, using monomial squares and shifted-Legendre orthogonality. All three spans must pass before the application can be accepted. No other span is covered.

The mathematical annulus lower-bound proof is unchanged. This supplement discharges its explicit full-polynomial-equality hypothesis only after successful computation and a later actual review. The original generic full-span workflow is not upgraded and no 1558-span computation is claimed.
