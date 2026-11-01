"""Artifact-specific hypotheses for the separately proved tuned interval induction."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction
import ast, json, pickle, sys, time
sys.dont_write_bytecode=True
from flint import arb, fmpq, ctx
from stream_precision_audit import unpack
from integer_period_prefix import inputs
from pure_cartesian_ball import refine_root
ROOT=Path('research/194_tuned_producer_enclosure')

def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def main():
    start=time.monotonic();ctx.prec=1536;source_rows=[]
    reviewed={
        'ffcore.py':{'RingArb':['scalar','poly','coeffs','is_zero'],'FarField':['__init__','p','products','step','save'],'':['polymul','_arb_pack']},
        'tuned_cQ.py':{'TunedQ':['__init__','poisson','T','add','responses','run_tuned']},
        'tuned_general.py':{'TunedGeneral':['__init__','jres','poisson','T','add','responses','run_tuned']}}
    for name in ['ffcore.py','tuned_cQ.py','tuned_general.py','tuned_c3.py']:
        path=Path('../a4-num/code')/name;raw=path.read_bytes();(ROOT/'sources'/name).write_bytes(raw)
        entry=dict(path=str(path),sha256=sha256(raw).hexdigest(),bytes=len(raw),reviewed_functions=[])
        tree=ast.parse(raw)
        for node in tree.body:
            if isinstance(node,ast.ClassDef) and node.name in reviewed.get(name,{}):
                for method in node.body:
                    if isinstance(method,(ast.FunctionDef,ast.AsyncFunctionDef)) and method.name in reviewed[name][node.name]:
                        entry['reviewed_functions'].append(dict(name=node.name+'.'+method.name,first_line=method.lineno,last_line=method.end_lineno))
            elif isinstance(node,ast.FunctionDef) and node.name in reviewed.get(name,{}).get('',[]):
                entry['reviewed_functions'].append(dict(name=node.name,first_line=node.lineno,last_line=node.end_lineno))
        source_rows.append(entry)
    rows=[]
    for period,roots in [(5,list(range(1,7))),(6,list(range(1,7)))]:
        coefficients,intervals,_,paths=inputs(period)
        topic='180_period_five_numerical_audit' if period==5 else '185_period_six_numerical_audit'
        for ri in roots:
            tag=f'tunedQ5_r{ri}_p1024' if period==5 else f'tuned13_r{ri}_p1024'
            source=Path('../a4-num/ckpt')/(tag+'.pkl');raw=source.read_bytes();digest=sha256(raw).hexdigest();state=pickle.loads(raw);del raw
            previous=json.loads((Path('research')/topic/'verification'/f'root{ri}_checks.json').read_text())
            assert digest==previous['source']['sha256']
            d=arb(*unpack(state['delta_pack']));c=arb(*unpack(state['c_l_pack']))
            assert d.contains(fmpq(2,period)) and c.contains(fmpq(period,period-2)) and c>1
            assert state['ring']=='arb' and state['prec']==1024 and state['stopped'] is None
            assert Fraction(state['delta_exact'])==Fraction(2,period) and max(state['f'])==300
            b,isolator=refine_root(coefficients,intervals[ri-1],1536)
            f1=[arb(*unpack(v)) for v in state['f'][1]]
            assert len(f1)==2 and f1[0]==1 and f1[1].contains(b)
            denominator_checks=0;resonances=[];density_divisors=0
            for n in range(1,301):
                p=1-n*d;P=p+1
                if n>=2:
                    lam=(n-1)*(c-1);assert lam>0;density_divisors+=1
                for j in range(1,len(state['g'][n])):
                    den=2*(4*j*j-P*P)
                    exact_resonance=n*2==period*2*(j+1)
                    assert den.contains(0)==exact_resonance,(period,ri,n,j)
                    denominator_checks+=1
                    if exact_resonance:resonances.append(n)
            assert resonances==list(range(2*period,301,period))
            row=dict(period=period,root_index=ri,source=dict(path=str(source),sha256=digest),parameter_containment=True,initial_root_containment=True,root_interval=isolator,source_hash_matches_independent_prefix=True,nonresonant_denominators_exclude_zero=True,poisson_denominator_checks=denominator_checks,density_divisors_positive=density_divisors,resonant_orders=resonances,final_stream_harmonic_status='order300 untuned; full stream norm excluded')
            rows.append(row);print(json.dumps(dict(period=period,root_index=ri,denominator_checks=denominator_checks,all_checks_pass=True)),flush=True)
            del state
    result=dict(checked_at_utc=stamp(),all_checks_pass=True,review_type='Manual source review of the listed recurrence operations, with automated artifact hypothesis checks; no formal verification of interpreter or interval library.',no_midpoint_replacement_in_reviewed_coefficient_update_paths=True,source_files=source_rows,rows=rows,actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'sources/tuned_producer_enclosure_audit.py').write_bytes(Path(__file__).read_bytes())
    print(json.dumps(dict(all_checks_pass=True,branches=len(rows),actual_elapsed_s=time.monotonic()-start)),flush=True)

if __name__=='__main__':main()
