"""Result232: own finite-data comparison and static method-description audit."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,math,re
R=Path('research/sec410_resolved_map_text');V=R/'verification';P=Path('research/hydrostatic_resolved_map_audit');PV=P/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();flat=lambda t:' '.join(t.split());checks=[]
def check(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
for row in json.loads((V/'INPUTS.json').read_text())['files']:check('frozen '+Path(row['frozen']).name,sha(row['frozen'])==row['sha256'])
s=json.loads((PV/'SUMMARY.json').read_text());check('independent227 gate278',s['status']=='PASS'and s['count']==278 and all(c['passed']for c in s['checks']));check('summary driverhash',s['driver_sha256']==sha('independent_code/summarize_hydrostatic_resolved_maps.py'));check('summary proofhash',s['proof_sha256']==sha(P/'SUMMARY_PROOF.md'));check('pipelinehash',s['pipeline_sha256']==sha(PV/'PIPELINE.json'))
old=flat((V/'add.txt').read_text());new=flat((R/'RECOMMENDED_ADD.txt').read_text())
vals={key:[x[key]for x in s['states'][:3]]for key in ['E','b','delta']}
vals['max']=[x['final_regions']['extent10000']['R_Nf']['R_Nf']for x in s['states'][:3]]
for label,field,digits,expected in [('E','E',3,['+0.673','-0.406','-1.395']),('B','b',3,['-4.770','-4.867','-4.948']),('delta','delta',None,['-1.64e-4','-1.81e-5','+1.29e-4']),('sampled maximum','max',None,['7.65e-2','1.89e-3','1.54e-2'])]:
 for k,(x,t)in enumerate(zip(vals[field],expected)):
  if digits is not None:check(label+' rounding '+str(k),f'{x:+.{digits}f}'==t)
  else:check(label+' rounding '+str(k),abs(x-float(t))<=0.005*10**math.floor(math.log10(abs(x))),dict(exact=x,printed=t))
  check(label+' literal '+str(k),t in old and t in new)
for N in [64,96,128]:
 tag=f'hsG_c3.0_N{N}_log';state=next(x for x in s['states']if x['tag']==tag);log=(V/(tag+'.log')).read_text();first=log.splitlines()[0];kw=ast.literal_eval(first[first.index('{'):]);last=json.loads(next(z[len('# RESULT '):]for z in log.splitlines()if z.startswith('# RESULT ')))
 for key,value in [('c','3.0'),('hstep','r'),('inner','log'),('maxit','60')]:check(tag+' parameter '+key,kw[key]==value)
 check(tag+' sizes and simple start',last['N']==N and last['M']==N//4 and last['start']=='simple'and not last['fine'])
 its=re.findall(r'it (\d+): line search failed',log);check(tag+' stall before cap',len(its)==1 and int(its[0])<60,its)
 check(tag+' coefficient log consistency',abs(last['E']-state['E'])<1e-9 and abs(last['B']-state['b'])<1e-9)
 check(tag+' panel count',last['n_in_effective']in [200,216,224]and(last['n_in_effective']-24)%8==0)
 raw=json.loads((PV/(tag+'.json')).read_text());lastlevel=raw['levels'][-1]
 points=lastlevel['points']
 check(tag+'774 independent points',len(points)==774)
 peak=max(r['R_Nf']for r in points if r['R_Nf']is not None);check(tag+'fullraw sample maximum',peak==state['final_regions']['extent10000']['R_Nf']['R_Nf'])
 check(tag+'axis included',any(r['x']==0 and r['y']>0 for r in points))
sc=(V/'PRODUCER_STATIC_hs_solve.py').read_text()
for clause in ["n0=24, per_decade=4, ngl=8",'n_pan = int(math.ceil(per_decade * np.log10(max(y.max(), 10.0))))','edges = ly[:, None] * np.linspace(0, 1, n_pan + 1)[None, :]','self.T_t = y[:, None] + Lt[:, None] * s[None, :]','np.hypot(Xq, Tq) if hstep == \'r\'']:
 check('static implementation '+clause,clause in sc)
for ym in [2,100,1e7]:
 n=math.ceil(4*math.log10(max(ym,10)))
 for y in [math.sqrt(ym),ym]:check('minimum panels '+str((ym,y)),n/math.log10(y)>=4-1e-14)
check('counterexample to fixed count per decade',math.ceil(4*6)/math.log10(100)!=math.ceil(4*6)/math.log10(1e6))
for root,file,tag,val in [('hydrostatic_extended_state_audit','SUMMARY.json','hsE_c3.0_N64_hr','+0.59'),('hydrostatic_state_audit','ALL21_SUMMARY.json','hsA_c3.0_N96','-0.41')]:
 g=json.loads((Path('research')/root/'verification'/file).read_text());r=next(x for x in g['states']if x['tag']==tag);x=float(r['exact']['E']);check('old map '+tag,f'{x:+.2f}'==val and val in new)
check('unsettled finite E spread',max(vals['E'])-min(vals['E'])>2)
check('nonmonotone sampled residual',vals['max'][0]>vals['max'][1]and vals['max'][2]>vals['max'][1])
check('geometric-wording repaired','resolves all scales'not in new and'fixed number of points per decade'not in new and'at least four panels per decade'in new)
check('finite conclusion','these runs still stall and their coefficients have not settled after this quadrature change.'in new)
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,values=vals,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),original_sha256=sha(V/'add.txt'),recommended_sha256=sha(R/'RECOMMENDED_ADD.txt'),verdict='Original numeric content CONFIRMED; literal fixed-points-per-decade claim REFUTED; recommended wording checked. No full-plane endpoint.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([c for c in checks if not c['passed']])
if out['status']!='PASS':raise SystemExit(1)
