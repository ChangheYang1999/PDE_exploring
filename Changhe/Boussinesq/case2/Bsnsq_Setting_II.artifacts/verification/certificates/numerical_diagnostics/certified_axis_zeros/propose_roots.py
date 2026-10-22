"""Uncertified multiprecision root proposals; strict integer tests decide validity."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import datetime,hashlib,json,resource,time
from pathlib import Path
import mpmath as mp
resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
resource.setrlimit(resource.RLIMIT_CPU,(530,540))
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest=json.loads((HERE/'data/input_manifest.json').read_text())
mp.mp.dps=700
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':sha(__file__),
        'status':'PROPOSALS ONLY; no certification','dps':mp.mp.dps,'bracket_decimal_digits':450,'states':[]}
start=time.process_time()
for state,guess in zip(manifest['states'],('23.75','25.96')):
    path=HERE/'data'/state['compiled_file'];assert sha(path)==state['compiled_sha256']
    c=json.loads(path.read_text());b=int(c['beta']);D=int(c['denominator']);modes=[]
    for mode in c['modes']:
        k,L,J=(int(mode[z])for z in ('k','L','J'))
        P,Q=([int(x)for x in mode[z]]for z in ('P','Q'))
        u,v=map(int,mode['moment'])
        modes.append((k,L,[(-mp.mpf(x)/(j-L)if j!=L else mp.mpf(0))for j,x in enumerate(P)],
                      mp.mpf(u)/v,mp.mpf(P[L])if L<len(P)else mp.mpf(0),
                      [mp.mpf(x)/(j+J)for j,x in enumerate(Q)]))
    def horner(coefs,t):
        a=mp.mpf(0)
        for x in reversed(coefs):a=a*t+x
        return a
    def h(t):
        q=1-t**(2*b);logt=mp.log(t);s=mp.mpf(0)
        for k,L,ic,mc,pc,oc in modes:
            ib=horner(ic,t)+t**L*(mc-pc*logt)
            s+=q**(-k)*ib+q**k*horner(oc,t)
        return b-t*s/(8*D*q)
    def ht_from_r(r):return h((1+r*r)**(-mp.mpf(1)/(2*b)))
    g=mp.mpf(guess)
    r=mp.findroot(ht_from_r,(g*mp.mpf('.999'),g*mp.mpf('1.001')),
                  tol=mp.mpf('1e-550'),maxsteps=40,verify=True)
    t=(1+r*r)**(-mp.mpf(1)/(2*b));den=10**450;num=int(mp.floor(t*den))
    row={'source_sha256':state['source_sha256'],'compiled_file':path.name,
         'compiled_sha256':sha(path),'beta':b,'r_proposal':mp.nstr(r,650),
         't_proposal':mp.nstr(t,650),'h_at_proposal':mp.nstr(h(t),50),
         't_lower':{'numerator':str(num-1),'denominator':str(den)},
         't_upper':{'numerator':str(num+2),'denominator':str(den)},
         'cpu_seconds_to_here':time.process_time()-start}
    record['states'].append(row)
    (HERE/'data/root_proposals.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'compiled_file':path.name,'r_proposal':mp.nstr(r,24),'h':row['h_at_proposal'],
                      'cpu_seconds':row['cpu_seconds_to_here']}),flush=True)
record['completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
record['cpu_seconds']=time.process_time()-start
(HERE/'data/root_proposals.json').write_text(json.dumps(record,indent=2)+'\n')
