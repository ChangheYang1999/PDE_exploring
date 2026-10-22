from pathlib import Path
from fractions import Fraction as F
import sys,os,json
sys.dont_write_bytecode=True
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
from flint import arb,fmpq,ctx
ctx.prec=256;ctx.threads=1
R=Path(__file__).resolve().parents[3];D=R/'research/resolution_aggregate_audit';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();pf=p.load(E/'proof_first.json');assert p.sha(D/'PROOF.md')==pf['proof_sha256']=='c6bf17a382f3edf0fec419c9f858b96c2fcb5f18f93ae92b7a15c3b5dc0cf3fc';manifest=p.load(E/'input_manifest.json');p.rehash(manifest['files'])
N=R.parent/'ipmA-num';tags=['','v3_h0.004','v4_M230','v5_R0knot2'];summary={a['tag']:a for a in p.load(D/'source/variants_summary.json')}
def Ff(x):assert type(x) is float and __import__('math').isfinite(x);return F.from_float(x)
def Q(x):x=F(x);return arb(fmpq(x.numerator,x.denominator))
def ep(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def en(x):return {'lo':str(ep(x.lower())),'hi':str(ep(x.upper()))}
def enc(l,r):return {'lo':str(l),'hi':str(r)}
def get(tag,stem):return p.load(N/'runs'/(stem+('_'+tag if tag else '')+'.json'))
k=Ff(.17936053129375418);L=Ff(7.651424601381517);g=F(1,2)-k;assert Ff(.5-.17936053129375418)==g and 0<g<F(1,2)
ceilings={
'middle':{'sup_W_over_m':['2.5965e-4','2.5965e-4','2.5971e-4','2.5965e-4'],'sup_W':['1.2015e-4','1.2015e-4','1.2018e-4','1.2015e-4'],'mult_half':['3.8071e-4','3.8071e-4','3.8079e-4','3.8071e-4'],'mult_half_minus_k':['3.3187e-4','3.3187e-4','3.3195e-4','3.3187e-4'],'L2':['4.973e-9','4.964e-9','5.001e-9','5.209e-9']},
'outer':{'sup_W_over_m':['9.3189e-5','9.3188e-5','9.3574e-5','9.3145e-5'],'mult_half':['7.3681e-3','7.3682e-3','7.3891e-3','7.3713e-3'],'mult_half_minus_k':['1.4636e-3','1.4636e-3','1.4684e-3','1.4640e-3'],'L2':['3.907e-7','3.907e-7','3.907e-7','3.915e-7']},
'inner':{'sup_W_over_m':['9.1893e-6','5.4351e-6','9.1892e-6','9.1794e-6'],'mult_half':['9.2024e-6','5.4429e-6','9.2023e-6','9.1925e-6'],'mult_half_minus_k':['9.1921e-6','5.4367e-6','9.1920e-6','9.1822e-6'],'L2':['3.483e-16','6.850e-17','3.483e-16','3.477e-16']}}
regions={};scalars={};display_checks=0;total=0
for ti,tag in enumerate(tags):
 middle=get(tag,'cert_resid_middle');rr=get(tag,'cert_resid_regions')['rows'];assert middle['done'] is True
 regions[tag]={}
 for region,rows in [('middle',middle['rows']),('outer',[r for r in rr if r['region']=='outer']),('inner',[r for r in rr if r['region']=='inner'])]:
  assert [r['ci'] for r in rows]==list(range(len(rows))) and len(rows)==summary[tag][region]['ncells']
  total+=len(rows);maxima={name:[F(0),F(0),-1] for name in ['mult_half','mult_half_minus_k']};bounds={};sums=F(0)
  left=min(Ff(r['t_a']) for r in rows);right=max(Ff(r['t_a'])+Ff(r['h']) for r in rows)
  for j,row in enumerate(rows):
   t=Ff(row['t_a']);h=Ff(row['h']);q=Ff(row['W_over_m']);ell=Ff(row['L2piece']);assert h>0 and q>=0 and ell>=0;sums+=ell
   base=1+Q(t+h).exp()/Q(L)
   for name,power in [('mult_half',F(1,2)),('mult_half_minus_k',g)]:
    z=Q(q)*base**Q(power);lo,hi=ep(z.lower()),ep(z.upper());m=maxima[name];m[0]=max(m[0],lo)
    if hi>m[1]:m[1]=hi;m[2]=j
  exact={'sup_W_over_m':max(Ff(row['W_over_m']) for row in rows),'L2':sums}
  if region=='middle':exact['sup_W']=max(Ff(row['W']) for row in rows)
  for name,v in exact.items():
   stored=Ff(summary[tag][region][name]);assert (stored==v if name!='L2' else stored>=v)
   assert F(ceilings[region][name][ti])>stored;display_checks+=1
  for name,(lo,hi,j) in maxima.items():
   if name in summary[tag][region]:assert Ff(summary[tag][region][name])>hi
   assert F(ceilings[region][name][ti])>hi;display_checks+=1
  domain={'left':en(Q(left).exp()),'right':en(Q(right).exp()),'log_left':str(left),'log_right':str(right)}
  regions[tag][region]={'cells':len(rows),'exact':{n:str(v) for n,v in exact.items()},'weighted':{n:{'lo':str(v[0]),'hi':str(v[1]),'max_row':v[2]} for n,v in maxima.items()},'nominal_domain':domain,'display_ceilings':{n:val[ti] for n,val in ceilings[region].items()}}
 raw=get(tag,'scalars_full' if not tag else 'scalars');sm=summary[tag]['scalars'];assert sm['x_star']==[raw['x_star_mid'],raw['x_star_rad']] and sm['g']==raw['g_star'] and sm['w_prime_P']==raw['w_prime_P'] and sm['mu_minus_1']==raw['mu_minus_1']
 sc={}
 for name in ['x_star','mu_minus_1','g','w_prime_P']:
  a,b=map(Ff,sm[name]);lo,hi=(a-b,a+b) if name=='x_star' else (a,b);assert lo<=hi;sc[name]={'lo':str(lo),'hi':str(hi),'mid':str((lo+hi)/2)}
 for name,rounded,step in [('x_star','8.600063805157','1e-12'),('w_prime_P','10.15072524381','1e-11')]:
  lo,hi=F(sc[name]['lo']),F(sc[name]['hi']);r,d=F(rounded),F(step);assert r-d/2<lo<=hi<r+d/2;sc[name]['common_13_significant_digit_rounding']=rounded
 scalars[tag]=sc
comparisons={}
for tag in tags[1:]:
 comp={}
 for region in ['middle','outer','inner']:
  comp[region]={n:str((Ff(summary[tag][region][n])-Ff(summary[''][region][n]))/Ff(summary[''][region][n])) for n in ['sup_W_over_m','mult_half_minus_k','L2']}
  if region=='middle':
   comp[region].update({n:str((Ff(summary[tag][region][n])-Ff(summary[''][region][n]))/Ff(summary[''][region][n])) for n in ['mult_half','sup_W']})
 comp['scalars']={n:{'midpoint_difference':str(F(scalars[tag][n]['mid'])-F(scalars[''][n]['mid'])),'overlap':max(F(scalars[tag][n]['lo']),F(scalars[''][n]['lo']))<=min(F(scalars[tag][n]['hi']),F(scalars[''][n]['hi']))} for n in scalars[tag]};comparisons[tag]=comp
assert not comparisons['v4_M230']['scalars']['g']['overlap']
# Verify the broad reported stability summaries for the saved bounds, not physical quantities.
for tag,comp in comparisons.items():
 for n in ['sup_W_over_m','mult_half','mult_half_minus_k','sup_W']:assert abs(F(comp['middle'][n]))<F('0.0003')
 assert abs(F(comp['outer']['sup_W_over_m']))<F('0.005')
 for region in ['middle','outer']:assert abs(F(comp[region]['L2']))<F('0.05')
# Nominal intervals have inward printed labels. Record definite discrepancies only.
refuted=[]
for tag in tags:
 for region,display in [('inner',('5.1555e-5','0.0076514')),('outer',('1468','3.5459e10') if tag=='v5_R0knot2' else ('3413','8.244e10'))]:
  dom=regions[tag][region]['nominal_domain'];bad=[]
  if F(display[0])>F(dom['left']['hi']):bad.append('left display exceeds exact nominal left endpoint')
  if F(display[1])<F(dom['right']['lo']):bad.append('right display below exact nominal right endpoint')
  if bad:refuted.append({'tag':tag,'region':region,'display':list(display),'defects':bad})
p.rehash(manifest['files'])
out={'start_utc':start,'utc':p.now(),'status':'PASS_CONDITIONAL_SAVED_ROW_AGGREGATION_AND_SCALAR_DISPLAY_AUDIT','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'inputs':manifest['files'],'input_manifest_sha256':p.sha(E/'input_manifest.json'),'exact_parameters':{'k':str(k),'L':str(L),'gamma':str(g)},'rows_audited':total,'printed_ceiling_checks':display_checks,'regions':regions,'scalars':scalars,'relative_comparisons_of_published_bounds':comparisons,'refuted_outward_nominal_domain_labels':refuted,'scope':'Only nominal row aggregation and scalar display logic. Cell physical majorants, interval coverage, trial reconstruction and PDE endpoint remain OPEN. Differences of upper bounds do not enclose differences of actual integrals.'};p.write(E/'check.json',out);print(json.dumps({n:out[n] for n in ['utc','status','rows_audited','printed_ceiling_checks','refuted_outward_nominal_domain_labels']}))
