"""Packet187 generator: exact Cox cell polynomials and rational area integrals."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import hashlib,io,json,sys,time
import numpy as np
from exact_temperature_certificate import spline_span
import modal_norm_power as iv
CORE=Path('verification/fixed_velocity_block_20261021T0056/source_snapshots/bq3core.py')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def export(path,target):
    path=Path(path).resolve();blob=path.read_bytes()
    with np.load(io.BytesIO(blob),allow_pickle=False)as a:
        d=int(a['deg']);nt=int(a['Nt']);K=int(a['K']);grade=float(a['grade']);ts=np.concatenate((np.zeros(d),np.linspace(0,1,nt+1)**grade,np.ones(d))).astype('<f8')
        assert str(a['rmap'].item())=='r2' and str(a['scheme'].item())=='mask' and int(a['mreg'])==2
        assert all(a[k].dtype==np.dtype('float64')for k in ['cG','beta','beta_basis','L','grade'])
        assert a['cG'].shape in [(K*(nt+d),),(K,nt+d)]
        raw=a['cG'].reshape(K,nt+d);assert np.isfinite(raw).all()and np.isfinite(ts).all()
        declared=dict(s.split(':',1)for s in a['code_sha256'].tolist());assert declared['bq3core.py']==sha(CORE)
        data={'schema':'exact-full-modal-G-v1','archive_path':str(path),'archive_sha256':hashlib.sha256(blob).hexdigest(),'source_core_path':str(CORE.resolve()),'source_core_sha256':sha(CORE),'degree':d,'Nt':nt,'K':K,'grade':str(Q.from_float(grade)),'basis_beta':str(Q.from_float(float(a['beta_basis']))),'beta':str(Q.from_float(float(a['beta']))),'L':str(Q.from_float(float(a['L']))),'knots':[str(Q.from_float(float(x)))for x in ts],'knot_binary_little_endian_sha256':hashlib.sha256(ts.tobytes()).hexdigest(),'coefficients':[[str(Q(0)if j<k//2 else Q.from_float(float(raw[k,j])))for j in range(nt+d)]for k in range(K)],'definition':'Exact binary-rational coefficients and generated binary-rational knots; odd modes carry rho. b is beta_basis. No floating subtraction.'}
    target.write_text(json.dumps(data,indent=2)+'\n');return data

def poly_square(p):
    q=[Q(0)]*(2*len(p)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(p):q[i+j]+=a*b
    return q

def aggregate(polys,d):
    out=[[Q(0)]*(2*d+1)for _ in range(4)]
    for k,p in enumerate(polys):
        sq=poly_square(p)
        for j,c in enumerate(sq):
            out[0][j]+=(2 if k==0 else 1)*c
            out[2][j]+=k*k*c
            if k%2:out[1][j]+=c;out[3][j]+=k*k*c
    return out

def integrate_aggregates(ag,lo,hi,b):
    N=(2*b).numerator//(2*b).denominator;alpha=2*b-N;p0=iv.power(lo,alpha);p1=iv.power(hi,alpha);ans=[]
    for even,odd in [(ag[0],ag[1]),(ag[2],ag[3])]:
        val=Q(0);tail=(Q(0),Q(0))
        for j,c in enumerate(even):val+=c*(hi**(j+2)-lo**(j+2))/(j+2)
        for j,c in enumerate(odd):tail=iv.add(tail,iv.mulq(iv.sub(iv.mulq(p1,hi**(N+j+2)),iv.mulq(p0,lo**(N+j+2))),c/(2*b+j+2)))
        ans.append(iv.outward(iv.sub((val,val),tail)))
    return ans

def generate(xs):
    a,b=xs;d=a['degree'];assert all(a[k]==b[k]for k in ['basis_beta','L','degree','knots','knot_binary_little_endian_sha256'])
    beta=Q(a['basis_beta']);assert beta>0 and Q(a['L'])>0
    knots=list(map(Q,a['knots']));K=max(a['K'],b['K']);cells=[];total=[[(Q(0),Q(0))for j in range(2)]for field in range(3)]
    for span in range(d,len(knots)-d-1):
        if knots[span]==knots[span+1]:continue
        families=[]
        for x in xs:
            A,B,local=spline_span(x,span);w=B-A;polys=[]
            for p in local:
                z=[Q(0)]*(d+1)
                for (i,j),c in p.items():
                    assert j==0
                    for n in range(i+1):z[n]+=c*comb(i,n)*(1-A)**(i-n)*(-1)**n/w**i
                polys.append(z)
            polys.extend([[Q(0)]*(d+1)for _ in range(K-len(polys))]);families.append(polys)
        families.append([[v-w for v,w in zip(p,q)]for p,q in zip(*families)])
        vals=[]
        for i,polys in enumerate(families):
            val=integrate_aggregates(aggregate(polys,d),1-B,1-A,beta);vals.append([iv.serialize(z)for z in val])
            for j in range(2):total[i][j]=iv.add(total[i][j],val[j])
        cells.append({'span':span,'t_interval':[str(A),str(B)],'z_interval':[str(1-B),str(1-A)],'polynomials_z':[[list(map(str,p))for p in polys]for polys in families[:2]],'integrals_I0_I1':vals})
        if len(cells)%8==0:print('generated cells',len(cells),flush=True)
    total=[[iv.outward((max(Q(0),z[0]),z[1]))for z in row]for row in total];relative=[]
    for j in range(2):
        de=total[2][j];ref=total[1][j];assert ref[0]>0
        relative.append((iv.square_root(de[0]/ref[1])[0],iv.square_root(de[1]/ref[0])[1]))
    return {'schema':'full-modal-area-norm-v1','basis_beta':a['basis_beta'],'L':a['L'],'degree':d,'mode_count':K,'quadrature':'Exact area integrals, all r from0 toinfinity, full angular orthogonality. G=Omega/x, fixed-r dphiG.','precision':{'bits':iv.BITS,'log_terms':iv.NLOG,'exp_degree':iv.NEXP},'cells':cells,'norm_squared_over_pi_b_L2':[[iv.serialize(z)for z in row]for row in total],'relative_L2_to_second':list(map(iv.serialize,relative))}

def main():
    root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True);started=datetime.now(timezone.utc).isoformat();t=time.monotonic();xs=[];inputs=[]
    for i,path in enumerate(sys.argv[2:]):
        p=root/f'input{i}.json';xs.append(export(path,p));inputs.append({'path':str(p.resolve()),'sha256':sha(p)})
    assert len(xs)==2
    result=generate(xs);result.update(inputs=inputs,created_utc=datetime.now(timezone.utc).isoformat(),started_utc=started,elapsed_seconds=time.monotonic()-t,generator_sha256=sha(__file__))
    p=root/'certificate.json';p.write_text(json.dumps(result,indent=2)+'\n');print('COMPUTED',result['elapsed_seconds'],[[[float(Q(v))for v in z]for z in row]for row in result['norm_squared_over_pi_b_L2']],[[float(Q(v))for v in z]for z in result['relative_L2_to_second']],flush=True)
if __name__=='__main__':main()
