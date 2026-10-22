"""Supplemental FLINT sums and pure-integer strict root rounding."""
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq as Q
from datetime import datetime,timezone
import argparse,json,hashlib,math
R=Path(__file__).resolve().parents[3];a=argparse.ArgumentParser();a.add_argument('mode',choices=['exterior','both']);o=a.parse_args();E=R/'research/derivative_norm_regional_composition/evidence'/o.mode
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
x=json.loads((E/'inputs.json').read_text());c=json.loads((E/'checks.json').read_text());assert c['inputs_sha256']==sha(E/'inputs.json') and c['mode']==o.mode
rows=[]
for region in ['outer','middle','inner']:
 for j,v in enumerate(c['regional_squared_ceilings'][region]):
  actual=Q(x['region_sq_upper_exact'][region][j]);printed=Q(str(F(v['decimal'])));unit=Q(v['unit_exact'])
  assert printed==Q(v['exact']) and 0<printed-actual<=unit
for key in ['exact_parent_reductions','displayed_region_reductions']:
 for j,v in enumerate(c[key]):
  summands=[Q(s) for s in v['summands_exact']];total=sum(reversed(summands),Q(0));assert total==Q(v['sum_exact'])
  expected=[Q(x['region_sq_upper_exact'][r][j]) if key=='exact_parent_reductions' else Q(str(F(c['regional_squared_ceilings'][r][j]['decimal']))) for r in ['inner','middle','outer']]
  assert summands==expected
  d=v['whole_plane_norm_ceiling'];q=Q(str(F(d['decimal'])));unit=Q(d['unit_exact']);assert q==Q(d['exact']) and q*q>total
  scaled=F(str(total/(unit*unit)));n=math.isqrt(scaled.numerator//scaled.denominator);assert n*n<=scaled<(n+1)**2;assert Q(n+1)*unit==q
  for z in v['engines'].values():
   sl,su=Q(z['sum']['lower_exact']),Q(z['sum']['upper_exact']);lo,hi=Q(z['root']['lower_exact']),Q(z['root']['upper_exact'])
   assert sl<=total<=su and 0<=lo<=hi<q and lo*lo<=total<=hi*hi
  rows.append({'field':key,'norm_index':j,'sum_exact':str(total),'decimal':d['decimal'],'unit_exact':str(unit),'positive_square_margin_exact':str(q*q-total)})
for j in range(2):
 inc=sum((Q(str(F(c['regional_squared_ceilings'][r][j]['decimal'])))-Q(x['region_sq_upper_exact'][r][j]) for r in ['inner','middle','outer']),Q(0))
 units=sum((Q(c['regional_squared_ceilings'][r][j]['unit_exact']) for r in ['inner','middle','outer']),Q(0));assert 0<inc<=units
 assert c['published_whole_plane_norm_ceilings'][j]==c['displayed_region_reductions'][j]['whole_plane_norm_ceiling']['decimal']
pins={str(p.relative_to(R)):sha(p) for p in [E/'inputs.json',E/'checks.json',Path(__file__).resolve()]}
z={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_FMPQ_REVERSED_SUMS_INTEGER_ROOTS_AND_DIRECTED_REGIONAL_ROUNDING','mode':o.mode,'rows':rows,'files':pins,'scope':'Independent scalar arithmetic of accepted regional parent upper bounds; no new physical enclosure or endpoint.'}
p=E/'own_integer_root_checks.json';assert not p.exists();p.write_text(json.dumps(z,indent=2)+'\n');print(z['utc'],z['status'])
