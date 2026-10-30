from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import importlib.util,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly
R=Path(__file__).resolve().parents[3];B=R/'research/scaled_quotient_rank'
sys.set_int_max_str_digits(0);sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('n4_rank_scaled_fields',R/'research/scaled_factored_weak/code/fields25.py');F=importlib.util.module_from_spec(spec);spec.loader.exec_module(F)
def main():
 start=time.monotonic();dest=B/'verification/result.json';assert not dest.exists();inputs={}
 def read(p):inputs[str(p.relative_to(R))]=sha(p);return json.loads(p.read_text())
 rawpath=R/'research/candidate_audits/data/C1-N1-016-legqs25-quot013/quot013_legqs25_m9to15_cpu_m16_exact.json';raw=read(rawpath)
 obj=read(R/'research/candidate016_holdout/verification/result.json');assert obj['raw_sha256']==sha(rawpath)
 oldpath=R/'research/optimizer_quotient_audit/source/N1_013_quot_exact.json';old=read(oldpath);audit=read(R/'research/optimizer_quotient_audit/verification/result.json')
 for local,h in audit['inputs'].items():assert sha(R/local)==h;inputs[local]=h
 row=[r for r in audit['rows'] if r['candidate']=='C1-N1-013-pairU-from007'][0];assert row['new_source_sha256']==sha(oldpath) and row['all_canonical_coefficients_equal']
 assert row['selected_columns']==1922 and row['nonpivot_relations']==0 and row['selected_original_shapes_match'] and sum(b['rank'] for b in row['blocks'])==1922
 shape=lambda g:(g['j'],g['m'],tuple(g['spec']))
 assert len(old['generators'])==1922 and len(raw['generators'])==2174
 assert list(map(shape,raw['generators'][:1922]))==list(map(shape,old['generators']))
 new=raw['generators'][1922:];shapes={shape(g) for g in new};expected={(j,m,('legqs',0,n,4,25)) for j in range(1,4) for m in range(9,16) for n in range(12)};assert len(new)==252 and shapes==expected
 c=Q(raw['cl_exact']);assert c==Q(4076476460239181,2251799813685248);delta=1-1/c;js=sorted({g['j'] for g in raw['generators']});assert js==list(range(8))
 classes=[]
 for i,j in enumerate(js):
  for k in js[i+1:]:
   v=(j-k)*delta/2;assert v.denominator!=1;classes.append({'j':j,'k':k,'difference':str(v)})
 a=Q(624);v0=-1/a;t0=1-v0;witnesses=[]
 for m in range(9,16):
  for n in range(12):
   A=F.generator(m,['legqs',0,n,4,25]);assert A.powers==(0,4+n,0)
   numerator=A.numerator_v();val=numerator(v0);wanted=Q(25)**8*v0**4*comb(2*n,n)*t0**(m+n);assert val==wanted and val!=0
   laurent=val/a**(4+n);witnesses.append({'m':m,'N':n,'pole_order':4+n,'numerator_at_pole':str(val),'laurent_coefficient':str(laurent),'leading_coefficient_formula_equal':True})
 p1=(3+1/c-delta)/2;leading=4*19*18*(p1-9-Q(4,625));assert leading!=0
 fixture={'cl_exact':str(c),'generators':[{'j':1,'m':9,'spec':['legqs',0,0,4,25],'coef':'1'}]};model=F.ScaledRadial(fixture);modes=sorted(n for j,n in model.rho);assert modes==[17,19]
 A=model.rho[1,17];num=A.P;order=next(i for i,v in enumerate(num) if v);assert order==10
 denominator=Q(1)
 for a,k in zip(F.SCALES,A.powers,strict=True):denominator*=(1+a)**k
 derived=num[10]/denominator;assert derived==leading
 for p in [Path(__file__),B/'PROOF.md',R/'research/scaled_factored_weak/code/fields25.py',R/'research/optimizer_quotient_audit/PROOF.md']:inputs[str(p.relative_to(R))]=sha(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':obj['candidate'],'raw_sha256':sha(rawpath),'old_basis_size':1922,'new_basis_size':252,'potential_rank':2174,'actual_shapes_equal':True,'branch_classes':classes,'pole_witnesses':witnesses,'new_blocks':21,'distinct_pole_orders_per_block':12,'density_support_containment':list(range(17,32,2)),'explicit_m9_N0_density_modes':modes,'mode17_leading_harmonic_coefficient':str(leading),'mode17_Cartesian_coefficient_equal':True,'exact_fixture':fixture,'inputs':inputs,'elapsed_seconds':time.monotonic()-start,'verdict':'OPEN independent theoretical review; exact finite witnesses pass. Potential rank only, no density rank or objective floor.'}
 with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('rank2174',sha(dest),'lowest density mode17',leading,'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
