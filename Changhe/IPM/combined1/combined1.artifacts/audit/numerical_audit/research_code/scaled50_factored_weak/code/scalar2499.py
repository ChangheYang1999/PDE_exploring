"""Independent scalar fixtures for factored localization and radial poles."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time,sys
from flint import arb,ctx,fmpq as Q,fmpq_poly as Poly
import importlib.util
_mpath=Path(__file__).resolve().parents[3]/"research/factored_pole_moments/code/moments.py"
_spec=importlib.util.spec_from_file_location("n4_radius50_scalar",_mpath)
_m=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(_m)
OLD,ar,beta,pole_moments,integral=_m.OLD,_m.ar,_m.beta,_m.pole_moments,_m.integral
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/scaled50_factored_weak'
sys.set_int_max_str_digits(0)
V=Poly([0,1]);sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def new(p,d):
    with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def main():
    start=time.monotonic();ctx.prec=2048
    fixtures=[]
    for b,m,a,maxk in [(Q(0),0,Q(1),12),(Q(-2,3),0,Q(2499),36),(Q(7,4),8,Q(99),24),(Q(5,3),3601,Q(2499),48),(Q(11,7),4801,Q(2499),64),(Q(-3,4),1045,Q(9999),24),(Q(7,3),1045,Q(99),24)]:
        tick=time.monotonic();values,checks=pole_moments(b,m,a,maxk)
        assert min(z.rel_accuracy_bits() for z in values)>150
        comparisons=[]
        if m==0:
            prior=OLD.pole_moments(b,a,maxk)
            comparisons=[x.overlaps(y) for x,y in zip(values,prior,strict=True)];assert all(comparisons)
        fixtures.append({'b':str(b),'m':m,'a':str(a),'maximum_power':maxk,'checks':checks,'old_m0_overlaps':comparisons,'endpoint_moments':[values[0].str(100),values[-1].str(100)],'elapsed_seconds':time.monotonic()-tick})
        print('moments',b,m,a,maxk,'bits',min(z.rel_accuracy_bits() for z in values),'seconds',time.monotonic()-tick,flush=True)
    integrals=[]
    cases=[(Q(1,3),0,Poly([2,-3,5]),[(Q(99),2),(Q(2499),3)]),(Q(-2,3),5,Poly([1,-5,2,7]),[(Q(2499),4),(Q(9999),2)]),(Q(7,4),12,Poly([3,0,-7,2]),[(Q(99),3),(Q(2499),2),(Q(9999),2)]),(Q(0),64,Poly([1]),[(Q(1),3)]),(Q(5,7),522,Poly([2,0,-3,1]),[])]
    for b,m,N,factors in cases:
        tick=time.monotonic();x,record=integral(b,m,N,factors)
        if m<=64:
            y,old=OLD.integral(b,N*(1-V)**m,factors);assert x.overlaps(y)
            comparison='Independent expanded localization and old pole recurrence'
        else:
            y=sum((ar(c)*beta(b+j+1,m+1) for j,c in enumerate(N)),arb(0));assert x.overlaps(y)
            comparison='Direct Gamma quotient for every polynomial beta moment'
        assert x.rel_accuracy_bits()>150 and y.rel_accuracy_bits()>150
        integrals.append({'b':str(b),'m':m,'numerator':[str(c) for c in N],'factors':[[str(a),d] for a,d in factors],'result':x.str(100),'comparison_result':y.str(100),'comparison':comparison,'overlap':True,'record':record,'elapsed_seconds':time.monotonic()-tick})
        print('integral',b,m,'bits',x.rel_accuracy_bits(),'seconds',time.monotonic()-tick,flush=True)
    paths=[BASE/'PROOF.md',Path(__file__),ROOT/'research/factored_pole_moments/code/moments.py',ROOT/'research/rational_pole_moments/code/moments.py',ROOT/'research/rational_pole_moments/PROOF.md',ROOT/'research/rational_pole_moments/reviews/T4/ACCEPTANCE.json']
    out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'inputs':{str(p.relative_to(ROOT)):sha(p) for p in paths},'pole_fixtures':fixtures,'integral_fixtures':integrals,'elapsed_seconds':time.monotonic()-start,'status':'OPEN independent review; finite scalar fixtures complete, no candidate result'}
    new(BASE/'verification/scalar2499.json',out);print('DONE',out['utc'],out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
