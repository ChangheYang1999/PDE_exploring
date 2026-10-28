"""Independent interval recombination of all exponent intervals.
No float comparison selects the certified maximum. Float calculations only
choose a rational split point, for which the proof permits any value.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'09_uniform_comparison/lead_certificate';DATA=BASE/'data';ctx.prec=256

def A(q):
 q=Q(q);return arb(q.numerator)/q.denominator

def upper(x):return arb(x.upper())
def maximum(values):
 result=values[0]
 for value in values[1:]:result=arb.max(result,value)
 return upper(result)
def dec(x,n=10):
 k=int((upper(x)*10**n).ceil().unique_fmpz());return f'{k//10**n}.{k%10**n:0{n}d}'
def read(name):return json.loads((DATA/name).read_text())

def main():
 nodes=read('nodes2.json');XU=list(map(Q,nodes['upper']));assert XU==sorted(set(XU))
 assert Q(nodes['groups'][0]['start'])==Q(1,200) and Q(nodes['groups'][-1]['end'])==Q(199,200)
 assert all(Q(g['end'])==Q(h['start']) for g,h in zip(nodes['groups'],nodes['groups'][1:]))
 inputs=['nodes2.json','upper_n384.json','upper_n384_b.json'];ups={};m=16
 for name in inputs[1:]:
  d=read(name);assert d['phase_intervals']==m and d['cells_per_axis']==384
  assert d['source_sha256']==hashlib.sha256((BASE/'source/refl_nodes.py').read_bytes()).hexdigest()
  for r in d['rows']:
   x=Q(r['alpha'])
   if x in ups:assert all(arb(a).overlaps(arb(b)) for a,b in zip(ups[x]['regular_grid'],r['regular_grid']))
   ups[x]=r
 sec=1/(arb.pi()/(4*m)).cos();allrows=[];winners={}
 for mode in ['thm35','thm34']:
  whole={'C':[],'D':[]};segments=0;subsegments=0
  for gi,g in enumerate(nodes['groups']):
   ln=f'lower2_g{gi}.json';fn=f'far2_g{gi}.json';inputs.extend([ln,fn]);ld=read(ln);fd=read(fn)
   assert Q(ld['a'])==Q(g['shape']) and Q(fd['plan_reference_alpha'])==Q(g['far_ref'])
   assert fd['phase_intervals']==m and fd['angles']==512 and fd['radial_cells']==128
   assert fd['source_sha256']==hashlib.sha256((BASE/'source/far_nodes.py').read_bytes()).hexdigest()
   X=list(map(Q,g['nodes']));assert X==sorted(set(X));lp={Q(r['alpha']):r for r in ld['rows']};fp={Q(r['alpha']):r for r in fd['rows']}
   assert set(X)<=set(lp);logs={}
   for x in X:
    l=arb(lp[x]['safe_decimal_lower_10_places']);u=arb(lp[x]['safe_decimal_upper_10_places']);assert 0<l<u
    logs[x]=((l/A(x)).log(),(u/A(x)).log())
   s,e=Q(g['start']),Q(g['end']);UI=[x for x in XU if s<=x<=e];assert UI[0]==s and UI[-1]==e
   bounds={'C':{},'D':{}}
   for x in UI:
    r=ups[x];a=A(x)
    if mode=='thm35':
     f=fp[x];assert len(r['regular_grid'])==len(f['far_phase_intervals'])==m+1
     regular=maximum([arb(y)+arb(z) for y,z in zip(r['regular_grid'],f['far_phase_intervals'])])*sec
     nearC=4*2**(-a/2)/(arb.pi()*a*(a+2))
     nearD=2**(1-a)*((a+2)/2).gamma()/(2*arb.pi().sqrt()*((a+3)/2).gamma()*a)+arb(1)/2
     assert nearC.overlaps(arb(r['near']))
     bounds['C'][x]=upper(nearC+regular);bounds['D'][x]=upper(nearD+regular)
    else:
     bounds['C'][x]=arb(r['safe_upper_C']);bounds['D'][x]=arb(r['safe_upper_D'])
   for a,b in zip(UI,UI[1:]):
    segments+=1;XX=[x for x in X if a<=x<=b];assert XX[0]==a and XX[-1]==b
    for kind in ['C','D']:
     E0=bounds[kind][a].log();E1=bounds[kind][b].log()
     def chord(t):return (A(b-t)*E0+A(t-a)*E1)/A(b-a)
     values=[];split_records=[]
     for x1,x2 in zip(XX,XX[1:]):
      subsegments+=1;i=X.index(x1);assert i>=1 and i+2<len(X);x0=X[i-1];x3=X[i+2]
      a1=(logs[x1][0]-logs[x0][1])/A(x1-x0);a2=(logs[x2][0]-logs[x3][1])/A(x3-x2)
      def line1(t):return logs[x1][0]+A(t-x1)*a1
      def line2(t):return logs[x2][0]+A(x2-t)*a2
      denom=a1+a2
      if denom.contains(0):c=(x1+x2)/2
      else:
       proposal=(logs[x2][0]+A(x2)*a2-logs[x1][0]+A(x1)*a1)/denom
       c=Q(float(proposal.mid())).limit_denominator(10**12);c=min(x2,max(x1,c))
      assert x1<=c<=x2
      v=[chord(x1)-A(x1).log()-line1(x1),chord(c)-A(c).log()-line1(c),chord(c)-A(c).log()-line2(c),chord(x2)-A(x2).log()-line2(x2)]
      values.extend(v);split_records.append([str(x1),str(c),str(x2)])
     mx=maximum(values);whole[kind].append(mx)
     allrows.append(dict(mode=mode,group=gi,kind=kind,upper_segment=[str(a),str(b)],log_bound=mx.str(45,more=True),ratio_upper=dec(mx.exp()),splits=split_records))
  result={kind:dict(log_bound=maximum(whole[kind]).str(45,more=True),ratio_upper=dec(maximum(whole[kind]).exp())) for kind in ['C','D']}
  result.update(upper_segments=segments,subsegments_counting_C_and_D=subsegments);winners[mode]=result
  print(mode,result,flush=True)
 small=A(Q(1,200));L=(arb(2).sqrt()-1)**small*(4/(arb.pi()*small*(small+2))-arb(1)/4);assert L>arb('126.199')
 Hdelta=(2-small)*(3-small)*arb(3).sqrt()/(8*arb.pi());assert Hdelta>arb('0.411775')
 smallD=arb('1.0172482934')+arb('0.5')/arb('126.199');largeD=arb('1.0262309397')+arb('0.5')/arb('82.355')
 assert smallD<arb('1.0213') and largeD<arb('1.0324')
 assert arb(winners['thm35']['C']['ratio_upper'])<arb('1.0830') and arb(winners['thm35']['D']['ratio_upper'])<arb('1.2899')
 hashes={str((DATA/n).relative_to(ROOT)):hashlib.sha256((DATA/n).read_bytes()).hexdigest() for n in sorted(set(inputs))}
 for p in sorted((BASE/'source').iterdir()):hashes[str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
 hashes['code/check_uniform_comparison.py']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,summary=winners,endpoint_checks=dict(L005=L.str(45,more=True),lower_deltaH=Hdelta.str(45,more=True),small_D_ratio=dec(smallD),large_D_ratio=dec(largeD)),rows=allrows,source_hashes=hashes,status='Independent recombination with exact interval coverage and outward maxima. Nodal certificate code audit is a separate prerequisite.')
 (ROOT/'data/uniform_comparison_independent.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
