"""Accept independent complete leaf evidence and replay its finite reduction."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction as Q
from math import comb
from flint import arb,ctx
import json,time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate017_complete_cover_peer'
ctx.prec=2048
ar=lambda x:arb(Q(x).numerator)/Q(x).denominator
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()

def rectangle(path):
 a,b,u,v=map(Q,[0,1,-1,1])
 for ch in path:
  if ch=='t':b=(a+b)/2
  elif ch=='T':a=(a+b)/2
  elif ch=='z':v=(u+v)/2
  elif ch=='Z':u=(u+v)/2
  else:raise AssertionError(ch)
 return a,b,u,v

def theta(ranges,u,v):
 lo,hi=map(arb,ranges['rx']);y0,y1=map(arb,ranges['ry'])
 assert all(q.is_finite() for q in [lo,hi,y0,y1])
 assert lo<=hi and y0<=y1
 x=abs(lo).max(abs(hi));z=Q(0) if u<=0<=v else min(abs(u),abs(v))
 s=(1-ar(z*z)).sqrt()
 return ((y0*y0+(x*s)**2).sqrt()-y0)/2

def bernstein(poly,n,a,b):
 local=[sum((poly[k]*comb(k,l)*a**(k-l)*(b-a)**l for k in range(l,n+1)),Q(0)) for l in range(n+1)]
 return [sum((local[k]*Q(comb(i,k),comb(n,k)) for k in range(i+1)),Q(0)) for i in range(n+1)]

def main():
 tick=time.monotonic();inputs={};checks={};out=B/'verification/result.json';assert not out.exists()
 def bind(p,expected=None):
  p=Path(p);rel=str(p.relative_to(R));h=inputs.get(rel)
  if h is None:h=sha(p);inputs[rel]=h
  assert expected is None or h==expected,(rel,h,expected)
  return json.loads(p.read_text()) if p.suffix=='.json' else None
 bind(B/'PROOF.md');bind(Path(__file__))
 frozen=bind(B/'source/MANIFEST.json');assert frozen['proof_sha256']==sha(B/'PROOF.md')
 for rel,row in frozen['sources'].items():bind(R/rel,row['sha256'])
 S=B/'source';manifest=bind(S/'data/manifest.json');p=bind(S/'data/parameters.json')
 peer=bind(S/'verification/result.json','373804eea41dd375f29edcaac94a5b4107fbf8f52641db0c4398dbdef95bdcb8')
 assert sha(S/'PROOF.md')==manifest['proof_sha256']
 assert sha(S/'data/parameters.json')==manifest['parameters_sha256']
 for name,h in manifest['sources'].items():bind(S/'source'/name,h)
 bind(R/frozen['polynomial_dependency'],frozen['polynomial_sha256'])
 expected_bindings={'manifest':sha(S/'data/manifest.json'),'checker':sha(S/'code/check.py'),'polynomials':frozen['polynomial_sha256']}
 checks['peer_source_graph']=peer['bindings']==expected_bindings
 deps=[('research/candidate017_background_margin/verification/result.json',None),
       ('research/rational_bernstein_peer/verification/result.json','085d9a4daa6cca2bfe387329498297bf61eb5c597b7a994671ad46ed2944bcf1'),
       ('research/scaled_reconstruction_peer/verification/result.json','960c230fc07d7daffe819fe7984967cd13fd005330add75173452be6fdcf3598'),
       ('research/scaled_hessian_peer/verification/result.json','0de14e144d06ad09cbf02fbc02844b467771aa0ad4ff2d821bd6bc9ce6131dfd')]
 for rel,h in deps:
  dep=bind(R/rel,h);assert all(dep['checks'].values())
  for key in ['inputs','own_inputs','reconstruction_inputs']:
   for q,v in dep.get(key,{}).items():bind(R/q,v)
  for key in ['retained_or_frozen','frozen_or_retained_sources']:
   for q,v in dep.get(key,{}).items():bind(R/q,v['stored_sha256'])
 checks['accepted_source_graphs']=True
 cover=bind(S/'source/N4_complete_cover.json');assert cover['all_pass'] and not cover['pending']
 accepted_recon=bind(S/'source/T4_378_result.json');hessian=bind(S/'source/T4_366_017.json')
 checks['raw_and_representation']=peer['raw_sha256']==cover['raw_sha256']==accepted_recon['raw_sha256']==hessian['raw_sha256']==p['raw_sha256']=='7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114' and accepted_recon['all_exact_coefficients_equal'] and accepted_recon['peer_polynomial_sha256']==frozen['polynomial_sha256']
 paths=set(peer['leaf_sha256']);checks['same_complete_paths']=paths=={q['path'] for q in cover['accepted']} and len(paths)==len(cover['accepted'])==247
 children={}
 for path in paths:
  for k,ch in enumerate(path):children.setdefault(path[:k],set()).add(ch)
 checks['full_binary_partition']=not paths.intersection(children) and '' in children and len(children)==246 and all(q in [{'t','T'},{'z','Z'}] for q in children.values())
 rects={q:rectangle(q) for q in paths};area=sum(((b-a)*(v-u) for a,b,u,v in rects.values()),Q(0));pairs=0
 for i,(a,b,u,v) in enumerate(rects.values()):
  assert 0<=a<b<=1 and -1<=u<v<=1
  for aa,bb,uu,vv in list(rects.values())[:i]:
   assert max(a,aa)>=min(b,bb) or max(u,uu)>=min(v,vv);pairs+=1
 checks['exact_partition_area']=area==2;checks['disjoint_pairs']=pairs==30381
 fixtures=0
 for n in [3,7]:
  poly=[Q((-1)**k*(k+1),k+2) for k in range(n+1)]
  for angular in [False,True]:
   a,b=(Q(-1),Q(1)) if angular else (Q(0),Q(1));base=bernstein(poly,n,a,b)
   transformed=[]
   for i in range(n+1):
    value=Q(0)
    for k in range(n+1):
     weight=sum((Q(comb(k,l)*comb(i,l)*(-1)**(k-l)*2**l,comb(n,l)) for l in range(min(i,k)+1)),Q(0)) if angular else Q(comb(i,k),comb(n,k)) if k<=i else Q(0)
     value+=poly[k]*weight
    transformed.append(value)
   assert transformed==base
   for right in [False,True]:
    got=[sum(((Q(comb(n-i,j-i),2**(n-i)) if j>=i else Q(0)) if right else (Q(comb(i,j),2**i) if j<=i else Q(0)))*base[j] for j in range(n+1)) for i in range(n+1)]
    lo,hi=((a+b)/2,b) if right else (a,(a+b)/2)
    assert got==bernstein(poly,n,lo,hi);fixtures+=1
 checks['eight_exact_transform_fixtures']=fixtures==8
 tau=ar(p['tau']);rows=[];edge=0;improved=0;worst=arb(0)
 for path in sorted(paths):
  row=bind(S/'verification/leaves'/(path+'.json'),peer['leaf_sha256'][path]);a,b,u,v=rects[path]
  assert row['path']==path and list(map(Q,row['rectangle']))==list(rects[path])
  assert row['bindings']==expected_bindings and row['precision_bits']==2048 and row['pass']
  den=arb(row['positive_denominator_lower']);assert den>0
  assert den.overlaps(ar((1+2499*(1-b))**19))
  plain=theta(row['plain_ranges'],u,v);stored_plain=arb(row['plain_theta_upper'])
  assert plain.is_finite() and plain.overlaps(stored_plain),(path,'plain',plain,stored_plain)
  choices=[plain];stored_choices=[stored_plain]
  if b==1:
   assert row['correlated_ranges'] is None and row['correlated_theta_upper'] is None;edge+=1
  else:
   assert row['correlated_ranges'] is not None
   corr=theta(row['correlated_ranges'],u,v);stored_corr=arb(row['correlated_theta_upper'])
   assert corr.is_finite() and corr.overlaps(stored_corr),(path,'correlated',corr,stored_corr)
   choices.append(corr);stored_choices.append(stored_corr);improved+=1
  bound=choices[0];selected=stored_choices[0]
  for q in choices[1:]:bound=bound.min(q)
  for q in stored_choices[1:]:selected=selected.min(q)
  recorded=arb(row['theta_upper']);assert recorded.overlaps(selected) and bound.overlaps(recorded)
  assert recorded<tau and bound<tau,(path,'tau',bound,recorded)
  upper=arb(bound.upper());worst=worst.max(upper)
  rows.append({'path':path,'theta_reassembled':bound.str(90),'theta_outward_upper':upper.str(90),'strict_slack':(tau-upper).str(80),'correlated_checked':b<1})
 checks['all_247_saved_ranges_and_theta']=len(rows)==247;checks['positive_denominators']=True
 checks['peer_scope']=peer['all_leaves_pass'] and peer['leaf_count']==247 and peer['coefficient_count']==40082 and peer['fixture_count']==8 and peer['independent_global_transform_and_subdivision'] and not peer['foreign_code_executed']
 c=Q(p['c']);cap=Q(p['kappa_upper']);rate=c+1-Q(p['tau'])-cap;floor=Q(p['rate_floor'])
 checks['exact_constants']=c==Q(4076476460239181,2251799813685248) and Q(p['tau'])==Q(2,25) and cap==Q(729080538628955349,10**18) and floor==Q(200123867,10**8)
 checks['strict_kappa']=hessian['whole_plane'] and arb(hessian['values']['kappa'])<ar(cap)
 checks['strict_rate']=rate>floor>2 and arb(peer['signed_rate_lower']).contains(ar(rate))
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 result={'utc':datetime.now(timezone.utc).isoformat(),'candidate':peer['candidate'],'raw_sha256':p['raw_sha256'],'checks':checks,'check_count':len(checks),'inputs':inputs,'peer_result_sha256':sha(S/'verification/result.json'),'leaf_count':247,'internal_nodes':246,'exact_area':str(area),'disjoint_pairs_checked':pairs,'fixtures':fixtures,'edge_leaves':edge,'correlated_leaves':improved,'maximum_reassembled_theta_upper':worst.str(100),'theta_upper_exact':p['tau'],'strict_kappa_upper_exact':str(cap),'strict_rate_lower_exact':str(rate),'strict_rate_decimal_lower_exact':str(floor),'leaf_reductions':rows,'precision_bits':ctx.prec,'peer_production_elapsed_seconds':peer['elapsed_seconds'],'own_foreign_code_executed':False,'full_polynomial_range_production_repeated_here':False,'verdict':'CONFIRMED complete independent017 background cover through T4-400, N4-310, N4-311 and N4-303; no inverse or existence conclusion','elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print('PASS',len(checks),'checks',len(inputs),'bindings','247 leaves','theta',worst.str(25),'rate>',str(floor),'sha',sha(out),'utc',result['utc'],'seconds',result['elapsed_seconds'])
if __name__=='__main__':main()
