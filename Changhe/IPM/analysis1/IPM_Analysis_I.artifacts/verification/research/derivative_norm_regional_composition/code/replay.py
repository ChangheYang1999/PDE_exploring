"""Exact integer endpoint and addition replay; no interval library imports."""
from common import *
import argparse,re

def qdecimal(s):
 assert type(s) is str and re.fullmatch(r'[0-9]+(?:\.[0-9]+)?',s)
 if '.' not in s:return F(int(s))
 a,b=s.split('.');return F(int(a+b),10**len(b))

def ceiling_record(z,v):
 q=qdecimal(z['decimal']);assert q==F(z['exact'])
 if v==0:assert q==0 and z['strict'] is False
 else:
  unit=F(z['unit_exact']);assert unit>0 and q-unit<=v<q and z['strict'] is True
 return q

def inspect(x,z):
 # Reconstruct the regional scalars directly from the FINAL parent output fields.
 ds={label:ROOT/rec['path'] for label,rec in x['parents'].items()};folder=ds['179'].parent
 s=load(folder/'full_summary.json');t=load(folder/'full_tails.json')
 expected={r:[] for r in REGIONS}
 for j in range(2):
  expected['middle'].append(max(F(s['engines'][e]['middle_bound_sums_exact'][j]) for e in ['arb512','iv200']))
  for region in ['inner','outer']:
   vals=[]
   for e in ['arb512','iv200']:
    m,k=t['bounds'][e][region+'_norm_squares'][j]['hi'];vals.append(F(int(m),1<<(-k)) if k<0 else F(int(m)*(1<<k)))
   expected[region].append(max(vals))
 for label,region in [('180','outer'),('181','inner')]:
  if label not in ds:continue
  s=load(ds[label].parent/'full_summary.json');expected[region]=[F(s['cell_squares_upper_exact'][j])+F(s['accepted_tail_squares_upper_exact'][j]) for j in range(2)]
 for r in REGIONS:assert expected[r]==two(x['region_sq_upper_exact'][r])
 counts={'regional_ceilings':0,'exact_sum_checks':0,'integer_root_enclosures':0,'root_ceilings':0}
 display={}
 for r in REGIONS:
  display[r]=[]
  for j in range(2):display[r].append(ceiling_record(z['regional_squared_ceilings'][r][j],expected[r][j]));counts['regional_ceilings']+=1
 for field,values in [('exact_parent_reductions',expected),('displayed_region_reductions',display)]:
  for j in range(2):
   r=z[field][j];terms=[values[region][j] for region in REGIONS];total=F(0)
   for v in reversed(terms):total=F(total.numerator*v.denominator+v.numerator*total.denominator,total.denominator*v.denominator)
   assert list(map(F,r['summands_exact']))==terms and F(r['sum_exact'])==total;counts['exact_sum_checks']+=1
   uppers=[]
   for e in ENGINES:
    lo,hi=pair(r['engines'][e]['sum']);assert lo<=total<=hi
    lo,hi=pair(r['engines'][e]['root']);assert lo*lo<=total<=hi*hi;uppers.append(hi);counts['integer_root_enclosures']+=1
   q=ceiling_record(r['whole_plane_norm_ceiling'],max(uppers));assert q*q>total if total else q==0;counts['root_ceilings']+=1
 assert z['published_whole_plane_norm_ceilings']==[r['whole_plane_norm_ceiling']['decimal'] for r in z['displayed_region_reductions']]
 assert z['sharper_exact_parent_norm_ceilings']==[r['whole_plane_norm_ceiling']['decimal'] for r in z['exact_parent_reductions']]
 assert counts=={'regional_ceilings':6,'exact_sum_checks':4,'integer_root_enclosures':8,'root_ceilings':4}
 return counts

def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=MODES);args=ap.parse_args();p=E/args.mode;sp=source();x=load(p/'inputs.json');z=load(p/'checks.json')
 assert x['mode']==z['mode']==args.mode and z['inputs_sha256']==sha(p/'inputs.json') and z['source_freeze_sha256']==sha(E/'source_freeze.json')
 assert when(z['utc'])<datetime.now(timezone.utc);rehash(x['files']);counts=inspect(x,z);rehash(sp);rehash(x['files'])
 out={'utc':now(),'status':'PASS_INTEGER_REGIONAL_EXTRACTION_SUMS_ROOT_ENDPOINTS_AND_DECIMAL_REPLAY','mode':args.mode,'inputs_sha256':sha(p/'inputs.json'),'checks_sha256':sha(p/'checks.json'),'counts':counts,'source_sha256':sha(Path(__file__))};write(p/'replay.json',out);print(json.dumps(out))
if __name__=='__main__':main()
