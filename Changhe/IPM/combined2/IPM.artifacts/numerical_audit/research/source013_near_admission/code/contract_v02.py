"""Exact owner provenance and complete near-panel record checks."""
from datetime import datetime,timezone
from fractions import Fraction as F
from pathlib import PurePosixPath
import math
STOP=datetime(2026,11,4,17,5,30,tzinfo=timezone.utc).timestamp()
CUTOFF=STOP-30
BASE='research/source013_near_cover'
MH='12f6e7a83345efa16bc98e45f77f87896b832a35015715444c069ea26a72897a'
RH='19560908574a48853e67dfe184502396e326430130651cc0177868a6dc02f18e'
CHECKS=0

def need(value,label=''):
 global CHECKS
 assert value,label
 CHECKS+=1

def instant(text):
 need(isinstance(text,str)and text.endswith('Z'),'UTC time required')
 value=datetime.fromisoformat(text.replace('Z','+00:00'))
 need(value.utcoffset().total_seconds()==0)
 return value.timestamp()

def measured(record):
 begin,end=instant(record['started_utc']),instant(record['finished_utc'])
 elapsed=record['elapsed_seconds']
 need(type(elapsed)in[int,float]and math.isfinite(elapsed)and elapsed>=0)
 need(begin<=end<=STOP and begin<CUTOFF)
 need(abs((end-begin)-elapsed)<5,'Recorded elapsed time disagrees with wall time')
 return begin,end

def path(name):
 need(isinstance(name,str)and name and '\\'not in name)
 p=PurePosixPath(name)
 need(not p.is_absolute()and '..'not in p.parts and str(p)==name)
 return p

def receipt(manifest,job,installation,execution,result,result_hash):
 need(manifest['schema']=='source013-near-cover-deployment-v1')
 need(job in manifest['jobs']and job['id']in['n0','n1','n2','n3','n4'])
 for record in[installation,execution,result]:
  need(record['job']==job['id']and record['owner']==job['owner'])
  need(type(record['cpu'])is int and record['cpu']==job['cpu'])
  need(record['manifest_sha256']==MH)
 need(installation['review_sha256']==execution['review_sha256']==RH)
 need(installation['worker_root']==BASE+'/worker_'+job['id'])
 need(execution['schema']=='source013-near-cover-deployment-execution-v1')
 need(execution['status']=='COMPLETED'and type(execution['exit_code'])is int and execution['exit_code']==0)
 need(execution['stop_reason']is None and execution['result_sha256']==result_hash)
 need(execution['guard_sha256']==manifest['files'][BASE+'/code/guard_v01.py'])
 need(result['schema']=='source013-near-cover-deployment-result-v1'and result['status']=='COMPLETED')
 need(result['block']==job and result['source']==manifest['source']and result['parameters']==manifest['parameters'])
 need(result['complete_requested_assignment']is True)
 need(result['source_admission_sha256']==manifest['files'][manifest['source_admission']])
 need(result['source_archive_sha256']==manifest['files'][manifest['source_archive']])
 need(result['code_sha256']==manifest['files'][BASE+'/code/worker_v01.py'])
 need(result['input_files']==manifest['files'])
 executed=result['executed_local_code']
 need(isinstance(executed,list)and executed==sorted(set(executed)))
 need(BASE+'/code/worker_v01.py'in executed and BASE+'/code/panel_kernel_v01.py'in executed)
 need(set(executed)<=set(manifest['copied_code']))
 installed=instant(installation['installed_utc']);eb,ee=measured(execution);rb,re=measured(result)
 need(installed<=eb<=rb<=re<=ee)
 resources=execution['initial_resources']
 need(type(resources['owner_lane_bytes'])is int and 0<=resources['owner_lane_bytes']<2_950_000_000)
 need(type(resources['filesystem_free_bytes'])is int and resources['filesystem_free_bytes']>=20_000_000_000)
 rows=result['panels'];need(isinstance(rows,list)and len(rows)==len(job['indices']))
 need([row['index']for row in rows]==job['indices'])
 for row in rows:
  need(type(row['index'])is int and path(row['path'])==PurePosixPath(f"output/panel_{row['index']:05d}.json.gz"))
  need(isinstance(row['sha256'],str)and len(row['sha256'])==64 and all(c in'0123456789abcdef'for c in row['sha256']))
  need(type(row['bytes'])is int and row['bytes']>0)
  for key in['primary_seconds','reduction_seconds']:
   need(type(row[key])in[int,float]and math.isfinite(row[key])and row[key]>=0)
 need([row['order']for row in result['laplacian_energies']]==[4,5,6])
 for row in result['laplacian_energies']:need(0<=F(row['lower_exact'])<=F(row['upper_exact']))
 return{'receipt_checks':CHECKS,'ordered_actual_times':True,'complete_assignment':True}

def panel(pair,plan,index,manifest,job,parent,metadata):
 need(pair['schema']=='source013-near-panel-pair-v1'and type(pair['panel_index'])is int and pair['panel_index']==index)
 expected=plan[index];need(pair['panel']==expected and metadata['panel_id']==expected['panel_id'])
 need(index in job['indices']and metadata['index']==index)
 identity={'source':manifest['source'],'source_admission_sha256':manifest['files'][manifest['source_admission']],
           'source_archive_sha256':manifest['files'][manifest['source_archive']],'manifest_sha256':MH,'job':job['id']}
 for key,value in identity.items():need(pair[key]==value,key)
 times=[]
 for kind,bits in[('primary',1024),('reduction',1536)]:
  row=pair[kind]
  need(row['status']=='LOCAL_NEAR_ENERGY_COMPUTED'and row['kind']==kind and row['precision_bits']==bits)
  need(row['panel']==expected and row['panel_id']==expected['panel_id'])
  for key,value in identity.items():need(row[key]==value,key)
  need(row['bandwidth']==160 and F(row['bound_E_upper_exact'])>0)
  need(row['code_sha256']==manifest['files'][BASE+'/code/panel_kernel_v01.py'])
  need(row['proof_sha256']==manifest['files'][BASE+'/APPLICATION_PROOF_v01.md'])
  need(row['elapsed_seconds']==metadata[kind+'_seconds'])
  need(type(row['generation_seconds'])in[int,float]and 0<=row['generation_seconds']<=row['elapsed_seconds'])
  times.extend(measured(row))
 need(times==sorted(times))
 need(instant(parent['started_utc'])<=times[0]<=times[-1]<=instant(parent['finished_utc']))
 intersections=[]
 for order in[4,5,6]:
  pc=pair['primary']['energy_coefficients'][str(order)];rc=pair['reduction']['energy_coefficients'][str(order)]
  need(len(pc)==len(rc)==129)
  for pp,rr in zip(pc,rc,strict=True):
   need(isinstance(pp,list)and isinstance(rr,list)and len(pp)==len(rr)==2)
   pl,pu,rl,ru=map(F,[*pp,*rr]);need(pl<=pu and rl<=ru and max(pl,rl)<=min(pu,ru))
  p=pair['primary']['laplacian_energies'][order-4];r=pair['reduction']['laplacian_energies'][order-4]
  need(type(p['order'])is int and p['order']==r['order']==order)
  pl,pu,rl,ru=map(F,[p['lower_exact'],p['upper_exact'],r['lower_exact'],r['upper_exact']])
  need(0<=pl<=pu and 0<=rl<=ru)
  lo,hi=max(pl,rl),min(pu,ru);need(lo<=hi)
  intersections.append({'order':order,'lower_exact':str(lo),'upper_exact':str(hi)})
 need(pair['containing_intersections']==intersections)
 return intersections,times

def chunk_execution(execution,request,request_hash,application,application_hash,result):
 need(execution['schema']=='finite-long-preparation-execution-v1')
 need(execution['status']=='COMPLETED'and execution['reason']is None and execution['old_process_signals']==0)
 need(execution['method_manifest_sha256']=='4bb8d2adf05b2a16ad09067e88cf1c24e714e6529222746985e12183895d99bb')
 need(execution['method_review_sha256']=='b45103ffd8b6a5f86d80fde7ad709e6873f395465fb6ad94f0114eaef3a2bfd2')
 need(execution['request_sha256']==request_hash and len(execution['stages'])==len(request['stages'])==1)
 stage=execution['stages'][0];need(type(stage['exit_code'])is int and stage['exit_code']==0)
 argv=['-B','research/source013_near_admission/code/chunk_v02.py','--request',application,'--request-sha256',application_hash]
 need(stage['argv']==request['stages'][0]['argv']==argv and request['stages'][0]['limit_seconds']==480)
 need(request['files'][application]==application_hash and result['request']==application and result['request_sha256']==application_hash)
 eb,ee=measured(execution);sb,se=measured(stage);rb,re=measured(result)
 need(eb<=sb<=rb<=re<=se<=ee and stage['elapsed_seconds']<=482)
 return True
