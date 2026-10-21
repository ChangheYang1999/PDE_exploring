"""Algebraic audit of saved common-point physical actions; no solver imports."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'verification'

def load(relative):
    p = ROOT / relative
    data = p.read_bytes()
    obj = json.loads(data)
    if not obj.get('complete'):
        raise RuntimeError(f'{relative} is incomplete: '+str([(x['tag'], len(x['rows'])) for x in obj['states']]))
    assert all(len(s['rows']) == len(obj['points']) for s in obj['states'])
    return obj, hashlib.sha256(data).hexdigest()

def whiten(A, M):
    Q, T = np.linalg.qr(M, mode='reduced')
    sm = np.linalg.svd(M, compute_uv=False)
    assert sm[-1] > 1e-10 * sm[0], 'Insufficient metric rank for numerical whitening'
    # B=A T^{-1}; only linear solves, no explicit inverse in the action.
    B = np.linalg.solve(T.T, A.T).T
    return Q, T, B, sm

def analyse(obj, label):
    arrays = {}
    answer = []
    for s in obj['states']:
        rows = s['rows']; n = len(rows)
        rho = np.array([r['rho'] for r in rows])
        dr = np.array([r['delta_rho'] for r in rows])
        norm = np.array([r['N_report_f'] for r in rows])
        raw = np.array([r['delta_R'] for r in rows])
        assert np.all(norm > 0)
        act = raw / norm[:, None]
        assert np.max(abs(act-np.array([r['action_over_fixed_Nf'] for r in rows]))) < 1e-15
        M = np.vstack([dr / (1+abs(rho[:, None])) / np.sqrt(n), np.array(s['dcl'])])
        A = act / np.sqrt(n)
        estep = np.array([r['spatial_step_change_fixed_units'] for r in rows]) / np.sqrt(n)
        etail = np.array([r['tail_action_bound_using_numerical_gradients'] for r in rows]) / np.sqrt(n)
        worst = np.argmax(abs(act), axis=0)
        item = {'tag':s['tag'], 'state_md5':s['state_md5'], 'direction_sha256':s['direction_sha256'],
                'node_direction_labels':s['labels'], 'maximum_absolute_node_unit_actions':np.max(abs(act),axis=0).tolist(),
                'maximizing_point_indices':worst.tolist(), 'maximizing_points':[obj['points'][i] for i in worst],
                'base_max_abs_R_over_Nf':float(max(abs(np.array([r['base_R'] for r in rows])/norm))),
                'node_unit_max_spatial_step_discrepancy':float(estep.max()*np.sqrt(n)),
                'node_unit_max_tail_bound_using_numerical_gradients':float(etail.max()*np.sqrt(n)), 'spaces':{}}
        for d in (4,10,14):
            Q,T,B,sm=whiten(A[:,:d],M[:,:d])
            # Entrywise absolute inverse of the small triangular factor propagates
            # saved entrywise magnitude bounds. This only bounds the two saved
            # step-matrix difference and the stated tail expression, respectively.
            absinv = abs(np.linalg.solve(T,np.eye(d)))
            se = float(np.linalg.norm(estep[:,:d]@absinv))
            te = float(np.linalg.norm(etail[:,:d]@absinv))
            values = np.linalg.svd(B,compute_uv=False)
            item['spaces'][str(d)] = {
                'metric_singular_values_descending':sm.tolist(), 'metric_condition':float(sm[0]/sm[-1]),
                'physical_action_singular_values_ascending':values[::-1].tolist(),
                'metric_QR_relative_reconstruction':float(np.linalg.norm(M[:,:d]-Q@T)/np.linalg.norm(M[:,:d])),
                'metric_Q_orthogonality':float(np.linalg.norm(Q.T@Q-np.eye(d))),
                'whitening_relative_reconstruction':float(np.linalg.norm(B@T-A[:,:d])/np.linalg.norm(A[:,:d])),
                'whitened_step_matrix_discrepancy_Frobenius_upper':se,
                'whitened_tail_matrix_Frobenius_upper_using_numerical_gradients':te}
            arrays[(s['tag'],d)] = {'M':M[:,:d], 'A':A[:,:d], 'Q':Q,'T':T,'B':B,
                                    'estep':estep[:,:d], 'etail':etail[:,:d]}
        answer.append(item)
    flat={f'{tag}_{d}_{k}':v for (tag,d),x in arrays.items() for k,v in x.items()}
    np.savez_compressed(OUT/(label+'_matrices.npz'),**flat)
    return answer,arrays

base,sha = load('verification/actions.json')
answer, arrays = analyse(base,'baseline2048')
result = {'date':datetime.now(timezone.utc).isoformat(), 'points':base['points'],
          'number_points':len(base['points']), 'baseline_sha256':sha,'baseline_config':base['config'],
          'scope':'Finite sampled physical numerator actions. No continuum norm, spectrum, kernel dimension, family, isolation, rigorous quadrature enclosure or endpoint.',
          'states':answer, 'crossgrid_sampled_density_spaces':[]}
for d in (4,10,14):
    a=arrays[('n96m40S',d)]; b=arrays[('n120m48_S',d)]
    cs=np.linalg.svd(a['Q'].T@b['Q'],compute_uv=False)
    va=np.linalg.svd(a['B'],compute_uv=False)[::-1];vb=np.linalg.svd(b['B'],compute_uv=False)[::-1]
    result['crossgrid_sampled_density_spaces'].append({'d':d,'cosines_descending':cs.tolist(),
        'physical_singular_value_ratios96over120_ascending':(va/vb).tolist(),
        'qualification':'Common59-dimensional sampling protocol, with the distinct base-density denominators preserved. No convergence in a continuum function space inferred.'})
if '--refined' in sys.argv:
    fine,fsha=load('refinement4096/actions.json')
    assert fine['points']==base['points']
    fans,fa=analyse(fine,'refined4096')
    result.update({'refined_sha256':fsha,'refined_config':fine['config'],'refined_states':fans,'refinement_comparison':[]})
    for key,aa in arrays.items():
        ff=fa[key];assert np.array_equal(aa['M'],ff['M'])
        bs=np.linalg.svd(aa['B'],compute_uv=False);fs=np.linalg.svd(ff['B'],compute_uv=False)
        frob=float(np.linalg.norm(aa['B']-ff['B']));spec=float(np.linalg.norm(aa['B']-ff['B'],2))
        diff=float(max(abs(bs-fs)))
        assert diff <= spec*(1+1e-10)+1e-13
        result['refinement_comparison'].append({'tag':key[0],'d':key[1],
            'whitened_matrix_difference_Frobenius':frob,'whitened_matrix_difference_spectral_norm':spec,
            'maximum_singular_value_change':diff,'matrix_difference_over_fine_smallest_sv':frob/float(fs[-1]),
            'scope':'Difference between two finite computed matrices; not an upper bound on the remaining quadrature error.'})
name='summary_refined.json' if '--refined' in sys.argv else 'summary2048.json'
(OUT/name).write_text(json.dumps(result,indent=2)+'\n')
print(name)
for s in result.get('refined_states',answer):
    print(s['tag'],'max10',s['maximum_absolute_node_unit_actions'][:10])
    for d,x in s['spaces'].items():
        print('space',d,'metriccond',x['metric_condition'],'physicalsv',x['physical_action_singular_values_ascending'],
              'step',x['whitened_step_matrix_discrepancy_Frobenius_upper'],'tail',x['whitened_tail_matrix_Frobenius_upper_using_numerical_gradients'])
for r in result.get('refinement_comparison',[]):print('refinement',r)
for r in result['crossgrid_sampled_density_spaces']:print('overlap',r)
