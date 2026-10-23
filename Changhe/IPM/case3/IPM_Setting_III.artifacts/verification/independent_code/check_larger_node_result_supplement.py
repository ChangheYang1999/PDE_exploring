"""Finite descriptive supplement. Existing accepted records remain immutable."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
import sys, json, math, hashlib, traceback
if sys.flags.optimize:
    raise SystemExit('optimized Python prohibited')
import numpy as np
R = Path('research/hydrostatic_larger_node_audit')
V = R / 'verification'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

def medians(values):
    finite = sorted(F(float(z)) for z in values if math.isfinite(float(z)))
    if not finite:
        return dict(defined=0, undefined=len(values), lower=None, upper=None, mean=None)
    lo, hi = finite[(len(finite)-1)//2], finite[len(finite)//2]
    return dict(defined=len(finite), undefined=len(values)-len(finite),
                lower=str(lo), upper=str(hi), mean=str((lo+hi)/2))

def fits(value, interval):
    return None if value is None else F(interval['lower']) <= F(value) <= F(interval['upper'])

def main():
    manufacture = sys.argv[1:] == ['--manufactures']
    if sys.argv[1:] and not manufacture:
        raise ValueError('only --manufactures permitted')
    target = V / ('RESULT_SUPPLEMENT_MANUFACTURES.json' if manufacture else 'RESULT_SUPPLEMENT.json')
    if target.exists():
        raise ValueError('preserve existing result before rerunning')
    checks, bindings, outputs = [], {}, {}
    def ck(name, condition, evidence=None):
        checks.append(dict(name=name, passed=bool(condition), evidence=evidence))
        if not condition:
            raise AssertionError((name, evidence))
    def bind(path, expected=None):
        p = str(path); h = sha(p)
        ck('binding '+p, (expected is None or h == expected) and (p not in bindings or bindings[p] == h))
        bindings[p] = h
        return Path(p)
    def gate(name, status):
        d = json.loads(bind(V/name).read_text())
        ck('complete '+name, d['status'] == status and d['count'] == len(d['checks']) and all(z['passed'] for z in d['checks']))
        for p, h in d.get('bindings', {}).items():
            bind(p, h)
        return d
    started = datetime.now(timezone.utc).isoformat()
    try:
        bind(__file__); bind(R/'FINAL_RESULTS_REVIEW_RESOLUTION_PROOF.md')
        if manufacture:
            cases = [([3.,1.], dict(defined=2,undefined=0,lower='1',upper='3',mean='2')),
                     ([3.,1.,2.], dict(defined=3,undefined=0,lower='2',upper='2',mean='2')),
                     ([], dict(defined=0,undefined=0,lower=None,upper=None,mean=None)),
                     ([float('nan')], dict(defined=0,undefined=1,lower=None,upper=None,mean=None)),
                     ([2.,2.,float('nan')], dict(defined=2,undefined=1,lower='2',upper='2',mean='2')),
                     ([1.,math.nextafter(1.,2.)], dict(defined=2,undefined=0,lower='1',upper='4503599627370497/4503599627370496',mean='9007199254740993/9007199254740992'))]
            for k, (values, expected) in enumerate(cases):
                ck('median case '+str(k), medians(values) == expected)
            interval = dict(lower='3/2', upper='5/2')
            ck('closed lower endpoint', fits('3/2', interval) is True)
            ck('closed upper endpoint', fits('5/2', interval) is True)
            ck('outside interval', fits('3', interval) is False)
            ck('undefined preserved', fits(None, interval) is None)
            ck('nonmonotone allowed descriptive', (F(2)-F(3) > 0) is False)
            status = 'PASS_MEDIAN_AND_SCOPE_MANUFACTURES'
        else:
            gate('RESULT_SUPPLEMENT_MANUFACTURES.json', 'PASS_MEDIAN_AND_SCOPE_MANUFACTURES')
            a = gate('FINAL_ARITHMETIC_CHECKS.json', 'PASS_FINITE_LARGER_NODE_ARITHMETIC_REQUIRES_FINAL_REVIEW')
            p = gate('PRINTED_COMPARISON_CHECKS.json', 'PASS_FINITE_PRINTED_COMPARISONS')
            ck('actual outputs only', a['synthetic_only'] is False and p['synthetic_only'] is False)
            center = gate('CENTER_REUSE_CHECKS.json', 'PASS_EXACT_CENTER_REUSE')
            ck('center statement delegated explicitly', center['scope'].startswith('Exact center data'))
            source = bind(V/'producer_hs_node_check_current_20261022_0728.py')
            median_lines = [line for line in source.read_text().splitlines() if 'np.median((np.abs(Rh) / Nf)[msk])' in line]
            ck('current producer NumPy median call as text', len(median_lines) == 1)
            false_flags, states = [], []
            ck('state order', [s['N'] for s in a['outputs']['states']] == [s['N'] for s in p['outputs']['states']] == [224,192])
            for st, printed in zip(a['outputs']['states'], p['outputs']['states']):
                n = st['N']; path = bind(V/'candidate'/('N'+str(n)+'_B.npz'))
                with np.load(path, allow_pickle=False) as z:
                    xy = z['xy']; rr = z['residual']
                radius = np.hypot(xy[:,0], xy[:,1]); rows = []
                for region, (low, high), prs in zip(st['regional_summaries'], [(0.,.1),(.1,1.),(1.,100.),(100.,float('inf'))], printed['rows']):
                    mask = (radius >= low) & (radius < high)
                    m = medians(rr[mask,3]); ck('regional count '+str((n,low)), int(mask.sum()) == region['count'])
                    pm = prs['metrics']['medianRf']
                    ck('exact central mean unchanged '+str((n,low)), m['mean'] == pm['B_exact'])
                    ck('undefined median count '+str((n,low)), m['defined'] == prs['median_defined_count'] and m['undefined'] == prs['median_undefined_count'])
                    for key, metric in prs['metrics'].items():
                        flag = metric['B_in_printed_rounding_interval']
                        ck('interval recomputation '+str((n,low,key)), flag is fits(metric['B_exact'], metric['producer_printed']))
                        if flag is False:
                            false_flags.append(dict(N=n,region=region['region'],metric=key,**metric))
                    interval = pm['producer_printed']
                    rows.append(dict(region=region['region'],count=region['count'],median=m,
                                     printed=interval, lower_in_printed=fits(m['lower'],interval),
                                     upper_in_printed=fits(m['upper'],interval), mean_in_printed=fits(m['mean'],interval)))
                z = st['regional_summaries'][3]['metrics']['absR']
                states.append(dict(N=n,points=len(radius),radius_min=float(radius.min()),radius_max=float(radius.max()),
                                   far_absR_maximizing_radius=math.hypot(z['x'],z['y']),medians=rows))
            old,new = a['outputs']['states'][1],a['outputs']['states'][0]; changes=[]
            for ro,rn in zip(old['regional_summaries'],new['regional_summaries']):
                for metric in ['Rf','Rv']:
                    left=F(ro['metrics'][metric]['value']);right=F(rn['metrics'][metric]['value'])
                    changes.append(dict(region=ro['region'],metric=metric,N192=str(left),N224=str(right),
                                        difference=str(right-left),increased=right>left))
            outputs=dict(states=states,all_false_interval_flags=false_flags,false_interval_count=len(false_flags),
                         all_inside_printed_intervals=not false_flags,normalized_cross_resolution=changes,
                         producer_current_source_median_lines=median_lines,
                         center_evidence_scope=a['outputs']['center_evidence_scope'],
                         scope='Finite descriptive summary. Current source text does not authenticate historical execution. Median matching does not identify a cause. No true-integral or convergence claim.')
            status = 'PASS_DESCRIPTIVE_MEDIAN_AND_SCOPE_SUPPLEMENT'
        for path,h in list(bindings.items()):
            ck('stable '+path, sha(path)==h)
    except Exception:
        status='FAIL';outputs['error']=traceback.format_exc();print(outputs['error'],flush=True)
    result=dict(status=status,synthetic_only=manufacture,started_utc=started,
                finished_utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,outputs=outputs)
    tmp=target.with_suffix('.tmp');tmp.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');tmp.replace(target)
    print(status,len(checks),outputs.get('false_interval_count'))
    if status=='FAIL':raise SystemExit(1)
if __name__=='__main__':main()
