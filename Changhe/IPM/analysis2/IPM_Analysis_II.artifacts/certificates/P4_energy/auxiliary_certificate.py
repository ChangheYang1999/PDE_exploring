"""Certificates for coefficient matrices in L2 and first-derivative estimates."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,json,time
from flint import arb,arb_mat,ctx
import compact_certificate as cc
from compact_matrix import A
cc.NT=30;cc.NZ=12


def load(state,quantity):
    d=json.loads(Path(__file__).with_name(f'state{state:03d}_auxiliary_polynomials.json').read_text())
    tt=cc.transforms(cc.NT);tz=cc.transforms(cc.NZ,Q(-1),Q(1)).transpose()
    P={}
    for key,items in d['polynomials'].items():
        M=arb_mat(cc.NT+1,cc.NZ+1)
        for i,k,v in items:M[i,k]=A(v)
        P[key]=tt*M*tz
    B={}
    for j in range(4):
        def p(label):return P[f'{label}_{j}']
        if quantity=='A':
            B['a',j]=-p('chi22')-p('chi04')
            B['b',j]=arb_mat(cc.NT+1,cc.NZ+1)
            B['c',j]=(p('chi31')+p('chi13'))/2
            base=arb(0);target=-arb(1)/20
        elif quantity=='DU':
            B['a',j]=p('chi22');B['b',j]=-p('chi22')
            B['c',j]=(p('chi13')-p('chi31'))/2
            base=arb(17)/20;target=arb(0)
        elif quantity=='N':
            B['a',j]=(p('chi24')+p('chi06'))/2
            B['b',j]=(p('chi42')+p('chi24'))/2
            B['c',j]=-(p('chi33')+p('chi15'))/2
            base=arb(100);target=arb(0)
        else:raise ValueError(quantity)
    return d,B,base,target

def factored_bounds(B,tlo,thi,zlo,zhi,delta,base):
    from math import comb
    wl=(1-A(thi))**(A(delta)/2);wu=(1-A(tlo))**(A(delta)/2)
    W=arb_mat([[sum((A(Q(comb(j,k)*comb(i,k),comb(3,k)))*wl**(j-k)*(wu-wl)**k for k in range(min(i,j)+1)),arb(0)) for j in range(4)] for i in range(4)])
    out={}
    for label in ('a','b','c'):
        coeff=arb_mat([B[label,j].entries() for j in range(4)])
        out[label]=cc.hull((W*coeff).entries())
    alo,ahi=out['a'];blo,bhi=out['b'];clo,chi=out['c']
    sine=arb(1) if zlo<=0<=zhi else (1-A(min(abs(zlo),abs(zhi)))**2).sqrt()
    off=abs(clo).max(abs(chi))*sine
    lc=(alo+blo-((alo-blo)**2+4*off**2).sqrt())/2
    lc=lc.max(alo.min(blo)-off)
    return base+(wl*lc).min(wu*lc),out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--state',type=int,default=131);ap.add_argument('--quantity',choices=['A','DU','N'],required=True);ap.add_argument('--seconds',type=int,default=480);ap.add_argument('--factor',action='store_true');args=ap.parse_args()
    ctx.prec=320;start=time.monotonic();d,B,base,target=load(args.state,args.quantity)
    delta=Q(d['delta']);Lt,Rt=cc.split_matrices(cc.NT);Lz,Rz=cc.split_matrices(cc.NZ)
    stack=[(B,Q(0),Q(1),Q(-1),Q(1),'',0,0)];accepted=[];failed=[];processed=0;worst=base
    while stack and time.monotonic()-start<args.seconds:
        b,tl,th,zl,zh,path,dt,dz=stack.pop();processed+=1
        lower,ranges=factored_bounds(b,tl,th,zl,zh,delta,base) if args.factor else cc.bounds(b,tl,th,zl,zh,delta,base,tight=True)
        if lower>=target:
            accepted.append({'path':path,'t':[str(tl),str(th)],'z':[str(zl),str(zh)],'lower':lower.str(50)});worst=worst.min(lower)
        elif dt+dz>=36:failed.append({'path':path,'lower':lower.str(50)})
        else:
            axis='t' if dt<=dz+2 else 'z'
            if axis=='t':
                left,right=cc.split(b,axis,Lt,Rt);tm=(tl+th)/2
                stack.extend([(right,tm,th,zl,zh,path+'T',dt+1,dz),(left,tl,tm,zl,zh,path+'t',dt+1,dz)])
            else:
                left,right=cc.split(b,axis,Lz,Rz);zm=(zl+zh)/2
                stack.extend([(right,tl,th,zm,zh,path+'Z',dt,dz+1),(left,tl,th,zl,zm,path+'z',dt,dz+1)])
        if processed%500==0:print(args.state,args.quantity,processed,len(accepted),len(failed),len(stack),'seconds',round(time.monotonic()-start,2),flush=True)
    status='COMPLETE' if not stack and not failed else 'INCOMPLETE'
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'state':args.state,'quantity':args.quantity,'factored':args.factor,'status':status,'precision':ctx.prec,'base':base.str(30),'target':target.str(30),'input_sha256':d['input_sha256'],'processed':processed,'pending':len(stack),'elapsed_seconds':time.monotonic()-start,'worst_accepted':worst.str(50),'accepted':accepted,'failed':failed,'pending_paths':[node[5] for node in stack]}
    Path(__file__).with_name(f'state{args.state:03d}_aux_{args.quantity}'+('_factored' if args.factor else '')+'_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(args.state,args.quantity,status,processed,len(accepted),len(failed),len(stack),'seconds',out['elapsed_seconds'],'worst',out['worst_accepted'],flush=True)
if __name__=='__main__':main()
