from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];ctx.prec=768;start=time.monotonic()
sha=lambda p:sha256(p.read_bytes()).hexdigest()
ar=lambda q:arb(q.p)/q.q
c=Q(4076476460239181,2251799813685248);g=1/c;q=g-4;delta=1-g;D=1-c*(q-delta)
mu=8/((-q-1)*(-q-2)*(-q-3));assert mu<Q(504423,100000)
E=arb(1)/2+arb(2)**ar(-q)+arb(2)**ar(3-q)+arb(2)**ar(q+2)/ar(-q)+arb(2)**ar(-q-2)/ar(-q-3)+arb(2)**ar(2-q)/ar(q+5)
assert E>133
expected={'007':'bcd0e49225807ba313dfb86ec386b4d3d3411bdcb233072d5047e84cc27ec58b','013':'3a2cf49c387db2fd95e7174a2b5f58103201857f01ba875e391b88714ab96471','014':'8168bf8b326124bc720cc992a5fbe0300d9b1250eb9f4e862b0f2ce38b53b6ce'}
rows=[];common=None;inputs=[Path(__file__),B/'PROOF.md',B/'source/T2_REVIEW_335.md']
for name in ['007','013','014']:
 p=B/f'data/{name}_endpoint.json';assert sha(p)==expected[name];inputs.append(p);j=json.loads(p.read_text());assert Q(j['c'])==c
 dec=lambda k:{int(n):Q(a) for n,a in j[k].items()}
 A=dec('F12');P=dec('P');T=dec('Theta0');dot=lambda a,b:sum((v*b.get(n,Q(0)) for n,v in a.items()),Q(0))
 if common is None:common=T
 assert common==T
 lam=dot(A,P)/dot(P,P);assert lam==Q(j['lambda'])
 ss=dot(A,A)-dot(A,P)**2/dot(P,P);assert ss>0
 b=(arb.pi()*ar(ss)).sqrt()/ar(4*c);hmin=b/(2*arb.pi()).sqrt();assert b<85020 and hmin>33917
 slope=sum((n*v for n,v in T.items()),Q(0));assert slope>Q(285227,10000)
 rsep=(E*ar(slope)/ar(D))**(1/ar(delta));cap=b*rsep**ar(q+1)/(-2*ar(q)-2).sqrt()
 rows.append({'candidate':name,'B':b.str(100),'H_min':hmin.str(100),'theta_prime_zero_exact':str(slope),'theta_prime_zero':ar(slope).str(100),'r_sep_lower_using_exact_point':rsep.str(100),'beta_cap_upper_using_exact_point':cap.str(100)})
rlow=(arb(133)*ar(Q(285227,10000))/ar(D))**(1/ar(delta));up=arb(85020)*rlow**ar(q+1)/(-2*ar(q)-2).sqrt();assert up<ar(Q(928,10**13))
out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'inputs':{str(p):sha(p) for p in inputs},'mu_exact':str(mu),'mu':ar(mu).str(100),'E':E.str(100),'q_exact':str(q),'delta_exact':str(delta),'D_delta_exact':str(D),'rows':rows,'r_low':rlow.str(100),'uniform_CI_cap_upper':up.str(100),'strict_rational_cap':'928/10000000000000','all_assertions_passed':True,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED independent analytic audit and directed numerical reach bound'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],out['uniform_CI_cap_upper'],out['elapsed_seconds'])
