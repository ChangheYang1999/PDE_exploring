"""Publish only jointly verified, complete same-source norm intervals."""
from pathlib import Path
import argparse,time
from flint import ctx
import evidence_v01 as e
import method_v01 as m
import independent_v01 as independent

def intersection(a,b):
 al,au=m.pair(a);bl,bu=m.pair(b);lo,hi=max(al,bl),min(au,bu);m.need(0<=lo<=hi);return list(map(str,[lo,hi]))
def combine(kind,primary,reduction):
 if kind=='weighted':
  a,b=primary['values'],reduction['values'];m.need(a['tensor_energies']==b['tensor_energies']);integers=[]
  for x,y in zip(a['integer_norms'],b['integer_norms'],strict=True):
   for key in ['order','energy_lower_exact','energy_upper_exact']:m.need(x[key]==y[key])
   integers.append({**x,'norm_interval_exact':intersection(x['norm_interval_exact'],y['norm_interval_exact'])})
  m.need(len(integers)==4 and a['fractional_order_exact']==b['fractional_order_exact']=='21/10')
  return {'tensor_energies':a['tensor_energies'],'integer_norms':integers,'fractional_order_exact':'21/10','fractional_norm_interval_exact':intersection(a['fractional_norm_interval_exact'],b['fractional_norm_interval_exact'])}
 m.need(kind=='unweighted'and primary['regions']==reduction['regions']and len(primary['panels'])==len(reduction['panels'])==114)
 rows=[]
 for index,(a,b)in enumerate(zip(primary['panels'],reduction['panels'],strict=True)):
  m.need(a['panel_index']==b['panel_index']==index)
  for key in ['block','local_index','binding','order','denominator_lower_exact','remainder_upper_exact']:m.need(a[key]==b[key])
  rows.append(intersection(a['energy_interval_exact'],b['energy_interval_exact']))
 values=m.total_quotient(rows,primary['regions']);independent.unweighted(rows,primary['regions'],values)
 return {'panels':rows,'regions':primary['regions'],'values':values}
def main():
 p=argparse.ArgumentParser();p.add_argument('--kind',choices=['weighted','unweighted'],required=True);p.add_argument('--manifest-sha256',required=True);p.add_argument('--review-sha256',required=True);args=p.parse_args()
 start,tick=e.stamp(),time.monotonic();ctx.prec=1536;data=e.load(args.manifest_sha256,args.review_sha256,args.kind=='weighted');records=[];files={}
 for mode in ['primary','reduction']:
  n=str((e.BASE/'verification'/(args.kind+'_'+mode+'_v01/result.json')).relative_to(e.ROOT));row=e.read(e.local(n));files[n]=e.digest(e.local(n))
  m.need(row['status']=='PASS'and row['source']==e.SOURCE and row['kind']==args.kind and row['mode']==mode)
  m.need(row['manifest_sha256']==args.manifest_sha256 and row['review_sha256']==args.review_sha256 and row['proof_sha256']==e.digest(e.BASE/'PROOF.md'))
  m.need(row['code_sha256']==e.digest(e.BASE/'code/compute_v01.py')and row['files']==data['files']and row['independent_checks']['checks']>0)
  m.need(row['precision_bits']==(1024 if mode=='primary'else 1536));e.freeze(row);records.append(row)
 a,b=records;m.need(b['primary_sha256']==files[b['primary']]);out=combine(args.kind,a,b)
 if args.kind=='weighted':
  regions=[data['regions'][n]for n in ['origin','annulus','exterior']]
  for row in [a['values'],b['values'],out]:independent.weighted(regions,row)
 else:
  for row in records:independent.unweighted([q['energy_interval_exact']for q in row['panels']],row['regions'],row['values'])
 e.freeze(data)
 result={'status':'CERTIFIED_NORMS','kind':args.kind,'source':e.SOURCE,'started_utc':start,'finished_utc':e.stamp(),'elapsed_seconds':time.monotonic()-tick,'manifest_sha256':args.manifest_sha256,'review_sha256':args.review_sha256,'input_files':files,'files':data['files'],'checks':m.CHECKS,'independent_checks':independent.CHECKS,'code_sha256':e.digest(Path(__file__)),'proof_sha256':e.digest(e.BASE/'PROOF.md'),'output':out,'scope':'Only the displayed same-source residual norm intervals, conditional on the admitted numerical certificates and reviewed execution. No background, inverse or stationary existence closure.'}
 dest=e.BASE/'verification'/(args.kind+'_publication_v01/result.json');e.put(dest,result);print('CERTIFIED_NORMS',args.kind,e.digest(dest),flush=True)
if __name__=='__main__':main()
