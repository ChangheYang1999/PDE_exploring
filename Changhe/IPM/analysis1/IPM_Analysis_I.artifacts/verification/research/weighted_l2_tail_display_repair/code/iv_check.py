from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from mpmath import iv
import json,hashlib,re,sys
sys.dont_write_bytecode=True;iv.dps=220
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/weighted_l2_tail_display_repair';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def decimal(s):
 m=re.fullmatch(r'([+-]?)(\d+)(?:\.(\d*))?(?:[eE]([+-]?\d+))?',s);assert m,s
 sign,whole,frac,ex=m.groups();frac=frac or '';return Q((-1 if sign=='-' else 1)*int(whole+frac))*Q(10)**(int(ex or 0)-len(frac))
def rat(s):
 z=s.split('/');assert len(z) in [1,2];return Q(int(z[0]),int(z[1]) if len(z)==2 else 1)
def iq(q):return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def ends(z):
 def f(v):s,m,e,bc=v;assert bc==m.bit_length();return Q((-1 if s else 1)*m)*Q(2)**e
 return {'lower_exact':str(f(z._mpi_[0])),'upper_exact':str(f(z._mpi_[1]))}
def run():
 x=load(E/'inputs.json');A=load(E/'arb.json');assert A['inputs_sha256']==sha(E/'inputs.json') and A['source_sha256']==sha(D/'code/arb_check.py')
 k,L,a,b=[rat(x['scalars'][n]) for n in ['k','L','a','b']];delta=Q(1,2)-k;F=sum((rat(z) for z in x['finite_inputs_exact'].values()),Q(0));assert F==rat(x['finite_sum_exact'])
 ci,co=rat(x['C_i_exact']),rat(x['C_o_exact']);r=x['report'];CI,CO=decimal(r['enlarged_C_i']),decimal(r['enlarged_C_o'])
 assert delta>0 and L>0 and a-5<b+17 and CI>ci>0 and CO>co>0
 def bi(C):return iv.pi*iq(C*C)*iv.exp(iq(2*(a-5)))
 def bo(C):return iv.pi*iq(C*C/delta)*iv.exp(iq(2+2*delta)*iv.ln(iq(L))-iq(2*delta*(b+17)))
 def root(z):return iv.exp(iv.ln(z)/2)
 I,O=bi(ci),bo(co);RI,RO=bi(CI),bo(CO)
 V={'inner_tail_sq_upper_endpoint':I,'outer_tail_sq_upper_endpoint':O,'finite_sq_upper_endpoint':iq(F),'finite_R2_upper_endpoint':root(iq(F)),'total_R2_upper_endpoint':root(O+I+iq(F)),'report_inner_tail':RI,'report_outer_tail':RO,'report_enlarged_total_norm':root(RO+RI+iq(F))}
 B={n:ends(z) for n,z in V.items()};labels={**x['labels'],'report_inner_tail':r['inner_tail_ceiling'],'report_outer_tail':r['outer_tail_ceiling'],'report_enlarged_total_norm':r['whole_ceiling']};checks={}
 for n,pair in B.items():
  ar=A['arb512'][n];lo=max(rat(ar['lower_exact']),rat(pair['lower_exact']));hi=min(rat(ar['upper_exact']),rat(pair['upper_exact']));assert lo<=hi,n
  q=decimal(labels[n]);assert q>rat(ar['upper_exact']) and q>rat(pair['upper_exact'])
  checks[n]={'decimal':labels[n],'above_both_upper_endpoints':True,'gap_above_iv_upper_exact':str(q-rat(pair['upper_exact']))}
 for n,z in A['source200_replay'].items():
  q=decimal(x['labels'][n]);u=rat(z['arb200']['upper_exact']);assert q>=u and q-u==rat(z['ceiling_gap_exact']);assert decimal(z['emitted_decimal'])==q
 printed=sum((decimal(t) for t in r['finite_printed_terms']),Q(0));assert F<decimal(r['finite_raw_ceiling']) and F<printed<decimal(r['finite_printed_sum_ceiling']);assert str(F)==A['finite_sum_exact'] and str(printed)==A['printed_sum_exact']
 v=load(ROOT/x['parent_path']);assert sha(ROOT/x['parent_path'])==x['parent_sha256'] and v['status']==x['parent_status'] and v['files']==x['parent_files']
 for n,h in x['parent_files'].items():assert sha(ROOT/n)==h,n
 for n,z in x['snapshots'].items():assert sha(ROOT/n)==z['sha256'],n
 return {'iv220':B,'label_checks':checks,'dual_interval_pairs':8,'source200_rational_upper_label_checks':5,'finite_sum_exact':str(F),'printed_sum_exact':str(printed),'parent_pin_count':len(x['parent_files']),'source_sha256':sha(Path(__file__)),'inputs_sha256':sha(E/'inputs.json'),'arb_check_sha256':sha(E/'arb.json'),'scope':'Independent separated-log interval path, exact decimal parser, integer-rational label comparisons and fresh pin audit only; no physical residual claim.'}
if __name__=='__main__':
 start=datetime.now(timezone.utc).isoformat();out={'start_utc':start,**run(),'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_IV220_AND_INTEGER_LABEL_REPAIR_REQUIRES_ACTUAL_REVIEW'}
 with (E/'iv.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],out['status'],out['dual_interval_pairs'],out['source200_rational_upper_label_checks'])
