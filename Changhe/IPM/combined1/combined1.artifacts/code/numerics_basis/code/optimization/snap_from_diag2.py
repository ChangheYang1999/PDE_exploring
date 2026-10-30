"""Write an immutable snapshot from (exact JSON, sectors JSON, diag2 JSON). argv: ID parent_id exact_json sectors_json diag2_json loss_label objective_desc 'description' 'notes'"""
import sys, json, os
sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/lib')
import ipm_exact as X, ipm_snapshot as SN
cid, parent, ex, sec, dg, loss_value, objective_desc, description, notes = sys.argv[1:10]
wt = sys.argv[10] if len(sys.argv) > 10 else None   # optional weak_tests JSON (theory_v02 NORM-T-WEAK-v1 distance)
LANE = 'RUN_ROOT/numerics_N1N2'
rep = json.load(open(sec)); cand = json.load(open(ex)); d = json.load(open(dg))
bs = SN.basis_summary(ex)
first = rep['first_nonzero']
parent_map = {'C1-BASE-S131': {'id': 'C1-BASE-S131', 'path': 'source/case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json', 'sha256': '7ff9415cbbe66f9d4a105aa4a999704e67157d8376c969b7561a1c01b1de57bc'},
              'C1-A2-d2': {'id': 'C1-A2-d2', 'path': 'source/analysis2/IPM_Analysis_II.artifacts/certificates/numerics_data/nb_d2_exact.json', 'sha256': 'f3339f85eff0ac81033a2a1f0fd07e12298ef9bd74da501a4e874c3cef6057e3'}}
bl2 = d.get('BL2', {})
wtd = json.load(open(wt)) if wt else None
weak_note = (' || first-mode weak probes (NORM-T-WEAK-v1 test functions, a = 0): largest FLOAT value over the 27 sampled k <= 4096 is %.4e at k = %s (a sampled maximum, not a bound; NC-T-DIST scalar budgets <= 3.793e-6, graded 4.572e-4); file %s' % (wtd['weak_distance_lower_bound_FLOAT'], wtd.get('k_of_max', '?'), os.path.basename(wt))) if wtd else ' || first-mode weak probes: not yet computed'
man = SN.write_snapshot(cid=cid, parent=parent_map.get(parent, parent), chart='PRIMARY', c_l_exact=cand['cl_exact'],
  theta0={'reference': 'state 131 exact Theta_0 (CONTRACTS section 2), preserved EXACTLY by the 10 leading-moment rows of branch 0', 'quarter_norm': rep['Theta0_quarter_norm']},
  a0={'value': d.get('a0_float'), 'status': 'FLOAT from exact coefficients (free parameter)'} if d.get('a0_float') is not None else {'value': cand['meta'].get('a0'), 'status': 'see sector/diag files'},
  b0n_status='EXACT (center row pivoted exactly; verified in rational arithmetic in finalize_exact)',
  basis_desc=dict(bs, description=objective_desc),
  coef_files=[(os.path.basename(ex), ex, 'c1-n1 generator list JSON (m, j, spec, coef exact rational string, coef_float); n_free/n_fixed', 'all coefficients exact rationals; pivot coefficients solved exactly (flint fmpq_mat), the others binary64 values')],
  evaluator_code=[LANE+'/numerics/lib/'+f for f in ('ipm_exact.py', 'ipm_eval.py', 'ipm_polar.py', 'ipm_origin.py', 'ipm_opt.py', 'ipm_opt2.py', 'ipm_farpart.py', 'ipm_hminus1.py', 'ipm_tail.py')]+[LANE+'/numerics/optimization/'+f for f in ('run_from_d2.py', 'run_e2.py', 'diag2.py', 'candA_setup.py')],
  sector_file=sec,
  loss={'value': float(loss_value), 'definition': objective_desc, 'label': 'LOSS'},
  notes=notes+weak_note+' || diag2 FLOAT summary (rule %s): G0 %.6g (far part F2 %.3g), G1 %.6g, P2 %.6g, rF %.6g, H %s, X3raw %.6g, sup|F| %.4g; first surviving sector exponent %s full-circle %.6g; (B-L2) theta_inner %.4g, kappa_inner %.4g, margin %.4g.' % (
      d['rule'], d['G0'], d['F2_far'] or 0, d['G1'], d['P2'], d['rF'], ('%.6g' % d['H']) if d.get('H') else 'n/a', d['X3_proxy_raw'], d['supF'], first['exponent'] if first else 'none', (first.get('full_L2', first.get('full_circle_L2', 0)) if first else 0), bl2.get('theta_inner_sup', float('nan')), bl2.get('kappa_inner', float('nan')), bl2.get('margin_c_plus_1_minus_theta_minus_kappa_minus_2', float('nan'))),
  description=description, extra_files=[dg]+([wt] if wt else []))
print('snapshot written', man['id'], man['created_utc'])
