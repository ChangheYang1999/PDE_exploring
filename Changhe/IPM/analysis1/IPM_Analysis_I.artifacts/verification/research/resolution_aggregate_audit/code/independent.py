from pathlib import Path
from fractions import Fraction as F
import json,sys,hashlib
from datetime import datetime,timezone
from flint import fmpq
from mpmath import iv
sys.dont_write_bytecode=True;iv.dps=80
R=Path(__file__).resolve().parents[3];D=R/'research/resolution_aggregate_audit';E=D/'evidence';N=R.parent/'ipmA-num'
def now():return datetime.now(timezone.utc).isoformat()
def sha(path):
 with Path(path).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def read(path):return json.loads(Path(path).read_text(),parse_float=str)
def checkpins(pins):
 for n,h in pins.items():assert sha(R/n)==h,n
start=now();A=json.loads((E/'check.json').read_text());manifest=json.loads((E/'input_manifest.json').read_text());checkpins(manifest['files']);assert sha(D/'PROOF.md')==A['proof_sha256']=='c6bf17a382f3edf0fec419c9f858b96c2fcb5f18f93ae92b7a15c3b5dc0cf3fc'
cache={}
def dec(token):
 token=str(token).lower();sg=-1 if token.startswith('-') else 1;token=token.lstrip('+-');mant,sep,ex=token.partition('e');ex=int(ex) if sep else 0
 whole,dot,frac=mant.partition('.');return fmpq(sg*int(whole+frac))*fmpq(10)**(ex-len(frac))
def binary(token):
 # Round decimal rational to IEEE binary64 by integer arithmetic, ties to even.
 token=str(token)
 if token in cache:return cache[token]
 r=dec(token)
 if r==0:return fmpq(0)
 sign=-1 if r<0 else 1;r=abs(r);a,b=int(r.p),int(r.q);e=a.bit_length()-b.bit_length()
 if r<fmpq(2)**e:e-=1
 assert fmpq(2)**e<=r<fmpq(2)**(e+1) and -1022<=e<=1023
 unit=fmpq(2)**(e-52);scaled=r/unit;n,rem=divmod(int(scaled.p),int(scaled.q));den=int(scaled.q)
 if 2*rem>den or 2*rem==den and n%2:n+=1
 out=sign*fmpq(n)*unit;cache[token]=out;return out
def rat(s):return fmpq(s)
def Q(x):return iv.mpf(int(x.p))/int(x.q)
def endpoint(t):sg,n,e,bc=t;return fmpq((-1 if sg else 1)*int(n))*fmpq(2)**int(e)
def bounds(z):return tuple(map(endpoint,z._mpi_))
def get(tag,stem):return read(N/'runs'/(stem+('_'+tag if tag else '')+'.json'))
tags=['','v3_h0.004','v4_M230','v5_R0knot2'];summary={v['tag']:v for v in read(D/'source/variants_summary.json')};k=binary('0.17936053129375418');L=binary('7.651424601381517');gamma=fmpq(1,2)-k
assert {n:str(x) for n,x in [('k',k),('L',L),('gamma',gamma)]}==A['exact_parameters']
# Read the displayed table afresh from the snapshot, with exact decimal ceilings.
table={}
for line in (D/'source/NUM_REPORT.md').read_text().splitlines():
 if not line.startswith('| '):continue
 cells=[x.strip() for x in line.strip('|').split('|')]
 if len(cells)==5 and cells[0].startswith(('middle sup','outer sup','inner sup','middle sum of L2','outer sum of L2','inner sum of L2')):table[cells[0].replace(' (lobe next to P)','')]=cells[1:]
names={'sup_W_over_m':'sup W/m','sup_W':'sup W','mult_half':'sup W (1+u)^{1/2}/m','mult_half_minus_k':'sup W (1+u)^{1/2-k}/m','L2':'sum of L2 pieces'}
outreg={};scalars={};rows_total=0;exact_checks=0;enclosures_checked=0;ceilings_checked=0
for ti,tag in enumerate(tags):
 mid=get(tag,'cert_resid_middle');other=get(tag,'cert_resid_regions')['rows'];assert mid['done'] is True;outreg[tag]={}
 for region,rows in [('middle',mid['rows']),('outer',[r for r in other if r['region']=='outer']),('inner',[r for r in other if r['region']=='inner'])]:
  assert [r['ci'] for r in rows]==list(range(len(rows)));rows_total+=len(rows);reference=A['regions'][tag][region];assert len(rows)==reference['cells'];sums=fmpq(0);wm=fmpq(0);ww=fmpq(0);weighted={n:[fmpq(0),fmpq(0),-1] for n in ['mult_half','mult_half_minus_k']}
  logleft=None;logright=None
  for j,row in enumerate(rows):
   t=binary(row['t_a']);h=binary(row['h']);q=binary(row['W_over_m']);ell=binary(row['L2piece']);assert h>0 and q>=0 and ell>=0
   sums+=ell;wm=max(wm,q)
   if region=='middle':ww=max(ww,binary(row['W']))
   logleft=t if logleft is None else min(logleft,t);logright=t+h if logright is None else max(logright,t+h)
   radius=iv.exp(Q(t+h));base=1+radius/Q(L)
   for name,exponent in [('mult_half',fmpq(1,2)),('mult_half_minus_k',gamma)]:
    lo,hi=bounds(Q(q)*iv.exp(Q(exponent)*iv.ln(base)));m=weighted[name];m[0]=max(m[0],lo)
    if hi>m[1]:m[1]=hi;m[2]=j
  exact={'sup_W_over_m':wm,'L2':sums}
  if region=='middle':exact['sup_W']=ww
  for name,x in exact.items():
   assert str(x)==reference['exact'][name];exact_checks+=1;stored=binary(summary[tag][region][name]);assert stored==x if name!='L2' else stored>=x
   printed=dec(table[region+' '+names[name]][ti]);assert printed>stored and printed==dec(reference['display_ceilings'][name]);ceilings_checked+=1
  for name,(lo,hi,index) in weighted.items():
   primary=reference['weighted'][name];assert max(lo,rat(primary['lo']))<=min(hi,rat(primary['hi'])) and index==primary['max_row'];enclosures_checked+=1
   if name in summary[tag][region]:assert binary(summary[tag][region][name])>hi
   printed=dec(table[region+' '+names[name]][ti]);assert printed>hi and printed==dec(reference['display_ceilings'][name]);ceilings_checked+=1
  endpoints={}
  for label,x in [('left',logleft),('right',logright)]:
   assert str(x)==reference['nominal_domain']['log_'+label];lo,hi=bounds(iv.exp(Q(x)));primary=reference['nominal_domain'][label];assert max(lo,rat(primary['lo']))<=min(hi,rat(primary['hi']));endpoints[label]={'lo':str(lo),'hi':str(hi)};enclosures_checked+=1
  outreg[tag][region]={'cells':len(rows),'exact':{n:str(v) for n,v in exact.items()},'weighted':{n:{'lo':str(v[0]),'hi':str(v[1]),'max_row':v[2]} for n,v in weighted.items()},'nominal_domain':endpoints}
 raw=get(tag,'scalars_full' if not tag else 'scalars');s={}
 for name,rkey in [('x_star',None),('mu_minus_1','mu_minus_1'),('g','g_star'),('w_prime_P','w_prime_P')]:
  if name=='x_star':m,r=binary(raw['x_star_mid']),binary(raw['x_star_rad']);l,u=m-r,m+r
  else:l,u=map(binary,raw[rkey])
  assert str(l)==A['scalars'][tag][name]['lo'] and str(u)==A['scalars'][tag][name]['hi'];s[name]={'lo':str(l),'hi':str(u),'mid':str((l+u)/2)};exact_checks+=2
 for name,rounded,step in [('x_star','8.600063805157','1e-12'),('w_prime_P','10.15072524381','1e-11')]:
  l,u=rat(s[name]['lo']),rat(s[name]['hi']);m,d=dec(rounded),dec(step);assert m-d/2<l<=u<m+d/2
 scalars[tag]=s
for tag in tags[1:]:
 for region in ['middle','outer','inner']:
  for name,expected in A['relative_comparisons_of_published_bounds'][tag][region].items():
   a,b=binary(summary[''][region][name]),binary(summary[tag][region][name]);assert str((b-a)/a)==expected;exact_checks+=1
 for name in scalars[tag]:
  x=A['relative_comparisons_of_published_bounds'][tag]['scalars'][name];assert str(rat(scalars[tag][name]['mid'])-rat(scalars[''][name]['mid']))==x['midpoint_difference'];assert (max(rat(scalars[tag][name]['lo']),rat(scalars[''][name]['lo']))<=min(rat(scalars[tag][name]['hi']),rat(scalars[''][name]['hi'])))==x['overlap'];exact_checks+=2
for defect in A['refuted_outward_nominal_domain_labels']:
 dom=outreg[defect['tag']][defect['region']]['nominal_domain'];l,u=map(dec,defect['display'])
 for what in defect['defects']:
  assert l>rat(dom['left']['hi']) if what.startswith('left') else u<rat(dom['right']['lo'])
assert rows_total==A['rows_audited'] and ceilings_checked==A['printed_ceiling_checks'];checkpins(manifest['files'])
out={'start_utc':start,'utc':now(),'status':'PASS_INDEPENDENT_INTEGER_BINARY64_FMPQ_IV_AGGREGATION','proof_sha256':sha(D/'PROOF.md'),'code_sha256':sha(Path(__file__)),'primary_sha256':sha(E/'check.json'),'input_manifest_sha256':sha(E/'input_manifest.json'),'rows_audited':rows_total,'exact_cross_checks':exact_checks,'interval_cross_checks':enclosures_checked,'printed_ceiling_checks':ceilings_checked,'distinct_decimal_tokens_decoded_without_float':len(cache),'regions':outreg,'scope':'Independent decimal-token integer binary64 rounding, fmpq sums and iv80 exp-log weights; conditional nominal aggregates only. No producer or primary evaluator import.'}
with (E/'independent.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
print(json.dumps({n:out[n] for n in ['utc','status','rows_audited','exact_cross_checks','interval_cross_checks','printed_ceiling_checks','distinct_decimal_tokens_decoded_without_float']}))
