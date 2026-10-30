"""Exact accepted-bound comparison; no new numerical source premise."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
import json,re,sys,time
R=Path(__file__).resolve().parents[3];B=R/'research/opposite_H_E2_order'
sys.set_int_max_str_digits(0)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();inputs={};checks={}
 def ck(k,v):assert k not in checks;checks[k]=bool(v);assert v,k
 def bind(p,h=None):
  p=Path(p);v=sha(p);assert h is None or v==h,(str(p),h,v);k=str(p.relative_to(R));assert k not in inputs or inputs[k]==v;inputs[k]=v;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 def ball(s):
  m=re.fullmatch(r'\[([0-9.eE+\-]+) \+/- ([0-9.eE+\-]+)\]',s);assert m,s
  a,r=Q(m[1]),Q(m[2]);assert r>0;return a-r,a+r
 rec=read(B/'verification/PROOF_FIRST.json');ck('proof_before_code',not rec['checker_exists']);bind(B/'PROOF.md',rec['proof_sha256']);bind(Path(__file__))
 par=read(B/'source/parameters.json',rec['parameters_sha256']);deps={}
 for rel,h in par['dependencies'].items():
  j=read(R/rel,h);ck('accepted:'+rel,all(j['checks'].values()));deps[Path(rel).parts[1]]=j
  for rr,hh in j['inputs'].items():bind(R/rr,hh)
 a=deps['negative_norm_forcing_assembly'];b=deps['candidate016_reviewed_upper']
 ck('candidate007',a['candidate']=='C1-N1-007-d2w-j7-e2bal');ck('candidate016',b['candidate']=='C1-N1-016-legqs25-quot013')
 ck('complete016_review',b['general_analytic_review_condition_discharged'] and b['full160_mode_field_covered'])
 h07lo,h07hi=ball(a['H_input_lower_ball']);h16=Q(b['H_strict_upper_exact']);ck('strict_H016_upper_square',Q(b['H_upper_square_exact'])<h16*h16)
 ck('positive_H_endpoints',0<h16<h07lo<h07hi)
 hg=h07lo-h16;ck('strict_H_gap',hg>Q(par['H_gap_floor'])>0)
 e16=Q(b['E2_strict_lower_exact']);e07=Q(a['E_upper']['strict_upper_exact']);e07lo,e07hi=ball(a['E_upper']['ball'])
 ck('strict_E2016_lower_square',0<e16*e16<Q(b['E2_lower_square_exact']))
 ck('strict_E2007_upper_ball',0<e07lo<e07hi<e07 and a['E_upper']['strict_bounds_verified'])
 eg=e16-e07;ck('strict_E2_gap',eg==Q(par['E2_gap_floor'])>0)
 for rr,hh in inputs.items():assert sha(R/rr)==hh
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'checks':checks,'check_count':len(checks),'H007_lower_endpoint_exact':str(h07lo),'H016_strict_upper_exact':str(h16),'H007_minus_H016_gap_lower_exact':str(hg),'H_gap_strict_display':par['H_gap_floor'],'E2016_strict_lower_exact':str(e16),'E2007_strict_upper_exact':str(e07),'E2016_minus_E2007_gap_strict_lower_exact':str(eg),'E2_gap_strict_display':par['E2_gap_floor'],'actual_H016_less_than_H007':True,'actual_E2007_less_than_E2016':True,'correction_distance_ordering_claimed':False,'peer_code_executed':False,'new_source_integrals':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED opposite strict actual H and E2 orderings, solely for the defined complete residual norms.'}
 p=B/'verification/result.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],len(checks),'checks',len(inputs),'bindings',sha(p),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
