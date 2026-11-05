#!/usr/bin/env python3
"""Rigorous scalar prices for proved Gaussian-commutator operator bounds.

Default background bounds are explicit assumptions, not certificates for the
actual field. A later consumer may substitute completed actual certificates.
"""
import argparse,json,math
from pathlib import Path
from flint import arb,ctx
ctx.prec=256
def poly_add(x,y):
    z=[arb(0)]*max(len(x),len(y))
    for i,a in enumerate(x):z[i]+=a
    for i,a in enumerate(y):z[i]+=a
    return z
def poly_scale(x,a):return [a*v for v in x]
def poly_mul(x,y):
    z=[arb(0)]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):z[i+j]+=a*b
    return z
def L1(poly,mu):
    return sum((c*(arb(2).sqrt()/mu)**k*(1+arb(k)/2).gamma() for k,c in enumerate(poly)),arb(0))
def L2(poly,mu):
    pp=poly_mul(poly,poly)
    val=sum((c*mu**(2-k)*(1+arb(k)/2).gamma()/(4*arb.pi()) for k,c in enumerate(pp)),arb(0))
    return val.sqrt()

def interpolate(S,q=arb(21)/10):
    A2=S[0]+arb(2).sqrt()*S[2]
    A3=(A2*A2+(S[1]+arb(2).sqrt()*S[3])**2).sqrt()
    return A2**(3-q)*A3**(q-2),A2,A3

def price(mu,slope,B0,B1,D2b,D3b,D2xb,D4xb):
    mu=arb(mu);a=arb(slope);B0=arb(B0);B1=arb(B1)
    D2b=arb(D2b);D3b=arb(D3b);D2xb=arb(D2xb);D4xb=arb(D4xb)
    # Tensor derivative bounds for W_a; d3<2a³ follows from its explicit formula.
    d=[None,a,arb(2).sqrt()*a*a,2*a**3]
    w=[arb(1),a/2,d[2],d[3]]
    G=[[arb(1)],[0,mu*mu],[arb(2).sqrt()*mu*mu,0,mu**4],[0,2*arb(3).sqrt()*mu**4,0,mu**6]]
    ratio=[arb(1),a]
    # [W,P]Jq: direct J², gradient-J² estimates are sharper than generic tensor contraction.
    Er=(arb.pi()/2).sqrt()/mu;gradp=mu*(arb.pi()/2).sqrt()
    A2W=a*Er+a*5*(2*arb.pi()).sqrt()*mu/2+2*a*a+2*a*gradp
    AGW=3*a+2*arb(2).sqrt()*a**3+4*a*a*gradp+a*(20+2*arb(2).sqrt()+4/arb(1).exp())*mu*mu
    A3W=(A2W*A2W+AGW*AGW).sqrt()
    KW=A2W**arb('0.9')*A3W**arb('0.1')
    # Weighted derivative L2 inputs use the exact tensor commutator identity
    # ||xD^j b||²=||D^j(xb)||²-j(j-1)||D^(j-1)b||².
    W2=(D2b*D2b+a*a*D2xb*D2xb).sqrt()
    W3=(D3b*D3b+a*a*D2xb*D4xb).sqrt()
    middle=[]
    for j in range(4):
        polys={0:[arb(0)],2:[arb(0)],3:[arb(0)]}
        for l in range(j+1):
            # Background index0 stands for B1 and its path difference.
            f=poly_scale(poly_mul([0,1],ratio),w[l])
            if l>=1:f=poly_add(f,[l*w[l-1]])
            polys[0]=poly_add(polys[0],poly_scale(poly_mul(f,G[j-l]),math.comb(j,l)))
            for k in [2,3]:
                if l>=k:
                    polys[k]=poly_add(polys[k],poly_scale(G[j-l],math.comb(j,l)*math.comb(l,k)*w[l-k]))
        middle.append(B1*L1(polys[0],mu)+W2*L2(polys[2],mu)+W3*L2(polys[3],mu))
    KB,A2B,A3B=interpolate(middle)
    third=[]
    for j in range(4):
        polys={k:[arb(0)] for k in range(4)}
        for l in range(j+1):
            for k in range(l+1):
                f=[0,a*math.comb(l,k)*w[l-k]]
                for z in range(1,l-k+1):
                    f=poly_add(f,[math.comb(l,z)*d[z]*math.comb(l-z,k)*w[l-z-k]])
                f=poly_mul(ratio,f)
                polys[k]=poly_add(polys[k],poly_scale(poly_mul(f,G[j-l]),math.comb(j,l)))
        third.append(B0*L1(polys[0],mu)+B1*L1(polys[1],mu)+D2b*L2(polys[2],mu)+D3b*L2(polys[3],mu))
    KT,A2T,A3T=interpolate(third)
    K1=arb(3).sqrt()*B0*KW
    K2=(arb(3).sqrt()+1)*KB
    K3=arb(3).sqrt()*KT
    Ksum=K1+K2+K3
    Ld=B1+a*B0
    # Symmetric kernel contains one W difference and a factor1/2.
    epsilon=a*(1+arb(2).sqrt())*Ld/(mu*mu)
    return {'mu':str(mu),'weight_slope':str(a),'Ld_assumed_upper':Ld.str(60),'weighted_D2b_L2_upper':W2.str(60),'weighted_D3b_L2_upper':W3.str(60),
            'KW':KW.str(60),'KB':KB.str(60),'KT':KT.str(60),'weak_K1':K1.str(60),'weak_K2':K2.str(60),'weak_K3':K3.str(60),'weak_Ksum':Ksum.str(60),
            'high_cross_epsilon':epsilon.str(60),'rate_high_plus_weak_at_R_over_M_1e6':(epsilon+Ksum/10**6).str(60),
            'Young_C_at_epsilon_002':(Ksum*Ksum/arb('.08')).str(60),
            'warning':'High/cross comparison E[G]-E[PmuG] only. The low form E[PmuG] is not bounded by this calculation.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).with_suffix('.json'))
    ap.add_argument('--B0',default='12');ap.add_argument('--B1',default='20')
    ap.add_argument('--D2b',default='12');ap.add_argument('--D3b',default='40')
    ap.add_argument('--D2xb',default='70');ap.add_argument('--D4xb',default='400');args=ap.parse_args()
    assumptions={k:getattr(args,k) for k in ['B0','B1','D2b','D3b','D2xb','D4xb']}
    rows=[price(mu,a,**assumptions) for a in ['2','5/4'] for mu in [20,30,40,50,60,80,100]]
    out={'status':'RIGOROUS_SCALAR_PRICES_GIVEN_EXPLICIT_UNVERIFIED_BACKGROUND_ASSUMPTIONS','assumed_background_bounds':assumptions,'rows':rows,'scope':'Formula constants and scalar interval arithmetic only; default field inputs are assumptions awaiting actual certificates, and the low-frequency Ew form is not controlled.'}
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    for r in rows:print(r['mu'],r['weight_slope'],'high',r['high_cross_epsilon'],'weak',r['weak_Ksum'],'combined',r['rate_high_plus_weak_at_R_over_M_1e6'])

if __name__=='__main__':main()
