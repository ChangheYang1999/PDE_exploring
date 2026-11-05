#!/usr/bin/env python3
"""Whole-plane M certificate from a frozen core prefix and signed far K.

Current full producer/configuration is never altered. Missing core records
produce only MATRIX_PREFIX_PENDING. Origin expansion is cached with bindings.
"""
import argparse,json,math,sys,time
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from flint import arb,ctx,fmpq as Q
HERE=Path(__file__).resolve().parent;ART=HERE.parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(ART/'coercivity_residual'))
from fields013 import Evaluator,C,SOURCE_HASHES,rational_arb
from asymptotics013 import Expansion
def read(p):return json.loads(Path(p).read_text())
def sha(p):return sha256(Path(p).read_bytes()).hexdigest()
def aa(x):
    x=F(x);return arb(x.numerator)/arb(x.denominator)
def bindings():
    files=[Path(__file__),ART/'certify_actual_matrix.py',ART/'actual_matrix_v01/configuration.json',
           ART/'coercivity_residual/fields013.py',ART/'coercivity_residual/asymptotics013.py',
           HERE/'signed_matrix_far_price_v01.json',HERE/'structure013_result.json']
    return {str(p.relative_to(ART)):sha(p) for p in files}
def checkhash(mapping):
    assert mapping
    for name,h in mapping.items():assert sha(ART/name)==h,('binding',name)
def complete(paths,max_depth):
    assert len(paths)==len(set(paths));ps=set(paths)
    def visit(s):
        if s in ps:assert not any(p.startswith(s) and p!=s for p in ps);return
        assert len(s)<max_depth;visit(s+'0');visit(s+'1')
    visit('')
def origin_certificate(cfg,bind,out):
    cache=out/'origin.json'
    meta={'bindings':bind,'radius':cfg['rmin'],'precision':cfg['precision'],'degree':12,'beta':cfg['beta']}
    if cache.exists():
        old=read(cache);assert old['meta']==meta
        return old['origin']
    e=Evaluator(cfg['precision'],1,1);ex=Expansion(e,'origin',12);r=aa(cfg['rmin'])
    def zero(name,i,j):return {(kind,n):a for (kind,n,p),a in ex.field(name,i,j).items() if p==0}
    assert zero('u1',1,0)=={('c',0):C-1}
    assert zero('u2',0,1)=={('c',0):1-C}
    assert zero('u1',0,1)==zero('u2',1,0)==zero('rho',1,0)=={}
    by=zero('rho',0,1);assert set(by)=={('c',0)}
    by0=rational_arb(by['c',0]);c=rational_arb(C);q=arb(21)/10;base=c+1-q*c;d0=c-1
    center=min((base-q*d0+by0).lower(),(base+q*d0).lower())
    def ur(name):
        total=arb(0)
        for (_,_,p),a in ex.field(name,0,0).items():
            assert p-1>=0;total+=arb(abs(a))*r**rational_arb(p-1)
        for a,p in ex.remainder_terms(name,0,0,r):
            assert p-1>=0;total+=a*r**rational_arb(p-1)
        return total
    u1,u2=ur('u1'),ur('u2');u0=(u1*u1+u2*u2).sqrt()
    error=4*r*r*(c+u0)
    error+=q*(ex.point_bound('u1',1,0,r,True)+(ex.point_bound('u1',0,1,r)+ex.point_bound('u2',1,0,r))/2)
    error+=ex.point_bound('rho',1,0,r)+ex.point_bound('rho',0,1,r,True)
    lower=center-error;assert lower.is_finite() and lower>=rational_arb(Q(cfg['beta']))
    result={'lower':lower.str(80),'center_lower':center.str(80),'perturbation_upper':error.str(80),
            'rho_y_origin':by0.str(80),'exact_strain_and_constant_harmonic_checks':True}
    cache.write_text(json.dumps({'meta':meta,'origin':result},indent=2)+'\n');return result
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--panels',type=int,default=711)
    ap.add_argument('--far-radius',type=int,default=30000);ap.add_argument('--out',type=Path,default=HERE/'matrix_prefix_signed_far_v01')
    args=ap.parse_args();tick=time.monotonic();args.out.mkdir(parents=True,exist_ok=True)
    cfg=read(ART/'actual_matrix_v01/configuration.json');ctx.prec=cfg['precision']
    assert cfg['source_hashes']==SOURCE_HASHES and Q(cfg['beta'])==Q(7,10);checkhash(cfg['bindings'])
    ratio=F(cfg['ratio']);rmin=F(cfg['rmin']);rmax=F(cfg['rmax']);N=cfg['panels']
    assert rmin*ratio**(N-1)<rmax<=rmin*ratio**N and 0<args.panels<=N
    endpoint=min(rmin*ratio**args.panels,rmax);assert endpoint>=args.far_radius
    price=read(HERE/'signed_matrix_far_price_v01.json');assert price['status']=='SIGNED_MATRIX_FAR_PRICE_COMPLETE'
    assert price['source_hashes']==SOURCE_HASHES and Q(price['fixed_c'])==C and price['q']=='21/10' and price['weight_a']=='2'
    checkhash(price['bindings']);far=[r for r in price['rows'] if r['radius']==args.far_radius];assert len(far)==1
    far=far[0];assert far['passes_beta_7_over_10'] and arb(far['matrix_lower'])>=arb(7)/10
    bind=bindings();origin=origin_certificate(cfg,bind,args.out)
    rows={};used={}
    for p in sorted((ART/'actual_matrix_v01').glob('chunk_*.json')):
        d=read(p);assert d['configuration']==cfg;take=[r for r in d['rows'] if r['index']<args.panels]
        if not take:continue
        used[str(p.relative_to(ART))]=sha(p)
        for row in take:
            i=row['index'];assert i not in rows and row['pass'];rows[i]=row
            complete([p['path'] for p in row['leaves']],cfg['max_depth'])
            for leaf in row['leaves']:
                assert leaf['pass']
                assert all(math.isfinite(leaf[k]) and leaf[k]>=0 for k in ['min_aa','min_dd','min_determinant'])
    missing=sorted(set(range(args.panels))-set(rows))
    result={'status':'MATRIX_PREFIX_PENDING' if missing else 'CERTIFIED_ACTUAL_MATRIX_PREFIX_SIGNED_FAR',
            'configuration':cfg,'used_base_panels':args.panels,'available_base_panels':len(rows),'missing_base_panels':missing,
            'core_endpoint_exact':str(endpoint),'exterior_start':args.far_radius,'origin_lower':origin['lower'],
            'origin_detail':origin,'exterior_lower':far['matrix_lower'],'exterior_detail':far,
            'used_chunk_sha256':used,'bindings':bind,'failed_base_panels':[],
            'total_leaves':sum(len(r['leaves']) for r in rows.values()),'elapsed_seconds':time.monotonic()-tick,
            'finished_utc':datetime.now(timezone.utc).isoformat(),
            'scope':'Actual whole-plane M>=7/10 only when prefix status CERTIFIED. Frozen full producer remains running unchanged. No stationary theorem claimed.'}
    (args.out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['configuration','used_chunk_sha256','core_endpoint_exact','missing_base_panels','bindings']},indent=2))
if __name__=='__main__':main()
