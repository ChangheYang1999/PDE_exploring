"""Resume an interrupted norm certificate, with exact source/provenance binding.
Completed intervals are retained; all derivatives are reconstructed and all
Cartesian checks are performed after the missing integrals finish.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import sys,json,time,hashlib
from flint import arb,ctx
import arb_norms as an
ah=an.ah
HERE=Path(__file__).resolve().parent

def resume(name):
    dest=HERE/(name+'_arb_norms.json')
    previous=dest.read_bytes()
    out=json.loads(previous)
    assert out['name']==name and out['status']=='PARTIAL'
    ctx.prec=out['precision_bits']
    start=time.monotonic()
    c,A,sha,rawsha,D=ah.construct(name)
    assert sha==out['canonical_sha256'] and rawsha==out['source_record_sha256']
    audit_path=HERE/'repair_audit.json'
    audit=json.loads(audit_path.read_text())
    row=next(r for r in audit['variants'] if r['name']==name)
    assert row['canonical_sha256']==sha and row['exact_difference_checked']
    assert audit['verdict']=='CONFIRMED'
    assert hashlib.sha256(audit_path.read_bytes()).hexdigest()==out['repair_audit_sha256']
    delta=1-1/c
    for nx in range(4):
        D[3,nx]=ah.diff(D[2,0],2,'y',delta) if nx==0 else ah.diff(D[2,nx-1],2,'x',delta)
    jobs=[('rF',0,False,True),('F',0,False,False),('DF',1,False,False),('omega_D2F',2,True,False),('omega_D3F',3,True,False)]
    assert set(out['norms']) <= {job[0] for job in jobs}
    for label,data in out['norms'].items():
        lo,hi=arb(data['lower_ball']),arb(data['upper_ball'])
        ul,uh=arb(data['u_lower_ball']),arb(data['u_upper_ball'])
        assert all(x.is_finite() and x>0 for x in [lo,hi,ul,uh])
        assert lo.overlaps(ul) and hi.overlaps(uh)
    record={'utc_started':datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'previous_record_sha256':hashlib.sha256(previous).hexdigest(),
            'resume_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'retained_norms':list(out['norms']), 'source_row_rechecked':True}
    out.setdefault('resumes',[]).append(record)
    for label,d,weight,rproxy in jobs:
        if label in out['norms']:continue
        gt,facts=an.group(D,d,delta,'t',weight,rproxy)
        s,t,e=an.integrate(gt,'t',weight)
        lo,hi=an.bound(s,t,e,weight)
        gu,_=an.group(D,d,delta,'u',weight,rproxy)
        ss,tt,ee=an.integrate(gu,'u',weight)
        l2,h2=an.bound(ss,tt,ee,weight)
        assert all(v.is_finite() for v in [s,t,ss,tt,lo,hi,l2,h2])
        assert s.overlaps(ss) and t.overlaps(tt) and lo.overlaps(l2) and hi.overlaps(h2)
        out['norms'][label]={'lower_ball':lo.str(80),'upper_ball':hi.str(80),
            'lower_endpoint':str(lo.lower()),'upper_endpoint':str(hi.upper()),
            'u_lower_ball':l2.str(80),'u_upper_ball':h2.str(80),
            'base_integral':s.str(80),'weighted_integral':t.str(80),
            'structural_endpoint_factors':facts}
        record['elapsed_seconds']=time.monotonic()-start
        out['utc_updated']=datetime.now(timezone.utc).isoformat(timespec='seconds')
        dest.write_text(json.dumps(out,indent=2)+'\n')
        print(label,lo.str(45),hi.str(45),'resume seconds',record['elapsed_seconds'],flush=True)
    checks=[]
    for xs,ys in [('0','1/10'),('1','0'),('1/2','1/2'),('1','2'),('3','1'),('60','80'),('0','1000')]:
        x,y=Q(xs),Q(ys)
        pv=ah.evaluate(D,delta,x,y)
        cv=ah.au.direct_F(A,c,ah.aq(x),ah.aq(y))
        ok={str(k):v.is_finite() and cv[k].is_finite() and v.overlaps(cv[k]) for k,v in pv.items()}
        assert len(ok)==10 and all(ok.values()),(xs,ys,ok)
        checks.append({'point':[xs,ys],'components':ok})
        print('Cartesian',xs,ys,'PASS',flush=True)
    record.update({'utc_completed':datetime.now(timezone.utc).isoformat(timespec='seconds'),
                   'elapsed_seconds':time.monotonic()-start})
    out.update({'utc_completed':record['utc_completed'],'cartesian_checks':checks,'status':'PENDING_PROOF_AUDIT'})
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print('DONE',name,record['elapsed_seconds'],flush=True)
if __name__=='__main__':resume(sys.argv[1])
