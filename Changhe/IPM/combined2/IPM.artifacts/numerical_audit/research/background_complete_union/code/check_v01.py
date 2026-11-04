"""Exact whole-plane assembly of separately adopted Source013 background bounds."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import argparse, json, os, sys, time
R=Path(__file__).resolve().parents[3];D=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'scripts'))
from campaign_bindings_v01 import Bindings, digest, named, P
p=argparse.ArgumentParser()
for key in ['host-adoption','host-sha256','matrix-adoption','matrix-sha256','output']:p.add_argument('--'+key,required=True)
a=p.parse_args();assert Path.cwd().resolve()==R
assert os.sched_getaffinity(0)=={50} and os.getpriority(os.PRIO_PROCESS,0)>=19
start=datetime.now(timezone.utc);tick=time.monotonic();b=Bindings();checks=0
out=named(R,a.output);assert out.parent==D/'verification' and not out.exists()
def ck(ok,why):
 global checks
 checks+=1;assert ok,why
def read(path,expected=None):
 b.add(path,expected);return json.loads(path.read_text())
def maps(data,base,keys):
 for key in keys:ck(key in data,'required complete map');b.mapping(base,data[key])
def coverage(indices):
 J=sorted(set(indices));ck(all(type(j)is int and 0<=j<128 for j in J),'valid radial indices')
 runs=[]
 for j in J:
  if not runs or j>runs[-1][1]+1:runs.append([j,j])
  else:runs[-1][1]=j
 intervals=[(Q(l,128),Q(r+1,128))for l,r in runs]
 for k in range(257):
  x=Q(k,256);ck(any(Q(j,128)<=x<=Q(j+1,128)for j in J)==any(l<=x<=r for l,r in intervals),'exact interval membership')
 def radial(t):return 'infinity' if t==1 else str(t/(1-t))
 gaps=[(intervals[k][1],intervals[k+1][0])for k in range(len(intervals)-1)]
 return dict(roots=J,distinct_indices=len(J),t_closed_components=[[str(l),str(r)]for l,r in intervals],r_squared_components=[[radial(l),radial(r)]for l,r in intervals],r_squared_open_gaps=[[radial(l),radial(r)]for l,r in gaps],whole_plane=J==list(range(128)),terminal_endpoint_convention='t=1 is a formal endpoint, not a finite point')
old=read(R/'research/background_progressive_union/verification/check_v03.json','bdb371df60185c9d6ca4f4d15d1e7c6f6c0a227f6b5fab68b0eb58c452f20bae')
oldad=read(R/'research/background_progressive_union/verification/actual_review_v03.json','69f72291b1d165b8ffc6eab439597daad94b9df79e274c4051966587e5498901')
ck(old['status']=='CONFIRMED_EXACT_PROGRESSIVE_UNION' and oldad['status']=='CONFIRMED_EXTERNAL_REVIEW' and oldad['kind']=='union60','adopted previous union')
ck(oldad['owner_union_sha256']==digest(R/'research/background_progressive_union/verification/check_v03.json'),'adopted exact old result')
ck(oldad['coverage']==old['coverage'],'old coverage agrees')
ck(old['source']['raw_sha256']=='a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a','fixed raw source')
ck(old['source']['fields_sha256']=='3d5f08e06859af2577f6e099374a8ce5e139a0b66280055ada847745943bf8cb','fixed complete field')
ck(old['source']['fixed_c_exact']=='4076476460239181/2251799813685248','fixed parameter')
maps(old,R,['files']);maps(oldad,R,['files','external_bindings'])
inner=read(R/'research/background_matrix_margin_recount/verification/actual_balanced_review_v02.json','76e620f4a5b57f2c9fbcc1502281cf561ca208707c84f8259e6c8908ca885ab4')
ordinary=read(R/'research/background_matrix_margin_recount/verification/actual_review_v01.json','e4fa4cac2540b2557bc69165e85c80a1d07bf830e5cbbe3332ec39425bed08e0')
outer=read(R/'research/background_matrix_margin_recount/verification/actual_rectangular_review_v01.json','d6e611eff7c48555dd3a49e86b97caf1af7e39047d0c3c39c147f6fc5385e463')
ck(inner['status']=='CONFIRMED_EXTERNAL_REVIEW' and inner['kind']=='balanced','inner actual adoption')
ck(ordinary['status']==outer['status']=='CONFIRMED_EXTERNAL_MATRIX_MARGIN_REVIEW','regional actual matrix adoptions')
for z in [inner,ordinary]:maps(z,R,['files','external_bindings'])
maps(outer,R,['own_bindings','external_bindings'])
ck(inner['combined_inner']['indices']==list(range(61)),'complete inner indices')
ck(inner['combined_inner']['r_squared_component']==['0','61/67'],'inner domain')
ck(outer['combined_exterior']['r_squared_interval']==['49/15','infinity'],'outer domain')
beta_in=Q(inner['combined_inner']['lower']);beta_out=Q(outer['combined_exterior']['lower'])
ck(beta_in==Q(704955805507,10**12) and beta_out==Q(761272835221,10**12),'regional constants')
hp=named(R,a.host_adoption);mp=named(R,a.matrix_adoption)
ck(hp==R/'research/ordinary_slabs_host_method/verification/actual_review_v01.json','fixed host adoption path')
ck(mp==R/'research/ordinary_host_matrix_margin/verification/actual_review_v01.json','fixed matrix adoption path')
had=read(hp,a.host_sha256);mad=read(mp,a.matrix_sha256)
ck(had['status']=='CONFIRMED_EXTERNAL_HOST_RECOUNT_REVIEW','complete actual host review')
ck(mad['status']=='CONFIRMED_EXTERNAL_HOST_MATRIX_REVIEW','complete actual matrix review')
for z in [had,mad]:maps(z,R,['files','external_dependencies'])
hr=R/'research/ordinary_slabs_host_method/verification/recount_v01.json';mr=R/'research/ordinary_host_matrix_margin/verification/check_v01.json'
host=read(hr,had['result_sha256']);matrix=read(mr,mad['result_sha256'])
ck(host['status']=='CONFIRMED_RECOUNT' and matrix['status']=='CONDITIONAL_EXACT_HOST_MATRIX_RECOUNT','completed host outputs')
ck(matrix['recount_sha256']==digest(hr),'matrix built on exact host recount')
for z,folder in [(had,'ordinary_slabs_host_method'),(mad,'ordinary_host_matrix_margin')]:
 e=read(R/f'research/{folder}/verification/execution_v01.json',z['execution_sha256'])
 ck(e['status']=='COMPLETED' and e['exit_code']==0 and e['reason']is None and e['inputs_unchanged'],'successful complete local execution')
 ck(e['old_process_signals']==0 and not e['own_child_signals'],'no interrupted local run')
 ck(e['output_sha256']==z['result_sha256'],'receipt output identity')
 b.mapping(R,e['bindings'])
b.mapping(P,host['bindings']);maps(matrix,R,['files','external_bindings'])
J=list(range(97,55,-1));ck([x['root_index']for x in host['slabs']]==J,'all 42 host slabs')
ck([x['index']for x in matrix['regions']]==J,'all 42 matrix slabs')
selected={x['index']:dict(x['flags'])for x in old['selected']}
ck(sorted(selected)==list(range(61))+list(range(98,128)),'exact old mask')
host_lowers=[]
for h,m in zip(host['slabs'],matrix['regions']):
 j=h['root_index'];domain=[str(Q(j,128-j)),str(Q(j+1,127-j))]
 ck(h['domain_r_squared']==m['domain_r_squared']==domain,'exact matching domains')
 ck(h['cell_count']==m['cell_count']==8192,'complete product cells')
 ck(h['joint_flags']['small_strain']is True,'joint weak gradient and small strain')
 ck(all(type(v)is bool for v in h['joint_flags'].values()),'boolean predicates')
 v=Q(m['outward_lower_exact']);ck(v>=Q(3,5),'matrix lower meets coarse target');host_lowers.append(v)
 selected[j]=dict(h['joint_flags'])
weak=coverage([j for j,f in selected.items()if f['small_strain']])
strong=coverage([j for j,f in selected.items()if f['both_small']])
ck(weak['whole_plane'],'complete joint weak cover')
ck(matrix['union_r_squared']==['7/9','49/15'],'complete matrix host domain')
ck(min(host_lowers)==Q(matrix['minimum_outward_lower_exact']),'host minimum')
beta=min(beta_in,beta_out,*host_lowers)
if all(h['joint_flags']['both_small']for h in host['slabs']):
 ck(strong['roots']==[j for j in range(128)if j not in [98,100,102,104]],'exact stronger mask')
for p in [D/'PROOF.md',D/'CONSUMER_PROTOCOL_v01.md',Path(__file__),R/'scripts/campaign_bindings_v01.py']:b.add(p)
b.recheck()
z=dict(status='ASSEMBLED_COMPLETE_BACKGROUND_PENDING_DISTINCT_REVIEW',started_utc=start.isoformat(),finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,arithmetic_checks=checks,binding_checks=b.checks,source=old['source'],global_bounds=dict(matrix_lower=str(beta),gradient_upper='1/4',strain_operator_upper='137/125'),matrix_components=dict(inner_lower=str(beta_in),host_lower=str(min(host_lowers)),outer_lower=str(beta_out)),coverage=dict(gradient_1_4=weak,gradient_71_500=strong),selected=[dict(index=j,flags=selected[j])for j in sorted(selected)],host_adoption_sha256=a.host_sha256,matrix_adoption_sha256=a.matrix_sha256,files=b.own(),external_dependencies=b.external(),scope='Exact union of actually adopted regional bounds under their imported source and containing-arithmetic hypotheses. Whole-plane background only; no near energy, H4 remainder, full inverse, invariant ball or existence theorem.')
with out.open('x')as f:json.dump(z,f,indent=2);f.write('\n')
print('COMPLETE_BACKGROUND_ASSEMBLED',str(beta),checks,b.checks,z['elapsed_seconds'],flush=True)
