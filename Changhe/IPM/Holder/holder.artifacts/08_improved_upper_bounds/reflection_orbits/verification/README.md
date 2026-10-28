# Verification evidence

Updated 2026-10-28T02:38:19Z.

The version-1 numerical certificates were RETRACTED in V036 because an inner assignment overwrote the integration angle. Their source snapshots are preserved here only for audit; their data are in data/retracted/. They must not be used.

The finite four-point transport proof remains valid. Its LP comparison is diagnostic. The corrected version-2 coarse Arb certificate is confirmed in V037, with an independent Cartesian/direct-radius Gauss comparison.

- Current source SHA256: `08e4a15e2c0c7f35f70709be786388c664729e7105348fcd0cbd9881abf9de48`.
- Corrected coarse data: `data/reflection_orbit_certificate_v2_coarse.json`.
- Independent comparison: `code/check_reflection_integrals.py` and `data/reflection_regular_diagnostic_v2.json`.
- Finite LP diagnostic: `data/reflection_orbit_lp_diagnostic.json`.
