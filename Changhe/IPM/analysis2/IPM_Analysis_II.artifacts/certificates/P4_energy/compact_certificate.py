"""Adaptive tensor Bernstein certificate on the compactified full quadrant.
All mathematical decisions use Arb intervals; floats appear only in progress displays.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import json,sys,time,argparse
from flint import arb,arb_mat,ctx
from compact_matrix import A

NT=28; NZ=11

def matrix(data):return arb_mat([[A(v) for v in row] for row in data])

def transforms(n,lo=Q(0),hi=Q(1)):
    return matrix([[sum((Q(comb(k,l)*comb(i,l),comb(n,l))*lo**(k-l)*(hi-lo)**l for l in range(min(i,k)+1)),Q(0)) for k in range(n+1)] for i in range(n+1)])

def split_matrices(n):
    left=matrix([[Q(comb(i,k),2**i) if k<=i else Q(0) for k in range(n+1)] for i in range(n+1)])
    right=matrix([[Q(comb(n-i,k-i),2**(n-i)) if k>=i else Q(0) for k in range(n+1)] for i in range(n+1)])
    return left,right

def load(state):
    path=Path(__file__).with_name(f'state{state:03d}_compact_polynomials.json')
    d=json.loads(path.read_text())
    tt=transforms(NT);tz=transforms(NZ,Q(-1),Q(1)).transpose()
    blocks={}
    for label in ('chi22','chi04','chi31'):
        for j in range(4):
            P=arb_mat(NT+1,NZ+1)
            for i,k,v in d['polynomials'][f'{label}_{j}']:P[i,k]=A(v)
            blocks[label,j]=tt*P*tz
    # Matrix entries other than the common diagonal base.
    B={}
    for j in range(4):
        B['a',j]=-2*blocks['chi22',j]-blocks['chi04',j]
        B['b',j]=blocks['chi22',j]
        B['c',j]=blocks['chi31',j]
    return d,B

def hull(values):
    values=iter(values);first=next(values);lo=first;hi=first
    for v in values:lo=lo.min(v);hi=hi.max(v)
    return lo.lower(),hi.upper()

def wcoeff(wl,wu):
    # Degree-four Bernstein transform of a polynomial with zero constant term.
    out=[]
    for i in range(5):
        row=[]
        for j in range(1,5):
            row.append(sum((A(Q(comb(j,k)*comb(i,k),comb(4,k)))*wl**(j-k)*(wu-wl)**k for k in range(min(i,j)+1)),arb(0)))
        out.append(row)
    return arb_mat(out)

def bounds(B,tlo,thi,zlo,zhi,delta,base,tight=False):
    wl=(1-A(thi))**(A(delta)/2);wu=(1-A(tlo))**(A(delta)/2)
    W=wcoeff(wl,wu);out={}
    for label in ('a','b','c'):
        coeff=arb_mat([B[label,j].entries() for j in range(4)])
        out[label]=hull((W*coeff).entries())
    alo,ahi=out['a'];blo,bhi=out['b'];clo,chi=out['c']
    if zlo<=0<=zhi:sine=arb(1)
    else:sine=(1-A(min(abs(zlo),abs(zhi)))**2).sqrt()
    coff=abs(clo).max(abs(chi))*sine
    lower=base+alo.min(blo)-coff
    # A second lower bound from trace and spectral radius, using enclosing entries.
    # Lower both diagonals simultaneously. For any vector, the off-diagonal
    # contribution is bounded below by -2*coff*abs(v1*v2).
    if tight:
        spectral=base+(alo+blo-((alo-blo)**2+4*coff**2).sqrt())/2
    else:
        av=alo.union(ahi);bv=blo.union(bhi)
        diff=abs(av-bv).upper()
        spectral=base+(alo+blo-(diff**2+4*coff**2).sqrt())/2
    return lower.max(spectral),out

def split(B,axis,L,R):
    if axis=='t':return ({key:L*value for key,value in B.items()},{key:R*value for key,value in B.items()})
    return ({key:value*L.transpose() for key,value in B.items()},{key:value*R.transpose() for key,value in B.items()})

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--state',type=int,default=131);ap.add_argument('--target',default='3.5');ap.add_argument('--max-cells',type=int,default=200000);ap.add_argument('--max-depth',type=int,default=32);ap.add_argument('--seconds',type=int,default=480);args=ap.parse_args()
    ctx.prec=256;start=time.monotonic();d,B=load(args.state)
    sd=json.loads((Path(__file__).resolve().parents[2]/'source_audit'/f'state{args.state:03d}_exact.json').read_text())
    base=2*A(sd['exact_parameters']['cl'])+1;delta=Q(d['delta']);target=A(args.target)
    Lt,Rt=split_matrices(NT);Lz,Rz=split_matrices(NZ)
    stack=[(B,Q(0),Q(1),Q(-1),Q(1),'',0,0)]
    accepted=[];failed=[];processed=0;worst=base
    while stack and processed<args.max_cells and time.monotonic()-start<args.seconds:
        b,tl,th,zl,zh,path,dt,dz=stack.pop();processed+=1
        lower,ranges=bounds(b,tl,th,zl,zh,delta,base)
        if lower>=target:
            accepted.append({'path':path,'t':[str(tl),str(th)],'z':[str(zl),str(zh)],'lower':lower.str(45)})
            worst=worst.min(lower)
        elif dt+dz>=args.max_depth:
            failed.append({'path':path,'t':[str(tl),str(th)],'z':[str(zl),str(zh)],'lower':lower.str(45)})
        else:
            # Both dimensions shrink geometrically. t has higher polynomial degree.
            axis='t' if dt<=dz+2 else 'z'
            if axis=='t':
                left,right=split(b,axis,Lt,Rt);tm=(tl+th)/2
                stack.extend([(right,tm,th,zl,zh,path+'T',dt+1,dz),(left,tl,tm,zl,zh,path+'t',dt+1,dz)])
            else:
                left,right=split(b,axis,Lz,Rz);zm=(zl+zh)/2
                stack.extend([(right,tl,th,zm,zh,path+'Z',dt,dz+1),(left,tl,th,zl,zm,path+'z',dt,dz+1)])
        if processed%100==0:print('cells',processed,'accepted',len(accepted),'failed',len(failed),'pending',len(stack),'seconds',round(time.monotonic()-start,2),'worst',worst.str(10),flush=True)
    status='COMPLETE' if not stack and not failed else 'INCOMPLETE'
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'state':args.state,'status':status,'target':args.target,'precision':ctx.prec,'input_sha256':d['input_sha256'],'processed':processed,'pending':len(stack),'elapsed_seconds':time.monotonic()-start,'worst_accepted':worst.str(50),'accepted':accepted,'failed':failed,'pending_paths':[node[5] for node in stack]}
    dest=Path(__file__).with_name(f'state{args.state:03d}_compact_certificate.json')
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(status,processed,len(accepted),len(failed),len(stack),'seconds',out['elapsed_seconds'],'worst',out['worst_accepted'],flush=True)

if __name__=='__main__':main()
