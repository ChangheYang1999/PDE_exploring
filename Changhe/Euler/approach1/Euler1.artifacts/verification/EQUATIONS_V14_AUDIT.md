# Equation summary v1.4 audit

Date: 2026-10-23T07:26:20.053110+00:00. Source SHA256: `151650c843e884f4c13b8f5c70882ea0c4b11ed285abb7b041464c984ef7f962`. Snapshot: `snapshots/EQUATIONS-151650c843e884f4.md`.

The canonical equations are confirmed. The new section 9.3 contains a correct L2 statement but five incorrect or insufficiently qualified summary clauses. These do not refute the full independently proved theorem. The previous section 7.2 Fourier classification defects also remain in this version; all unchanged derivations retain their earlier dated checks in evidence/equations_audit_current.json.

| Check | Verdict | Method and result |
|---|---|---|
| 9.3 spectrum wording | REFUTED | A negative real eigenvalue is not always present. For U=(-x/2-a*y,a*x-y/2,z), a nonzero, spec(DV)={c-1/2+ia,c-1/2-ia,c+1}. Use negative-real-part eigenvalue. Rank two does give two nonzero real eigenvalues of opposite signs; rank three need not. |
| 9.3 local zero-set wording | REFUTED | At rank two the implicit function theorem contains the full nearby zero set in a C2 arc; it can initially be a closed subset of that arc. Only the subsequent connected-alpha argument supplies an actual equilibrium subarc. Say isolated point or closed subset of a C2 arc. |
| 9.3 sublinear conclusion | REFUTED | Nonzero constant U=b with P=-(1-c)b dot y is an exact sublinear solution. The theorem gives no nonconstant sublinear profile, or no nonzero profile under global decay. Use those words instead of no nontrivial profile without defining nontrivial. |
| 9.3 growth scope | REFUTED | Sublinear unbounded growth is included. Replace growing velocity in the exclusion list by failure of sublinearity, including affine backgrounds. |
| 9.3 relative-residual implication | REFUTED | The qualitative compactness floor concerns true whole-space absolute L-infinity momentum residual under all fixed class bounds. A relative residual requires a specified uniformly bounded denominator and global norm before this implication follows. Finite-sample relative training or holdout residual is insufficient. Merely decreasing toward a positive floor is also possible. |
| 9.3 L2 exact theorem | CONFIRMED | The theorem statement Omega=0 and U constant under C2, uniform U=o(R), 0<c<1/2 is independently proved. Its decaying specialization excludes the full primary class. See THEORY_V3_AUDIT.md and research/uncountable-stagnation/PROOF.md. |
