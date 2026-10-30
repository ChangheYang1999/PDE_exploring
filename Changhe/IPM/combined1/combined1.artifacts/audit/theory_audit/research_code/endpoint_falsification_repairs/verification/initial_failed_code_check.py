"""Source-bound logical repair audit, with independent cutoff arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,difflib,time,re
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=768
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();read=lambda p:json.loads((B/p).read_text());checks=[]
def req(name,test,value=None):
 assert bool(test),(name,str(value));checks.append({'claim':name,'value':None if value is None else str(value)})
def ar(x):
 x=Q(x);return arb(x.numerator)/x.denominator
m=read('data/manifest.json');req('proof first',m['proof_written_before_checker'])
for p,h in m['inputs'].items():req('binding '+p,sha(B/p)==h)
for z in read('data/input_sources.json')['inputs']:req('copy '+z['local'],sha(B/z['local'])==z['sha256'])
old=(B/'source/revision1.md').read_text();new=(B/'source/revision2.md').read_text();words=[z for z in difflib.SequenceMatcher(None,old.split(),new.split(),autojunk=False).get_opcodes() if z[0]!='equal']
req('37 read changes',len(words)==37)
req('224-line revision2',len(new.splitlines())==224)
req('old revision binding',sha(B/'source/revision1.md')=='6eede4644e0f5c82859909135e7ed0c6031b871a5e069228107ab93a06e2c1cc')
req('new revision binding',sha(B/'source/revision2.md')=='660b089b8e6435065918f020a45d971cce4d82e8210675944322f3d7c47dd7f5')
req('unchanged program',sha(B/'source/T2_script.py')=='f47ab3e03e0d5268d0905c036f58499cce2fc32c607f07f5583115811bc388'.replace('ce2fc','cefe2fc'))
a=[[x.strip() for x in l.strip('|').split('|')] for l in old.splitlines() if l.startswith('| FW-') or l.startswith('| graded')]
z=[[x.strip() for x in l.strip('|').split('|')] for l in new.splitlines() if l.startswith('| FW-') or l.startswith('| graded')]
req('13 target rows',len(a)==len(z)==13)
for i,(x,y) in enumerate(zip(a,z)):
 req('unchanged numerical row '+str(i),x[:4]==y[:4])
 if i<2:req('OPEN target '+str(i),y[-1]=='not shown (OPEN)')
 else:req('unchanged other verdict '+str(i),x[-1]==y[-1])
for i in range(1,6):req('repair marker '+str(i),f'[T4-443 {i}]' in new)
for literal in ['withdrawn as\n  unproved','The question is OPEN, not false','not a proved admissible constant','unsupported (stale), not','The converse is not proved','hypothesis on the listed coefficient choices','is assumed, not proved']:
 req('repair text '+literal,literal in new)
prior=read('source/own_result.json');req('prior948checks',prior['check_count']==948 and len(prior['checks'])==948 and prior['proof_sha256']==sha(B/'source/own_PROOF.md'))
c=Q(4076476460239181,2251799813685248);q=1/c-4;d=1-1/c;D=5*c-1;alpha=-2*q-2;Emin=Q(prior['Emin_exact']);beta=50/(arb(651)*arb(28248).sqrt())
req('graded lower bracket',beta>ar(Q(45697,10**8)),beta);req('graded upper bracket',beta<ar(Q(25,54684)),beta)
rows=[]
for r in prior['rows']:
 name=r['candidate'];bb=arb(r['B']);g=ar(r['g0_exact']);H=arb(r['H0']);fac=ar(D)*bb/((2*arb.pi()).sqrt()*H*g)
 target=lambda bt:fac*(bb/(bt*ar(alpha).sqrt()))**ar(d/(-q-1))
 exact=target(beta);printed=target(ar(Q(25,54684)))
 req(name+' printed cutoff',printed<ar('0.2694533'),printed)
 req(name+' larger exact cutoff',exact>ar('0.2694533'),exact)
 req(name+' still excluded',exact<ar(Emin))
 for key,cap in [('Emin_H0','1.43912e-7'),('Emin_Phi_v0','1.14141e-7'),('current_H0','2.66323e-8')]:req(name+' unchanged reach '+key,arb(r['reach'][key]['bound'])<ar(cap))
 req(name+' current crude',arb(r['constant_current']['crude'])<ar('1.66122e-8'))
 req(name+' current shape',arb(r['constant_current']['shape'])<ar('1.89061e-9'))
 rows.append({'candidate':name,'graded_cutoff_at_H0':exact.str(90),'printed_cutoff_at_H0':printed.str(90)})
req('current list below smallest target',Q('2.66323e-8')<Q(1,2**25))
req('V floor below trans target',Q('1.14141e-7')<Q(1,2**23))
for p,h in m['inputs'].items():req('unchanged '+p,sha(B/p)==h)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'word_change_blocks':len(words),'graded_ceiling':beta.str(90),'cutoffs':rows,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'foreign_code_executed':False,'verdict':'CONFIRMED all five logical repairs and unchanged numerical table; qualify the remaining 0.2694533 wording as the printed target, not the exact graded ceiling; small Db universal-constant question remains OPEN'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),out['utc'],out['elapsed_seconds'])
for r in rows:print(r)
