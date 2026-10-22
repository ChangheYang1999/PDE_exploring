"""Arb direct powers versus iv separated logarithmic scalar reduction."""
import os,sys
sys.dont_write_bytecode=True
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,re
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];ROOT=D.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def write(p,z):p.write_text(json.dumps(z,indent=2,allow_nan=False)+'\n')
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ae(x):
 assert x.is_finite()
 def dy(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
 return dy(x.lower()),dy(x.upper())
def ie(x):
 def dy(x):s,m,e,bc=x;assert s in (0,1) and m>=0 and bc==int(m).bit_length();return (-1 if s else 1)*F(int(m))*F(2)**int(e)
 return tuple(dy(v) for v in x._mpi_)
def rec(x):return {'lower_exact':str(x[0]),'upper_exact':str(x[1])}
def decimal_ceil(q,digits=20):
 assert q>0;exp=0
 while q<F(10)**exp:exp-=1
 while q>=F(10)**(exp+1):exp+=1
 place=exp-digits+1;u=F(10)**place;n=q//u+1;c=n*u;assert c>q
 return f'{n}e{place}',str(c)
def ball(s):
 m=re.fullmatch(r'\[\s*([-0-9.eE+]+)\s*\+/-\s*([-0-9.eE+]+)\s*\]',s);assert m,s
 c,r=map(F,m.groups());assert r>=0;return c-r,c+r
start=now();freeze=json.loads((D/'evidence/source_freeze.json').read_text())
for path,h in freeze['files'].items():assert sha(ROOT/path)==h,path
x=json.loads((D/'evidence/inputs.json').read_text());assert sha(Path(x['literal_archive']['path']))==x['literal_archive']['sha256']
for path,z in x['source_snapshots'].items():assert sha(ROOT/path)==z['sha256'],path
v={n:F(q) for n,q in x['scalars'].items()};k,L,a,b=[v[n] for n in ['k','L','a','b']];delta=F(1,2)-k;assert delta>0 and L>0 and a-5<b+17
ci,co=F(x['C_i_exact']),F(x['C_o_exact']);CI,CO=F(x['reported_enlarged_C_i']),F(x['reported_enlarged_C_o']);assert 0<ci<CI and 0<co<CO
fin=F(x['finite_sum_exact']);assert fin==sum(map(F,x['finite_binary64_upper_inputs'].values()),F(0)) and fin>0
ctx.prec=512;ctx.threads=1;iv.dps=220
ri=aa(a-5).exp();ro=aa(b+17).exp();u=ro/aa(L)
Bia=arb.pi()*aa(ci)**2*ri**2;Boa=arb.pi()*aa(co)**2*aa(L)**2*u**aa(-2*delta)/aa(delta)
Bii=iv.pi*iq(ci*ci)*iv.exp(iq(2*(a-5)));Boi=iv.pi*iv.exp(iq(2+2*delta)*iv.log(iq(L))-iq(2*delta*(b+17)))*iq(co*co/delta)
valsA={'inner_tail_sq_upper':Bia,'outer_tail_sq_upper':Boa,'finite_regions_sq':aa(fin),'total_sq':aa(fin)+Bia+Boa,'total_R2_upper':(aa(fin)+Bia+Boa).sqrt(),'finite_R2_upper':aa(fin).sqrt(),'r_T_in_exact':ri,'r_T_out_exact':ro,'report_inner_bound':arb.pi()*aa(CI)**2*ri**2,'report_outer_bound':arb.pi()*aa(CO)**2*aa(L)**2*u**aa(-2*delta)/aa(delta)}
valsI={'inner_tail_sq_upper':Bii,'outer_tail_sq_upper':Boi,'finite_regions_sq':iq(fin),'total_sq':iq(fin)+Bii+Boi,'total_R2_upper':iv.sqrt(iq(fin)+Bii+Boi),'finite_R2_upper':iv.sqrt(iq(fin)),'r_T_in_exact':iv.exp(iq(a-5)),'r_T_out_exact':iv.exp(iq(b+17)),'report_inner_bound':iv.pi*iq(CI*CI)*iv.exp(iq(2*(a-5))),'report_outer_bound':iv.pi*iv.exp(iq(2+2*delta)*iv.log(iq(L))-iq(2*delta*(b+17)))*iq(CO*CO/delta)}
ans={};ceilings={};enclosures={}
for name in valsA:
 A=ae(valsA[name]);I=ie(valsI[name]);assert 0<A[0]<=A[1] and 0<I[0]<=I[1] and max(A[0],I[0])<=min(A[1],I[1]),name
 lo,hi=min(A[0],I[0]),max(A[1],I[1]);enclosures[name]=(lo,hi);ans[name]={'arb512':rec(A),'iv220':rec(I),'arb_display_diagnostic':valsA[name].str(24)};text,q=decimal_ceil(hi);ceilings[name]={'decimal':text,'exact':q};assert F(q)>hi
 if name in x['stored_printed_balls']:
  P=ball(x['stored_printed_balls'][name]);assert P[0]<=lo<=hi<=P[1],('saved ball does not contain independent bounds',name)
labels={}
for key,text in x['endpoint_labels'].items():
 name=key.removesuffix('_endpoint');lo,hi=enclosures[name];q=F(text)
 verdict='INWARD_BELOW_BOTH_LOWER_ENDPOINTS' if q<lo else 'STRICTLY_ABOVE_BOTH_UPPER_ENDPOINTS' if q>hi else 'UNDECIDED_INTERVAL_INTERSECTION'
 labels[key]={'label':text,'verdict':verdict,'gap_from_lower_exact':str(lo-q),'gap_from_upper_exact':str(q-hi)}
reported={}
for region in ['inner','outer']:
 q=F(x['report_tail_ceilings'][region]);lo,hi=enclosures['report_'+region+'_bound'];assert q>hi
 short=F(x['report_summary_short_values'][region]);orig=enclosures[region+'_tail_sq_upper'];assert short<orig[0]
 reported[region]={'enlarged_constant':x['reported_enlarged_C_'+('i' if region=='inner' else 'o')],'ceiling':str(q),'strictly_outward':True,'summary_short_value':str(short),'summary_is_below_enlarged_bound_lower':short<lo,'summary_is_below_original_bound_lower':True}
q=F(x['report_whole_ceiling']);assert q>enclosures['total_R2_upper'][1]
for path,h in freeze['files'].items():assert sha(ROOT/path)==h,path
assert sha(Path(x['literal_archive']['path']))==x['literal_archive']['sha256']
z={'start_utc':start,'utc':now(),'status':'PASS_CONDITIONAL_WEIGHTED_L2_TAIL_SCALAR_REDUCTION_REQUIRES_ACTUAL_REVIEW','source_freeze_sha256':sha(D/'evidence/source_freeze.json'),'inputs_sha256':sha(D/'evidence/inputs.json'),'independent_intervals':ans,'strict_decimal_ceilings':ceilings,'endpoint_label_checks':labels,'report_tail_ceiling_checks':reported,'whole_conditional_ceiling':{'decimal':x['report_whole_ceiling'],'strictly_outward_for_stored_scalar_inputs':True},'counts':{'dual_scalar_enclosures':len(ans),'checked_endpoint_labels':len(labels),'report_tail_ceilings':2,'independent_printed_ball_containments':sum(n in x['stored_printed_balls'] for n in ans)},'physical_majorants_validated':False,'finite_region_integrals_validated':False,'scope':x['scope']}
assert not (D/'evidence/checks.json').exists();write(D/'evidence/checks.json',z)
print(json.dumps({n:z[n] for n in ['utc','status','endpoint_label_checks','report_tail_ceiling_checks','whole_conditional_ceiling','counts']},indent=2))
