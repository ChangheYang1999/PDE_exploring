#!/usr/bin/env python3
"""Read-only reader for ONE full assessment record file (no ledger row needed; for the standalone handoff assessment of E3 option A). Prints the science
leaves in the same order as outputs/dev_v9/read_assessment.py and, with a reference record, the leaf differences. Usage: read_assessment_record.py <record.json> [reference_record.json]"""
import sys, json, hashlib
rec_path = sys.argv[1]; rec = json.load(open(rec_path)); print('record', rec_path, 'sha256', hashlib.sha256(open(rec_path, 'rb').read()).hexdigest())
def g(d, *ks):
    for k in ks: d = d.get(k) if isinstance(d, dict) else None
    return d
ti = rec.get('tight_independent_integral') or {}
print('candidate', rec.get('candidate_path'), rec.get('candidate_sha256')); print('code_manifest_sha256', rec.get('code_manifest_sha256'), 'basis_version', rec.get('basis_version'), 'began', rec.get('began_utc'), 'finished', rec.get('finished_utc'))
print('cl', rec.get('cl'), 'a0', g(rec, 'widths', 'a0') or rec.get('a0'), 'five_Taylor_max', rec.get('five_Taylor_max'), 'constraints', rec.get('five_Taylor'), 'center_abs', rec.get('center_abs'), 'poisson_max_abs', rec.get('poisson_max_abs'))
print('tight J_abs', {k: ti.get(k) for k in ti if k in ('J_abs', 'error_abs', 'accuracy_passed', 'J_mesh', 'J_mesh_minus_J_abs', 'training_J_abs', 'difference_from_trial_value', 'seconds')})
fm = rec.get('frozen32_maxima') or {}; rm = rec.get('refined_maxima') or {}
for t in ('E_f', 'E_rho'):
    print(t, 'frozen', (fm.get(t) or {}).get('value'), 'at', (fm.get(t) or {}).get('xy'), 'region', (fm.get(t) or {}).get('region'), '| refined', (rm.get(t) or {}).get('value'), 'at', (rm.get(t) or {}).get('xy'))
no = rec.get('near_origin') or {}; print('near_origin', {k: v for k, v in no.items() if isinstance(v, (int, float)) or v is None})
om = rec.get('origin_truncation_monitor') or {}; print('origin monitor worst', om.get('worst_band_relative'), 'stop', om.get('scientific_stop'))
sp = rec.get('rf_reference_spot_check') or {}; print('rf reference spot worst ratio', sp.get('worst_ratio'), 'stop', sp.get('scientific_stop'))
sn = rec.get('rf_spot_nodes_v912_v914') or {}; print('rf spot nodes worst random', sn.get('worst_ratio_random'), 'targeted', sn.get('worst_ratio_targeted'), 'stop', sn.get('scientific_stop'), 'random_failures', sn.get('random_failures'))
ff = rec.get('farfield') or {}; lead = ff.get('actual_leading_density_power') or {}
print('farfield exponent', lead.get('exponent'), lead.get('exponent_exact'), 'growth', lead.get('growth'), 'coefficient_L2', lead.get('coefficient_L2'), 'grows flag', ff.get('original_density_residual_grows'))
for N in ('1', '2', '3'):
    e = (ff.get('E') or {}).get(N) or {}; print(' E%s L2 %s unresolved(>19) %s fraction %s I_N %s' % (N, e.get('L2'), e.get('unresolved_harmonics_gt19_L2'), e.get('unresolved_fraction'), e.get('scale_invariant_ratio_I_N')))
comp = rec.get('completeness_v913') or rec.get('completeness') or {}; print('completeness', {k: (v if not isinstance(v, (list, dict)) else v) for k, v in comp.items()})
# Verdict: a conservative reconstruction of what assess_cadence860.py (lines 56 to 90) derives for the ledger row from a record (the record itself carries no
# top-level failed/scientific_stop). The wrapper reads two stop flags directly (origin_truncation_monitor.scientific_stop, rf_reference_spot_check.scientific_stop);
# this reader also checks a third (rf_spot_nodes_v912_v914.scientific_stop), so it can only be stricter than the wrapper, never more lenient. failed = completeness_v913.failed
# is not False (anything but the boolean False counts as failure); an untyped flag is a stop; mode full / is_full_assessment and tight-integral accuracy_passed are checked as the wrapper does.
compv = rec.get('completeness_v913') if isinstance(rec.get('completeness_v913'), dict) else {}
ti_ok = isinstance(rec.get('tight_independent_integral'), dict) and rec['tight_independent_integral'].get('accuracy_passed') is True
full_ok = compv.get('mode') == 'full' and compv.get('is_full_assessment') is True
failed_flag = compv.get('failed'); failed = failed_flag is not False
flags = {'origin_truncation_monitor': om.get('scientific_stop'), 'rf_reference_spot_check': sp.get('scientific_stop'), 'rf_spot_nodes_v912_v914': sn.get('scientific_stop')}
untyped = [k for k, v in flags.items() if not isinstance(v, bool)]
stop = bool(failed or untyped or any(v is True for v in flags.values()) or not full_ok or not ti_ok)
print('VERDICT (conservative reconstruction, not stored in the record; stricter than the wrapper by the third flag): full assessment %s (mode %r, is_full_assessment %r); tight integral accuracy_passed %r; completeness_v913.failed = %r -> failed %s; stop flags %s; untyped %s; SCIENTIFIC STOP WOULD BE RAISED: %s; sources %s' % (
      full_ok, compv.get('mode'), compv.get('is_full_assessment'), (rec.get('tight_independent_integral') or {}).get('accuracy_passed') if isinstance(rec.get('tight_independent_integral'), dict) else 'missing', failed_flag, failed, flags, untyped, stop,
      [k for k, v in flags.items() if v is True] + (['failed_assessment_v913a'] if failed else []) + (['untyped_scientific_stop_flags: %s' % untyped] if untyped else []) + ([] if full_ok else ['not_a_full_assessment']) + ([] if ti_ok else ['full_record_without_passed_tight_integral'])))
print('stored top-level fields (absent in a record; the ledger row carries them): failed', 'absent' if 'failed' not in rec else rec.get('failed'), 'scientific_stop', 'absent' if 'scientific_stop' not in rec else rec.get('scientific_stop'), '| sampled_only', rec.get('sampled_only'), 'peak85 checks', [c.get('passed') for c in (rec.get('peak_independent85_checks') or [])])
if len(sys.argv) > 2:
    ref = json.load(open(sys.argv[2])); rff = ref.get('farfield') or {}; rfm = ref.get('frozen32_maxima') or {}; rti = ref.get('tight_independent_integral') or {}
    print('\nREFERENCE', sys.argv[2], 'candidate', ref.get('candidate_sha256'))
    print(' J_abs tight: this %r ref %r' % (ti.get('J_abs'), rti.get('J_abs')))
    for t in ('E_f', 'E_rho'): print(' %s frozen: this %r at %r | ref %r at %r' % (t, (fm.get(t) or {}).get('value'), (fm.get(t) or {}).get('xy'), (rfm.get(t) or {}).get('value'), (rfm.get(t) or {}).get('xy')))
    print(' exponent: this %r ref %r' % (lead.get('exponent'), (rff.get('actual_leading_density_power') or {}).get('exponent')))
    for N in ('1', '2', '3'):
        a = (ff.get('E') or {}).get(N) or {}; b = (rff.get('E') or {}).get(N) or {}; print(' E%s L2 this %r ref %r | unresolved fraction this %r ref %r' % (N, a.get('L2'), b.get('L2'), a.get('unresolved_fraction'), b.get('unresolved_fraction')))
