from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
folder=root/'07_diagonal_identity_term/finite_small_values';folder.mkdir(exist_ok=True)
(folder/'PROOF.md').write_text('''# Strict separation at three small positive exponents

Use the real homogeneous Euclidean Hölder seminorm on R^2, the quotient-space singular integrals, and the smooth compact-test suprema defined in `../../01_setup/PROOF.md`. Let C_alpha be the common norm of T_xx and T_xy and D_alpha the norm of R_1^2. Then

| alpha | C_alpha upper | D_alpha lower | D_alpha - C_alpha lower |
|---|---:|---:|---:|
| 1/1000 | 637.0652723887 | 637.3340501785 | 0.2687777898 |
| 1/100 | 64.1129530993 | 64.3702681064 | 0.2573150071 |
| 1/20 | 13.2090680608 | 13.4165946841 | 0.2075266233 |

These are inequalities, not exact norms. The upper bounds are the V045 exterior-circle construction. The lower bounds use the witness and complete integral estimates of `../finite_projection_witness/PROOF.md`, with a=1, rho=1/6, delta=1/24 and R=4096. This is the same construction and the same three-patch 1024-by-1024 Arb160 regular-integral enclosure as `../finite_certified_values/PROOF.md`.

The sufficient seminorm constants are bounded by 1.000000240308, 1.000024085602 and 1.000608619784, respectively. They follow from `../refined_profile_constant/PROOF.md` and the cancellation-free auxiliary inequality in `../positive_profile_bound/PROOF.md`. The latter inequality follows from the midpoint Taylor remainder for t^k on [R,1], where k=1/(1-alpha). The 32768-cell Arb192 enclosure covers the interval between 10^-6 and 1-10^-6, with the previously proved analytic estimates on both omitted endpoints.

For each exponent the regular enclosure is added to the explicit local leading term, both analytic error terms are subtracted, and the identity contribution 1/2 is added. Dividing by the certified positive seminorm upper bound gives the reported lower endpoint, rounded downward to ten decimal places. Every row, common parameter and source hash is checked by `code/combine_finite_projection.py`. The full data are `data/finite_D_lower_a001.json`, `data/finite_D_lower_a01.json` and `data/finite_D_lower_a05.json` relative to the lane root.

The independent script `code/check_finite_small_D.py` recomputes the endpoint terms at 90 decimal digits, converts the adverse Arb regular endpoint to an exact rational, and verifies each displayed decimal against the resulting value. An independent 480-by-600 Gaussian quadrature lies in each regular enclosure. This floating comparison checks implementation consistency; the proof uses the interval enclosures and analytic bounds.

The fixed increments converge along the compact smooth approximations from the setup theorem. Thus the same lower bounds hold for the test-function suprema. Exact decimal subtraction proves the final column.
''')
files=['data/profile_constant_positive_certificate.json','data/finite_projection_fine_a001.json','data/finite_projection_fine_a01.json','data/finite_projection_fine_a05.json','data/finite_D_lower_a001.json','data/finite_D_lower_a01.json','data/finite_D_lower_a05.json','data/finite_small_D_independent_checks.json','code/check_finite_small_D.py','07_diagonal_identity_term/finite_small_values/PROOF.md']
(folder/'verification.json').write_text(json.dumps(dict(time_utc=now,verdict='CONFIRMED',files={f:sha256((root/f).read_bytes()).hexdigest() for f in files}),indent=2)+'\n')
with (root/'VERIFY_REPORT.md').open('a') as out:
 out.write(f'''\n## V055: Cancellation-free projection-profile enclosure\n\nDate: {now}\n\nClaim: For 0<alpha<=1/2, the sufficient profile constant K_alpha can be enclosed using the smaller of B(u) and the positive-term auxiliary upper bound in 07_diagonal_identity_term/positive_profile_bound/PROOF.md.\n\nMethod: Re-derived the midpoint Taylor bound for t^k on [R,1], divided by the lower derivative k R^(k-1), and checked the algebraic identity for B. Audited every interval and the two endpoint estimates in code/certify_profile_positive.py. The old certified formula remains available; the new one is an additional upper bound.\n\nResult: data/profile_constant_positive_certificate.json proves K_.001<=1.000000240308, K_.01<=1.000024085602, K_.05<=1.000608619784, K_.1<=1.002470641264, K_.2<=1.010555855930, K_.3<=1.026981110219 and K_.5<=1.089352283627. These are sufficient upper bounds, not exact seminorms.\n\nVerdict: **CONFIRMED**.\n\n## V056: Three further certified finite-exponent separations\n\nDate: {now}\n\nClaim: D_.001>=637.3340501785, D_.01>=64.3702681064 and D_.05>=13.4165946841. Their respective separations above the certified C upper bounds are 0.2687777898, 0.2573150071 and 0.2075266233.\n\nMethod: Applied the already audited finite projection enclosure with a=1, rho=1/6, delta=1/24, R=4096 and 1024-by-1024 cells on each of three patches. Rechecked source hashes and exact row coverage, and combined with V055. Independently recomputed all endpoint terms at 90 decimal digits from exact adverse regular endpoints. Separate 480-by-600 Gaussian values lie inside all three regular enclosures.\n\nResult: Every displayed D lower endpoint lies below the independently recomputed value. Complete statement and proof: 07_diagonal_identity_term/finite_small_values/PROOF.md. The adjacent verification manifest records exact input hashes. These inequalities apply to the homogeneous seminorm and the compact smooth test-function supremum.\n\nVerdict: **CONFIRMED**.\n''')
with (root/'NOTES_FOR_TEAM.md').open('a') as out:
 out.write(f'''\n## {now}: V055-V056, small-exponent strict separations complete\n\nCertified: D_.001>=637.3340501785 > C_.001 upper637.0652723887; D_.01>=64.3702681064 > C_.01 upper64.1129530993; D_.05>=13.4165946841 > C_.05 upper13.2090680608. Data finite_D_lower_a001/a01/a05.json use the same schema as the earlier .1/.2 files, so the lead table generator can include them. Complete proof and manifest: 07_diagonal_identity_term/finite_small_values/. Positive profile K bounds also cover .3 and .5. Next I will certify the extended projection family at .3 and develop paired local-circle upper transport.\n\nThe full cone envelope of the current axis D LP data interpolates its nodes within 5.2e-13, but two independent continuous quadratures give only about1.649, against the discrete objective2.49066. A denser interpolated proposal gives about1.739. These are diagnostic observations, not certified bounds or a refutation of the LP experiment. The finite-node objective cannot yet support a continuous lower-bound claim. Also the statement that the finite-alpha norm is not attained in the diagonal direction should remain a numerical conjecture: a fixed-grid direction scan alone cannot prove it.\n''')
p=root/'code/build_verified_table.py'
s=p.read_text().replace("['finite_D_lower_a10.json','finite_D_lower_a20.json']","['finite_D_lower_a001.json','finite_D_lower_a01.json','finite_D_lower_a05.json','finite_D_lower_a10.json','finite_D_lower_a20.json']")
p.write_text(s)
index=root/'INDEX.md'
with index.open('a') as out:out.write('\n- `07_diagonal_identity_term/positive_profile_bound/PROOF.md`: stable sufficient profile constants (V055).\n- `07_diagonal_identity_term/finite_small_values/PROOF.md`: three further certified strict separations (V056).\n')
print(now)
