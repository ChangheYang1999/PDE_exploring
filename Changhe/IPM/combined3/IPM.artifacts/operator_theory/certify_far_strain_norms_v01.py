#!/usr/bin/env python3
"""Rigorous all-mode radial certificate for D2,D3,D4 of far strain.

Panel derivatives: actual Arb Taylor coefficients + source Cauchy majorants.
Endpoints: exact origin/far profile expansions + Gaussian erflog tails.
Only new combined3 files are written. Run with Python -B.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
import json
import math
from pathlib import Path
import sys
import time
from flint import arb,arb_series,fmpq as Q,ctx

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator,rational_arb
from asymptotics013 import Expansion
from far_strain_norms import FarStrain

def aa(x):
    x=F(x);return arb(x.numerator)/arb(x.denominator)
def upq(x):
    assert x.is_finite()
    return str(x.upper().fmpq())
def hashfile(p):return sha256(Path(p).read_bytes()).hexdigest()
def bindings():
    out={str(p.relative_to(HERE.parent)):hashfile(p) for p in
         [Path(__file__),HERE/'far_strain_norms.py',HERE.parent/'coercivity_residual/fields013.py',HERE.parent/'coercivity_residual/asymptotics013.py']}
    return out
def cut_disk_majorant(r,scale,near=False):
    """Bound |chi| (near=True) or |1-chi| on |z-r|<=r/8."""
    ell=arb(8).log()/(2*arb.pi().sqrt())
    Y=(arb(1)/8).asin()/ell
    if near:
        lo=((arb(7)*r/8)/(scale*arb(8).sqrt())).log()/ell
        hi=((arb(9)*r/8)/(scale*arb(8).sqrt())).log()/ell
    else:
        lo=-((arb(9)*r/8)/(scale*arb(8).sqrt())).log()/ell
        hi=-((arb(7)*r/8)/(scale*arb(8).sqrt())).log()/ell
    dist=arb(0) if lo<=0<=hi else min(abs(lo).abs_lower(),abs(hi).abs_lower())
    return lo.erfc()/2+Y/arb.pi().sqrt()*(Y*Y-dist*dist).exp()

def cauchy_panel(fs,k,j,subdiv,degree):
    lower=F(2)**k*(1+F(j,subdiv));upper=F(2)**k*(1+F(j+1,subdiv))
    center=(lower+upper)/2;h=(upper-lower)/2;r=aa(center);hh=aa(h)
    tick=time.monotonic()
    rr,entries=fs.strain_series(r,degree=degree+4)
    major,R=fs.e.mode_majorants(r)
    bound11=major['u1',1,0]
    keys=major['u1',0,1].keys()|major['u2',1,0].keys()
    bound12={key:(major['u1',0,1].get(key,arb(0))+major['u2',1,0].get(key,arb(0)))/2 for key in keys}
    cm=cut_disk_majorant(r,fs.strain_scale)
    inner=R/2;theta=hh/inner
    assert theta<1 and hh<r/8
    tball=arb(0,hh.abs_upper());rball=r+tball
    totals=[arb(0),arb(0),arb(0)];worst_tail=arb(0)
    for entry,bb in zip(entries,[bound11,bound12]):
        for key,poly in entry.items():
            kind,n=key
            if kind=='s' and n==0:continue
            assert poly.prec>=degree+5
            bm=bb.get(key,arb(0))*cm
            jets=[];pd=poly
            for order in range(5):
                val=arb(0)
                for cc in reversed(pd.coeffs()[:degree+5-order]):val=val*tball+cc
                rem=(math.factorial(order)*bm/inner**order*theta**(degree+5-order)/(1-theta)).abs_upper()
                worst_tail=max(worst_tail,rem)
                jets.append(val+arb(0,rem));pd=pd.derivative()
            f0,f1,f2,f3,f4=jets
            lap=f2+f1/rball-arb(n*n)*f0/rball**2
            lapr=f3+f2/rball-arb(1+n*n)*f1/rball**2+arb(2*n*n)*f0/rball**3
            laplap=f4+2*f3/rball-arb(1+2*n*n)*f2/rball**2+arb(1+2*n*n)*f1/rball**3+arb(n**4-4*n*n)*f0/rball**4
            vals=[lap.abs_upper()**2,
                  lapr.abs_upper()**2+arb(n*n)*lap.abs_upper()**2/rball.abs_lower()**2,
                  laplap.abs_upper()**2]
            angular=2*arb.pi() if n==0 else arb.pi()
            for z in range(3):totals[z]+=2*angular*aa(upper)*vals[z]*aa(upper-lower)
    return {'k':k,'j':j,'subdiv':subdiv,'degree':degree,'radius_interval':[str(lower),str(upper)],
            'energy_upper_exact':[upq(x) for x in totals],
            'max_jet_remainder_upper':upq(worst_tail),'seconds':time.monotonic()-tick}

def derivative_constants(n):
    a=528+n*n;b=25104+18*n*n
    c=1622544+1056*n*n+abs(n**4-4*n*n)
    return [arb(a*a),arb(b*b+n*n*a*a),arb(c*c)]

def gaussian_integral(power,C,end,ell,origin):
    """Integral r^(power-1) exp(-2 log(C/r or C*r)^2/ell²)."""
    if origin:
        t0=(C/end).log();b=-power;pref=C**power
    else:
        t0=(C*end).log();b=power;pref=C**(-power)
    return pref*(b*b*ell*ell/8).exp()*ell*arb.pi().sqrt()/(2*arb(2).sqrt())*(arb(2).sqrt()/ell*(t0-b*ell*ell/4)).erfc()

def end_tails(fs,rlo,rhi,exp_degree=18):
    ell=arb(8).log()/(2*arb.pi().sqrt());scale=fs.strain_scale
    gamma=1-arb(2251799813685248)/4076476460239181
    count=4*(162+1);constants=derivative_constants(162)
    def strain_point_bound(ex,r):
        b11=ex.point_bound('u1',1,0,r)
        b12=(ex.point_bound('u1',0,1,r)+ex.point_bound('u2',1,0,r))/2
        return max(b11,b12)
    tick=time.monotonic();ex0=Expansion(fs.e,'origin',degree=exp_degree)
    M0=strain_point_bound(ex0,arb(9)*rlo/8)
    C0=8*scale*arb(8).sqrt()/9
    x0=(C0/rlo).log()/ell;Y=(arb(1)/8).asin()/ell
    assert x0>0
    K0=(1/(2*x0)+Y*(Y*Y).exp())/arb.pi().sqrt()
    origins=[]
    for m,cc in zip([2,3,4],constants):
        origins.append(4*arb.pi()*count*M0*M0*K0*K0*cc*gaussian_integral(arb(2-2*m),C0,rlo,ell,True))
    print('origin_tail_complete',time.monotonic()-tick,flush=True)
    exf=Expansion(fs.e,'far',degree=exp_degree)
    Mf=strain_point_bound(exf,arb(7)*rhi/8)
    # On |z-r|<=r/8, |S_harmonic(z)|<=Mf*(r/rhi)^(-gamma).
    Cf=7/(8*scale*arb(8).sqrt());xf=(Cf*rhi).log()/ell
    assert xf>0
    Kf=(1/(2*xf)+Y*(Y*Y).exp())/arb.pi().sqrt()
    correction=[]
    for m,cc in zip([2,3,4],constants):
        correction.append((4*arb.pi()*count*Mf*Mf*rhi**(2*gamma)*Kf*Kf*cc*gaussian_integral(2-2*gamma-2*m,Cf,rhi,ell,False)).sqrt())
    cache={}
    def vel(name,i,j):
        key=name,i,j
        if key not in cache:cache[key]=exf.tail_L2_bound(name,i,j,rhi)
        return cache[key]
    def comp(i,j,laporder):
        terms=[]
        for l in range(laporder+1):
            coef=math.comb(laporder,l);dx=i+2*l;dy=j+2*(laporder-l)
            terms.append((coef,dx,dy))
        v11=sum((coef*vel('u1',dx+1,dy) for coef,dx,dy in terms),arb(0))
        v12=sum((coef*(vel('u1',dx,dy+1)+vel('u2',dx+1,dy))/2 for coef,dx,dy in terms),arb(0))
        return [v11,v12]
    b2=comp(0,0,1);b3=comp(1,0,1)+comp(0,1,1);b4=comp(0,0,2)
    exterior=[]
    for bb,err in zip([b2,b3,b4],correction):
        norm=(2*sum((x*x for x in bb),arb(0))).sqrt()+err
        exterior.append(norm*norm)
    print('exterior_tail_complete',time.monotonic()-tick,flush=True)
    return {'origin_energy_upper_exact':[upq(x) for x in origins],
            'exterior_energy_upper_exact':[upq(x) for x in exterior],
            'origin_source_complex_bound':str(M0),'exterior_source_complex_bound':str(Mf),
            'exterior_chi_correction_norm_upper_arb':[str(x) for x in correction],
            'expansion_degree':exp_degree,'seconds':time.monotonic()-tick}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['tails','panel','run-shard','assemble'])
    ap.add_argument('--scale',default='2');ap.add_argument('--precision',type=int,default=512)
    ap.add_argument('--subdiv',type=int,default=128);ap.add_argument('--degree',type=int,default=80)
    ap.add_argument('--klo',type=int,default=-4);ap.add_argument('--khi',type=int,default=10)
    ap.add_argument('--k',type=int,default=2);ap.add_argument('--j',type=int,default=0)
    ap.add_argument('--shard',type=int,default=0);ap.add_argument('--shards',type=int,default=8)
    ap.add_argument('--output-dir',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.precision;args.output_dir.mkdir(parents=True,exist_ok=True)
    bind=bindings();meta={'bindings':bind,'scale':args.scale,'precision':args.precision,'subdiv':args.subdiv,
                        'degree':args.degree,'klo':args.klo,'khi':args.khi}
    if args.mode=='assemble':
        sums=[F(0),F(0),F(0)];count=0
        tail=json.loads((args.output_dir/'tails.json').read_text());assert tail['meta']==meta
        for k in range(args.klo,args.khi):
            for j in range(args.subdiv):
                p=args.output_dir/f'panel_{k}_{j:04d}.json';d=json.loads(p.read_text());assert d['meta']==meta
                assert d['panel']['k']==k and d['panel']['j']==j
                for i,x in enumerate(d['panel']['energy_upper_exact']):sums[i]+=F(x)
                count+=1
        for key in ['origin_energy_upper_exact','exterior_energy_upper_exact']:
            for i,x in enumerate(tail['tails'][key]):sums[i]+=F(x)
        norms=[aa(x).sqrt() for x in sums];m2=((norms[0]*norms[2]+norms[1]**2)/(2*arb.pi())).sqrt()
        out={'meta':meta,'status':'COMPLETE_RADIAL_UPPER_CERTIFICATE','panel_count':count,
             'energy_upper_exact':[str(x) for x in sums],'D2_D3_D4_upper_arb':[str(x) for x in norms],
             'M2_upper_arb':str(m2),'M2_below_11_over_20':bool(m2<aa(F(11,20))),
             'TIS_p_charge_upper_arb':str(arb(21)/20*m2),'stationary_existence':'NOT CLAIMED'}
        (args.output_dir/'result.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));return
    fs=FarStrain(args.precision,args.scale)
    if args.mode=='tails':
        data=end_tails(fs,aa(F(2)**args.klo),aa(F(2)**args.khi))
        out={'meta':meta,'tails':data};(args.output_dir/'tails.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps(out,indent=2));return
    if args.mode=='panel':
        data=cauchy_panel(fs,args.k,args.j,args.subdiv,args.degree)
        print(json.dumps({'meta':meta,'panel':data},indent=2));return
    tick=time.monotonic();done=0
    for k in range(args.klo,args.khi):
        for j in range(args.subdiv):
            idx=(k-args.klo)*args.subdiv+j
            if idx%args.shards!=args.shard:continue
            p=args.output_dir/f'panel_{k}_{j:04d}.json'
            if p.exists():
                old=json.loads(p.read_text());assert old['meta']==meta;continue
            data=cauchy_panel(fs,k,j,args.subdiv,args.degree)
            p.write_text(json.dumps({'meta':meta,'panel':data},indent=2)+'\n');done+=1
            if done%8==0:print('shard',args.shard,'new_panels',done,'elapsed',round(time.monotonic()-tick,2),flush=True)
    print('SHARD_COMPLETE',args.shard,'new_panels',done,'seconds',time.monotonic()-tick,flush=True)
if __name__=='__main__':main()
