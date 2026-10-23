"""Independent high precision axis reconstruction of saved Q polynomials.

Use exact binary coefficient values, forward Chebyshev recurrence, fixed-point
map inversion, and rational eighth-order differences. This reads previously
computed canonical velocities; it does not generate another velocity law.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,math
import numpy as np
import mpmath as mp

mp.mp.dps=80
outdir=Path('evidence/q_far_precision');outdir.mkdir(parents=True,exist_ok=True)
allrows=[]
for folder in sorted(Path('evidence/q_evaluations').glob('qlsrel*')):
    source=folder/'axis_q2.json';snapshot=folder/'snapshot.npz'
    if not source.exists() or not snapshot.exists():continue
    prior=json.loads(source.read_text())
    if 'finished_utc' not in prior:continue
    data=np.load(snapshot,allow_pickle=False)
    N=int(data['N']);M=int(data['M']);raw=np.asarray(data['u'])
    coeff=[];start=0
    for k in range(M):
        nk=N+1-k;coeff.append([mp.mpf(float(c)) for c in raw[start:start+nk]]);start+=nk
    L=mp.mpf(float(data['L']));kap=mp.mpf(float(data['p']));eta=1/kap;gam=1-eta
    ell=mp.mpf(float(data['cl']));mu=mp.mpf(float(data['mu'])) if 'mu' in data else mp.mpf(0)
    def polynomial(c,t):
        if len(c)==1:return c[0]
        t0=mp.mpf(1);t1=t;acc=c[0]+c[1]*t
        for ck in c[2:]:
            t2=2*t*t1-t0;acc+=ck*t2;t0,t1=t1,t2
        return acc
    def axis(y):
        y=mp.mpf(y)
        if not y:return mp.mpf(0)
        sign=mp.sign(y);r=abs(y);h=(L/r)**eta;z=min(mp.mpf(1),h)
        for iteration in range(400):
            nxt=h*(1-z/2)**(eta/2)
            if abs(nxt-z)<=mp.mpf('1e-72')*abs(nxt):z=nxt;break
            z=nxt
        else:raise ArithmeticError('High precision map did not converge')
        t=1-z;sig=1-z/2;power=mp.mpf(1);acc=mp.mpf(0)
        for c in coeff:
            acc+=power*polynomial(c,t);power*=-sig
        return sign*r*z*acc/2
    K=L**eta*mp.fsum([(-1)**k*mp.fsum(c) for k,c in enumerate(coeff)])/2
    weights=[mp.mpf(4)/5,-mp.mpf(1)/5,mp.mpf(4)/105,-mp.mpf(1)/280]
    pred_nf=abs(ell*gam-1)/(ell*gam+1);pred_nv=abs(ell*gam-1)/(1+gam)
    rows=[]
    for old in prior['points']:
        r=mp.mpf(old['y']);rho=axis(r);vel=mp.mpf(old['U'][1]);diffs=[]
        for step in ['.003','.0015','.00075']:
            h=r*mp.mpf(step)
            dr=mp.fsum(w*(axis(r+(j+1)*h)-axis(r-(j+1)*h))/h for j,w in enumerate(weights))
            transport=(ell*r+vel)*dr;R=transport-rho;Nf=abs(transport)+abs(rho);Nv=abs(rho)+abs(r*dr)+abs(vel*dr)
            diffs.append({'relative_step':step,'rho_y':str(dr),'dilation_exponent':str(r*dr/rho),'R':str(R),'Nf':str(Nf),'Nv':str(Nv),'R_Nf':str(abs(R)/Nf),'R_Nv':str(abs(R)/Nv)})
        rows.append({'radius':str(r),'rho':str(rho),'scaled_rho_actual':str(rho/r**gam),'density_double_relative_error':float(abs(mp.mpf(old['rho'])-rho)/abs(rho)),'U2_from_independent_q2':old['U'][1],'FD8':diffs,'old_double_FD8_Nf':[v['R_Nf'] for v in old['residuals']]})
        result={'utc':datetime.now(timezone.utc).isoformat(),'source':str(source),'source_checkpoint_sha256':prior['metadata']['sha256'],'precision_digits':80,'actual_gamma':str(gam),'actual_K':str(K),'ell':str(ell),'Nf_limit':str(pred_nf),'Nv_limit':str(pred_nv),'points':rows,'scope':'High precision scalar axis density and independent FD8 using exact binary saved coefficients. Canonical velocity is the previously independent q2 kernel, whose q1 difference is recorded separately. No claim of a uniform global residual or nearby profile.'}
        (outdir/(folder.name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({'utc':result['utc'],'tag':folder.name,'radius':str(r),'density_double_relative_error':rows[-1]['density_double_relative_error'],'Nf':diffs[-1]['R_Nf']}),flush=True)
    result['finished_utc']=datetime.now(timezone.utc).isoformat()
    result['max_density_double_relative_error']=max(v['density_double_relative_error'] for v in rows)
    result['max_FD8_Nf_step_spread']=max(float(max(mp.mpf(v['R_Nf']) for v in row['FD8'])-min(mp.mpf(v['R_Nf']) for v in row['FD8'])) for row in rows)
    assert result['max_FD8_Nf_step_spread']<1e-10
    (outdir/(folder.name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    allrows.append({k:v for k,v in result.items() if k!='points'})
(outdir/'summary.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','states':allrows},indent=2)+'\n')
