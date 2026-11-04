"""Independent rational audit of the seven-region near assembly and NR25 inputs."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from flint import arb, ctx
import json, os, sys, time
R=Path(__file__).resolve().parents[3];D=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'scripts'))
from campaign_bindings_v01 import Bindings,digest,named
assert os.sched_getaffinity(0)=={50} and os.getpriority(os.PRIO_PROCESS,0)>=19
assert all(os.environ.get(k)=='1' for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'])
sys.set_int_max_str_digits(0)
start=datetime.now(timezone.utc);tick=time.monotonic();B=Bindings();checks=0

def ck(ok,label):
 global checks
 checks+=1;assert ok,label

def read(p,h=None):B.add(p,h);return json.loads(p.read_text())
def dt(s):
 z=datetime.fromisoformat(s.replace('Z','+00:00'));ck(z.utcoffset().total_seconds()==0,'UTC');return z

def maps(z):
 for k in ['files','own_bindings','external_bindings','external_dependencies']:
  if k in z:B.mapping(R,z[k])

def exact(s):
 ck(isinstance(s,str),'rational string');q=Q(s);ck(str(q)==s,'canonical rational');return q

def energies(rows):
 ck([z['order'] for z in rows]==[4,5,6],'energy orders');out={}
 for z in rows:
  lo,hi=exact(z['lower_exact']),exact(z['upper_exact']);ck(0<=lo<=hi,'containing nonnegative interval');out[z['order']]=(lo,hi)
 return out

xp=R/'research/source013_near_norms/verification/wholeplane_v02/result.json'
ep=R/'research/finite_long_preparation/verification/assemble_source013_wholeplane_near_norms_v02/execution.json'
x=read(xp);e=read(ep)
ck(x['schema']=='source013-wholeplane-near-norms-v1' and x['status']=='ADMITTED_WHOLEPLANE_NEAR_NORMS','actual schema')
ck(e['status']=='COMPLETED' and e['reason'] is None and e['old_process_signals']==0,'original successful receipt')
ck(e['method_manifest_sha256']=='4bb8d2adf05b2a16ad09067e88cf1c24e714e6529222746985e12183895d99bb','finite method')
ck(e['method_review_sha256']=='b45103ffd8b6a5f86d80fde7ad709e6873f395465fb6ad94f0114eaef3a2bfd2','finite method review')
q=read(named(R,e['request']),e['request_sha256']);app=read(named(R,x['request']),x['request_sha256'])
number=int(Path(e['request']).stem.removeprefix('preparation_request_v'))
rp=R/f'research/finite_long_preparation/verification/request_review_{number}_v01.json'
qr=read(rp,e['execution_review_sha256'])
ck(qr['status']=='BOUND' and qr['request_sha256']==e['request_sha256'],'actual concrete request adoption')
ck(qr['method_manifest_sha256']==e['method_manifest_sha256'] and qr['method_review_sha256']==e['method_review_sha256'],'same admitted gate')
ck(qr['own_bindings'][e['request']]==e['request_sha256'],'concrete adoption binds outer request')
ck(dt(qr['received_utc'])<=dt(e['started_utc']),'concrete adoption precedes execution')
maps(qr)
ck(app['schema']=='source013-near-norms-request-v1' and app['source']==x['source'],'application source')
ck(len(q['stages'])==len(e['stages'])==1,'single stage')
ck(q['stages'][0]['limit_seconds']==480 and e['stages'][0]['exit_code']==0,'successful finite stage')
ck(q['stages'][0]['argv']==e['stages'][0]['argv']==['-B','research/source013_near_norms/code/assemble_v03.py','--request',x['request'],'--request-sha256',x['request_sha256']],'exact execution')
ck(dt(q['created_utc'])<=dt(e['started_utc'])<=dt(x['started_utc'])<=dt(x['finished_utc'])<=dt(e['finished_utc'])<=start,'execution chronology')
ck(x['method_sha256']=='903ef7381a7b8b10d5c87900ad9894af3e2771e4338428b159f1c98473860e56','near method')
ck(x['review_sha256']=='d0a7a1bd5bf51f8b78d76cc226f873856f62f274762019aa9e0c600d43a1397a','near review')
method=read(R/'research/source013_near_norms/verification/manifest_v02.json',x['method_sha256'])
ck(x['source']==method['source'] and x['panel_count']==561,'fixed complete source')
ck(x['input_files']==app['files'],'method input identity')
ck(x['code_sha256']==method['files']['research/source013_near_norms/code/assemble_v03.py'],'actual admitted consumer code')
ck(x['blocks']==app['blocks'] and x['endpoints']==app['endpoints'],'identical regional selection')
ck([b['job'] for b in x['blocks']]==['n0','n1','n2','n3','n4'],'five ordered owners')
regions=[];seen=[];region_names=[]
for i,b in enumerate(x['blocks']):
 z=read(named(R,b['result']),b['sha256']);ar=read(named(R,b['actual_review']),b['actual_review_sha256']);er=read(named(R,b['execution']),b['execution_sha256'])
 indices=list(range(i,561,5));seen+=indices
 ck(z['status']=='ADMITTED_NEAR_BLOCK' and z['job']==b['job'] and z['source']==x['source'],'containing regional source')
 ck(z['block']['indices']==indices and z['panel_count']==len(indices) and z['complete_requested_assignment'] is True,'complete owner assignment')
 ck(ar['status']=='BOUND' and ar['result_sha256']==b['sha256'] and ar['execution_sha256']==b['execution_sha256'],'actual block adoption')
 ck(ar['own_bindings'][b['result']]==b['sha256'] and ar['own_bindings'][b['execution']]==b['execution_sha256'],'adoption byte bindings')
 ck(er['status']=='COMPLETED' and er['reason'] is None and er['old_process_signals']==0,'block receipt')
 ck(ar['request_sha256']==er['request_sha256'],'same actual block request')
 ck(dt(er['finished_utc'])<=dt(ar['received_utc'])<=dt(e['started_utc']),'block chronology')
 maps(ar);regions.append(energies(z['laplacian_energies']));region_names.append(b['job'])
ck(sorted(seen)==list(range(561)),'partition of middle annulus')
for region in ['origin','exterior']:
 b=x['endpoints'][region];pr=read(named(R,b['primary']),b['primary_sha256']);z=read(named(R,b['reduction']),b['reduction_sha256']);ar=read(named(R,b['actual_review']),b['actual_review_sha256'])
 ck(pr['source']==z['source']==x['source'],'endpoint source')
 ck(z['status']=='LOCAL_NEAR_ENDPOINT_COMPUTED' and z['region']==region and z['kind']=='reduction','endpoint reduction')
 ck(z['primary_sha256']==b['primary_sha256'],'same endpoint primary')
 ck(z['geometry'][region]['radius_exact']==('1/4096' if region=='origin' else '10000'),'exact boundary radius')
 ck(ar['status']=='BOUND' and ar['primary_sha256']==b['primary_sha256'] and ar['reduction_sha256']==b['reduction_sha256'],'actual endpoint adoption')
 for k in ['primary','reduction','primary_execution','reduction_execution']:
  B.add(named(R,b[k]),b[k+'_sha256']);ck(ar['own_bindings'][b[k]]==b[k+'_sha256'],'endpoint adopted byte')
 maps(ar);regions.append(energies(z['containing_intersections']));region_names.append(region)
ck([z['order'] for z in x['norms']]==[4,5,6],'norm orders');grid=Q(1,10**24);upper={};energy={}
for z in x['norms']:
 j=z['order'];lo=sum((r[j][0] for r in regions),Q(0));hi=sum((r[j][1] for r in regions),Q(0))
 ck(lo==exact(z['energy_lower_exact']) and hi==exact(z['energy_upper_exact']),'independent seven region sum')
 a,b=Q(z['norm_lower_decimal']),Q(z['norm_upper_decimal']);ck(0<=a<=b and a*a<=lo<=hi<b*b,'outward norm interval')
 ck((a+grid)**2>=lo and (b-grid)**2<=hi,'norm display resolution');upper[j]=b;energy[j]=hi
ctx.prec=512;p=arb.pi();pl,ph=map(exact,x['pi_interval_exact'])
ck(3<pl<=Q(str(p.lower().fmpq()))<=Q(str(p.upper().fmpq()))<=ph<4,'independent pi containment')
m=x['moment_inputs'];ck(exact(m['pi_lower_exact'])==pl,'same pi lower')
ck(m['fourier_normalization']=='(2*pi)^(-2) with nonunitary forward transform','NR25 normalization')
options=[(upper[4]*upper[6]+upper[5]**2)/(2*pl),upper[4]*upper[6]/pl]
ck(list(map(exact,m['M4_squared_upper_options_exact']))==options,'independent M4 alternatives')
small=min(options);ck(exact(m['M4_squared_upper_exact'])==small,'M4 minimum');v=Q(m['M4_upper_decimal'])
ck(v>=grid and (v-grid)**2<=small<v*v,'outward M4 root')
expected=[(Q(mu),ratio) for mu in ['41','83/2','42','45','46','48','52','56','64','80'] for ratio in [Q(1,2),Q(3,4)]]
ck(len(m['tail_rows'])==len(expected),'all tail rows');compact=[]
for row,(mu,ratio) in zip(m['tail_rows'],expected):
 v=mu*ratio;ck(exact(row['mu_exact'])==mu and exact(row['threshold_ratio_exact'])==ratio and exact(row['threshold_exact'])==v and row['p_exact']=='21/10','exact tail parameters')
 ck([r['derivative_order'] for r in row['methods']]==[4,5,6],'three tail alternatives');choices=[]
 for z in row['methods']:
  j=z['derivative_order'];bound=(energy[j]/(4*pl*(Q(j)-Q(31,10))))**5*v**(31-10*j);t=Q(z['tail_upper_decimal'])
  ck(exact(z['tenth_power_upper_exact'])==bound,'independent tenth power formula')
  ck(t>=grid and (t-grid)**10<=bound<t**10,'outward tenth root');choices.append((t,j))
 chosen=min(choices);ck(Q(row['tail_upper_decimal'])==chosen[0] and row['chosen_derivative_order']==chosen[1],'minimum valid tail upper')
 compact.append(dict(mu=str(mu),ratio=str(ratio),upper=row['tail_upper_decimal'],order=chosen[1]))
for z in [q,app,x,method]:maps(z)
for path in [D/'PROOF.md',D/'formal/README.md',D/'code/run_v01.py',Path(__file__),R/'scripts/campaign_bindings_v01.py']:B.add(path)
B.recheck()
out=dict(status='PASS_INDEPENDENT_WHOLEPLANE_ARITHMETIC',started_utc=start.isoformat(),finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,arithmetic_checks=checks,binding_checks=B.checks,source=x['source'],result_sha256=digest(xp),execution_sha256=digest(ep),regions=region_names,panel_count=len(seen),norms=x['norms'],M4_upper_decimal=m['M4_upper_decimal'],tail_rows=compact,pi_check_precision=ctx.prec,own_bindings=B.own(),external_dependencies=B.external(),data_symlink_aliases=B.symlinks,scope='Independent arithmetic and provenance audit under the accepted containing regional theorems. No new field evaluation or full near price. Distinct actual review remains required.')
with (D/'verification/check_v01.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['status'],checks,B.checks,out['elapsed_seconds'],digest(D/'verification/check_v01.json'),flush=True)
