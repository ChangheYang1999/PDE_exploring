"""No numerics-lane code imports; independent exact metadata and aggregation."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from io import BytesIO
import hashlib,json,math
import numpy as np
from flint import arb,ctx
ctx.prec=512;ctx.threads=1
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1];NUM=LANE.parent/'s2-num/work'
SOURCE=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
def aa(v):return arb(v.numerator)/v.denominator if isinstance(v,F) else arb(v)
def fq(v):return F.from_float(float(v))
def stamp():return datetime.now(timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
manifest={}
def snapshot(path,name):
    b=path.read_bytes();(TOP/'inputs'/name).write_bytes(b);manifest[name]={'source':str(path),'sha256':sha(b),'bytes':len(b)};return b
raw=SOURCE.read_bytes();assert sha(raw)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
orig=np.load(BytesIO(raw),allow_pickle=False);knots=list(map(fq,orig['knots']));spans=[(knots[i],knots[i+1]) for i in range(len(knots)-1) if knots[i]<knots[i+1]]
assert len(spans)==1558
lo,hi=knots[0],knots[-1];cells=[('minf',None,lo-4)]
inbounds=[lo-4,lo-2,lo-1,lo-F(1,2),lo]
cells += [('inner',a,b) for a,b in zip(inbounds,inbounds[1:])]
cells += [('mid',a,b) for a,b in spans]
outbounds=[hi,hi+F(1,2),hi+1,hi+2,hi+4,hi+8]
cells += [('outer',a,b) for a,b in zip(outbounds,outbounds[1:])]+[('pinf',hi+8,None)]
assert len(cells)==1569
assert all(cells[i][2]==cells[i+1][1] for i in range(len(cells)-1))
ta=np.array([float(b if a is None else a) for _,a,b in cells]);hh=np.array([np.nan if a is None or b is None else float(b-a) for _,a,b in cells]);kind=np.array([x[0] for x in cells]);theta=np.array([float(arb.pi()*i/128) for i in range(65)])
left=np.array([a is None or a<=0 for _,a,b in cells]);right=np.array([b is None or b>=0 for _,a,b in cells]);assert left.any() and right.any()
sets={};summaries={}
for tag,prefix in [('MARGIN','margin'),('HYPA','hypA')]:
    for suffix in ('','_A','_B'):
        name=tag+suffix
        d=np.load(BytesIO(snapshot(NUM/'runs'/name/(prefix+'.npz'),name+'.npz')),allow_pickle=False)
        js=json.loads(snapshot(NUM/'runs'/name/(prefix+'.json'),name+'.json'))
        sets[name]=d;summaries[name]=js
        for key,expected in [('cell_ta',ta),('cell_h',hh),('cell_kind',kind),('theta_edges',theta)]:
            if expected.dtype.kind in 'f':assert np.array_equal(d[key],expected,equal_nan=True),(name,key)
            else:assert np.array_equal(d[key],expected),(name,key)
        assert js['ntheta']==64 and js['prec']==160
for name in ('exact_trial.py','opimage.py','encl.py','tailbound.py','margin.py','hypA.py','outward.py','merge_margin.py','merge_hypA.py'):
    snapshot(NUM/name,'code_'+name)
M=sets['MARGIN'];H=sets['HYPA'];mcells=[]
for tag,prefix,owner in [('MARGIN','margin','M_lo'),('HYPA','hypA','Dlo')]:
    merged=sets[tag];parts=[sets[tag+'_A'],sets[tag+'_B']]
    masks=[np.isfinite(d[owner]).all(axis=1) if d[owner].ndim==2 else np.isfinite(d[owner]) for d in parts]
    assert np.all(np.sum(masks,axis=0)==1),tag
    keys=[k for k in merged.files if k not in ('cell_ta','cell_h','cell_kind','theta_edges')]
    for part,mask in zip(parts,masks):
        for k in keys:assert np.array_equal(merged[k][mask],part[k][mask],equal_nan=True),(tag,k)
    mcells.append({'tag':tag,'part_owner_counts':[int(x.sum()) for x in masks],'complete_unique_ownership':True})
for k in M.files:
    if k not in ('cell_ta','cell_h','cell_kind','theta_edges'):assert np.isfinite(M[k]).all(),k
for k in ('Dlo','Dhi','DPlo','DPhi','IDCHK','A1','A0','KWlo','KWhi','Qlo','Qhi'):assert np.isfinite(H[k]).all(),k
for k in ('DD2','DP2','A0W'):assert np.isfinite(H[k][left]).all(),k
for k in ('DCK','DPK'):assert np.isfinite(H[k][right]).all(),k
assert np.all(M['NREF']==1)
assert np.array_equal(M['M_ref'],M['M_lo']) and np.array_equal(M['MA_ref'],M['MA_lo'])
assert np.all(H['Dlo']<=H['Dhi']) and np.all(H['DPlo']<=H['DPhi'])
assert np.all(H['Qlo']<=H['Qhi']) and np.all(H['KWlo']<=H['KWhi'])
assert np.all(M['DV'][...,0]<=M['DV'][...,1]) and np.all(M['Q'][...,0]<=M['Q'][...,1])
ms=summaries['MARGIN'];hs=summaries['HYPA'];checks={}
def eq(key,actual,reported):
    assert fq(actual)==fq(reported),(key,actual,reported)
    checks[key]={'exact':str(fq(actual)),'decimal_diagnostic':float(actual)}
eq('m_R',np.min(M['M_ref']),ms['inf_m_lower_bound'])
eq('m_a',np.min(M['MA_ref']),ms['aniso_inf_ma_lower_bound'])
eq('gradient',np.max(M['GR_up']),ms['sup_grad_rho_finite'])
eq('DU',np.max(M['DU_up']),ms['sup_DU'])
eq('bplus',np.max(M['BP_up']),ms['sup_bplus'])
eq('q_lower',np.min(M['Q'][...,0]),ms['q_range'][0]);eq('q_upper',np.max(M['Q'][...,1]),ms['q_range'][1])
eq('d_lower',np.min(H['Dlo']),hs['d_inf']);eq('d_upper',np.max(H['Dhi']),hs['d_sup'])
eq('dprime',max(abs(np.min(H['DPlo'])),abs(np.max(H['DPhi']))),hs['dprime_abs_sup'])
eq('left_d',np.max(H['DD2'][left]),hs['A_left']['sup_dD_e2']);eq('left_dp',np.max(H['DP2'][left]),hs['A_left']['sup_dp_e2'])
eq('right_d',np.max(H['DCK'][right]),hs['A_right']['sup_dcl_ek']);eq('right_dp',np.max(H['DPK'][right]),hs['A_right']['sup_dp_ek'])
eq('MQ',np.max(H['A1']),hs['M_Q']);eq('MP',max(np.max(H['A0W'][left]),np.max(H['A0'][right])),hs['M_P'])
eq('kappa_lower',np.min(H['KWlo']),hs['kappa_star_lower']);eq('kappa_upper',np.max(H['KWhi']),hs['kappa_w_sup'])
eq('identity',np.max(H['IDCHK']),hs['identity_check_max'])
assert fq(hs['A_left']['C_left'])>=fq(hs['A_left']['sup_dD_e2'])+fq(hs['A_left']['sup_dp_e2'])
assert fq(hs['A_right']['C_right'])>=fq(hs['A_right']['sup_dcl_ek'])+fq(hs['A_right']['sup_dp_ek'])
assert np.min(M['M_ref'])>0 and np.min(M['MA_ref'])>0 and np.min(H['Dlo'])>0
# Rectangle inclusion for every nonpositive VLO box.
xlo=F(4559930541822721,562949953421312);xhi=F(5122880495244367,562949953421312)
zeros=[];outside=[]
for ci,ti in np.argwhere(M['VLO']<=0):
    ci=int(ci);ti=int(ti);_,a,b=cells[ci]
    assert a is not None and b is not None
    rm=aa(a).exp();rp=aa(b).exp();tm=arb.pi()*ti/128;tp=arb.pi()*(ti+1)/128
    inside=bool((rm*tp.cos()).lower()>=aa(xlo) and (rp*tm.cos()).upper()<=aa(xhi) and (rp*tp.sin()).upper()<=arb(1)/2)
    item={'cell':ci,'theta_index':ti,'t_left_exact':str(a),'t_right_exact':str(b),'inside_Q':inside}
    zeros.append(item)
    if not inside:outside.append(item)
positive=M['VLO'][M['VLO']>0]
out={'date':stamp(),'status':'PASS_CONDITIONAL_ON_EXPORTED_CELL_BOUNDS','original_sha256':sha(raw),'radial_cells':len(cells),'angular_cells':64,'total_boxes':1569*64,'part_ownership':mcells,'all_applicable_entries_finite':True,'all_refinement_counts_one':True,'aggregates':checks,'Z':{'nonpositive_boxes':len(zeros),'outside_Q':len(outside),'outside_Q_boxes':outside,'all_nonpositive_boxes':zeros,'minimum_positive_VLO_exact':str(fq(np.min(positive))),'inner_halfline_minimum_exact':str(fq(np.min(M['VLO'][0]))),'global_Z_accepted':len(outside)==0},'manifest':manifest,'proof_sha256':sha((TOP/'PROOF.md').read_bytes()),'script_sha256':sha(Path(__file__).read_bytes())}
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('manifest','Z','aggregates')},indent=2))
print('nonpositive boxes',len(zeros),'outside Q',len(outside))
