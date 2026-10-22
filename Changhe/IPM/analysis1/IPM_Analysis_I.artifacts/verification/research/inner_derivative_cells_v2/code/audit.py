"""Independent saved-output geometry and exact reduction; no model regeneration."""
from protocol import *
import argparse
from mpmath import iv
iv.dps=220

def iq(v):
 v=F(v);return iv.mpf(v.numerator)/v.denominator

def endpoints(x):
 def dy(v):
  s,m,e,bc=v;assert bc>=0 and m>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
 return tuple(dy(v) for v in x._mpi_)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--tag',choices=['smoke','full'],required=True);args=ap.parse_args();started=now();p,deps=source();s=load(OUT/(args.tag+'_summary.json'));rehash(s['files']);cs=cells();indices=SMOKE if args.tag=='smoke' else list(range(44));assert s['indices']==indices and s['full_inner']==(args.tag=='full')
 path=OUT/(args.tag+'_rows.jsonl');assert s['rows_sha256']==sha(path) and s['source_freeze_sha256']==sha(OUT/'source_freeze.json');sums=[F(0),F(0)];count=0;geometric=0;components=0;input_count=0;jet_count=0;maxima=[(F(-1),None),(F(-1),None)]
 assert str(INNER_RESULT.relative_to(ROOT)) in p and p[str(INNER_RESULT.relative_to(ROOT))]==sha(INNER_RESULT)
 old=load(INNER_RESULT);assert F(old['ta_exact'])==F(-685794559684773,140737488355328);k=F(old['k_exact']);L=F(old['L_exact']);ta=F(old['ta_exact']);assert 0<k<1
 with path.open() as f:
  h=parse(next(f));assert h['indices']==indices and h['files']==s['files'] and h['source_freeze_sha256']==s['source_freeze_sha256']
  for line in f:
   r=parse(line);i=indices[count];check_record(r,i,cs);count+=1;input_count+=r['iv']['derivative_input_checks'];jet_count+=r['iv']['cross_method_input_jet_checks'];left,right=cs[i];t=ta+left
   factor=iv.pi*iq(right-left)*iq(L**6)*iv.exp(iq(-4*t))*iv.exp(iq(F(3,2)-k)*iv.log(1+iv.exp(iq(2*t))/iq(L**2)))
   for engine in ['arb','iv']:
    z=r[engine];B=[interval(v)[1] for v in z['B']];C=[interval(v)[1] for v in z['C']]
    for q in range(3):
     part=z['parts'][q];err=interval(part['error'])
     pol=interval(part['polynomial']) if engine=='arb' else (F(part['polynomial_upper_exact']),)*2
     angular=interval(part['theta_polynomial']) if engine=='arb' else (F(part['theta_polynomial_upper_exact']),)*2
     assert pol[0]>=0 and angular[0]>=0
     # Final upper endpoints must dominate the exact sum of component upper endpoints.
     assert B[q]>=pol[1]+err[1]
     if q<2:assert C[q]>=angular[1]+1043*err[1]
     components+=1
    vals=[iq(B[0])**2+iq(B[1])**2+iq(C[0])**2,(iq(B[0])+iq(B[1]))**2+(iq(B[1])+iq(B[2]))**2+(iq(C[0])+iq(C[1]))**2]
    for q,v in enumerate(vals):
     lo,hi=endpoints(factor*v);reported=interval(z['norm_squares'][q]);assert max(lo,reported[0])<=min(hi,reported[1]),('geometric integral disjoint',i,engine,q);geometric+=1
   for q in range(2):
    v=max(interval(r[e]['norm_squares'][q])[1] for e in ['arb','iv']);sums[q]+=v
    if v>maxima[q][0]:maxima[q]=(v,i)
 assert count==len(indices)==s['cells'] and [str(v) for v in sums]==s['cell_squares_upper_exact'];tails=tail_squares();total=[x+y for x,y in zip(sums,tails)]
 assert [str(v) for v in tails]==s['accepted_tail_squares_upper_exact'] and [str(v) for v in total]==s['combined_squares_upper_exact']
 for q,v in enumerate(total):
  c=F(s['norms']['strict_decimal_ceilings'][q]);assert c>0 and c*c>v
  lo,hi=endpoints(iv.sqrt(iq(v)))
  for e in ['arb512','iv200']:
   x=interval(s['norms'][e][q]);assert max(lo,x[0])<=min(hi,x[1]) and c>x[1]
 assert s['all_coefficient_overlap_checks']==count*17226 and s['all_derivative_input_checks']==input_count and s['all_cross_method_input_jet_checks']==jet_count==count*62688;rehash(s['files']);rehash(p)
 z={'start_utc':started,'utc':now(),'status':'PASS_COMPLETE_INNER_SAVED_OUTPUT_AUDIT','full_inner':s['full_inner'],'cells':count,'indices':indices,'summary_sha256':sha(OUT/(args.tag+'_summary.json')),'rows_sha256':sha(path),'geometric_integral_checks':geometric,'derivative_component_checks':components,'all_coefficient_overlap_checks':s['all_coefficient_overlap_checks'],'all_derivative_input_checks':input_count,'all_cross_method_input_jet_checks':jet_count,'exact_sum_and_strict_ceiling_checks':True,'maximum_contribution_cells':[i for v,i in maxima],'maximum_cell_squares_upper_exact':[str(v) for v,i in maxima],'required_replay_cells':SMOKE if args.tag=='smoke' else sorted(set(REPLAY+[i for v,i in maxima])),'scope':'Every saved row, exact coverage and reduction audited. Does not rerun every Taylor model; independence is supplied by both complete engines.'}
 write(OUT/(args.tag+'_audit.json'),z);print(json.dumps(z),flush=True)
if __name__=='__main__':main()
