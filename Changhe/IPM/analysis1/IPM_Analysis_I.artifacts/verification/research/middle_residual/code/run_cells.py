"""Resume-safe exhaustive middle-cell driver; exact bounds only, no server or external writes."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,gzip,hashlib,time,resource,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from fast_moments import aa,integral,shift_poly
from cell_core import bound_cell,ff
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/middle_residual/evidence'
sys.path.insert(0,str(BASE/'research/ball_transport/code'))
from dyadic_ball import export_ball,import_ball

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'utc':utc(),**kw}),flush=True)
BOUND_KEYS=('W_upper_exact','W_over_m_upper_exact','Wm_times_one_plus_u_power_half_upper_exact','Wm_times_one_plus_u_power_half_minus_k_upper_exact')
REMAINDER_KEYS=('retained_Bernstein_sum','nonpolynomial_remainder','discarded_polynomial_remainder','max_Green_remainder')
def validate_row(row,ci,partition,k,L):
 assert row['type']=='cell' and row['cell']==ci and row['degree']==16
 part=partition[ci];assert row['parent_span']==part['parent_span']
 left,right=F(part['left_exact']),F(part['right_exact'])
 assert F(row['left_exact'])==left and F(row['right_exact'])==right
 assert F(row['tc_exact'])==(left+right)/2 and F(row['h_exact'])==(right-left)/2
 for key in BOUND_KEYS:assert F(row[key])>=0
 for key in REMAINDER_KEYS:assert 0<=F(row[key]['lower_exact'])<=F(row[key]['upper_exact'])
 u=aa(left).exp()/aa(L);fresh=u**3*(1+u*u)**aa((k-3)/2);fresh_lower=ff(fresh.mid())-ff(fresh.rad())
 assert 0<F(row['m_left']['lower_exact'])<=fresh_lower
 assert F(row['weight_power_half_exact'])==F(1,2) and F(row['weight_power_half_minus_k_exact'])==F(1,2)-k
 assert F(row['W_upper_exact'])>=sum((F(row[key]['upper_exact']) for key in REMAINDER_KEYS[:3]),F(0))
 assert F(row['W_over_m_upper_exact'])*F(row['m_left']['lower_exact'])>=F(row['W_upper_exact'])
def resume_rows(path,header,partition,k,L):
 if path.exists():
  raw=path.read_bytes();lines=raw.splitlines(keepends=True);offset=0
  for i,line in enumerate(lines):
   if not line.endswith(b'\n'):
    assert i==len(lines)-1
    recovery={'utc':utc(),'original_sha256':hashlib.sha256(raw).hexdigest(),'original_bytes':len(raw),'retained_bytes':offset,'reason':'Interrupted final line, even if its JSON parses'}
    (E/('recovery_'+str(time.time_ns())+'.json')).write_text(json.dumps(recovery,indent=2)+'\n')
    with path.open('r+b') as f:f.truncate(offset);f.flush();os.fsync(f.fileno())
    raw=raw[:offset];break
   offset+=len(line)
 else:raw=b''
 if not raw:
  with path.open('w') as f:f.write(json.dumps(header,separators=(',',':'))+'\n');f.flush();os.fsync(f.fileno())
  return []
 lines=raw.splitlines();assert json.loads(lines[0])==header,'Resume header, source or input changed'
 rows=[]
 for line in lines[1:]:
  row=json.loads(line);validate_row(row,len(rows),partition,k,L);rows.append(row)
 return rows

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--stop-after',type=int,default=7809);ap.add_argument('--tag',default='full_q16');args=ap.parse_args();assert 0<args.stop_after<=7809
 ctx.prec=384;ctx.threads=1;resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=time.monotonic()
 kp=E/'original_knots.jsonl.gz';mp=E/'knot_manifest.json';manifest=json.loads(mp.read_bytes());assert sha(kp)==manifest['output_sha256'];assert manifest['spans']==1558 and manifest['cells']==7809
 deps={'driver':Path(__file__),'cell_core':Path(__file__).parent/'cell_core.py','fast_moments':Path(__file__).parent/'fast_moments.py','ball_transport':BASE/'research/ball_transport/code/dyadic_ball.py','archive_audit':Path(__file__).parent/'audit_knots.py'};hashes={k:sha(v) for k,v in deps.items()}
 checkpath=E/'setup_checks.json';checks=json.loads(checkpath.read_bytes());assert checks['status']=='PASS';assert checks['hashes']['cell_core.py']==hashes['cell_core'] and checks['hashes']['fast_moments.py']==hashes['fast_moments']
 data=BASE/'data_exact/modal_v2.json';assert sha(data)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';tr=json.loads(data.read_bytes());k,L=[F.from_float(float.fromhex(tr['scalars_hex'][v])) for v in ('k','L')];knots=sorted(set(F.from_float(float.fromhex(v)) for v in tr['arrays']['knots']['hex']))
 assert len(knots)==1559 and 0<k<1 and L>0
 kap=E/'knot_audit.json';ka=json.loads(kap.read_bytes());assert ka['status']=='PASS' and ka['archive_sha256']==sha(kp) and ka['manifest_sha256']==sha(mp) and ka['cells']==7809 and ka['spans']==1558 and ka['footer_read']
 assert ka['source_sha256']==hashes['archive_audit'];assert all(v['minimum_accuracy_bits']>200 for v in ka['moment_argument_endpoint_checks'])
 pp=E/'partition_exact.json';assert sha(pp)==ka['partition_sha256'];partdata=json.loads(pp.read_bytes());assert partdata['input_sha256']==sha(data) and partdata['cells']==7809
 parentparts=partdata['spans'];assert len(parentparts)==1558
 partition=[]
 for si,part in enumerate(parentparts):
  assert part['span']==si and part['first_cell']==len(partition) and isinstance(part['count'],int) and part['count']>0
  a,b=F(part['a_exact']),F(part['b_exact']);assert (a,b)==tuple(knots[si:si+2])
  for q in range(part['count']):partition.append({'parent_span':si,'left_exact':str(a+(b-a)*F(q,part['count'])),'right_exact':str(a+(b-a)*F(q+1,part['count']))})
 assert len(partition)==7809
 pubp=BASE/'research/residual_samples/evidence/published_residual_snapshot.json';assert sha(pubp)=='439df9893cf99ee0389e04358ff79146e7a95e71a061d1d09d025879ddacc331';pub=json.loads(pubp.read_bytes(),parse_float=F);assert len(pub['rows'])==7809 and [r['ci'] for r in pub['rows']]==list(range(7809))
 spp=BASE/'research/residual_samples/evidence/sample_result.json';assert sha(spp)=='0608fe74dbeef4eaf21e26aedffe61453f558e25e0e902dd72fda6b3084f630c';points={v['cell']:v for v in json.loads(spp.read_bytes())['samples']}
 header={'type':'header','schema':'ipm-middle-cell-bounds-v1','cells_required':7809,'degree':16,'precision_bits':384,'hashes':hashes,'knot_manifest_sha256':sha(mp),'knot_audit_sha256':sha(kap),'partition_sha256':sha(pp),'setup_checks_sha256':sha(checkpath),'knot_input_sha256':sha(kp),'modal_input_sha256':sha(data),'comparison_sha256':sha(pubp),'point_crosscheck_sha256':sha(spp),'k_exact':str(k),'L_exact':str(L)}
 outpath=E/(args.tag+'_cells.jsonl');rows=resume_rows(outpath,header,partition,k,L);nextci=len(rows);emit(stage='start_or_resume',completed=nextci,stop_after=args.stop_after)
 crosschecks=[];seen_spans=0;expected_first=0;complete=False
 with gzip.open(kp,'rt') as inp, outpath.open('a') as out:
  ih=json.loads(next(inp));assert ih['type']=='header' and ih['hashes']==manifest['hashes'] and ih['cells']==7809 and ih['spans']==1558
  assert ih['hashes']['fast_moments']==hashes['fast_moments'] and ih['hashes']['ball_transport']==hashes['ball_transport']
  for line in inp:
   item=json.loads(line)
   if item['type']=='complete':assert seen_spans==1558 and expected_first==7809 and item['cells']==7809 and item['spans']==1558 and not inp.read();complete=True;break
   assert item['type']=='span' and item['span']==seen_spans;seen_spans+=1
   si=item['span'];a,b=map(F,(item['a_exact'],item['b_exact']));assert (a,b)==tuple(knots[si:si+2]);center=F(item['polynomial_mid_exact']);assert center==(a+b)/2
   nchild=item['count'];first=item['first_cell'];assert nchild>0 and first==expected_first;assert all(item[key]==value for key,value in parentparts[si].items());expected_first+=nchild
   if first+nchild<=nextci:continue
   assert first<=nextci<first+nchild
   polys=[[import_ball(v) for v in row] for row in item['density_polynomials']];I=list(map(import_ball,item['i_left']));J=list(map(import_ball,item['j_right']));assert len(polys)==262 and all(len(p)==8 for p in polys) and len(I)==len(J)==261 and all(v==0 for v in polys[-1])
   for offset in range(nchild):
    ci=first+offset
    if ci<nextci:continue
    assert ci==nextci
    if ci>=args.stop_after:break
    left=a+(b-a)*F(offset,nchild);right=a+(b-a)*F(offset+1,nchild);tc=(left+right)/2;assert a<=left<right<=b;delta=tc-center;hl=tc-a;hr=b-tc;cache={}
    ivals=[];jvals=[]
    for n in range(1,262):
     rate=-(2*n+4);ivals.append(aa(rate*hl).exp()*I[n-1]+integral(polys[n-1],delta,hl,rate,True,cache))
     rate=4-2*n;jvals.append(aa(rate*hr).exp()*J[n-1]+integral(polys[n],delta,hr,rate,False,cache))
    jets=[shift_poly(p,delta) for p in polys]
    row={'cell':ci,'cell_endpoints_exact':[str(left),str(right)],'t_exact':str(tc),'density_polynomial_at_point':[[export_ball(v) for v in p] for p in jets],'i':list(map(export_ball,ivals)),'j':list(map(export_ball,jvals))}
    if ci in points:
     old=points[ci];assert old['t_exact']==str(tc) and old['cell_endpoints_exact']==row['cell_endpoints_exact']
     for new,key in [(ivals,'i'),(jvals,'j')]:
      for v,w in zip(new,old[key]):assert v.overlaps(import_ball(w)),(ci,key)
     for pp,qq in zip(jets,old['density_polynomial_at_point']):
      for v,w in zip(pp,qq):assert v.overlaps(import_ball(w)),(ci,'density')
     row['residual_coefficients']=old['residual_coefficients'];crosschecks.append(ci)
    bound=bound_cell(row,k,L,knots,pub,Q=16,keep_coefficients=False);bound['type']='cell';bound['parent_span']=si
    Wm=aa(F(bound['W_over_m_upper_exact']))
    for name,power in [('half',F(1,2)),('half_minus_k',F(1,2)-k)]:
     endpoint=right if power>=0 else left;factor=(1+aa(endpoint).exp()/aa(L))**aa(power);upper=(Wm*factor).upper();assert upper.rad()==0;bound['Wm_times_one_plus_u_power_'+name+'_upper_exact']=str(ff(upper));bound['weight_power_'+name+'_exact']=str(power)
    validate_row(bound,ci,partition,k,L)
    out.write(json.dumps(bound,separators=(',',':'))+'\n');out.flush();os.fsync(out.fileno());rows.append(bound);nextci+=1
    if ci%25==0 or ci in points:emit(stage='cell_done',cell=ci,Wm=bound['W_over_m_upper_display'],comparison=bound['Wm_comparison'],seconds=time.monotonic()-start)
    if nextci%25==0:
     (E/(args.tag+'_progress.json')).write_text(json.dumps({'utc':utc(),'cells_complete':nextci,'cells_required':7809,'seconds_this_process':time.monotonic()-start,'driver_sha256':hashes['driver']},indent=2)+'\n')
   if nextci>=args.stop_after and args.stop_after<7809:break
 # Full completion also requires reading the source footer, including when resuming all cells.
 assert nextci==min(args.stop_after,7809)
 if args.stop_after==7809:assert complete and seen_spans==1558
 maxima={key:max(rows,key=lambda r:F(r[key])) for key in BOUND_KEYS}
 summary={'utc':utc(),'status':'COMPUTED_REQUIRES_INDEPENDENT_OUTPUT_AUDIT' if nextci==7809 else 'PARTIAL','cells_complete':nextci,'cells_required':7809,'source_footer_read':complete,'seconds_this_process':time.monotonic()-start,'hashes':hashes,'run_header':header,'output_sha256':sha(outpath),'input_sha256':sha(kp),'new_point_crosschecks':crosschecks,'maxima':{key:{'cell':r['cell'],'bound_exact':r[key],'left_exact':r['left_exact'],'right_exact':r['right_exact']} for key,r in maxima.items()},'scope':'Middle region only; center and exterior excluded. No global inverse or a posteriori endpoint.'}
 (E/(args.tag+'_summary.json')).write_text(json.dumps(summary,indent=2)+'\n');emit(stage='done',status=summary['status'],cells=nextci,seconds=time.monotonic()-start)
if __name__=='__main__':main()
