"""Compare full lead polar responses with the independent Cartesian identity."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,importlib.util,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import fmpq,fmpq_poly
from generic_response_identity import Rat
ROOT=Path('research/284_full_polar_response_comparison')
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def poly(c):return fmpq_poly([fmpq(x) for x in c])
def main(Q):
 start=time.monotonic();base=Path('research')/({9:'277_period_nine_symbolic_response',10:'282_period_ten_symbolic_response'}[Q]);lowbase=Path('research')/({9:'267_period_nine_tuning',10:'281_period_ten_finite_algebra'}[Q]);target=ROOT/'verification'/f'Q{Q}';target.mkdir(exist_ok=True)
 check=read(base/'verification/checks.json');assert check['all_checks_pass']
 lowpath=lowbase/'verification/prefix_polynomials.json.gz';low=read(lowpath)
 genpath=base/'verification/reduced_generic.json.gz';gen=read(genpath);cols=list(map(poly,gen['numerator_by_b_degree']));D=poly(gen['denominator']);assert len(cols)==Q+1
 source=Path('../a4-lead/code/tuned/tq_sym.py');frozen=ROOT/'sources'/f'lead_tq_sym_Q{Q}.py';frozen.write_bytes(source.read_bytes())
 spec=importlib.util.spec_from_file_location(f'lead_polar_Q{Q}',frozen);T=importlib.util.module_from_spec(spec);argv=sys.argv;sys.argv=['tq_sym.py',str(Q),'3']
 try:spec.loader.exec_module(T)
 finally:sys.argv=argv
 T.Fk=Rat;T.R=Rat;T.K=Rat(fmpq_poly([0,1]));T.one=Rat.one
 fixed={kind:{int(n):{int(m):poly(c) for m,c in row['sine_polynomials'].items()} for n,row in low['fields'][kind].items() if int(n)<=(Q if kind=='f' else Q-1)} for kind in ['f','g']}
 values=[0,1,-1,2,-2,3,-3,4,-4,5,-5][:Q+1];rows=[]
 for value in values:
  begin=time.monotonic();T.B=Rat(value)
  ff={n:{m:Rat(p(value)) for m,p in row.items() if p(value)} for n,row in fixed['f'].items()};gg={n:{m:Rat(p(value)) for m,p in row.items() if p(value)} for n,row in fixed['g'].items()}
  pf,pg=T.low_orders(Q);prefix_checks=0
  for expected,actual in [(ff,pf),(gg,pg)]:
   for n,field in expected.items():
    cleaned={m:v for m,v in actual[n].items() if v}
    assert set(field)==set(cleaned),('prefix_support',Q,value,n)
    for m,v in field.items():assert v==cleaned[m],('prefix_coefficient',Q,value,n,m);prefix_checks+=1
  result,_=T.sigma(None,ff,gg);expected=Rat(sum((c*value**i for i,c in enumerate(cols)),fmpq_poly([])),D);assert result==expected,('full_identity',Q,value)
  row=dict(b=value,exact_full_identity=True,low_prefix_coefficients=prefix_checks,numerator_degree=result.n.degree(),denominator_degree=result.d.degree(),actual_elapsed_s=time.monotonic()-begin);rows.append(row)
  (target/'partial.json').write_text(json.dumps(dict(rows=rows),indent=2)+'\n');print(json.dumps(dict(at=now(),Q=Q,**row)),flush=True)
 out=dict(checked_at_utc=now(),all_checks_pass=True,Q=Q,degree_bound=Q,distinct_b_values=values,rows=rows,exact_low_prefix_comparisons=sum(x['low_prefix_coefficients'] for x in rows),inputs=[ref(lowpath),ref(genpath),ref(base/'verification/checks.json')],lead_source=ref(source),frozen_lead_source=ref(frozen),arithmetic='Shared audited Q(k) engine; distinct Cartesian and polar derivative implementations.',actual_elapsed_s=time.monotonic()-start)
 (target/'checks.json').write_text(json.dumps(out,indent=2)+'\n');(ROOT/'sources/full_polar_response_comparison.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(dict(at=now(),Q=Q,complete=True,elapsed_s=out['actual_elapsed_s'])),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--Q',type=int,choices=[9,10],required=True);a=p.parse_args()
 try:main(a.Q)
 except Exception as exc:
  target=ROOT/'verification'/f'Q{a.Q}';target.mkdir(exist_ok=True);d=dict(at=now(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)]);(target/'FAILURE.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d),flush=True);raise SystemExit(1)
