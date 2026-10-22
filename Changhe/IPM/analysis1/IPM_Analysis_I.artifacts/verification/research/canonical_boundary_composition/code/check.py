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
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_boundary_composition';E=D/'evidence'
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

# These replace the copied generic dependency definitions; no accepted producer is imported.
DEPS={'98':('research/full_green_linkage/evidence/verdict.json','a026f566d277e12ed22b05ec1eb5aadfabe66449940eb3644c96cbe961fbabd5'),'156':('research/canonical_archive_second/evidence/verdict.json','5e5a0879c90afca49df5586e8c602c3b8a990dbea61a5280918646fddb68e75f'),'157':('research/canonical_three_cell_linkage/evidence/verdict.json','094d96a64c1c15d31851de9b6426c94ff437d8de48f99e8229d4316282ef075f')}
EDGES={'radial_tm_instance':'5094d932431eb3abf2a0fedce225d3cd0e15b1ff499f7ef06471d2390710e6db','full_green_linkage':DEPS['98'][1],'full_t_linkage':'3732110a42745c75a1f10cf1e057d0d0d6b81a087bb74e3d9289ef0b0e33635b'}
PART='research/middle_residual/evidence/partition_exact.json';PSHA='56ce08f1b8d0ee7cf2508f23de5c29fff326167332021bdfd21fb5db005612f2';GREEN=str(B.parent/'ipmA-num/data/cert_green.npz');GSHA=EXTERNAL[GREEN]

def identities():
 from math import factorial,comb
 # Direct formal differentiation in a six-symbol Fraction vector space.
 def add(*v):return [sum(x,F(0)) for x in zip(*v,strict=True)]
 def mul(a,v):return [a*x for x in v]
 basis=[[F(int(i==j)) for j in range(6)] for i in range(6)]
 H,G,Hd,Gd,I,J=basis;count=0;dig=hashlib.sha256()
 for n in range(1,262):
  m=2*n;Ip=add(H,mul(-(m+4),I));Jp=add(mul(m-4,J),mul(-1,G));S=mul(F(1,2),add(H,G));Sd=mul(F(1,2),add(Hd,Gd));a=add(S,mul(-m,I));b=add(mul(m,J),mul(-1,S));f=mul(F(1,2),add(mul(4-m,H),mul(4+m,G),Hd,Gd));ap=add(mul(4,a),Sd,mul(-m,Ip));bp=add(mul(4,b),mul(m,Jp),mul(-1,Sd));psi=mul(F(1,2),add(J,mul(-1,I)));psip=add(mul(4,psi),mul(F(1,2),add(Jp,mul(-1,Ip))))
  pairs=[(ap,add(mul(-m,a),f)),(bp,add(mul(m,b),mul(-1,f))),(add(a,b),mul(2*m,psi)),(add(b,mul(-1,a)),mul(2,psip)),(add(bp,mul(-2,b)),add(mul(m-2,b),mul(-1,f))),(add(ap,mul(-2,a)),add(mul(-(m+2),a),f))]
  # Independent fmpq derivation: build the generator matrix, then multiply rows.
  z=fmpq(0);one=fmpq(1);T=[[z for j in range(6)] for i in range(6)];T[0][2]=one;T[1][3]=one;T[4][0]=one;T[4][4]=fmpq(-(m+4));T[5][1]=-one;T[5][5]=fmpq(m-4)
  qa=[fmpq(1,2),fmpq(1,2),z,z,fmpq(-m),z];qb=[fmpq(-1,2),fmpq(-1,2),z,z,z,fmpq(m)];qfvec=[fmpq(4-m,2),fmpq(4+m,2),fmpq(1,2),fmpq(1,2),z,z];qp=[z,z,z,z,fmpq(-1,2),fmpq(1,2)]
  deriv=lambda v:[sum((v[i]*T[i][j] for i in range(6)),z) for j in range(6)]
  da,db,dp=map(deriv,[qa,qb,qp]);qpairs=[([4*qa[j]+da[j] for j in range(6)],[-m*qa[j]+qfvec[j] for j in range(6)]),([4*qb[j]+db[j] for j in range(6)],[m*qb[j]-qfvec[j] for j in range(6)]),([qa[j]+qb[j] for j in range(6)],[2*m*qp[j] for j in range(6)]),([qb[j]-qa[j] for j in range(6)],[8*qp[j]+2*dp[j] for j in range(6)]),([2*qb[j]+db[j] for j in range(6)],[(m-2)*qb[j]-qfvec[j] for j in range(6)]),([2*qa[j]+da[j] for j in range(6)],[-(m+2)*qa[j]+qfvec[j] for j in range(6)])]
  for ident,((lhs,rhs),(ql,qr)) in enumerate(zip(pairs,qpairs,strict=True)):
   need(lhs==rhs and ql==qr and lhs==list(map(qf,ql)),'two independent exact Green identities');count+=6;dig.update(json.dumps([n,ident,list(map(str,lhs))]).encode())
 # Exact normalization jet dependence: direct binomial convolution vs triangular solve.
 src=load(B/SOURCE);alpha=K-3;bo=hx(src['scalars_hex']['bo']);eq=[];jets=[]
 for i in range(7):
  c=-(alpha+bo)**i/factorial(i);recur=(-fmpq(str(alpha))**i-sum((fmpq(comb(i,j))*fmpq(str(-bo))**(i-j)*factorial(j)*eq[j] for j in range(i)),fmpq(0)))/factorial(i);eq.append(recur);need(c==qf(recur),'exact normalized six-jet dependence');jet=alpha**i+sum(comb(i,j)*(-bo)**(i-j)*factorial(j)*(-(alpha+bo)**j/factorial(j)) for j in range(i+1));need(jet==0,'all seven preserved normalized jets');jets.append(str(c))
 return {'modes':261,'identities_per_mode':6,'scalar_coefficients_each_method':count,'coefficient_identity_sha256':dig.hexdigest(),'normalization_jets_each_method':7,'normalization_correction_coefficients_exact':jets,'mode2_zero_rate_included':True}

def main():
 start=now();tic=time.monotonic();pins={};deps={}
 for tag,(name,h) in DEPS.items():pin(pins,name,h);deps[tag]=load(B/name);merge(pins,deps[tag])
 x,y,z=deps['98'],deps['156'],deps['157'];gate156(y)
 need(x['status']=='CONFIRMED_COMPLETE_GREEN_AB_BOUNDARIES_SHARED_CANONICAL_INPUTS' and x['spans']==1558 and x['boundaries']==7810 and x['modes']==261 and x['entries_per_engine']==4076820 and x['recorded_complete_method_comparisons']==8153640 and x['canonical_footer_read'] is True,'actual complete98')
 need(z['status']=='CONFIRMED_THREE_SELECTED_CANONICAL_RADIAL_MODELS_CONDITIONAL_ON_ARCHIVE_MOMENTS' and z['cells']==[0,4102,7808] and z['modes']==261 and z['degree']==12,'actual selected157')
 need({v['topic']:v['verdict_sha256'] for v in z['dependency_verdicts']}==EDGES,'exact93/98/99 direct edges')
 for topic,h in EDGES.items():need(z['files']['research/'+topic+'/evidence/verdict.json']==h,'actual inherited157 verdict pin')
 reviews={'98':review_gate(x,'full_green_actual_complete',x['actual_output_review'],x['postreview_record']),'156':review_gate(y,'canonical_archive_second_actual',y['actual_output_review'],load(B/'research/canonical_archive_second/evidence/postreview_record.json')),'157':review_gate(z,'canonical_three_cell_actual_v2',z['actual_output_review'],z['postreview_record'])}
 for n,h in [(SOURCE,SSHA),(ARCHIVE,ASHA),(ZPATH,ZSHA),(PART,PSHA),(GREEN,GSHA),('research/modal_repair/PROOF.md','9f97fa684956c47bb5b9547f0fe8fabe1df51f036e312dd7022873f8cec37843'),('research/modal_repair/evidence/audit_verdict.json','c17c7f4dfbc86ac789838d59d846f5641cae59577dd8e62987edd31904dab6b8')]:pin(pins,n,h)
 for d in [x,z]:
  need(d['files'][SOURCE]==SSHA and d['files'][ARCHIVE]==ASHA and d['files'][PART]==PSHA,'same whole-box archive and source')
  if ZPATH in d['files']:need(d['files'][ZPATH]==ZSHA,'same directly present normalization slot')
 # Pin and require every source/evidence edge of the accepted normalization audit.
 modal=load(B/'research/modal_repair/evidence/audit_verdict.json');need(modal['verdict']=='CONFIRMED','accepted exact normalization')
 for n,h in modal['source_and_evidence_sha256'].items():pin(pins,n,h)
 for n in ['research/modal_green/PROOF.md','research/full_green_linkage/PROOF.md','research/canonical_three_cell_linkage/PROOF.md','research/canonical_archive_second/PROOF.md','research/canonical_archive_second/ADDENDUM.md','research/canonical_archive_second/POSTREVIEW_ADJUDICATION.md']:pin(pins,n)
 src=load(B/SOURCE);knots=sorted(set(map(hx,src['arrays']['knots']['hex'])));need(len(knots)==1559 and [knots[0],knots[-1]]==JOINS and src['degree']==7 and src['outer_jl'][0]==[0,0],'same exact trial joins/degree/normalization attachment');need(hx(src['scalars_hex']['k'])==K and hx(src['scalars_hex']['L'])==L,'same exact k,L')
 need(len(src['outer_jl'])==10 and len({tuple(v) for v in src['outer_jl']})==10 and all(len(v)==2 and all(type(i)is int and i>=0 for i in v) for v in src['outer_jl']),'all exact outer index pairs')
 zn=load(B/ZPATH)['values']['A00_correction'];Z=[str(ff(zn[k])) for k in ['lower_exact_dyadic','upper_exact_dyadic']];need(F(Z[0])<=F(Z[1]),'ordered common normalization Z')
 part=load(B/PART);need(part['schema']=='ipm-middle-partition-v1' and part['input_sha256']==SSHA and part['grid_sha256']==GSHA and part['cells']==7809 and len(part['spans'])==1558,'complete exact common partition')
 afile=B/'research/canonical_archive_second/evidence/full_spans.jsonl';glines=(B/'research/full_green_linkage/evidence/full_spans.jsonl').read_bytes().splitlines(keepends=True);alines=afile.read_bytes().splitlines(keepends=True)
 need(len(glines)==1560 and len(alines)==3118 and all(l.endswith(b'\n') for l in glines+alines),'complete accepted finite streams');gh=parse(glines[0]);gf=parse(glines[-1]);ah=parse(alines[0]);af=parse(alines[-1]);fw=[parse(v) for v in alines[1:1559]];bw=[parse(v) for v in alines[1559:-1]]
 need(ah['type']=='header' and ah['full_run'] is True and ah['source_sha256']==SSHA and ah['archive_sha256']==ASHA and ah['normalization_sha256']==ZSHA and ah['Z_exact']==Z,'same exact accepted156 normalized tuple')
 need(af['type']=='complete' and af['counts']==y['counts'] and af['prefix_sha256']==hashlib.sha256(b''.join(alines[:-1])).hexdigest(),'complete156stream digest/counters')
 need([r['span'] for r in fw]==list(range(1558)) and [r['span'] for r in bw]==list(range(1557,-1,-1)),'complete original span orders');bw.reverse()
 need(gh['type']=='header' and gh['full_run'] is True and gh['expected_boundaries']==7810 and gh['expected_spans']==1558 and gh['green_sha256']==GSHA and gh['selected_spans']==list(range(1558)),'complete98header')
 need(gh['files'][SOURCE]==SSHA and gh['files'][ARCHIVE]==ASHA and gh['files'][PART]==PSHA,'exact98 premise identity');need(gf['type']=='complete' and gf['spans']==1558 and gf['boundaries']==7810,'complete98footer')
 counts={'spans':0,'child_cells':0,'boundaries':0,'H_shapes':0,'moment_shapes':0,'zero_H_coefficients_two_routes':0,'zero_J_targets_two_routes':0,'original_row_hashes':0,'green_counts_each_engine':0,'selected_green_coordinates':0};boundaries=[];parents=[];zeroJ=[]
 with gzip.open(B/ARCHIVE,'rt') as f:
  h=parse(next(f));need(h['hashes']['input']==SSHA and h['hashes']['normalization']==ZSHA and h['comparison_grid_sha256']==GSHA and h['scalars_exact']['k']==str(K) and h['scalars_exact']['L']==str(L),'same original scalar header')
  for i in range(1558):
   line=next(f);need(line.endswith('\n'),'complete original row');r=parse(line);g=parse(glines[i+1]);a,b=knots[i:i+2];p=part['spans'][i];c=p['count'];first=p['first_cell'];need(type(c)is int and c>0 and first==counts['child_cells'],'positive contiguous partition')
   for row in [r,g,p,fw[i],bw[i]]:need(row['span']==i and ff(row['a_exact'])==a and ff(row['b_exact'])==b,'same exact span five ways')
   need(r['type']=='span' and g['type']=='span' and fw[i]['type']=='forward' and bw[i]['type']=='backward','all typed rows');need(r['count']==g['count']==c and r['first_cell']==g['first_cell']==first and ff(r['polynomial_mid_exact'])==(a+b)/2,'same exact midpoint/subdivision')
   need(fw[i]['archive_line_sha256']==hashlib.sha256(line.encode()).hexdigest() and fw[i]['H_count']==2096 and fw[i]['comparisons']==bw[i]['comparisons']==261,'156same actual full original record');counts['original_row_hashes']+=1
   need(len(r['density_polynomials'])==262 and all(len(v)==8 for v in r['density_polynomials']) and len(r['i_left'])==len(r['j_right'])==261,'all original finite arrays')
   for v in r['density_polynomials'][261]:need(ball(v)==(F(0),F(0)),'exact highest zero H');counts['zero_H_coefficients_two_routes']+=1
   need(ball(r['j_right'][260])==(F(0),F(0)),'exact zero-radius highest J');counts['zero_J_targets_two_routes']+=1
   saved=next(v for v in bw[i]['samples'] if v['mode']==261);need(saved['family']=='J' and saved['span']==i and list(map(ff,saved['target']))==[F(0),F(0)] and list(map(ff,saved['candidate']))==[F(0),F(0)],'actual156 exact point target result');zeroJ.append(i)
   nb=c+int(i==1557);need(g['boundaries']==nb and not g['failures'] and g['counts']=={key:{'CONTAINED':nb*261} for key in ['A/arb','A/iv','B/arb','B/iv']},'all actual98 positive memberships');counts['green_counts_each_engine']+=2*nb*261
   local=[a+(b-a)*F(j,c) for j in range(nb)]
   # Second exact formula computes numerator before dividing, in fmpq.
   other=[qf((fmpq(str(a))*(c-j)+fmpq(str(b))*j)/c) for j in range(nb)];need(local==other,'all exact rational boundaries two methods')
   for v in g['selected_records']:need(first<=v['boundary']<first+nb and ff(v['t_exact'])==local[v['boundary']-first],'every saved98 selected coordinate');counts['selected_green_coordinates']+=1
   boundaries+=local;parents += [i]*c;counts['spans']+=1;counts['child_cells']+=c;counts['boundaries']+=nb;counts['H_shapes']+=2096;counts['moment_shapes']+=522
  tail=parse(next(f));need(tail['type']=='complete' and tail['spans']==1558 and tail['cells']==7809 and not f.read(),'complete original archive footer')
 need(counts['spans']==1558 and counts['child_cells']==7809 and len(boundaries)==counts['boundaries']==7810 and counts['green_counts_each_engine']==4076820 and counts['H_shapes']==3265568 and counts['moment_shapes']==813276 and len(zeroJ)==1558,'all complete counters');need(all(a<b for a,b in zip(boundaries,boundaries[1:])),'strict exact child partition')
 selected=load(B/'research/canonical_three_cell_linkage/evidence/checks.json');need(sha(B/'research/canonical_three_cell_linkage/evidence/checks.json')==z['checks_sha256'],'accepted actual157 checks');need([v['cell'] for v in selected['cells']]==[0,4102,7808],'exact three cells');actual=[];ctx.prec=512;ctx.threads=1;iv.dps=170
 for row in selected['cells']:
  c=row['cell'];a,b=boundaries[c:c+2];need([ff(row['left_exact']),ff(row['right_exact'])]==[a,b] and row['parent']==parents[c] and ff(row['length_exact'])==b-a<=ff(row['h_upper_exact']),'same selected interval and h bound')
  recs=row['E'];need([v['engine'] for v in recs]==['arb640','iv200'],'two original directedE records');targets=[]
  for v in recs:
   lo,hi,tl,th=map(ff,[v['lower'],v['upper'],v['target_lower'],v['target_upper']]);need(0<tl<=lo<=hi<=th,'accepted exact E containment');targets.append([tl,th])
  need(targets[0]==targets[1],'same target E both engines');target=targets[0];fresh=[ae(ai(a).exp()),list(map(iep,iv.exp(ii(a))._mpi_))]
  for interval in fresh:need(target[0]<=interval[0]<=interval[1]<=target[1],'fresh current exact E containment')
  candidate='research/radial_tm_instance/evidence/selected_v3_cell_'+str(c).zfill(4)+'.npz';need(z['files'][candidate]==row['saved_candidate_sha256'],'same actual named candidate');pin(pins,candidate,row['saved_candidate_sha256']);actual.append({'cell':c,'parent':parents[c],'left_exact':str(a),'right_exact':str(b),'h_upper_exact':row['h_upper_exact'],'E_target_exact':list(map(str,target)),'fresh_arb512_exact':list(map(str,fresh[0])),'fresh_iv170_exact':list(map(str,fresh[1])),'candidate_sha256':row['saved_candidate_sha256']})
 symbolic=identities();pr=load(E/'proof_first.json');need(pr['sha256']==sha(D/'PROOF.md') and datetime.fromisoformat(pr['utc'])<datetime.fromisoformat(start),'proof before code/check')
 for n in ['PROOF.md','REVIEW_RESOLUTION.md','code/check.py','evidence/proof_first.json']:pin(pins,D/n)
 for n,h in pins.items():need(sha(B/n)==h,'all final unchanged dependencies')
 result={'start_utc':start,'utc':now(),'status':'PASS_CANONICAL_BOUNDARIES_AND_THREE_RADIAL_CELLS_COMPOSITION_REQUIRES_ACTUAL_REVIEW','accepted_dependencies':{tag:{'path':p,'sha256':h,'utc':deps[tag]['utc']} for tag,(p,h) in DEPS.items()},'dependency_reviews':reviews,'source_sha256':SSHA,'archive_sha256':ASHA,'normalization_sha256':ZSHA,'Z_exact':Z,'k_exact':str(K),'L_exact':str(L),'partition_sha256':PSHA,'green_sha256':GSHA,'counts':counts,'symbolic_checks':symbolic,'three_cells':actual,'direct157_dependencies':EDGES,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tic,'scope':'Discharge only the canonical archive premise of98 all7810boundaries/all261modes and157 cells0,4102,7808/all261 degree12models, for the distinguished exactly normalized trial. All prior analytic/arithmetic hypotheses, order20 remainder refinement and runtime-only qualification retained. No162full result, historical array transfer, physical forcing/inverse/X3/nonlinear endpoint.'};write(E/'checks.json',result);print(json.dumps({k:result[k] for k in ['utc','status','counts','symbolic_checks','seconds']}))
if __name__=='__main__':main()
