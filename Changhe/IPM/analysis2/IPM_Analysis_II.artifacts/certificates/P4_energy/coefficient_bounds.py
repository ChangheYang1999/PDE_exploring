"""Global derivative bounds on the independently certified DU partition."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,sys,time
from flint import arb,arb_mat,ctx
import compact_certificate as cc
from compact_matrix import A
cc.NT=30;cc.NZ=12
FIELDS={
    'rho_x':({'chi31':-1,'chi13':-1},True),
    'rho_y':({'chi22':-1,'chi04':-1},False),
    'rho_xxx':({'chi51':-1,'chi33':-1},True),
    'rho_xxy':({'chi42':-1,'chi24':-1},False),
    'rho_xyy':({'chi33':-1,'chi15':-1},True),
    'rho_yyy':({'chi24':-1,'chi06':-1},False),
    'chi22':({'chi22':1},False),'chi31':({'chi31':1},True),'chi13':({'chi13':1},True),
    'chi51':({'chi51':1},True),'chi42':({'chi42':1},False),'chi33':({'chi33':1},True),'chi24':({'chi24':1},False),'chi15':({'chi15':1},True),
}

def run(state):
    ctx.prec=320;start=time.monotonic()
    here=Path(__file__).resolve().parent
    d=json.loads((here/f'state{state:03d}_auxiliary_polynomials.json').read_text());delta=Q(d['delta'])
    cert=json.loads((here/f'state{state:03d}_aux_DU_certificate.json').read_text());assert cert['status']=='COMPLETE'
    leaves={row['path']:row for row in cert['accepted']}
    tt=cc.transforms(cc.NT);tz=cc.transforms(cc.NZ,Q(-1),Q(1)).transpose();P={}
    for key,items in d['polynomials'].items():
        M=arb_mat(cc.NT+1,cc.NZ+1)
        for i,k,v in items:M[i,k]=A(v)
        P[key]=tt*M*tz
    B={}
    for field,(terms,sine) in FIELDS.items():
        for j in range(4):B[field,j]=sum((factor*P[f'{label}_{j}'] for label,factor in terms.items()),arb_mat(cc.NT+1,cc.NZ+1))
    Lt,Rt=cc.split_matrices(cc.NT);Lz,Rz=cc.split_matrices(cc.NZ)
    global_bounds={field:arb(0) for field in FIELDS};records=[]
    def visit(b,path,tl,th,zl,zh):
        if path not in leaves:
            kids={q[len(path)] for q in leaves if q.startswith(path)}
            assert kids in ({'t','T'},{'z','Z'})
            axis='t' if kids=={'t','T'} else 'z'
            left,right=cc.split(b,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz)
            if axis=='t':
                tm=(tl+th)/2;visit(left,path+'t',tl,tm,zl,zh);visit(right,path+'T',tm,th,zl,zh)
            else:
                zm=(zl+zh)/2;visit(left,path+'z',tl,th,zl,zm);visit(right,path+'Z',tl,th,zm,zh)
            return
        row=leaves[path];assert list(map(Q,row['t']))==[tl,th] and list(map(Q,row['z']))==[zl,zh]
        W=cc.wcoeff((1-A(th))**(A(delta)/2),(1-A(tl))**(A(delta)/2));local={}
        sine=arb(1) if zl<=0<=zh else (1-A(min(abs(zl),abs(zh)))**2).sqrt()
        for field,(_,is_sine) in FIELDS.items():
            coeff=arb_mat([b[field,j].entries() for j in range(4)])
            lo,hi=cc.hull((W*coeff).entries());upper=abs(lo).max(abs(hi))
            if is_sine:upper*=sine
            global_bounds[field]=global_bounds[field].max(upper)
            local[field]=upper.str(45)
        records.append({'path':path,'upper_bounds':local})
    visit(B,'',Q(0),Q(1),Q(-1),Q(1))
    summary={k:v.str(50) for k,v in global_bounds.items()}
    G=global_bounds['rho_x'].max(global_bounds['rho_y']);H=arb(0);J=arb(0);K=arb(0)
    for label in ('rho_xxx','rho_xxy','rho_xxyy','rho_yyy'):
        if label in global_bounds:H=H.max(global_bounds[label])
    H=H.max(global_bounds['rho_xyy'])
    for label in ('chi22','chi31','chi13'):J=J.max(global_bounds[label])
    for label in ('chi51','chi42','chi33','chi24','chi15'):K=K.max(global_bounds[label])
    summary.update({'G_grad_rho_components':G.str(50),'H_third_rho_components':H.str(50),'J_DU_components':J.str(50),'K_third_U_components':K.str(50),'D2rho_Frobenius_squared_upper':(16*G*H).str(50),'D2U_tensor_squared_upper':(32*J*K).str(50)})
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'state':state,'input_sha256':d['input_sha256'],'precision':ctx.prec,'leaves':len(records),'method':'Exact polynomial coefficients, Arb tensor Bernstein bounds on a complete rational partition, plus the one-dimensional Landau inequality.','bounds':summary,'leaf_bounds':records,'elapsed_seconds':time.monotonic()-start}
    (here/f'state{state:03d}_coefficient_bounds.json').write_text(json.dumps(out,indent=2)+'\n')
    print(state,json.dumps(summary,indent=2),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 131)
