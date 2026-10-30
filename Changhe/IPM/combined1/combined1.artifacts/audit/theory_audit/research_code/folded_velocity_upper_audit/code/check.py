"""Independent full-plane cell enclosure of the compensated kernel integral."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib, json, time, math
from flint import arb, acb, ctx
B=Path(__file__).resolve().parents[1];begin=time.monotonic()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
M=json.loads((B/'data/manifest.json').read_text())
assert sha(B/'PROOF.md')==M['proof_sha256']
for name,digest in M['inputs'].items():assert sha(B/name)==digest,name
P=json.loads((B/'data/parameters.json').read_text());ctx.prec=P['bits']
mesh=[Q(v) for v in json.loads((B/'data/mesh.json').read_text())]
assert mesh[0]==Q(1,20) and mesh[-1]==2000 and all(x<y for x,y in zip(mesh,mesh[1:]))
def A(v):
    z=Q(v);return arb(z.numerator)/z.denominator
def upper(v):
    m,e=v.upper().man_exp();return Q(int(m))*Q(2)**int(e)
def maximum(vs):
    result=vs[0]
    for v in vs[1:]:result=(result+v+abs(result-v))/2
    return result
pi=arb.pi();q=1/A(P['c'])-4;a=-q;rho=A(P['rho']);ta0=A(mesh[0]);tend=A(mesh[-1])
assert -5<q<-3 and ta0<1-rho and tend>1+rho
J=P['near_series_terms'];po=a*rho;Nsum=arb(0)
for j in range(1,J+1):
    last=po/j;Nsum+=last;po=po*(a+j)*rho/(j+1)
z=rho*(a+J)/(J+1);assert z<1
N=Nsum/a+arb(0,(last*z/(1-z)/a).upper())
origin=(8/pi)*ta0**(q+5)/(q+5)+6*ta0**(q+7)/((1-ta0*ta0)**2*(q+7))
exterior=(4/pi)*tend**(q+3)/(-q-3)+(tend/(tend-1))**2*tend**q/a
nphi=P['angular_cells'];sub=P['crossing_subdivision'];dphi=pi/(2*nphi)
unit=[acb(((j+arb(1)/2)*dphi).cos(),((j+arb(1)/2)*dphi).sin()) for j in range(nphi)]
rows=[];extra=[];slack=arb(0);L=arb(0);cells=0;crossings=0;subcells=0;branches_total=0
min_d2=None;min_d1=None

def branch_data(lo,hi,pc,width,uc=None):
    global min_d1,min_d2,branches_total
    mid=(lo+hi)/2;d=(hi-lo)/2+hi*width/2
    if uc is None:uc=acb(pc.cos(),pc.sin())
    center=mid*uc;zp=1-center;zm=1+center
    dp,dm=abs(zp),abs(zm);safe_m=dm-d
    assert safe_m>0,'cell enclosure reached -1'
    dmq=upper(-safe_m);min_d2=dmq if min_d2 is None else max(min_d2,dmq)
    invm=1/(zm*zm);out=[]
    if not dp+d<rho:
        safe_p=dp-d;assert safe_p>0,'active singular branch disk reached +1'
        dpq=upper(-safe_p);min_d1=dpq if min_d1 is None else max(min_d1,dpq)
        invp=1/(zp*zp)
        val=(invp-invm)/(4*pi)-center/pi
        der=(invp/zp+invm/zm)/(2*pi)-1/pi
        hess=3*(safe_p**(-4)+safe_m**(-4))/(2*pi)
        err=d*abs(der)+(d*d/2)*hess
        out.append((val.real,val.imag,err,abs(val)))
    if not dp-d>rho:
        val=-invm/(4*pi)-center/pi
        der=invm/zm/(2*pi)-1/pi
        hess=3*safe_m**(-4)/(2*pi)
        err=d*abs(der)+(d*d/2)*hess
        out.append((val.real,val.imag,err,abs(val)))
    assert out
    branches_total+=len(out)
    return out

for i in range(len(mesh)-1):
    lo,hi=A(mesh[i]),A(mesh[i+1]);weight=dphi*(hi**(q+2)-lo**(q+2))/(q+2)
    assert weight>0
    values=[]
    for j in range(nphi):
        pc=(arb(j)+arb(1)/2)*dphi
        vals=branch_data(lo,hi,pc,dphi,unit[j]);cells+=1
        if len(vals)==1:
            re,im,err,mag=vals[0];values.append((re,im))
            slack+=2*weight*err;L+=4*weight*mag
        else:
            crossings+=1
            for ii in range(sub):
                u0=lo+(hi-lo)*ii/sub;u1=lo+(hi-lo)*(ii+1)/sub
                width=dphi/sub;sw=width*(u1**(q+2)-u0**(q+2))/(q+2);assert sw>0
                for jj in range(sub):
                    angle=(arb(j)+(arb(jj)+arb(1)/2)/sub)*dphi
                    bs=branch_data(u0,u1,angle,width)
                    extra.append((sw,bs));L+=4*sw*maximum([b[3] for b in bs]);subcells+=1
    rows.append((weight,values))
    if i%100==0 or i+1==len(mesh)-1:
        progress={'utc':datetime.now(timezone.utc).isoformat(),'radial_rows':i+1,'cells':cells,'crossing_cells':crossings,'subcells':subcells,'elapsed_seconds':time.monotonic()-begin,'stage':'cell geometry'}
        (B/'verification/progress.json').write_text(json.dumps(progress,indent=2)+'\n')
        print(json.dumps(progress),flush=True)
assert cells==(len(mesh)-1)*nphi and subcells==crossings*sub*sub
setup=time.monotonic()-begin
print('Cell setup complete',setup,flush=True)
cache={}
def U(fraction):
    if fraction in cache:return cache[fraction]
    angle=pi*A(fraction)/2;cb,sb=angle.cos(),angle.sin();tot=arb(0)
    for weight,values in rows:
        local=arb(0)
        for re,im in values:
            x,y=cb*re,sb*im;local+=abs(x+y)+abs(x-y)
        tot+=weight*local
    tot+=slack
    for weight,bs in extra:
        plus=maximum([abs(cb*b[0]+sb*b[1])+b[2] for b in bs])
        minus=maximum([abs(cb*b[0]-sb*b[1])+b[2] for b in bs])
        tot+=weight*(plus+minus)
    result=upper(2*tot+origin+exterior);cache[fraction]=result
    if len(cache)%20==0:print('Direction evaluations',len(cache),'elapsed',time.monotonic()-begin,flush=True)
    return result
work=[(Q(i,16),Q(i+1,16)) for i in range(16)]
best=max(U(Q(i,16)) for i in range(17));done=[];tol=Q(P['direction_tolerance'])
while work:
    left,right=work.pop();ul,ur=U(left),U(right);best=max(best,ul,ur)
    bound=upper((A(ul)+A(ur))/2+L*pi*A(right-left)/4)
    if bound<=best+tol or right-left<=Q(1,16384):
        done.append((left,right,bound))
    else:
        mid=(left+right)/2;work.extend([(left,mid),(mid,right)])
done.sort();assert done[0][0]==0 and done[-1][1]==1
assert all(x[1]==y[0] for x,y in zip(done,done[1:]))
assert sum((right-left for left,right,_ in done),Q(0))==1
Fup=max(x[2] for x in done)
E=(2/pi)*N+(A(Fup)+arb(1)/2)/a
passed=E<A(P['target_E'])
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-begin,'setup_seconds':setup,
 'bits':ctx.prec,'proof_sha256':M['proof_sha256'],'manifest_sha256':sha(B/'data/manifest.json'),'checker_sha256':sha(Path(__file__)),
 'cells':cells,'crossing_cells':crossings,'subcells':subcells,'checked_branch_count':branches_total,
 'direction_evaluations':len(cache),'direction_intervals':len(done),'complete_direction_partition':True,
 'N':N.str(70),'origin_integral_bound':origin.str(70),'exterior_integral_bound':exterior.str(70),
 'Lipschitz_bound':L.str(70),'single_cell_slack_sum':slack.str(70),
 'distance_to_minus1_lower_exact':str(-min_d2),'active_distance_to_plus1_lower_exact':str(-min_d1),
 'F_upper_exact':str(Fup),'F_upper_display':A(Fup).str(70),'E_bound_ball':E.str(70),'E_upper_exact':str(upper(E)),
 'target_E':P['target_E'],'strict_target_pass':bool(passed),
 'direction_partition':[{'left':str(x),'right':str(y),'upper':str(z)} for x,y,z in done],
 'direction_endpoint_bounds':[{'coordinate':str(x),'upper':str(y)} for x,y in sorted(cache.items())],
 'status':'CONFIRMED independent complete upper bound' if passed else 'OPEN target not reached',
 'foreign_code_executed':False,'stationary_H_budget_supplied':False,'existence_claimed':False}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('direction_partition','direction_endpoint_bounds')},indent=2),flush=True)
assert passed,'The stated target did not pass.'
