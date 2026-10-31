# Independent radial implementation of the proved identity

Status: derivation checked before implementation; runtime checks pending.

The code in `independent/src/independent_linear.py` uses only the independent
radial jets and angular tables. It does not import a production field evaluator.
The exact statement and proof are in the parent `PROOF.md`.

Write q = r^2, k = R0^2/(q+R0^2), and B_q = dB/dq. The radial coefficient
inside the transformed twisted potential is

    (delta + c nu k) B + 2 c q B_q + w k S M B_partner,

before applying the existing coefficient twist. Here S is -1 for a cosine
coefficient and +1 for a sine coefficient, and M is the nonnegative azimuthal
index. This follows because the coefficient vector for partial_phi is
`-S M B_partner`. The coefficient twist commutes with that constant rotation
matrix. For the untwisted E channel, the last term is `w S M B_partner`,
without k. The envelope still contributes c nu k. The exact deltas are zero
for A/C, -1 for B/D, and 1-c(ell+3) for E. Damping is included in B before
forming B_q.

The transformed velocity uses only the value of the toroidal radial
coefficient and the value and first q-derivative of the poloidal coefficient:

    U_linear = sum[f (grad H cross y)
                   + ((ell+1) g + 2 q g_q) grad H
                   - 2 ell g_q y H].

Consequently the first derivative of B_q is sufficient, so B through two
radial derivatives suffices. The implementation must not expose a second
radial derivative of the transformed coefficient: its scratch second-jet
slot omits B_qqq and is not valid. Only the finished velocity is public.
At q=0 all expressions are finite and use the Cartesian angular polynomials.
For positive radii, evaluating the angular features on unit directions and
restoring homogeneous powers reduces large powers inside the polynomials.

Qualification requires agreement with the direct linear combination at
ordinary radii and independent 70-digit direct evaluation at far radii.
Neither this identity nor those finite checks is an error bound for pressure.
