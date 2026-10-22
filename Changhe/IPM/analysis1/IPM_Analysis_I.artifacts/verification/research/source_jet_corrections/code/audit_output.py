"""Fresh saved-output audit using fmpq endpoints and a different quadratic root."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,time
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
from flint import fmpq,arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/source_jet_corrections/evidence'
ctx.prec=1536;ctx.threads=1
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def exact(v):
 m,e=v.man_exp();return fmpq(int(m))*fmpq(2)**int(e)
def pair(item):return [fmpq(item[k]) for k in ['lower_exact','upper_exact']]
def main():
 tic=time.monotonic();c=json.loads((E/'checks.json').read_text());assert c['status']=='PASS_NEW_JET_AND_FACE_SCALARS';counts=Counter()
 for p,h in c['files'].items():assert sha(B/p)==h,p
 j=json.loads((B/'research/modal_source/evidence/source_result.json').read_text())['final_values']
 x0,x1=pair(j['xstar']);m0,m1=pair(j['mu_minus_1']);g0,g1=pair(j['g']);p0,p1=pair(j['gprime']);d=fmpq(c['delta_exact'])
 assert m0<=m1<0 and min(x0,g0,p0)>0
 # All corners of each exact multilinear expression; deliberately avoid the producer's monotonic formulas.
 vals={'D':[-m*g for m in [m0,m1] for g in [g0,g1]],'C':[-m+g+p for m in [m0,m1] for g in [g0,g1] for p in [p0,p1]],'H':[2*g-x*p for g in [g0,g1] for x in [x0,x1] for p in [p0,p1]]}
 extrem={k:[min(v),max(v)] for k,v in vals.items()}
 vals['margin']=[dd-cc*d-2*d*d for dd in extrem['D'] for cc in extrem['C']];extrem['margin']=[min(vals['margin']),max(vals['margin'])]
 for key,ends in extrem.items():assert ends==pair(c['exact_ranges'][key]);counts['exact_extrema_equal']+=2
 # Fresh corner enclosures must be completely contained in saved portable bounds.
 for key,seq in vals.items():
  lo,hi=pair(c['portable_bounds'][key])
  for q in seq:
   z=arb(q);assert lo<=exact(z.lower())<=exact(z.upper())<=hi,(key,q);counts['fresh_corner_contains']+=1
 roots=[]
 for cc in extrem['C']:
  for dd in extrem['D']:
   z=((arb(cc)**2+8*arb(dd)).sqrt()-arb(cc))/4
   lo,hi=pair(c['portable_bounds']['root_scale']);assert lo<=exact(z.lower())<=exact(z.upper())<=hi
   assert exact(z.lower())>d;roots.append(str(z));counts['fresh_alternative_root_contains']+=1
 assert extrem['D'][0]>fmpq(67,10**8) and fmpq(300229,10000)<extrem['C'][0]<=extrem['C'][1]<fmpq(30023,1000)
 assert extrem['H'][0]>fmpq(571,10) and extrem['margin'][0]>0
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FRESH_JET_SCALARS','method':'fmpq all-corner extrema, fresh Arb1536 whole-enclosure containment, subtractive quadratic root different from stable producer; no producer import.','counts':dict(counts),'checks_sha256':sha(E/'checks.json'),'source_sha256':sha(B/'research/modal_source/evidence/source_result.json'),'self_sha256':sha(__file__),'alternative_root_displays':roots,'seconds':time.monotonic()-tic}
 (E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
