"""Rebuild every branch/remainder bound and audit exact partition coverage."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import factorial
import hashlib,json
from flint import arb,ctx
import certify as c
ctx.prec=512;ctx.threads=1
TOP=Path(__file__).resolve().parents[1];d=c.Trial();out=[]
def exact(v):
    m,e=v.man_exp();return F(int(m))*F(2)**int(e)
def record(v):return {'ball':v.str(60),'lower_exact':str(exact(v.lower())),'upper_exact':str(exact(v.upper()))}
for path in sorted((TOP/'evidence').glob('raw_x3_*_result.json')):
    result=json.loads(path.read_text());part=json.loads(path.with_name(path.name.replace('_result','_partition')).read_text());settings=result['settings']
    assert result['input_sha256']==part['input_sha256']==d.sha
    rad=part['q'];ang=part['theta_over_pi_half'];eq=F(1,2**settings['qcap']);et=F(1,2**settings['tcap'])
    assert F(rad[0][0])==eq and F(rad[-1][1])==1-eq
    assert F(ang[0][0])==0 and F(ang[-1][1])==1-et
    for rows in (rad,ang):
        assert all(F(row[0])<F(row[1]) for row in rows)
        assert all(F(rows[i][1])==F(rows[i+1][0]) for i in range(len(rows)-1))
    radial=arb(0);angular=arb(0)
    for row in rad:
        a,b=F(row[0]),F(row[1]);i=row[2]
        assert d.knots[i]<=a<b<=d.knots[i+1]
        fresh=d.radial_bound(a,b,i);assert fresh is not None
        logm,margins=fresh;assert all(v>0 for v in margins)
        assert logm<settings['maxlog']
        radial+=c.ball(b-a)*logm.exp()
    radial*=arb.pi()/2*c.gauss_constant(settings['nq'])
    for row in ang:
        a,b=F(row[0]),F(row[1]);fresh=d.angle_bound(a,b);assert fresh is not None
        logm,kernel,margin=fresh;assert margin>0 and logm<settings['maxlog']
        angular+=c.ball(b-a)*arb.pi()/2*logm.exp()*kernel
    angular*=c.gauss_constant(settings['nt'])*arb(2)**(2*settings['nt'])
    strips=c.ball(eq)*arb.pi()*d.m0
    width=c.ball(et)*arb.pi()/2;theta_strip=width**3/3*(d.csum+d.ct*width**(d.p-2)).exp()
    error=radial+angular+strips+theta_strip
    for key,value in [('radial',radial),('angular',angular),('q_strips',strips),('theta_strip',theta_strip)]:
        assert value.upper()<=arb(part['errors'][key]).upper(),(path.name,key,value,part['errors'][key])
    c.audit_nodes(settings['nq']);c.audit_nodes(settings['nt'])
    strain=d.pref*(arb(result['quadrature_sum'])+arb(0,error.upper()));defect=3/d.k-1-strain
    assert strain>c.ball(F('15.72608782162349')) and strain<c.ball(F('15.72608782162351'))
    assert defect>c.ball(F('1.03011e-8')) and defect<c.ball(F('1.03012e-8'))
    out.append({'file':path.name,'radial_cells':len(rad),'angular_cells':len(ang),'error':record(d.pref*error),'strain':record(strain),'defect':record(defect),'canonical_ell':record((1+strain)/3),'held_a':record(1/d.k-strain),'held_b':record(1/d.k+strain)})
    print('audited',path.name,flush=True)
assert len(out)==2
for name in ['strain','defect']:
    first,second=[x[name] for x in out]
    assert max(F(first['lower_exact']),F(second['lower_exact']))<min(F(first['upper_exact']),F(second['upper_exact']))
result={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','precision_bits':ctx.prec,'input_sha256':d.sha,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'coverage':'exact disjoint contiguous radial and angular partitions plus proved endpoint strips','branch_checks':'every saved rectangle rechecked at 512 bits','outputs':out}
(TOP/'evidence/bounds_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
