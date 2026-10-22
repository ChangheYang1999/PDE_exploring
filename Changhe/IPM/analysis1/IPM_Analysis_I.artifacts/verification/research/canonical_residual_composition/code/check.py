"""Premise substitution and independent exact scalar arithmetic, not a regional rerun."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,gzip,re,time
from flint import fmpq,arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_residual_composition';E=D/'evidence'
ARCHIVE='research/middle_residual/evidence/original_knots.jsonl.gz';ASHA='c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648'
SOURCE='data_exact/modal_v2.json';SSHA='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';ZPATH='research/modal_repair/evidence/independent_gauss_iv.json';ZSHA='0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a'
DEPS={'146':('research/global_residual_second/evidence/verdict.json','b1e466d52d91cce5c7e3ff5d4ed9cf3d9ce9c95d7094992a995dfd6c84eaaae4'),'156':('research/canonical_archive_second/evidence/verdict.json','5e5a0879c90afca49df5586e8c602c3b8a990dbea61a5280918646fddb68e75f')}
EXTERNAL={str(B.parent/'ipmA-num/data'/n):h for n,h in [('cert_green.npz','c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'),('cert_inner_green.npz','4ba853bbad32a43894fe2f21a9f419b6ec23d7079b5a38a8b3a5b4702c20e8ee'),('cert_outer_green.npz','db1138f81d3dca243d2e3cd1ca07830740c89b32f526de5b75adf1d4329f2858'),('trial_v2_h0.008.npz','a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874')]}
K=F(1615536043799051,9007199254740992);L=F(8614738245908811,1125899906842624);JOINS=[F(-685794559684773,140737488355328),F(2289893859708677,281474976710656)]
MKEYS={'W':'W_upper_exact','W_over_m':'W_over_m_upper_exact','weighted_1/2':'Wm_times_one_plus_u_power_half_upper_exact','weighted_'+str(F(1,2)-K):'Wm_times_one_plus_u_power_half_minus_k_upper_exact'}
def now():return datetime.now(timezone.utc).isoformat()
def need(x,s):
 if not x:raise ValueError(s)
def unique(items):
 d={}
 for k,v in items:need(k not in d,'duplicate JSON key');d[k]=v
 return d
def parse(s):return json.loads(s,object_pairs_hook=unique,parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
def load(p):return parse(Path(p).read_text())
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write(p,v):
 with Path(p).open('x') as f:json.dump(v,f,indent=2);f.write('\n')
def pin(pins,n,h=None):
 p=(B/n).resolve();need(p.is_relative_to(B) or EXTERNAL.get(str(p))==h and h is not None,'fixed read-only external file');n=str(p.relative_to(B)) if p.is_relative_to(B) else str(p);actual=sha(p);need(h is None or actual==h,'immutable file '+n);need(n not in pins or pins[n]==actual,'consistent pin');pins[n]=actual;return actual
def merge(pins,v):
 for n,h in v['files'].items():pin(pins,n,h)
def qf(q):return F(int(q.numerator),int(q.denominator))
def ff(s):
 x=F(s);need(x==qf(fmpq(s)),'independent exact rational import');return x
def ball(x):
 need(set(x)=={'schema','mid_m','mid_e','rad_m','rad_e'} and x['schema']=='arb-dyadic-mid-radius-v1','unchanged exact ball schema')
 for k in ['mid_m','mid_e','rad_m','rad_e']:need(type(x[k]) in (int,str) and re.fullmatch(r'-?\d+',str(x[k])) is not None,'integer dyadic component')
 m=F(int(x['mid_m']))*F(2)**int(x['mid_e']);r=F(int(x['rad_m']))*F(2)**int(x['rad_e']);need(r>=0,'nonnegative radius');qm=fmpq(x['mid_m'])*fmpq(2)**int(x['mid_e']);qr=fmpq(x['rad_m'])*fmpq(2)**int(x['rad_e']);a,b=m-r,m+r;need((a,b)==(qf(qm-qr),qf(qm+qr)),'two dyadic endpoint routes');return a,b
def hx(s):
 m=re.fullmatch(r'([+-]?)0x([0-9a-f]+)\.([0-9a-f]*)p([+-]?[0-9]+)',s);need(m is not None,'exact hex');sg,a,b,e=m.groups();return F((-1 if sg=='-' else 1)*int(a+b,16))*F(2)**(int(e)-4*len(b))
def ii(x):x=F(x);return iv.mpf(x.numerator)/iv.mpf(x.denominator)
def iep(t):
 s,m,e,b=t;need(b>=0,'finite interval endpoint');return (-1)**s*F(int(m))*F(2)**int(e)
def ai(x):x=F(x);return arb(x.numerator)/arb(x.denominator)
def ae(x):return [qf(x.lower().fmpq()),qf(x.upper().fmpq())]
def review_gate(v,tag,r,post):
 m=load(B/'notes/reviews'/f'{tag}_metadata.json');raw=load(B/'notes/reviews'/f'{tag}_response.json');text=(B/'notes/reviews'/f'{tag}_response.md').read_text();req=B/'notes/reviews'/f'{tag}_request.txt'
 need(m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['requested_model']=='us.anthropic.claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual accepted dependency model')
 need(m['request_id']==r['request_id'] and m['input_sha256']==r['input_sha256']==sha(req),'actual dependency request binding');need(text=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n','full raw response');need(datetime.fromisoformat(m['end_utc'])<datetime.fromisoformat(post['utc'])<datetime.fromisoformat(v['utc']),'actual later dependency disposition')
 need(post['review_request_id']==m['request_id'] and post['review_input_sha256']==m['input_sha256'] and post['review_response_sha256']==sha(B/'notes/reviews'/f'{tag}_response.json'),'actual disposition identity')
 return {k:m[k] for k in ['request_id','input_sha256','actual_response_model','stop_reason','start_utc','end_utc']}
def gate156(v):
 need(v['status']=='CONFIRMED_COMPLETE_CANONICAL_MOMENT_ARCHIVE' and v['counts']=={'H':3265568,'I':406638,'J':406638,'I_steps':406638,'J_steps':406638} and v['moment_targets']==813276 and v['exact_H_coefficients']==3265568 and v['independent_exact_anchors']==783,'actual complete156')
 for n,h in [(ARCHIVE,ASHA),(SOURCE,SSHA),(ZPATH,ZSHA)]:need(v['files'][n]==h,'identical canonical input')
def gate146(v):
 need(v['status']=='CONFIRMED_WHOLE_PLANE_RESIDUAL_WITH_COMPLETE_SECOND_MIDDLE_SHARED_CANONICAL_INPUTS' and v['cells']=={'inner':54,'middle':7809,'outer':89},'actual complete146');need(v['actual_full_middle_verdict_sha256']=='1f4190763b9017802e0c09bb085aae535c1c0b98b3b1f1e7d7cdc9256ee0d159','actual46 binding')
def main():
 start=now();tic=time.monotonic();pins={};deps={}
 for tag,(name,h) in DEPS.items():pin(pins,name,h);deps[tag]=load(B/name);merge(pins,deps[tag])
 v146=deps['146'];v156=deps['156'];gate146(v146);gate156(v156)
 reviews={'146':review_gate(v146,'global_residual_second_complete_v2',v146['reviews']['global_residual_second_complete_v2'],v146['postreview_record']),'156':review_gate(v156,'canonical_archive_second_actual',v156['actual_output_review'],load(B/'research/canonical_archive_second/evidence/postreview_record.json'))}
 for n,h in [(ARCHIVE,ASHA),(SOURCE,SSHA),(ZPATH,ZSHA),('research/modal_repair/PROOF.md','9f97fa684956c47bb5b9547f0fe8fabe1df51f036e312dd7022873f8cec37843'),('research/modal_repair/evidence/audit_verdict.json','c17c7f4dfbc86ac789838d59d846f5641cae59577dd8e62987edd31904dab6b8')]:pin(pins,n,h)
 src=load(B/SOURCE);knots=sorted(set(map(hx,src['arrays']['knots']['hex'])));need(len(knots)==1559 and [knots[0],knots[-1]]==JOINS,'all exact original knots');need(hx(src['scalars_hex']['k'])==K and hx(src['scalars_hex']['L'])==L,'distinguished exact parameters')
 z=load(B/ZPATH)['values']['A00_correction'];Z=[str(ff(z[k])) for k in ['lower_exact_dyadic','upper_exact_dyadic']];need(F(Z[0])<=F(Z[1]),'ordered common Z')
 with (B/'research/canonical_archive_second/evidence/full_spans.jsonl').open() as f:head=parse(next(f))
 need(head['source_sha256']==SSHA and head['archive_sha256']==ASHA and head['normalization_sha256']==ZSHA and head['Z_exact']==Z and head['full_run'] is True,'same accepted156 header')
 counts={'spans':0,'child_cells':0,'H_shapes':0,'moment_shapes':0,'endpoint_H_two_exact_boxes':0,'endpoint_moment_two_exact_boxes':0,'exact_knot_geometry':0};boundary={}
 with gzip.open(B/ARCHIVE,'rt') as f:
  header=parse(next(f));need(header['hashes']['input']==SSHA and header['hashes']['normalization']==ZSHA and header['scalars_exact']['k']==str(K) and header['scalars_exact']['L']==str(L),'regional common header')
  for i in range(1558):
   line=next(f);need(line.endswith('\n'),'complete archive line');r=parse(line);a,b,mid=map(ff,[r['a_exact'],r['b_exact'],r['polynomial_mid_exact']]);need(r['span']==i and r['type']=='span' and r['first_cell']==counts['child_cells'] and type(r['count']) is int and r['count']>0,'complete ordered child cover');need(a==knots[i]<b==knots[i+1] and mid==(a+b)/2,'all exact original joins');counts['exact_knot_geometry']+=3
   need(len(r['density_polynomials'])==262 and all(len(x)==8 for x in r['density_polynomials']) and len(r['i_left'])==len(r['j_right'])==261,'full archive shapes');counts['spans']+=1;counts['child_cells']+=r['count'];counts['H_shapes']+=2096;counts['moment_shapes']+=522
   if i in [0,1557]:
    boundary[i]=r
    for row in r['density_polynomials']:
     for v in row:ball(v);counts['endpoint_H_two_exact_boxes']+=1
    for v in r['i_left']+r['j_right']:ball(v);counts['endpoint_moment_two_exact_boxes']+=1
  footer=parse(next(f));need(footer['type']=='complete' and footer['spans']==1558 and footer['cells']==7809 and not f.read(),'whole original gzip footer and no extra bytes')
 need(counts=={'spans':1558,'child_cells':7809,'H_shapes':3265568,'moment_shapes':813276,'endpoint_H_two_exact_boxes':4192,'endpoint_moment_two_exact_boxes':1044,'exact_knot_geometry':4674},'all archive counters')
 def inherited(n):need(n in v146['files'],'operative input in accepted146');pin(pins,n,v146['files'][n]);return load(B/n)
 inn=inherited('research/inner_majorant/evidence/inner_result.json');out=inherited('research/outer_majorant/evidence/outer_result.json');last=inherited('research/outer_majorant/evidence/final_span.json');ex=inherited('research/outer_majorant/evidence/final_span_extract.json')
 need(last==boundary[1557],'whole actual last archive record');need(ex['archive_sha256']==ASHA and ex['full_gzip_footer_read'] is True and ex['final_span_sha256']==sha(B/'research/outer_majorant/evidence/final_span.json'),'last extraction binds complete archive')
 need(inn['dependency_pins']['input']==out['dependency_pins']['input']==SSHA and inn['dependency_pins']['archive']==out['dependency_pins']['archive']==ASHA and out['dependency_pins']['normalization']==ZSHA,'same regional inputs');need(F(inn['ta_exact'])==JOINS[0] and F(out['tb_exact'])==JOINS[1] and list(map(F,out['knot_interval_exact']))==knots[-2:],'exact boundary joins');need(F(inn['k_exact'])==K and F(inn['L_exact'])==L and F(out['scalars_exact']['k'])==K and F(out['scalars_exact']['L'])==L,'same regional k,L')
 need(inn['archive_join_checks']==1834 and out['checks']['archive_joins']==1834,'inherited complete endpoint jets');need([x['n'] for x in inn['cases'][0]['upper_Green']]==list(range(2,262)) and [x['n'] for x in out['green']]==list(range(1,262)),'all inherited boundary Green records')
 c=inn['canonical_c_consistency'];need(F(c['lower_exact'])<=3/K-1<=F(c['upper_exact']),'inner normalization consistency only')
 old=inherited('research/global_residual_assembly/evidence/primary_assembly_v2.json');vi=inherited('research/inner_cells/evidence/verdict.json');vo=inherited('research/outer_cells/evidence/verdict.json');vm=inherited('research/middle_second/evidence/full_q16_verdict.json')
 need(vm['cells']==7809 and vm['spans']==1558 and vi['cells']==54 and vo['cells']==89,'full regional coverage counts');need(old['regions']['inner']['full_tail'] is True and old['regions']['outer']['full_tail'] is True and list(map(F,old['joins_exact']))==JOINS,'closed full tails and joins')
 regional={'inner':ff(vi['L2_join_squared_upper_exact']),'middle':ff(vm['L2_squared_upper_exact']),'outer':ff(vo['L2_join_squared_upper_exact'])};need(all(x>=0 for x in regional.values()),'nonnegative regional squared bounds');need(regional['inner']==ff(old['regions']['inner']['squared_norm_exact']) and regional['outer']==ff(old['regions']['outer']['squared_norm_exact']),'unchanged end regions')
 S=sum(regional.values(),F(0));replace=ff(old['global_N2']['input_squared_exact'])-ff(old['regions']['middle']['squared_norm_exact'])+regional['middle'];native=sum((fmpq(str(regional[n])) for n in ['outer','middle','inner']),fmpq(0));need(S==replace==qf(native)==ff(v146['squared_norm_exact']) and S>0,'three exact squared sums')
 ctx.prec=384;ctx.threads=1;iv.dps=140;ar=ae(ai(S).sqrt());ir=list(map(iep,iv.sqrt(ii(S))._mpi_));ceiling=F('0.001903991978');need(ceiling==ff(v146['N2_strict_ceiling_exact']),'same strict norm ceiling')
 for endpoints in [ar,ir]:need(0<endpoints[0]<=endpoints[1]<ceiling and endpoints[0]**2<=S<=endpoints[1]**2,'outward exact squared root test')
 need(S<ceiling**2 and max(ar[0],ir[0])<=min(ar[1],ir[1]),'strict norm ceiling and independent root overlap')
 sup={};ceilings=['0.000428057986','0.000291624061','0.007737963257','0.001510081576']
 for (key,mkey),decimal in zip(MKEYS.items(),ceilings,strict=True):
  vals={'inner':ff(vi['public_bounds'][key]['authoritative_upper_exact']),'middle':ff(vm['maxima'][mkey]['upper_exact']),'outer':ff(vo['public_bounds'][key]['authoritative_upper_exact'])};need(vals=={n:ff(x) for n,x in v146['suprema'][key]['regional_upper_exact'].items()},'three accepted supremum sources');upper=max(vals.values());native_sorted=sorted(fmpq(str(x)) for x in vals.values())[-1];need(upper==qf(native_sorted)==ff(v146['suprema'][key]['upper_exact'])<F(decimal)==ff(v146['suprema'][key]['strict_ceiling']['exact']),'two exact maxima and strict ceilings');sup[key]={'regions':{n:str(x) for n,x in vals.items()},'upper_exact':str(upper),'strict_decimal':decimal}
 proof=load(E/'proof_first.json');need(proof['sha256']==sha(D/'PROOF.md') and datetime.fromisoformat(proof['utc'])<datetime.fromisoformat(start),'unchanged proof before execution')
 for p in [D/'PROOF.md',D/'code/check.py',E/'proof_first.json']:pin(pins,str(p.relative_to(B)))
 for n,h in pins.items():need(sha(B/n)==h,'unchanged application inputs')
 value={'start_utc':start,'utc':now(),'status':'PASS_COMPLETE_CANONICAL_RESIDUAL_PREMISE_COMPOSITION_REQUIRES_ACTUAL_REVIEW','counts':counts,'accepted_dependencies':{tag:{'path':n,'sha256':h,'utc':deps[tag]['utc']} for tag,(n,h) in DEPS.items()},'dependency_reviews':reviews,'source_sha256':SSHA,'archive_sha256':ASHA,'normalization_sha256':ZSHA,'Z_exact':Z,'k_exact':str(K),'L_exact':str(L),'joins_exact':list(map(str,JOINS)),'regional_squared_exact':{n:str(x) for n,x in regional.items()},'squared_norm_exact':str(S),'root_arb384_exact':list(map(str,ar)),'root_iv140_exact':list(map(str,ir)),'strict_N2_decimal':'0.001903991978','suprema':sup,'boundary_contracts':{'first_J_right':261,'last_I_left':261,'inner_full_endpoint_jets':1834,'outer_full_endpoint_jets':1834,'last_whole_record_equal':True},'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tic,'scope':'Only the shared canonical H/I/J archive premise of accepted146 is discharged for the distinguished normalized modal_v2 trial. Regional analytic and arithmetic proofs, common inverse and all other old hypotheses remain. Fresh scalar and data-contract checks do not recompute regional polynomials. No physical derivative forcing, global inverse, X3 distance, nonlinear closure or decisive endpoint.'};write(E/'checks.json',value);print(json.dumps({k:value[k] for k in ['utc','status','counts','seconds']}))
if __name__=='__main__':main()
