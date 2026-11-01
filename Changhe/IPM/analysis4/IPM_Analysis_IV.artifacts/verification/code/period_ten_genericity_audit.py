"""Recheck the admitted algebraic inputs of period-ten genericity."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,time
from certificate_admission import read,ref,checkref
start=time.monotonic();base=Path('research/287_period_ten_genericity');checked=[]
paths=['research/257_period_seven_eight_genericity/verification/admission.json','research/281_period_ten_finite_algebra/verification/obstruction_admission.json','research/282_period_ten_symbolic_response/verification/admission.json']
for p in paths:
 d=read(p);assert d['verdict'] in ['PROVED','PROVED_FINITE_ALGEBRA']
 for k in ['proof','independent_review']:
  checkref(d[k]);checked.append(d[k])
 checked.append(ref(p))
finite=read(paths[1]);symbolic=read(paths[2]);assert finite['degree']==20 and finite['root_count']==14 and symbolic['degree_bound']==10 and symbolic['root_count']==14
checkref(finite['evidence']);checkref(symbolic['evidence']);obs=read(finite['evidence']['path']);response=read(symbolic['evidence']['path'])
assert obs['all_checks_pass'] and response['all_checks_pass'];co=list(map(int,obs['primitive_coefficients']));assert len(co)==21 and co[-1]>0 and co[0]!=0
possible=set(range(1,20))
for row in obs['modular_irreducibility']:
 assert sum(row['factor_degrees'])==20;options={0}
 for d in row['factor_degrees']:options|={x+d for x in list(options)}
 possible&=options
assert not possible
assert response['small_degrees']=={str(k):10 for k in range(2,21)} and len(response['limit_coefficients'])==11 and F(response['limit_coefficients'][-1])!=0
for name,row in response['factor_data'].items():
 for f in row['factors']:
  r=F(f['root']);assert not(r.denominator==1 and r>=21)
out=dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,Q=10,degree=20,response_degree=10,root_count=14,amplitude_response_exponent=10,amplitude_radius_exponent='5',checked_references=checked,finite_evidence=finite['evidence'],symbolic_evidence=symbolic['evidence'],proper_factor_degree_intersection=sorted(possible),scope='Algebraic dependency recheck for the standalone genericity proof, without recomputing the full symbolic derivative recurrence.',actual_elapsed_s=time.monotonic()-start)
(base/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');(base/'sources/period_ten_genericity_audit.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(out))
