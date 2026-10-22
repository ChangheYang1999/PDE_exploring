"""Independent exact output arithmetic and failure contracts for primary assembly."""
import importlib.util
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone

BASE=Path(__file__).resolve().parents[3]
D=BASE/'research/global_residual_assembly'
p=D/'code/assemble_primary.py'
spec=importlib.util.spec_from_file_location('primary_assembly_contract_subject',p)
subject=importlib.util.module_from_spec(spec);spec.loader.exec_module(subject)
r=json.loads((D/'evidence/primary_assembly.json').read_text())
checks=[]

def record(name, condition):
    if not condition:raise ValueError(name)
    checks.append(name)

def rejection(name, action):
    try:action()
    except ValueError:checks.append(name);return
    raise ValueError('missing rejection '+name)

squares={name:F(region['squared_norm_exact']) for name,region in r['regions'].items()}
E=squares['inner']+squares['middle']+squares['outer']
record('all_positive_regional_squares',all(x>0 for x in squares.values()))
root=r['global_N2'];record('exact_squared_norm_sum',E==F(root['input_squared_exact']))
for engine in ['arb512','iv160']:
    a,b=map(F,root[engine]);record(engine+'_exact_enclosure',0<=a<=b and a*a<=E<=b*b)
ceiling=F(root['strict_upper_decimal'])
record('integer_ceiling_identical_decimal',ceiling==F(root['strict_upper_exact']))
record('integer_ceiling_strict_square',F(root['integer_lower_exact'])**2<=E<ceiling**2)
record('squared_norm_sum_not_regional_max',E>max(squares.values()))
for key,entry in r['global_suprema'].items():
    regional={n:F(v) for n,v in entry['regional_upper_exact'].items()}
    upper=F(entry['authoritative_upper_exact'])
    record(key+'_regional_max',upper==max(regional.values())==regional[entry['largest_upper_bound_region']])
    record(key+'_decimal_ceiling',upper<F(entry['strict_upper_decimal'])==F(entry['strict_upper_exact']))
record('origin_and_infinite_tail_present',r['regions']['inner']['full_tail'] is True and r['regions']['outer']['full_tail'] is True)
record('primary_only_scope',r['regions']['middle']['evidence_level']=='PRIMARY_ONLY' and 'PRIMARY' in r['status'])
record('whole_region_counts',[r['regions'][n]['cells'] for n in ['inner','middle','outer']]==[54,7809,89])
for f,expected in r['files'].items():
    with (BASE/f).open('rb') as stream:actual=hashlib.file_digest(stream,'sha256').hexdigest()
    record('pin_'+f,actual==expected)
# Exact square values, non-squares, and values immediately around decimal boundaries.
fixtures=[F(0),F(1),F(2),F(1,10**100),F(10**100),F(9,16),F(1,3)]
for n in [1,2,17,291624061,1903991978]:
    center=F(n,10**12)**2
    fixtures.extend([center-F(1,10**60),center,center+F(1,10**60)])
for i,value in enumerate(fixtures):
    x=subject.sqrt_three_methods(value)
    a,b=F(x['integer_lower_exact']),F(x['strict_upper_exact'])
    record('sqrt_boundary_'+str(i),0<=a<=b and a*a<=value<b*b)
for value in [F(0),F(1,10**12),F(1,3),F(10**50)]:
    x=subject.ceiling(value);record('strict_rational_ceiling_'+str(value),F(x['strict_upper_exact'])>value)
rejection('negative_squared_norm',lambda:subject.sqrt_three_methods(F(-1)))
rejection('negative_ceiling',lambda:subject.ceiling(F(-1)))
for name,text in [('duplicate','{"a":1,"a":2}'),('NaN','{"a":NaN}'),('Infinity','{"a":Infinity}'),('negativeInfinity','{"a":-Infinity}')]:
    rejection(name,lambda text=text:subject.loads(text))
for name,intervals,a,b in [('empty',[],F(0),F(1)),('gap',[(F(0),F(1,3)),(F(1,2),F(1))],F(0),F(1)),('overlap',[(F(0),F(2,3)),(F(1,2),F(1))],F(0),F(1)),('reverse',[(F(1),F(0))],F(1),F(0)),('truncated',[(F(0),F(1,2))],F(0),F(1))]:
    rejection('partition_'+name,lambda intervals=intervals,a=a,b=b:subject.contiguous(intervals,a,b))
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_ARITHMETIC_AND_FAILURE_CONTRACTS','checks':len(checks),'check_names':checks,'source_sha256':hashlib.file_digest(Path(__file__).open('rb'),'sha256').hexdigest(),'assembly_source_sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest(),'assembly_sha256':hashlib.file_digest((D/'evidence/primary_assembly.json').open('rb'),'sha256').hexdigest(),'scope':'Independent exact saved-output arithmetic plus synthetic failure contracts. No regenerated regional coefficients or full independent middle result.'}
(D/'evidence/assembly_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['utc','status','checks']}))
