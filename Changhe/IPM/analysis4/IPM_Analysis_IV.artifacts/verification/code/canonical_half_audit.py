"""Independent finite norms, all Poisson identities and exact-prefix comparisons."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
import argparse,gzip,json,math,pickle,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,fmpq,ctx
from stream_precision_audit import unpack
from certified_initial_majorants import pack
ROOT=Path('research/291_canonical_half_finite')
def ref(p):return dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())
def text(x):return x.str(40,radius=True)
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def main():
 start=time.monotonic();ctx.prec=768;zero=arb(0);logten=arb(10).log()
 p=Path('../a4-num/ckpt/log_sin1_c2_p512.pkl');raw=p.read_bytes();digest=sha256(raw).hexdigest();size=len(raw);s=pickle.loads(raw);del raw
 assert (s['A'],s['B'],s['ring'],s['prec'])==('1','2','arb',512)
 assert max(s['f'])==max(s['g'])==300
 lp=Path('../a4-num/logs/log_sin1_c2_p512.jsonl');lr=lp.read_bytes();logs=[json.loads(x) for x in lr.splitlines() if x.strip()];header=logs[0]
 assert header['delta']=='1/2' and header['c_l']=='2' and header['f1']==['1']
 printed={x['n']:x for x in logs if 'n' in x};assert all(n in printed for n in range(1,301))
 (ROOT/'sources/producer_log.jsonl.gz').write_bytes(gzip.compress(lr,compresslevel=9,mtime=0))
 ep=ROOT/'verification/exact_prefix.json';exact=json.loads(ep.read_bytes());assert exact['orders']==12 and exact['all_checks_pass']
 selected={field:{str(n):s[field][n] for n in range(1,13)} for field in ['f','g']}
 selected['source_sha256']=digest
 (ROOT/'verification/packed_prefix.json.gz').write_bytes(gzip.compress(json.dumps(selected,separators=(',',':')).encode(),mtime=0))
 manifest=dict(checked_at_utc=now(),source=str(p),source_sha256=digest,source_bytes=size,maximum_order=300,checkpoint_flags={k:s.get(k) for k in ['radii_reset_at','perturbed_seed','midpoint_only']},producer_log=dict(path=str(lp),sha256=sha256(lr).hexdigest()),exact_prefix=ref(ep),bits=768)
 (ROOT/'verification/input_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 rows=[];positions=poisson=canonical=prefix_checks=printed_checks=0;max_error=0.;max_column_relative=zero;max_column_location=None;uncertain=[];norms={}
 def get(A,q,j):return A[q][j] if 0<=q<len(A) and 0<=j<len(A[q]) else zero
 for n in range(1,301):
  decoded={};row=dict(n=n,fields={});printed_row=printed[n]
  assert not printed_row.get('midpoint_only',False)
  for field,logkey,colkey in [('f','log10_sum_cols','log10_col_l1'),('g','log10_sum_gcols','log10_gcol_l1')]:
   cols=[[arb(*unpack(v)) for v in col] for col in s[field][n]];decoded[field]=cols;positions+=sum(map(len,cols))
   colnorm=[sum(map(abs,col),zero) for col in cols];total=sum(colnorm,zero);assert total>0;norms[field,n]=total
   for q,(col,norm) in enumerate(zip(cols,colnorm)):
    mids=sum((abs(v.mid()) for v in col),zero);rads=sum((v.rad() for v in col),zero)
    if mids==0:
     if rads!=0:uncertain.append([n,field,q])
    else:
     rel=rads/mids
     if float(rel.mid())>float(max_column_relative.mid()):max_column_relative=rel;max_column_location=[n,field,q]
    if norm>0 and q<len(printed_row.get(colkey,[])):
     value=printed_row[colkey][q]
     if value is not None and math.isfinite(float(value)):
      err=abs(float((norm.log()/logten).mid())-float(value));assert err<2e-10,(n,field,q,err);max_error=max(max_error,err);printed_checks+=1
   value=printed_row.get(logkey)
   if value is not None:
    err=abs(float((total.log()/logten).mid())-float(value));assert err<2e-10,(n,field,err);max_error=max(max_error,err);printed_checks+=1
   facts={q:arb(math.factorial(q))*v/colnorm[0] for q,v in enumerate(colnorm) if q>0 and v>0}
   detail=dict(norm=pack(total),log10_norm=text(total.log()/logten),root=text(total.root(n)),degree=len(cols)-1,relative_radius=text(total.rad()/abs(total.mid())))
   if facts:
    win=max(facts,key=lambda q:float(facts[q].log().mid()));cert=all(facts[win]>v for q,v in facts.items() if q!=win)
    detail.update(nonconstant_factorial_maximizer=win,maximum_strictly_certified=cert,nonconstant_factorial_ratio=text(facts[win]),log10_nonconstant_factorial_ratio=text(facts[win].log()/logten),nonconstant_below_constant=bool(facts[win]<1))
   row['fields'][field]=detail
   if n<=12:
    ex=exact['rows'][n-1]['density' if field=='f' else 'stream']
    for q in range(max(len(cols),1+max(map(int,ex),default=-1))):
     amplitudes=ex.get(str(q),{})
     width=max(len(cols[q]) if q<len(cols) else 0,1+max(((int(m)-(field=='f'))//2 for m in amplitudes),default=-1))
     for j in range(width):
      m=2*j+(field=='f');v=fmpq(amplitudes.get(str(m),'0'));assert get(cols,q,j).contains(arb(v)),('prefix',n,field,q,j);prefix_checks+=1
  F,G=decoded['f'],decoded['g'];P=arb(2)-arb(n)/2;scale=res=zero;local=can=0
  for col in G:assert col[0].is_zero()
  for q in range(max(len(F),len(G))):
   for j in range(1,max(max(map(len,F)),max(map(len,G)))+1):
    lhs=(4*j*j-P*P)*get(G,q,j)-2*P*(q+1)*get(G,q+1,j)-(q+1)*(q+2)*get(G,q+2,j)
    rhs=((P-2*j)*get(F,q,j-1)+(q+1)*get(F,q+1,j-1)+(P+2*j)*get(F,q,j)+(q+1)*get(F,q+1,j))/2
    d=lhs-rhs;assert d.contains(0),('Poisson',n,q,j,text(d));res+=abs(d);scale+=abs(lhs)+abs(rhs);local+=1
    if q==0 and n==4+4*j:assert get(G,0,j).is_zero();can+=1
  poisson+=local;canonical+=can;row['poisson']=dict(coefficients=local,canonical_constants=can,relative_residual=text(res/scale) if scale>0 else '0')
  row['log10_N_over_M']=text((norms['g',n]/norms['f',n]).log()/logten);rows.append(row)
  if n%20==0:print(json.dumps(dict(at=now(),n=n,positions=positions,poisson=poisson,elapsed_s=time.monotonic()-start)),flush=True)
 late=[r for r in rows if r['n']>=200]
 result=dict(**manifest,all_checks_pass=True,scope='Finite arithmetic of supplied balls; independent exact canonical prefix through12. No convergence conclusion.',norm_coefficient_positions=positions,poisson_coefficients=poisson,canonical_constants=canonical,exact_prefix_comparisons=prefix_checks,printed_comparisons=printed_checks,maximum_printed_log_error=max_error,maximum_column_relative_radius=text(max_column_relative),maximum_column_relative_location=max_column_location,zero_center_nonzero_radius_columns=uncertain,late_density_nonconstant_maximizers=sorted({r['fields']['f']['nonconstant_factorial_maximizer'] for r in late}),late_density_maximizers_strict=all(r['fields']['f']['maximum_strictly_certified'] for r in late),late_density_nonconstant_below_constant=all(r['fields']['f']['nonconstant_below_constant'] for r in late),rows=rows,actual_elapsed_s=time.monotonic()-start)
 sources=[]
 for name in ['canonical_half_audit.py','stream_precision_audit.py','certified_initial_majorants.py']:
  dest=ROOT/'sources'/name;dest.write_bytes(Path('code',name).read_bytes());sources.append(ref(dest))
 result['sources']=sources;(ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as e:
  failure=dict(at=now(),type=type(e).__name__,error=str(e),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)])
  (ROOT/'verification/FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
