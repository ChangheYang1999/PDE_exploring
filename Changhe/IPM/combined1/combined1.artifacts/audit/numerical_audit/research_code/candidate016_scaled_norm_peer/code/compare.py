"""Compare frozen completed norms and certify explicit conservative decimals."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys,time
from flint import arb,ctx,fmpq as Q
R=Path(__file__).resolve().parents[3];B=R/'research/candidate016_scaled_norm_peer'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def decimal(q):
 # Endpoint construction below uses a denominator dividing 10^30.
 q=Q(q);n=int(q.numerator*10**30//q.denominator);return f'{n//10**30}.{n%10**30:030d}'
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--own',required=True);parser.add_argument('--peer',default='source/N3_norms_partial_v01.json');parser.add_argument('--labels',default='G0');parser.add_argument('--output',required=True);args=parser.parse_args()
 ctx.prec=2048;start=time.monotonic();inputs={};checks={};labels=args.labels.split(',')
 def bind(p,h=None):
  p=Path(p);actual=sha(p);assert h is None or actual==h,(p,actual,h);inputs[str(p.relative_to(R))]=actual;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 audit=read(B/'verification/source_audit.json');assert audit['verdict'].startswith('CONFIRMED')
 for rel,h in audit['inputs'].items():bind(R/rel,h)
 own=read(B/args.own);peer=read(B/args.peer)
 for rel,h in own['inputs'].items():bind(R/rel,h)
 for name,h in peer['code_sha256'].items():bind(B/'source'/name,h)
 assert own['candidate']==peer['name']=='C1-N1-016-legqs25-quot013'
 assert own['raw_sha256']==peer['source_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
 assert own['cl_exact']==peer['cl']=='4076476460239181/2251799813685248' and own['delta_exact']==peer['delta']=='1824676646553933/4076476460239181'
 checks['same_raw_c_delta']=True
 assert own['precision_bits']==2048 and peer['precision_bits']==1024;checks['stated_precisions']=True
 assert own['no_spatial_quadrature'] and not own['peer_field_or_norm_routines_called'];checks['own_exact_route']=True
 assert own['fields']['D0_0']['component_count']==1360;checks['all1360_residual_components']=True
 pts=own['point_checks'];assert pts['value_count']==33 and len(pts['records'])==3 and pts['minimum_accuracy_bits']>120
 for row in pts['records']:
  assert len(row['values'])==11
  for k,z in row['values'].items():assert z['overlap'] and arb(z['own']).is_finite() and arb(z['Cartesian']).is_finite() and arb(z['own']).overlaps(arb(z['Cartesian']))
 checks['all33_cartesian_comparisons']=True
 reports={}
 expected={'G0':('0',0,[]),'rF':('-1',1,[]),'G1':('0',0,[]),'P2':('-4/5',0,[('3','4/5',56)])}
 for label in labels:
  a=own['norms'][label];b=peer['norms'][label];assert a['label']==b['label']==label and a['status'].startswith('COMPLETE') and b['status']=='FINITE'
  shift,tp,series=expected[label];assert b['a_shift']==shift and b['t_power']==tp and [(v['c'],v['alpha'],v['N']) for v in b['series']]==series
  gs=a['groups'];assert len(gs)==a['complete_group_count']>0 and len({g['ell_sum'] for g in gs})==len(gs)
  S=arb(0);T=arb(0);minimum=10**9
  for g in gs:
   assert Q(g['b'])>-1 and g['endpoint_v_order']>=0
   z=arb(g['integral_ball']);assert z.is_finite();S+=z;minimum=min(minimum,g['integral_accuracy_bits'])
   m=g['decomposition'];assert m['exact_reconstruction'] and Q(m['b'])==Q(g['b']) and all(Q(x)>0 and int(k)>0 for x,k in m['factors'])
   if label=='P2':
    z=arb(g['weighted_integral_ball']);assert z.is_finite();T+=z;minimum=min(minimum,g['weighted_integral_accuracy_bits']);assert g['weighted_decomposition']['exact_reconstruction']
  assert S.overlaps(arb(a['S_ball'])) and S>0
  if label=='P2':assert T.overlaps(arb(a['T_ball'])) and Q(a['series_absolute_error'])>0
  else:assert a['T_ball'] is None and a['series_absolute_error']=='0'
  lo=arb(a['norm_lower_ball']);hi=arb(a['norm_upper_ball']);pl=arb(b['norm_lower_ball']);pu=arb(b['norm_upper_ball'])
  assert all(z.is_finite() and z>0 for z in [lo,hi,pl,pu]) and minimum>120
  assert lo.overlaps(pl) and hi.overlaps(pu)
  # Printed peer endpoints are containing balls. Compare the exact lower/upper
  # endpoint enclosures separately, rather than requiring the P2 gap to vanish.
  assert pl.lower()<lo.lower() and lo.upper()<pl.upper()
  assert pu.lower()<hi.lower() and hi.upper()<pu.upper()
  lower=Q(int((lo.lower()*10**30).floor().unique_fmpz())-1,10**30)
  upper=Q(int((hi.upper()*10**30).ceil().unique_fmpz())+1,10**30)
  assert ar(lower)<lo.lower() and ar(upper)>hi.upper()
  # N3's wider displayed balls need not fit these finer accepted decimals.
  # They are checked for compatibility, not treated as new data for the proof.
  reports[label]={'accepted_lower_exact':str(lower),'accepted_upper_exact':str(upper),'accepted_lower_decimal':decimal(lower),'accepted_upper_decimal':decimal(upper),'own_lower_ball':a['norm_lower_ball'],'own_upper_ball':a['norm_upper_ball'],'peer_lower_ball':b['norm_lower_ball'],'peer_upper_ball':b['norm_upper_ball'],'own_groups':len(gs),'peer_groups':b['n_groups'],'minimum_integral_accuracy_bits':minimum,'ordered_pair_count':a['ordered_pair_count'],'peer_40digit_endpoint_balls_contain_own':True,'full1024bit_peer_endpoint_reproduction':'OPEN; own saved balls retain100 decimal digits','whole_plane_no_quadrature':True}
  checks['complete_'+label]=True
 for p in [B/'PROOF.md',Path(__file__)]:bind(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':own['candidate'],'raw_sha256':own['raw_sha256'],'inputs':inputs,'checks':checks,'norms':reports,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED explicit whole-plane decimal enclosures by independent exact production; no H, inverse or existence claim'}
 dest=B/args.output;assert not dest.exists()
 with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'CONFIRMED',labels,'SHA256',sha(dest),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
