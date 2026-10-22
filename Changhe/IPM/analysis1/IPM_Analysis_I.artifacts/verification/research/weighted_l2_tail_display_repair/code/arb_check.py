from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from decimal import Decimal,ROUND_CEILING,getcontext
import ast,json,hashlib,re,sys
from flint import arb,ctx
sys.dont_write_bytecode=True;ctx.threads=1
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/weighted_l2_tail_display_repair';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def a(q):q=Q(q);return arb(q.numerator)/q.denominator
def ends(b):
 def f(z):m,e=z.man_exp();return Q(int(m))*Q(2)**int(e)
 assert b.is_finite();return {'lower_exact':str(f(b.lower())),'upper_exact':str(f(b.upper()))}
def run():
 x=load(E/'inputs.json');f=load(E/'proof_first.json');assert sha(D/'PROOF.md')==f['proof_sha256']
 for n,h in x['parent_files'].items():assert sha(ROOT/n)==h
 assert sha(ROOT/x['parent_path'])==x['parent_sha256']
 for n,z in x['snapshots'].items():assert sha(ROOT/n)==z['sha256']
 k,L,aa,bb=[Q(x['scalars'][n]) for n in ['k','L','a','b']];delta=Q(1,2)-k;ci,co=Q(x['C_i_exact']),Q(x['C_o_exact']);F=Q(x['finite_sum_exact']);r=x['report'];CI,CO=Q(r['enlarged_C_i']),Q(r['enlarged_C_o'])
 assert 0<k<Q(1,2) and L>0 and aa-5<bb+17 and ci<CI and co<CO
 ctx.prec=512;ri=a(aa-5).exp();ro=a(bb+17).exp();u=ro/a(L)
 bi=arb.pi()*a(ci)**2*ri**2;bo=arb.pi()*a(co)**2*a(L)**2*u**a(-2*delta)/a(delta)
 BI=arb.pi()*a(CI)**2*ri**2;BO=arb.pi()*a(CO)**2*a(L)**2*u**a(-2*delta)/a(delta)
 vals={'inner_tail_sq_upper_endpoint':bi,'outer_tail_sq_upper_endpoint':bo,'finite_sq_upper_endpoint':a(F),'finite_R2_upper_endpoint':a(F).sqrt(),'total_R2_upper_endpoint':(a(F)+bi+bo).sqrt(),'report_inner_tail':BI,'report_outer_tail':BO,'report_enlarged_total_norm':(a(F)+BI+BO).sqrt()}
 A={n:ends(v) for n,v in vals.items()}
 for n,t in x['labels'].items():assert Q(t)>Q(A[n]['upper_exact']),n
 for n,t in [('report_inner_tail',r['inner_tail_ceiling']),('report_outer_tail',r['outer_tail_ceiling']),('report_enlarged_total_norm',r['whole_ceiling'])]:assert Q(t)>Q(A[n]['upper_exact'])
 assert F==sum(map(Q,x['finite_inputs_exact'].values()),Q(0)) and F<Q(r['finite_raw_ceiling'])
 printed=sum(map(Q,r['finite_printed_terms']),Q(0));assert F<printed<Q(r['finite_printed_sum_ceiling'])
 # Execute only the two explicitly inspected pure functions, never the foreign module.
 source=(D/'sources/r2_tails_v2.py').read_text();tree=ast.parse(source)
 defs=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ['ball_upper','exact_ceil']];assert len(defs)==2
 assert 'ctx.prec = 200' in source and 'getcontext().prec = 80; getcontext().rounding = ROUND_CEILING' in source
 ns={'arb':arb,'re':re,'Fraction':Q,'Decimal':Decimal,'ROUND_CEILING':ROUND_CEILING};exec(compile(ast.Module(body=defs,type_ignores=[]),'snapshot_pure_functions','exec'),ns)
 ctx.prec=200;getcontext().prec=80;getcontext().rounding=ROUND_CEILING
 raw=load(ROOT/'research/weighted_l2_tail_reduction/evidence/inputs.json');tail=load(ROOT/'research/weighted_l2_tail_reduction/sources/cert_tail.json');inner=load(ROOT/'research/weighted_l2_tail_reduction/sources/cert_inner_tail.json')
 L200=arb(float(L));k200=arb(float(k));a200=arb(float(aa));b200=arb(float(bb));d200=arb(1)/2-k200
 C200o=ns['ball_upper'](tail['tail_bound_weighted']);C200i=ns['ball_upper'](inner['bound_W_over_m'])
 Ri=(a200-5).exp();Ro=(b200+17).exp();U=Ro/L200
 O=arb.pi()*C200o**2*L200**2*U**(-2*d200)/d200;I=arb.pi()*C200i**2*Ri**2
 ff=arb(float(Q(x['finite_inputs_exact']['middle'])))+arb(float(Q(x['finite_inputs_exact']['outer'])))+arb(float(Q(x['finite_inputs_exact']['inner'])))
 targets={'inner_tail_sq_upper_endpoint':(I,10),'outer_tail_sq_upper_endpoint':(O,10),'finite_sq_upper_endpoint':(ff,12),'finite_R2_upper_endpoint':(ff.sqrt(),12),'total_R2_upper_endpoint':((ff+O+I).sqrt(),12)}
 replay={}
 for n,(z,digits) in targets.items():
  s=ns['exact_ceil'](z,digits);ep=ends(z);assert s==x['labels'][n] and Q(s)>=Q(ep['upper_exact'])
  replay[n]={'digits':digits,'emitted_decimal':s,'arb200':ep,'ceiling_gap_exact':str(Q(s)-Q(ep['upper_exact']))}
 return {'arb512':A,'source200_replay':replay,'finite_sum_exact':str(F),'printed_sum_exact':str(printed),'parent_pin_count':len(x['parent_files']),'snapshots_sha256':{n:z['sha256'] for n,z in x['snapshots'].items()},'source_sha256':sha(Path(__file__)),'inputs_sha256':sha(E/'inputs.json'),'scope':'8 exact scalar intervals and five source upper-label replays; physical premises remain open.'}
if __name__=='__main__':
 start=datetime.now(timezone.utc).isoformat();out={'start_utc':start,**run(),'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ARB512_REPAIRED_LABELS_AND_ACTUAL_PURE_FUNCTION_REPLAY_REQUIRES_INDEPENDENT_CHECK'}
 with (E/'arb.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],out['status'],out['parent_pin_count'])
