"""Independent comparison of the rationally rounded origin ceiling cover."""
from datetime import datetime,timezone
from pathlib import Path
from hashlib import sha256
import json,time
from flint import arb,ctx,fmpq as Q
R=Path(__file__).resolve().parents[3];B=R/'research/origin_dyadic_ceiling'
def H(p):return sha256(p.read_bytes()).hexdigest()
def ar(x):return arb(x.numerator)/arb(x.denominator)
start=time.monotonic();ctx.prec=1024
peerpath=B/'source/T4_candidate007_origin_cover.json';peer=json.loads(peerpath.read_text())
ownpath=B/'verification/candidate007_modes13.json';own=json.loads(ownpath.read_text())
can=R/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/canonical.json'
files={
 'projected_laplacian/verification/candidate007_mode1.json':R/'research/projected_laplacian_audit/source/verification/candidate007_mode1.json',
 'projected_laplacian/verification/candidate007_mode3.json':R/'research/projected_laplacian_audit/source/verification/candidate007_mode3.json',
 'projected_laplacian/data/candidate007_canonical.json':can,
 'origin_dyadic_inverse/PROOF.md':B/'source/T4_origin_dyadic_inverse_PROOF.md',
 'origin_dyadic_inverse/APPLICATION_007.md':B/'source/T4_APPLICATION_007.md',
 'origin_dyadic_inverse/code/check_007.py':B/'source/T4_check_007.py',
 'weak_probe_audit/code/reproduce.py':R/'research/projected_laplacian_audit/source/T4_reproduce.py'}
for k,v in peer['inputs'].items():assert H(files[k])==v,(k,H(files[k]),v)
assert Q(own['c'])==Q(peer['c']);c=Q(own['c']);A=1+1/c
assert Q(own['strain'])==Q(peer['strain'])==1-c
checks={}
for k,a,b in [('a0',ar(Q(own['a0'])),arb(peer['a0'])),('a0_margin',ar(Q(own['a0_margin'])),arb(peer['a0_minus_5c_minus4'])),('s_star',arb(own['maximizer']),arb(peer['s_star'])),('H',arb(own['Hmax']),arb(peer['H']))]:
 checks[k]=bool(a.overlaps(b));assert checks[k]
Hup=Q(peer['H_upper']);assert Hup==Q(57,50) and arb(own['Hmax'])<ar(Hup)
rows=[]
for old,row in zip(own['cells'],peer['rows']):
 l,h,e=map(Q,[old['left'],old['right'],old['norm_evaluation_at']])
 assert (l,h,e)==tuple(map(Q,[row['left'],row['right'],row['evaluation']]))
 low=arb(old['lower']); high=ar(Hup*(1+c-c*l)/(1+l))
 gap=low-high;ratio=low/high
 vals={'lower':low,'upper':high,'margin':gap,'ratio':ratio}
 matched={k:bool(v.overlaps(arb(row[k]))) for k,v in vals.items()}
 assert all(matched.values()) and gap>0 and ratio>1
 rows.append({'left':str(l),'right':str(h),'norm_evaluation_at':str(e),**{k:v.str(100) for k,v in vals.items()},'peer_overlaps':matched})
assert len(rows)==7 and Q(rows[0]['left'])==0 and Q(rows[-1]['right'])==A
inputs={str(p.relative_to(R)):H(p) for p in list(files.values())+[peerpath,ownpath,Path(__file__),B/'PROOF.md',B/'REVIEW_T4.md']}
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':own['candidate'],'scalar_checks':checks,'H_upper':str(Hup),'rows':rows,'inputs':inputs,'elapsed_seconds':time.monotonic()-start,
 'verdict':'CONFIRMED independent arithmetic and conditional scalar cover. Actual inverse theorem and resulting scheme application await required Opus review.'}
p=B/'verification/peer_comparison.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print(out['verdict'],len(checks)+sum(len(x['peer_overlaps']) for x in rows),'checks',out['elapsed_seconds'])
