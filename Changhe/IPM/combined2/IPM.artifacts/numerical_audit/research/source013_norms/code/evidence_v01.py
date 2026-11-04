"""Bind actual source013 admitted regions; keep block-local panel indices."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import gzip,json,os,sys,time
import method_v01 as v
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/source013_norms'
SOURCE={'id':'C2-N1-013','raw_sha256':'a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a','canonical_sha256':'2531d462643034e1083b40f5e60a6c4b0fa3ba84425cea3cadb68c767847fc33','fields_sha256':'3d5f08e06859af2577f6e099374a8ce5e139a0b66280055ada847745943bf8cb','fixed_c_exact':'4076476460239181/2251799813685248'}
ENERGY='research/source013_energy_admission';ANNULUS='research/source013_annulus_admission';DERIVATIVE='research/source013_derivative_restart';EXTERIOR='research/source013_exterior_admission'
EM='ad4e3ced2994e633afcfc09305975d31e4f1b9de9a92dd0b91bdb0740ec4effa';ER='f1e6b02164077653c7bbaac2a5aa5593ba52e090414e81e05a0f2fdb3f209bca';AM='2e1f35b2489b1111e8c3ddf781817eecb854b6dc0356b18655fab27cb20c8fa2'
sys.set_int_max_str_digits(0)
def local(n):
 p=Path(n);v.need(isinstance(n,str)and n and not p.is_absolute()and'..'not in p.parts);return ROOT/p
def digest(p):
 d=sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
def read(p):return json.loads(p.read_text())
def stamp():return datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
def put(p,d):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x')as f:json.dump(d,f,indent=2);f.write('\n')
def binding(e,n,h=None):
 q=digest(local(n));v.need(h is None or q==h,n)
 if n in e['files']:v.need(e['files'][n]==q,n)
 e['files'][n]=q;return q
def record(e,n):binding(e,n);return read(local(n))
def freeze(e):
 for n,h in e['files'].items():v.need(digest(local(n))==h,n)
def method(e,topic,expected=None,expected_review=None):
 mn=topic+'/verification/manifest_v01.json';rn=topic+'/verification/external_review_v01.json';mh=binding(e,mn,expected);rh=binding(e,rn,expected_review)
 m,r=read(local(mn)),read(local(rn));v.need(r['status']=='BOUND'and r['manifest_sha256']==mh)
 for n,h in m['files'].items():binding(e,n,h)
 return m,mh,rh
def admission(e,topic,job,mh,rh):
 r=record(e,topic+'/verification/'+job+'_v01/result.json');v.need(r['status']=='ADMITTED_LOCAL_ENERGIES'and r['job']==job and r['source']==SOURCE)
 v.need(r['admission_manifest_sha256']==mh and r['admission_review_sha256']==rh and r['receipt_checks']['checks']>0)
 for n,h in r['copied_records'].items():binding(e,n,h)
 original=record(e,topic+'/verification/'+job+'_v01/output_result.json');v.need(original['status']=='COMPLETED'and original['source']==SOURCE)
 v.need(r['deployment_manifest_sha256']==original['manifest_sha256'])
 return r,original

def load(mh,rh,derivatives=True):
 v.need(os.sched_getaffinity(0)=={50}and os.getpriority(os.PRIO_PROCESS,0)>=19 and sys.version_info[:3]==(3,12,13))
 v.need(all(os.environ.get(k)=='1'for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']))
 e={'source':SOURCE,'files':{},'regions':{}};own,_,_=method(e,'research/source013_norms',mh,rh)
 em,emh,erh=method(e,ENERGY,EM,ER);am,amh,arh=method(e,ANNULUS,AM)
 origin,op=admission(e,ENERGY,'origin',emh,erh);o=origin['outputs'];v.need(o['weight']=='P-S1'and o['radius_exact']=='1/50'and len(o['tensor_energies'])==4)
 v.need(origin['deployment_manifest_sha256']=='b40a43373fb2769dd11f7c89c727116ecf2c992932622d47dc9822ba7a4cd72a'and origin['deployment_review_sha256']=='f7380cc7a9346f509e0d4ef68ccb002a0e764d10a0268cf9f128aaedea744c49')
 v.need(o['norm_bounds']==op['bounds']and len(op['bounds'])==4)
 for j,(row,b)in enumerate(zip(o['tensor_energies'],op['bounds'],strict=True)):
  v.need(row['order']==b['derivative_order']==j);lo,hi=v.pair([b['norm_lower_exact'],b['norm_upper_exact']]);v.need(0<=lo and lo*lo==v.Q(row['lower_exact'])==v.Q(b['energy_lower_exact'])and hi*hi==v.Q(row['upper_exact'])==v.Q(b['energy_upper_exact']))
 e['regions']['origin']=o['tensor_energies']
 xm,xmh,xrh=method(e,EXTERIOR,own['files'][EXTERIOR+'/verification/manifest_v01.json']);exterior,xp=admission(e,EXTERIOR,'exterior',xmh,xrh);x=exterior['outputs'];v.need(len(x['bounds'])==len(xp['results'])==2)
 v.need(exterior['deployment_manifest_sha256']=='86dcf83162501b78b949c90b8b707a051cb8f95d7aa0ee15efa581eb38282c12'and exterior['deployment_review_sha256']==xm['files']['research/source013_exterior_deployment/verification/external_review_v03.json'])
 for saved,original,w in zip(x['bounds'],xp['results'],['P-S1','P-S2'],strict=True):
  v.need(saved['weight']==original['weight']==w and saved['radius_exact']==original['radius_exact']=='10000')
  lo,hi=v.pair([saved['norm_lower_exact'],saved['norm_upper_exact']]);v.need(lo==v.Q(original['complete_tail_norm']['lower_exact'])and hi==v.Q(original['complete_tail_norm']['upper_exact'])and lo>=0)
  v.need(lo*lo==v.Q(saved['energy_lower_exact'])and hi*hi==v.Q(saved['energy_upper_exact']))
 e['exterior_zeroth']=[x['bounds'][0]['energy_lower_exact'],x['bounds'][0]['energy_upper_exact']]
 aggregate=record(e,ANNULUS+'/verification/assembled_v01/result.json');v.need(aggregate['status']=='ADMITTED_COMPLETE_ANNULUS'and aggregate['source']==SOURCE)
 v.need(aggregate['admission_manifest_sha256']==amh and aggregate['admission_review_sha256']==arh and aggregate['complete_requested_partition']is True)
 v.need(aggregate['code_sha256']==am['files'][ANNULUS+'/code/assemble_v01.py'])
 v.need(aggregate['parent_indices']==list(range(114))and aggregate['sigma_exact']=='1'and aggregate['r0_exact']=='1/2'and aggregate['radius_lower_exact']=='1/50'and aggregate['radius_upper_exact']=='10000')
 for n,h in aggregate['files'].items():binding(e,n,h)
 deploy=record(e,'research/source013_annulus_deployment/verification/manifest_v01.json');v.need(deploy['source']==SOURCE and len(deploy['jobs'])==6)
 v.need(aggregate['deployment_manifest_sha256']=='6e937943b0165ff14be3e915b9b2e27b79c2f60ce34421f876739f8fbf185c2b'and aggregate['deployment_review_sha256']=='50b05d35eed71da818c3d6f8e7cc5a658649f798a9cb6d3003f4a2fe8038a3c7')
 parent=record(e,deploy['parent_request']);v.need(digest(local(deploy['parent_request']))==deploy['parent_request_sha256'])
 sums=[[v.Q(0),v.Q(0)]for _ in range(4)];blocks=[];indices=[];edge=v.Q(1,50);v.need(len(aggregate['admissions'])==6)
 for job,b in zip(deploy['jobs'],aggregate['admissions'],strict=True):
  expected=ANNULUS+'/verification/admit_'+job['id']+'_v01/result.json';v.need(b['job']==job['id']and b['path']==expected);binding(e,expected,b['sha256']);r=record(e,expected)
  v.need(r['status']=='ADMITTED_REGIONAL_ENERGIES'and r['source']==SOURCE and r['block']==job and r['job']==job['id'])
  v.need(r['admission_manifest_sha256']==amh and r['admission_review_sha256']==arh and r['code_sha256']==am['files'][ANNULUS+'/code/admit_v01.py'])
  v.need(r['deployment_manifest_sha256']==aggregate['deployment_manifest_sha256']and r['deployment_review_sha256']==aggregate['deployment_review_sha256'])
  v.need(r['reduction_checks']>0 and r['precision_bits']==1536 and r['reduction_details']['complete_exact_partition']is True)
  v.need(r['parent_request']==deploy['parent_request']and r['parent_request_sha256']==deploy['parent_request_sha256'])
  v.need(len(r['panels'])==len(job['indices'])==job['stop']-job['start']and job['indices']==list(range(job['start'],job['stop'])))
  v.need(v.Q(r['radius_lower_exact'])==edge);edge=v.Q(r['radius_upper_exact']);indices+=job['indices']
  for n,h in r['files'].items():binding(e,n,h)
  original_path=str(Path(expected).parent/'output_result.json');original=record(e,original_path);v.need(digest(local(original_path))==r['original_result_sha256']and original['energies']==r['energies'])
  v.need(len(r['energies'])==4)
  for j,row in enumerate(r['energies']):
   v.need(row['derivative_order']==j);lo,hi=v.pair([row['lower_exact'],row['upper_exact']]);v.need(lo>=0);sums[j][0]+=lo;sums[j][1]+=hi
  blocks.append(r)
 v.need(indices==list(range(114))and edge==10000 and len(aggregate['energies'])==4)
 for j,row in enumerate(aggregate['energies']):v.need(row['derivative_order']==j and v.pair([row['lower_exact'],row['upper_exact']])==tuple(sums[j]))
 e['regions']['annulus']=[{'order':j,'lower_exact':str(row[0]),'upper_exact':str(row[1])}for j,row in enumerate(sums)];e['blocks']=blocks;e['parent']=parent
 if derivatives:
  dm,dmh,drh=method(e,DERIVATIVE);r=record(e,DERIVATIVE+'/verification/admission_v01/result.json')
  v.need(r['status']=='ADMITTED_EXTERIOR_DERIVATIVES'and r['source']==SOURCE and r['manifest_sha256']==dmh and r['review_sha256']==drh and r['receipt_checks']['checks']>0)
  v.need(r['archive_source']==x['source_archive']==dm['archive_source'])
  for n,h in r['copied_records'].items():binding(e,n,h)
  original=record(e,DERIVATIVE+'/verification/admission_v01/output_result.json');v.need(original['results']==r['results']and original['source']==SOURCE)
  v.need(len(r['results'])==2 and r['results'][0]['weight']=='P-S1');levels=r['results'][0]['exterior_energies'];v.need(levels['radius_exact']=='10000'and len(levels['tensor_energies'])==4)
  e['regions']['exterior']=levels['tensor_energies']
 freeze(e);return e

def panels(e):
 edge=v.Q(1,50);count=0
 for block in e['blocks']:
  for local_index,b in enumerate(block['panels']):
   global_index=block['block']['start']+local_index;v.need(global_index==count);binding(e,b['path'],b['sha256'])
   with gzip.open(local(b['path']),'rt')as f:row=json.load(f)
   v.need(row['panel_index']==local_index and row['request']==e['parent']['panels'][global_index]);r=row['request']
   c,h,d=map(v.Q,[r[k]for k in ['center_exact','half_width_exact','inner_disk_exact']]);v.need(0<h<d<c and c-h==edge);edge=c+h
   v.need(r['sigma_exact']=='1'and r['r0_exact']=='1/2');K=row['taylor_order'];v.need(type(K)is int and K==r['order']and K>=0 and len(row['rows'])==4)
   zeroth=row['rows'][0];v.need(zeroth['derivative_order']==0);coeff=[v.pair(q)for q in zeroth['integrand_taylor_coefficients']];v.need(len(coeff)==K+1)
   H=v.Q(zeroth['complex_integrand_upper_exact']);v.need(H>0);old=2*h*H*(h/d)**(K+1)/(1-h/d);v.need(old==v.Q(zeroth['integration_remainder_upper_exact']))
   lower=max(v.Q(0),sum((2*h*coeff[k][0]/(k+1)for k in range(0,K+1,2)),v.Q(0))-old);upper=sum((2*h*coeff[k][1]/(k+1)for k in range(0,K+1,2)),v.Q(0))+old
   v.need(lower==v.Q(zeroth['energy_lower_exact'])and upper==v.Q(zeroth['energy_upper_exact']))
   m=1+4*c*c-8*c*d-4*d*d;v.need(m>0);count+=1
   yield {'index':global_index,'block':block['job'],'local_index':local_index,'binding':b,'c':c,'h':h,'d':d,'K':K,'H':H,'m':m,'error':old/m,'coefficients':coeff}
 v.need(count==114 and edge==10000)
