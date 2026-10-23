"""Independent DR snapshot audit; mathematics written first in result 165.
No producer code is imported. CPU only, one process, one BLAS thread.
"""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import argparse,hashlib,json,math,time
import numpy as np
from scipy.special import roots_legendre
from q_checkpoint_reader import QCheckpoint
from q_exact_jets import jets,pack
from complementary_inverse_charts import ComplementaryQ,FullChart
from angular_log_inverse import AngularLogInverse
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient
from q_mp_primitives import MPQPrimitives,guard_digits
import mpmath as mp

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):Path(p).write_text(json.dumps(d,indent=2)+'\n')
def unpack(x):
    if isinstance(x,(dict,list,tuple,str,bool)) or x is None:return x
    return x.item() if hasattr(x,'item') else x

def tests():
    rows=[]
    for M in (2,3,8,16):
        theta=(np.arange(3*M)+.5)*math.pi/(6*M)
        Fv=np.cos(2*M*theta)
        A=np.cos(2*np.arange(M)[:,None]*theta)
        proj=A@Fv/(3*M);proj[1:]*=2
        err=float(np.max(abs(proj)))
        assert err<2e-14 and max(abs(Fv))>.8
        rows.append({'M':M,'discarded_mode_projection_max':err,'original_max':float(max(abs(Fv)))})
    eps=F(1,100);v=[eps,F(1)];w=[F(1),-eps];den=1+eps**2
    matrix=[[(v[i]*v[j]-w[i]*w[j])/den for j in range(2)]for i in range(2)]
    assert matrix[0][1]==matrix[1][0]
    assert [sum(matrix[i][j]*v[j]for j in range(2))for i in range(2)]==v
    assert [sum(matrix[i][j]*w[j]for j in range(2))for i in range(2)]==[-x for x in w]
    assert 1/den>F(98,100)
    return {'status':'PASS','angular_truncation':rows,'symmetric_matrix_exact':[[str(x)for x in r]for r in matrix],
            'unstable_eigenvector':[str(x)for x in v],'exterior_squared_norm_fraction':str(1/den),'exponentially_growing_core_amplitude':str(eps)}

def grid(model,logr,theta,order,cw,C,cx):
    sn,cs=np.sin(theta)[None,:],np.cos(theta)[None,:]
    rows={k:np.empty((len(logr),len(theta)))for k in ['R','Nf','Nv','rho','U1','U2','G','identity_error']}
    for use_defect in (True,False):
        ids=np.flatnonzero((logr<=model.log_core)==use_defect)
        if not len(ids):continue
        owner=model if use_defect else FullChart(model)
        ff=AngularLogInverse(owner,order).fields(logr[ids],theta)
        d=ff['H']+owner.a*sn
        gx=ff['grad_radial']*cs-ff['grad_angular']*sn
        gy=ff['grad_radial']*sn+ff['grad_angular']*cs
        ux=ff['ur']*cs-ff['ut']*sn;uy=ff['ur']*sn+ff['ut']*cs
        tx=(C*cs+ux/cw)*gx/cw;ty=(C*sn+uy/cw)*gy/cw
        rr=tx+ty-d/cw
        gg=cw*d-(cx*cs+ux)*gx-(cx*sn+uy)*gy
        vals={'R':rr,'Nf':abs(tx)+abs(ty)+abs(d/cw),'Nv':abs(d/cw)+abs(cs*gx+sn*gy)/cw+abs(ux*gx+uy*gy)/cw**2,
              'rho':d,'U1':ux,'U2':uy,'G':gg,'identity_error':rr+gg/cw**2}
        for k,v in vals.items():rows[k][ids]=v
    assert all(np.all(np.isfinite(v))for v in rows.values())
    assert min(rows['Nf'].flat)>0 and min(rows['Nv'].flat)>0
    return rows

def summary(z,logr,theta):
    r=np.exp(logr);records={};peaks=[]
    for name,lo,hi in [('core',0,1),('annulus',1,100),('far',100,float('inf')),('all',0,float('inf'))]:
        ids=np.flatnonzero((r>=lo)&(r<hi));row={}
        for nm,values in [('R_Nf',abs(z['R'])/z['Nf']),('R_Nv',abs(z['R'])/z['Nv']),('abs_R',abs(z['R'])*r[:,None]),('abs_G',abs(z['G'])*r[:,None])]:
            i,j=np.unravel_index(np.argmax(values[ids]),(len(ids),len(theta)));i=int(ids[i]);j=int(j)
            point=[float(r[i]*math.cos(theta[j])),float(r[i]*math.sin(theta[j]))]
            row[nm]={'maximum':float(values[i,j]),'point':point,'radius':float(r[i]),'theta':float(theta[j]),'R':float(z['R'][i,j]*r[i]),'Nf':float(z['Nf'][i,j]*r[i]),'Nv':float(z['Nv'][i,j]*r[i])}
            if name in ('core','annulus') and nm=='R_Nf':peaks.append(point)
        records[name]=row
    return records,peaks

def mp_value(v,d=60):
    if isinstance(v,dict):return {k:mp_value(x,d)for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [mp_value(x,d)for x in v]
    if v is None:return None
    return mp.nstr(v,d)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('states',nargs='+');ap.add_argument('--tag',default='dr_first_tau20');args=ap.parse_args()
    folder=Path('research/dynamic_rescaling_implementation/verification')/args.tag;folder.mkdir(parents=True,exist_ok=True)
    gate=Path('research/q_full_inverse_primitives/verification/manufactured.json');assert json.loads(gate.read_text())['status']=='PASS'
    result={'started_utc':utc(),'status':'RUNNING','code_sha256':sha(__file__),'proof_sha256':sha('research/dynamic_rescaling_implementation/PROOF.md'),'manufactured_gate_sha256':sha(gate),'algebraic_tests':tests(),'states':[],
            'scope':'Frozen snapshots only. Complete canonical inverse, independent Cartesian differentiation, empirical precision/order checks. Unequal stored times do not constitute matched-time trajectory convergence. No continuum instability or endpoint claim.'}
    output=folder/'AUDIT.json'
    def checkpoint():result['updated_utc']=utc();save(output,result)
    checkpoint()
    import torch
    torch.set_num_threads(1)
    # Saved diagnostics contain NumPy scalar floats. Permit only their numeric constructors.
    torch.serialization.add_safe_globals([np._core.multiarray.scalar,np.dtype,type(np.dtype("float64")),type(np.dtype("float32"))])
    for path in args.states:
        start=time.monotonic();source=Path(path);frozen=folder/source.name
        frozen.write_bytes(source.read_bytes())
        st=torch.load(frozen,map_location='cpu',weights_only=True)
        q=QCheckpoint(frozen);mod=ComplementaryQ(frozen)
        cw=float(st['cw']);cx=float(st['cx']);C=float(st['C']);assert cw>0
        meta={k:unpack(st[k])for k in ['N','M','C','cw','cx','c','tau','Tphys','b3_pred','dtau','step','M2','L','p','gamma','proj']if k in st}
        j=jets(q.coeff,q.kappa,C);canonical_c=float(j['c']);actual_delta=float(F(C)+j['c']/F(cw)-1)
        row={'source':str(source),'frozen':str(frozen),'source_sha256':sha(frozen),'metadata':meta,'exact_jet_data':pack({k:v for k,v in j.items()if not k.endswith('polynomial')}),
             'canonical_c':canonical_c,'producer_c':float(st['c']),'c_difference':canonical_c-float(st['c']),
             'normalized_center_defect_exact':str(F(C)+j['c']/F(cw)-1),'normalized_center_defect':actual_delta,
             'rate_relation_error':cx-C*cw,'node_reconstruction_error':q.node_reconstruction_error(),'grid':[],'direct_checks':[],'multiprecision':[]}
        result['states'].append(row);checkpoint()
        # Exact polynomial Gauss order and an independent doubled-order comparison.
        row['moments']=[]
        for order in ((q.N+8)//2,q.N+12):
            xg,wg=roots_legendre(order);out={}
            for R in (0.,1.,10.,100.):
                tR=-1. if R==0 else float(q.coordinates(np.array([R]))[0][0])
                t=(1+tR)/2+(1-tR)*xg/2;s=(1+t)/2
                Q=(1-t)/2+q.kappa*(1+t)
                out[str(R)]=float((1-tR)/16*np.sum(wg*Q*(q.polynomial(1,t)-s*q.polynomial(2,t))))
            out['I0_minus_exact_c_plus_a_over4']=out['0.']-(canonical_c+float(j['a'])/4) if '0.'in out else out['0.0']-(canonical_c+float(j['a'])/4)
            row['moments'].append({'order':order,'values':out})
        endpoint=[math.fsum(c)for c in q.coeff];D=q.L**(1/q.kappa)/2
        row['tail']={'A1':D*(endpoint[0]-endpoint[1]/2),'A3':D*(endpoint[1]-endpoint[2])/2,'K':D*math.fsum((-1)**k*v for k,v in enumerate(endpoint)),
                     'actual_exponent_exact':str(1-1/F(q.kappa)),'C_times_exponent_minus_one_exact':str(F(C)*(1-1/F(q.kappa))-1),
                     'endpoint_modes':endpoint,'max_absolute_endpoint_mode_k_ge_1':max(map(abs,endpoint[1:]))}
        # Broad independent physical grid, plus exact vertical axis. Horizontal zeros excluded geometrically, no threshold.
        logr=np.unique(np.r_[np.linspace(-18,18,91),np.log([.01,.1,1.,10.,100.,1e6,1e12])])
        theta=np.unique(np.r_[.0003,.003,.03,(np.arange(49)+.5)*math.pi/98,math.pi/2])
        row['grid_log_radius']=logr.tolist();row['grid_theta']=theta.tolist()
        previous=None;peaks=[]
        for order in (128,256):
            z=grid(mod,logr,theta,order,cw,C,cx);s,pp=summary(z,logr,theta);peaks=pp
            r={'order':order,'summary':s,'points':len(logr)*len(theta),'identity_scaled_error':float(np.max(abs(z['identity_error'])/(1+abs(z['R']))))}
            if previous is not None:r['inverse_difference_over_Nf']=float(np.max(abs(z['R']-previous['R'])/z['Nf']))
            row['grid'].append(r);previous=z;checkpoint()
            print(json.dumps({'utc':utc(),'snapshot':source.name,'order':order,'c_error':row['c_difference'],'core':s['core']['R_Nf'],'annulus':s['annulus']['R_Nf']}),flush=True)
        points=[peaks[0],peaks[1],[.03,.07],[0.,.25],[.6, .8],[6.,8.]]
        # Kernel quadrature and FD8 use unscaled fields, then normalize algebraically.
        for nr,nt,ne,outer in ((40,256,144,4.),(64,512,224,8.)):
            inv=DirectInverse(q.rho,Quadrature(nr,nt,ne,outer,q.L*2**(-q.kappa),q.p,16*q.L,q.kappa))
            values=[]
            for x,y in points:
                rawrho=float(q.rho(x,y));U=inv.velocity(x,y);samples=[]
                for h in (.003,.0015,.00075):
                    gx,gy=map(float,cartesian_gradient(q.rho,x,y,h,0.));tx=(C*x+U[0]/cw)*gx/cw;ty=(C*y+U[1]/cw)*gy/cw
                    R=tx+ty-rawrho/cw;nf=abs(tx)+abs(ty)+abs(rawrho/cw);nv=abs(rawrho/cw)+abs(x*gx+y*gy)/cw+abs(U[0]*gx+U[1]*gy)/cw**2
                    samples.append({'h':h,'gradient':[gx,gy],'R':R,'Nf':nf,'Nv':nv,'R_Nf':abs(R)/nf,'R_Nv':abs(R)/nv})
                values.append({'point':[x,y],'raw_rho':rawrho,'raw_U':U.tolist(),'residuals':samples})
            row['direct_checks'].append({'quadrature':[nr,nt,ne,outer],'points':values});checkpoint()
            print(json.dumps({'utc':utc(),'snapshot':source.name,'direct_quadrature':[nr,nt,ne,outer],'points':len(values)}),flush=True)
        # Exact quotient coefficients; no float normalization repair.
        cc=[[F(float(v))/F(cw)for v in c]for c in q.coeff]
        for digits in (55,85):
            with mp.workdps(digits+guard_digits(q.N,q.M,q.kappa)):
                mpmodel=MPQPrimitives(cc,F(q.L),F(q.kappa),F(C))
                pr={'digits':digits,'working_digits':mp.mp.dps,'a':mp.nstr(mpmodel.a,digits),'c':mp.nstr(mpmodel.c,digits),'delta':mp.nstr(mpmodel.delta,digits),'points':[]}
                for x,y in points:
                    pr['points'].append(mp_value(mpmodel.at(x,y),digits))
                row['multiprecision'].append(pr);checkpoint()
                print(json.dumps({'utc':utc(),'snapshot':source.name,'mp_digits':digits,'points':len(points)}),flush=True)
        with mp.workdps(110):
            pairs=[]
            for a,b in zip(row['multiprecision'][0]['points'],row['multiprecision'][1]['points']):
                errors={k:mp.nstr(abs(mp.mpf(a[k])-mp.mpf(b[k]))/(1+abs(mp.mpf(b[k]))),25)for k in ['R','Nf','Nv','R_Nf','R_Nv']}
                pairs.append({'point':[b['x'],b['y']],'errors':errors})
            row['precision_comparisons']=pairs
        row['elapsed_seconds']=time.monotonic()-start;row['status']='COMPUTED';checkpoint()
    result['status']='COMPUTED';result['finished_utc']=utc();checkpoint()
if __name__=='__main__':main()
