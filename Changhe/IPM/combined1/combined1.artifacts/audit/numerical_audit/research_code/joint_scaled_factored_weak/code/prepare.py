"""Prepare a separate four-pole backend from the retained own radius50 code."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/joint_scaled_factored_weak';OLD=ROOT/'research/scaled50_factored_weak'
def put(name,s):
 p=BASE/'code'/name
 with p.open('x') as f:f.write(s)
def replace(s,a,b):
 assert a in s,a
 return s.replace(a,b)
source={}
for name in ['fields50.py','weak.py','calibrate_v2.py','check_candidates.py']:
 p=OLD/'code'/name;source[str(p.relative_to(ROOT))]=sha256(p.read_bytes()).hexdigest()
s=(OLD/'code/fields50.py').read_text();s=replace(s,'SCALES = (Q(99), Q(2499), Q(9999))','SCALES = (Q(99), Q(624), Q(2499), Q(9999))\nZERO_POWERS = (0,)*len(SCALES)');s=replace(s,'(0, 0, 0)','ZERO_POWERS');put('fields_joint.py',s)
s=(OLD/'code/weak.py').read_text();s=replace(s,'from fields50 import','from fields_joint import');s=replace(s,'scaled50_factored_weak','joint_scaled_factored_weak');put('weak.py',s)
s=(OLD/'code/calibrate_v2.py').read_text();s=replace(s,'radius50 factored','simultaneous radius25/radius50 factored');s=replace(s,'from fields50 import','from fields_joint import');s=replace(s,'scaled50_factored_weak','joint_scaled_factored_weak');s=replace(s,'n4_factored50','n4_factored_joint');s=replace(s,'(A.powers[0],0,A.powers[1])','(A.powers[0],0,0,A.powers[1])');s=replace(s,'a=Rat(Poly([1,2,3]),(2,3,1));b=Rat(Poly([2,-1]),(1,2,2))','a=Rat(Poly([1,2,3]),(2,3,2,1));b=Rat(Poly([2,-1]),(1,2,1,2))');s=replace(s,'D=LINEARS[0]**2*LINEARS[1]**3*LINEARS[2]','D=LINEARS[0]**2*LINEARS[1]**3*LINEARS[2]**2*LINEARS[3]');s=replace(s,'(4,6,2)','(4,6,4,2)');s=replace(s,'(2,3,1)','(2,3,2,1)');s=replace(s,"{'j':3,'m':3,'spec':['legqs',2,4,4,50],'coef':'11/19'},","{'j':3,'m':3,'spec':['legqs',2,4,4,50],'coef':'11/19'},\n        {'j':3,'m':3,'spec':['legqs',1,5,4,25],'coef':'-19/31'},");s=replace(s,"{'j':2,'m':1,'spec':['legqs',0,2,1,50],'coef':'4/5'}]}","{'j':2,'m':1,'spec':['legqs',0,2,1,50],'coef':'4/5'},\n        {'j':2,'m':1,'spec':['legqs',2,3,2,25],'coef':'-3/7'}]}");s=replace(s,'tick=time.monotonic();model=ScaledRadial(data);mixed=[]','tick=time.monotonic();model=ScaledRadial(data);mixed=[]\n        mixed_key=(3,6) if index==0 else (2,2)\n        A=model.deriv(0,0)[mixed_key];assert A.powers[1]>0 and A.powers[2]>0');s=replace(s,"g['spec'][-1]!=50","g['spec'][-1] not in (25,50)");s=replace(s,"'exact_fixture':data,'mixed_derivatives':mixed","'exact_fixture':data,'simultaneous_poles624_and2499_in_same_branch_mode':True,'mixed_derivatives':mixed");s=replace(s,'scalar2499','scalar_joint');s=replace(s,'fields50.py','fields_joint.py')
anchor="    paths=[BASE/'verification/scalar_joint.json'"
assert anchor in s
extra='''    scale_regressions=[];extra_paths=[]
    for ident,dirname,modname,filename in [('016','scaled_factored_weak','n4_joint_regression25','fields25.py'),('017','scaled50_factored_weak','n4_joint_regression50','fields50.py')]:
        oldpath=ROOT/'research'/dirname/'code'/filename
        prior=module(modname,oldpath)
        directory=next((ROOT/'research/candidate_audits/data').glob('C1-N1-'+ident+'-*'))
        manifest_path=directory/'MANIFEST.json';manifest=json.loads(manifest_path.read_text())
        rawpath=directory/manifest['coefficient_files'][0]['name']
        assert sha(rawpath)==manifest['coefficient_files'][0]['sha256']
        tick=time.monotonic();before=prior.ScaledRadial(rawpath);after=ScaledRadial(rawpath)
        def conversion(A):
            return Rat(A.P,(A.powers[0],A.powers[1],0,A.powers[2])) if ident=='016' else Rat(A.P,(A.powers[0],0,A.powers[1],A.powers[2]))
        compared={name:equal(getattr(after,name),getattr(before,name),conversion) for name in ['rho','u1','u2','rx','ry']}
        for key,field in before.derivatives.items():compared[str(key)]=equal(after.deriv(*key),field,conversion)
        assert all(compared.values())
        scale_regressions.append({'candidate':directory.name,'raw_sha256':sha(rawpath),'coefficientwise_fields':compared,'prior_engine':str(oldpath.relative_to(ROOT)),'elapsed_seconds':time.monotonic()-tick})
        extra_paths.extend([oldpath,manifest_path,rawpath])
        print('SINGLE SCALE EXACT FIELDS',ident,len(compared),time.monotonic()-tick,flush=True)
'''
s=s.replace(anchor,extra+anchor)
s=replace(s,"oldrecord=json.loads(oldresult.read_text());paths.append(oldresult)","oldrecord=json.loads(oldresult.read_text());paths.append(oldresult);paths.extend(extra_paths)")
s=replace(s,"'candidate010_probe_points':points010,","'candidate010_probe_points':points010,'single_scale_regressions':scale_regressions,")
put('calibrate.py',s)
s=(OLD/'code/check_candidates.py').read_text();s=replace(s,'from fields50 import','from fields_joint import');s=replace(s,'scaled50_factored_weak','joint_scaled_factored_weak');s=replace(s,'n4_candidate50','n4_candidate_joint');s=replace(s,'fields50.py','fields_joint.py');s=replace(s,'calibrate_v2.py','calibrate.py');s=replace(s,'scalar2499','scalar_joint');put('check_candidates.py',s)
put('run_calibration.sh','set -eu\npython3 -B research/joint_scaled_factored_weak/code/scalar_joint.py\npython3 -B research/joint_scaled_factored_weak/code/calibrate.py\n')
with (BASE/'verification/PREPARATION.json').open('x') as f:json.dump({'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':sha256((BASE/'PROOF.md').read_bytes()).hexdigest(),'source_own_code_sha256':source,'foreign_code_executed':False},f,indent=2);f.write('\n')
print('Prepared separate four-pole code; no calibration executed.')
