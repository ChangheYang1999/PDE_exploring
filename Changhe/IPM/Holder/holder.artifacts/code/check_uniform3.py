"""Independently recombine the third uniform pass with exact interval coverage."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
from check_uniform_comparison import A,upper,maximum,dec
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'09_uniform_comparison/pass3';OLD=ROOT/'09_uniform_comparison/lead_certificate/data';ctx.prec=256

def load(path):return json.loads(path.read_text())
def main():
 nodes=load(OLD/'nodes2.json');old=load(ROOT/'data/uniform_comparison_independent.json');prior={(r['group'],r['kind'],tuple(r['upper_segment'])):r for r in old['rows'] if r['mode']=='thm35'}
 inputs=[OLD/'nodes2.json',ROOT/'data/uniform_comparison_independent.json'];locals={};middle={};m=16;sec=1/(arb.pi()/(4*m)).cos()
 # Every certificate source is frozen and checked, independently of the lead combiner.
 for folder in ['local','mid']:
  for p in sorted((BASE/'data'/folder).glob('*.json')):
   d=load(p);inputs.append(p)
   for name,h in d['source_hashes'].items():
    src=BASE/'source'/name;assert hashlib.sha256(src.read_bytes()).hexdigest()==h,(p,name);inputs.append(src)
   if folder=='local':locals.setdefault(Q(d['alpha']),[]).append(d)
   else:
    assert d['angles_per_half']==d['radial_cells']==512 and d['phase_intervals']==m and d['integer_unit']==2**44
    middle[p.name]=d
 md=list(middle.values());assert md
 for d in md:
  for key in ['groups','source_hashes','plan_trials','precision_bits']:assert d[key]==md[0][key],key
 cov=[0]*512;mt={};expected={(Q(ref),Q(text)) for ref,texts in (g.split(':') for g in md[0]['groups'].split(';')) for text in texts.split(',')}
 for d in md:
  assert 0<=d['row_start']<d['row_stop']<=512
  for row in range(d['row_start'],d['row_stop']):cov[row]+=1
  assert len(d['rows'])==len(expected) and {(Q(r['plan_reference_alpha']),Q(r['alpha'])) for r in d['rows']}==expected
  for r in d['rows']:
   key=(Q(r['plan_reference_alpha']),Q(r['alpha']));v=[arb(s) for s in r['middle_phase_intervals']];assert len(v)==m+1
   mt[key]=v if key not in mt else [x+y for x,y in zip(mt[key],v)]
 assert cov==[1]*512
 lt={};small={}
 for x,ds in locals.items():
  cov=[[0]*(m+1) for _ in range(256)];tot=[arb(0)]*(m+1)
  for d in ds:
   assert d['angles_per_circle']==512 and d['radial_cells']==256 and d['phase_intervals']==m and Q(d['delta'])==Q(1,64)
   for key in ['source_hashes','integer_unit','precision_bits']:assert d[key]==ds[0][key]
   assert set(map(int,d['partial_phase_intervals']))==set(range(d['phase_start'],d['phase_stop']))
   for r in range(d['row_start'],d['row_stop']):
    for j in range(d['phase_start'],d['phase_stop']):cov[r][j]+=1
   for j,v in d['partial_phase_intervals'].items():tot[int(j)]+=arb(v)
  assert all(v==1 for row in cov for v in row)
  a=A(x);delta=A(Q(1,64));S=4*2**(a/2)*delta**a/(arb.pi()*a*(a+2))+(1+2*delta)**a*delta**2/(2*(1-delta)**2)
  for d in ds:assert S.overlaps(arb(d['small_disk_upper']))
  lt[x]=tot;small[x]=S
 rows=[];nodal=[]
 for gi,g in enumerate(nodes['groups']):
  bounds={};X=list(map(Q,g['nodes']));s,e=Q(g['start']),Q(g['end']);UI=[Q(x) for x in nodes['upper'] if s<=Q(x)<=e]
  assert UI[0]==s and UI[-1]==e
  ld=load(OLD/f'lower2_g{gi}.json');inputs.append(OLD/f'lower2_g{gi}.json');assert Q(ld['a'])==Q(g['shape']);lp={Q(r['alpha']):r for r in ld['rows']}
  logs={x:((arb(lp[x]['safe_decimal_lower_10_places'])/A(x)).log(),(arb(lp[x]['safe_decimal_upper_10_places'])/A(x)).log()) for x in X}
  if 2<=gi<=6:
   ref=Q(g['far_ref']);fd=load(OLD/f'far2_g{gi}.json');inputs.append(OLD/f'far2_g{gi}.json');assert Q(fd['plan_reference_alpha'])==ref and fd['phase_intervals']==m
   fp={Q(r['alpha']):r for r in fd['rows']}
   for x in UI:
    vals=[l+w+arb(f) for l,w,f in zip(lt[x],mt[(ref,x)],fp[x]['far_phase_intervals'])];assert len(vals)==m+1
    bounds[x]=upper(small[x]+sec*maximum(vals));nodal.append(dict(group=gi,alpha=str(x),upper_C=bounds[x].str(55,more=True)))
  for a,b in zip(UI,UI[1:]):
   oldrec=prior[(gi,'C',(str(a),str(b)))];oldlog=arb(oldrec['log_bound']);fresh=None;splits=[]
   if bounds:
    E0,E1=bounds[a].log(),bounds[b].log()
    def chord(t):return (A(b-t)*E0+A(t-a)*E1)/A(b-a)
    XX=[x for x in X if a<=x<=b];assert XX[0]==a and XX[-1]==b;vv=[]
    for x,y in zip(XX,XX[1:]):
     i=X.index(x);assert i>=1 and i+2<len(X);prev,nxt=X[i-1],X[i+2]
     sl=(logs[x][0]-logs[prev][1])/A(x-prev);sr=(logs[y][0]-logs[nxt][1])/A(nxt-y)
     denominator=sl+sr
     if denominator.contains(0):c=(x+y)/2
     else:
      v=(logs[y][0]+A(y)*sr-logs[x][0]+A(x)*sl)/denominator;c=Q(float(v.mid())).limit_denominator(10**12);c=min(y,max(x,c))
     assert x<=c<=y
     vv.extend([chord(x)-A(x).log()-logs[x][0],chord(c)-A(c).log()-logs[x][0]-A(c-x)*sl,chord(c)-A(c).log()-logs[y][0]-A(y-c)*sr,chord(y)-A(y).log()-logs[y][0]])
     splits.append([str(x),str(c),str(y)])
    fresh=maximum(vv)
   chosen=oldlog if fresh is None else upper(arb.min(oldlog,fresh))
   rows.append(dict(group=gi,upper_segment=[str(a),str(b)],old_log_upper=oldlog.str(55,more=True),new_log_upper=None if fresh is None else fresh.str(55,more=True),chosen_log_upper=chosen.str(55,more=True),safe_ratio=dec(chosen.exp()),splits=splits))
 mx=maximum([arb(r['chosen_log_upper']) for r in rows]);assert mx.exp()<arb('1.0625')
 summary=dict(C_log_upper=mx.str(55,more=True),C_ratio_upper=dec(mx.exp()),D_ratio_upper=old['summary']['thm35']['D']['ratio_upper'],whole_interval_C='1.0625',whole_interval_D='1.2894')
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,summary=summary,upper_segments=len(rows),nodal=nodal,rows=rows,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(inputs+[Path(__file__)]))},status='Recombination confirmed. Full new local and middle nodal replay is a separate prerequisite.')
 (BASE/'verification/independent_recombination.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
