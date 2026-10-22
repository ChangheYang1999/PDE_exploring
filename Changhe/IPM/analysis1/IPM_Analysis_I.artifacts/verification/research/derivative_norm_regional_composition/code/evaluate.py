"""Independent library paths for each exact and displayed regional sum."""
from common import *
import argparse
from flint import arb,ctx
from mpmath import iv

def aa(q):q=F(q);return arb(q.numerator)/q.denominator

def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator

def ae(x):
 assert x.is_finite()
 def one(v):m,e=v.man_exp();return F(int(m))*F(2)**int(e)
 return tuple(map(one,[x.lower(),x.upper()]))

def ie(x):
 def one(v):
  s,m,e,bc=v;assert s in [0,1] and m>=0 and bc==int(m).bit_length()
  return (-1 if s else 1)*F(int(m))*F(2)**int(e)
 return tuple(map(one,x._mpi_))

def record(p):a,b=p;assert 0<=a<=b;return {'lower_exact':str(a),'upper_exact':str(b)}

def dec(q):
 q=F(q);assert q>=0
 n,d=q.numerator,q.denominator;u=v=0
 while d%2==0:d//=2;u+=1
 while d%5==0:d//=5;v+=1
 assert d==1
 scale=max(u,v);n*=2**(scale-u)*5**(scale-v)
 if scale==0:return str(n)
 t=str(n).zfill(scale+1);return t[:-scale]+'.'+t[-scale:]

def ceiling(q):
 q=F(q);assert q>=0
 if q==0:return {'decimal':'0','exact':'0','unit_exact':'1','strict':False}
 exponent=0
 while q<F(10)**exponent:exponent-=1
 while q>=F(10)**(exponent+1):exponent+=1
 unit=F(10)**(exponent-23);r=(q//unit+1)*unit;s=dec(r)
 assert F(s)==r and r-unit<=q<r
 return {'decimal':s,'exact':str(r),'unit_exact':str(unit),'strict':True}

def reduction(values):
 assert len(values)==3 and all(F(x)>=0 for x in values)
 vals=list(map(F,values));exact=sum(vals,F(0));ctx.prec=512;ctx.threads=1;iv.dps=220
 av=aa(vals[0])+aa(vals[1])+aa(vals[2]);bv=iq(vals[2])+iq(vals[1])+iq(vals[0])
 ar=av.sqrt();br=iv.mpf(0) if exact==0 else iv.exp(iv.log(bv)/2)
 records={'arb512':{'sum':record(ae(av)),'root':record(ae(ar))},'iv220':{'sum':record(ie(bv)),'root':record(ie(br))}}
 for v in records.values():
  lo,hi=pair(v['sum']);assert lo<=exact<=hi
  lo,hi=pair(v['root']);assert lo*lo<=exact<=hi*hi
 assert max(pair(v['root'])[0] for v in records.values())<=min(pair(v['root'])[1] for v in records.values())
 hi=max(pair(v['root'])[1] for v in records.values());c=ceiling(hi);q=F(c['exact']);assert q*q>exact if exact else q==0
 return {'summands_exact':list(map(str,vals)),'sum_exact':str(exact),'engines':records,'whole_plane_norm_ceiling':c}

def compute(x):
 rows={r:two(x['region_sq_upper_exact'][r]) for r in REGIONS};decimal={r:[ceiling(v) for v in rows[r]] for r in REGIONS}
 out={'regional_squared_ceilings':decimal,'exact_parent_reductions':[],'displayed_region_reductions':[]}
 for j in range(2):
  out['exact_parent_reductions'].append(reduction([rows[r][j] for r in REGIONS]))
  out['displayed_region_reductions'].append(reduction([F(decimal[r][j]['exact']) for r in REGIONS]))
 out['published_whole_plane_norm_ceilings']=[v['whole_plane_norm_ceiling']['decimal'] for v in out['displayed_region_reductions']]
 out['sharper_exact_parent_norm_ceilings']=[v['whole_plane_norm_ceiling']['decimal'] for v in out['exact_parent_reductions']]
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=MODES);args=ap.parse_args();p=E/args.mode
 pins=source();freeze=load(p/'input_freeze.json');x=load(p/'inputs.json')
 assert x['mode']==args.mode and freeze['inputs_sha256']==sha(p/'inputs.json') and freeze['source_freeze_sha256']==x['source_freeze_sha256']==sha(E/'source_freeze.json')
 assert when(x['utc'])<when(freeze['utc'])<datetime.now(timezone.utc);rehash(x['files'])
 z={'start_utc':now(),'status':'COMPUTED_REGIONAL_SCALAR_COMPOSITION_REQUIRES_REPLAY_AND_ACTUAL_REVIEW','mode':args.mode,'inputs_sha256':sha(p/'inputs.json'),'source_freeze_sha256':sha(E/'source_freeze.json'),**compute(x)}
 rehash(pins);rehash(x['files']);z['utc']=now();write(p/'checks.json',z)
 print(json.dumps({'utc':z['utc'],'mode':args.mode,'regional_squared_ceilings':z['regional_squared_ceilings'],'published_whole_plane_norm_ceilings':z['published_whole_plane_norm_ceilings']}))
if __name__=='__main__':main()
