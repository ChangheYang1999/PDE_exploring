"""P301 independent scalar comparisons only; no NUM module imported/executed."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,math,time
V=Path('research/301_runtime_24_48_comparison/verification');start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();C=[]
def ck(name,ok,detail=None):C.append(dict(name=name,passed=bool(ok),detail=detail))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
a=json.loads((V/'runtime12_24.json').read_text());b=json.loads((V/'runtime24_48.json').read_text());f=json.loads((V/'freeze.json').read_text());n=lambda s:' '.join(s.split());src=n((V/'runtime_readonly.py.txt').read_text());old=[{k:(v if k=='state'else float(v))for k,v in x.items()}for x in csv.DictReader((V/'P291_norms.csv').read_text().splitlines())if x['state']=='rtvel_K48_b3092']
for x in f['inputs']:ck('frozen_'+x['snapshot'],sha(V/x['snapshot'])==x['sha256'])
ck('proof_precedes_controls',f['proof_written_utc']<start);ck('proof_unchanged',sha(V.parent/'PROOF.md')==f['proof_sha256'])
for name,j in [('12_24',a),('24_48',b)]:
 ck(name+'_metadata',j['beta']==3.092 and j['lam']==0.9326700862338395 and j['K']==48 and j['Nt']==56 and j['state']=='runs/blamB48ext_beta3.092.npz');ck(name+'_eight_radii',[x['r']for x in j['rows']]==[10.**k for k in range(2,10)]);ck(name+'_missing_arrays_and_hashes',not any(x in j for x in ['sha256','angles','velocity','components']))
ck('order_labels',a['ng_ref']==12 and a['ng']==24 and b['ng_ref']==24 and b['ng']==48)
for phrase in ['for ng in (args.ng_ref, args.ng):','for (r, U12), (_, U48) in zip(W[args.ng_ref], W[args.ng]):','mU = np.abs(U48).max()','max_U48=float(mU)','args.nphi + 2','[1:-1]','default=181',"default='1e2,1e3,1e4,1e5,1e6,1e7,1e8,1e9'",'Wv[0] - bt[0] * X[0]']:ck('readonly_source_'+phrase,phrase in src)
rows=[]
for x,y,z in zip(a['rows'],b['rows'],old):
 r=x['r'];M24=x['max_U48'];M48=y['max_U48'];Mref=z['independent_max_V'];D1224=x['max_dU'];D2448=y['max_dU'];D1248=z['max_dU'];margin=1e-10*max(1,M24,M48,Mref,D1248);tag=str(r)
 ck(tag+'_same_r',r==y['r']==z['r']);ck(tag+'_M48_identical_to_P291',M48==z['max_U48']);ck(tag+'_finite_positive',all(math.isfinite(v)and v>0 for v in [M24,M48,Mref,D1224,D2448,D1248]))
 for label,rr in [('12_24',x),('24_48',y)]:
  ck(tag+'_'+label+'_norm_ratio',abs(rr['max_dU']/rr['max_U48']-rr['rel_to_maxU'])<1e-14);ck(tag+'_'+label+'_dilation_ratio',abs(rr['max_dU']/(3.092*r)-rr['rel_to_beta_r'])<1e-14)
 ck(tag+'_norm_increment_compatible',abs(M48-M24)<=D2448+margin,dict(lhs=abs(M48-M24),rhs=D2448,rounding_margin=margin));ck(tag+'_three_order_increment_compatible',abs(D1248-D1224)<=D2448+margin,dict(lhs=abs(D1248-D1224),rhs=D2448,rounding_margin=margin))
 if r>=1e5:ck(tag+'_reported_four_digits',format(x['rel_to_maxU'],'.4g')==format(z['rel_to_maxU'],'.4g'),[x['rel_to_maxU'],z['rel_to_maxU']])
 row=dict(r=r,M24_reported=M24,M48_reported=M48,Mref_independent=Mref,D12_24_reported=D1224,D24_48_reported=D2448,D12_48_reported=D1248,relative_increment24_48=D2448/M48,norm_discrepancy24=abs(M24-Mref),relative_norm_discrepancy24=abs(M24-Mref)/Mref,norm_discrepancy48=abs(M48-Mref),relative_norm_discrepancy48=abs(M48-Mref)/Mref,conditional_transferred_lower24=max(0,abs(M48-Mref)-D2448),relative_transferred_lower24=max(0,abs(M48-Mref)-D2448)/Mref,increment_ratio12_24_to12_48=D1224/D1248,rounding_margin=margin);rows.append(row)
# A manufactured common-offset example exactly defeats an error upper bound from increments.
for h in [1.,1000.,1e8]:
 ref=[2.,-3.];vv=[x+h for x in ref];ck('common_bias_'+str(h),max(abs(x-y)for x,y in zip(vv,vv))==0 and max(abs(x-y)for x,y in zip(vv,ref))==h)
with(V/'COMPARISON.csv').open('w')as h:w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
d=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,passed=sum(x['passed']for x in C),total=len(C),checks=C,rows=rows,code_sha256=sha(__file__));(V/'checks.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items()if k not in ['checks','rows']},indent=2));print('FAILURES',json.dumps([x for x in C if not x['passed']],indent=2));print('LARGEST_RADIUS',json.dumps(rows[-1],indent=2))
