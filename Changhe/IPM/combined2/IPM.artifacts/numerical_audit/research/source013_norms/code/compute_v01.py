"""Source013 norm primary or independent containing reduction."""
from pathlib import Path
import argparse,time
from flint import ctx
import method_v01 as m
import evidence_v01 as e
import independent_v01 as independent

def main():
 p=argparse.ArgumentParser();p.add_argument('--kind',choices=['weighted','unweighted'],required=True);p.add_argument('--mode',choices=['primary','reduction'],required=True);p.add_argument('--manifest-sha256',required=True);p.add_argument('--review-sha256',required=True);args=p.parse_args()
 start,tick=e.stamp(),time.monotonic();ctx.prec=1024 if args.mode=='primary'else 1536;proof=e.BASE/'PROOF.md'
 data=e.load(args.manifest_sha256,args.review_sha256,args.kind=='weighted');primary=None;primary_path=e.BASE/'verification'/(args.kind+'_primary_v01/result.json')
 if args.mode=='reduction':
  primary=e.read(primary_path);m.need(primary['status']=='PASS'and primary['source']==e.SOURCE and primary['kind']==args.kind and primary['mode']=='primary')
  m.need(primary['manifest_sha256']==args.manifest_sha256 and primary['review_sha256']==args.review_sha256 and primary['code_sha256']==e.digest(Path(__file__)))
  m.need(primary['proof_sha256']==e.digest(proof)and primary['files']==data['files']);e.freeze({'files':primary['files']})
 if args.kind=='weighted':
  regions=[data['regions'][n]for n in ['origin','annulus','exterior']];values=m.norms(m.tensor_totals(regions,args.mode=='reduction'),args.mode=='reduction');checked=independent.weighted(regions,values)
  if primary is not None:
   checked=independent.weighted(regions,primary['values']);m.need(primary['values']['tensor_energies']==values['tensor_energies'])
  output={'values':values,'independent_checks':checked}
 else:
  rows=[];old=iter(primary['panels'])if primary else None
  for panel in e.panels(data):
   mark=time.monotonic();fn=m.reciprocal_integral if args.mode=='primary'else m.newton_integral
   lo,hi=fn(panel['coefficients'],panel['c'],panel['h'],panel['K']);finite=m.enclosure(lo,hi);lo,hi=m.pair(finite);interval=m.enclosure(lo-panel['error'],hi+panel['error'],True)
   row={'panel_index':panel['index'],'block':panel['block'],'local_index':panel['local_index'],'binding':panel['binding'],'order':panel['K'],'denominator_lower_exact':str(panel['m']),'finite_integral_interval_exact':finite,'remainder_upper_exact':str(panel['error']),'energy_interval_exact':interval,'elapsed_seconds':time.monotonic()-mark}
   if old is not None:
    saved=next(old)
    for k in ['panel_index','block','local_index','binding','order','denominator_lower_exact','remainder_upper_exact']:m.need(row[k]==saved[k])
    pl,pu=m.pair(saved['energy_interval_exact']);rl,ru=m.pair(interval);m.need(max(pl,rl)<=min(pu,ru))
   rows.append(row);print(e.stamp(),args.kind,args.mode,'panel',panel['index'],row['elapsed_seconds'],flush=True)
  if old is not None:m.need(next(old,None)is None)
  origin=data['regions']['origin'][0];regions=m.outer([origin['lower_exact'],origin['upper_exact']],data['exterior_zeroth']);values=m.total_quotient([r['energy_interval_exact']for r in rows],regions,args.mode=='reduction')
  checked=independent.unweighted([r['energy_interval_exact']for r in rows],regions,values)
  if primary is not None:
   m.need(regions==primary['regions']);independent.unweighted([r['energy_interval_exact']for r in primary['panels']],regions,primary['values'])
  output={'panels':rows,'regions':regions,'values':values,'independent_checks':checked}
 e.freeze(data)
 result={'status':'PASS','kind':args.kind,'mode':args.mode,'started_utc':start,'finished_utc':e.stamp(),'elapsed_seconds':time.monotonic()-tick,'source':e.SOURCE,'manifest_sha256':args.manifest_sha256,'review_sha256':args.review_sha256,'precision_bits':ctx.prec,'code_sha256':e.digest(Path(__file__)),'proof_sha256':e.digest(proof),'files':data['files'],'checks':m.CHECKS,'independent_assertions':independent.CHECKS,**output,'scope':'Complete same-source regional consumer; primary and independent reduction must both pass before publication. No background or stationary closure.'}
 if primary is not None:result.update({'primary':str(primary_path.relative_to(e.ROOT)),'primary_sha256':e.digest(primary_path)})
 dest=e.BASE/'verification'/(args.kind+'_'+args.mode+'_v01/result.json');e.put(dest,result);print('PASS',args.kind,args.mode,m.CHECKS,independent.CHECKS,time.monotonic()-tick,flush=True)
if __name__=='__main__':main()
