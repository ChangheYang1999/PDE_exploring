"""Whole-plane M>=19/5 certificate for an exact refit; all acceptance in Arb."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,json,time,hashlib
from flint import arb,arb_mat,ctx
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'02_energy/verification'))
from compact_matrix import A,add,derivative,chebyshev,encode
from compact_certificate import transforms,split_matrices,split,bounds

def construct(data):
    delta=1-1/Q(data['cl']);polys={}
    assert max(j for j,m,k in data['canonical_order'])==3
    for label,axes in [('chi22','xxyy'),('chi04','yyyy'),('chi31','xxxy')]:
        for branch in range(4):
            trig={};p=(4-(branch+1)*delta)/2
            for (j,m,k),a in zip(data['canonical_order'],data['canonical_coefficients']):
                if j!=branch:continue
                T={('c',2*m,0):Q(a)}
                for di,axis in enumerate(axes):T=derivative(T,p,k,di,axis)
                for (kind,n,l),v in T.items():add(trig,kind,n,k-2+l,v)
            assert all(l>=0 for kind,n,l in trig)
            P={}
            for (kind,n,l),v in trig.items():
                assert n%2==0 and kind==('s' if label=='chi31' else 'c')
                C=chebyshev(n//2-1,'U') if kind=='s' else chebyshev(n//2)
                for zdeg,c in enumerate(C):P[l,zdeg]=P.get((l,zdeg),Q(0))+v*c
            polys[label,branch]={key:v for key,v in P.items() if v}
    return delta,polys

def initial(polys,nt,nz):
    tt=transforms(nt);tz=transforms(nz,Q(-1),Q(1)).transpose();blocks={}
    for key,P in polys.items():
        M=arb_mat(nt+1,nz+1)
        for (i,j),v in P.items():M[i,j]=A(v)
        blocks[key]=tt*M*tz
    B={}
    for j in range(4):
        B['a',j]=-2*blocks['chi22',j]-blocks['chi04',j]
        B['b',j]=blocks['chi22',j];B['c',j]=blocks['chi31',j]
    return B

def run(name):
    ctx.prec=320;start=time.monotonic()
    data=json.loads((HERE/f'{name}_audit.json').read_text());delta,P=construct(data)
    nt=max(i for p in P.values() for i,j in p);nz=max(j for p in P.values() for i,j in p)
    outp={'source_sha256':data['source_sha256'],'canonical_sha256':data['canonical_sha256'],'delta':str(delta),'nt':nt,'nz':nz,'polynomials':{f'{label}_{j}':encode(p) for (label,j),p in P.items()}}
    (HERE/f'{name}_matrix_polynomials.json').write_text(json.dumps(outp,indent=2)+'\n')
    print('constructed',name,nt,nz,'seconds',time.monotonic()-start,flush=True)
    B=initial(P,nt,nz);Lt,Rt=split_matrices(nt);Lz,Rz=split_matrices(nz)
    base=2*A(data['cl'])+1;target=A(Q(19,5))
    stack=[(B,Q(0),Q(1),Q(-1),Q(1),'')];good=[];bad=[];count=0
    while stack and time.monotonic()-start<480:
        b,tl,th,zl,zh,path=stack.pop();count+=1
        low,_=bounds(b,tl,th,zl,zh,delta,base,True)
        if low>=target:
            good.append({'path':path,'t':[str(tl),str(th)],'z':[str(zl),str(zh)],'lower':low.str(55)})
        elif len(path)>=36:bad.append(path)
        else:
            bm={};scores={}
            for ax,L,R in [('t',Lt,Rt),('z',Lz,Rz)]:
                left,right=split(b,ax,L,R)
                if ax=='t':
                    mid=(tl+th)/2
                    children=[(left,tl,mid,zl,zh,path+'t'),(right,mid,th,zl,zh,path+'T')]
                else:
                    mid=(zl+zh)/2
                    children=[(left,tl,th,zl,mid,path+'z'),(right,tl,th,mid,zh,path+'Z')]
                values=[bounds(ch[0],*ch[1:5],delta,base,True)[0] for ch in children]
                bm[ax]=children;scores[ax]=min(float(v.mid()) for v in values)
            ax=max(scores,key=scores.get);stack.extend(reversed(bm[ax]))
        if count%100==0:print(name,count,'good',len(good),'bad',len(bad),'pending',len(stack),'seconds',time.monotonic()-start,flush=True)
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'name':name,'source_sha256':data['source_sha256'],'canonical_sha256':data['canonical_sha256'],'status':'COMPLETE' if not stack and not bad else 'INCOMPLETE','target':'19/5','precision':ctx.prec,'nt':nt,'nz':nz,'accepted':good,'failed':bad,'pending':[x[-1] for x in stack],'elapsed_seconds':time.monotonic()-start}
    (HERE/f'{name}_matrix_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(name,out['status'],'leaves',len(good),'seconds',out['elapsed_seconds'],flush=True)

if __name__=='__main__':run(sys.argv[1])
