"""Source-bound theory arithmetic; does not repeat candidate integrations."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import difflib, hashlib, json, re, time
from flint import arb, ctx
B=Path(__file__).resolve().parents[1]; start=time.monotonic(); ctx.prec=512
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads((B/p).read_text())
checks=[]
def require(name,test,value=None):
 assert bool(test),(name,str(value))
 checks.append({'claim':name,'value':None if value is None else str(value)})
def ar(x):
 x=Q(x);return arb(x.numerator)/x.denominator
manifest=read('data/manifest.json')
require('proof binding',sha(B/'PROOF.md')==manifest['proof_sha256'])
for p,h in manifest['inputs'].items():require('source '+p,sha(B/p)==h)
text=(B/'source/THEORY_FINAL.md').read_text(); old=(B/'source/accepted_draft34.md').read_text()
require('frozen 1810-line draft38',len(text.splitlines())==1810 and sha(B/'source/THEORY_FINAL.md')=='ccaa8623477ffdffbb977e866e669cffc9546a657eade246d053941ea0162a02')
require('accepted draft34',sha(B/'source/accepted_draft34.md')=='febf6c09e19a2e6b585c5263348250017d4af86fca9aa731db89fbc6d6106b40')
changes=[z for z in difflib.SequenceMatcher(None,old.split(),text.split(),autojunk=False).get_opcodes() if z[0]!='equal']
require('all 124 word-change blocks',len(changes)==124)
require('743-line complete word comparison',len((B/'source/word_changes.txt').read_text().splitlines())==743)
p=read('data/parameters.json'); ceilings=list(map(Q,p['ceilings'])); table=[]
for line in text.splitlines():
 if not line.startswith('| '):continue
 v=[a.strip() for a in line.strip('|').split('|')]
 if len(v)!=6 or not re.match(r'^(?:d2|Mpen2|0\d\d)$',v[0]) or v[2]=='-':continue
 floor=Q(v[1].split()[0]); ratios=[]
 for k,c0 in enumerate(ceilings):
  ratio=floor/c0; require(v[0]+' ratio '+str(k),ratio>Q(v[k+2]),ratio)
  ratios.append({'exact':str(ratio),'printed_lower':v[k+2]})
 table.append({'candidate':v[0],'floor':str(floor),'ratios':ratios})
require('all 21 table rows',len(table)==21)
x={k:Q(v) for k,v in p['sharpw'].items()}; rate=x['mu']-x['C']*x['s']-x['cU']*x['r']*72
require('exact high rate',rate==Q(63092119,405000000),rate)
require('lower rate',rate>Q('0.1557'))
require('inverse',1/rate<Q('6.4226'))
slack=x['r']-x['eta']/Q('0.1557');require('exact positive slack',slack==Q(7,1557000000),slack)
require('exact rate self-map',x['r']-x['eta']/rate>0)
contraction=ar(x['r']/x['betaL'])/(2*(arb.pi()*ar(x['s'])*(1+ar(x['s']))).sqrt())
require('contraction bound',contraction<ar('0.0137200'),contraction)
ceiling=(2*ar(x['mu'])/3)*(ar(x['mu'])/(3*ar(x['C']))).sqrt()/(ar(x['cU'])*ar(x['w2']).sqrt())
require('family ceiling',ceiling<ar('0.0000028496'),ceiling)
require('fixed ball radius',x['r']/1024==Q('0.0000013193359375'))
# The two independent mode records supply the containing endpoint energies.
n4=read('source/N4_dyadic_result.json'); name='C1-N1-016-legqs25-quot013'; r=n4['results'][name]
bound=read('source/N4_dyadic_bound_result.json')
require('production output binding',bound['result_sha256']==sha(B/'source/N4_dyadic_result.json') and bound['all_before_hashes_unchanged'] and bound['source_count']==21)
require('peer proof binding',n4['inputs']['research/joint_scaled_dyadic016/PROOF.md']==sha(B/'source/N4_dyadic_PROOF.md'))
require('peer checker binding',n4['inputs']['research/joint_scaled_dyadic016/code/check.py']==sha(B/'source/N4_dyadic_check.py'))
modes=[]
for n in [1,3]:
 filename=f'source/N4_dyadic_mode{n}.json'; m=read(filename); modes.append(m)
 rel=f'research/joint_scaled_dyadic016/verification/{name}/mode_{n:03d}.json'
 require('mode binding '+str(n),sha(B/filename)==n4['inputs'][rel]==bound['final_modes'][rel])
 require('actual raw '+str(n),m['raw_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42')
 require('two derivative constructions '+str(n),m['Cartesian_polar_equal'] and m['mixed_derivatives_equal'])
 require('complete group count '+str(n),m['group_count']==len(m['decompositions'])==51)
 for j,z in enumerate(m['endpoints']):require(f'mode{n} endpoint{j}',Q(z['diagonal_integrability_margin'])>0)
 for j,z in enumerate(m['decompositions']):require(f'mode{n} exact decomposition{j}',z['exact_reconstruction'])
 for w in m['weights']:
  require(f'mode{n} complete moments '+w['a'],len(w['groups'])==51 and w['accuracy_bits']>150)
  for j,g in enumerate(w['groups']):require(f'mode{n} weight{w["a"]} moment{j}',Q(g['b'])>-1 and g['accuracy_bits']>150)
norms={}
for a in ['1/4','7/4']:
 total=sum((arb(next(w['energy'] for w in m['weights'] if w['a']==a)) for m in modes),arb(0))
 require('endpoint sum '+a,total.overlaps(arb(r['square_norms'][a])) and total>0)
 norms[a]=total.sqrt();require('endpoint norm '+a,norms[a].overlaps(arb(r['norms'][a])))
 peer=arb(r['peer_comparisons'][a]['peer_square']);require('N3 containing endpoint '+a,peer.contains(total))
c=Q('4076476460239181/2251799813685248');d=c-1;A=1+1/c
require('origin assumptions',Q(r['a0_exact'])>=5*c-4 and Q(r['strain_exact'])==1-c and 1<c<2)
sstar=(ar(2*d-3)+(ar(2*d-3)**2+ar(16*d)).sqrt())/8
require('unique interior max',sstar>0 and sstar<ar(d))
H=(ar(d)-sstar)*(4*arb.pi()*sstar*(1+sstar)).sqrt()
require('H independent overlap',H.overlaps(arb(r['Hmax'])))
require('Astar cell limits',Q(3,2)<A<Q(7,4))
points=[Q(k,4) for k in range(7)]+[A]; cells=[]
for i,(left,right) in enumerate(zip(points[:-1],points[1:])):
 e=Q(1,4) if i==0 else Q(7,4); require('right endpoint dominates '+str(i),e>=right)
 low=arb(5)**ar((left-2)/2)*norms[str(e)]; high=H*ar((1+c-c*left)/(1+left)); gap=low-high; ratio=low/high
 own={'left':str(left),'right':str(right),'norm_at':str(e),'lower':low.str(100),'upper':high.str(100),'gap':gap.str(100),'ratio':ratio.str(100)}
 peer=r['seven_cells'][i]
 for key,z in [('lower',low),('upper',high),('gap',gap),('ratio',ratio)]:require(f'cell{i} peer {key}',z.overlaps(arb(peer[key])))
 require('cell positive '+str(i),gap>0)
 require('cell conservative factor '+str(i),ratio>ar('1.253908386497'))
 cells.append(own)
q=1/c-4;delta=1-1/c;kappa=1-q
lam=arb(1)/2+5*arb(2)**ar(1-q)
require('lambda source overlap',lam.overlaps(arb(read('source/outer.json')['lambda'])))
require('REFUTED lambda exact decimal',lam>ar('109.6024'),lam)
require('piecewise small radius consequence',lam>ar('2.74'))
require('large radius consequence',lam*(arb(5)/18860)**ar(delta)>ar('2.74'))
N1=arb(read('source/origin.json')['rows'][3]['N13'])
require('REFUTED upward-rounded projected lower',N1<ar('13.758676'),N1)
require('correct projected lower',N1>ar('13.75867597'))
require('023 factor genuinely greater',Q('0.002634958245163687')/Q(25,54684)>Q('5.763'))
Emin=Q(read('source/universal.json')['Etest_exact']);ru=5*(lam/ar(Emin))**ar(1/delta)
average=ar(Emin)*(1-ar(delta/(kappa+delta))*(arb(18860)/ru)**ar(kappa))
require('switch beyond target',ru>18860,ru)
require('full fallback average',average>ar('0.79303'),average)
for rr in read('source/outer.json')['rows']:
 for target,tr in rr['targets'].items():require(rr['candidate']+' target '+target,arb(tr['K'])<ar('0.785064'))
for rr in read('source/average.json')['rows']:
 for target,tr in rr['targets'].items():require(rr['candidate']+' outer fallback '+target,arb(tr['averaged_floor_at_beta'])>ar('0.79303648'))
for literal in ['c[h] = 0','if K = 0 the majorant is linear','for r >= max(L0, 5) and at least H lambda for L0 <= r < 5','No exact solution near any candidate has been shown to exist.']:
 require('retained hypothesis '+literal,literal in ' '.join(text.split()))
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'table':table,'table_rows':len(table),'word_change_blocks':len(changes),'dyadic_cells':cells,'lambda':lam.str(100),'N1_projection':N1.str(100),'common_average':average.str(100),'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'source_sha256':sha(B/'source/THEORY_FINAL.md'),'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED changed conditional mathematics and seven-cell consequence; REFUTED exact lambda decimal and upward-rounded two-projection inference; scope repairs in proof'}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks,',len(table),'table rows, 7 cells,',result['utc'],result['elapsed_s'])
