"""Independent saved-result and provenance audit for the corner moment note."""
import json,hashlib,os,sys
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
assert not sys.flags.optimize
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/corner_moments/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ce12(q):q=F(q)*10**12;return F(-((-q.numerator)//q.denominator),10**12)
def interval(obj):
 lo,hi=F(obj['lower_exact']),F(obj['upper_exact']);assert 0<lo<=hi;return lo,hi

def main():
 source=BASE/'research/corner_moments/code/check_moments.py';proof=BASE/'research/corner_moments/PROOF.md';ep=E/'checks.json';e=json.loads(ep.read_text())
 assert e['status']=='PASS_EXACT_ALGEBRA_AND_TWO_INTERVAL_CONSTANTS' and sha(source)==e['source_sha256'] and sha(proof)==e['proof_sha256']
 assert e['parameters_exact']=={'a':'129/20','b':'307/100','A':'238/25','gamma':'1129/1000'}
 assert e['moment_coefficients_checked']==20 and e['norm_interval_overlaps']==40 and e['angular_interval_overlaps']==4
 assert e['J_zero'] and F(e['K_alpha00_d3_exact'])==-1 and F(e['K_c_alpha20_exact'])==F(-4,3) and F(e['unbounded_growth_power_exact'])==F(38,25)
 assert [r['degree'] for r in e['results']]==[1,3,5,7];overlaps=0;rows=[]
 for r in e['results']:
  k=r['degree'];assert r['angular_frequency']==k+2 and r['radial_beta_arguments_exact']==[str(2*(F(238,25)-k-1)),str(2*(k+1-F(1129,1000)))]
  al,au=interval(r['J_arb']);il,iu=interval(r['J_iv']);assert max(al,il)<=min(au,iu)
  assert len(r['coefficients'])==k+1
  for l,c in enumerate(r['coefficients']):
   assert (c['i'],c['l'],c['j'])==(1 if l%2 else 2,l,k-l)
   for name in ['composite','unit_square_upper']:
    x0,x1=interval(c[name+'_arb']);y0,y1=interval(c[name+'_iv']);assert max(x0,y0)<=min(x1,y1);overlaps+=1
  c=r['coefficients'][0];assert c['binomial']==1
  row={'degree':k,'J_upper_exact':str(ce12(max(au,iu)))}
  for name in ['composite','unit_square_upper']:
   bound=max(F(c[name+'_arb']['upper_exact']),F(c[name+'_iv']['upper_exact']));public=ce12(bound);assert public>bound;row[name+'_d_k_upper_exact']=str(public)
  rows.append(row)
 assert overlaps==40
 for r in e['coupling_identities']:
  expected={'(6, 3)':'-7'} if r['velocity_degree']==7 else {};assert r['rectangle_remainder']==expected
 paths={Path(__file__),source,proof,ep};reviews={}
 for tag in ['corner_moments_review','corner_moments_closure']:
  mp=BASE/f'notes/reviews/{tag}_metadata.json';m=json.loads(mp.read_text());request=(BASE/f'notes/reviews/{tag}_request.txt').read_text()
  assert m['actual_response_model']=='claude-opus-5-5' and m['stop_reason']=='end_turn' and hashlib.sha256(request.encode()).hexdigest()==m['input_sha256']
  if tag.endswith('closure'):
   for p in [source,proof,ep]:
    marker='\n\nFILE '+str(p.relative_to(BASE))+'\n';assert request.split(marker,1)[1].split('\n\nFILE ',1)[0]==p.read_text()
  reviews[tag]={'actual_model':m['actual_response_model'],'end_utc':m['end_utc']}
  for suffix in ['request.txt','response.json','response.md','metadata.json']:paths.add(BASE/f'notes/reviews/{tag}_{suffix}')
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','claims':['canonical coefficient kernel and sign','pure product-weight moment functional unbounded for every A','bounded support moment criterion A>k+1','exact composite-weight dual norm iff A>k+1 and gamma<k+1','J=0 and K=-alpha00*d3-(4/3)c*alpha20 as degree5 asymptotic coefficients','global pure-weight-to-local coupling obstruction, growth R^(38/25) at working parameters'],'methods':'Own complex-kernel derivation and Hilbert-dual norm proof; exact sparse bivariate algebra; Arb512 Chebyshev angular square and iv180 direct binomial angular square. Both numerical methods share the proved beta/gamma integration identities. Final audit uses exact rational endpoint decoding and independent upward public rounding.','public_rows':rows,'reviews':reviews,'files':{str(p.relative_to(BASE)):sha(p) for p in sorted(paths)},'scope':'No D1 double-block estimate, T2 annular trace, full variable-C8-alpha coupling, global inverse, fixed point, existence, exclusion or decisive endpoint.'}
 tmp=E/'verdict.json.tmp';tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,E/'verdict.json')
 for rel,h in result['files'].items():assert sha(BASE/rel)==h
 print(json.dumps({'utc':result['utc'],'status':result['status'],'pins':len(paths),'public_rows':rows,'sha256':sha(E/'verdict.json')}))
if __name__=='__main__':main()
